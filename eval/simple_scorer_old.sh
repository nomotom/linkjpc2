#!/bin/sh -x

score_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/exp/"
#score_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/sample/"
#score_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/final_rev3/"
#score_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/anal_20211016/"

#上記のディレクトリを作成し評価対象リストをおく
eval_target_list="${score_dir_base}target.txt"

# scorer="./eval/linkjp_scorer_formal.py"
scorer="/Users/masako/Documents/SHINRA/2021-LinkJP/scorer/linkjp_scorer"
#common_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/"

gold_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-211027/link_annotation/"
#grep 'script' ${script} | grep -v '##' | grep python | awk '{print $6}' |perl -pe 's/\${out_dir_base}//;' | perl -pe 's/\///g;'| perl -pe 's/\.tsv/\.json/;'|sort | uniq > ${target}

cat ${eval_target_list} | while read line
do
  # mkdir ${eval_target}${line}
  python ${scorer} airport ${gold_dir}Airport.json ${score_dir_base}${line}/Airport.json --ignore-link-type | perl -pe 's/^/airport /;' > ${score_dir_base}${line}/Airport_score.txt
  python ${scorer} city ${gold_dir}City.json ${score_dir_base}${line}/City.json --ignore-link-type | perl -pe 's/^/city /;' > ${score_dir_base}${line}/City_score.txt
  python ${scorer} company ${gold_dir}Company.json ${score_dir_base}${line}/Company.json --ignore-link-type | perl -pe 's/^/company /;' > ${score_dir_base}${line}/Company_score.txt
  python ${scorer} compound ${gold_dir}Compound.json ${score_dir_base}${line}/Compound.json --ignore-link-type | perl -pe 's/^/compound /;' > ${score_dir_base}${line}/Compound_score.txt
  python ${scorer} conference ${gold_dir}Conference.json ${score_dir_base}${line}/Conference.json --ignore-link-type | perl -pe 's/^/conference /;' > ${score_dir_base}${line}/Conference_score.txt
  python ${scorer} person ${gold_dir}Person.json ${score_dir_base}${line}/Person.json --ignore-link-type | perl -pe 's/^/person /;' > ${score_dir_base}${line}/Person_score.txt
  python ${scorer} lake ${gold_dir}Lake.json ${score_dir_base}${line}/Lake.json --ignore-link-type | perl -pe 's/^/lake /;' > ${score_dir_base}${line}/Lake_score.txt
done



