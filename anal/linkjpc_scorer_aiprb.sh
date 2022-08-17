#!/bin/bash
###########################################################
# 準備
###########################
# 1) 評価対象リストの作成　
# 2) 評価対象の指定
# 3) 図の出力指定
# 4) 図のx軸ラベル回転設定
###########################
#1) 評価対象のグループ指定
# anal="systems"

# 評価対象のグループ詳細
#target_prec_key="precision"
#target_recall_key="recall"
#target_f1_key="f1"
#tmp_target_key=${target_f1_key}

# scorerの出力ファイルのディレクトリ
# ここに全スコアをまとめたファイルが生成される
#org_score_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/exp_systems/score/"
#org_score_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/exp/score/"
#org_score_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/aiprb/score_1module/"
#org_score_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/aiprb/score_2module/"
#org_score_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/aiprb/score_3module/"
org_score_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/aiprb/score_3system/"


# 評価対象のシステムリストとスコアをまとめた出力ファイルを置くディレクトリ
#anal_target_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/exp/anal/"
#anal_target_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/aiprb/anal_1module/"
#anal_target_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/aiprb/anal_2module/"
#anal_target_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/aiprb/anal_3module/"
anal_target_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/aiprb/anal_3system/"

#2) 評価対象リストの作成
# 評価のディレクトリ
# score_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/evaluation/"
# target_dir_base="${score_dir_base}eval/"
#keyword="cat"
#評価対象システムの親ディレクトリ
# eval_target_dir="${target_dir_base}${anal}_${tmp_target_key}/"
#eval_target_dir="${target_dir_base}${keyword}/"

#anal_target_fname="anal_target.txt"
#anal_target_fname="anal_target_ablation_1module.txt"
#anal_target_fname="anal_target_ablation_2module.txt"
#anal_target_fname="anal_target_ablation_3module.txt"
anal_target_fname="anal_target_3system.txt"

#上記のディレクトリを作成し評価対象リストをおく
anal_target_list="${anal_target_dir}${anal_target_fname}"
#AIPCB_CBI
#AIPRB_WSM
#AIPRB_SMW
#AIPRB_SMWL
#ATID_ATAG
#ATID_ATAG_SEARCH
#NAIST_baseline_plus_bert
#NAIST_only_bert
#amano_genre


#3) 図の出力

# 散布図を出力するか
scatter_out="N"

# ヒートマップを出力するか
heatmap_out="Y"

#4) ヒートマップのX軸を回転させる出力ファイルのキーワード

#x_rotation=("amano, NAIST, ATID, AIPRB, AIPCB")
x_rotation=("mint, tinm, wlink, slink, l_")

#5) 属性名にリンク先のある正解数を併記するか
set_att_freq="Y"


################################################################################
# scorer="/Users/masako/Documents/SHINRA/2021-LinkJP/scorer/linkjp_scorer"
# scorer="/Users/masako/Documents/SHINRA/2021-LinkJP/scorer/linkjp_scorer_formal.py"

#common_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/"

gold_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-211027/link_annotation/"
#grep 'script' ${script} | grep -v '##' | grep python | awk '{print $6}' |perl -pe 's/\${out_dir_base}//;' | perl -pe 's/\///g;'| perl -pe 's/\.tsv/\.json/;'|sort | uniq > ${target}

score_file_name="sys_score_all.tsv"

script_mod_scorer_result='./anal/mod_scorer_result_rev.py'
# script_mod_scorer_result='./anal/mod_scorer_result.py'
script_anal_scorer_result='./anal/anal_scorer_result_rev.py'

# 評価はsimple_scorer_rev.shで行う
#
#cat ${eval_target_list} | while read line
#do
#  mkdir ${eval_target}${line}
#  python ${scorer} airport ${gold_dir}Airport.json ${score_dir_base}${line}/Airport.json --ignore-link-type | perl -pe 's/^/airport /;' > ${eval_target}${line}/Airport_score.txt
#  python ${scorer} city ${gold_dir}City.json ${score_dir_base}${line}/City.json --ignore-link-type | perl -pe 's/^/city /;' > ${eval_target}${line}/City_score.txt
#  python ${scorer} company ${gold_dir}Company.json ${score_dir_base}${line}/Company.json --ignore-link-type | perl -pe 's/^/company /;' > ${eval_target}${line}/Company_score.txt
#  python ${scorer} compound ${gold_dir}Compound.json ${score_dir_base}${line}/Compound.json --ignore-link-type | perl -pe 's/^/compound /;' > ${eval_target}${line}/Compound_score.txt
#  python ${scorer} conference ${gold_dir}Conference.json ${score_dir_base}${line}/Conference.json --ignore-link-type | perl -pe 's/^/conference /;' > ${eval_target}${line}/Conference_score.txt
#  python ${scorer} person ${gold_dir}Person.json ${score_dir_base}${line}/Person.json --ignore-link-type | perl -pe 's/^/person /;' > ${eval_target}${line}/Person_score.txt
#  python ${scorer} lake ${gold_dir}Lake.json ${score_dir_base}${line}/Lake.json --ignore-link-type | perl -pe 's/^/lake /;' > ${eval_target}${line}/Lake_score.txt
#done
##

cat ${anal_target_list} | while read line
do
  mkdir ${anal_target_dir}${line}
done
python ${script_mod_scorer_result} ${org_score_dir} ${anal_target_dir} ${anal_target_list} ${set_att_freq}

python ${script_anal_scorer_result} ${anal_target_dir} ${anal_target_list} ${scatter_out} ${heatmap_out} ${x_rotation}

