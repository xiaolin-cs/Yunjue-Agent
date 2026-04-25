#!/usr/bin/env bash
# Run the ReAct + memory agent over a dataset and dump per-task predictions.
# Replaces the retired scripts/evolve.sh.
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  ./scripts/run.sh --dataset <DATASET> --run_name <RUN_NAME> \
      [--batch_size <N>] [--start <STEP>] [--train_steps <N>] [--timeout <SECONDS>]

Supported Datasets:
  HLE
  XBENCH-deepsearch, XBENCH-scienceqa, XBENCH-all
  DEEPSEARCHQA, DEEPRESEARCH, FINSEARCHCOMP, BROWSECOMP

Examples:
  ./scripts/run.sh --dataset HLE --run_name hle_run --batch_size 4 --start 10 --train_steps 20
  ./scripts/run.sh --dataset DEEPSEARCHQA --run_name dsqa_run --batch_size 5 --timeout 600
EOF
}

DATASET=""
RUN_NAME=""
BATCH_SIZE="5"
START_STEP="0"
TRAIN_STEPS=""
TIMEOUT=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dataset)
      DATASET="${2:-}"; shift 2;;
    --run_name)
      RUN_NAME="${2:-}"; shift 2;;
    --batch_size)
      BATCH_SIZE="${2:-}"; shift 2;;
    --start)
      START_STEP="${2:-}"; shift 2;;
    --train_steps)
      TRAIN_STEPS="${2:-}"; shift 2;;
    --timeout)
      TIMEOUT="${2:-}"; shift 2;;
    -h|--help)
      usage; exit 0;;
    *)
      echo "Unknown argument: $1" >&2
      usage
      exit 2
      ;;
  esac
done

if [[ -z "$DATASET" || -z "$RUN_NAME" ]]; then
  usage
  exit 2
fi

if ! [[ "$BATCH_SIZE" =~ ^[0-9]+$ ]] || [[ "$BATCH_SIZE" -le 0 ]]; then
  echo "Error: --batch_size must be a positive integer, got: $BATCH_SIZE" >&2
  exit 2
fi

if ! [[ "$START_STEP" =~ ^[0-9]+$ ]]; then
  echo "Error: --start must be a non-negative integer, got: $START_STEP" >&2
  exit 2
fi

if [[ -n "$TRAIN_STEPS" ]]; then
  if ! [[ "$TRAIN_STEPS" =~ ^[0-9]+$ ]] || [[ "$TRAIN_STEPS" -le 0 ]]; then
    echo "Error: --train_steps must be a positive integer, got: $TRAIN_STEPS" >&2
    exit 2
  fi
fi

if [[ -n "$TIMEOUT" ]]; then
  if ! [[ "$TIMEOUT" =~ ^[0-9]+$ ]] || [[ "$TIMEOUT" -le 0 ]]; then
    echo "Error: --timeout must be a positive integer (seconds), got: $TIMEOUT" >&2
    exit 2
  fi
fi

if ! command -v uv >/dev/null 2>&1; then
  echo "Error: uv not found in PATH" >&2
  exit 127
fi

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

LOG_DIR="output/${RUN_NAME}/logs"
mkdir -p "$LOG_DIR"

CMD=( uv run run_dataset.py
      --dataset "$DATASET"
      --run_name "$RUN_NAME"
      --batch_size "$BATCH_SIZE"
      --start "$START_STEP" )

if [[ -n "$TRAIN_STEPS" ]]; then
  CMD+=( --train_steps "$TRAIN_STEPS" )
fi

if [[ -n "$TIMEOUT" ]]; then
  CMD+=( --timeout "$TIMEOUT" )
fi

echo "Running: ${CMD[*]}"
"${CMD[@]}"

echo "Done. Predictions: output/${RUN_NAME}/predictions.jsonl"
echo "Logs:              ${LOG_DIR}"
