# Copyright (c) 2026 Yunjue Tech
# SPDX-License-Identifier: Apache-2.0
"""Run the ReAct + memory agent over a dataset and dump per-task predictions.

This is the successor to the retired ``evolve.py``. The tool-evolve/merge/cluster
pipeline has been removed; this script now only orchestrates batched task
execution through ``src.main.run_task`` and appends predictions to a JSONL file.

Usage example:
    uv run run_dataset.py \
        --dataset HLE \
        --run_name hle_run \
        --batch_size 5 \
        --timeout 600
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import multiprocessing
import shutil
import time
import traceback
from datetime import datetime
from pathlib import Path
from typing import Iterable

from langchain_core.tracers.langchain import wait_for_all_tracers

from dataloader import load_dataset
from src.main import run_task


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def run_task_process(
    query: str,
    run_dir: Path,
    task_id: str,
    timeout: int = 5400,
    exp_name: str = "test",
):
    """Wrapper to run the async task in a separate process with a timeout."""

    async def run_with_timeout():
        try:
            return await asyncio.wait_for(
                run_task(
                    query,
                    run_dir,
                    task_id=task_id,
                    exp_name=exp_name,
                ),
                timeout=timeout,
            )
        except asyncio.TimeoutError:
            logger.error(f"Task {task_id} timed out after {timeout} seconds")
            return ({"error": f"Timeout after {timeout} seconds", "task_id": task_id}, 0)

    return asyncio.run(run_with_timeout())


async def run(
    data_iter: Iterable[dict],
    train_steps: int,
    start: int,
    run_dir: Path,
    prediction_file: Path,
    timeout: int,
    exp_name: str = "test",
):
    manager = multiprocessing.Manager()
    step = 0
    total_queries = 0
    total_tool_call_cnt = 0

    try:
        for data in data_iter:
            data_items = data["data_items"]
            if step < start:
                step += 1
                total_queries += len(data_items)
                continue

            task_ids = [data_item["task_id"] for data_item in data_items]
            process_args = [
                (
                    data_item["query"],
                    run_dir,
                    data_item["task_id"],
                    timeout,
                    exp_name,
                )
                for data_item in data_items
            ]

            # Use multiprocessing to run tasks in parallel processes.
            # Per-task apply_async + polling lets us keep completed results even if some workers hang.
            with multiprocessing.Pool(processes=len(data_items)) as pool:
                async_jobs = [pool.apply_async(run_task_process, args) for args in process_args]
                deadline = time.time() + timeout + 60
                results = [None] * len(async_jobs)
                pending: set[int] = set(range(len(async_jobs)))

                while pending and time.time() < deadline:
                    done_now = []
                    for idx in list(pending):
                        if async_jobs[idx].ready():
                            try:
                                results[idx] = async_jobs[idx].get()
                            except Exception as e:
                                results[idx] = (
                                    {"error": str(e), "task_id": task_ids[idx]},
                                    0,
                                )
                            done_now.append(idx)
                    for idx in done_now:
                        pending.discard(idx)
                    if pending:
                        time.sleep(1)

                timed_out_task_ids: set[str] = set()
                for idx in pending:
                    results[idx] = (
                        {"error": f"Timeout after {timeout} seconds", "task_id": task_ids[idx]},
                        0,
                    )
                    timed_out_task_ids.add(task_ids[idx])

                if pending:
                    logger.error(
                        f"Batch {step} exceeded timeout ({timeout}s) in "
                        f"{len(pending)} worker(s); terminating pool"
                    )
                    pool.terminate()
                else:
                    pool.close()
                pool.join()

            # Also drop tools for tasks that timed out inside the worker.
            for idx, result in enumerate(results):
                payload = result[0] if isinstance(result, tuple) else None
                if isinstance(payload, dict):
                    err = payload.get("error", "")
                    if isinstance(err, str) and "Timeout" in err:
                        timed_out_task_ids.add(task_ids[idx])

            for task_id in timed_out_task_ids:
                private_tool_dir = Path(run_dir) / "private_dynamic_tools" / f"dynamic_tools_{task_id}"
                shutil.rmtree(private_tool_dir, ignore_errors=True)

            try:
                with open(prediction_file, "a", encoding="utf-8") as f:
                    for idx, result in enumerate(results):
                        payload = result[0] if isinstance(result, tuple) else result
                        record = {
                            "question_index": data_items[idx]["task_id"],
                            "question": data_items[idx]["query"],
                            "prediction": payload,
                        }
                        f.write(json.dumps(record, ensure_ascii=False) + "\n")

                new_tool_call_cnt = sum(
                    (result[1] if isinstance(result, tuple) else 0) or 0 for result in results
                )
                total_tool_call_cnt += new_tool_call_cnt
                logger.info(
                    f"Step: {step}, batch tool calls: {new_tool_call_cnt}, "
                    f"cumulative tool calls: {total_tool_call_cnt}"
                )
            except Exception as e:
                logger.error(f"Error writing predictions for step {step}: {e}")
                logger.error(f"Traceback:\n{traceback.format_exc()}")

            total_queries += len(data_items)
            wait_for_all_tracers()

            step += 1
            if step >= train_steps + start:
                break
    finally:
        manager.shutdown()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run dataset tasks through the ReAct agent")
    parser.add_argument("--batch_size", type=int, default=5, help="Batch size")
    parser.add_argument(
        "--dataset",
        type=str,
        default="DEEPSEARCHQA",
        help=(
            "Dataset name "
            "(supported: 'HLE', 'XBENCH-deepsearch', 'XBENCH-scienceqa', "
            "'XBENCH-all', 'DEEPSEARCHQA', 'DEEPRESEARCH', 'FINSEARCHCOMP')"
        ),
    )
    parser.add_argument(
        "--train_steps",
        type=int,
        default=100000,
        help="Number of batches to process (default 100000 to run all data)",
    )
    parser.add_argument("--start", type=int, default=0, help="Start from the n-th batch")
    parser.add_argument("--run_name", type=str, default="test", help="Run name")
    parser.add_argument(
        "--timeout",
        type=int,
        default=9000,
        help="Timeout in seconds for each query execution",
    )

    args = parser.parse_args()

    data_file = Path(args.dataset).stem
    run_name = (
        args.run_name
        or f"{data_file}_steps{args.train_steps}_bs{args.batch_size}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    )

    run_dir = Path("output") / run_name
    run_dir.mkdir(parents=True, exist_ok=True)

    predictions_file = run_dir / "predictions.jsonl"

    data_iter = load_dataset(args.dataset, batch_size=args.batch_size)

    asyncio.run(
        run(
            data_iter,
            args.train_steps,
            args.start,
            run_dir,
            predictions_file,
            args.timeout,
            args.run_name,
        )
    )
