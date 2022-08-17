#!/bin/sh -x
now=`date +%Y%m%d%H%M%S`
script="./linkjpc.py"
common_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/common/"
tmp_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/sample/"
in_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/ene_annotation/"
gold_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/link_annotation/"
out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20211020/"
eval_target="./eval_target_sample"
out_dir_tmp_base="/Users/masako/tmp/sample/202101020/"
setting_dir="${out_dir_base}setting/"
eval_script="./linkjpc_eval_sample.sh"
#####################


## AIPRB_SMW
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_frp_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
#
## AIPRB_WSM
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink__mint_e_attr_w/ --mod w:s:m -f a --mint e --wlink frp -ar_tgt w
#
## AIPCB_CBI
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_incl_m_imax1_o/ --mod m -f i --mint p -i_tgt m -i_max 1 -i_type o

##2021/10/9
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_05/ --mod l -l_min 0.5
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_06/ --mod l -l_min 0.6
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_07/ --mod l -l_min 0.7
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e/ --mod m --mint e -f n
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_mid_wlink_rp_attr_w_al_am_bl_w/ --mod msw -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp/ --mod msw -f n --mint e -s_min 0.5 --wlink frp
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod msw -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_attr_w_al_am_bl_w_incl_w_imax5_io/ --mod msw -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type o
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_attr_w_bl_w_incl_w_imax5_if/ --mod msw -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt w -i_tgt w -i_max 5 -i_type f
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_l_05/ --mod mswl -f n --mint e -s_min 0.5 --wlink frp -l_min 0.5
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_l_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_l_attr_w_al_am_bl_w_incl_w_imax5_io/ --mod mswl -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type o
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_l_attr_w_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt w -i_tgt w -i_max 5 -i_type f
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_l_06_attr_w_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink frp -l_min 0.6 -ar_tgt w -bl_tgt w -i_tgt w -i_max 5 -i_type f
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_mid_wlink_frp_l_06_attr_w_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 -s_prb mid --wlink frp -l_min 0.6 -ar_tgt w -bl_tgt w -i_tgt w -i_max 5 -i_type f
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_l_06_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink frp -l_min 0.6 -ar_tgt w -bl_tgt w -i_tgt w -i_max 5 -i_type f
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_attr_w_al_am_bl_w/ --mod msw -f ab --mint e -s_min 0.5 --wlink rp -ar_tgt w -al am -bl_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod msw -f abi --mint e -s_min 0.5 --wlink rp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_attr_w_bl_w_incl_w_imax5_if/ --mod msw -f abi --mint e -s_min 0.5 --wlink rp -ar_tgt w -bl_tgt w -i_tgt w -i_max 5 -i_type f
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_l_attr_w_al_am_bl_w/ --mod mswl -f ab --mint e -s_min 0.5 --wlink rp -ar_tgt w -al am -bl_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_l_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink rp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_l_06_attr_w_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink rp -l_min 0.6 -ar_tgt w -bl_tgt w -i_tgt w -i_max 5 -i_type f
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_slink05_wlink_frp/ --mod mtsw -f n --mint e --tinm e -s_min 0.5 --wlink frp
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_slink05_wlink_frp_l_05/ --mod mtswl -f n --mint e --tinm e -s_min 0.5 --wlink frp -l_min 0.5
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink05_mid_wlink_frp_attr_tw_al_am_bl_tw/ --mod mtsw -f ab --mint e --tinm e -tmt trim -s_min 0.5 -s_prb mid --wlink frp -ar_tgt tw -al am -bl_tgt tw
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink05_wlink_frp/ --mod mtsw -f n --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink05_wlink_frp_attr_tw_al_am_bl_tw/ --mod mtsw -f ab --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -ar_tgt tw -al am -bl_tgt tw
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink05_wlink_frp_attr_tw_al_am_bl_tw_incl_tw_imax5_if/ --mod mtsw -f abi --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -ar_tgt tw -al am -bl_tgt tw -i_tgt tw -i_max 5 -i_type f
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink05_wlink_frp_attr_tw_al_am_bl_tw_incl_tw_imax5_of/ --mod mtsw -f abi --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -ar_tgt tw -al am -bl_tgt tw -i_tgt tw -i_max 5 -i_type o
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink05_wlink_frp_l_05/ --mod mtswl -f n --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -l_min 0.5
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink05_wlink_frp_l_attr_tw_al_am_bl_tw/ --mod mtswl -f ab --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -ar_tgt tw -al am -bl_tgt tw
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink05_wlink_frp_l_attr_tw_al_am_bl_tw_incl_tw_imax5_if/ --mod mtswl -f abi --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -ar_tgt tw -al am -bl_tgt tw -i_tgt tw -i_max 5 -i_type f
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink05_wlink_frp_attr_w_al_am_bl_tw_incl_w_imax5_if/ --mod mtsw -f abi --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt tw -i_tgt w -i_max 5 -i_type f
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim/ --mod m --mint e -tmm trim -f n
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e/ --mod mt --mint e -tmm trim --tinm e -f n
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_trim/ --mod mt --mint e -tmm trim --tinm e -tmt trim -f n
#
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_incl_m_imax1_a/ --mod m -f i --mint p -i_tgt m -i_max 1 -i_type a
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_incl_m_imax1_f/ --mod m -f i --mint p -i_tgt m -i_max 1 -i_type f
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_incl_m_imax1_o/ --mod m -f i --mint p -i_tgt m -i_max 1 -i_type o
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_incl_m_imax3_a/ --mod m -f i --mint p -i_tgt m -i_max 3 -i_type a
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_incl_m_imax3_f/ --mod m -f i --mint p -i_tgt m -i_max 3 -i_type f
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_incl_m_imax3_o/ --mod m -f i --mint p -i_tgt m -i_max 3 -i_type o
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_frp/ --mod msw -f n --mint p -s_min 0.5 --wlink frp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_frp_l_05/ --mod mswl -f n --mint p -s_min 0.5 --wlink frp -l_min 0.5
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_tinm_p/ --mod mt --mint p --tinm p -f n
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_tinm_p_slink05_wlink_frp/ --mod mtsw -f n --mint p --tinm p -s_min 0.5 --wlink frp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_tinm_p_slink05_wlink_frp_l_05/ --mod mtswl -f n --mint p --tinm p -s_min 0.5 --wlink frp -l_min 0.5
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_tinm_p_trim/ --mod mt --mint p -tmm trim --tinm p -tmt trim -f n
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05/ --mod s -s_min 0.5 -f n
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__mint_e__wlink_frp_attr_w/ --mod s:m:w -f a --mint e -s_min 0.5 --wlink frp -ar_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__mint_e__wlink_frp_attr_w_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__wlink_frp__mint_e_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod s:w:m -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__wlink_frp__mint_e_modw_1_05_03_02_01_attr_w_al_am_bl_w/ --mod s:w:m -f ab --mint e -s_min 0.5 --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am -bl_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_frp_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_rp_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e_wlink_frp__tinm_e_trim_attr_tw_al_am_bl_tw/ --mod s:mw:t -f ab --mint e --tinm e -tmt trim -s_min 0.5 -s_prb mid --wlink frp -ar_tgt tw -al am -bl_tgt tw
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e_wlink_rp__tinm_e_trim_attr_tw_al_am_bl_tw/ --mod s:mw:t -f ab --mint e --tinm e -tmt trim -s_min 0.5 -s_prb mid --wlink rp -ar_tgt tw -al am -bl_tgt tw
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__wlink_frp__mint_e_attr_w_al_am_bl_w/ --mod s:w:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__wlink_frpl__mint_e_attr_w_al_am_bl_w/ --mod s:w:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frpl -ar_tgt w -al am -bl_tgt w
#
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__wlink_frp__mint_e_attr_w_bl_w/ --mod s:w:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -bl_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__wlink_frp__mint_e_modw_1_05_03_02_01_attr_w_al_am_bl_w/ --mod s:w:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am -bl_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__wlink_rp__mint_e_attr_w_al_am_bl_w/ --mod s:w:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w
#
#
#
#
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__wlink_rp__mint_e_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod s:w:m -f abi --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink06/ --mod s -s_min 0.6 -f n
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink07/ --mod s -s_min 0.7 -f n
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink__mint_e__wlink_frp_attr_w/ --mod s:m:w -f a --mint e --wlink frp -ar_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_mid__mint_e__wlink_frp_attr_w/ --mod s:m:w -f a --mint e --wlink frp -s_prb mid -ar_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_mid__mint_e__wlink_frp_attr_w_al_am/ --mod s:m:w -f a --mint e --wlink frp -s_prb mid -ar_tgt w -al am
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink__mint_e__wlink_frp_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod s:m:w -f abi --mint e --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink__mint_e__wlink_frp_l_06_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod s:m:wl -f abi --mint e --wlink frp -l_min 0.6 -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_mid__mint_e__wlink_frp_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod s:m:w -f abi --mint e --wlink frp -s_prb mid -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_mid__mint_e__wlink_frp_l_06_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod s:m:wl -f abi --mint e --wlink frp -s_prb mid -l_min 0.6 -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_mid__mint_e__wlink_rp_attr_w/ --mod s:m:w -f a --mint e --wlink rp -s_prb mid -ar_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_mid__mint_e__wlink_rp_attr_w_al_am/ --mod s:m:w -f a --mint e --wlink rp -s_prb mid -ar_tgt w -al am
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_mid__mint_e__wlink_rp_attr_w_al_am_incl_w_imax5_if/ --mod s:m:w -f ai --mint e --wlink rp -s_prb mid -ar_tgt w -al am -i_tgt w -i_max 5 -i_type f
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e/ --mod t --tinm e -f n
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_trim/ --mod t --tinm e -tmt trim -f n
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p/ --mod t --tinm p -f n
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f/ --mod w --wlink f -f n
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp/ --mod w --wlink frp -f n
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__mint_e__slink05_mid_attr_w_al_am_bl_w/ --mod w:m:s -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl__mint_e__slink05_mid_attr_w_al_am_bl_w/ --mod w:m:s -f ab --mint e -s_min 0.5 -s_prb mid --wlink frpl -ar_tgt w -al am -bl_tgt w
#
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__mint_e_slink05_mid__tinm_e_trim_attr_tw_al_am_bl_tw/ --mod w:ms:t -f ab --mint e --tinm e -tmt trim -s_min 0.5 -s_prb mid --wlink frp -ar_tgt tw -al am -bl_tgt tw
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05__mint_e_modw_1_05_03_02_01_attr_w_al_am_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am -bl_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05_mid__mint_e_attr_w_al_am_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl__slink05_mid__mint_e_attr_w_al_am_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frpl -ar_tgt w -al am -bl_tgt w
#
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05_mid__mint_e_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod w:s:m -f abi --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05_mid__mint_e_attr_w_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -bl_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05_mid__mint_e_modw_1_05_03_02_01_attr_w_al_am_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am -bl_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink__mint_e_attr_w/ --mod w:s:m -f a --mint e --wlink frp -ar_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_mid__mint_e_attr_w/ --mod w:s:m -f a --mint e --wlink frp -s_prb mid -ar_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl__slink_mid__mint_e_attr_w/ --mod w:s:m -f a --mint e --wlink frpl -s_prb mid -ar_tgt w
#
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_mid_mint_e__tinm_e_attr_w_al_am/ --mod w:ms:t -f a --mint e --tinm e -tmt trim --wlink frp -s_prb mid -ar_tgt w -al am
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_mid_mint_e__tinm_e_trim_attr_w_al_am/ --mod w:ms:t -f a --mint e --tinm e -tmt trim --wlink frp -s_prb mid -ar_tgt w -al am
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl/ --mod w --wlink frpl -f n
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l/ --mod w --wlink l -f n
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_m/ --mod w --wlink m -f n
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p/ --mod w --wlink p -f n
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r/ --mod w --wlink r -f n
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp/ --mod w --wlink rp -f n
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__mint_e__slink05_mid_attr_w_al_am_bl_w/ --mod w:m:s -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__mint_e__slink05_mid_attr_w_bl_w/ --mod w:m:s -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -bl_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__mint_e__slink05_mid_bl_w/ --mod w:m:s -f b --mint e -s_min 0.5 -s_prb mid --wlink rp  -bl_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__mint_e_slink05_mid_tinm_e__trim_attr_tw_al_am_bl_tw/ --mod w:ms:t -f ab --mint e --tinm e -tmt trim -s_min 0.5 -s_prb mid --wlink rp -ar_tgt tw -al am -bl_tgt tw
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink05__mint_e_modw_1_05_03_02_01_attr_w_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 --wlink rp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -bl_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink05_mid__mint_e_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod w:s:m -f abi --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink05_mid__mint_e_attr_w_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -bl_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink05_mid__mint_e_modw_1_05_03_02_01_attr_w_al_am_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am -bl_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink05_mid__mint_e_modw_1_05_03_02_01_attr_w_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -bl_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink__mint_e_attr_w/ --mod w:s:m -f a --mint e --wlink rp -ar_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink_mid__mint_e_attr_w/ --mod w:s:m -f a --mint e --wlink rp -s_prb mid -ar_tgt w
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink_mid__mint_e_attr_w_al_am/ --mod w:s:m -f a --mint e --wlink rp -s_prb mid -ar_tgt w -al am
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink_mid_mint_e__tinm_e_attr_w_al_am/ --mod w:ms:t -f a --mint e --tinm e -tmt trim --wlink rp -s_prb mid -ar_tgt w -al am
##2021/10/9#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink_mid_mint_e__tinm_e_trim_attr_w_al_am/ --mod w:ms:t -f a --mint e --tinm e -tmt trim --wlink rp -s_prb mid -ar_tgt w -al am
#
#
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink__mint_e__attr_w_al_am_bl_w_incl_w_imax5_if/ --mod w:s:ml -f abi --mint e --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink__mint_e_l_06_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod w:s:ml -f abi --mint e --wlink frp -l_min 0.6 -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_mid__mint_e_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod w:s:ml -f abi --mint e --wlink frp -s_prb mid -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_mid__mint_e_l_06_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod w:s:ml -f abi --mint e --wlink frp -s_prb mid -l_min 0.6 -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
#
############################################################################
##2021/10/8 ここからは未整理
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e__slink05_mid__wlink_frp_attr_w_al_am_bl_w/ --mod m:s:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e__wlink_frp__slink05_mid_attr_w_al_am_bl_w/ --mod m:w:s -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
##
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e__slink05__wlink_frp_attr_mtw_al_am_bl_tw/ --mod mt:s:w -f ab --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -ar_tgt tw -al am -bl_tgt tw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__wlink_frp__mint_e_trim_tinm_e_attr_tw_al_am_bl_tw/ --mod s:w:mt -f ab --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -ar_tgt tw -al am -bl_tgt tw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__mint_e_trim_tinm_e__wlink_frp_attr_tw_al_am_bl_tw/ --mod s:mt:w -f ab --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -ar_tgt tw -al am -bl_tgt tw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05_mid__mint_e_modw_1_05_03_02_01/ --mod w:s:m -f n --mint e -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05_mid__mint_e_modw_1_07_05_03_01/ --mod w:s:m -f n --mint e -s_prb mid --wlink frp --mod_w 1.0:0.7:0.5:0.3:0.1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05_mid__mint_e_modw_1_06_04_02_01/ --mod w:s:m -f n --mint e -s_prb mid --wlink frp --mod_w 1.0:0.6:0.4:0.2:0.1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05_mid__mint_e_modw_1_04_03_02_01/ --mod w:s:m -f n --mint e -s_prb mid --wlink frp --mod_w 1.0:0.4:0.3:0.2:0.1
###
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__mint_e__slink05_mid_modw_1_05_03_02_01/ --mod w:m:s -f n --mint e -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__mint_e__slink05_mid_modw_1_07_05_03_01/ --mod w:m:s -f n --mint e -s_prb mid --wlink frp --mod_w 1.0:0.7:0.5:0.3:0.1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__mint_e__slink05_mid_modw_1_06_04_02_01/ --mod w:m:s -f n --mint e -s_prb mid --wlink frp --mod_w 1.0:0.6:0.4:0.2:0.1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__mint_e__slink05_mid_modw_1_04_03_02_01/ --mod w:m:s -f n --mint e -s_prb mid --wlink frp --mod_w 1.0:0.4:0.3:0.2:0.1
###
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__wlink_frp__mint_e_modw_1_05_03_02_01/ --mod s:w:m -f n --mint e -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__wlink_frp__mint_e_modw_1_07_05_03_01/ --mod s:w:m -f n --mint e -s_prb mid --wlink frp --mod_w 1.0:0.7:0.5:0.3:0.1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__wlink_frp__mint_e_modw_1_06_04_02_01/ --mod s:w:m -f n --mint e -s_prb mid --wlink frp --mod_w 1.0:0.6:0.4:0.2:0.1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__wlink_frp__mint_e_modw_1_04_03_02_01/ --mod s:w:m -f n --mint e -s_prb mid --wlink frp --mod_w 1.0:0.4:0.3:0.2:0.1
##
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_frp_modw_1_05_03_02_01/ --mod s:m:w -f n --mint e -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_frp_modw_1_07_05_03_01/ --mod s:m:w -f n --mint e -s_prb mid --wlink frp --mod_w 1.0:0.7:0.5:0.3:0.1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_frp_modw_1_06_04_02_01/ --mod s:m:w -f n --mint e -s_prb mid --wlink frp --mod_w 1.0:0.6:0.4:0.2:0.1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_frp_modw_1_04_03_02_01/ --mod s:m:w -f n --mint e -s_prb mid --wlink frp --mod_w 1.0:0.4:0.3:0.2:0.1
##
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05_mid__mint_e/ --mod w:s:m -f n --mint e -s_prb mid --wlink frp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__mint_e__slink05_mid/ --mod w:m:s -f n --mint e -s_prb mid --wlink frp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__wlink_frp__mint_e/ --mod s:w:m -f n --mint e -s_prb mid --wlink frp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_frp/ --mod s:m:w -f n --mint e -s_prb mid --wlink frp
##
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_frp_attr_w_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -bl_tgt w
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_frp_attr_w_bl_mw/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -bl_tgt mw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_frp_attr_w_bl_msw/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -bl_tgt msw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__wlink_frp__mint_e_modw_1_05_03_02_01_attr_w_bl_w/ --mod s:w:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -bl_tgt w
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__wlink_frp__mint_e_modw_1_05_03_02_01_attr_w_al_am_bl_mw/ --mod s:w:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am -bl_tgt mw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__wlink_frp__mint_e_modw_1_05_03_02_01_attr_w_al_am_bl_msw/ --mod s:w:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am -bl_tgt msw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_frpl_wls03_wlb02_wlf01_attr_w_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frpl -wls 0.3 -wlb 0.2 -wlf 0.1 -ar_tgt w -bl_tgt w
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_trim_tmin08/ --mod mt -f n --mint e --tinm p -tmm trim -tmt trim -t_min 0.8
##
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl_wls03_wlb02_wlf01__slink05_mid__mint_e__attr_w_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frpl -wls 0.3 -wlb 0.2 -wlf 0.1 -ar_tgt w -bl_tgt w
#######################################
###try
##
##
###prbが抜けていた　ここから
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink05_mid__mint_e_modw_1_05_03_02_01_attr_w_bl_mw/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -bl_tgt mw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink05_mid__mint_e_modw_1_05_03_02_01_attr_w_bl_msw/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -bl_tgt msw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink05_mid__mint_e_modw_1_05_03_02_01_attr_mw_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt mw -bl_tgt w
####${eval_script}
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05_mid__mint_e_modw_1_05_03_02_01_attr_w_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -bl_tgt w
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05_mid__mint_e_modw_1_05_03_02_01_attr_w_bl_mw/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -bl_tgt mw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05_mid__mint_e_modw_1_05_03_02_01_attr_w_bl_msw/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -bl_tgt msw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05_mid__mint_e_modw_1_05_03_02_01_attr_mw_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt mw -bl_tgt w
####${eval_script}
####
#####prbがrawになっていた
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_mid_wlink_frp/ --mod msw -f n --mint e -s_min 0.5 -s_prb mid --wlink frp
###prb抜け
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__mint_e__slink_mid_attr_w_al_am/ --mod w:s:m -f a --mint e --wlink frp -s_prb mid -ar_tgt w -al am
###ディレクトリ名と食い違い
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_mint_e_attr_w_anc09_ang01_al_am/ --mod w:ms -f a --mint e --wlink frp -ar_tgt w -anc 0.9 -ang 0.1 -al am
##${eval_script}
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid__mint_e__wlink_rp/ --mod s:m:w -f n --mint e -s_min 0.5 -s_prb mid --wlink rp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_raw__mint_e_trim_wlink_rp/ --mod s:mw -f n --mint e -tmm trim -s_min 0.5 -s_prb raw --wlink rp
#######################################
###${eval_script}
##
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__mint_e__wlink_frp_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__mint_e__wlink_frp_l_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
##
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__mint_e__tinm_p_wlink_frp_attr_w_al_am_bl_w/ --mod s:m:tw -f ab --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mint_e_l__tinm_p_wlink_frp_attr_w_al_am_bl_w/ --mod msl:tw -f ab --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mint_e_l__wlink_frp_tinm_p_attr_w_al_am_bl_w/ --mod msl:w:t -f ab --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__wlink_frp__mint_e_attr_w_al_am_bl_w/ --mod s:w:m -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink05__mint_e_attr_w_al_am_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
##
##
###frp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_attr_w_al_am_bl_w/ --mod msw -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_l_attr_w_al_am_bl_w/ --mod mswl -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
##
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_attr_w_bl_w/ --mod msw -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt w
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp_l_attr_w_bl_w/ --mod mswl -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt w
###
###
####rp
##
###
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_attr_w_bl_w/ --mod msw -f ab --mint e -s_min 0.5 --wlink rp -ar_tgt w -bl_tgt w
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_l_attr_w_bl_w/ --mod mswl -f ab --mint e -s_min 0.5 --wlink rp -ar_tgt w -bl_tgt w
##
##
##here
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_l_attr_w_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink rp -ar_tgt w -bl_tgt w -i_tgt w -i_max 5 -i_type f
##
#
#
#
#
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__mint_e__slink_mid_attr_w/ --mod w:s:m -f a --mint e --wlink frp -s_prb mid -ar_tgt w
#
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink__mint_e_attr_w_al_am/ --mod w:s:m -f a --mint e --wlink rp  -ar_tgt w -al am
#
####0928-1555#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_raw__mint_e_attr_w_anc09_ang01_al_am/ --mod w:s:m -f a --mint e -s_prb raw --wlink frp -ar_tgt w -anc 0.9 -ang 0.1 -al am
####0928-1555#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_mid_mint_e_attr_w_anc09_ang01_al_am/ --mod w:s:m -f a --mint e -s_prb mid --wlink frp -ar_tgt w -anc 0.9 -ang 0.1 -al am
####0928-1555#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_raw_mint_e_attr_w_anc09_ang01_al_am/ --mod w:s:m -f a --mint e -s_prb raw --wlink frp -ar_tgt w -anc 0.9 -ang 0.1 -al am
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp_attr_w_anc09_ang01_al_am__slink__mint_e/ --mod w:s:m -f a --wlink frp -ar_tgt w -anc 0.9 -ang 0.1 -al am
#
#
##from here(sample)
#
#
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink05_wlink_frp_l_attr_tw_al_am_bl_tw_incl_tw_imax5_of/ --mod mtswl -f abi --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -ar_tgt tw -al am -bl_tgt tw -i_tgt tw -i_max 5 -i_type o
#
###mint_e_tinm_p, frp
## mint_e_tinm_　＋　attr: ok
## timp_p + incl: ng > 要検討
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink05_wlink_frp_attr_w/ --mod mtsw -f ab --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink05_wlink_frp_attr_w_al_am/ --mod mtsw -f ab --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink05_wlink_frp_attr_w_al_am_bl_w/ --mod mtsw -f ab --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink05_wlink_frp_attr_w_al_am_bl_tw_incl_w_imax5_of/ --mod mtsw -f abi --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt tw -i_tgt w -i_max 5 -i_type o
##
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink05_wlink_frp_attr_w_bl_tw/ --mod mtsw -f ab --mint e --tinm p -tmt trim -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt tw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink05_wlink_frp_l_attr_w_al_am_bl_tw/ --mod mtswl -f ab --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt tw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink05_wlink_frp_l_attr_w_al_am_bl_tw_incl_w_imax5_if/ --mod mtswl -f abi --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt tw -i_tgt w -i_max 5 -i_type f
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink05_wlink_frp_l_attr_w_bl_tw/ --mod mtswl -f ab --mint e --tinm p -tmt trim -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt tw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink05_wlink_frp_l_attr_w_bl_tw_incl_w_imax5_if/ --mod mtsw -f abi --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt tw -i_tgt w -i_max 5 -i_type f
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
##
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l/ --mod l -f n -a_max 1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e/ --mod mt -f n --mint e --tinm e
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim/ --mod mt -f n --mint e --tinm e -tmt trim
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p/ --mod m -f n --mint p
##
##
### mint p trim: +attr ok
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim/ --mod m -f n --mint p -tmm trim
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim/ --mod t -f n --tinm p -tmt trim
##
##########################################################################
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_attr_l_anc09_ang01/ --mod l -f a -ar_tgt m -anc 0.9 -ang 0.1
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_bl_l/ --mod l -f b -bl_tgt l
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_incl_l_imax5_if/ --mod l -f i -i_tgt l -i_max 5 -i_type f
####0927-1750#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_attr_m_anc09_ang01/ --mod m -f a --mint e -ar_tgt m -anc 0.9 -ang 0.1
###
###latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_bl_m/ --mod m --mint e -f b -bl_tgt m
###latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_incl_m_imax5_if/ --mod m --mint e -f i -i_tgt m -i_max 5 -i_type f
###
###
###
###latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05/ --mod ms -f n --mint e -s_min 0.5
###0928-1410#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_mid/ --mod ms -f n --mint e -s_min 0.5 -s_prb mid
###0928-1308#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_raw/ --mod ms -f n --mint e -s_min 0.5 -s_prb raw
###latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink/ --mod msw -f n --mint e -s_min 0.5 --wlink
####0927-1750#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_f/ --mod msw -f n --mint e -s_min 0.5 --wlink f
####0927-1750#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_fp/ --mod msw -f n --mint e -s_min 0.5 --wlink fp
####0927-1750#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frpl/ --mod msw -f n --mint e -s_min 0.5 --wlink frpl
###
###${eval_script}
###
###
###0928-1308#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_raw_wlink_r/ --mod msw -f n --mint e -s_min 0.5 -s_prb raw --wlink r
###0928-1308#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_r/ --mod msw -f n --mint e -s_min 0.5 --wlink r
#
##ここからチェックの続き
#
###0928-1308#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_raw_wlink_frp/ --mod msw -f n --mint e -s_min 0.5 -s_prb raw --wlink frp
###0928-1506#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_mid_wlink_rp/ --mod msw -f n --mint e -s_min 0.5 -s_prb mid --wlink rp
###0928-1308#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_raw_wlink_rp/ --mod msw -f n --mint e -s_min 0.5 -s_prb raw --wlink rp
###0928-1308#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp/ --mod msw -f n --mint e -s_min 0.5 --wlink rp
##
####0927-1750#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rpl/ --mod msw -f n --mint e -s_min 0.5 --wlink rpl
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_bl_s/ --mod msw -f b --mint e -s_min 0.5 --wlink rp -bl_tgt s
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_raw_wlink_rp_bl_s/ --mod msw -f b --mint e -s_min 0.5 -s_prb raw --wlink rp -bl_tgt s
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_bl_w/ --mod msw -f b --mint e -s_min 0.5 --wlink rp -bl_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_raw_bl_w/ --mod msw -f b --mint e -s_min 0.5 -s_prb raw --wlink rp -bl_tgt w
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rpl_l_attr_msw_anc09_ang01_bl_sw_incl_sw_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink rpl -ar_tgt msw -anc 0.9 -ang 0.1 -bl_tgt sw -i_tgt sw -i_max 5 -i_type f
###
##${eval_script}
##
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_incl_mt_imax5_if/ --mod mt --mint e --tinm e -f i -i_tgt mt -i_max 5 -i_type f
##
##
###${eval_script}
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_attr_m_anc09_ang01/ --mod mt -f a --mint e --tinm e -ar_tgt m -anc 0.9 -ang 0.1
###0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_attr_t_anc09_ang01/ --mod mt -f a --mint e --tinm e -ar_tgt t -anc 0.9 -ang 0.1
###0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_bl_m/ --mod mt --mint e --tinm e -f b -bl_tgt m
###0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_bl_t/ --mod mt --mint e --tinm e -f b -bl_tgt t
###0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_slink05/ --mod mts -f n --mint e --tinm e -s_min 0.5
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_slink05_raw/ --mod mts -f n --mint e --tinm e -s_min 0.5 -s_prb raw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_slink05_wlink_frp_attr_m_anc09_ang01_incl_m_imax5_if_bl_mtw/ --mod mtsw -f abi --mint e --tinm e -s_min 0.5 --wlink frp -ar_tgt mw -anc 0.9 -ang 0.1 -i_tgt m -i_max 5 -i_type f -bl_tgt mtw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_slink05_raw_wlink_frp_attr_m_anc09_ang01_incl_m_imax5_if_bl_mtw/ --mod mtsw -f abi --mint e --tinm e -s_min 0.5 --wlink frp -ar_tgt mw -anc 0.9 -ang 0.1 -i_tgt m -i_max 5 -i_type f -bl_tgt mtw
##
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_slink05_wlink_fr_attr_m_anc09_ang01_incl_m_imax5_if_bl_mtw/ --mod mtsw -f abi --mint e --tinm e -s_min 0.5 --wlink fr -ar_tgt mw -anc 0.9 -ang 0.1 -i_tgt m -i_max 5 -i_type f -bl_tgt mtw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_slink05_raw_wlink_fr_attr_m_anc09_ang01_incl_m_imax5_if_bl_mtw/ --mod mtsw -f abi --mint e --tinm e -s_min 0.5 --wlink fr -ar_tgt mw -anc 0.9 -ang 0.1 -i_tgt m -i_max 5 -i_type f -bl_tgt mtw
##
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_incl_m_imax5_if/ --mod mt --mint e --tinm e -f i -i_tgt m -i_max 5 -i_type f
#
##${eval_script}
###retry
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_attr_t_anc09_ang01_al_r/ --mod mt -f a --mint e --tinm e -tmt trim -ar_tgt t -anc 0.9 -ang 0.1
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_attr_t_anc09_ang01_al_am/ --mod mt -f a --mint e --tinm e -tmt trim -ar_tgt t -anc 0.9 -ang 0.1 -al am
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_attr_t_anc09_ang01_al_am_bl_t/ --mod mt -f a --mint e --tinm e -tmt trim -ar_tgt t -anc 0.9 -ang 0.1 -al am -bl_tgt t
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_attr_t_anc09_ang01_al_am_bl_t_incl_t_imax5_if/ --mod mt -f abi --mint e --tinm e -tmt trim -ar_tgt t -anc 0.9 -ang 0.1 -al am -bl_tgt t -i_tgt t -i_max 5 -i_type f
#
###0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_attr_t_anc09_ang01_al_ar/ --mod mt -f a --mint e --tinm e -tmt trim -ar_tgt t -anc 0.9 -ang 0.1 -al ar
##
###retry
##
###0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_wlink_f/ --mod mtw -f n --mint e --tinm e --wlink f
###0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_wlink_fr/ --mod mtw -f n --mint e --tinm e --wlink fr
###0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_wlink_frp/ --mod mtw -f n --mint e --tinm e --wlink frp
###0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_wlink_frpl/ --mod mtw -f n --mint e --tinm e --wlink frpl
###0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_wlink_r/ --mod mtw -f n --mint e --tinm e --wlink r
###0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_wlink_rp/ --mod mtw -f n --mint e --tinm e --wlink rp
###0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_wlink_rpl/ --mod mtw -f n --mint e --tinm e --wlink rpl
##
##${eval_script}
##
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p/ --mod mt -f n --mint e --tinm p
###0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_attr_mt_anc09_ang01/ --mod mt -f a --mint e --tinm p -ar_tgt mt -anc 0.9 -ang 0.1 -al n
###0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_attr_mt_anc09_ang01_al_a/ --mod mt -f a --mint e --tinm p -ar_tgt mt -anc 0.9 -ang 0.1 -al a
###0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_attr_mt_anc09_ang01_al_am/ --mod mt -f a --mint e --tinm p -ar_tgt mt -anc 0.9 -ang 0.1 -al am
###0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_attr_mt_anc09_ang01_al_ar/ --mod mt -f a --mint e --tinm p -ar_tgt mt -anc 0.9 -ang 0.1 -al ar
###0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_attr_mt_anc09_ang01_al_r/ --mod mt -f a --mint e --tinm p -ar_tgt mt -anc 0.9 -ang 0.1 -al r
##
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_attr_t_anc09_ang01/ --mod mt -f a --mint e --tinm p -ar_tgt t -anc 0.9 -ang 0.1 -al n
###0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_attr_t_anc09_ang01_al_a/ --mod mt -f a --mint e --tinm p -ar_tgt t -anc 0.9 -ang 0.1 -al a
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_attr_t_anc09_ang01_al_am/ --mod mt -f a --mint e --tinm p -ar_tgt t -anc 0.9 -ang 0.1 -al am
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_attr_t_anc09_ang01_al_am_bl_t/ --mod mt -f a --mint e --tinm p -ar_tgt t -anc 0.9 -ang 0.1 -al am -bl_tgt t
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_attr_t_anc09_ang01_al_am_bl_t_incl_t_imax5_if/ --mod mt -f a --mint e --tinm p -ar_tgt t -anc 0.9 -ang 0.1 -al am -bl_tgt t -i_tgt t -i_max 5 -i_type f
#
###0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_attr_t_anc09_ang01_al_r/ --mod mt -f a --mint e --tinm p -ar_tgt t -anc 0.9 -ang 0.1 -al r
###0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_attr_t_anc09_ang01_al_ar/ --mod mt -f a --mint e --tinm p -ar_tgt t -anc 0.9 -ang 0.1 -al ar
##${eval_script}
#
#
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__mint_e__slink_raw_attr_w_anc09_ang01_al_am/ --mod w:m:s -f a --mint e -s_prb raw --wlink frp -ar_tgt w -anc 0.9 -ang 0.1 -al am
####0928-1555#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__mint_e_slink_attr_w_anc09_ang01_al_am/ --mod w:ms -f a --mint e --wlink frp -ar_tgt w -anc 0.9 -ang 0.1 -al am
####0928-1555#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__mint_e_slink_mid_attr_w_anc09_ang01_al_am/ --mod w:ms -f a --mint e -s_prb mid --wlink frp -ar_tgt w -anc 0.9 -ang 0.1 -al am
####0928-1555#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__mint_e_slink_raw_attr_w_anc09_ang01_al_am/ --mod w:ms -f a --mint e -s_prb raw --wlink frp -ar_tgt w -anc 0.9 -ang 0.1 -al am
###
#
#
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_trim/ --mod mt -f n --mint e --tinm p -tmt trim
###0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_trim_attr_t_anc09_ang01/ --mod mt -f a --mint e --tinm p -tmt trim -ar_tgt t -anc 0.9 -ang 0.1
###0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_trim_attr_t_anc09_ang01_al_a/ --mod mt -f a --mint e --tinm p -tmt trim -ar_tgt t -anc 0.9 -ang 0.1 -al a
###0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_trim_attr_t_anc09_ang01_al_am/ --mod mt -f a --mint e --tinm p -tmt trim -ar_tgt t -anc 0.9 -ang 0.1 -al am
###0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_trim_attr_t_anc09_ang01_al_ar/ --mod mt -f a --mint e --tinm p -tmt trim -ar_tgt t -anc 0.9 -ang 0.1 -al ar
###0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_trim_attr_t_anc09_ang01_al_r/ --mod mt -f a --mint e --tinm p -tmt trim -ar_tgt t -anc 0.9 -ang 0.1 -al r
##
##${eval_script}
##mint_e_trim +attr:OK
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_attr_m_anc09_ang01/ --mod m -f a --mint e -tmm trim -ar_tgt m -anc 0.9 -ang 0.1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_attr_m_anc09_ang01_al_r/ --mod m -f a --mint e -tmm trim -ar_tgt m -anc 0.9 -ang 0.1 -al r
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_attr_m_anc09_ang01_al_am/ --mod m -f a --mint e -tmm trim -ar_tgt m -anc 0.9 -ang 0.1 -al am
###0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_attr_m_anc09_ang01_al_ar/ --mod m -f a --mint e -tmm trim -ar_tgt m -anc 0.9 -ang 0.1 -al ar
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_bl_m/ --mod m --mint e -tmm trim -f b -bl_tgt m
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_incl_m_imax5_if/ --mod m -f i --mint e -tmm trim -i_tgt m -i_max 5 -i_type f
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_slink05_wlink_rp/ --mod msw -f n --mint e -tmm trim -s_min 0.5 --wlink rp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_slink05_raw_wlink_rp/ --mod msw -f n --mint e -tmm trim -s_min 0.5 -s_prb raw --wlink rp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_slink05_wlink_rp_attr_m_anc09_ang01/ --mod msw -f a --mint e -tmm trim -s_min 0.5 --wlink rp -ar_tgt m -anc 0.9 -ang 0.1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_slink05_wlink_rp_attr_mw_anc09_ang01/ --mod msw -f a --mint e -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw -anc 0.9 -ang 0.1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_slink05_wlink_rp_attr_ms_anc09_ang01/ --mod msw -f a --mint e -tmm trim -s_min 0.5 --wlink rp -ar_tgt ms -anc 0.9 -ang 0.1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_slink05_wlink_rp_attr_s_anc09_ang01/ --mod msw -f a --mint e -tmm trim -s_min 0.5 --wlink rp -ar_tgt s -anc 0.9 -ang 0.1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_slink05_wlink_rp_attr_w_anc09_ang01/ --mod msw -f a --mint e -tmm trim -s_min 0.5 --wlink rp -ar_tgt w -anc 0.9 -ang 0.1
##
###${eval_script}
##
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_attr_m_anc09_ang01/ --mod mt -f a --mint e --tinm -e -tmm trim -ar_tgt m -anc 0.9 -ang 0.1
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_attr_m_anc09_ang01_al_am/ --mod mt -f a --mint e --tinm e -tmm trim -ar_tgt m -anc 0.9 -ang 0.1 -al am
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_attr_m_anc09_ang01_al_am_bl_t/ --mod mt -f a --mint e --tinm e -tmm trim -ar_tgt m -anc 0.9 -ang 0.1 -al am -bl mt
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_attr_m_anc09_ang01_al_am_bl_t_incl_t_imax5_if/ --mod mt -f a --mint e --tinm e -tmm trim -ar_tgt m -anc 0.9 -ang 0.1 -al am -bl_tgt mt -i_tgt t -i_max 5 -i_type f
#
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_attr_m_anc09_ang01_al_r/ --mod mt -f a --mint e --tinm e -tmm trim -ar_tgt m -anc 0.9 -ang 0.1 -al r
#
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p/ --mod mt -f n --mint e -tmm trim --tinm p
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_attr_m_anc09_ang01/ --mod mt -f a --mint e --tinm -p -tmm trim -ar_tgt m -anc 0.9 -ang 0.1
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_attr_m_anc09_ang01_al_am/ --mod mt -f a --mint e --tinm p -tmm trim -ar_tgt m -anc 0.9 -ang 0.1 -al am
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_attr_m_anc09_ang01_al_am_bl_t/ --mod mt -f a --mint e --tinm p -tmm trim -ar_tgt m -anc 0.9 -ang 0.1 -al am -bl t
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_attr_m_anc09_ang01_al_am_bl_t_incl_t_imax5_if/ --mod mt -f a --mint e --tinm p -tmm trim -ar_tgt m -anc 0.9 -ang 0.1 -al am -bl_tgt mt -i_tgt t -i_max 5 -i_type f
#
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_trim/ --mod mt -f n --mint e -tmm trim --tinm p -tmt trim
#
###0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_wlink_frp/ --mod mw -f n --mint e --wlink frp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_wlink_frpl/ --mod mw -f n --mint e --wlink frpl
###0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_wlink_r/ --mod mw -f n --mint e --wlink r
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_wlink_r_attr_w_anc09_ang01/ --mod mw -f a --mint e --wlink r -ar_tgt w -anc 0.9 -ang 0.1
###0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_wlink_rp/ --mod mw -f n --mint e --wlink rp
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_wlink_rp_attr_m_anc09_ang01/ --mod mw -f a --mint e --wlink rp -ar_tgt m -anc 0.9 -ang 0.1
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_wlink_rp_attr_w_anc09_ang01/ --mod mw -f a --mint e --wlink rp -ar_tgt w -anc 0.9 -ang 0.1
##
##${eval_script}
##
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_cmax100/ --mod m -f n --mint p -c_max 100
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_cmax10/ --mod m -f n --mint p -c_max 10
###0927-1750#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_attr_m_anc09_ang01/ --mod m -f a --mint p -ar_tgt m -anc 0.9 -ang 0.1
###0927-1750#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_attr_m_anc09_ang01_al_r/ --mod m -f a --mint p -ar_tgt m -anc 0.9 -ang 0.1 -al r
###0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_attr_m_anc09_ang01_al_am/ --mod m -f a --mint p -ar_tgt m -anc 0.9 -ang 0.1 -al am
###0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_attr_m_anc09_ang01_al_ar/ --mod m -f a --mint p -ar_tgt m -anc 0.9 -ang 0.1 -al ar
##
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_attr_m_anc09_ang01_bl_m/ --mod m --mint p -f ab -ar_tgt m -anc 0.9 -ang 0.1 -bl_tgt m
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_attr_m_anc09_ang01_bl_m_incl_m_imax5_if/ --mod m --mint p -f abi -ar_tgt m -anc 0.9 -ang 0.1 -bl_tgt m -i_tgt m -i_max 5 -i_type f
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_attr_m_anc09_ang01_incl_m_imax5_if/ --mod m --mint p -f ai -ar_tgt m -anc 0.9 -ang 0.1 -i_tgt m -i_max 5 -i_type f
###0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_bl_m/ --mod m --mint p -f b -bl_tgt m
###0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_incl_m_imax5_if/ --mod m --mint p -f i -i_tgt m -i_max 5 -i_type f
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_bl_m_incl_m_imax5_if/ --mod m --mint p -f bi -bl_tgt m -i_tgt m -i_max 5 -i_type f
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05/ --mod ms -f n --mint p -s_min 0.5
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_attr_m_anc09_ang01/ --mod ms -f a --mint p -s_min 0.5 -ar_tgt m
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_m_incl_w_imax5_if/ --mod msw -f i --mint p --wlink m -s_min 0.5 -i_tgt w -i_max 5 -i_type f
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_mp_incl_w_imax5_if/ --mod msw -f i --mint p --wlink mp -s_min 0.5 -i_tgt w -i_max 5 -i_type f
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_r/ --mod msw -f n --mint p -s_min 0.5 --wlink r
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_rp/ --mod msw -f n --mint p -s_min 0.5 --wlink rp
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_r_attr_m_anc09_ang01/ --mod msw -f a --mint p -s_min 0.5 --wlink r -ar_tgt m -anc 0.9 -ang 0.1
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_rp_attr_m_anc09_ang01/ --mod msw -f a --mint p -s_min 0.5 --wlink rp -ar_tgt m -anc 0.9 -ang 0.1
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_r_attr_ms_anc09_ang01/ --mod msw -f a --mint p -s_min 0.5 --wlink r -ar_tgt ms -anc 0.9 -ang 0.1
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_rp_attr_ms_anc09_ang01/ --mod msw -f a --mint p -s_min 0.5 --wlink rp -ar_tgt ms -anc 0.9 -ang 0.1
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_r_attr_msw_anc09_ang01/ --mod msw -f a --mint p -s_min 0.5 --wlink r -ar_tgt msw -anc 0.9 -ang 0.1
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_rp_attr_msw_anc09_ang01/ --mod msw -f a --mint p -s_min 0.5 --wlink rp -ar_tgt msw -anc 0.9 -ang 0.1
##
###${eval_script}
#
##mint p trim: +attr: ok
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_attr_m_anc09_ang01/ --mod m -f a --mint p -tmm trim -ar_tgt m -anc 0.9 -ang 0.1
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_attr_m_anc09_ang01_al_a/ --mod m -f a --mint p -tmm trim -ar_tgt m -anc 0.9 -ang 0.1 -al am
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_attr_m_anc09_ang01_al_am/ --mod m -f a --mint p -tmm trim -ar_tgt m -anc 0.9 -ang 0.1 -al am
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_attr_m_anc09_ang01_al_ar/ --mod m -f a --mint p -tmm trim -ar_tgt m -anc 0.9 -ang 0.1 -al ar
##
###0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_bl_m/ --mod m -f b --mint p -tmm trim -bl_tgt m
###0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_incl_m_imax5_if/ --mod m -f i --mint p -tmm trim -i_tgt m -i_max 5 -i_type f
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_wlink_r/ --mod mw -f n --mint p --wlink r
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_wlink_rp/ --mod mw -f n --mint p --wlink rp
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_wlink_r_attr_m_anc09_ang01/ --mod mw -f a --mint p --wlink r -ar_tgt m -anc 0.9 -ang 0.1
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_wlink_rp_attr_m_anc09_ang01/ --mod mw -f a --mint p --wlink rp -ar_tgt m -anc 0.9 -ang 0.1
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_wlink_r_attr_mw_anc09_ang01/ --mod mw -f a --mint p --wlink r -ar_tgt mw -anc 0.9 -ang 0.1
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_wlink_rp_attr_mw_anc09_ang01/ --mod mw -f a --mint p --wlink rp -ar_tgt mw -anc 0.9 -ang 0.1
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p04/ --mod m -f n --mint p -m_min 0.4
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p06/ --mod m -f n --mint p -m_min 0.6
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p08/ --mod m -f n --mint p -m_min 0.8
##
##${eval_script}
##
####slink系
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid/ --mod s -f n -s_min 0.5 -s_prb mid
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_raw/ --mod s -f n -s_min 0.5 -s_prb raw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_attr_s_anc09_ang01/ --mod s -f a -s_min 0.5 -ar_tgt s -anc 0.9 -ang 0.1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_attr_s_anc09_ang01_al_r/ --mod s -f a -s_min 0.5 -ar_tgt s -anc 0.9 -ang 0.1 -al r
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_attr_s_anc09_ang01_al_ar/ --mod s -f a -s_min 0.5 -ar_tgt s -anc 0.9 -ang 0.1 -al ar
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_attr_s_anc09_ang01_al_am/ --mod s -f a -s_min 0.5 -ar_tgt s -anc 0.9 -ang 0.1 -al am
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_raw_attr_s_anc09_ang01_al_am/ --mod s -f a -s_min 0.5 -s_prb raw -ar_tgt s -anc 0.9 -ang 0.1 -al am
###
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_attr_s_anc09_ang01_bl_s/ --mod s -f ab -s_min 0.5 -ar_tgt s -anc 0.9 -ang 0.1 -bl_tgt s
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_attr_s_anc09_ang01_bl_s_incl_s_imax5_if/ --mod s -f abi -s_min 0.5 -ar_tgt s -anc 0.9 -ang 0.1 -bl_tgt s -i_tgt s -i_max 5 -i_type f
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_attr_s_anc09_ang01_incl_s_imax5_if/ --mod s -f ai -s_min 0.5 -ar_tgt s -anc 0.9 -ang 0.1 -i_tgt s -i_max 5 -i_type f
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_bl_s/ --mod s -f b -s_min 0.5 -bl_tgt s
###0928-1410#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid_bl_s/ --mod s -f b -s_min 0.5 -s_prb mid -bl_tgt s
###0928-1410#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_raw_bl_s/ --mod s -f b -s_min 0.5 -s_prb raw -bl_tgt s
##
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_incl_s_imax5_if/ --mod s -f i -s_min 0.5 -i_tgt s -i_max 5 -i_type f
###0928-1410#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid_incl_s_imax5_if/ --mod s -f i -s_min 0.5 -s_prb mid -i_tgt s -i_max 5 -i_type f
###0928-1410#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_raw_incl_s_imax5_if/ --mod s -f i -s_min 0.5 -s_prb raw -i_tgt s -i_max 5 -i_type f
#
###0928-1410#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_wlink_rp/ --mod sw -f n  -s_min 0.5 --wlink rp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__wlink_rp__mint_e/ --mod s:w:m -f n --mint e -s_min 0.5 --wlink rp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__wlink_rp__mint_e_tinm_e_trim/ --mod s:w:mt -f n --mint e --tinm e -tmt trim -s_min 0.5 --wlink rp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__wlink_rp__mint_e_tinm_p/ --mod s:w:mt -f n --mint e --tinm p -s_min 0.5 --wlink rp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__wlink_rp__mint_e_trim_tinm_e/ --mod s:w:mt -f n --mint e --tinm e -tmm trim -s_min 0.5 --wlink rp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__wlink_rp_mint_e_trim__tinm_e/ --mod s:mw:t -f n --mint e -tmm trim --tinm e -s_min 0.5 --wlink rp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__wlink_rp_mint_e_trim__tinm_e_bl_t/ --mod s:mw:t -f n --mint e -tmm trim --tinm e -s_min 0.5 --wlink rp -bl_tgt t
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__wlink_rp_mint_e_trim__tinm_e_bl_tw/ --mod s:mw:t -f n --mint e -tmm trim --tinm e -s_min 0.5 --wlink rp -bl_tgt tw
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__wlink_rp_mint_e_trim__tinm_e_bl_tw_i_tw/ --mod s:mw:t -f n --mint e -tmm trim --tinm e -s_min 0.5 --wlink rp -bl_tgt tw -i_tgt tw -i_max 5 -i_type f
##
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__wlink_rp_mint_e__tinm_e/ --mod s:mw:t -f n --mint e --tinm e -s_min 0.5 --wlink rp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__wlink_rp_mint_e__tinm_e_trim/ --mod s:mw:t -f n --mint e --tinm e -tmt trim -s_min 0.5 --wlink rp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__wlink_rp_mint_e__tinm_p/ --mod s:mw:t -f n --mint e --tinm p -s_min 0.5 --wlink rp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05__wlink_rp_mint_e__tinm_p_trim/ --mod s:mw:t -f n --mint e --tinm p -tmt trim -s_min 0.5 --wlink rp
##
###0928-1410#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mid_wlink_rp/ --mod sw -f n -s_min 0.5 -s_prb mid --wlink rp
###0928-1410#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_raw_wlink_rp/ --mod sw -f n -s_min 0.5 -s_prb raw --wlink rp
## #${eval_script}
##
###0928-1308#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink06_raw/ --mod s -f n -s_min 0.6 -s_prb raw
###0928-1506#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink06_mid/ --mod s -f n -s_min 0.6 -s_prb mid
###0928-1410#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink07_mid/ --mod s -f n -s_min 0.7 -s_prb mid
###0928-1308#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink07_raw/ --mod s -f n -s_min 0.7 -s_prb raw
## #${eval_script}
##
####tinm系
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_attr_t_anc09_ang01/ --mod t -f a --tinm e  -ar_tgt t -anc 0.9 -ang 0.1
####0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_attr_t_anc09_ang01_al_a/ --mod t -f a --tinm e  -ar_tgt t -anc 0.9 -ang 0.1 -al a
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_attr_t_anc09_ang01_al_am/ --mod t -f a --tinm e  -ar_tgt t -anc 0.9 -ang 0.1 -al am
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_attr_t_anc09_ang01_al_am_bl_t/ --mod t -f a --tinm e  -ar_tgt t -anc 0.9 -ang 0.1 -al am -bl_tgt t
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_attr_t_anc09_ang01_al_am_bl_t_incl_t_imax5_if/ --mod t -f a --tinm e  -ar_tgt t -anc 0.9 -ang 0.1 -al am -bl_tgt t -i_tgt t -i_max 5 -i_type f
#
####0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_attr_t_anc09_ang01_al_ar/ --mod t -f a --tinm e  -ar_tgt t -anc 0.9 -ang 0.1 -al ar
####0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_attr_t_anc09_ang01_al_r/ --mod t -f a --tinm e  -ar_tgt t -anc 0.9 -ang 0.1 -al r
###
####0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_bl_t/ --mod t -f b --tinm e  -bl_tgt t
###
##${eval_script}
###
####0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_incl_t_imax5_if/ --mod t -f i --tinm e -i_tgt t -i_max 5 -i_type f
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_slink05/ --mod ts -f n --tinm e -s_min 0.5
#
## tinm_e_trim: +attr: ok
###
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_trim_attr_t_anc09_ang01/ --mod t -f a --tinm e -tmt trim -ar_tgt t -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_trim_attr_t_anc09_ang01_al_a/ --mod t -f a --tinm e -tmt trim -ar_tgt t -anc 0.9 -ang 0.1 -al a
##latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_trim_attr_t_anc09_ang01_al_am/ --mod t -f a --tinm e -tmt trim -ar_tgt t -anc 0.9 -ang 0.1 -al am
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_trim_attr_t_anc09_ang01_al_ar/ --mod t -f a --tinm e -tmt trim -ar_tgt t -anc 0.9 -ang 0.1 -al ar
###
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_wlink_r/ --mod tw -f n --tinm e --wlink r
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_wlink_rp/ --mod tw -f n --tinm e --wlink rp
###
### #${eval_script}
###
####0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_attr_t_anc09_ang01/ --mod t -f a --tinm p  -ar_tgt t -anc 0.9 -ang 0.1
####0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_attr_t_anc09_ang01_al_a/ --mod t -f a --tinm p  -ar_tgt t -anc 0.9 -ang 0.1 -al a
####0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_attr_t_anc09_ang01_al_am/ --mod t -f a --tinm p -ar_tgt t -anc 0.9 -ang 0.1 -al am
####0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_attr_t_anc09_ang01_al_ar/ --mod t -f a --tinm p -ar_tgt t -anc 0.9 -ang 0.1 -al ar
####0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_attr_t_anc09_ang01_al_r/ --mod t -f a --tinm p  -ar_tgt t -anc 0.9 -ang 0.1 -al r
####0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_attr_t_anc09_ang01_bl_t/ --mod t --tinm p -f ab -ar_tgt t -anc 0.9 -ang 0.1 -bl_tgt t
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_attr_t_anc09_ang01_bl_t_incl_t_imax5_if/ --mod t -f abi --tinm p -ar_tgt t -anc 0.9 -ang 0.1 -bl_tgt t -i_tgt t -i_max 5 -i_type f
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_attr_t_anc09_ang01_incl_t_imax5_if/ --mod t -f ai --tinm p -ar_tgt t -anc 0.9 -ang 0.1 -i_tgt t -i_max 5 -i_type f
####0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_bl_t/ --mod t -f b --tinm p  -bl_tgt t
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_bl_t_incl_t_imax5_if/ --mod t -f bi --tinm p -bl_tgt t -i_tgt t -i_max 5 -i_type f
### #${eval_script}
###
####0928-0830#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_incl_t_imax5_if/ --mod t -f i --tinm p -i_tgt t -i_max 5 -i_type f
##latest#python script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_attr_t_anc09_ang01/ --mod t -f a --tinm p -tmt trim -ar_tgt t -anc 0.9 -ang 0.1
##latest#python script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_attr_t_anc09_ang01_al_m/ --mod t -f a --tinm p -tmt trim -ar_tgt t -anc 0.9 -ang 0.1 -al m
####0928-0830#python script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_attr_t_anc09_ang01_al_r/ --mod t -f a --tinm p -tmt trim -ar_tgt t -anc 0.9 -ang 0.1 -al r
####0928-0830#python script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_attr_t_anc09_ang01_al_ar/ --mod t -f a --tinm p -tmt trim -ar_tgt t -anc 0.9 -ang 0.1 -al ar
###
####0928-0830#python script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_bl_t/ --mod t -f b --tinm p -tmt trim -bl_tgt t
###
### #${eval_script}
###
####0927-1750#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink f -ar_tgt w -anc 0.9 -ang 0.1 -al r
####0926-1930#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_attr_w_anc09_ang01_al_ar/ --mod w -f a --wlink f -ar_tgt w -anc 0.9 -ang 0.1 -al ar
###
#######latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_attr_w_anc09_ang01/ --mod w -f a --wlink f -ar_tgt w -anc 0.9 -ang 0.1
####0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_incl_w_imax5_if/ --mod w -f i --wlink f -i_tgt w -i_max 5 -i_type f
####0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_bl_w/ --mod w -f b --wlink f -bl_tgt w
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_slink05_mint_e/ --mod msw: -f n --mint e -s_min 0.5 --wlink f
###
###
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fl/ --mod w -f n --wlink fl
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fl_attr_w_anc09_ang01/ --mod w -f a --wlink fl -ar_tgt w -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fl_attr_w_anc09_ang01_al_a/ --mod w -f a --wlink fl -ar_tgt w -anc 0.9 -ang 0.1 -al a
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fl_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink fl -ar_tgt w -anc 0.9 -ang 0.1 -al r
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fl_attr_w_anc09_ang01_al_am/ --mod w -f a --wlink fl -ar_tgt w -anc 0.9 -ang 0.1 -al am
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fl_attr_w_anc09_ang01_al_ar/ --mod w -f a --wlink fl -ar_tgt w -anc 0.9 -ang 0.1 -al ar
####0927-1750#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fl_wls05_wlb03_wlf02_attr_w_anc09_ang01/ --mod w -f a --wlink fl　-wls 0.5 -wlb 0.3 -wlf 0.2 -ar_tgt w -anc 0.9 -ang 0.1
####0927-1750#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fl_wls05_wlb03_wlf02_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink fl -wls 0.5 -wlb 0.3 -wlf 0.2 -ar_tgt w -anc 0.9 -ang 0.1 -al r
####0926-1930#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fl_wls05_wlb03_wlf02_attr_w_anc09_ang01_al_ar/ --mod w -f a --wlink fl -wls 0.5 -wlb 0.3 -wlf 0.2 -ar_tgt w -anc 0.9 -ang 0.1 -al ar
###
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fl_bl_w/ --mod w -f b --wlink fl -bl_tgt w
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fl_incl_w_imax5_if/ --mod w -f i --wlink fl -i_tgt w -i_max 5 -i_type f
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fp/ --mod w -f n --wlink fp
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fp_attr_w_anc09_ang01/ --mod w -f a --wlink fp -ar_tgt w -anc 0.9 -ang 0.1
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fp_bl_w/ --mod w -f b --wlink fp -bl_tgt w
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fp_incl_w_imax5_if/ --mod w -f i --wlink fp -i_tgt w -i_max 5 -i_type f
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fp_slink05_mint_e/ --mod msw: -f n --mint e -s_min 0.5 --wlink fp
####
####
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fpl/ --mod w -f n --wlink fpl
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fpl_attr_w_anc09_ang01/ --mod w -f a --wlink fpl -ar_tgt w -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fpl_attr_w_anc09_ang01_al_am/ --mod w -f a --wlink fpl -ar_tgt w -anc 0.9 -ang 0.1 -al ampython $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fpl_attr_w_anc09_ang01_al_ar/ --mod w -f a --wlink fpl -ar_tgt w -anc 0.9 -ang 0.1 -al ar
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fpl_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink fpl -ar_tgt w -anc 0.9 -ang 0.1 -al r
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fpl_wls05_wlb03_wlf02/ --mod w -f n --wlink fpl -wls 0.5 -wlb 0.3 -wlf 0.2
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fpl_wls05_wlb03_wlf02_attr_w_anc09_ang01/ --mod w -f a --wlink fpl -wls 0.5 -wlb 0.3 -wlf 0.2 -ar_tgt w -anc 0.9 -ang 0.1
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fpl_wls05_wlb03_wlf02_attr_w_anc09_ang01_al_am/ --mod w -f a --wlink fpl -wls 0.5 -wlb 0.3 -wlf 0.2 -ar_tgt w -anc 0.9 -ang 0.1 -al am
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fpl_wls05_wlb03_wlf02_attr_w_anc09_ang01_al_ar/ --mod w -f a --wlink fpl -wls 0.5 -wlb 0.3 -wlf 0.2 -ar_tgt w -anc 0.9 -ang 0.1 -al ar
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fpl_wls05_wlb03_wlf02_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink fpl -wls 0.5 -wlb 0.3 -wlf 0.2 -ar_tgt w -anc 0.9 -ang 0.1 -al r
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fpl_bl_w/ --mod w -f b --wlink fpl -bl_tgt w
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fpl_incl_w_imax5_if/ --mod w -f i --wlink fpl -i_tgt w -i_max 5 -i_type f
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fr/ --mod w -f n --wlink fr
#####0927-1750#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fr_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink fr -ar_tgt w -anc 0.9 -ang 0.1 -al r
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fr_attr_w_anc09_ang01_al_am/ --mod w -f a --wlink fr -ar_tgt w -anc 0.9 -ang 0.1 -al am
#####0926-1930#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fr_attr_w_anc09_ang01_al_ar/ --mod w -f a --wlink fr -ar_tgt w -anc 0.9 -ang 0.1 -al ar
####
########latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fr_attr_w_anc09_ang01/ --mod w -f a --wlink fr -ar_tgt w -anc 0.9 -ang 0.1
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fr_incl_w_imax5_if/ --mod w -f i --wlink fr -i_tgt w -i_max 5 -i_type f
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fr_bl_w/ --mod w -f b --wlink fr -bl_tgt w
########python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fr_slink05_mint_e/ --mod msw: -f n --mint e -s_min 0.5 --wlink fr
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp_attr_w_anc09_ang01/ --mod w -f a --wlink frp -ar_tgt w -anc 0.9 -ang 0.1 -al n
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink frp -ar_tgt w -anc 0.9 -ang 0.1 -al r
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp_attr_w_anc09_ang01_al_ar/ --mod w -f a --wlink frp -ar_tgt w -anc 0.9 -ang 0.1 -al ar
###
###
####retry
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__mint_e__slink_attr_w_anc09_ang01_al_am/ --mod w:m:s -f a --mint e --wlink frp -ar_tgt w -anc 0.9 -ang 0.1 -al am
####0928-1555#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__mint_e__slink_mid_attr_w_anc09_ang01_al_am/ --mod w:m:s -f a --mint e -s_prb mid --wlink frp -ar_tgt w -anc 0.9 -ang 0.1 -al am
####retry
#
#
#####0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp_bl_w/ --mod w -f b --wlink frp -bl_tgt w
#####0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp_incl_w_imax5_if/ --mod w -f i --wlink frp -i_tgt w -i_max 5 -i_type f
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl_attr_w_anc09_ang01/ --mod w -f a --wlink frpl -ar_tgt w -anc 0.9 -ang 0.1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl_attr_w_anc09_ang01_al_a/ --mod w -f a --wlink frpl -ar_tgt w -anc 0.9 -ang 0.1 -al a
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl_attr_w_anc09_ang01_al_am/ --mod w -f a --wlink frpl -ar_tgt w -anc 0.9 -ang 0.1 -al ar
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl_attr_w_anc09_ang01_al_ar/ --mod w -f a --wlink frpl -ar_tgt w -anc 0.9 -ang 0.1 -al ar
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink frpl -ar_tgt w -anc 0.9 -ang 0.1 -al r
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl_wls05_wlb03_wlf02/ --mod w -f n --wlink frpl -wls 0.5 -wlb 0.3 -wlf 0.2
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl_wls05_wlb03_wlf02_attr_w_anc09_ang01/ --mod w -f a --wlink frpl -wls 0.5 -wlb 0.3 -wlf 0.2 -ar_tgt w -anc 0.9 -ang 0.1
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl_wls05_wlb03_wlf02_attr_w_anc09_ang01_al_am/ --mod w -f a --wlink frpl -wls 0.5 -wlb 0.3 -wlf 0.2 -ar_tgt w -anc 0.9 -ang 0.1 -al am
####
#####0927-1430#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls05_wlb03_wlf03/ --mod w -f n --wlink l -wls 0.5 -wlb 0.3 -wlf 0.3
#####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls05_wlb03_wlf02/ --mod w -f n --wlink l -wls 0.5 -wlb 0.3 -wlf 0.2
#####0927-1430#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls05_wlb03_wlf01/ --mod w -f n --wlink l -wls 0.5 -wlb 0.3 -wlf 0.1
#####0927-1430#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls05_wlb04_wlf03/ --mod w -f n --wlink l -wls 0.5 -wlb 0.4 -wlf 0.3
#####0927-1430#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls05_wlb04_wlf02/ --mod w -f n --wlink l -wls 0.5 -wlb 0.4 -wlf 0.2
#####0927-1430#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls05_wlb04_wlf01/ --mod w -f n --wlink l -wls 0.5 -wlb 0.4 -wlf 0.1
#####0927-1430#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls04_wlb03_wlf03/ --mod w -f n --wlink l -wls 0.4 -wlb 0.3 -wlf 0.3
#####0927-1430#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls04_wlb03_wlf02/ --mod w -f n --wlink l -wls 0.4 -wlb 0.3 -wlf 0.2
#####0927-1430#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls04_wlb03_wlf01/ --mod w -f n --wlink l -wls 0.4 -wlb 0.3 -wlf 0.1
#####0927-1430#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls03_wlb03_wlf03/ --mod w -f n --wlink l -wls 0.3 -wlb 0.3 -wlf 0.3
#####0927-1430#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls03_wlb03_wlf02/ --mod w -f n --wlink l -wls 0.3 -wlb 0.3 -wlf 0.2
#####0927-1430#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls03_wlb02_wlf01/ --mod w -f n --wlink l -wls 0.3 -wlb 0.3 -wlf 0.1
####
#### #${eval_script}
####
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_m_attr_w_anc09_ang01/ --mod w -f a --wlink m -ar_tgt w -anc 0.9 -ang 0.1
#####0927-1750#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_m_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink m -ar_tgt w -anc 0.9 -ang 0.1 -al r
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_m_attr_w_anc09_ang01_al_ar/ --mod w -f a --wlink m -ar_tgt w -anc 0.9 -ang 0.1 -al ar
###
####
####
########python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_m_attr_w_anc09_ang01_incl_w_imax5_if/ --mod w -f ai --wlink m -ar_tgt w -anc 0.9 -ang 0.1 -i_tgt w -i_max 5 -i_type f
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_m_incl_w_imax5_if/ --mod w -f i --wlink m -i_tgt w -i_max 5 -i_type f
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_m_bl_w/ --mod w -f b --wlink m -bl_tgt w
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_ml/ --mod w -f n --wlink ml
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_ml_attr_w_anc09_ang01/ --mod w -f a --wlink ml -ar_tgt w -anc 0.9 -ang 0.1
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_ml_attr_w_anc09_ang01_al_a/ --mod w -f a --wlink ml -ar_tgt w -anc 0.9 -ang 0.1 -al a
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_ml_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink ml -ar_tgt w -anc 0.9 -ang 0.1 -al r
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_ml_attr_w_anc09_ang01_al_am/ --mod w -f a --wlink ml -ar_tgt w -anc 0.9 -ang 0.1 -al am
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_ml_attr_w_anc09_ang01_al_ar/ --mod w -f a --wlink ml -ar_tgt w -anc 0.9 -ang 0.1 -al ar
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_ml_attr_w_anc09_ang01_incl_w_imax5_if/ --mod w -f ai --wlink ml -ar_tgt w -anc 0.9 -ang 0.1 -i_tgt w -i_max 5 -i_type f
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_ml_bl_w/ --mod w -f b --wlink ml -bl_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_ml_incl_w_imax5_if/ --mod w -f i --wlink ml -i_tgt w -i_max 5 -i_type f
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mp/ --mod w -f n --wlink mp
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mp_attr_w_anc09_ang01/ --mod w -f a --wlink mp -ar_tgt w -anc 0.9 -ang 0.1
#####0927-1750#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mp_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink mp -ar_tgt w -anc 0.9 -ang 0.1 -al r
#####0926-1930#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mp_attr_w_anc09_ang01_al_ar/ --mod w -f a --wlink mp -ar_tgt w -anc 0.9 -ang 0.1 -al ar
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mp_attr_w_anc09_ang01_al_am/ --mod w -f a --wlink mp -ar_tgt w -anc 0.9 -ang 0.1 -al am
###
########python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mp_attr_w_anc09_ang01_incl_w_imax5_if/ --mod w -f ai --wlink mp -ar_tgt w -anc 0.9 -ang 0.1 -i_tgt w -i_max 5 -i_type f
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mp_incl_w_imax5_if/ --mod w -f i --wlink mp -i_tgt w -i_max 5 -i_type f
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mp_bl_w/ --mod w -f b --wlink mp -bl_tgt w
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mpl/ --mod w -f n --wlink mpl
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mpl_attr_w_anc09_ang01/ --mod w -f a --wlink mpl -ar_tgt w -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mpl_attr_w_anc09_ang01_al_am/ --mod w -f a --wlink mpl -ar_tgt w -anc 0.9 -ang 0.1 -al am
###
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mpl_attr_w_anc09_ang01_incl_w_imax5_if/ --mod w -f ai --wlink mpl -ar_tgt w -anc 0.9 -ang 0.1 -i_tgt w -i_max 5 -i_type f
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mpl_bl_w/ --mod w -f b --wlink mpl -bl_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mpl_incl_w_imax5_if/ --mod w -f i --wlink mpl -i_tgt w -i_max 5 -i_type f
####
##### #${eval_script}
####
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_attr_w_anc09_ang01/ --mod w --wlink r -f a -ar_tgt w -anc 0.9 -ang 0.1
#####0927-1750#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_attr_w_anc09_ang01_al_r/ --mod w --wlink r -f a -ar_tgt w -anc 0.9 -ang 0.1 -al r
#####0926-1930#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_attr_w_anc09_ang01_al_ar/ --mod w --wlink r -f a -ar_tgt w -anc 0.9 -ang 0.1 -al ar
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_attr_w_anc09_ang01_al_am/ --mod w --wlink r -f a -ar_tgt w -anc 0.9 -ang 0.1 -al am
###
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_incl_w_imax5_if/ --mod w -f i --wlink r -i_tgt w -i_max 5 -i_type f
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_bl_w/ --mod w -f b --wlink r -bl_tgt w
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl/ --mod w -f n --wlink rl
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_attr_w_anc09_ang01/ --mod w -f a --wlink rl -ar_tgt w -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_attr_w_anc09_ang01_al_am/ --mod w -f a --wlink rl -ar_tgt w -anc 0.9 -ang 0.1 -al am
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink rl -ar_tgt w -anc 0.9 -ang 0.1 -al r
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_attr_w_anc09_ang01_al_ar/ --mod w -f a --wlink rl -ar_tgt w -anc 0.9 -ang 0.1 -al ar
####
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bl_w/ --mod w -f b --wlink rl -bl_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_incl_w_imax5_if/ --mod w -f i --wlink rl -i_tgt w -i_max 5 -i_type f
####${eval_script}
####
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp_attr_w_anc09_ang01/ --mod w -f a --wlink rp -ar_tgt w -anc 0.9 -ang 0.1
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink rp -ar_tgt w -anc 0.9 -ang 0.1 -al r
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp_attr_w_anc09_ang01_al_am/ --mod w -f a --wlink rp -ar_tgt w -anc 0.9 -ang 0.1 -al am
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp_attr_w_anc09_ang01_al_ar/ --mod w -f a --wlink rp -ar_tgt w -anc 0.9 -ang 0.1 -al ar
###
####
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp_bl_w/ --mod w -f b --wlink rp -bl_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp_incl_w_imax5_if/ --mod w -f i --wlink rp -i_tgt w -i_max 5 -i_type f
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rpl/ --mod w -f n --wlink rpl
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rpl_attr_w_anc09_ang01/ --mod w -f a --wlink rpl -ar_tgt w -anc 0.9 -ang 0.1
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rpl_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink rpl -ar_tgt w -anc 0.9 -ang 0.1 -al r
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rpl_attr_w_anc09_ang01_al_ar/ --mod w -f a --wlink rpl -ar_tgt w -anc 0.9 -ang 0.1 -al ar
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rpl_attr_w_anc09_ang01_al_am/ --mod w -f a --wlink rpl -ar_tgt w -anc 0.9 -ang 0.1 -al am
####
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rpl_attr_w_anc09_ang01_incl_w_imax5_if/ --mod w -f ai --wlink rpl -ar_tgt w -anc 0.9 -ang 0.1 -i_tgt w -i_max 5 -i_type f
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rpl_incl_w_imax5_if/ --mod w -f i --wlink rpl -i_tgt w -i_max 5 -i_type f
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rpl_bl_w/ --mod w -f b --wlink rpl -bl_tgt w
#${eval_script}
#
#
##rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210926/*_pre.tsv
##rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210926/*/*_summary.tsv
##rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210926/*/*_anal.tsv
##rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210926/*/*_fn.tsv
##rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210926/*/Airport.tsv
##rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210926/*/City.tsv
##rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210926/*/Company.tsv
##rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210926/*/Compound.tsv
##rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210926/*/Conference.tsv
##rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210926/*/Lake.tsv
##rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210926/*/Person.tsv
##rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210926/*/*.tsv
##grep 'latest' ~/PycharmProjects/linkjpc/linkjpc_all_sample.sh |  awk '{print $6}' | perl -pe 's/\${out_dir_base}//;' | perl -pe 's/\///g;' | sort | uniq > $eval_target$$
###grep 'script' ~/PycharmProjects/linkjpc/linkjpc_all_sample.sh | grep -v '#' | awk '{print $6}' | perl -pe 's/\${out_dir_base}//;' | perl -pe 's/\///g;' | sort | uniq > $eval_target
##python json2tsv_linkjp.py $out_dir_base $gold_dir $in_dir $eval_target$$.txt
##python evaluation_linkjp_old.py $out_dir_base $gold_dir $eval_target$$.txt
##cd $out_dir_base
##cat */all_summary.tsv > all_summary_pre.tsv
##cat ../summary_header.txt all_summary_pre.tsv > all_summary.tsv
##cp all_summary.tsv eval_$$.txt
##cp ~/PycharmProjects/linkjpc/linkjpc_all_sample.sh env_$$.txt
##cat ./*/*_summary.tsv | grep -v SYS_ID | grep -v ^e | grep -v ^p | sort -d > summary_category_pre.tsv
##cat ../summary_cat_header.txt summary_category_pre.tsv > summary_category.tsv
##cp summary_category.tsv ${setting_dir}summary_category_$$.txt
