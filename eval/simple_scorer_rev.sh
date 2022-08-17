#!/bin/sh -x


# 出力　親ディレクトリ
#1) aiprb
#out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/aiprb/score_1module/"
#out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/aiprb/score_2module/"
#out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/aiprb/score_3module/"
#out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/aiprb/score_3system/"
#out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/bert_aiprb_modules/score/"
#out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/aiprb_n/score/"
out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/final_rev3/score/"


#2) systems
#out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/exp_systems/score/"

# 評価対象　親ディレクトリ
#1) aiprb
#sys_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/bert_aiprb_modules/"

#2) systems
#sys_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/exp_systems/"

#3) aiprb_n
#sys_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/aiprb_n/"
sys_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/final_rev3/"


#評価対象親ディレクトリに評価対象リストをおく
#eval_target_list="${sys_dir_base}eval_target.txt"
#eval_target_list="${sys_dir_base}eval_target_ablation_1module.txt"
#eval_target_list="${sys_dir_base}eval_target_ablation_2module.txt"
#eval_target_list="${sys_dir_base}eval_target_ablation_3module.txt"
eval_target_list="${sys_dir_base}eval_target.txt"


#score_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/sample/"
#score_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/final_rev3/"
#score_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/anal_20211016/"

# Usamiさんに2021/11/30にslack DMでいただいた評価結果返却のコードを一部修正したもの
scorer_all="/Users/masako/Documents/SHINRA/2021-LinkJP/scorer/linkjp_scorer_formal.py"

#GitHubで公開されているカテゴリ別評価ツール
scorer_cat="/Users/masako/Documents/SHINRA/2021-LinkJP/scorer/linkjp_scorer"

gold_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-211027/link_annotation/"
#grep 'script' ${script} | grep -v '##' | grep python | awk '{print $6}' |perl -pe 's/\${out_dir_base}//;' | perl -pe 's/\///g;'| perl -pe 's/\.tsv/\.json/;'|sort | uniq > ${target}


attr_type="all"
# attr_type="del_slink"


cat ${eval_target_list} | while read line
do
  mkdir ${out_dir_base}${line}
  # 全体のファイル
  python ${scorer_all} ${gold_dir} ${sys_dir_base}${line} ${out_dir_base}${line} ${attr_type}
  # カテゴリ別ファイル
  python ${scorer_cat} airport ${gold_dir}Airport.json ${sys_dir_base}${line}/Airport.json ${attr_type} --ignore-link-type | perl -pe 's/^/Airport /;' | perl -pe 's/^Airport precision/cat precision/' > ${out_dir_base}${line}/Airport_score.txt
  python ${scorer_cat} city ${gold_dir}City.json ${sys_dir_base}${line}/City.json ${attr_type} --ignore-link-type | perl -pe 's/^/City /;'| perl -pe 's/^City precision/cat precision/'> ${out_dir_base}${line}/City_score.txt
  python ${scorer_cat} company ${gold_dir}Company.json ${sys_dir_base}${line}/Company.json ${attr_type} --ignore-link-type | perl -pe 's/^/Company /;' | perl -pe 's/^Company precision/cat precision/' > ${out_dir_base}${line}/Company_score.txt
  python ${scorer_cat} compound ${gold_dir}Compound.json ${sys_dir_base}${line}/Compound.json ${attr_type} --ignore-link-type | perl -pe 's/^/Compound /;' | perl -pe 's/^Compound precision/cat precision/' > ${out_dir_base}${line}/Compound_score.txt
  python ${scorer_cat} conference ${gold_dir}Conference.json ${sys_dir_base}${line}/Conference.json ${attr_type} --ignore-link-type | perl -pe 's/^/Conference /;' | perl -pe 's/^Conference precision/cat precision/' > ${out_dir_base}${line}/Conference_score.txt
  python ${scorer_cat} person ${gold_dir}Person.json ${sys_dir_base}${line}/Person.json ${attr_type} --ignore-link-type | perl -pe 's/^/Person /;' | perl -pe 's/^Person precision/cat precision/' > ${out_dir_base}${line}/Person_score.txt
  python ${scorer_cat} lake ${gold_dir}Lake.json ${sys_dir_base}${line}/Lake.json ${attr_type} --ignore-link-type | perl -pe 's/^/Lake /;' | perl -pe 's/^Lake precision/cat precision/' > ${out_dir_base}${line}/Lake_score.txt
#  python ${scorer_cat} airport ${gold_dir}Airport.json ${sys_dir_base}${line}/Airport.json --ignore-link-type | perl -pe 's/^/airport /;' > ${out_dir_base}${line}/Airport_score.txt
#  python ${scorer_cat} city ${gold_dir}City.json ${sys_dir_base}${line}/City.json --ignore-link-type | perl -pe 's/^/city /;' > ${out_dir_base}${line}/City_score.txt
#  python ${scorer_cat} company ${gold_dir}Company.json ${sys_dir_base}${line}/Company.json --ignore-link-type | perl -pe 's/^/company /;' > ${out_dir_base}${line}/Company_score.txt
#  python ${scorer_cat} compound ${gold_dir}Compound.json ${sys_dir_base}${line}/Compound.json --ignore-link-type | perl -pe 's/^/compound /;' > ${out_dir_base}${line}/Compound_score.txt
#  python ${scorer_cat} conference ${gold_dir}Conference.json ${sys_dir_base}${line}/Conference.json --ignore-link-type | perl -pe 's/^/conference /;' > ${out_dir_base}${line}/Conference_score.txt
#  python ${scorer_cat} person ${gold_dir}Person.json ${sys_dir_base}${line}/Person.json --ignore-link-type | perl -pe 's/^/person /;' > ${out_dir_base}${line}/Person_score.txt
#  python ${scorer_cat} lake ${gold_dir}Lake.json ${sys_dir_base}${line}/Lake.json --ignore-link-type | perl -pe 's/^/lake /;' > ${out_dir_base}${line}/Lake_score.txt
done

#cat ${eval_target_list} | while read line
#do
#  mkdir ${out_dir_base}${line}
#  # 全体のファイル
#  python ${scorer_all} ${gold_dir} ${sys_dir_base}${line} ${out_dir_base}${line}
#  # カテゴリ別ファイル
#  python ${scorer_cat} airport ${gold_dir}Airport.json ${sys_dir_base}${line}/Airport.json --ignore-link-type | perl -pe 's/^/Airport /;' | perl -pe 's/^Airport precision/cat precision/' > ${out_dir_base}${line}/Airport_score.txt
#  python ${scorer_cat} city ${gold_dir}City.json ${sys_dir_base}${line}/City.json --ignore-link-type | perl -pe 's/^/City /;'| perl -pe 's/^City precision/cat precision/'> ${out_dir_base}${line}/City_score.txt
#  python ${scorer_cat} company ${gold_dir}Company.json ${sys_dir_base}${line}/Company.json --ignore-link-type | perl -pe 's/^/Company /;' | perl -pe 's/^Company precision/cat precision/' > ${out_dir_base}${line}/Company_score.txt
#  python ${scorer_cat} compound ${gold_dir}Compound.json ${sys_dir_base}${line}/Compound.json --ignore-link-type | perl -pe 's/^/Compound /;' | perl -pe 's/^Compound precision/cat precision/' > ${out_dir_base}${line}/Compound_score.txt
#  python ${scorer_cat} conference ${gold_dir}Conference.json ${sys_dir_base}${line}/Conference.json --ignore-link-type | perl -pe 's/^/Conference /;' | perl -pe 's/^Conference precision/cat precision/' > ${out_dir_base}${line}/Conference_score.txt
#  python ${scorer_cat} person ${gold_dir}Person.json ${sys_dir_base}${line}/Person.json --ignore-link-type | perl -pe 's/^/Person /;' | perl -pe 's/^Person precision/cat precision/' > ${out_dir_base}${line}/Person_score.txt
#  python ${scorer_cat} lake ${gold_dir}Lake.json ${sys_dir_base}${line}/Lake.json --ignore-link-type | perl -pe 's/^/Lake /;' | perl -pe 's/^Lake precision/cat precision/' > ${out_dir_base}${line}/Lake_score.txt
##  python ${scorer_cat} airport ${gold_dir}Airport.json ${sys_dir_base}${line}/Airport.json --ignore-link-type | perl -pe 's/^/airport /;' > ${out_dir_base}${line}/Airport_score.txt
##  python ${scorer_cat} city ${gold_dir}City.json ${sys_dir_base}${line}/City.json --ignore-link-type | perl -pe 's/^/city /;' > ${out_dir_base}${line}/City_score.txt
##  python ${scorer_cat} company ${gold_dir}Company.json ${sys_dir_base}${line}/Company.json --ignore-link-type | perl -pe 's/^/company /;' > ${out_dir_base}${line}/Company_score.txt
##  python ${scorer_cat} compound ${gold_dir}Compound.json ${sys_dir_base}${line}/Compound.json --ignore-link-type | perl -pe 's/^/compound /;' > ${out_dir_base}${line}/Compound_score.txt
##  python ${scorer_cat} conference ${gold_dir}Conference.json ${sys_dir_base}${line}/Conference.json --ignore-link-type | perl -pe 's/^/conference /;' > ${out_dir_base}${line}/Conference_score.txt
##  python ${scorer_cat} person ${gold_dir}Person.json ${sys_dir_base}${line}/Person.json --ignore-link-type | perl -pe 's/^/person /;' > ${out_dir_base}${line}/Person_score.txt
##  python ${scorer_cat} lake ${gold_dir}Lake.json ${sys_dir_base}${line}/Lake.json --ignore-link-type | perl -pe 's/^/lake /;' > ${out_dir_base}${line}/Lake_score.txt
#done
#


