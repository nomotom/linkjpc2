#!/bin/sh -x
###########################################################
# 準備
###########################
# 1) 評価対象リストの作成　
# 2) 評価対象の指定
# 3) 図の出力指定
# 4) 図のx軸ラベル回転設定
###########################
#1) 評価対象のグループ指定
anal="5_module"

# 評価対象のグループ詳細
target_prec_key="top_precision"
target_recall_key="top_recall"
target_f1_key="top_f1"
tmp_target_key=${target_recall_key}

#2) 評価対象リストの作成
# 実行結果と評価のディレクトリ
score_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/anal_multi_20211022/"
#score_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/anal_20211016/"
target_dir_base="${score_dir_base}eval/"

#評価対象システムの親ディレクトリ
eval_target="${target_dir_base}${anal}_${tmp_target_key}/"

#上記のディレクトリを作成し評価対象リストをおく
eval_target_list="${eval_target}target.txt"

#3) 図の出力

# 散布図を出力するか
scatter_out="N"

# ヒートマップを出力するか
heatmap_out="Y"

#4) ヒートマップのX軸を回転させる出力ファイルのキーワード

x_rotation=("2_module,3_module,4_module")

################################################################################
scorer="/Users/masako/Documents/SHINRA/2021-LinkJP/scorer/linkjp_scorer"
#common_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/"

gold_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-211027/link_annotation/"
#grep 'script' ${script} | grep -v '##' | grep python | awk '{print $6}' |perl -pe 's/\${out_dir_base}//;' | perl -pe 's/\///g;'| perl -pe 's/\.tsv/\.json/;'|sort | uniq > ${target}


script_mod_scorer_result='./mod_scorer_result.py'
script_anal_scorer_result='./anal_scorer_result.py'
#
cat ${eval_target_list} | while read line
do
  mkdir ${eval_target}${line}
  python ${scorer} airport ${gold_dir}Airport.json ${score_dir_base}${line}/Airport.json --ignore-link-type | perl -pe 's/^/airport /;' > ${eval_target}${line}/Airport_score.txt
  python ${scorer} city ${gold_dir}City.json ${score_dir_base}${line}/City.json --ignore-link-type | perl -pe 's/^/city /;' > ${eval_target}${line}/City_score.txt
  python ${scorer} company ${gold_dir}Company.json ${score_dir_base}${line}/Company.json --ignore-link-type | perl -pe 's/^/company /;' > ${eval_target}${line}/Company_score.txt
  python ${scorer} compound ${gold_dir}Compound.json ${score_dir_base}${line}/Compound.json --ignore-link-type | perl -pe 's/^/compound /;' > ${eval_target}${line}/Compound_score.txt
  python ${scorer} conference ${gold_dir}Conference.json ${score_dir_base}${line}/Conference.json --ignore-link-type | perl -pe 's/^/conference /;' > ${eval_target}${line}/Conference_score.txt
  python ${scorer} person ${gold_dir}Person.json ${score_dir_base}${line}/Person.json --ignore-link-type | perl -pe 's/^/person /;' > ${eval_target}${line}/Person_score.txt
  python ${scorer} lake ${gold_dir}Lake.json ${score_dir_base}${line}/Lake.json --ignore-link-type | perl -pe 's/^/lake /;' > ${eval_target}${line}/Lake_score.txt
done

python ${script_mod_scorer_result} ${score_dir_base} ${anal} ${tmp_target_key}

python ${script_anal_scorer_result} ${score_dir_base} ${anal} ${tmp_target_key} ${scatter_out} ${heatmap_out} ${x_rotation}

