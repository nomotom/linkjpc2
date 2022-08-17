#!/bin/sh -x
now=`date +%Y%m%d%H%M%S`
script="./linkjpc.py"
common_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/common/"
tmp_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/sample/"
in_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/ene_annotation/"
gold_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/link_annotation/"
out_dir_tmp_base="/Users/masako/tmp/sample/tmp_test/"
setting_dir="${out_dir_tmp_base}setting/"
eval_target="./eval_target_tmp.txt"

#grep 'script' ~/PycharmProjects/linkjpc/linkjpc_test_sample.sh | awk '{print $6}' | perl -pe 's/\${out_dir_tmp_base}//;' | perl -pe 's/\///g;' | sort | uniq > $eval_target

#grep 'script' ~/PycharmProjects/linkjpc/linkjpc_all_sample.sh | awk '{print $6}' | perl -pe 's/\${out_dir_tmp_base}//;' | perl -pe 's/\///g;' | sort | uniq > $eval_target
python json2tsv_linkjp.py $out_dir_tmp_base $gold_dir $in_dir $eval_target
python evaluation_linkjp.py $out_dir_tmp_base $gold_dir $eval_target
cd $out_dir_tmp_base

cat */all_summary.tsv > all_summary_pre.tsv
cat ../summary_header.txt all_summary_pre.tsv > all_summary.tsv
cp all_summary.tsv eval_${now}.txt
cp ~/PycharmProjects/linkjpc/linkjpc_all_sample.sh env_${now}.txt
cat ./*/*_summary.tsv | grep -v SYS_ID | grep -v ^e | grep -v ^p | sort -d > summary_category_pre.tsv
cat ../summary_cat_header.txt summary_category_pre.tsv > summary_category.tsv
cp summary_category.tsv ${setting_dir}summary_category_${now}.txt
