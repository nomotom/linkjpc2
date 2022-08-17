#!/bin/sh -x
now=`date +%Y%m%d%H%M%S`
script="./linkjpc.py"
common_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/common/"
tmp_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/leaderboard/"
in_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/leaderboard/ene_annotation/"
#gold_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/link_annotation/"
#out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/leaderboard_out/20211010/"
out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/leaderboard_out/final_rev4"

out_dir_tmp_base="/Users/masako/tmp/leaderboard/20211010/"
setting_dir="${out_dir_base}setting/"
#########################
#eval_target="./eval_target_sample"
#eval_script="./linkjpc_eval_sample.sh"
#####################

#sample dataの結果がよかったもの　2021/10/10
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_l_06_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink frp -l_min 0.6 -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_l_06_attr_w_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink frp -l_min 0.6 -ar_tgt w -bl_tgt w -i_tgt w -i_max 5 -i_type f
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_l_06_attr_w_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink rp -l_min 0.6 -ar_tgt w -bl_tgt w -i_tgt w -i_max 5 -i_type f

#sample dataの結果がよかったもの 2021/10/9
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_l_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_l_attr_w_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt w -i_tgt w -i_max 5 -i_type f
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_l_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink rp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f


## AIPCB_CBI
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_incl_m_imax1_o/ --mod m -f i --mint p -i_tgt m -i_max 1 -i_type o
#
## AIPRB_SMW
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_frp_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
#
## AIPRB_WSM
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink__mint_e_attr_w/ --mod w:s:m -f a --mint e --wlink frp -ar_tgt w

