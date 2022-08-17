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
out_dir_tmp_base="/Users/masako/tmp/sample/20211030/pre/"
#out_dir_tmp_base2="/Users/masako/tmp/sample/sampletest/"

setting_dir="${out_dir_base}setting/"

python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_tmp_base --gen_html


## 2021/10/20
#python ./linkjpc_prep_org.py $common_data_dir $tmp_data_dir $out_dir_tmp_base $in_dir $out_dir_tmp_base  --gen_html
#
## 2021/10/20
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_tmp_base --pre_matching mint --title_matching_mint trim --char_match_min 0.1
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_tmp_base --pre_matching mint --title_matching_mint full --char_match_min 0.1
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_tmp_base --pre_matching tinm --title_matching_tinm trim --char_match_min 0.1
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_tmp_base --pre_matching tinm --title_matching_tinm full --char_match_min 0.1

#2021/9/19
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_tmp_base  --gen_html
#2021/9/20
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_tmp_base  --gen_slink
#2021/9/20
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_base  --gen_back_link

#2021/9/22
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_tmp_base  --gen_title2pid

#done
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_tmp_base --pre_matching mint --title_matching trim --char_match_min 0.2
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_tmp_base --pre_matching mint --title_matching full --char_match_min 0.2
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_tmp_base --pre_matching tinm --title_matching trim --char_match_min 0.2
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_tmp_base --pre_matching tinm --title_matching full --char_match_min 0.2


#done
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_base  --gen_back_link_full

#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_base  --gen_link_prob




#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $out_dir_base  --gen_back_link_light


#redirect_nodis
#2021/9/14 9:39
#python ./linkjpc_prep_old.py ${common_data_dir} ${tmp_data_dir} ${in_dir} ${out_dir_tmp_base} ${out_dir_tmp_base} --redirect
#python ./linkjpc_prep_old.py ${common_data_dir} ${tmp_data_dir} ${in_dir} ${out_dir_tmp_base} ${out_dir_tmp_base} --gen_title2pid
#python ./linkjpc_prep_old.py ~/Documents/SHINRA/2021-LinkJP/Download/ ~/Documents/SHINRA/2021-LinkJP/Download/html/ ~/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/ene_annotation/ ~/tmp/ ~/tmp/--pre_matching --char_match_min 0.2 --char_match_cand_num_max 1000
#python ./linkjpc_prep_old.py ~/Documents/SHINRA/2021-LinkJP/Download/ ~/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/ene_annotation/ ~/Documents/SHINRA/2021-LinkJP/Download/ ~/Documents/SHINRA/2021-LinkJP/Download/ --html
#python ./linkjpc_prep_old.py ${common_data_dir} ${tmp_data_dir} ${in_dir} ${out_dir_tmp_base} --log_level info --pre_matching mint --title_matching trim --char_match_min 0.2
#python $script ${common_data_dir} ${tmp_data_dir} ${in_dir} $sample${out_dir_tmp_base} --log_level info --pre_matching tinm --title_matching trim --char_match_min 0.2
#python ./linkjpc_prep_old.py ${common_data_dir} ${tmp_data_dir} ${in_dir} ${out_dir_tmp_base} --log_level info --pre_matching mint --title_matching full --char_match_min 0.2
#python ./linkjpc_prep_old.py ${common_data_dir} ${tmp_data_dir} ${in_dir} ${out_dir_tmp_base} --log_level info --pre_matching tinm --title_matching full --char_match_min 0.2
#python ./linkjpc_prep_old.py ~/Documents/SHINRA/2021-LinkJP/Download/ljc_data/common/ ~/Documents/SHINRA/2021-LinkJP/Download/ljc_data/sample/ ~/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/ene_annotation/ ~/tmp/sample2/  --pre_matching mint --char_match_min 0.2
#python ./linkjpc_prep_old.py ~/Documents/SHINRA/2021-LinkJP/Download/ljc_data/common/ ~/Documents/SHINRA/2021-LinkJP/Download/ljc_data/sample/ ~/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/ene_annotation/ ~/tmp/sample2/  --pre_matching tinm --char_match_min 0.2
