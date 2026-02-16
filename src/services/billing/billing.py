# Copyright (c) 2026 Yunjue Tech
# SPDX-License-Identifier: Apache-2.0
"""
Billing module for tracking LLM token usage and cost.

Usage:
    1. Create a BillingTracker and pass it via config callbacks:
        tracker = BillingTracker()
        config = {"callbacks": [tracker]}
        result = await graph.ainvoke(input, config=config)

    2. After execution, get usage summary:
        summary = tracker.get_summary()
        print(f"Total cost: ${summary.total_cost_usd:.4f}")
"""
from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.outputs import LLMResult

logger = logging.getLogger(__name__)

COSTS_FILENAME = "run_costs.json"

# Anthropic pricing per 1M tokens (input, output) - USD, as of 2025
# Source: https://docs.anthropic.com/en/docs/about-claude/pricing
DEFAULT_PRICING: Dict[str, tuple[float, float]] = {
    "claude-sonnet-4-5-20250929": (3.0, 15.0),
    "claude-haiku-4-20250929": (1.0, 5.0),
    "claude-3-5-sonnet-20241022": (3.0, 15.0),
    "claude-3-haiku-20240307": (0.25, 1.25),
    "claude-3-opus-20240229": (15.0, 75.0),
    "default": (3.0, 15.0),  # fallback for unknown models
}


@dataclass
class UsageRecord:
    """Single LLM call usage record."""

    input_tokens: int = 0
    output_tokens: int = 0
    model: str = ""
    invocation_id: str = ""

    @property
    def total_tokens(self) -> int:
        return self.input_tokens + self.output_tokens

    def cost_usd(self, pricing: Optional[Dict[str, tuple[float, float]]] = None) -> float:
        """Calculate cost in USD based on model pricing."""
        pricing = pricing or DEFAULT_PRICING
        key = self.model if self.model in pricing else "default"
        input_price, output_price = pricing[key]
        return (self.input_tokens / 1_000_000 * input_price) + (
            self.output_tokens / 1_000_000 * output_price
        )


@dataclass
class BillingSummary:
    """Aggregated billing summary for a task."""

    records: List[UsageRecord] = field(default_factory=list)
    total_input_tokens: int = 0
    total_output_tokens: int = 0
    total_cost_usd: float = 0.0

    def add_record(self, record: UsageRecord, pricing: Optional[Dict[str, tuple[float, float]]] = None):
        self.records.append(record)
        self.total_input_tokens += record.input_tokens
        self.total_output_tokens += record.output_tokens
        self.total_cost_usd += record.cost_usd(pricing)


class BillingTracker(BaseCallbackHandler):
    """
    LangChain callback handler that tracks LLM token usage and cost.

    Collects usage from on_llm_end and aggregates per run.
    """

    def __init__(self, pricing: Optional[Dict[str, tuple[float, float]]] = None):
        super().__init__()
        self._summary = BillingSummary()
        self._pricing = pricing or DEFAULT_PRICING

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        """Extract token usage from LLM response and record it."""
        for gen_list in response.generations:
            for gen in gen_list:
                message = getattr(gen, "message", None)
                if message is None:
                    continue
                record = self._extract_usage(message, kwargs)
                if record and (record.input_tokens > 0 or record.output_tokens > 0):
                    self._summary.add_record(record, self._pricing)
                    logger.debug(
                        f"Billing: +{record.input_tokens} in, +{record.output_tokens} out, "
                        f"model={record.model}, cost=${record.cost_usd(self._pricing):.6f}"
                    )

    def _extract_usage(self, message: Any, kwargs: Any) -> Optional[UsageRecord]:
        """Extract usage from AIMessage or similar."""
        usage = getattr(message, "usage_metadata", None) or {}
        if not usage and hasattr(message, "response_metadata"):
            usage = (message.response_metadata or {}).get("usage", {})
        if not usage and hasattr(message, "response_metadata"):
            usage = (message.response_metadata or {}).get("token_usage", {})

        if isinstance(usage, dict):
            input_tokens = usage.get("input_tokens", usage.get("input", 0))
            output_tokens = usage.get("output_tokens", usage.get("output", 0))
        else:
            input_tokens = getattr(usage, "input_tokens", 0) or 0
            output_tokens = getattr(usage, "output_tokens", 0) or 0

        model = ""
        if hasattr(message, "response_metadata") and message.response_metadata:
            model = (
                message.response_metadata.get("model_name")
                or message.response_metadata.get("model")
                or ""
            )

        invocation_id = str(kwargs.get("invocation_id", ""))

        return UsageRecord(
            input_tokens=int(input_tokens),
            output_tokens=int(output_tokens),
            model=model,
            invocation_id=invocation_id,
        )

    def get_summary(self) -> BillingSummary:
        """Return the aggregated usage summary."""
        return self._summary

    def reset(self) -> None:
        """Reset the tracker for a new run."""
        self._summary = BillingSummary()


def get_billing_config(tracker: Optional[BillingTracker] = None) -> Dict[str, Any]:
    """
    Build config dict with billing callback for graph.ainvoke.

    Usage:
        tracker = BillingTracker()
        config = {**base_config, **get_billing_config(tracker)}
        await graph.ainvoke(input, config=config)
        print(tracker.get_summary())
    """
    if tracker is None:
        return {}
    return {"callbacks": [tracker]}


def append_run_cost_to_file(
    run_dir: Path,
    task_id: str,
    summary: BillingSummary,
) -> None:
    """
    Append this run's cost to the cumulative costs file.
    Uses file locking for safe concurrent writes (multiprocessing).
    Amounts are accumulated; the file is never overwritten, only updated.
    """
    run_dir = Path(run_dir)
    costs_path = run_dir / COSTS_FILENAME

    run_entry = {
        "task_id": task_id,
        "cost_usd": round(summary.total_cost_usd, 6),
        "input_tokens": summary.total_input_tokens,
        "output_tokens": summary.total_output_tokens,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    run_dir.mkdir(parents=True, exist_ok=True)

    try:
        import fcntl
        has_fcntl = True
    except ImportError:
        has_fcntl = False

    def do_update():
        with open(costs_path, "a+", encoding="utf-8") as f:
            if has_fcntl:
                fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            try:
                f.seek(0)
                raw = f.read()
                if raw.strip():
                    try:
                        data = json.loads(raw)
                    except json.JSONDecodeError:
                        data = {"total_cost_usd": 0.0, "total_input_tokens": 0, "total_output_tokens": 0, "runs": []}
                else:
                    data = {"total_cost_usd": 0.0, "total_input_tokens": 0, "total_output_tokens": 0, "runs": []}

                data["total_cost_usd"] = round(data["total_cost_usd"] + summary.total_cost_usd, 6)
                data["total_input_tokens"] = data["total_input_tokens"] + summary.total_input_tokens
                data["total_output_tokens"] = data["total_output_tokens"] + summary.total_output_tokens
                data.setdefault("runs", []).append(run_entry)

                f.seek(0)
                f.truncate()
                json.dump(data, f, indent=2, ensure_ascii=False)
            finally:
                if has_fcntl:
                    fcntl.flock(f.fileno(), fcntl.LOCK_UN)

    # Retry on lock contention (another process writing)
    for attempt in range(5):
        try:
            do_update()
            logger.info(f"Billing: appended cost ${summary.total_cost_usd:.4f} to {costs_path}")
            return
        except (BlockingIOError, OSError) as e:
            if attempt < 4:
                import time
                time.sleep(0.2 * (attempt + 1))
            else:
                logger.warning(f"Failed to append cost to {costs_path}: {e}")
