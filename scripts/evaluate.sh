# use system arg as predictions path
predictions_path=$1
dataset_name=$2
benchmark=$3
max_workers=1
uv run scripts/evaluate.py --benchmark $benchmark --predictions $predictions_path --dataset $dataset_name --max-workers $max_workers