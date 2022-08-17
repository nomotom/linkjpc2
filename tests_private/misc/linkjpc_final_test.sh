#!/bin/sh -x
script="./linkjpc.py"
common_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/common/"
tmp_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/test/"
gold_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-210825/link_annotation/"
in_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-210825/ene_annotation/"
out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/final_rev5/"
#eval_target="./eval_target_test"
out_dir_tmp_base="/Users/masako/tmp/test/tmp_test/"


######
# FINAL rev5
#####
### AIPCB_CBI
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_incl_m_imax1_o/ --mod m -f i --mint p -i_tgt m -i_max 1 -i_type o
##
#### AIPRB_SMW
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_frp_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
###
#### AIPRB_WSM
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink__mint_e_attr_w/ --mod w:s:m -f a --mint e --wlink frp -ar_tgt w
#########
##
#######
### ANAL
#######
#### フィルタなし
## 結果が同じもの
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e/ --mod m --mint e -f n
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e/ --mod t --tinm e -f n
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e/ --mod mt --mint e --tinm e -f n
#
## 結果が異なるもの　ここから
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim/ --mod m --mint e -tmm trim -f n
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_trim/ --mod t --tinm e -tmt trim -f n
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e/ --mod mt --mint e -tmm trim --tinm e -f n
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim/ --mod mt --mint e --tinm e -tmt trim -f n
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_trim/ --mod mt --mint e -tmm trim --tinm e -tmt trim -f n
## ここまで
#
## 結果が同じもの
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p/ --mod m --mint p -f n
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p/ --mod t --tinm p -f n
#
## 結果が異なるもの　ここから
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_tinm_p/ --mod mt --mint p --tinm p -f n
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_tinm_p_trim/ --mod mt --mint p -tmm trim --tinm p -tmt trim -f n
## ここまで
#
## 結果が同じもの　10/6 1:00
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05/ --mod s -s_min 0.5 -f n
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink06/ --mod s -s_min 0.6 -f n
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink07/ --mod s -s_min 0.7 -f n
##
## 結果が同じもの
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f/ --mod w --wlink f -f n
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r/ --mod w --wlink r -f n
#
## 結果が異なるもの　ここから
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_m/ --mod w --wlink m -f n
## ここまで
#
## 結果が同じもの
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p/ --mod w --wlink p -f n
#
## 結果が異なるもの　ここから
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l/ --mod w --wlink l -f n
## ここまで
## 結果が同じもの
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp/ --mod w --wlink rp -f n
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp/ --mod w --wlink frp -f n
#
## 結果が異なるもの　ここから
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl/ --mod w --wlink frpl -f n
##ここまで
#
## 結果が同じもの 10/5修正版 10/6 1:00
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_05/ --mod l -l_min 0.5
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_06/ --mod l -l_min 0.6
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_07/ --mod l -l_min 0.7
##
##
###m/t+ sw
## 結果が異なるもの ここから
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp/ --mod msw -f n --mint e -s_min 0.5 --wlink frp
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_slink05_wlink_frp/ --mod mtsw -f n --mint e --tinm e -s_min 0.5 --wlink frp
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink05_wlink_frp/ --mod mtsw -f n --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_frp/ --mod msw -f n --mint p -s_min 0.5 --wlink frp
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_tinm_p_slink05_wlink_frp/ --mod mtsw -f n --mint p --tinm p -s_min 0.5 --wlink frp
## ここまで
##
###m/t + swl
## 結果が異なるもの ここから
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_l_05/ --mod mswl -f n --mint e -s_min 0.5 --wlink frp -l_min 0.5
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_slink05_wlink_frp_l_05/ --mod mtswl -f n --mint e --tinm e -s_min 0.5 --wlink frp -l_min 0.5
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink05_wlink_frp_l_05/ --mod mtswl -f n --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -l_min 0.5
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_frp_l_05/ --mod mswl -f n --mint p -s_min 0.5 --wlink frp -l_min 0.5
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_tinm_p_slink05_wlink_frp_l_05/ --mod mtswl -f n --mint p --tinm p -s_min 0.5 --wlink frp -l_min 0.5


###################################################################################
#sample dataの結果がよかったもの 2021/10/9
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_l_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_l_attr_w_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt w -i_tgt w -i_max 5 -i_type f
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_l_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink rp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f




##
#final
#cand1
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_frp_attr_w_al_am_bl_w_incl_w_imax3_a/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 3 -i_type a
##cand2
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink05_mid__mint_e_modw_1_05_03_02_01_attr_w_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid  --wlink rp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -bl_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__mint_e__wlink_frp_attr_w/ --mod s:m:w -f a --mint e -s_min 0.5 --wlink frp -ar_tgt w
#
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__wlink_frp__mint_e_modw_1_05_03_02_01_attr_w_al_am_bl_w/ --mod s:w:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am -bl_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05_mid__mint_e_modw_1_05_03_02_01_attr_w_al_am_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am -bl_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_mid__mint_e_attr_w/ --mod w:s:m -f a --mint e --wlink frp -s_prb mid -ar_tgt w
#
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink05__mint_e_modw_1_05_03_02_01_attr_w_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 --wlink rp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -bl_tgt w
#
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__mint_e__wlink_frp_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
##多分実行時に近いのは上
#
#
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__mint_e__wlink_frp_attr_w_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt w
#
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__wlink_frp__mint_e_modw_1_05_03_02_01_attr_w_al_am_bl_w/ --mod s:w:m -f ab --mint e -s_min 0.5 --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am -bl_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05__mint_e_modw_1_05_03_02_01_attr_w_al_am_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am -bl_tgt w





#以下は元の予定

#AIPRB

# 1) slink05__mint_e__wlink_frp_attr_w_al_am_bl_w (sample data: 0.8240)
# AIPRB_SMW

#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_frp_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
#(33517) 9/29 19:XX #python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__mint_e__wlink_frp_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w


# 2) wlink_rp__slink05__mint_e_modw_1_05_03_02_01_attr_w_bl_w (sample data: 0.8237)
# AIPRB_WSM
#(94400) 9/30 14:29 python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink05_mid__mint_e_modw_1_05_03_02_01_attr_w_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 --wlink rp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -bl_tgt w

#AIPCB (ベースライン）


# 3) mint_p_incl_w_imax5_if
# AIPCB_MPI

#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_incl_m_imax5_if/ --mod m -f i --mint p -i_tgt m -i_max 5 -i_type f



######


