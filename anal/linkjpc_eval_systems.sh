#!/bin/sh -x
#now=`date +%Y%m%d%H%M%S`
#now=`date +%Y%m%d%H%M%S`
#pid=$$

#script="./linkjpc_multi_ans.sh"
#script="./linkjpc_final_test.sh"
#script="./tests_private/linkjpc_test_systems.sh"
#script="./tests_private/linkjpc_test_private.sh"

#script="./linkjpc_all_test.sh"
#script="./linkjpc_multi_ans.sh"
#script="./linkjpc_org.py"
# script="./linkjpc_test.sh"

common_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/common/"
tmp_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/test/"
in_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-211027/ene_annotation/"
gold_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-211027/link_annotation/"
# out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/exp/"
# out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/aiprb/"
out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/exp_systems/"


#out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/anal_20211104/"

#out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/anal_multi_20211104/"

#out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/final_rev5/"
#out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/final_rev4/"
#out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/anal_multi_20211030/"
#out_dir_base="/Users/masako/Documents/tmp/test/tmp_test/20211030/"
#out_dir_base="/Users/masako/tmp/test/tmp_test/"


#out_dir_tmp_base="/Users/masako/tmp/sample/tmp_test"
setting_dir="${out_dir_base}setting/"
# eval_target="${out_dir_base}eval_target_ablation_single_module.txt"
eval_target="${out_dir_base}eval_target.txt"


# eval_target="${out_dir_base}eval_test_target"
eval_script="./anal/evaluation_linkjp.py"

# 2021/12/23 再帰リンクの属性を除いた評価に対応
attr_type="all"
# attr_type="del_slink"


# 入力ファイル、正解（リンクタイプつき）、システム出力をtsv化
python ./anal/json2tsv_linkjp.py $out_dir_base $gold_dir $in_dir $eval_target
#python json2tsv_linkjp.py $out_dir_base $gold_dir $in_dir $eval_target$$
#python evaluation_linkjp_old.py $out_dir_base $gold_dir $eval_target$$
#python evaluation_linkjp_new.py $out_dir_base $gold_dir $in_dir $eval_target$$
python $eval_script $out_dir_base $gold_dir $in_dir $eval_target $attr_type
# python evaluation_linkjp_new.py $out_dir_base $gold_dir $in_dir $eval_target
# python evaluation_linkjp_new.py $out_dir_base $gold_dir $in_dir $eval_target$$

# python evaluation_linkjp_ex.py $out_dir_base $gold_dir $eval_target$$

cd $out_dir_base


cat */all_summary.tsv > all_summary_pre.tsv
cat ../summary_header.txt all_summary_pre.tsv > all_summary.tsv
cp all_summary.tsv eval.txt
# cp all_summary.tsv eval_$$.txt
# cp $script env.txt
# cp $script env_$$.txt
cat ./*/*_summary.tsv | grep -v SYS_ID | grep -v ^e | grep -v ^p | sort -d > summary_category_pre.tsv
#cat ../summary_cat_header.txt summary_category_pre.tsv > summary_category_$$.tsv
cat ../summary_cat_header.txt summary_category_pre.tsv > summary_category.tsv

#cat ../summary_cat_header.txt summary_category_pre.tsv > summary_category_${now}.tsv
mkdir ${setting_dir}
cp summary_category.tsv ${setting_dir}summary_category.txt
#cp summary_category.tsv ${setting_dir}summary_category_$$.txt
#cp summary_category.tsv ${setting_dir}summary_category_${now}.txt
