import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage, message_to_dict

logger = logging.getLogger(__name__)


class MemoryAnalyzer:
    def __init__(self, llm, query_id: Optional[str]) -> None:
        self._llm = llm
        self._query_id = query_id
        self._seq = 0
        self._classifier_prompt: str = ""
        self._task_analysis_prompt: str = ""
        self._claim_analysis_prompt: str = ""
        self._output_file: Optional[Path] = None
        self._init_paths_and_prompts()

    @staticmethod
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

    @staticmethod
    def _extract_task_flag(classifier_output_text: str) -> bool:
        text = classifier_output_text.strip()
        try:
            parsed = json.loads(text)
            return isinstance(parsed, list) and any(
                isinstance(item, str) and item.lower() == "task" for item in parsed
            )
        except json.JSONDecodeError:
            return "task" in text.lower()

    @staticmethod
    def _extract_claim_flag(classifier_output_text: str) -> bool:
        text = classifier_output_text.strip()
        try:
            parsed = json.loads(text)
            return isinstance(parsed, list) and any(
                isinstance(item, str) and item.lower() == "content" for item in parsed
            )
        except json.JSONDecodeError:
            return "content" in text.lower()

    @staticmethod
    def _convert_string_to_dict(content: str) -> dict | str:
        try:
            normalized = content.replace("```json", "").replace("```", "").strip()
            return json.loads(normalized)
        except json.JSONDecodeError:
            return content

    def _convert_message_to_dict(self, message: dict) -> dict:
        if (
            isinstance(message, dict)
            and isinstance(message.get("data"), dict)
            and isinstance(message["data"].get("content"), str)
        ):
            message["data"]["content"] = self._convert_string_to_dict(message["data"]["content"])
        return message

    def _init_paths_and_prompts(self) -> None:
        if not self._query_id:
            return
        try:
            base_dir = Path(__file__).resolve().parents[1] / "workplace" / "shared"
            prompt_dir = base_dir / "memprompts"
            self._classifier_prompt = (prompt_dir / "classifer.md").read_text(encoding="utf-8")
            self._task_analysis_prompt = (prompt_dir / "task_analysis.md").read_text(encoding="utf-8")
            self._claim_analysis_prompt = (prompt_dir / "claim_analysis.md").read_text(encoding="utf-8")
            output_dir = base_dir / self._query_id
            output_dir.mkdir(parents=True, exist_ok=True)
            self._output_file = output_dir / "memory_analysis.json"
        except Exception as e:
            logger.warning(f"Failed to initialize memory analysis for query_id={self._query_id}: {e}")
            self._output_file = None

    def _persist_memory_record(self, record: dict[str, Any]) -> None:
        if self._output_file is None:
            return
        records: list[dict[str, Any]] = []
        if self._output_file.exists():
            try:
                existing = json.loads(self._output_file.read_text(encoding="utf-8"))
                if isinstance(existing, dict) and isinstance(existing.get("records"), list):
                    records = existing["records"]
            except Exception:
                records = []
        records.append(record)
        payload = {
            "query_id": self._query_id,
            "total_records": len(records),
            "records": records,
        }
        self._output_file.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    def analyze_and_persist_call_input(
        self,
        state_messages: list[BaseMessage],
        tool_steps: int,
        retry_count: int,
    ) -> None:
        if not state_messages:
            return
        if not self._classifier_prompt or self._output_file is None:
            return
        try:
            input_message = state_messages[-1]
            input_text = self._message_text(input_message).strip()
            if not input_text:
                return
            classifier_response = self._llm.invoke(
                [SystemMessage(content=self._classifier_prompt), HumanMessage(content=input_text)]
            )
            classifier_output_text = self._message_text(classifier_response)
            record: dict[str, Any] = {
                "seq": self._seq + 1,
                "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                "query_id": self._query_id,
                "tool_steps": tool_steps,
                "retry_count": retry_count,
                "input_message_type": type(input_message).__name__,
                "input_last_message": input_text,
                "classifier_output": self._convert_message_to_dict(message_to_dict(classifier_response)),
                "task_analysis_output": None,
                "claim_analysis_output": None,
            }
            if self._extract_task_flag(classifier_output_text):
                task_response = self._llm.invoke(
                    [SystemMessage(content=self._task_analysis_prompt), HumanMessage(content=input_text)]
                )
                record["task_analysis_output"] = self._convert_message_to_dict(message_to_dict(task_response))
            if self._extract_claim_flag(classifier_output_text):
                claim_response = self._llm.invoke(
                    [SystemMessage(content=self._claim_analysis_prompt), HumanMessage(content=input_text)]
                )
                record["claim_analysis_output"] = self._convert_message_to_dict(message_to_dict(claim_response))
            self._seq += 1
            self._persist_memory_record(record)
        except Exception as e:
            logger.warning(f"Memory analyze/persist skipped due to error: {e}")

