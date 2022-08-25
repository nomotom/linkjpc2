#!/bin/sh -x




#2) systems
#out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/exp_systems/score/"

# 評価対象　親ディレクトリ
#1) aiprb
#sys_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/bert_aiprb_modules/"

#2) systems
#sys_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/exp_systems/"

#3) aiprb_n
#sys_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/aiprb_n/"
# sys_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/final_rev3/"

# 20220818
sys_dir_base="/Users/masako/Documents/SHINRA/2022-LinkJP/test_out/shinra2021base_20220824/"

# 出力　親ディレクトリ
#1) aiprb
#out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/aiprb/score_1module/"
#out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/aiprb/score_2module/"
#out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/aiprb/score_3module/"
#out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/aiprb/score_3system/"
#out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/bert_aiprb_modules/score/"
#out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/aiprb_n/score/"
# out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/final_rev3/score/"
out_dir_base="${sys_dir_base}score/"


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
# scorer_all="/Users/masako/Documents/SHINRA/2021-LinkJP/scorer/linkjp_scorer_formal.py"
scorer_all="/Users/masako/Documents/SHINRA/2022-LinkJP/scorer/linkjp_scorer_formal_rev_2022.py"

#GitHubで公開されているカテゴリ別評価ツール
scorer_cat="/Users/masako/Documents/SHINRA/2022-LinkJP/scorer/linkjp_scorer"

# scorer_cat="./scorer/linkjp_scorer"

# gold_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-211027/link_annotation/"
gold_dir="/Users/masako/Documents/SHINRA/2022-LinkJP/Download/leaderboard-link-ans-20220816/link_annotation/"

#grep 'script' ${script} | grep -v '##' | grep python | awk '{print $6}' |perl -pe 's/\${out_dir_base}//;' | perl -pe 's/\///g;'| perl -pe 's/\.tsv/\.json/;'|sort | uniq > ${target}


attr_type="all"
# attr_type="del_slink"


cat ${eval_target_list} | while read line
do
  mkdir ${out_dir_base}${line}
  # 全体のファイル
  python ${scorer_all} ${gold_dir} ${sys_dir_base}${line} ${out_dir_base}${line} ${attr_type}
  # カテゴリ別ファイル
#  python ${scorer_cat} person ${gold_dir}Person_dist.jsonl ${sys_dir_base}${line}/Person.jsonl ${attr_type} --ignore-link-type | perl -pe 's/^/person/;' > ${out_dir_base}${line}/Person_score.txt
#  python ${scorer_cat} god ${gold_dir}God_dist.jsonl ${sys_dir_base}${line}/God.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/god/;' > ${out_dir_base}${line}/God_score.txt
#  python ${scorer_cat} individual_animal_other ${gold_dir}Individual_Animal_Other_dist.jsonl ${sys_dir_base}${line}/Individual_Animal_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/individual_animal_other/;' > ${out_dir_base}${line}/Individual_Animal_Other_score.txt
#  python ${scorer_cat} racehorse ${gold_dir}Racehorse_dist.jsonl ${sys_dir_base}${line}/Racehorse.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/racehorse/;' > ${out_dir_base}${line}/Racehorse_score.txt
#  python ${scorer_cat} individual_flora ${gold_dir}Individual_Flora_dist.jsonl ${sys_dir_base}${line}/Individual_Flora.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/individual_flora/;' > ${out_dir_base}${line}/Individual_Flora_score.txt
#  python ${scorer_cat} organization_other ${gold_dir}Organization_Other_dist.jsonl ${sys_dir_base}${line}/Organization_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/organization_other/;' > ${out_dir_base}${line}/Organization_Other_score.txt
#  python ${scorer_cat} international_organization ${gold_dir}International_Organization_dist.jsonl ${sys_dir_base}${line}/International_Organization.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/international_organization/;' > ${out_dir_base}${line}/International_Organization_score.txt
#  python ${scorer_cat} show_organization ${gold_dir}Show_Organization_dist.jsonl ${sys_dir_base}${line}/Show_Organization.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/show_organization/;' > ${out_dir_base}${line}/Show_Organization_score.txt
#  python ${scorer_cat} family ${gold_dir}Family_dist.jsonl ${sys_dir_base}${line}/Family.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/family/;' > ${out_dir_base}${line}/Family_score.txt
#  python ${scorer_cat} ethnic_group_other ${gold_dir}Ethnic_Group_Other_dist.jsonl ${sys_dir_base}${line}/Ethnic_Group_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/ethnic_group_other/;' > ${out_dir_base}${line}/Ethnic_Group_Other_score.txt
#  python ${scorer_cat} nationality ${gold_dir}Nationality_dist.jsonl ${sys_dir_base}${line}/Nationality.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/nationality/;' > ${out_dir_base}${line}/Nationality_score.txt
#  python ${scorer_cat} sports_federation ${gold_dir}Sports_Federation_dist.jsonl ${sys_dir_base}${line}/Sports_Federation.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/sports_federation/;' > ${out_dir_base}${line}/Sports_Federation_score.txt
#  python ${scorer_cat} sports_league ${gold_dir}Sports_League_dist.jsonl ${sys_dir_base}${line}/Sports_League.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/sports_league/;' > ${out_dir_base}${line}/Sports_League_score.txt
#  python ${scorer_cat} sports_team ${gold_dir}Sports_Team_dist.jsonl ${sys_dir_base}${line}/Sports_Team.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/sports_team/;' > ${out_dir_base}${line}/Sports_Team_score.txt
#  python ${scorer_cat} nonprofit_organization ${gold_dir}Nonprofit_Organization_dist.jsonl ${sys_dir_base}${line}/Nonprofit_Organization.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/nonprofit_organization/;' > ${out_dir_base}${line}/Nonprofit_Organization_score.txt
#  python ${scorer_cat} company ${gold_dir}Company_dist.jsonl ${sys_dir_base}${line}/Company.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/company/;' > ${out_dir_base}${line}/Company_score.txt
#  python ${scorer_cat} company_group ${gold_dir}Company_Group_dist.jsonl ${sys_dir_base}${line}/Company_Group.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/company_group/;' > ${out_dir_base}${line}/Company_Group_score.txt
#  python ${scorer_cat} political_organization_other ${gold_dir}Political_Organization_Other_dist.jsonl ${sys_dir_base}${line}/Political_Organization_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/political_organization_other/;' > ${out_dir_base}${line}/Political_Organization_Other_score.txt
#  python ${scorer_cat} government ${gold_dir}Government_dist.jsonl ${sys_dir_base}${line}/Government.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/government/;' > ${out_dir_base}${line}/Government_score.txt
#  python ${scorer_cat} political_party ${gold_dir}Political_Party_dist.jsonl ${sys_dir_base}${line}/Political_Party.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/political_party/;' > ${out_dir_base}${line}/Political_Party_score.txt
#  python ${scorer_cat} cabinet ${gold_dir}Cabinet_dist.jsonl ${sys_dir_base}${line}/Cabinet.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/cabinet/;' > ${out_dir_base}${line}/Cabinet_score.txt
#  python ${scorer_cat} military ${gold_dir}Military_dist.jsonl ${sys_dir_base}${line}/Military.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/military/;' > ${out_dir_base}${line}/Military_score.txt
#  python ${scorer_cat} location_other ${gold_dir}Location_Other_dist.jsonl ${sys_dir_base}${line}/Location_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/location_other/;' > ${out_dir_base}${line}/Location_Other_score.txt
#  python ${scorer_cat} gpe_other ${gold_dir}GPE_Other_dist.jsonl ${sys_dir_base}${line}/GPE_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/gpe_other/;' > ${out_dir_base}${line}/GPE_Other_score.txt
#  python ${scorer_cat} city ${gold_dir}City_dist.jsonl ${sys_dir_base}${line}/City.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/city/;' > ${out_dir_base}${line}/City_score.txt
#  python ${scorer_cat} province ${gold_dir}Province_dist.jsonl ${sys_dir_base}${line}/Province.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/province/;' > ${out_dir_base}${line}/Province_score.txt
#  python ${scorer_cat} country ${gold_dir}Country_dist.jsonl ${sys_dir_base}${line}/Country.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/country/;' > ${out_dir_base}${line}/Country_score.txt
#  python ${scorer_cat} continental_region ${gold_dir}Continental_Region_dist.jsonl ${sys_dir_base}${line}/Continental_Region.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/continental_region/;' > ${out_dir_base}${line}/Continental_Region_score.txt
#  python ${scorer_cat} domestic_region ${gold_dir}Domestic_Region_dist.jsonl ${sys_dir_base}${line}/Domestic_Region.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/domestic_region/;' > ${out_dir_base}${line}/Domestic_Region_score.txt
#  python ${scorer_cat} geological_region_other ${gold_dir}Geological_Region_Other_dist.jsonl ${sys_dir_base}${line}/Geological_Region_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/geological_region_other/;' > ${out_dir_base}${line}/Geological_Region_Other_score.txt
#  python ${scorer_cat} spa ${gold_dir}Spa_dist.jsonl ${sys_dir_base}${line}/Spa.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/spa/;' > ${out_dir_base}${line}/Spa_score.txt
#  python ${scorer_cat} mountain ${gold_dir}Mountain_dist.jsonl ${sys_dir_base}${line}/Mountain.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/mountain/;' > ${out_dir_base}${line}/Mountain_score.txt
#  python ${scorer_cat} island ${gold_dir}Island_dist.jsonl ${sys_dir_base}${line}/Island.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/island/;' > ${out_dir_base}${line}/Island_score.txt
#  python ${scorer_cat} river ${gold_dir}River_dist.jsonl ${sys_dir_base}${line}/River.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/river/;' > ${out_dir_base}${line}/River_score.txt
#  python ${scorer_cat} lake ${gold_dir}Lake_dist.jsonl ${sys_dir_base}${line}/Lake.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/lake/;' > ${out_dir_base}${line}/Lake_score.txt
#  python ${scorer_cat} sea ${gold_dir}Sea_dist.jsonl ${sys_dir_base}${line}/Sea.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/sea/;' > ${out_dir_base}${line}/Sea_score.txt
#  python ${scorer_cat} bay ${gold_dir}Bay_dist.jsonl ${sys_dir_base}${line}/Bay.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/bay/;' > ${out_dir_base}${line}/Bay_score.txt
#  python ${scorer_cat} astronomical_object_other ${gold_dir}Astronomical_Object_Other_dist.jsonl ${sys_dir_base}${line}/Astronomical_Object_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/astronomical_object_other/;' > ${out_dir_base}${line}/Astronomical_Object_Other_score.txt
#  python ${scorer_cat} astronomical_object_part ${gold_dir}Astronomical_Object_Part_dist.jsonl ${sys_dir_base}${line}/Astronomical_Object_Part.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/astronomical_object_part/;' > ${out_dir_base}${line}/Astronomical_Object_Part_score.txt
#  python ${scorer_cat} galaxy ${gold_dir}Galaxy_dist.jsonl ${sys_dir_base}${line}/Galaxy.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/galaxy/;' > ${out_dir_base}${line}/Galaxy_score.txt
#  python ${scorer_cat} star ${gold_dir}Star_dist.jsonl ${sys_dir_base}${line}/Star.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/star/;' > ${out_dir_base}${line}/Star_score.txt
#  python ${scorer_cat} planet_satellite ${gold_dir}Planet_Satellite_dist.jsonl ${sys_dir_base}${line}/Planet_Satellite.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/planet_satellite/;' > ${out_dir_base}${line}/Planet_Satellite_score.txt
#  python ${scorer_cat} constellation ${gold_dir}Constellation_dist.jsonl ${sys_dir_base}${line}/Constellation.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/constellation/;' > ${out_dir_base}${line}/Constellation_score.txt
#  python ${scorer_cat} facility_other ${gold_dir}Facility_Other_dist.jsonl ${sys_dir_base}${line}/Facility_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/facility_other/;' > ${out_dir_base}${line}/Facility_Other_score.txt
#  python ${scorer_cat} facility_part ${gold_dir}Facility_Part_dist.jsonl ${sys_dir_base}${line}/Facility_Part.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/facility_part/;' > ${out_dir_base}${line}/Facility_Part_score.txt
#  python ${scorer_cat} dam ${gold_dir}Dam_dist.jsonl ${sys_dir_base}${line}/Dam.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/dam/;' > ${out_dir_base}${line}/Dam_score.txt
#  python ${scorer_cat} archaeological_place_other ${gold_dir}Archaeological_Place_Other_dist.jsonl ${sys_dir_base}${line}/Archaeological_Place_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/archaeological_place_other/;' > ${out_dir_base}${line}/Archaeological_Place_Other_score.txt
#  python ${scorer_cat} cemetery ${gold_dir}Cemetery_dist.jsonl ${sys_dir_base}${line}/Cemetery.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/cemetery/;' > ${out_dir_base}${line}/Cemetery_score.txt
#  python ${scorer_cat} foe_other ${gold_dir}FOE_Other_dist.jsonl ${sys_dir_base}${line}/FOE_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/foe_other/;' > ${out_dir_base}${line}/FOE_Other_score.txt
#  python ${scorer_cat} military_base ${gold_dir}Military_Base_dist.jsonl ${sys_dir_base}${line}/Military_Base.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/military_base/;' > ${out_dir_base}${line}/Military_Base_score.txt
#  python ${scorer_cat} castle ${gold_dir}Castle_dist.jsonl ${sys_dir_base}${line}/Castle.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/castle/;' > ${out_dir_base}${line}/Castle_score.txt
#  python ${scorer_cat} palace ${gold_dir}Palace_dist.jsonl ${sys_dir_base}${line}/Palace.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/palace/;' > ${out_dir_base}${line}/Palace_score.txt
#  python ${scorer_cat} public_institution ${gold_dir}Public_Institution_dist.jsonl ${sys_dir_base}${line}/Public_Institution.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/public_institution/;' > ${out_dir_base}${line}/Public_Institution_score.txt
#  python ${scorer_cat} accommodation ${gold_dir}Accommodation_dist.jsonl ${sys_dir_base}${line}/Accommodation.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/accommodation/;' > ${out_dir_base}${line}/Accommodation_score.txt
#  python ${scorer_cat} medical_institution ${gold_dir}Medical_Institution_dist.jsonl ${sys_dir_base}${line}/Medical_Institution.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/medical_institution/;' > ${out_dir_base}${line}/Medical_Institution_score.txt
#  python ${scorer_cat} school ${gold_dir}School_dist.jsonl ${sys_dir_base}${line}/School.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/school/;' > ${out_dir_base}${line}/School_score.txt
#  python ${scorer_cat} research_institute ${gold_dir}Research_Institute_dist.jsonl ${sys_dir_base}${line}/Research_Institute.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/research_institute/;' > ${out_dir_base}${line}/Research_Institute_score.txt
#  python ${scorer_cat} market ${gold_dir}Market_dist.jsonl ${sys_dir_base}${line}/Market.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/market/;' > ${out_dir_base}${line}/Market_score.txt
#  python ${scorer_cat} power_plant ${gold_dir}Power_Plant_dist.jsonl ${sys_dir_base}${line}/Power_Plant.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/power_plant/;' > ${out_dir_base}${line}/Power_Plant_score.txt
#  python ${scorer_cat} park ${gold_dir}Park_dist.jsonl ${sys_dir_base}${line}/Park.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/park/;' > ${out_dir_base}${line}/Park_score.txt
#  python ${scorer_cat} shopping_complex ${gold_dir}Shopping_Complex_dist.jsonl ${sys_dir_base}${line}/Shopping_Complex.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/shopping_complex/;' > ${out_dir_base}${line}/Shopping_Complex_score.txt
#  python ${scorer_cat} sports_facility ${gold_dir}Sports_Facility_dist.jsonl ${sys_dir_base}${line}/Sports_Facility.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/sports_facility/;' > ${out_dir_base}${line}/Sports_Facility_score.txt
#  python ${scorer_cat} museum ${gold_dir}Museum_dist.jsonl ${sys_dir_base}${line}/Museum.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/museum/;' > ${out_dir_base}${line}/Museum_score.txt
#  python ${scorer_cat} zoo ${gold_dir}Zoo_dist.jsonl ${sys_dir_base}${line}/Zoo.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/zoo/;' > ${out_dir_base}${line}/Zoo_score.txt
#  python ${scorer_cat} amusement_park ${gold_dir}Amusement_Park_dist.jsonl ${sys_dir_base}${line}/Amusement_Park.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/amusement_park/;' > ${out_dir_base}${line}/Amusement_Park_score.txt
#  python ${scorer_cat} theater ${gold_dir}Theater_dist.jsonl ${sys_dir_base}${line}/Theater.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/theater/;' > ${out_dir_base}${line}/Theater_score.txt
#  python ${scorer_cat} worship_place ${gold_dir}Worship_Place_dist.jsonl ${sys_dir_base}${line}/Worship_Place.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/worship_place/;' > ${out_dir_base}${line}/Worship_Place_score.txt
#  python ${scorer_cat} car_stop ${gold_dir}Car_Stop_dist.jsonl ${sys_dir_base}${line}/Car_Stop.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/car_stop/;' > ${out_dir_base}${line}/Car_Stop_score.txt
#  python ${scorer_cat} station ${gold_dir}Station_dist.jsonl ${sys_dir_base}${line}/Station.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/station/;' > ${out_dir_base}${line}/Station_score.txt
#  python ${scorer_cat} airport ${gold_dir}Airport_dist.jsonl ${sys_dir_base}${line}/Airport.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/airport/;' > ${out_dir_base}${line}/Airport_score.txt
#  python ${scorer_cat} port ${gold_dir}Port_dist.jsonl ${sys_dir_base}${line}/Port.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/port/;' > ${out_dir_base}${line}/Port_score.txt
#  python ${scorer_cat} road_facility ${gold_dir}Road_Facility_dist.jsonl ${sys_dir_base}${line}/Road_Facility.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/road_facility/;' > ${out_dir_base}${line}/Road_Facility_score.txt
#  python ${scorer_cat} railway_facility ${gold_dir}Railway_Facility_dist.jsonl ${sys_dir_base}${line}/Railway_Facility.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/railway_facility/;' > ${out_dir_base}${line}/Railway_Facility_score.txt
#  python ${scorer_cat} line_other ${gold_dir}Line_Other_dist.jsonl ${sys_dir_base}${line}/Line_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/line_other/;' > ${out_dir_base}${line}/Line_Other_score.txt
#  python ${scorer_cat} road ${gold_dir}Road_dist.jsonl ${sys_dir_base}${line}/Road.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/road/;' > ${out_dir_base}${line}/Road_score.txt
#  python ${scorer_cat} railroad ${gold_dir}Railroad_dist.jsonl ${sys_dir_base}${line}/Railroad.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/railroad/;' > ${out_dir_base}${line}/Railroad_score.txt
#  python ${scorer_cat} water_route ${gold_dir}Water_Route_dist.jsonl ${sys_dir_base}${line}/Water_Route.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/water_route/;' > ${out_dir_base}${line}/Water_Route_score.txt
#  python ${scorer_cat} canal ${gold_dir}Canal_dist.jsonl ${sys_dir_base}${line}/Canal.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/canal/;' > ${out_dir_base}${line}/Canal_score.txt
#  python ${scorer_cat} tunnel ${gold_dir}Tunnel_dist.jsonl ${sys_dir_base}${line}/Tunnel.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/tunnel/;' > ${out_dir_base}${line}/Tunnel_score.txt
#  python ${scorer_cat} bridge ${gold_dir}Bridge_dist.jsonl ${sys_dir_base}${line}/Bridge.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/bridge/;' > ${out_dir_base}${line}/Bridge_score.txt
#  python ${scorer_cat} product_other ${gold_dir}Product_Other_dist.jsonl ${sys_dir_base}${line}/Product_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/product_other/;' > ${out_dir_base}${line}/Product_Other_score.txt
#  python ${scorer_cat} service ${gold_dir}Service_dist.jsonl ${sys_dir_base}${line}/Service.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/service/;' > ${out_dir_base}${line}/Service_score.txt
#  python ${scorer_cat} brand ${gold_dir}Brand_dist.jsonl ${sys_dir_base}${line}/Brand.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/brand/;' > ${out_dir_base}${line}/Brand_score.txt
#  python ${scorer_cat} software ${gold_dir}Software_dist.jsonl ${sys_dir_base}${line}/Software.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/software/;' > ${out_dir_base}${line}/Software_score.txt
#  python ${scorer_cat} information_appliance ${gold_dir}Information_Appliance_dist.jsonl ${sys_dir_base}${line}/Information_Appliance.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/information_appliance/;' > ${out_dir_base}${line}/Information_Appliance_score.txt
#  python ${scorer_cat} toy ${gold_dir}Toy_dist.jsonl ${sys_dir_base}${line}/Toy.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/toy/;' > ${out_dir_base}${line}/Toy_score.txt
#  python ${scorer_cat} musical_instrument ${gold_dir}Musical_Instrument_dist.jsonl ${sys_dir_base}${line}/Musical_Instrument.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/musical_instrument/;' > ${out_dir_base}${line}/Musical_Instrument_score.txt
#  python ${scorer_cat} drug ${gold_dir}Drug_dist.jsonl ${sys_dir_base}${line}/Drug.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/drug/;' > ${out_dir_base}${line}/Drug_score.txt
#  python ${scorer_cat} character ${gold_dir}Character_dist.jsonl ${sys_dir_base}${line}/Character.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/character/;' > ${out_dir_base}${line}/Character_score.txt
#  python ${scorer_cat} art_other ${gold_dir}Art_Other_dist.jsonl ${sys_dir_base}${line}/Art_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/art_other/;' > ${out_dir_base}${line}/Art_Other_score.txt
#  python ${scorer_cat} painting ${gold_dir}Painting_dist.jsonl ${sys_dir_base}${line}/Painting.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/painting/;' > ${out_dir_base}${line}/Painting_score.txt
#  python ${scorer_cat} broadcast_program ${gold_dir}Broadcast_Program_dist.jsonl ${sys_dir_base}${line}/Broadcast_Program.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/broadcast_program/;' > ${out_dir_base}${line}/Broadcast_Program_score.txt
#  python ${scorer_cat} movie ${gold_dir}Movie_dist.jsonl ${sys_dir_base}${line}/Movie.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/movie/;' > ${out_dir_base}${line}/Movie_score.txt
#  python ${scorer_cat} show ${gold_dir}Show_dist.jsonl ${sys_dir_base}${line}/Show.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/show/;' > ${out_dir_base}${line}/Show_score.txt
#  python ${scorer_cat} music ${gold_dir}Music_dist.jsonl ${sys_dir_base}${line}/Music.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/music/;' > ${out_dir_base}${line}/Music_score.txt
#  python ${scorer_cat} video_work ${gold_dir}Video_Work_dist.jsonl ${sys_dir_base}${line}/Video_Work.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/video_work/;' > ${out_dir_base}${line}/Video_Work_score.txt
#  python ${scorer_cat} printing_other ${gold_dir}Printing_Other_dist.jsonl ${sys_dir_base}${line}/Printing_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/printing_other/;' > ${out_dir_base}${line}/Printing_Other_score.txt
#  python ${scorer_cat} newspaper ${gold_dir}Newspaper_dist.jsonl ${sys_dir_base}${line}/Newspaper.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/newspaper/;' > ${out_dir_base}${line}/Newspaper_score.txt
#  python ${scorer_cat} magazine ${gold_dir}Magazine_dist.jsonl ${sys_dir_base}${line}/Magazine.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/magazine/;' > ${out_dir_base}${line}/Magazine_score.txt
#  python ${scorer_cat} book ${gold_dir}Book_dist.jsonl ${sys_dir_base}${line}/Book.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/book/;' > ${out_dir_base}${line}/Book_score.txt
#  python ${scorer_cat} game_other ${gold_dir}Game_Other_dist.jsonl ${sys_dir_base}${line}/Game_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/game_other/;' > ${out_dir_base}${line}/Game_Other_score.txt
#  python ${scorer_cat} digital_game ${gold_dir}Digital_Game_dist.jsonl ${sys_dir_base}${line}/Digital_Game.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/digital_game/;' > ${out_dir_base}${line}/Digital_Game_score.txt
#  python ${scorer_cat} food_other ${gold_dir}Food_Other_dist.jsonl ${sys_dir_base}${line}/Food_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/food_other/;' > ${out_dir_base}${line}/Food_Other_score.txt
#  python ${scorer_cat} dish ${gold_dir}Dish_dist.jsonl ${sys_dir_base}${line}/Dish.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/dish/;' > ${out_dir_base}${line}/Dish_score.txt
#  python ${scorer_cat} weapon_other ${gold_dir}Weapon_Other_dist.jsonl ${sys_dir_base}${line}/Weapon_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/weapon_other/;' > ${out_dir_base}${line}/Weapon_Other_score.txt
#  python ${scorer_cat} firearms ${gold_dir}Firearms_dist.jsonl ${sys_dir_base}${line}/Firearms.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/firearms/;' > ${out_dir_base}${line}/Firearms_score.txt
#  python ${scorer_cat} vehicle_other ${gold_dir}Vehicle_Other_dist.jsonl ${sys_dir_base}${line}/Vehicle_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/vehicle_other/;' > ${out_dir_base}${line}/Vehicle_Other_score.txt
#  python ${scorer_cat} car ${gold_dir}Car_dist.jsonl ${sys_dir_base}${line}/Car.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/car/;' > ${out_dir_base}${line}/Car_score.txt
#  python ${scorer_cat} train ${gold_dir}Train_dist.jsonl ${sys_dir_base}${line}/Train.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/train/;' > ${out_dir_base}${line}/Train_score.txt
#  python ${scorer_cat} aircraft ${gold_dir}Aircraft_dist.jsonl ${sys_dir_base}${line}/Aircraft.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/aircraft/;' > ${out_dir_base}${line}/Aircraft_score.txt
#  python ${scorer_cat} ship ${gold_dir}Ship_dist.jsonl ${sys_dir_base}${line}/Ship.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/ship/;' > ${out_dir_base}${line}/Ship_score.txt
#  python ${scorer_cat} spaceship ${gold_dir}Spaceship_dist.jsonl ${sys_dir_base}${line}/Spaceship.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/spaceship/;' > ${out_dir_base}${line}/Spaceship_score.txt
#  python ${scorer_cat} military_vehicle ${gold_dir}Military_Vehicle_dist.jsonl ${sys_dir_base}${line}/Military_Vehicle.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/military_vehicle/;' > ${out_dir_base}${line}/Military_Vehicle_score.txt
#  python ${scorer_cat} military_aircraft ${gold_dir}Military_Aircraft_dist.jsonl ${sys_dir_base}${line}/Military_Aircraft.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/military_aircraft/;' > ${out_dir_base}${line}/Military_Aircraft_score.txt
#  python ${scorer_cat} military_ship ${gold_dir}Military_Ship_dist.jsonl ${sys_dir_base}${line}/Military_Ship.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/military_ship/;' > ${out_dir_base}${line}/Military_Ship_score.txt
#  python ${scorer_cat} doctrine_method_other ${gold_dir}Doctrine_Method_Other_dist.jsonl ${sys_dir_base}${line}/Doctrine_Method_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/doctrine_method_other/;' > ${out_dir_base}${line}/Doctrine_Method_Other_score.txt
#  python ${scorer_cat} offense ${gold_dir}Offense_dist.jsonl ${sys_dir_base}${line}/Offense.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/offense/;' > ${out_dir_base}${line}/Offense_score.txt
#  python ${scorer_cat} award ${gold_dir}Award_dist.jsonl ${sys_dir_base}${line}/Award.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/award/;' > ${out_dir_base}${line}/Award_score.txt
#  python ${scorer_cat} decoration ${gold_dir}Decoration_dist.jsonl ${sys_dir_base}${line}/Decoration.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/decoration/;' > ${out_dir_base}${line}/Decoration_score.txt
#  python ${scorer_cat} money_form ${gold_dir}Money_Form_dist.jsonl ${sys_dir_base}${line}/Money_Form.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/money_form/;' > ${out_dir_base}${line}/Money_Form_score.txt
#  python ${scorer_cat} technology ${gold_dir}Technology_dist.jsonl ${sys_dir_base}${line}/Technology.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/technology/;' > ${out_dir_base}${line}/Technology_score.txt
#  python ${scorer_cat} standard ${gold_dir}Standard_dist.jsonl ${sys_dir_base}${line}/Standard.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/standard/;' > ${out_dir_base}${line}/Standard_score.txt
#  python ${scorer_cat} system ${gold_dir}System_dist.jsonl ${sys_dir_base}${line}/System.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/system/;' > ${out_dir_base}${line}/System_score.txt
#  python ${scorer_cat} examination ${gold_dir}Examination_dist.jsonl ${sys_dir_base}${line}/Examination.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/examination/;' > ${out_dir_base}${line}/Examination_score.txt
#  python ${scorer_cat} doctrine_thought ${gold_dir}Doctrine_Thought_dist.jsonl ${sys_dir_base}${line}/Doctrine_Thought.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/doctrine_thought/;' > ${out_dir_base}${line}/Doctrine_Thought_score.txt
#  python ${scorer_cat} culture ${gold_dir}Culture_dist.jsonl ${sys_dir_base}${line}/Culture.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/culture/;' > ${out_dir_base}${line}/Culture_score.txt
#  python ${scorer_cat} religion ${gold_dir}Religion_dist.jsonl ${sys_dir_base}${line}/Religion.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/religion/;' > ${out_dir_base}${line}/Religion_score.txt
#  python ${scorer_cat} academic ${gold_dir}Academic_dist.jsonl ${sys_dir_base}${line}/Academic.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/academic/;' > ${out_dir_base}${line}/Academic_score.txt
#  python ${scorer_cat} theory ${gold_dir}Theory_dist.jsonl ${sys_dir_base}${line}/Theory.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/theory/;' > ${out_dir_base}${line}/Theory_score.txt
#  python ${scorer_cat} style ${gold_dir}Style_dist.jsonl ${sys_dir_base}${line}/Style.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/style/;' > ${out_dir_base}${line}/Style_score.txt
#  python ${scorer_cat} sport ${gold_dir}Sport_dist.jsonl ${sys_dir_base}${line}/Sport.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/sport/;' > ${out_dir_base}${line}/Sport_score.txt
#  python ${scorer_cat} plan ${gold_dir}Plan_dist.jsonl ${sys_dir_base}${line}/Plan.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/plan/;' > ${out_dir_base}${line}/Plan_score.txt
#  python ${scorer_cat} rule_other ${gold_dir}Rule_Other_dist.jsonl ${sys_dir_base}${line}/Rule_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/rule_other/;' > ${out_dir_base}${line}/Rule_Other_score.txt
#  python ${scorer_cat} treaty ${gold_dir}Treaty_dist.jsonl ${sys_dir_base}${line}/Treaty.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/treaty/;' > ${out_dir_base}${line}/Treaty_score.txt
#  python ${scorer_cat} law ${gold_dir}Law_dist.jsonl ${sys_dir_base}${line}/Law.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/law/;' > ${out_dir_base}${line}/Law_score.txt
#  python ${scorer_cat} position_vocation ${gold_dir}Position_Vocation_dist.jsonl ${sys_dir_base}${line}/Position_Vocation.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/position_vocation/;' > ${out_dir_base}${line}/Position_Vocation_score.txt
#  python ${scorer_cat} language_other ${gold_dir}Language_Other_dist.jsonl ${sys_dir_base}${line}/Language_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/language_other/;' > ${out_dir_base}${line}/Language_Other_score.txt
#  python ${scorer_cat} national_language ${gold_dir}National_Language_dist.jsonl ${sys_dir_base}${line}/National_Language.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/national_language/;' > ${out_dir_base}${line}/National_Language_score.txt
#  python ${scorer_cat} currency ${gold_dir}Currency_dist.jsonl ${sys_dir_base}${line}/Currency.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/currency/;' > ${out_dir_base}${line}/Currency_score.txt
#  python ${scorer_cat} virtual_address_other ${gold_dir}Virtual_Address_Other_dist.jsonl ${sys_dir_base}${line}/Virtual_Address_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/virtual_address_other/;' > ${out_dir_base}${line}/Virtual_Address_Other_score.txt
#  python ${scorer_cat} channel ${gold_dir}Channel_dist.jsonl ${sys_dir_base}${line}/Channel.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/channel/;' > ${out_dir_base}${line}/Channel_score.txt
#  python ${scorer_cat} event_other ${gold_dir}Event_Other_dist.jsonl ${sys_dir_base}${line}/Event_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/event_other/;' > ${out_dir_base}${line}/Event_Other_score.txt
#  python ${scorer_cat} natural_phenomenon ${gold_dir}Natural_Phenomenon_dist.jsonl ${sys_dir_base}${line}/Natural_Phenomenon.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/natural_phenomenon/;' > ${out_dir_base}${line}/Natural_Phenomenon_score.txt
#  python ${scorer_cat} natural_disaster_other ${gold_dir}Natural_Disaster_Other_dist.jsonl ${sys_dir_base}${line}/Natural_Disaster_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/natural_disaster_other/;' > ${out_dir_base}${line}/Natural_Disaster_Other_score.txt
#  python ${scorer_cat} earthquake ${gold_dir}Earthquake_dist.jsonl ${sys_dir_base}${line}/Earthquake.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/earthquake/;' > ${out_dir_base}${line}/Earthquake_score.txt
#  python ${scorer_cat} flood_damage ${gold_dir}Flood_Damage_dist.jsonl ${sys_dir_base}${line}/Flood_Damage.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/flood_damage/;' > ${out_dir_base}${line}/Flood_Damage_score.txt
#  python ${scorer_cat} occasion_other ${gold_dir}Occasion_Other_dist.jsonl ${sys_dir_base}${line}/Occasion_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/occasion_other/;' > ${out_dir_base}${line}/Occasion_Other_score.txt
#  python ${scorer_cat} religious_festival ${gold_dir}Religious_Festival_dist.jsonl ${sys_dir_base}${line}/Religious_Festival.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/religious_festival/;' > ${out_dir_base}${line}/Religious_Festival_score.txt
#  python ${scorer_cat} election ${gold_dir}Election_dist.jsonl ${sys_dir_base}${line}/Election.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/election/;' > ${out_dir_base}${line}/Election_score.txt
#  python ${scorer_cat} competition ${gold_dir}Competition_dist.jsonl ${sys_dir_base}${line}/Competition.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/competition/;' > ${out_dir_base}${line}/Competition_score.txt
#  python ${scorer_cat} exhibition ${gold_dir}Exhibition_dist.jsonl ${sys_dir_base}${line}/Exhibition.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/exhibition/;' > ${out_dir_base}${line}/Exhibition_score.txt
#  python ${scorer_cat} conference ${gold_dir}Conference_dist.jsonl ${sys_dir_base}${line}/Conference.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/conference/;' > ${out_dir_base}${line}/Conference_score.txt
#  python ${scorer_cat} incident_other ${gold_dir}Incident_Other_dist.jsonl ${sys_dir_base}${line}/Incident_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/incident_other/;' > ${out_dir_base}${line}/Incident_Other_score.txt
#  python ${scorer_cat} traffic_accident ${gold_dir}Traffic_Accident_dist.jsonl ${sys_dir_base}${line}/Traffic_Accident.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/traffic_accident/;' > ${out_dir_base}${line}/Traffic_Accident_score.txt
#  python ${scorer_cat} political_incident ${gold_dir}Political_Incident_dist.jsonl ${sys_dir_base}${line}/Political_Incident.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/political_incident/;' > ${out_dir_base}${line}/Political_Incident_score.txt
#  python ${scorer_cat} war ${gold_dir}War_dist.jsonl ${sys_dir_base}${line}/War.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/war/;' > ${out_dir_base}${line}/War_score.txt
#  python ${scorer_cat} natural_object_other ${gold_dir}Natural_Object_Other_dist.jsonl ${sys_dir_base}${line}/Natural_Object_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/natural_object_other/;' > ${out_dir_base}${line}/Natural_Object_Other_score.txt
#  python ${scorer_cat} compound ${gold_dir}Compound_dist.jsonl ${sys_dir_base}${line}/Compound.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/compound/;' > ${out_dir_base}${line}/Compound_score.txt
#  python ${scorer_cat} mineral ${gold_dir}Mineral_dist.jsonl ${sys_dir_base}${line}/Mineral.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/mineral/;' > ${out_dir_base}${line}/Mineral_score.txt
#  python ${scorer_cat} living_thing_other ${gold_dir}Living_Thing_Other_dist.jsonl ${sys_dir_base}${line}/Living_Thing_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/living_thing_other/;' > ${out_dir_base}${line}/Living_Thing_Other_score.txt
#  python ${scorer_cat} fictional_species ${gold_dir}Fictional_Species_dist.jsonl ${sys_dir_base}${line}/Fictional_Species.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/fictional_species/;' > ${out_dir_base}${line}/Fictional_Species_score.txt
#  python ${scorer_cat} bacteria_virus ${gold_dir}Bacteria_Virus_dist.jsonl ${sys_dir_base}${line}/Bacteria_Virus.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/bacteria_virus/;' > ${out_dir_base}${line}/Bacteria_Virus_score.txt
#  python ${scorer_cat} fungus ${gold_dir}Fungus_dist.jsonl ${sys_dir_base}${line}/Fungus.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/fungus/;' > ${out_dir_base}${line}/Fungus_score.txt
#  python ${scorer_cat} mollusk ${gold_dir}Mollusk_dist.jsonl ${sys_dir_base}${line}/Mollusk.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/mollusk/;' > ${out_dir_base}${line}/Mollusk_score.txt
#  python ${scorer_cat} arthropod ${gold_dir}Arthropod_dist.jsonl ${sys_dir_base}${line}/Arthropod.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/arthropod/;' > ${out_dir_base}${line}/Arthropod_score.txt
#  python ${scorer_cat} insect ${gold_dir}Insect_dist.jsonl ${sys_dir_base}${line}/Insect.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/insect/;' > ${out_dir_base}${line}/Insect_score.txt
#  python ${scorer_cat} fish ${gold_dir}Fish_dist.jsonl ${sys_dir_base}${line}/Fish.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/fish/;' > ${out_dir_base}${line}/Fish_score.txt
#  python ${scorer_cat} amphibia ${gold_dir}Amphibia_dist.jsonl ${sys_dir_base}${line}/Amphibia.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/amphibia/;' > ${out_dir_base}${line}/Amphibia_score.txt
#  python ${scorer_cat} dinosaur ${gold_dir}Dinosaur_dist.jsonl ${sys_dir_base}${line}/Dinosaur.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/dinosaur/;' > ${out_dir_base}${line}/Dinosaur_score.txt
#  python ${scorer_cat} reptile ${gold_dir}Reptile_dist.jsonl ${sys_dir_base}${line}/Reptile.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/reptile/;' > ${out_dir_base}${line}/Reptile_score.txt
#  python ${scorer_cat} bird ${gold_dir}Bird_dist.jsonl ${sys_dir_base}${line}/Bird.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/bird/;' > ${out_dir_base}${line}/Bird_score.txt
#  python ${scorer_cat} mammal ${gold_dir}Mammal_dist.jsonl ${sys_dir_base}${line}/Mammal.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/mammal/;' > ${out_dir_base}${line}/Mammal_score.txt
#  python ${scorer_cat} flora ${gold_dir}Flora_dist.jsonl ${sys_dir_base}${line}/Flora.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/flora/;' > ${out_dir_base}${line}/Flora_score.txt
#  python ${scorer_cat} living_thing_part_other ${gold_dir}Living_Thing_Part_Other_dist.jsonl ${sys_dir_base}${line}/Living_Thing_Part_Other.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/living_thing_part_other/;' > ${out_dir_base}${line}/Living_Thing_Part_Other_score.txt
#  python ${scorer_cat} animal_part ${gold_dir}Animal_Part_dist.jsonl ${sys_dir_base}${line}/Animal_Part.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/animal_part/;' > ${out_dir_base}${line}/Animal_Part_score.txt
#  python ${scorer_cat} flora_part ${gold_dir}Flora_Part_dist.jsonl ${sys_dir_base}${line}/Flora_Part.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/flora_part/;' > ${out_dir_base}${line}/Flora_Part_score.txt
#  python ${scorer_cat} animal_disease ${gold_dir}Animal_Disease_dist.jsonl ${sys_dir_base}${line}/Animal_Disease.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/animal_disease/;' > ${out_dir_base}${line}/Animal_Disease_score.txt
#  python ${scorer_cat} color ${gold_dir}Color_dist.jsonl ${sys_dir_base}${line}/Color.jsonl ${attr_type} --ignore-link-type| perl -pe 's/^/color/;' > ${out_dir_base}${line}/Color_score.txt
# till here
  #
#  python ${scorer_cat} airport ${gold_dir}Airport_dist.jsonl ${sys_dir_base}${line}/Airport.jsonl ${attr_type} --ignore-link-type | perl -pe 's/^/Airport /;' | perl -pe 's/^Airport precision/cat precision/' > ${out_dir_base}${line}/Airport_score.txt
#  python ${scorer_cat} city ${gold_dir}City_dist.jsonl ${sys_dir_base}${line}/City.jsonl ${attr_type} --ignore-link-type | perl -pe 's/^/City /;'| perl -pe 's/^City precision/cat precision/'> ${out_dir_base}${line}/City_score.txt
#  python ${scorer_cat} company ${gold_dir}Company_dist.jsonl ${sys_dir_base}${line}/Company.jsonl ${attr_type} --ignore-link-type | perl -pe 's/^/Company /;' | perl -pe 's/^Company precision/cat precision/' > ${out_dir_base}${line}/Company_score.txt
#  python ${scorer_cat} compound ${gold_dir}Compound_dist.jsonl ${sys_dir_base}${line}/Compound.jsonl ${attr_type} --ignore-link-type | perl -pe 's/^/Compound /;' | perl -pe 's/^Compound precision/cat precision/' > ${out_dir_base}${line}/Compound_score.txt
#  python ${scorer_cat} conference ${gold_dir}Conference_dist.jsonl ${sys_dir_base}${line}/Conference.jsonl ${attr_type} --ignore-link-type | perl -pe 's/^/Conference /;' | perl -pe 's/^Conference precision/cat precision/' > ${out_dir_base}${line}/Conference_score.txt
#  python ${scorer_cat} person ${gold_dir}Person_dist.jsonl ${sys_dir_base}${line}/Person.jsonl ${attr_type} --ignore-link-type | perl -pe 's/^/Person /;' | perl -pe 's/^Person precision/cat precision/' > ${out_dir_base}${line}/Person_score.txt
#  python ${scorer_cat} lake ${gold_dir}Lake_dist.jsonl ${sys_dir_base}${line}/Lake.jsonl ${attr_type} --ignore-link-type | perl -pe 's/^/Lake /;' | perl -pe 's/^Lake precision/cat precision/' > ${out_dir_base}${line}/Lake_score.txt
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


