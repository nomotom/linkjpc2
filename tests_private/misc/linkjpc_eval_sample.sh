#!/bin/sh -x
#now=`date +%Y%m%d%H%M%S`
#now=`date +%Y%m%d%H%M%S`
#pid=$$

script="./linkjpc.py"
common_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/common/"
tmp_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/sample/"
in_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/ene_annotation/"
gold_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/link_annotation/"
out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20211019_2/"
eval_target="${out_dir_base}eval_sample_target"
#out_dir_tmp_base="/Users/masako/tmp/sample/tmp_test"
setting_dir="${out_dir_base}setting/"

cat ~/PycharmProjects/linkjpc/linkjpc_all_sample.sh | grep 'script'  | grep 'python'| grep -v '#' | awk '{print $6}' | perl -pe 's/\${out_dir_base}//;' | perl -pe 's/\///g;' | sort | uniq > ${eval_target}$$

#cat ~/PycharmProjects/linkjpc/linkjpc_all_sample.sh | grep 'script' | grep -v '#' | grep 'python'| awk '{print $6}' | perl -pe 's/\${out_dir_base}//;' | perl -pe 's/\///g;' | sort | uniq > ${eval_target}$$
python json2tsv_linkjp.py $out_dir_base $gold_dir $in_dir ${eval_target}$$
python evaluation_linkjp.py $out_dir_base $gold_dir ${eval_target}$$
cd $out_dir_base
cat */all_summary.tsv > all_summary_pre.tsv
cat ../summary_header.txt all_summary_pre.tsv > all_summary.tsv
cp all_summary.tsv eval_$$.txt
cp ~/PycharmProjects/linkjpc/linkjpc_all_sample.sh env_$$.txt
cat ./*/*_summary.tsv | grep -v SYS_ID | grep -v ^e | grep -v ^p | sort -d > summary_category_pre.tsv
cat ../summary_cat_header.txt summary_category_pre.tsv > summary_category_$$.tsv
#cat ../summary_cat_header.txt summary_category_pre.tsv > summary_category_${now}.tsv
cp summary_category_$$.tsv ${setting_dir}summary_category_$$.txt
#cp summary_category.tsv ${setting_dir}summary_category_${now}.txt

