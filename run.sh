#!/bin/bash
echo "beginning preprocessing"
python3 data_combiner.py
python3 reorder.py
python3 features_and_labels.py
echo "preprocessing done"
echo "beginning evaluation"
python3 testharness.py
python3 classification.py
echo "evaluation concluded"
exit 0
