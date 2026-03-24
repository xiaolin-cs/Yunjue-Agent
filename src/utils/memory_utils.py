import re
import unicodedata
import os
import tqdm
from math import sqrt
from typing import Any, Dict, List, Optional, Tuple

_EMBEDDING_MODEL_CACHE: Dict[Tuple[str, str], Tuple[Any, Any]] = {}

# =========================
# Main entry
# =========================
def normalize_text(text: str) -> str:
    if text is None:
        return ""
    
    text = text.strip()
    
    # 1. Unicode normalization (full-width/half-width统一)
    text = unicodedata.normalize("NFKC", text)
    
    # 2. Convert to lowercase (only for English)
    text = text.lower()
    
    # 3. Unify punctuation
    text = normalize_punctuation(text)
    
    # 4. Normalize whitespace
    text = normalize_whitespace(text)
    
    # 5. Normalize numbers/time (lightweight, without semantic damage)
    text = normalize_numbers(text)
    
    # 6. Optional: English contractions processing
    text = normalize_english_contractions(text)
    
    return text


# =========================
# Submodules
# =========================

def normalize_punctuation(text: str) -> str:
    """Unify Chinese and English punctuation"""
    mapping = {
        "，": ",",
        "。": ".",
        "！": "!",
        "？": "?",
        "：": ":",
        "；": ";",
        "（": "(",
        "）": ")",
        "【": "[",
        "】": "]",
        "“": "\"",
        "”": "\"",
        "‘": "'",
        "’": "'",
        "—": "-",
        "～": "~",
    }
    
    for k, v in mapping.items():
        text = text.replace(k, v)
    
    return text


def normalize_whitespace(text: str) -> str:
    """Compress extra spaces"""
    # Multiple spaces → single space
    text = re.sub(r"\s+", " ", text)
    
    # Remove spaces before punctuation
    text = re.sub(r"\s+([,.!?;:])", r"\1", text)
    
    return text.strip()


def normalize_numbers(text: str) -> str:
    """
    Light number normalization (without changing semantics)
    - Unify 03 → 3
    - Do not convert Chinese numbers (to avoid accidental damage)
    """
    # Remove leading 0
    text = re.sub(r"\b0+(\d+)\b", r"\1", text)
    
    return text


def normalize_english_contractions(text: str) -> str:
    """Common English contractions (optional)"""
    contractions = {
        "can't": "can not",
        "won't": "will not",
        "n't": " not",
        "'re": " are",
        "'s": " is",
        "'d": " would",
        "'ll": " will",
        "'ve": " have"
    }
    
    for k, v in contractions.items():
        text = text.replace(k, v)
    
    return text


def get_qwen3_embeddings(
    texts: List[str],
    model: str = "Qwen3-Embedding-8B",
    batch_size: int = 16,
) -> List[List[float]]:
    """Get embeddings for normalized texts with local Qwen3 model via transformers."""
    if not texts:
        return []

    try:
        import torch  # type: ignore[reportMissingImports]
        from transformers import AutoModel, AutoTokenizer  # type: ignore[reportMissingImports]
    except Exception as e:
        raise RuntimeError(
            "transformers and torch are required for local Qwen3 embeddings."
        ) from e

    normalized_texts = [normalize_text(text) for text in texts]
    hf_model_id = "Qwen/Qwen3-Embedding-8B" if model == "Qwen3-Embedding-8B" else model
    cache_dir: Optional[str] = os.getenv("QWEN_EMBEDDING_CACHE_DIR")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    cache_key = (hf_model_id, device)

    if cache_key not in _EMBEDDING_MODEL_CACHE:
        tokenizer = AutoTokenizer.from_pretrained(hf_model_id, cache_dir=cache_dir)
        embed_model = AutoModel.from_pretrained(hf_model_id, cache_dir=cache_dir)
        embed_model.eval()
        embed_model.to(device)
        _EMBEDDING_MODEL_CACHE[cache_key] = (tokenizer, embed_model)

    tokenizer, embed_model = _EMBEDDING_MODEL_CACHE[cache_key]
    embeddings: List[List[float]] = []

    with torch.no_grad():
        for i in tqdm.tqdm(range(0, len(normalized_texts), batch_size)):
            batch_texts = normalized_texts[i : i + batch_size]
            encoded = tokenizer(
                batch_texts,
                padding=True,
                truncation=True,
                max_length=512,
                return_tensors="pt",
            )
            encoded = {k: v.to(device) for k, v in encoded.items()}
            outputs = embed_model(**encoded)
            hidden_states = outputs.last_hidden_state  # [B, T, H]
            attention_mask = encoded["attention_mask"].unsqueeze(-1).float()  # [B, T, 1]
            pooled = (hidden_states * attention_mask).sum(dim=1) / attention_mask.sum(dim=1).clamp(min=1e-9)
            pooled = torch.nn.functional.normalize(pooled, p=2, dim=1)
            embeddings.extend(pooled.cpu().tolist())

    return embeddings


def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    if len(vec1) != len(vec2) or not vec1:
        return 0.0
    dot = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = sqrt(sum(a * a for a in vec1))
    norm2 = sqrt(sum(b * b for b in vec2))
    if norm1 == 0.0 or norm2 == 0.0:
        return 0.0
    return dot / (norm1 * norm2)


def deduplicate_texts_by_embedding_similarity(
    texts: List[str],
    high_similarity_threshold: float = 0.92,
    low_similarity_threshold: float = 0.82,
    model: str = "Qwen3-Embedding-8B",
) -> Dict[str, Any]:
    """
    Classify short texts by embedding similarity using two safety thresholds.

    - ``high_similarity_threshold``: very high similarity → treat as definite duplicate
      of an earlier text (same semantic cluster, canonical = earlier index).
    - ``low_similarity_threshold``: similarity in [low, high) → suspicious / needs a
      downstream agent; **all original texts are still returned**.

    ``duplicate_characteristic`` per item:
    - ``unique``: no earlier text within ``low_similarity_threshold``.
    - ``definite_duplicate``: best match among earlier indices ≥ high threshold.
    - ``suspicious_duplicate``: best earlier match ≥ low but < high (not upgraded to definite).

    Returns:
    {
      "texts": [...],  # all inputs, order preserved
      "embeddings": [...],
      "per_text": [
        {
          "index": int,
          "text": str,
          "duplicate_characteristic": "unique" | "definite_duplicate" | "suspicious_duplicate",
          "related_earlier_index": int | null,
          "max_similarity_to_earlier": float | null,
          "referenced_by_later_indices": [int, ...],
        },
        ...
      ],
      "definite_duplicate_pairs": [{"earlier_index": int, "later_index": int, "similarity": float}, ...],
      "suspicious_pairs_for_agent": [{"earlier_index": int, "later_index": int, "similarity": float}, ...],
      "definite_unique_indices": [...],  # indices that are not definite_duplicate (auto-dedup view)
      "high_similarity_threshold": float,
      "low_similarity_threshold": float,
    }
    """
    if low_similarity_threshold > high_similarity_threshold:
        raise ValueError(
            "low_similarity_threshold must be <= high_similarity_threshold "
            f"(got low={low_similarity_threshold}, high={high_similarity_threshold})."
        )

    if not texts:
        return {
            "texts": [],
            "embeddings": [],
            "per_text": [],
            "definite_duplicate_pairs": [],
            "suspicious_pairs_for_agent": [],
            "definite_unique_indices": [],
            "high_similarity_threshold": high_similarity_threshold,
            "low_similarity_threshold": low_similarity_threshold,
        }

    embeddings = get_qwen3_embeddings(texts, model=model)
    n = len(texts)

    per_text: List[Dict[str, Any]] = []
    definite_pairs: List[Dict[str, Any]] = []
    suspicious_pairs: List[Dict[str, Any]] = []

    for j in range(n):
        best_i: Optional[int] = None
        best_sim: float = -1.0
        for i in range(j):
            sim = cosine_similarity(embeddings[i], embeddings[j])
            if sim > best_sim:
                best_sim = sim
                best_i = i

        if best_i is None or best_sim < low_similarity_threshold:
            characteristic = "unique"
            related: Optional[int] = None
            max_sim_out: Optional[float] = None
        elif best_sim >= high_similarity_threshold:
            characteristic = "definite_duplicate"
            related = best_i
            max_sim_out = best_sim
            definite_pairs.append(
                {
                    "earlier_index": best_i,
                    "later_index": j,
                    "similarity": best_sim,
                }
            )
        else:
            characteristic = "suspicious_duplicate"
            related = best_i
            max_sim_out = best_sim
            suspicious_pairs.append(
                {
                    "earlier_index": best_i,
                    "later_index": j,
                    "similarity": best_sim,
                }
            )

        per_text.append(
            {
                "index": j,
                "text": texts[j],
                "duplicate_characteristic": characteristic,
                "related_earlier_index": related,
                "max_similarity_to_earlier": max_sim_out,
                "referenced_by_later_indices": [],
            }
        )

    # Back-references: who points to this index as the best earlier match?
    for j, entry in enumerate(per_text):
        rel = entry["related_earlier_index"]
        if rel is not None:
            per_text[rel]["referenced_by_later_indices"].append(j)

    definite_unique_indices = [
        entry["index"]
        for entry in per_text
        if entry["duplicate_characteristic"] not in ["definite_duplicate"]
    ]
    suspicious_duplicate_indices = [
        entry["index"]
        for entry in per_text
        if entry["duplicate_characteristic"] in ["suspicious_duplicate"]
    ]
    definite_duplicate_indices = [
        entry["index"]
        for entry in per_text
        if entry["duplicate_characteristic"] in ["definite_duplicate"]
    ]

    return {
        "texts": list(texts),
        "embeddings": embeddings,
        "per_text": per_text,
        "definite_duplicate_pairs": definite_pairs,
        "suspicious_pairs_for_agent": suspicious_pairs,
        "definite_unique_indices": definite_unique_indices,
        "suspicious_duplicate_indices": suspicious_duplicate_indices,
        "definite_duplicate_indices": definite_duplicate_indices,
        "high_similarity_threshold": high_similarity_threshold,
        "low_similarity_threshold": low_similarity_threshold,
    }