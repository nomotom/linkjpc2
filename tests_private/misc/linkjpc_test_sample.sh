#!/bin/sh -x
now=`date +%Y%m%d%H%M%S`
script="./linkjpc.py"
common_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/common/"
tmp_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/sample/"


in_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/ene_annotation/"
gold_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/link_annotation/"
#out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20211004/"
eval_target="./eval_target_sample.txt"
out_dir_tmp_base="/Users/masako/tmp/sample/tmp_test/"

setting_dir="${out_dir_base}setting/"


#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_incl_m_imax1_o/ --mod m -f i --mint p -i_tgt m -i_max 1 -i_type o
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_incl_m_imax1_f/ --mod m -f i --mint p -i_tgt m -i_max 1 -i_type f
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}mint_p_incl_m_imax3_a/ --mod m -f i --mint p -i_tgt m -i_max 3 -i_type a
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}mint_p_incl_m_imax3_o/ --mod m -f i --mint p -i_tgt m -i_max 3 -i_type o


#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}mint_e_slink05_wlink_frp_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod msw -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f


#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}tinm_p_incl_t_imax5/ --mod t -f i --tinm p -i_tgt t -i_type f -i_max 5



#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}slink05_mod/ --mod s -f n -s_min 0.5 -s_prb mod
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}mint_e_slink05_raw/ --mod ms -f n --mint e -s_min 0.5 -s_prb raw

#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_attr_m_anc09_ang01_al_am/ --mod m -f a --mint p -ar_tgt m -anc 0.9 -ang 0.1 -al am
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_attr_m_anc09_ang01_al_ar/ --mod m -f a --mint p -ar_tgt m -anc 0.9 -ang 0.1 -al ar


#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}wlink_r/ --mod w -f n --wlink r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}wlink_rl/ --mod w -f n --wlink rl

#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_attr_m_anc09_ang00_al_r/ --mod m -f a --mint p -ar_tgt m -anc 0.9 -ang 0.0 -al r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_attr_m_anc09_ang00/ --mod m -f a --mint p -ar_tgt m -anc 0.9 -ang 0.0 -al n

#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}mint_e_slink05_wlink_rpl_l_attr_msw_anc09_ang01_bl_sw_incl_sw/ --mod mswl -f abi --mint e -s_min 0.5 --wlink rpl -ar_tgt msw -anc 0.9 -ang 0.1 -bl_tgt sw -i_tgt sw


#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}mint_e_trim_attr_m_anc09_ang01/ --mod m -f a --mint e -tm trim -ar_tgt m -anc 0.9
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}mint_e_trim_attr_m_anc03/ --mod m -f a --mint e -tm trim -ar_tgt m -anc 0.3
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}mint_p_attr_m_anc03/ --mod m -f a --mint p -ar_tgt m -anc 0.3
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}mint_p_attr_m_anc09/ --mod m -f a --mint p -ar_tgt m -anc 0.9
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}wlink_m/ --mod w -f n --wlink m
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}wlink_m_attr_w_anc03/ --mod w -f a --wlink m -ar_tgt w -anc 0.3
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}wlink_m_attr_w_anc09/ --mod w -f a --wlink m -ar_tgt w -anc 0.9
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}wlink_r_attr_w_anc03/ --mod w --wlink r -f a -ar_tgt w -anc 0.9
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}wlink_r_attr_w_anc09/ --mod w --wlink r -f a -ar_tgt w -anc 0.9
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}wlink_rp_attr_w_anc03/ --mod w -f a --wlink rp -ar_tgt w -anc 0.3
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}wlink_rp_attr_w_anc09/ --mod w -f a --wlink rp -ar_tgt w -anc 0.9
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}wlink_rpl_attr_w_anc03/ --mod w -f a --wlink rpl -ar_tgt w -anc 0.3
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}wlink_rpl_attr_w_anc09/ --mod w -f a --wlink rpl -ar_tgt w -anc 0.9
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}wlink_u_attr_w_anc03/ --mod w -f a --wlink u -ar_tgt w -anc 0.3
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}wlink_u_attr_w_anc09/ --mod w -f a --wlink u -ar_tgt w -anc 0.9

#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p/ --mod m -f n --mint p


#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp_attr_w_anc03/ --mod w -f a --wlink rp -ar_tgt w -anc 0.3

#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_attr_m_anc05/ --mod m -f a --mint e -tm trim -ar_tgt m -anc 0.5
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_attr_m_anc09/ --mod m -f a --mint e -tm trim -ar_tgt m -anc 0.9
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_attr_m_anc09/ --mod m -f a --mint p -tm trim -ar_tgt m -anc 0.9
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_attr_m_anc05/ --mod m -f a --mint p -tm trim -ar_tgt m -anc 0.5

#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim/ --mod m -f n --mint p -tm trim

#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r/ --mod w -f n --wlink r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl/ --mod w -f n --wlink rl
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp/ --mod w -f n --wlink rp

#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e/ --mod t -f n --tinm e

#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e/ --mod m -f n --mint e


#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}wlink_rp_attr_w_anc07/ --mod w -f a --wlink rp -ar_tgt w -anc 0.7
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}wlink_rp_attr_w_anc09/ --mod w -f a --wlink rp -ar_tgt w -anc 0.9
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}wlink_rp_attr_w_anc05/ --mod w -f a --wlink rp -ar_tgt w -anc 0.5

#wlink
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}wlink_rpl/ --mod w -f n --wlink rpl
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_tmp_base}wlink_rpl_bl_w/ --mod w -f b --wlink rpl -bl_tgt w
