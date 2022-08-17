#!/bin/bash
script="./linkjpc/linkjpc.py"
base_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/"
base_data_dir="${base_dir}Download/"
common_data_dir="${base_data_dir}ljc_data/common/"
tmp_data_dir="${base_data_dir}ljc_data/test/"
in_dir="${base_data_dir}linkjp-eval-211027/ene_annotation/"
out_dir_base="${base_dir}test_out/exp_multi/"

# cf. github公開版
#script="./linkjpc/linkjpc_org.py"
#base_dir="/XXXX/XXXX/2021-LinkJP/"
#base_data_dir="${base_dir}Download/"
#common_data_dir="${base_data_dir}ljc_data/common/"
#tmp_data_dir="${base_data_dir}ljc_data/test/"
#in_dir="${base_data_dir}linkjp-eval-211027/ene_annotation/"
#out_dir_base="${base_dir}test_out/sample/"

## mint のみ
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_amax_10M_cmax_10M/ -a_max 10000000 --mod m --mint e -c_max 10000000
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_amax_10M_cmax_10M/ -a_max 10000000 --mod m --mint e -c_max 10000000
#
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_amax_10M_cmax_10M/ -a_max 10000000 --mod m --mint p -c_max 10000000
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_10M_cmax_10M/ -a_max 10000000 --mod m --mint p -tmt -c_max 10000000
#
#
## tinm のみ
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_amax_10M_cmax_10M/ -a_max 10000000 --mod t --tinm e -c_max 10000000
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_trim_amax_10M_cmax_10M/ -a_max 10000000 --mod t --tinm e -tmt -c_max 10000000
#
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_amax_10M_cmax_10M/ -a_max 10000000 --mod t --tinm p -c_max 10000000
#
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_amax_10M_cmax_10M/ -a_max 10000000 --mod t --tinm p -tmt -c_max 10000000
#
### selflinkのみ
### rawとfixedの中間
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_04_mid_amax_10M/ -a_max 10000000 --mod s -s_min 0.4 -s_prb mid
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid_amax_10M/ -a_max 10000000 --mod s -s_min 0.5 -s_prb mid
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_06_mid_amax_10M/ -a_max 10000000 --mod s -s_min 0.6 -s_prb mid
##
### サンプルデータのratioそのまま
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_04_raw_amax_10M/ -a_max 10000000 --mod s -s_min 0.4 -s_prb raw
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_raw_amax_10M/ -a_max 10000000 --mod s -s_min 0.5 -s_prb raw
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_06_raw_amax_10M/ -a_max 10000000 --mod s -s_min 0.6 -s_prb raw
##
### 全て1.0とする  04 = 05 > 06
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_04_fixed_amax_10M/ -a_max 10000000 --mod s -s_min 0.4 -s_prb fixed
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_fixed_amax_10M/ -a_max 10000000 --mod s -s_min 0.5 -s_prb fixed
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_06_fixed_amax_10M/ -a_max 10000000 --mod s -s_min 0.6 -s_prb fixed
#
## wlinkのみ r = fr > m > f
## mention内同スコア
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_m_amax_10M_nobreak/ -a_max 10000000 --mod w --wlink m --no-wl_break
## mention内最右により加点
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_amax_10M_nobreak/ -a_max 10000000 --mod w --wlink r --no-wl_break
## mention内最初により加点
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_amax_10M_nobreak/ -a_max 10000000 --mod w --wlink f --no-wl_break
## mention内最初と最右により加点
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fr_amax_10M_nobreak/ -a_max 10000000 --mod w --wlink fr --no-wl_break

# linkprobのみ 03 = 04 = 05 > 07 > 09 > 10
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_03_10M/ -a_max 10000000 --mod l -l_min 0.3
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_04_10M/ -a_max 10000000 --mod l -l_min 0.4
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_05_10M/ -a_max 10000000 --mod l -l_min 0.5
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_06_10M/ -a_max 10000000 --mod l -l_min 0.6
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_07_10M/ -a_max 10000000 --mod l -l_min 0.7
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_09_10M/ -a_max 10000000 --mod l -l_min 0.9
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_10_10M/ -a_max 10000000 --mod l -l_min 1.0

# AIPCB_CBI
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_cmax_10M_incl_m_imax_1_o_10M/ -a_max 10000000 --mod m -f i --mint p -i_tgt m -i_max 1 -i_type o -c_max 10000000
#### AIPRB_WSM
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink__mint_e_cmax_10M_attr_w_amax_10M/ -a_max 10000000 --mod w:s:m -f a --mint e --wlink frp -ar_tgt w -c_max 10000000
## AIPRB_SWM
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e_cmax_10M__wlink_frp_attr_w_al_am_bl_w_amax_10M/ -a_max 10000000 --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w -c_max 10000000


###################
#
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_frp_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
#
#
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_br_09_fr_09/ --mod w -f n --wlink l -wl_bca r -wl_bca_ratio 0.9 -wl_fca r -wl_fca_ratio 0.9
#
######
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rpl_amax_1K/ --mod w -f n --wlink rpl -a_max 1000
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl_amax_1K/ --mod w -f n --wlink frpl -a_max 1000
##
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_amax_1K/ --mod w -f n --wlink f  -a_max 1000
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fr_amax_1K/ --mod w -f n --wlink fr  -a_max 1000
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_amax_1K/ --mod w -f n --wlink r -a_max 1000
##
##
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_frpl_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frpl -ar_tgt w -al am -bl_tgt w
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl__slink__mint_e_attr_w/ --mod w:s:m -f a --mint e --wlink frpl -ar_tgt w
##
#
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl_wln_02_wlp_03_wls_05/ --mod w -f n --wlink frpl -wln 0.2 -wlp 0.3 -wls 0.5
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fl/ --mod w -f n --wlink fl
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l/ --mod w -f n --wlink l
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p/ --mod w -f n --wlink p
#
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl/ --mod w -f n --wlink rl
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl_attr_w/ --mod w -f a --wlink frpl -ar_tgt w
#
#
## 結果が異なるもの　ここから
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim/ --mod m --mint e -tmm trim -f n
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_trim/ --mod t --tinm e -tmt trim -f n
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e/ --mod mt --mint e -tmm trim --tinm e -f n
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim/ --mod mt --mint e --tinm e -tmt trim -f n
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_trim/ --mod mt --mint e -tmm trim --tinm e -tmt trim -f n
##
### 結果が異なるもの　ここから
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_tinm_p/ --mod mt --mint p --tinm p -f n
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_tinm_p_trim/ --mod mt --mint p -tmm trim --tinm p -tmt trim -f n
### ここまで
##
### 結果が異なるもの　ここから
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_m/ --mod w --wlink m -f n
### ここまで
##
### 結果が異なるもの　ここから
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l/ --mod w --wlink l -f n
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_incl_w_imax3_f/ --mod w -f i --wlink l -i_tgt w -i_max 3 -i_type f
#
### ここまで
##
####m/t+ sw
### 結果が異なるもの ここから
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp/ --mod msw -f n --mint e -s_min 0.5 --wlink frp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_slink05_wlink_frp/ --mod mtsw -f n --mint e --tinm e -s_min 0.5 --wlink frp
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink05_wlink_frp/ --mod mtsw -f n --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_frp/ --mod msw -f n --mint p -s_min 0.5 --wlink frp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_tinm_p_slink05_wlink_frp/ --mod mtsw -f n --mint p --tinm p -s_min 0.5 --wlink frp
### ここまで
###
####m/t + swl
### 結果が異なるもの ここから
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_l_05/ --mod mswl -f n --mint e -s_min 0.5 --wlink frp -l_min 0.5
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_slink05_wlink_frp_l_05/ --mod mtswl -f n --mint e --tinm e -s_min 0.5 --wlink frp -l_min 0.5
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink05_wlink_frp_l_05/ --mod mtswl -f n --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -l_min 0.5
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_frp_l_05/ --mod mswl -f n --mint p -s_min 0.5 --wlink frp -l_min 0.5
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_tinm_p_slink05_wlink_frp_l_05/ --mod mtswl -f n --mint p --tinm p -s_min 0.5 --wlink frp -l_min 0.5
## ここまで
#
#######
## FINAL
######
#
## AIPRB_SMW
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_frp_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
#
## AIPRB_WSM
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink__mint_e_attr_w/ --mod w:s:m -f a --mint e --wlink frp -ar_tgt w
#######
#
######
## ANAL
######
## フィルタなし
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e/ --mod m --mint e -f n
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e/ --mod t --tinm e -f n
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e/ --mod mt --mint e --tinm e -f n
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim/ --mod mt --mint e -tmm trim -f n
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_trim/ --mod mt --tinm e -tmt trim -f n
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e/ --mod mt --mint e -tmm trim -tinm e -f n
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim/ --mod mt --mint e --tinm e -tmt trim -f n
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_trim/ --mod mt --mint e -tmm trim --tinm e -tmt trim -f n
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p/ --mod m --mint p -f n
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p/ --mod t --tinm p -f n
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_tinm_p/ --mod mt --mint p --tinm p -f n
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_tinm_p_trim/ --mod mt --mint p -tmm trim --tinm p -tmt trim -f n
##
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05/ --mod s -s_min 0.5 -f n
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink06/ --mod s -s_min 0.6 -f n
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink07/ --mod s -s_min 0.7 -f n
###
###
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f/ --mod w --wlink f -f n
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r/ --mod w --wlink r -f n
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_m/ --mod w --wlink m -f n
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p/ --mod w --wlink p -f n
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l/ --mod w --wlink l -f n
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp/ --mod w --wlink rp -f n
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp/ --mod w --wlink frp -f n
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl/ --mod w --wlink frpl -f n
##
## 10/5修正版
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_05/ --mod l -l_min 0.5
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_06/ --mod l -l_min 0.6
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_07/ --mod l -l_min 0.7
#
############################################################################
## フィルタあり
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_incl_m_imax1_o/ --mod m -f i --mint p -i_tgt m -i_max 1 -i_type o
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_incl_m_imax1_f/ --mod m -f i --mint p -i_tgt m -i_max 1 -i_type f
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_incl_m_imax1_a/ --mod m -f i --mint p -i_tgt m -i_max 1 -i_type a
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_incl_m_imax3_o/ --mod m -f i --mint p -i_tgt m -i_max 3 -i_type o
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_incl_m_imax3_f/ --mod m -f i --mint p -i_tgt m -i_max 3 -i_type f
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_incl_m_imax3_a/ --mod m -f i --mint p -i_tgt m -i_max 3 -i_type a
#
##m/t+ sw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp/ --mod msw -f n --mint e -s_min 0.5 --wlink frp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_slink05_wlink_frp/ --mod mtsw -f n --mint e --tinm e -s_min 0.5 --wlink frp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink05_wlink_frp/ --mod mtsw -f n --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_frp/ --mod msw -f n --mint p -s_min 0.5 --wlink frp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_tinm_p_slink05_wlink_frp/ --mod mtsw -f n --mint p --tinm p -s_min 0.5 --wlink frp
##
###m/t + swl
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_l_05/ --mod mswl -f n --mint e -s_min 0.5 --wlink frp -l_min 0.5
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_slink05_wlink_frp_l_05/ --mod mtswl -f n --mint e --tinm e -s_min 0.5 --wlink frp -l_min 0.5
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink05_wlink_frp_l_05/ --mod mtswl -f n --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -l_min 0.5
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_frp_l_05/ --mod mswl -f n --mint p -s_min 0.5 --wlink frp -l_min 0.5
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_tinm_p_slink05_wlink_frp_l_05/ --mod mtswl -f n --mint p --tinm p -s_min 0.5 --wlink frp -l_min 0.5
#############################################################################
#
##
##
###0929AM- (ただしinclは0929PM-)
###msw
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_attr_w_al_am_bl_w_incl_w_imax5_io/ --mod msw -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type o
##
###mswl
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_l_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_l_attr_w_al_am_bl_w_incl_w_imax5_io/ --mod mswl -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type o
##
###mtsw
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink05_wlink_frp_attr_tw_al_am_bl_tw/ --mod mtsw -f ab --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -ar_tgt tw -al am -bl_tgt tw
##
###mtswl
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink05_wlink_frp_l_attr_tw_al_am_bl_tw/ --mod mtswl -f ab --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -ar_tgt tw -al am -bl_tgt tw
##
###smtw
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__mint_e__tinm_p_wlink_frp_attr_w_al_am_bl_w/ --mod s:m:tw -f ab --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mint_e_l__tinm_p_wlink_frp_attr_w_al_am_bl_w/ --mod sml:tw -f ab --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
##
###smw **
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__mint_e__wlink_frp_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 --wlink rp -ar_tgt w -al am -bl_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__mint_e__wlink_frp_l_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_frp_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_rp__attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w
##
##
##
###smlw
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mint_e_l__wlink_frp_tinm_p_attr_w_al_am_bl_w/ --mod sml:w:t -f ab --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
##
###smtw
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e_wlink_rp__tinm_e_trim_attr_tw_al_am_bl_tw/ --mod s:mw:t -f ab --mint e --tinm e -tmt trim -s_min 0.5 -s_prb mid --wlink rp -ar_tgt tw -al am -bl_tgt tw
##
###smw
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_frp_attr_w_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -bl_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_frp_attr_w_bl_mw/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -bl_tgt mw
##
##
###swm **
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__wlink_frp__mint_e__attr_w_al_am_bl_w/ --mod s:w:m -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__wlink_rp__mint_e_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod s:w:m -f abi --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__wlink_frp__mint_e__attr_w_al_am_bl_w/ --mod s:w:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__wlink_rp__mint_e__attr_w_al_am_bl_w/ --mod s:w:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__wlink_frp__mint_e_attr_w_bl_w/ --mod s:w:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -bl_tgt w
##
##
###wsm ***
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05__mint_e__attr_w_al_am_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05_mid__mint_e_attr_w_al_am_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
###best
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink05_mid__mint_e_attr_w_al_am_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink05_mid__mint_e_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod w:s:m -f abi --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink05_mid__mint_e_attr_w_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w
##
###wms *
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__mint_e__slink05_mid_attr_w_al_am_bl_w/ --mod w:m:s -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__mint_e_mid__slink05_attr_w_al_am_bl_w/ --mod w:m:s -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__mint_e_slink05_mid__tinm_e_trim_attr_tw_al_am_bl_tw/ --mod w:ms:t -f ab --mint e --tinm e -tmt trim -s_min 0.5 -s_prb mid --wlink rp -ar_tgt tw -al am -bl_tgt tw
##
###wmst
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__mint_e_slink05_mid__tinm_e_trim_attr_tw_al_am_bl_tw/ --mod w:ms:t -f ab --mint e --tinm e -tmt trim -s_min 0.5 -s_prb mid --wlink frp -ar_tgt tw -al am -bl_tgt tw
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__mint_e_slink05_mid__tinm_e_trim_attr_w_al_am_bl_t/ --mod w:ms:t -f ab --mint e --tinm e -tmt trim -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt t
##
##
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_frp_modw_1_05_03_02_01_attr_w_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -bl_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_rp_modw_1_05_03_02_01_attr_w_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -bl_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_frp_modw_1_05_03_02_01_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am -bl_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_rp_modw_1_05_03_02_01_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am -bl_tgt w
###
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05_mid__mint_e_modw_1_05_03_02_01_attr_w/ --mod w:s:m -f a --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05_mid__mint_e_modw_1_05_03_02_01_attr_w_al_am/ --mod w:s:m -f a --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05_mid__mint_e_modw_1_05_03_02_01_attr_w_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -bl_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05_mid__mint_e_modw_1_05_03_02_01_attr_w_al_am_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am -bl_tgt w
###
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink05_mid__mint_e_modw_1_05_03_02_01_attr_w/ --mod w:s:m -f a --mint e -s_min 0.5 -s_prb mid --wlink rp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink05_mid__mint_e_modw_1_05_03_02_01_attr_w_al_am/ --mod w:s:m -f a --mint e -s_min 0.5 -s_prb mid --wlink rp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink05_mid__mint_e_modw_1_05_03_02_01_attr_w_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -bl_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink05_mid__mint_e_modw_1_05_03_02_01_attr_w_al_am_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am -bl_tgt w
##
##
##
####final cand
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__wlink_frp__mint_e_modw_1_05_03_02_01_attr_w_al_am_bl_w/ --mod s:w:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am -bl_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05_mid__mint_e_modw_1_05_03_02_01/ --mod w:s:m -f n --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1
###
####s_prbが抜けていた
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05_mid__mint_e_modw_1_05_03_02_01_attr_w_bl_mw/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -bl_tgt mw
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_mid__mint_e_attr_w/ --mod w:s:m -f a --mint e --wlink frp -s_prb mid -ar_tgt w
###
###
###${eval_script}
####baseline
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_incl_w_imax5_if/ --mod m -f i --mint p -i_tgt m -i_max 5 -i_type f
###${eval_script}
##
############
##frp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_attr_w_al_am_bl_w/ --mod msw -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
##latest0929#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_l_attr_w_al_am_bl_w/ --mod mswl -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
#
##here
##retry
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod msw -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
#
#
##priority
#
#
#
##swm
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__wlink_frp__mint_e_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod s:w:m -f abi --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
#
##wsm
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05_mid__mint_e_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod w:s:m -f abi --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
#
##smwt
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e_wlink_frp__tinm_e_trim_attr_w_al_am_bl_w/ --mod s:mw:t -f ab --mint e --tinm e -tmt trim -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
#
#
#
##rp
#
##wsm or wms
#
#
##variation
#
##${eval_script}
######
##till here
######
#
#
#
##latest0929#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_attr_w_bl_w/ --mod msw -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt w
##latest0929#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_l_attr_w_bl_w/ --mod mswl -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt w
##
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_attr_w_bl_w_incl_w_imax5_if/ --mod msw -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt w -i_tgt w -i_max 5 -i_type f
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_l_attr_w_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt w -i_tgt w -i_max 5 -i_type f
##
###rp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_mid_wlink_rp_attr_w_al_am_bl_w/ --mod msw -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_attr_w_al_am_bl_w/ --mod msw -f ab --mint e -s_min 0.5 --wlink rp -ar_tgt w -al am -bl_tgt w
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_l_attr_w_al_am_bl_w/ --mod mswl -f ab --mint e -s_min 0.5 --wlink rp -ar_tgt w -al am -bl_tgt w
###
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod msw -f abi --mint e -s_min 0.5 --wlink rp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_l_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink rp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
###
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_attr_w_bl_w/ --mod msw -f ab --mint e -s_min 0.5 --wlink rp -ar_tgt w -bl_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_l_attr_w_bl_w/ --mod mswl -f ab --mint e -s_min 0.5 --wlink rp -ar_tgt w -bl_tgt w
###
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_attr_w_bl_w_incl_w_imax5_if/ --mod msw -f abi --mint e -s_min 0.5 --wlink rp -ar_tgt w -bl_tgt w -i_tgt w -i_max 5 -i_type f
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_l_attr_w_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink rp -ar_tgt w -bl_tgt w -i_tgt w -i_max 5 -i_type f
##
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink05_mid_wlink_frp_attr_tw_al_am_bl_tw/ --mod mtsw -f ab --mint e --tinm e -tmt trim -s_min 0.5 -s_prb mid --wlink frp -ar_tgt tw -al am -bl_tgt tw
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink05_wlink_frp_attr_tw_al_am_bl_tw_incl_tw_imax5_if/ --mod mtsw -f abi --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -ar_tgt tw -al am -bl_tgt tw -i_tgt tw -i_max 5 -i_type f
##
###from here(sample)
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink05_wlink_frp_attr_tw_al_am_bl_tw_incl_tw_imax5_if/ --mod mtsw -f abi --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -ar_tgt tw -al am -bl_tgt tw -i_tgt tw -i_max 5 -i_type f
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink05_wlink_frp_attr_tw_al_am_bl_tw_incl_tw_imax5_of/ --mod mtsw -f abi --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -ar_tgt tw -al am -bl_tgt tw -i_tgt tw -i_max 5 -i_type o
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink05_wlink_frp_l_attr_tw_al_am_bl_tw_incl_tw_imax5_if/ --mod mtswl -f abi --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -ar_tgt tw -al am -bl_tgt tw -i_tgt tw -i_max 5 -i_type f
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink05_wlink_frp_l_attr_tw_al_am_bl_tw_incl_tw_imax5_of/ --mod mtswl -f abi --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -ar_tgt tw -al am -bl_tgt tw -i_tgt tw -i_max 5 -i_type o
##
####mint_e_tinm_p, frp
### mint_e_tinm_　＋　attr: ok
### timp_p + incl: ng > 要検討
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink05_wlink_frp_attr_w/ --mod mtsw -f ab --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink05_wlink_frp_attr_w_al_am/ --mod mtsw -f ab --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink05_wlink_frp_attr_w_al_am_bl_tw/ --mod mtsw -f ab --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt tw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink05_wlink_frp_attr_w_al_am_bl_w/ --mod mtsw -f ab --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink05_wlink_frp_attr_w_al_am_bl_tw_incl_w_imax5_if/ --mod mtsw -f abi --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt tw -i_tgt w -i_max 5 -i_type f
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink05_wlink_frp_attr_w_al_am_bl_tw_incl_w_imax5_of/ --mod mtsw -f abi --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt tw -i_tgt w -i_max 5 -i_type o
##
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink05_wlink_frp_attr_w_bl_tw/ --mod mtsw -f ab --mint e --tinm p -tmt trim -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt tw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink05_wlink_frp_l_attr_w_al_am_bl_tw/ --mod mtswl -f ab --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt tw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink05_wlink_frp_l_attr_w_al_am_bl_tw_incl_w_imax5_if/ --mod mtswl -f abi --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt tw -i_tgt w -i_max 5 -i_type f
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink05_wlink_frp_l_attr_w_bl_tw/ --mod mtswl -f ab --mint e --tinm p -tmt trim -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt tw
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink05_wlink_frp_l_attr_w_bl_tw_incl_w_imax5_if/ --mod mtsw -f abi --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt tw -i_tgt w -i_max 5 -i_type f
####
###mint_e_trim_tinm_e, frp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink05_wlink_frp_attr_mw/ --mod mtsw -f ab --mint e --tinm e -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink05_wlink_frp_attr_mw_al_am/ --mod mtsw -f ab --mint e --tinm e -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -al am
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink05_wlink_frp_attr_mw_al_am_bl_tw/ --mod mtsw -f ab --mint e --tinm e -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -al am -bl_tgt tw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink05_wlink_frp_attr_mw_al_am_bl_tw_incl_tw_imax_if/ --mod mtsw -f abi --mint e --tinm e -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -al am -bl_tgt tw -i_tgt tw -i_max 5 -i_type f
##
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink05_wlink_frp_l_attr_mw/ --mod mtswl -f a --mint e --tinm e -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink05_wlink_frp_l_attr_mw_al_am/ --mod mtswl -f a --mint e --tinm e -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -al am
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink05_wlink_frp_l_attr_mw_al_am_bl_tw/ --mod mtswl -f ab --mint e --tinm e -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -al am -bl_tgt tw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink05_wlink_frp_l_attr_mw_al_am_bl_tw_incl_tw_imax5_if/ --mod mtswl -f abi --mint e --tinm e -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -al am -bl_tgt tw -i_tgt tw -i_max 5 -i_type f
##
###mint_e_trim_tinm_e, rp mint+ar ok
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink05_wlink_rp_attr_mw/ --mod mtsw -f a --mint e --tinm e -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink05_wlink_rp_attr_mtw/ --mod mtsw -f a --mint e --tinm e -tmm trim -s_min 0.5 --wlink rp -ar_tgt mtw
##
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink05_wlink_rp_attr_mw_al_am/ --mod mtsw -f ab --mint e --tinm e -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw -al am
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink05_wlink_rp_attr_mw_al_am_bl_tw/ --mod mtsw -f ab --mint e --tinm e -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw -al am -bl_tgt tw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink05_wlink_rp_attr_mw_al_am_bl_tw_incl_tw_imax5_if/ --mod mtsw -f abi --mint e --tinm e -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw -al am -bl_tgt tw -i_tgt tw -i_max 5 -i_type f
##
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink05_wlink_rp_l_attr_mw/ --mod mtswl -f a --mint e --tinm e -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink05_wlink_rp_l_attr_mw_al_am/ --mod mtswl -f a --mint e --tinm e -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw -al am
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink05_wlink_rp_l_attr_mw_al_am_bl_tw/ --mod mtswl -f ab --mint e --tinm e -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw -al am -bl_tgt tw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink05_wlink_rp_l_attr_mw_al_am_bl_tw_incl_tw_imax5_if/ --mod mtswl -f abi --mint e --tinm e -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw -al am -bl_tgt tw -i_tgt tw -i_max 5 -i_type f
##
###(mint_e_trim_tinm_p, frp) mint e trim: +ar ok
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink05_wlink_frp_attr_mw/ --mod mtsw -f a --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink05_wlink_frp_attr_mtw/ --mod mtsw -f a --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mtw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink05_wlink_frp_attr_mw_al_am/ --mod mtsw -f a --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -al am
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink05_wlink_frp_attr_mtw_al_am/ --mod mtsw -f a --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mtw -al am
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink05_wlink_frp_attr_mw_al_am_bl_tw/ --mod mtsw -f ab --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -al am -bl_tgt tw
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink05_wlink_frp_attr_mtw_al_am_bl_tw/ --mod mtsw -f ab --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mtw -al am -bl_tgt tw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink05_wlink_frp_attr_mw_bl_tw_incl_w_imax5_if/ --mod mtsw -f abi --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -bl_tgt tw -i_tgt w -i_max 5 -i_type f
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink05_wlink_frp_attr_mtw_bl_tw_incl_w_imax5_if/ --mod mtsw -f abi --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mtw -bl_tgt tw -i_tgt w -i_max 5 -i_type f
##
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink05_wlink_frp_l_attr_mw/ --mod mtswl -f a --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink05_wlink_frp_l_attr_mw_al_am/ --mod mtswl -f a --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -al am
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink05_wlink_frp_l_attr_mw_al_am_bl_tw/ --mod mtswl -f ab --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -al am -bl_tgt tw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink05_wlink_frp_l_attr_mw_al_am_bl_tw_incl_w_imax5_if/ --mod mtswl -f abi --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -al am -bl_tgt tw -i_tgt w -i_max 5 -i_type f
##
###mint_e_trim_tinm_p, rp: mint+attr:ok tinm+attr:ng
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink05_wlink_rp_attr_mw/ --mod mtsw -f a --mint e --tinm p -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink05_wlink_rp_attr_mw_al_am/ --mod mtsw -f a --mint e --tinm p -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw -al am
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink05_wlink_rp_attr_mw_al_am_bl_tw/ --mod mtsw -f ab --mint e --tinm p -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw -al am -bl_tgt tw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink05_wlink_rp_attr_mw_bl_tw_incl_w_imax5_if/ --mod mtsw -f abi --mint e --tinm p -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw -bl_tgt tw -i_tgt w -i_max 5 -i_type f
##
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink05_wlink_rp_l_attr_mw/ --mod mtswl -f ab --mint e --tinm p -tmm trim -s_min 0.5 --wlink rp -al am -ar_tgt mw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink05_wlink_rp_l_attr_mw_al_am/ --mod mtswl -f ab --mint e --tinm p -tmm trim -s_min 0.5 --wlink rp -al am -ar_tgt mw -al am
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink05_wlink_rp_l_attr_mw_al_am_bl_tw/ --mod mtswl -f ab --mint e --tinm p -tmm trim -s_min 0.5 --wlink rp -al am -ar_tgt mw -bl_tgt tw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink05_wlink_rp_l_attr_mw_al_am_bl_tw_incl_w_imax5_if/ --mod mtswl -f abi --mint e --tinm p -tmm trim -s_min 0.5 --wlink rp -al am -ar_tgt mw -bl_tgt tw -i_tgt w -i_max 5 -i_type f
#
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l/ --mod l -f n -a_max 1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e/ --mod m
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim/ --mod m -f n --mint e -tmm trim
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e/ --mod m -f n --mint e --tinm e
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim/ --mod m -f n --mint e --tinm e -tmt trim
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p/ --mod m -f n --mint p
#
#
## mint p trim: +attr ok
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim/ --mod m -f n --mint p -tmm trim
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05/ --mod s -f n -s_min 0.5
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e/ --mod t -f n --tinm e
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_trim/ --mod t -f n --tinm e -tmt trim
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p/ --mod t -f n --tinm p
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim/ --mod t -f n --tinm p -tmt trim
#
#
#
##rm -i ${out_dir_base}*.tsv
##rm ${out_dir_base}*_pre.tsv
##rm ${out_dir_base}*/*_summary.tsv
##rm ${out_dir_base}*/*_anal.tsv
##rm ${out_dir_base}*/*_fn.tsv
##rm ${out_dir_base}*/Airport.tsv
##rm ${out_dir_base}*/City.tsv
##rm ${out_dir_base}*/Company.tsv
##rm ${out_dir_base}*/Compound.tsv
##rm ${out_dir_base}*/Conference.tsv
##rm ${out_dir_base}*/Lake.tsv
##rm ${out_dir_base}*/Person.tsv
##rm ${out_dir_base}*/*.tsv
##grep 'script' ~/PycharmProjects/linkjpc/linkjpc_all_test.sh |  awk '{print $6}' | perl -pe 's/\${out_dir_base}//;' | perl -pe 's/\///g;' | sort | uniq > $eval_target
###grep 'script' ~/PycharmProjects/linkjpc/linkjpc_all_sample.sh | grep -v '#' | awk '{print $6}' | perl -pe 's/\${out_dir_base}//;' | perl -pe 's/\///g;' | sort | uniq > $eval_target
##python json2tsv_linkjp.py $out_dir_base $gold_dir $in_dir $eval_target
##python evaluation_linkjp_old.py $out_dir_base $gold_dir $eval_target
##cd $out_dir_base
##cat */all_summary.tsv > all_summary_pre.tsv
##cat ../summary_header.txt all_summary_pre.tsv > all_summary.tsv
##cp all_summary.tsv eval_$$.txt
##cp ~/PycharmProjects/linkjpc/linkjpc_all_sample.sh env_$$.txt
##cat ./*/*_summary.tsv | grep -v SYS_ID | grep -v ^e | grep -v ^p | sort -d > summary_category_pre.tsv
##cat ../summary_cat_header.txt summary_category_pre.tsv > summary_category.tsv
##cp summary_category.tsv ${setting_dir}summary_category_$$.txt
