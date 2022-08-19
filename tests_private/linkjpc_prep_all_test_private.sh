#!/bin/bash

script="./linkjpc/linkjpc_prep.py"
# base_dir_ljp2021="/Users/masako/Documents/SHINRA/2021-LinkJP/"
base_dir_ljp2022="/Users/masako/Documents/SHINRA/2022-LinkJP/"
# base_data_dir_ljp2021="${base_dir_ljp2021}Download/"
base_data_dir_ljp2022="${base_dir_ljp2022}Download/"
#common_data_dir="${base_data_dir}ljc_data/common_test/"
## common_data_dir="${base_data_dir}ljc_data/common/"
#tmp_data_dir="${base_data_dir}ljc_data/test_test/"
## tmp_data_dir="${base_data_dir}ljc_data/test/"
#in_dir="${base_data_dir}linkjp-eval-211027/ene_annotation/"
#sample_gold_dir="${base_dir}Download/linkjp-sample-210428/link_annotation/"
## out_dir_base="${base_dir}test_out/anal_20211116/"

common_data_dir="${base_data_dir_ljp2022}ljc_data/common/"
tmp_data_dir="${base_data_dir_ljp2022}ljc_data/test/"
in_dir="${base_data_dir_ljp2022}leaderboard-link-ans-20220816/ene_annotation/"
# sample_gold_dir_ljp2021="${base_dir_ljp2021}Download/linkjp-sample-210428/link_annotation/"
sample_gold_dir_ljp2022="${base_dir_ljp2022}Download/ljc_data/train-link-20220712/link_annotation/"

sample_gold_dir="${sample_gold_dir_ljp2022}"
sample_input_dir="${base_dir_ljp2022}Download/ljc_data/train-link-20220712/ene_annotation/"

# skip: 20210819
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_redirect
# skip: 20210819
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_incoming_link

# 20210819 (結果は同じ)
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_title2pid_ext

#skip: 20210819
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_back_link

# 20210819 (必須)
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_common_html

# 20210819 (必須)
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_sample_gold_tsv
# 不具合　gen_common_htmlに戻る　g_cat_pid_titleのタイトルがおかしい  →　解決したかどうか不明

# 20210819
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_link_dist
# ↑　不具合あり　backlinkは使えない

# 20210819
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_link_prob

# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --pre_matching mint --title_matching_mint trim --char_match_min 0.1
# 20210819
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --pre_matching mint --title_matching_mint full --char_match_min 0.1
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --pre_matching tinm --title_matching_tinm trim --char_match_min 0.1
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --pre_matching tinm --title_matching_tinm full --char_match_min 0.1

# 20210819
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_slink
# 20210819
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_linkable


# gen_htmlの前に入力ファイルのhtmlファイルをいかにコピ＝する
# '/Users/masako/Documents/SHINRA/2022-LinkJP/Download/ljc_data/test/html/*/*.html'
# 20210819
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir --gen_html