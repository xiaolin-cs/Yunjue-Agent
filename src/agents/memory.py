import json
import logging
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage, message_to_dict
from src.utils.memory_utils import deduplicate_texts_by_embedding_similarity

logger = logging.getLogger(__name__)

_CLAIMS_TEMPLATE_BLOCK = re.compile(r"\{\{#CLAIMS\}\}[\s\S]*?\{\{/CLAIMS\}\}")


class MemoryAnalyzer:
    def __init__(self, llm, query_id: Optional[str], exp_name: Optional[str] = None) -> None:
        self._llm = llm
        self._query_id = query_id
        self._exp_name = exp_name or "default"
        self._seq = 0
        self._classifier_prompt: str = ""
        self._task_analysis_prompt: str = ""
        self._claim_analysis_prompt: str = ""
        self._output_file: Optional[Path] = None
        self._tasks_file: Optional[Path] = None
        self._claims_file: Optional[Path] = None
        self._init_paths_and_prompts()
        self.dedup_params = {
            "tasks": {
                "high_similarity_threshold": 0.95,
                "low_similarity_threshold": 0.82,
                "payload_key": "tasks",
                "text_field": "description",
                "file": self._tasks_file,
            },
            "claims": {
                "high_similarity_threshold": 0.92,
                "low_similarity_threshold": 0.85,
                "payload_key": "claims",
                "text_field": "statement",
                "file": self._claims_file,
            },
        }

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
            prompt_dir = self._shared_root_dir() / "memprompts"
            self._classifier_prompt = (prompt_dir / "classifer.md").read_text(encoding="utf-8")
            self._task_analysis_prompt = (prompt_dir / "task_analysis.md").read_text(encoding="utf-8")
            self._claim_analysis_prompt = (prompt_dir / "claim_analysis.md").read_text(encoding="utf-8")
            output_dir = self._query_base_dir(self._query_id)
            output_dir.mkdir(parents=True, exist_ok=True)
            self._output_file = output_dir / "memory_analysis.json"
            self._tasks_file = output_dir / "TASKS.json"
            self._claims_file = output_dir / "CLAIMS.json"
        except Exception as e:
            logger.warning(f"Failed to initialize memory analysis for query_id={self._query_id}: {e}")
            self._output_file = None
            self._tasks_file = None
            self._claims_file = None

    @staticmethod
    def _shared_root_dir() -> Path:
        return Path(__file__).resolve().parents[1] / "workplace" / "shared"

    def _shared_dir(self) -> Path:
        return self._shared_root_dir() / self._exp_name

    def _query_base_dir(self, query_id: str) -> Path:
        return self._shared_dir() / query_id

    @staticmethod
    def _task_id_sort_key(task_id: str) -> tuple[int, int | str]:
        if isinstance(task_id, str) and task_id.upper().startswith("T"):
            suffix = task_id[1:].strip()
            try:
                return (0, int(suffix))
            except ValueError:
                return (1, task_id)
        return (1, str(task_id))

    @staticmethod
    def _format_claim_lines(claims: list[dict[str, Any]]) -> str:
        lines: list[str] = []
        for claim in claims:
            if not isinstance(claim, dict):
                continue
            cid = claim.get("claim_id", "")
            stmt = claim.get("statement", "")
            if not isinstance(stmt, str):
                stmt = str(stmt)
            lines.append(f"- {cid} | {stmt}")
        return "\n".join(lines)

    @staticmethod
    def _fill_prompt_template(template: str, task_objective: str, claims_block_body: str) -> str:
        text = template.replace("{{TASK_OBJECTIVE}}", task_objective)
        text = _CLAIMS_TEMPLATE_BLOCK.sub(claims_block_body.rstrip(), text)
        return text

    def _resolve_query_paths(
        self, query_id: Optional[str]
    ) -> tuple[Optional[str], Optional[Path], Optional[Path]]:
        qid = query_id if query_id is not None else self._query_id
        if not qid:
            return None, None, None
        base = self._query_base_dir(qid)
        return qid, base / "TASKS.json", base / "CLAIMS.json"

    @staticmethod
    def _pick_smallest_todo_task(tasks: list[dict[str, Any]]) -> Optional[dict[str, Any]]:
        todos = [
            t
            for t in tasks
            if isinstance(t, dict) and str(t.get("status", "")).strip().lower() == "todo"
        ]
        if not todos:
            return None
        return min(
            todos,
            key=lambda t: MemoryAnalyzer._task_id_sort_key(str(t.get("task_id", ""))),
        )

    def snapshot(
        self,
        task_objective: str = "",
        query_id: Optional[str] = None,
    ) -> Optional[str]:
        """
        Dispatch snapshot: if any task is ``todo``, run ``snapshot_execute`` with the
        smallest-``task_id`` todo task; otherwise if no task is ``todo``, run ``snapshot_plan``.
        Generates a snapshot as long as at least one of CLAIMS.json or TASKS.json exists.
        """
        _, tasks_path, claims_path = self._resolve_query_paths(query_id)
        if tasks_path is None or claims_path is None:
            return None

        claims_exists = claims_path.exists()
        tasks_exists = tasks_path.exists()  
        if not claims_exists and not tasks_exists:
            return None

        claims = self._read_items_file(claims_path, "claims") if claims_exists else []
        tasks = self._read_items_file(tasks_path, "tasks") if tasks_exists else []

        current = self._pick_smallest_todo_task(tasks)
        if current is not None:
            exec_template_path = self._shared_root_dir() / "memprompts" / "progress_execution.md"
            if not exec_template_path.exists():
                logger.warning("progress_execution.md not found at %s", exec_template_path)
                return None
            template = exec_template_path.read_text(encoding="utf-8")
            return self.snapshot_execute(task_objective, current, claims, template)

        else:
            plan_template_path = self._shared_root_dir() / "memprompts" / "progress_planning.md"
            if not plan_template_path.exists():
                logger.warning("progress_planning.md not found at %s", plan_template_path)
                return None
            template = plan_template_path.read_text(encoding="utf-8")
            return self.snapshot_plan(task_objective, claims, template)

    def write_snapshot_md(
        self,
        task_objective: str = "",
        query_id: Optional[str] = None,
    ) -> Optional[Path]:
        """
        Run ``snapshot()`` and overwrite ``shared/<run_name>/<query_id>/snapshot.md`` with the result.
        If snapshot generation fails (e.g. missing CLAIMS.json), the file is not written.
        """
        qid = query_id if query_id is not None else self._query_id
        # logger.info(f"(Test) write_snapshot_md: qid: {qid}")
        if not qid:
            return None
        try:
            content = self.snapshot(task_objective=task_objective, query_id=query_id)
            # logger.info(f"(Test) write_snapshot_md: content: {content}")
            if content is None:
                return None
            out_dir = self._query_base_dir(qid)
            out_dir.mkdir(parents=True, exist_ok=True)
            path = out_dir / "snapshot.md"
            path.write_text(content, encoding="utf-8")
            return path
        except Exception as e:
            logger.warning("write_snapshot_md failed for query_id=%s: %s", qid, e)
            return None

    def read_snapshot_md(self, query_id: Optional[str] = None) -> str:
        """
        Read ``shared/<run_name>/<query_id>/snapshot.md`` (UTF-8). Returns empty string if missing or unreadable.
        """
        qid = query_id if query_id is not None else self._query_id
        if not qid:
            return ""
        path = self._query_base_dir(qid) / "snapshot.md"
        if not path.exists():
            return ""
        try:
            return path.read_text(encoding="utf-8")
        except Exception as e:
            logger.warning("read_snapshot_md failed for query_id=%s: %s", qid, e)
            return ""

    def parse_instruction_task_id_from_snapshot_text(self, text: str) -> Optional[str]:
        """Parse ``**T1**`` from the ``# Current Instruction`` section of snapshot text."""
        if "# Current Instruction" not in text:
            return None
        idx = text.find("# Current Instruction")
        rest = text[idx + len("# Current Instruction") :]
        m = re.search(r"\*\*(T\d+)\*\*", rest)
        if m:
            return m.group(1)
        return None

    def mark_task_done_in_tasks_json(self, task_id: str) -> None:
        """Set ``status`` to ``done`` for ``task_id`` in ``shared/<run_name>/<query_id>/TASKS.json``."""
        _, tasks_path, _ = self._resolve_query_paths(self._query_id)
        if tasks_path is None or not tasks_path.exists():
            return
        try:
            data = json.loads(tasks_path.read_text(encoding="utf-8"))
            tasks = data.get("tasks")
            logger.info(f"mark_task_done_in_tasks_json: tasks: {tasks}")
            if not isinstance(tasks, list):
                return
            for t in tasks:
                if not isinstance(t, dict):
                    continue
                if str(t.get("task_id", "")).strip() == task_id:
                    logger.info(f"mark_task_done_in_tasks_json: t: {t}")
                    t["status"] = "done"
                    break
            tasks_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception as e:
            logger.warning("Failed to mark task %s done in %s: %s", task_id, tasks_path, e)

    def snapshot_execute(
        self,
        task_objective: str,
        current_task: dict[str, Any],
        claims: list[dict[str, Any]],
        template: str,
    ) -> str:
        """Fill ``progress_execution`` template: instruction from ``current_task``, claims list."""
        instruction = current_task.get("description", "")
        if not isinstance(instruction, str):
            instruction = str(instruction)
        tid = current_task.get("task_id", "")
        instruction_block = (
            f"**{tid}** — {instruction.strip()}" if tid else instruction.strip()
        )
        claims_body = self._format_claim_lines(claims)
        text = template.replace("{{TASK_OBJECTIVE}}", task_objective)
        text = text.replace("{{INSTRUCTION_OR_EMPTY}}", instruction_block)
        text = _CLAIMS_TEMPLATE_BLOCK.sub(claims_body.rstrip(), text)
        return text

    def snapshot_plan(
        self,
        task_objective: str,
        claims: list[dict[str, Any]],
        template: str,
    ) -> str:
        """Fill ``progress_planning`` template with ``TASK_OBJECTIVE`` and all claims."""
        claims_body = self._format_claim_lines(claims)
        return self._fill_prompt_template(template, task_objective, claims_body)

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

    @staticmethod
    def _extract_task_descriptions(record: dict[str, Any]) -> list[str]:
        output = record.get("task_analysis_output")
        if not isinstance(output, dict):
            return []
        data = output.get("data")
        if not isinstance(data, dict):
            return []
        content = data.get("content")
        if not isinstance(content, dict):
            return []
        tasks = content.get("tasks")
        if not isinstance(tasks, list):
            return []
        descriptions: list[str] = []
        for task in tasks:
            if not isinstance(task, dict):
                continue
            desc = task.get("description")
            if isinstance(desc, str):
                desc = desc.strip()
                if desc:
                    descriptions.append(desc)
        return descriptions

    @staticmethod
    def _extract_claim_statements(record: dict[str, Any]) -> list[str]:
        output = record.get("claim_analysis_output")
        if not isinstance(output, dict):
            return []
        data = output.get("data")
        if not isinstance(data, dict):
            return []
        content = data.get("content")
        if not isinstance(content, dict):
            return []
        claims = content.get("claims")
        if not isinstance(claims, list):
            return []
        statements: list[str] = []
        for claim in claims:
            if not isinstance(claim, dict):
                continue
            stmt = claim.get("statement")
            if isinstance(stmt, str):
                stmt = stmt.strip()
                if stmt:
                    statements.append(stmt)
        return statements

    @staticmethod
    def _extract_items_from_output(output: dict[str, Any], payload_key: str) -> list[dict[str, Any]]:
        if not isinstance(output, dict):
            return []
        data = output.get("data")
        if not isinstance(data, dict):
            return []
        content = data.get("content")
        if not isinstance(content, dict):
            return []
        items = content.get(payload_key)
        if not isinstance(items, list):
            return []
        return [item for item in items if isinstance(item, dict)]

    @staticmethod
    def _dedup_items_by_text_field(
        existing_items: list[dict[str, Any]],
        new_items: list[dict[str, Any]],
        text_field: str,
        dedup_params: dict[str, Any],
    ) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
        combined = existing_items + new_items
        texts = []
        for item in combined:
            value = item.get(text_field, "")
            texts.append(value.strip() if isinstance(value, str) else "")
        if not combined:
            return [], []
        dedup_result = deduplicate_texts_by_embedding_similarity(texts, **dedup_params)
        keep_indices = set(dedup_result.get("definite_unique_indices", []))
        deduped_combined = [item for idx, item in enumerate(combined) if idx in keep_indices]
        base_idx = len(existing_items)
        deduped_new = [
            item for idx, item in enumerate(combined) if idx in keep_indices and idx >= base_idx
        ]
        return deduped_combined, deduped_new

    @staticmethod
    def _read_items_file(path: Path, key: str) -> list[dict[str, Any]]:
        if not path.exists():
            return []
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
            items = payload.get(key, [])
            if isinstance(items, list):
                return [item for item in items if isinstance(item, dict)]
        except Exception:
            return []
        return []

    @staticmethod
    def _write_items_file(path: Path, key: str, items: list[dict[str, Any]]) -> None:
        payload = {key: items}
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    @staticmethod
    def _renumber_tasks_in_place(items: list[dict[str, Any]]) -> None:
        """Assign task_id T1..Tn and remap dependencies to new ids."""
        old_ids: list[str] = []
        for item in items:
            oid = item.get("task_id")
            old_ids.append(oid.strip() if isinstance(oid, str) else "")
        # First occurrence wins when multiple rows shared the same LLM task_id.
        old_id_to_new: dict[str, str] = {}
        for j, oid in enumerate(old_ids):
            if oid and oid not in old_id_to_new:
                old_id_to_new[oid] = f"T{j + 1}"
        for i, item in enumerate(items):
            item["task_id"] = f"T{i + 1}"
            deps = item.get("dependencies")
            if not isinstance(deps, list):
                continue
            new_deps: list[str] = []
            for d in deps:
                if isinstance(d, str):
                    key = d.strip()
                    new_deps.append(old_id_to_new.get(key, d))
            item["dependencies"] = new_deps

    @staticmethod
    def _renumber_claims_in_place(items: list[dict[str, Any]]) -> None:
        for i, item in enumerate(items):
            item["claim_id"] = f"C{i + 1}"

    def _deduplicate_and_persist(self, output: dict[str, Any], target: str) -> dict[str, Any]:
        if target not in ("tasks", "claims"):
            raise ValueError(f"target must be 'tasks' or 'claims', got: {target}")

        config = self.dedup_params.get(target, {})
        target_file = config.get("file")
        payload_key = config.get("payload_key", target)
        text_field = config.get("text_field")
        if target_file is None or not text_field:
            return output

        current_items = self._extract_items_from_output(output, payload_key)
        if not current_items:
            return output

        existing_items = self._read_items_file(target_file, payload_key)
        dedup_settings = {
            k: v
            for k, v in config.items()
            if k in ("high_similarity_threshold", "low_similarity_threshold", "model")
        }
        deduped_all_items, deduped_new_items = self._dedup_items_by_text_field(
            existing_items,
            current_items,
            text_field,
            dedup_settings,
        )
        new_item_ids = {id(item) for item in deduped_new_items}
        if target == "tasks":
            self._renumber_tasks_in_place(deduped_all_items)
        else:
            self._renumber_claims_in_place(deduped_all_items)
        deduped_new_items = [item for item in deduped_all_items if id(item) in new_item_ids]
        self._write_items_file(target_file, payload_key, deduped_all_items)
        if (
            isinstance(output.get("data"), dict)
            and isinstance(output["data"].get("content"), dict)
        ):
            output["data"]["content"][payload_key] = deduped_new_items
        return output

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
                task_output = self._convert_message_to_dict(message_to_dict(task_response))
                record["task_analysis_output"] = self._deduplicate_and_persist(task_output, "tasks")
            if self._extract_claim_flag(classifier_output_text):
                claim_response = self._llm.invoke(
                    [SystemMessage(content=self._claim_analysis_prompt), HumanMessage(content=input_text)]
                )
                claim_output = self._convert_message_to_dict(message_to_dict(claim_response))
                record["claim_analysis_output"] = self._deduplicate_and_persist(claim_output, "claims")
            self._seq += 1
            self._persist_memory_record(record)
        except Exception as e:
            logger.warning(f"Memory analyze/persist skipped due to error: {e}")

