#!/bin/bash

# EXAMPLES: linkjpc_prep

## !! PLEASE MODIFY THE DIRECTORIES BELOW !!
script="./linkjpc/linkjpc_prep.py"
in_dir="XXX"
tmp_data_dir="XXX/"
common_data_dir="XXX/"
sample_gold_dir="XXX"      # link_annotationのparent directory
sample_input_dir="XXX"     # ene_annotationのparent directory
#########################################################################################

python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_change_wikipedia_info
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --conv_sample_json_pageid
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_target_attr
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_enew_rev_year
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_title2pid
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_incoming_link
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_redirect
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_title2pid_ext
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_lang_link
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --pre_matching mint --conv_year --title_matching_mint full --char_match_min 0.5
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --pre_matching mint --conv_year --title_matching_mint trim --char_match_min 0.5
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --pre_matching tinm --conv_year --title_matching_tinm full --char_match_min 0.5
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --pre_matching tinm --conv_year --title_matching_tinm trim --char_match_min 0.5
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_back_link
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_sample_gold_tsv --conv_year
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_link_prob --conv_year
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_slink --conv_year
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_linkable  --conv_year
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_attr_rng --conv_year
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_common_html_conv_year
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_link_dist --conv_year
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_html_conv_year



