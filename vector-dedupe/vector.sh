#!/bin/bash
MY_DIR="$(dirname "$(realpath "$0")")"
cd $MY_DIR
# rm $MY_DIR/data/file/checkpoints.json
python3 /home/d/lou-dev/vector/vector-dedupe/generate.py $ & GENID=$(echo $!)
export MY_DIR=$MY_DIR
valgrind --tool=massif /home/d/lou-dev/vector/target/release/vector -w --config /home/d/lou-dev/vector/vector-dedupe/vector.yaml
kill -9 $GENID