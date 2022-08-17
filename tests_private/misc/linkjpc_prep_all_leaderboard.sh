#!/bin/sh -x
now=`date +%Y%m%d%H%M%S`
script="./linkjpc_prep.py"
common_data_org_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/"
common_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/common/"
tmp_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/leaderboard/"
in_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/leaderboard/ene_annotation/"
in_for_view_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/leaderboard/ene_annotation/for_view/"

sample_gold_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/link_annotation/"
#gold_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/link_annotation/"
out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/leaderboard_out/20211023/"
eval_target="./eval_target_sample.txt"
out_dir_tmp_base="/Users/masako/tmp/leaderboard/20211022/"
#out_dir_tmp_base2="/Users/masako/tmp/sample/sampletest/"
title_file="title.txt"

setting_dir="${out_dir_base}setting/"
# matching
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_tmp_base --pre_matching mint --title_matching_mint trim --char_match_min 0.2
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_tmp_base --pre_matching mint --title_matching_mint full --char_match_min 0.2
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_tmp_base --pre_matching tinm --title_matching_tinm trim --char_match_min 0.2
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_tmp_base --pre_matching tinm --title_matching_tinm full --char_match_min 0.2

# backlink
# title
#cat ${in_for_view_dir}*.json | grep '\"title\"' |  awk 'begin{FS=": "}{print $2}' | perl -pe 's/^"//' | perl -pe 's/\",//'| sort | uniq > ${tmp_data_dir}${title_file}
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_base --gen_back_link_full
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_base --gen_back_link_light

# htmltag
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_base --gen_html
