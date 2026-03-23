import re
import unicodedata
import os
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
    
    # 1. Unicode标准化（全角/半角统一）
    text = unicodedata.normalize("NFKC", text)
    
    # 2. 转小写（仅对英文有效）
    text = text.lower()
    
    # 3. 标点统一
    text = normalize_punctuation(text)
    
    # 4. 空白规范化
    text = normalize_whitespace(text)
    
    # 5. 数字/时间规范化（轻量，不破坏语义）
    text = normalize_numbers(text)
    
    # 6. 可选：英文缩写处理
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
    # 多空格 → 单空格
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
        for i in range(0, len(normalized_texts), batch_size):
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
    similarity_threshold: float = 0.92,
    model: str = "Qwen3-Embedding-8B",
) -> Dict[str, Any]:
    """
    Deduplicate semantically similar short texts using embeddings.

    Returns:
    {
      "unique_texts": [...],
      "unique_indices": [...],
      "duplicate_groups": [{"kept_index": int, "duplicate_indices": [...], "similarities": [...]}],
      "embeddings": [...]
    }
    """
    if not texts:
        return {
            "unique_texts": [],
            "unique_indices": [],
            "duplicate_groups": [],
            "embeddings": [],
        }

    embeddings = get_qwen3_embeddings(texts, model=model)
    kept_indices: List[int] = []
    duplicate_groups: List[Dict[str, Any]] = []

    # Greedy dedup: keep earliest sentence in each semantic cluster.
    for idx, emb in enumerate(embeddings):
        matched_group = None
        for group in duplicate_groups:
            kept_idx = group["kept_index"]
            sim = cosine_similarity(embeddings[kept_idx], emb)
            if sim >= similarity_threshold:
                matched_group = (group, sim)
                break

        if matched_group is None:
            kept_indices.append(idx)
            duplicate_groups.append(
                {
                    "kept_index": idx,
                    "duplicate_indices": [],
                    "similarities": [],
                }
            )
        else:
            group, sim = matched_group
            group["duplicate_indices"].append(idx)
            group["similarities"].append(sim)

    unique_texts = [texts[i] for i in kept_indices]
    return {
        "unique_texts": unique_texts,
        "unique_indices": kept_indices,
        "duplicate_groups": duplicate_groups,
        "embeddings": embeddings,
    }