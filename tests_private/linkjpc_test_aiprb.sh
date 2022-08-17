#!/bin/bash
script="./linkjpc/linkjpc.py"
base_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/"
base_data_dir="${base_dir}Download/"
common_data_dir="${base_data_dir}ljc_data/common/"
tmp_data_dir="${base_data_dir}ljc_data/test/"
in_dir="${base_data_dir}linkjp-eval-211027/ene_annotation/"
out_dir_base="${base_dir}test_out/aiprb/"


## cf. github公開版
##script="./linkjpc/linkjpc_org.py"
##base_dir="/XXXX/XXXX/2021-LinkJP/"
##base_data_dir="${base_dir}Download/"
##common_data_dir="${base_data_dir}ljc_data/common/"
##tmp_data_dir="${base_data_dir}ljc_data/test/"
##in_dir="${base_data_dir}linkjp-eval-211027/ene_annotation/"
##out_dir_base="${base_dir}test_out/sample/"
#
#提出版
# AIPCB_CBI: mint_p_incl_m_imax1_o
# AIPRB_WSM: wlink_frp__slink__mint_e_attr_w (= wlink_frp__slink_05_fixed__mint_e_attr_w )
# AIPRB_SMW: slink_05_mid__mint_e__wlink_frp_attr_w_al_am_bl_w
# AIPRB_SMWL: slink_05_mid__mint_e__wlink_rp_l_06_attr_w_al_am_bl_w

#元のシステム
## EXAMPLE (wikipedia link (+attribute range filtering) > self link > exact match)
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_05_mint_e_attr_w/ --mod w:s:m -f a --mint e --wlink frp -s_min 0.5 -ar_tgt w
## EXAMPLE (self link > exact match > wikipedia link (+attribute range filtering, back link filtering)
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_frp_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
## EXAMPLE (baseline: partial match + incoming link filtering)
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_incl_m_imax1_o/ --mod m -f i --mint p -i_tgt m -i_max 1 -i_type o
# AIPRB_SMW 別版 (- wlink f) +l06 (= SMWL)
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_l_06_attr_w_al_am_bl_w/ --mod s:m:lw -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w -l_min 0.6



#
## mint eのみ
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e/ --mod m --mint e
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim/ --mod m --mint e -tmm trim
#
#
## mint pのみ
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p/ --mod m --mint p
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim/ --mod m --mint p -tmm trim
#
## tinm e のみ
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e/ --mod t --tinm e
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_trim/ --mod t --tinm e -tmt trim
#
## tinm pのみ
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p/ --mod t --tinm p
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim/ --mod t --tinm p -tmt trim
##
##
### selflinkのみ
### rawとfixedの中間
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_04_mid/ --mod s -s_min 0.4 -s_prb mid
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid/ --mod s -s_min 0.5 -s_prb mid
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_06_mid/ --mod s -s_min 0.6 -s_prb mid
###
#### サンプルデータのratioそのまま
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_04_raw/ --mod s -s_min 0.4 -s_prb raw
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_raw/ --mod s -s_min 0.5 -s_prb raw
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_06_raw/ --mod s -s_min 0.6 -s_prb raw
###
#### 全て1.0とする  04 = 05 > 06
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_04_fixed/ --mod s -s_min 0.4 -s_prb fixed
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_fixed/ --mod s -s_min 0.5 -s_prb fixed
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_06_fixed/ --mod s -s_min 0.6 -s_prb fixed
###
### wlinkのみ r = fr > m > f
### mention内同スコア
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_m/ --mod w --wlink m
### mention内最右により加点
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r/ --mod w --wlink r
### mention内最初により加点
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f/ --mod w --wlink f
### mention内最初と最右により加点
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fr/ --mod w --wlink fr
### mention前後の指定行内
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fl/ --mod w --wlink fl
##
###
##### linkprobのみ 06 > 03 = 04 = 05 > 07 > 09 > 10
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_03/ --mod l -l_min 0.3
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_04/ --mod l -l_min 0.4
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_05/ --mod l -l_min 0.5
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_06/ --mod l -l_min 0.6
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_07/ --mod l -l_min 0.7
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_08/ --mod l -l_min 0.8
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_09/ --mod l -l_min 0.9
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_10/ --mod l -l_min 1.0
#
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e/ --mod m --mint e
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp/ --mod w --wlink frp
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp_attr_w/ --mod w -f a --wlink rp -ar_tgt w
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp_attr_w_al_am_bl_w/ --mod w -f ab --wlink frp -ar_tgt w -al am -bl_tgt w
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp_attr_w_bl_w/ --mod w -f ab --wlink frp -ar_tgt w -bl_tgt w
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp_bl_w/ --mod w -f b --wlink frp -bl_tgt w
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp/ --mod w --wlink rp
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp_attr_w/ --mod w -f a --wlink rp -ar_tgt w
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp_attr_w_al_am_bl_w/ --mod w -f ab --wlink rp -ar_tgt w -al am -bl_tgt w
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp_attr_w_bl_w/ --mod w -f ab --wlink rp -ar_tgt w -bl_tgt w
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp_bl_w/ --mod w -f b --wlink rp -bl_tgt w
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink/ --mod s
#ADD
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid/ --mod s -s_min 0.5 -s_prb mid

## AIPCB_CBI
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_incl_m_imax1_o/ --mod m -f i --mint p -i_tgt m -i_max 1 -i_type o
#
#### AIPRB_WSM
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink__mint_e_attr_w/ --mod w:s:m -f a --mint e --wlink frp -ar_tgt w
## ablation
#### AIPRB_WSM 別版(- wlink f) この方が良い
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink__mint_e_attr_w/ --mod w:s:m -f a --mint e --wlink rp -ar_tgt w
#### AIPRB_WSM - wlink p
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fr__slink__mint_e_attr_w/ --mod w:s:m -f a --mint e --wlink fr -ar_tgt w
#### AIPRB_WSM - wlink r
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fp__slink__mint_e_attr_w/ --mod w:s:m -f a --mint e --wlink fp -ar_tgt w
#### AIPRB_WSM - attr_w
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink__mint_e/ --mod w:s:m --mint e --wlink frp
#### AIPRB_WSM +s_prb mid
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_mid__mint_e_attr_w/ --mod w:s:m -f a -s_prb mid --mint e --wlink frp -ar_tgt w
#### AIPRB_WSM +s_prb raw
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_raw__mint_e_attr_w/ --mod w:s:m -f a -s_prb raw --mint e --wlink frp -ar_tgt w
#### AIPRB_WSM weight
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp_slink_mint_e_attr_w/ --mod smw -f a --mint e --wlink frp -ar_tgt w
#### AIPRB_WSM - M
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp_slink_attr_w/ --mod w:s -f a --wlink frp -ar_tgt w
#### AIPRB_WSM -S
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__mint_e_attr_w/ --mod w:m -f a --mint e --wlink frp -ar_tgt w
#### AIPRB_WSM -W
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink__mint_e/ --mod s:m -f a --mint e
#
##### AIPRB_WSM + l06
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink__mint_e_l_06_attr_w/ --mod w:s:lm -f a --mint e --wlink frp -l_min 0.6 -ar_tgt w
#
##### AIPRB_WSM + l06
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_l_06__mint_e_attr_w/ --mod w:ls:m -f a --mint e --wlink frp -l_min 0.6 -ar_tgt w
#
##### AIPRB_WSM + l06
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_06_wlink_frp__slink__mint_e_attr_w/ --mod lw:s:m -f a --mint e --wlink frp -l_min 0.6 -ar_tgt w
#
##### AIPRB_WSM + l06 (equal weight)
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp_slink_mint_e_l_06_attr_w/ --mod lmsw -f a --mint e --wlink frp -l_min 0.6 -ar_tgt w
#
##here
##### AIPRB_WSM  別版(- wlink f)  - attr_w
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink__mint_e/ --mod w:s:m --mint e --wlink rp
##### AIPRB_WSM  別版(- wlink f)  +s_prb mid
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink_mid__mint_e_attr_w/ --mod w:s:m -f a -s_prb mid --mint e --wlink rp -ar_tgt w
##### AIPRB_WSM  別版(- wlink f)  +s_prb raw
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink_raw__mint_e_attr_w/ --mod w:s:m -f a -s_prb raw --mint e --wlink rp -ar_tgt w
##### AIPRB_WSM  別版(- wlink f)  weight
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp_slink_mint_e_attr_w/ --mod smw -f a --mint e --wlink rp -ar_tgt w
##### AIPRB_WSM  別版(- wlink f)  - M
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp_slink_attr_w/ --mod w:s -f a --wlink rp -ar_tgt w
##### AIPRB_WSM 別版(- wlink f) -S
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__mint_e_attr_w/ --mod w:m -f a --mint e --wlink rp -ar_tgt w
##
###### AIPRB_WSM 別版(- wlink f) +l_06
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink__mint_e_l_06_attr_w/ --mod w:s:lm -f a --mint e --wlink rp -ar_tgt w -l_min 0.6
##### AIPRB_WSM 別版(- wlink f) +l_06
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink_l_06__mint_e_attr_w/ --mod w:ls:m -f a --mint e --wlink rp -ar_tgt w -l_min 0.6
##### AIPRB_WSM 別版(- wlink f) +l_06 最良
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_06_wlink_rp__slink__mint_e_attr_w/ --mod lw:s:m -f a --mint e --wlink rp -ar_tgt w -l_min 0.6
###
##### AIPRB_WSM 別版(- wlink f) +l_06 (equal weight)
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_06_wlink_rp_slink_mint_e_attr_w/ --mod lmsw -f a --mint e --wlink rp -ar_tgt w -l_min 0.6
#
##### AIPRB_WSM 別版(- wlink f) +l_06 最良　- attr_w
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_06_wlink_rp__slink__mint_e/ --mod lw:s:m --mint e --wlink rp -l_min 0.6
#
###### AIPRB_WSM 別版(- wlink f) +l_06 最良 -mint
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_06_wlink_rp__slink_attr_w/ --mod lw:s -f a --wlink rp -ar_tgt w -l_min 0.6
#
###### AIPRB_WSM 別版(- wlink f) +l_06 最良 -slink
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_06_wlink_rp__mint_e_attr_w/ --mod lw:m -f a --mint e --wlink rp -ar_tgt w -l_min 0.6
#
###### AIPRB_WSM 別版(- wlink f) +l_06 最良 -wlink
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_06__slink__mint_e/ --mod l:s:m --mint e -l_min 0.6
#
###### AIPRB_WSM 別版(- wlink f) +l_06 最良　slink variation
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_06_wlink_rp__slink_05_fixed_mint_e_attr_w/ --mod lw:s:m -f a --mint e --wlink rp -ar_tgt w -l_min 0.6 -s_min 0.5 -s_prb fixed
###### AIPRB_WSM 別版(- wlink f) +l_06 最良  slink variation
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_06_wlink_rp__slink_05_raw_mint_e_attr_w/ --mod lw:s:m -f a --mint e --wlink rp -ar_tgt w -l_min 0.6 -s_min 0.5 -s_prb raw
###### AIPRB_WSM 別版(- wlink f) +l_06 最良  slink variation
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_06_wlink_rp__slink_05_mid_mint_e_attr_w/ --mod lw:s:m -f a --mint e --wlink rp -ar_tgt w -l_min 0.6 -s_min 0.5 -s_prb mid
##
##hereherehere
##
### AIPRB_SMW
###tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_frp_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
### ablation
### AIPRB_SMW -s_prb fixed
###tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_fixed__mint_e__wlink_frp_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb fixed --wlink frp -ar_tgt w -al am -bl_tgt w
### AIPRB_SMW -s_prb raw
###tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_raw__mint_e__wlink_frp_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb raw --wlink frp -ar_tgt w -al am -bl_tgt w
### AIPRB_SMW 別版(- wlink f)
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w
### AIPRB_SMW  - wlink r
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_fp_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink fp -ar_tgt w -al am -bl_tgt w
### AIPRB_SMW - wlink p
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_fr_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink fr -ar_tgt w -al am -bl_tgt w
### AIPRB_SMW - bl_w
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_frp_attr_w_al_am/ --mod s:m:w -f a --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am
### AIPRB_SMW - al_am
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_frp_attr_w_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -bl_tgt w
#### AIPRB_SMW - attr_w
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_frp_bl_w/ --mod s:m:w -f b --mint e -s_min 0.5 -s_prb mid --wlink frp -bl_tgt w
#### AIPRB_SMW weight
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid_mint_e_wlink_frp_attr_w_al_am_bl_w/ --mod smw -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
### AIPRB_SMW -M
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__wlink_frp_attr_w_al_am_bl_w/ --mod s:w -f ab -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
### AIPRB_SMW -W
#ADD
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e/ --mod s:m --mint e -s_min 0.5 -s_prb mid
### AIPRB_SMW -S
#ADD
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e__wlink_frp_attr_w_al_am_bl_w/ --mod m:w -f ab --mint e --wlink frp -ar_tgt w -al am -bl_tgt w
##
#### AIPRB_SMW  +l06
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_frp_l_06_attr_w_al_am_bl_w/ --mod s:m:lw -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w -l_min 0.6
#
### AIPRB_SMW  +l06
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e_l_06__wlink_frp_attr_w_al_am_bl_w/ --mod s:lm:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w -l_min 0.6
#
### AIPRB_SMW  +l06
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_06_slink_05_mid__mint_e__wlink_frp_attr_w_al_am_bl_w/ --mod ls:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w -l_min 0.6
#
## AIPRB_SMW 別版 (- wlink f)- wlink p
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_r_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink r -ar_tgt w -al am -bl_tgt w
## AIPRB_SMW 別版 (- wlink f)- bl_w
##tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_attr_w_al_am/ --mod s:m:w -f a --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am
## AIPRB_SMW　別版 (- wlink f) - al_am
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_attr_w_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -bl_tgt w
## AIPRB_SMW 別版 (- wlink f)- attr_w
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_bl_w/ --mod s:m:w -f b --mint e -s_min 0.5 -s_prb mid --wlink rp -bl_tgt w
# AIPRB_SMW 別版 (- wlink f)weight
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid_mint_e_wlink_rp_attr_w_al_am_bl_w/ --mod smw -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w
# AIPRB_SMW 別版 (- wlink f)-M
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__wlink_rp_attr_w_al_am_bl_w/ --mod s:w -f ab -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w
# AIPRB_SMW 別版 (- wlink f)-M nofilter
#AAAA
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__wlink_rp/ --mod s:w  -s_min 0.5 -s_prb mid --wlink rp 

# AIPRB_SMW 別版 (- wlink f)-S
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e__wlink_rp_attr_w_al_am_bl_w/ --mod m:w -f ab --mint e --wlink rp -ar_tgt w -al am -bl_tgt w

# AIPRB_SMW 別版 (- wlink f) +l06 (= SMWL) -W
#ADD
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__l_06/ --mod s:m:l --mint e -s_min 0.5 -s_prb mid -l_min 0.6

# AIPRB_SMW 別版 (- wlink f) +l06 (= SMWL)
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_l_06_attr_w_al_am_bl_w/ --mod s:m:lw -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w -l_min 0.6
# ablation
# SMWL - 全フィルタ
#ADDADDADD
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_l_06/ --mod s:m:lw --mint e -s_min 0.5 -s_prb mid --wlink rp -l_min 0.6

#ablation
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp/ --mod s:m:w --mint e -s_min 0.5 -s_prb mid --wlink rp
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__l_06/ --mod s:m:l --mint e -s_min 0.5 -s_prb mid -l_min 0.6
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__wlink_rp_l_06/ --mod s:lw -s_min 0.5 -s_prb mid --wlink rp -l_min 0.6
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e__wlink_rp_l_06/ --mod m:lw --mint e --wlink rp -l_min 0.6

#AAAAAA
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e__l_06/ --mod m:l --mint e -l_min 0.6
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e__wlink_rp/ --mod m:w --mint e --wlink rp
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__l_06/ --mod s:l -s_min 0.5 -s_prb mid -l_min 0.6
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__wlink_rp/ --mod s:w -s_min 0.5 -s_prb mid --wlink rp
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp_l_06/ --mod lw --wlink rp -l_min 0.6

# SMWL - al am
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_l_06_attr_w_bl_w/ --mod s:m:lw -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -bl_tgt w -l_min 0.6
#till here
# SMWL - attr
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_l_06_bl_w/ --mod s:m:lw -f b --mint e -s_min 0.5 -s_prb mid --wlink rp -bl_tgt w -l_min 0.6
# SMWL - bl
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_l_06_attr_w_al_am/ --mod s:m:lw -f a --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -l_min 0.6

# AIPRB_SMW 別版 (- wlink f) +l06 variation
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e_l_06__wlink_rp_attr_w_al_am_bl_w/ --mod s:lm:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w -l_min 0.6
#ablation
# AIPRB_SMW 別版 (- wlink f) +l06 -attr
##ADDADD
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e_l_06__wlink_rp_bl_w/ --mod s:lm:w -f b --mint e -s_min 0.5 -s_prb mid --wlink rp -bl_tgt w -l_min 0.6
##ADDADD
# AIPRB_SMW 別版 (- wlink f) +l06 -bl
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e_l_06__wlink_rp_attr_w_al_am/ --mod s:lm:w -f a --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -l_min 0.6


# AIPRB_SMW 別版 (- wlink f) +l06 variation
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid_l_06__mint_e__wlink_rp_attr_w_al_am_bl_w/ --mod ls:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w -l_min 0.6
# ablation
# AIPRB_SMW 別版 (- wlink f) +l06 -attr
#ADD
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid_l_06__mint_e__wlink_rp_bl_w/ --mod ls:m:w -f b --mint e -s_min 0.5 -s_prb mid --wlink rp -bl_tgt w -l_min 0.6
# AIPRB_SMW 別版 (- wlink f) +l06 -bl
#ADD
#tmp#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid_l_06__mint_e__wlink_rp_attr_w_al_am/ --mod ls:m:w -f a --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -l_min 0.6

