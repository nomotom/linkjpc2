#!/bin/bash

base_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/"
sys_all_base_dir="${base_dir}test_out/exp/"
# sys_judged="${sys_all_base_dir}*/*_judge.tsv"
sys_all_judge_tp="${sys_all_base_dir}sys_all_judge_tp.tsv"
script="./anal/cat_judge.py"


cat ${sys_all_base_dir}*/*_judge.tsv | awk 'BEGIN{FS="\t"}$14 ~ /TP/{print}' > ${sys_all_judge_tp}
python ${script}