#!/usr/bin/env python3
"""Classify and optionally analyze the last message from each ChatAnthropic run."""

from __future__ import annotations

import argparse
import json
import os
import warnings
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core._api import LangChainBetaWarning
from langchain_core.load import load as lc_load
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage, message_to_dict


@dataclass
class ChatRun:
    index: int
    run_id: str | None
    model: str | None
    serialized_messages: list[dict[str, Any]]


def _walk_chat_nodes(obj: Any) -> Iterable[dict[str, Any]]:
    if isinstance(obj, dict):
        if obj.get("name") == "ChatAnthropic":
            yield obj
        for value in obj.values():
            yield from _walk_chat_nodes(value)
    elif isinstance(obj, list):
        for item in obj:
            yield from _walk_chat_nodes(item)


def _extract_serialized_messages(node: dict[str, Any]) -> list[dict[str, Any]]:
    raw_messages = ((node.get("inputs") or {}).get("messages")) or []
    if isinstance(raw_messages, list) and len(raw_messages) == 1 and isinstance(raw_messages[0], list):
        raw_messages = raw_messages[0]
    if not isinstance(raw_messages, list):
        raise ValueError(f"Unexpected messages payload type: {type(raw_messages).__name__}")
    if not all(isinstance(item, dict) for item in raw_messages):
        raise ValueError("messages should be list[dict]")
    return raw_messages


def _collect_chat_runs(trace_obj: Any) -> list[ChatRun]:
    runs: list[ChatRun] = []
    for idx, node in enumerate(_walk_chat_nodes(trace_obj), start=1):
        outputs = node.get("outputs") or {}
        llm_output = outputs.get("llm_output") or {}
        runs.append(
            ChatRun(
                index=idx,
                run_id=node.get("id"),
                model=llm_output.get("model_name") or llm_output.get("model"),
                serialized_messages=_extract_serialized_messages(node),
            )
        )
    return runs


def _restore_messages(serialized_messages: list[dict[str, Any]]) -> list[BaseMessage]:
    warnings.simplefilter("ignore", category=LangChainBetaWarning)
    restored: list[BaseMessage] = []
    for message_obj in serialized_messages:
        loaded = lc_load(message_obj)
        if not isinstance(loaded, BaseMessage):
            raise TypeError(f"Loaded object is not a BaseMessage: {type(loaded).__name__}")
        restored.append(loaded)
    return restored


def _build_llm(model: str, max_tokens: int) -> ChatAnthropic:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY is required")

    kwargs: dict[str, Any] = {
        "model": model,
        "api_key": api_key,
        "max_tokens": max_tokens,
        "max_retries": 3,
    }
    base_url = os.getenv("ANTHROPIC_BASE_URL")
    if base_url:
        kwargs["base_url"] = base_url
    return ChatAnthropic(**kwargs)


def _message_text(message: BaseMessage) -> str:
    content = message.content
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        text_parts: list[str] = []
        for item in content:
            if isinstance(item, str):
                text_parts.append(item)
            elif isinstance(item, dict):
                if item.get("type") == "text":
                    text_parts.append(str(item.get("text", "")))
                else:
                    text_parts.append(json.dumps(item, ensure_ascii=False))
            else:
                text_parts.append(str(item))
        return "\n".join(text_parts)
    return str(content)


def _extract_task_flag(classifier_output_text: str) -> bool:
    text = classifier_output_text.strip()
    try:
        parsed = json.loads(text)
        return isinstance(parsed, list) and any(isinstance(item, str) and item.lower() == "task" for item in parsed)
    except json.JSONDecodeError:
        return "task" in text.lower()


def _extract_claim_flag(classifier_output_text: str) -> bool:
    text = classifier_output_text.strip()
    try:
        parsed = json.loads(text)
        return isinstance(parsed, list) and any(isinstance(item, str) and item.lower() == "content" for item in parsed)
    except json.JSONDecodeError:
        return "content" in text.lower()


def _convert_string_to_dict(content: str) -> dict:
    """Convert a string to a dictionary. content: ```json {json_content}```
    """
    try:
        content = content.replace("```json", "").replace("```", "")
        content = content.strip()
        return json.loads(content)
    except json.JSONDecodeError:
        return content

def _convert_message_to_dict(message: dict) -> dict:
    """Convert a message to a dictionary.
    """
    message['data']['content'] = _convert_string_to_dict(message['data']['content'])
    return message

def analyze_trace(
    trace_path: Path,
    classifier_prompt_path: Path,
    task_analysis_prompt_path: Path,
    claim_analysis_prompt_path: Path,
    output_path: Path,
    override_model: str | None,
    max_tokens: int,
    max_runs: int | None,
    dry_run: bool,
) -> None:
    trace_obj = json.loads(trace_path.read_text(encoding="utf-8"))
    runs = _collect_chat_runs(trace_obj)
    if max_runs is not None:
        runs = runs[:max_runs]

    if not runs:
        print("No ChatAnthropic runs found.")
        return

    classifier_prompt = classifier_prompt_path.read_text(encoding="utf-8")
    task_analysis_prompt = task_analysis_prompt_path.read_text(encoding="utf-8")
    claim_analysis_prompt = claim_analysis_prompt_path.read_text(encoding="utf-8")
    print(f"Found {len(runs)} ChatAnthropic runs in {trace_path}")
    llm_cache: dict[str, ChatAnthropic] = {}
    records: list[dict[str, Any]] = []

    for run in runs:
        model = override_model or run.model
        if not model:
            raise RuntimeError(f"Run {run.index} has no model in trace output, and --model was not provided.")

        messages = _restore_messages(run.serialized_messages)
        print(f"\n=== Run {run.index} ===")
        print(f"run_id: {run.run_id}")
        print(f"model: {model}")
        print(f"message_count: {len(messages)}")

        record: dict[str, Any] = {
            "run_index": run.index,
            "run_id": run.run_id,
            "model": model,
            "input_last_message": None,
            "classifier_output": None,
            "task_analysis_output": None,
        }

        if not messages:
            records.append(record)
            continue

        last_message_text = _message_text(messages[-1]).strip()
        record["input_last_message"] = last_message_text

        if dry_run:
            record["dry_run"] = True
            records.append(record)
            continue

        if model not in llm_cache:
            llm_cache[model] = _build_llm(model=model, max_tokens=max_tokens)
        llm = llm_cache[model]

        classifier_response = llm.invoke(
            [
                SystemMessage(content=classifier_prompt),
                HumanMessage(content=last_message_text),
            ]
        )
        record["classifier_output"] = message_to_dict(classifier_response)
        record["classifier_output"] = _convert_message_to_dict(record["classifier_output"])
        classifier_output_text = _message_text(classifier_response)

        if _extract_task_flag(classifier_output_text):
            task_response = llm.invoke(
                [
                    SystemMessage(content=task_analysis_prompt),
                    HumanMessage(content=last_message_text),
                ]
            )
            record["task_analysis_output"] = message_to_dict(task_response)
            record["task_analysis_output"] = _convert_message_to_dict(record["task_analysis_output"])
        if _extract_claim_flag(classifier_output_text):
            claim_response = llm.invoke(
                [
                    SystemMessage(content=claim_analysis_prompt),
                    HumanMessage(content=last_message_text),
                ]
            )
            record["claim_analysis_output"] = message_to_dict(claim_response)
            record["claim_analysis_output"] = _convert_message_to_dict(record["claim_analysis_output"])
        records.append(record)
        print("classified and recorded.")

    output = {
        "trace_file": str(trace_path),
        "classifier_prompt_file": str(classifier_prompt_path),
        "task_analysis_prompt_file": str(task_analysis_prompt_path),
        "total_chat_runs": len(runs),
        "records": records,
    }
    output_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nSaved output JSON to: {output_path}")


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Classify the last message of each ChatAnthropic run and run task analysis when classifier output contains 'task'."
    )
    parser.add_argument(
        "--trace-file",
        type=Path,
        default=Path("src/workplace/memorysrc/project_traces_0e8eb6b4-d1b3-45b1-a009-b5de22cb7761.json"),
        help="Path to LangSmith trace JSON file.",
    )
    parser.add_argument(
        "--classifier-prompt-file",
        type=Path,
        default=Path("src/workplace/shared/memprompts/classifer.md"),
        help="Path to classifier system prompt.",
    )
    parser.add_argument(
        "--task-analysis-prompt-file",
        type=Path,
        default=Path("src/workplace/shared/memprompts/task_analysis.md"),
        help="Path to task analysis system prompt.",
    )
    parser.add_argument(
        "--claim-analysis-prompt-file",
        type=Path,
        default=Path("src/workplace/shared/memprompts/claim_analysis.md"),
        help="Path to claim analysis system prompt.",
    )
    parser.add_argument(
        "--output-file",
        type=Path,
        default=Path("src/workplace/memorysrc/classifier_task_analysis_outputs.json"),
        help="Path to output JSON file.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=None,
        help="Override model name. If omitted, use model from each ChatAnthropic run in trace.",
    )
    parser.add_argument("--max-tokens", type=int, default=4096, help="max_tokens used for ChatAnthropic calls.")
    parser.add_argument("--max-runs", type=int, default=None, help="Process first N ChatAnthropic runs only.")
    parser.add_argument("--dry-run", action="store_true", help="Only restore messages and save placeholders.")
    return parser.parse_args()


def main() -> None:
    load_dotenv()
    args = _parse_args()
    analyze_trace(
        trace_path=args.trace_file,
        classifier_prompt_path=args.classifier_prompt_file,
        task_analysis_prompt_path=args.task_analysis_prompt_file,
        claim_analysis_prompt_path=args.claim_analysis_prompt_file,
        output_path=args.output_file,
        override_model=args.model,
        max_tokens=args.max_tokens,
        max_runs=args.max_runs,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
