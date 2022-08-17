#!/bin/sh -x
now=`date +%Y%m%d%H%M%S`
script="./linkjpc_prep.py"
common_data_org_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/"
common_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/common/"
tmp_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/sample/"
in_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/ene_annotation/"
#sample gold dir (for generating selflink info)
sample_gold_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/link_annotation/"
gold_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/link_annotation/"
out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210921/"
eval_target="./eval_target_sample.txt"
out_dir_tmp_base="/Users/masako/tmp/sample/20210921/"


setting_dir="${out_dir_base}setting/"

python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_tmp_base --gen_back_link_full
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_tmp_base --gen_back_link_light

