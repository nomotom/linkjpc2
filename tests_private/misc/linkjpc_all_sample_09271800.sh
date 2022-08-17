#!/bin/sh -x
now=`date +%Y%m%d%H%M%S`
script="./linkjpc.py"
common_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/common/"
tmp_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/sample/"
in_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/ene_annotation/"
gold_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/link_annotation/"
out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210923/"
eval_target="./eval_target_sample.txt"
out_dir_tmp_base="/Users/masako/tmp/sample/20210923/"
setting_dir="${out_dir_base}setting/"
eval_script="./linkjpc_eval_sample.sh"


#これはmodの設定間違い上書き中

#
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l/ --mod l -f n
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_attr_l_anc09_ang01/ --mod l -f a -ar_tgt m -anc 0.9 -ang 0.1
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_bl_l/ --mod l -f b -bl_tgt l
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_incl_l/ --mod l -f i -i_tgt l
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e/ --mod m -f n --mint e
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_attr_m_anc09_ang01/ --mod m -f a --mint e -ar_tgt m -anc 0.9 -ang 0.1
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_bl_m/ --mod m --mint e -f b -bl_tgt m
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_incl_m/ --mod m --mint e -f i -i_tgt m

${eval_script}

python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05/ --mod ms -f n --mint e -s_min 0.5
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_f/ --mod msw -f n --mint e -s_min 0.5 --wlink f
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_fp/ --mod msw -f n --mint e -s_min 0.5 --wlink fp
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frp/ --mod msw -f n --mint e -s_min 0.5 --wlink frp
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_frpl/ --mod msw -f n --mint e -s_min 0.5 --wlink frpl

${eval_script}

python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_r/ --mod ms -f n --mint e -s_min 0.5 -wlink r
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp/ --mod msw -f n --mint e -s_min 0.5 --wlink rp
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rpl/ --mod msw -f n --mint e -s_min 0.5 --wlink rpl
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_bl_s/ --mod msw -f b --mint e -s_min 0.5 --wlink rp -bl_tgt s
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rp_bl_w/ --mod msw -f b --mint e -s_min 0.5 --wlink rp -bl_tgt w
###9/24#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink05_wlink_rpl_l_attr_msw_anc09_ang01_bl_sw_incl_sw/ --mod mswl -f abi --mint e -s_min 0.5 --wlink rpl -ar_tgt msw -anc 0.9 -ang 0.1 -bl_tgt sw -i_tgt sw

${eval_script}

python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e/ --mod mt -f n --mint e --tinm e
#0926-1500python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e/ --mod mt --mint e --tinm e -f n
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_incl_mt/ --mod mt --mint e --tinm e -f i -i_tgt mt
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_attr_m_anc09_ang01/ --mod mt -f a --mint e --tinm e -ar_tgt m -anc 0.9 -ang 0.1
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_attr_t_anc09_ang01/ --mod mt -f a --mint e --tinm e -ar_tgt t -anc 0.9 -ang 0.1
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_bl_m/ --mod mt --mint e --tinm e -f b -bl_tgt m
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_bl_t/ --mod mt --mint e --tinm e -f b -bl_tgt t
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_slink05/ --mod ms -f n --mint e --tinm e -s_min 0.5
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_slink05_wlink_frp_attr_m_anc09_ang01_incl_m_bl_mtw/ --mod mtsw -f abi --mint e --tinm e -s_min 0.5 --wlink frp -ar_tgt mw -anc 0.9 -ang 0.1 -i_tgt m -bl_tgt mtw
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_slink05_wlink_fr_attr_m_anc09_ang01_incl_m_bl_mtw/ --mod mtsw -f abi --mint e --tinm e -s_min 0.5 --wlink fr -ar_tgt mw -anc 0.9 -ang 0.1 -i_tgt m -bl_tgt mtw

python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim/ --mod mt -f n --mint e --tinm e -tmt trim
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_attr_m_anc09_ang01/ --mod m -f a --mint e --tinm e -tmt trim -ar_tgt m -anc 0.9 -ang 0.1 -al n
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_wlink_f/ --mod mtw -f n --mint e --tinm e --wlink f
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_wlink_fr/ --mod mtw -f n --mint e --tinm e --wlink fr
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_wlink_frp/ --mod mtw -f n --mint e --tinm e --wlink frp
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_wlink_frpl/ --mod mw -f n --mint e --tinm e --wlink frpl
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_wlink_r/ --mod mw -f n --mint e --tinm e --wlink r
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_wlink_rp/ --mod mtw -f n --mint e --tinm e --wlink rp
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_wlink_rpl/ --mod mtw -f n --mint e --tinm e --wlink rpl

${eval_script}

python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p/ --mod mt -f n --mint e --tinm p
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_attr_m_anc09_ang01/ --mod m -f a --mint e --tinm p -ar_tgt m -anc 0.9 -ang 0.1 -al n
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_attr_m_anc09_ang01_al_r/ --mod m -f a --mint e --tinm p -ar_tgt m -anc 0.9 -ang 0.1 -al r
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_trim/ --mod mt -f n --mint e --tinm p -tmt trim
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_trim_attr_t_anc09_ang01/ --mod m -f a --mint e --tinm p -tmt trim -ar_tgt t -anc 0.9 -ang 0.1
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_trim_attr_t_anc09_ang01_al_r/ --mod m -f a --mint e --tinm p -tmt trim -ar_tgt t -anc 0.9 -ang 0.1 -al r

${eval_script}

python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim/ --mod m -f n --mint e -tmm trim
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_attr_m_anc09_ang01/ --mod m -f a --mint e -tmm trim -ar_tgt m -anc 0.9 -ang 0.1
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_attr_m_anc09_ang01_al_r/ --mod m -f a --mint e -tmm trim -ar_tgt m -anc 0.9 -ang 0.1 -al r
#0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_bl_m/ --mod m --mint e -tmm trim -f b -bl_tgt m
#0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_incl_m/ --mod m -f i --mint e -tmm trim -i_tgt m
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_slink05_wlink_rp/ --mod msw -f n --mint e -tmm trim -s_min 0.5 --wlink rp
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_slink05_wlink_rp_attr_m_anc09_ang01/ --mod msw -f a --mint e -tmm trim -s_min 0.5 --wlink rp -ar_tgt m -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_slink05_wlink_rp_attr_ms_anc09_ang01/ --mod msw -f a --mint e -tmm trim -s_min 0.5 --wlink rp -ar_tgt ms -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_slink05_wlink_rp_attr_mw_anc09_ang01/ --mod msw -f a --mint e -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_slink05_wlink_rp_attr_ms_anc09_ang01/ --mod msw -f a --mint e -tmm trim -s_min 0.5 --wlink rp -ar_tgt ms -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_slink05_wlink_rp_attr_s_anc09_ang01/ --mod msw -f a --mint e -tmm trim -s_min 0.5 --wlink rp -ar_tgt s -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_slink05_wlink_rp_attr_w_anc09_ang01/ --mod msw -f a --mint e -tmm trim -s_min 0.5 --wlink rp -ar_tgt w -anc 0.9 -ang 0.1

${eval_script}

python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e/ --mod mt -f n --mint e -tmm trim --tinm e
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p/ --mod mt -f n --mint e -tmm trim --tinm p
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_trim/ --mod mt -f n --mint e -tmm trim --tinm p -tmt trim
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_incl_m/ --mod mt --mint e --tinm e -f i -i_tgt m
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_wlink_frp/ --mod mw -f n --mint e --wlink frp
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_wlink_frpl/ --mod mw -f n --mint e --wlink frpl
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_wlink_r/ --mod mw -f n --mint e --wlink r
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_wlink_r_attr_w_anc09_ang01/ --mod mw -f a --mint e --wlink r -ar_tgt w -anc 0.9 -ang 0.1
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_wlink_rp/ --mod mw -f n --mint e --wlink rp
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_wlink_rp_attr_m_anc09_ang01/ --mod mw -f a --mint e --wlink rp -ar_tgt m -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_wlink_rp_attr_w_anc09_ang01/ --mod mw -f a --mint e --wlink rp -ar_tgt w -anc 0.9 -ang 0.1
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_wlink_rpl/ --mod mw -f n --mint e --wlink rpl

${eval_script}

python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p/ --mod m -f n --mint p
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_cmax100/ --mod m -f n --mint p -c_max 100
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_cmax10/ --mod m -f n --mint p -c_max 10
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_attr_m_anc09_ang01/ --mod m -f a --mint p -ar_tgt m -anc 0.9 -ang 0.1
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_attr_m_anc09_ang01_al_r/ --mod m -f a --mint p -ar_tgt m -anc 0.9 -ang 0.1 -al r
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_attr_m_anc09_ang01_bl_m/ --mod m --mint p -f ab -ar_tgt m -anc 0.9 -ang 0.1 -bl_tgt m
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_attr_m_anc09_ang01_bl_m_incl_m/ --mod m --mint p -f abi -ar_tgt m -anc 0.9 -ang 0.1 -bl_tgt m -i_tgt m
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_attr_m_anc09_ang01_incl_m/ --mod m --mint p -f ai -ar_tgt m -anc 0.9 -ang 0.1 -i_tgt m
#0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_bl_m/ --mod m --mint p -f b -bl_tgt m
#0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_incl_m/ --mod m --mint p -f i -i_tgt m
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_bl_m_incl_m/ --mod m --mint p -f bi -bl_tgt m -i_tgt m
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05/ --mod ms -f n --mint p -s_min 0.5
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_attr_m_anc09_ang01/ --mod ms -f a --mint p -s_min 0.5 -ar_tgt m
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_m_incl_w/ --mod msw -f i --mint p --wlink m -s_min 0.5 -i_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_mp_incl_w/ --mod msw -f i --mint p --wlink mp -s_min 0.5 -i_tgt w
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_r/ --mod msw -f n --mint p -s_min 0.5 --wlink r
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_rp/ --mod msw -f n --mint p -s_min 0.5 --wlink rp
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_r_attr_m_anc09_ang01/ --mod msw -f a --mint p -s_min 0.5 --wlink r -ar_tgt m -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_rp_attr_m_anc09_ang01/ --mod msw -f a --mint p -s_min 0.5 --wlink rp -ar_tgt m -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_r_attr_ms_anc09_ang01/ --mod msw -f a --mint p -s_min 0.5 --wlink r -ar_tgt ms -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_rp_attr_ms_anc09_ang01/ --mod msw -f a --mint p -s_min 0.5 --wlink rp -ar_tgt ms -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_r_attr_msw_anc09_ang01/ --mod msw -f a --mint p -s_min 0.5 --wlink r -ar_tgt msw -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_slink05_wlink_rp_attr_msw_anc09_ang01/ --mod msw -f a --mint p -s_min 0.5 --wlink rp -ar_tgt msw -anc 0.9 -ang 0.1

${eval_script}

python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim/ --mod m -f n --mint p -tmm trim
###9/24#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_attr_m_anc07_ang01/ --mod m -f a --mint p -tmm trim -ar_tgt m -anc 0.7 -ang 0.1
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_attr_m_anc08_ang01/ --mod m -f a --mint p -tmm trim -ar_tgt m -anc 0.8 -ang 0.1
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_attr_m_anc09_ang00/ --mod m -f a --mint p -tmm trim -ar_tgt m -anc 0.9 -ang 0.0
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_attr_m_anc09_ang01/ --mod m -f a --mint p -tmm trim -ar_tgt m -anc 0.9 -ang 0.1
#0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_bl_m/ --mod m -f b --mint p -tmm trim -bl_tgt m
#0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_incl_m/ --mod m -f i --mint p -tmm trim -i_tgt m
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_wlink_r/ --mod mw -f n --mint p --wlink r
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_wlink_rp/ --mod mw -f n --mint p --wlink rp
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_wlink_r_attr_m_anc09_ang01/ --mod mw -f a --mint p --wlink r -ar_tgt m -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_wlink_rp_attr_m_anc09_ang01/ --mod mw -f a --mint p --wlink rp -ar_tgt m -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_wlink_r_attr_mw_anc09_ang01/ --mod mw -f a --mint p --wlink r -ar_tgt mw -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_wlink_rp_attr_mw_anc09_ang01/ --mod mw -f a --mint p --wlink rp -ar_tgt mw -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p04/ --mod m -f n --mint p -m_min 0.4
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p06/ --mod m -f n --mint p -m_min 0.6
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p08/ --mod m -f n --mint p -m_min 0.8

${eval_script}

#slink系
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05/ --mod s -f n -s_min 0.5
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_attr_s_anc09_ang01/ --mod s -f a -s_min 0.5 -ar_tgt s -anc 0.9 -ang 0.1
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_attr_s_anc09_ang01_al_r/ --mod s -f a -s_min 0.5 -ar_tgt s -anc 0.9 -ang 0.1 -al r
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_attr_s_anc09_ang01_bl_s/ --mod s -f ab -s_min 0.5 -ar_tgt s -anc 0.9 -ang 0.1 -bl_tgt s
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_attr_s_anc09_ang01_bl_s_incl_s/ --mod s -f abi -s_min 0.5 -ar_tgt s -anc 0.9 -ang 0.1 -bl_tgt s -i_tgt s
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_attr_s_anc09_ang01_incl_s/ --mod s -f ai -s_min 0.5 -ar_tgt s -anc 0.9 -ang 0.1 -i_tgt s
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_bl_s/ --mod s -f b -s_min 0.5 -bl_tgt s
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_incl_s/ --mod s -f i -s_min 0.5 -i_tgt s
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mint_e_tinm_e_wlink_rp/ --mod smtw -f n --mint e -tinm e -s_min 0.5 --wlink rp
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mint_e_wlink_r/ --mod smw -f n --mint e -s_min 0.5 --wlink r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mint_e_wlink_rp/ --mod smw -f n --mint e -s_min 0.5 --wlink rp
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mint_e_trim_wlink_rp/ --mod smw -f n --mint e -tmm trim -s_min 0.5 --wlink rp
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mint_e_trim_wlink_rp_attr_m_anc09_ang01/ --mod smw -f a --mint e -tmm trim -s_min 0.5 --wlink rp -ar_tgt m -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mint_e_trim_wlink_rp_attr_s_anc09_ang01/ --mod smw -f a --mint e -tmm trim -s_min 0.5 --wlink rp -ar_tgt s -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mint_e_trim_wlink_rp_attr_w_anc09_ang01/ --mod smw -f a --mint e -tmm trim -s_min 0.5 --wlink rp -ar_tgt w -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mint_e_trim_wlink_rp_attr_m_anc09_ang01_incl_m/ --mod smw -f ai --mint e -tmm trim -s_min 0.5 --wlink rp -ar_tgt m -anc 0.9 -ang 0.1 -i_tgt m
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mint_e_trim_wlink_rp_attr_s_anc09_ang01_incl_s/ --mod smw -f ai --mint e -tmm trim -s_min 0.5 --wlink rp -ar_tgt s -anc 0.9 -ang 0.1 -i_tgt s
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink05_mint_e_trim_wlink_rp_attr_w_anc09_ang01_incl_w/ --mod smw -f ai --mint e -tmm trim -s_min 0.5 --wlink rp -ar_tgt w -anc 0.9 -ang 0.1 -i_tgt w
###9/24#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink06/ --mod s -f n -s_min 0.6
###9/24#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink07/ --mod s -f n -s_min 0.7

${eval_script}

#tinm系
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e/ --mod t -f n --tinm e
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_attr_t_anc09_ang01/ --mod t -f a --tinm e  -ar_tgt t -anc 0.9 -ang 0.1
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_attr_t_anc09_ang01_al_r/ --mod t -f a --tinm e  -ar_tgt t -anc 0.9 -ang 0.1 -al r
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_bl_t/ --mod t -f b --tinm e  -bl_tgt t
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_incl_t/ --mod t -f i --tinm e -i_tgt t
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_slink05/ --mod ts -f n --tinm e -s_min 0.5
#0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_trim/ --mod t -f n --tinm e -tmt trim
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_attr_t_anc09_ang01/ --mod t -f a --tinm e  -ar_tgt t -anc 0.9 -ang 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_wlink_r/ --mod tw -f n --tinm e --wlink r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_wlink_rp/ --mod tw -f n --tinm e --wlink rp
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p/ --mod t -f n --tinm p
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim/ --mod t -f n --tinm p -tmt trim
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_attr_t_anc09_ang01/ --mod t -f a --tinm p  -ar_tgt t -anc 0.9 -ang 0.1
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_attr_t_anc09_ang01_al_r/ --mod t -f a --tinm p  -ar_tgt t -anc 0.9 -ang 0.1 -al r
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_attr_t_anc09_ang01_bl_t/ --mod t --tinm p -f ab -ar_tgt t -anc 0.9 -ang 0.1 -bl_tgt t
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_attr_t_anc09_ang01_bl_t_incl_t/ --mod t -f abi --tinm p -ar_tgt t -anc 0.9 -ang 0.1 -bl_tgt t -i_tgt t
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_attr_t_anc09_ang01_incl_t1/ --mod t -f ai --tinm p -ar_tgt t -anc 0.9 -ang 0.1 -i_tgt t
#0926-1500#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_bl_t/ --mod t -f b --tinm p  -bl_tgt t
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_bl_t_incl_t/ --mod t -f bi --tinm p -bl_tgt t -i_tgt t
${eval_script}


#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_incl_t/ --mod t -f i --tinm p -i_tgt t
script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim/ --mod t -f n --tinm p -tmt trim
script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_attr_t_anc09_ang01/ --mod t -f a --tinm p -tmt trim -ar_tgt t -anc 0.9 -ang 0.1
script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_attr_t_anc09_ang01_al_r/ --mod t -f a --tinm p -tmt trim -ar_tgt t -anc 0.9 -ang 0.1 -al r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_bl_t/ --mod t -f b --tinm p -tmt trim -bl_tgt t

${eval_script}

python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f/ --mod w -f n --wlink f
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_attr_w_anc09_ang01/ --mod w -f a --wlink f -ar_tgt w -anc 0.9 -ang 0.1
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink f -ar_tgt w -anc 0.9 -ang 0.1 -al r
####latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_attr_w_anc09_ang01/ --mod w -f a --wlink f -ar_tgt w -anc 0.9 -ang 0.1
#0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_incl_w/ --mod w -f i --wlink f -i_tgt w
#0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_bl_w/ --mod w -f b --wlink f -bl_tgt w
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_slink05_mint_e/ --mod wsm: -f n --mint e -s_min 0.5 --wlink f


python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fl/ --mod w -f n --wlink fl
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fl_attr_w_anc09_ang01/ --mod w -f a --wlink fl -ar_tgt w -anc 0.9 -ang 0.1
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fl_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink fl -ar_tgt w -anc 0.9 -ang 0.1 -al r
#0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fl_bl_w/ --mod w -f b --wlink fl -bl_tgt w
#0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fl_incl_w/ --mod w -f i --wlink fl -i_tgt w
#0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fp/ --mod w -f n --wlink fp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fp_attr_w_anc09_ang01/ --mod w -f a --wlink fp -ar_tgt w -anc 0.9 -ang 0.1
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fp_bl_w/ --mod w -f b --wlink fp -bl_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fp_incl_w/ --mod w -f i --wlink fp -i_tgt w
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fp_slink05_mint_e/ --mod wsm: -f n --mint e -s_min 0.5 --wlink fp
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fpl/ --mod w -f n --wlink fpl
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fpl_attr_w_anc09_ang01/ --mod w -f a --wlink fpl -ar_tgt w -anc 0.9 -ang 0.1
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fpl_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink fpl -ar_tgt w -anc 0.9 -ang 0.1 -al r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fpl_bl_w/ --mod w -f b --wlink fpl -bl_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fpl_incl_w/ --mod w -f i --wlink fpl -i_tgt w
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fr/ --mod w -f n --wlink fr
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fr_attr_w_anc09_ang01/ --mod w -f a --wlink fr -ar_tgt w -anc 0.9 -ang 0.1
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fr_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink fr -ar_tgt w -anc 0.9 -ang 0.1 -al r
####latest#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fr_attr_w_anc09_ang01/ --mod w -f a --wlink fr -ar_tgt w -anc 0.9 -ang 0.1
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fr_incl_w/ --mod w -f i --wlink fr -i_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fr_bl_w/ --mod w -f b --wlink fr -bl_tgt w
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fr_slink05_mint_e/ --mod wsm: -f n --mint e -s_min 0.5 --wlink fr
#0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp/ --mod w -f n --wlink frp
#0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp_attr_w_anc09_ang01/ --mod w -f a --wlink frp -ar_tgt w -anc 0.9 -ang 0.1 -al n
#0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink frp -ar_tgt w -anc 0.9 -ang 0.1 -al r
#0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp_bl_w/ --mod w -f b --wlink frp -bl_tgt w
#0927-0800#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp_incl_w/ --mod w -f i --wlink frp -i_tgt w
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl/ --mod w -f n --wlink frpl
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl_attr_w_anc09_ang01/ --mod w -f a --wlink frpl -ar_tgt w -anc 0.9 -ang 0.1
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink frpl -ar_tgt w -anc 0.9 -ang 0.1 -al r
 #0927-1430#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls05_wlp03_wln03/ --mod w -f n --wlink l -wls 0.5 -wlp 0.3 -wln 0.3
 #0927-1430#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls05_wlp03_wln02/ --mod w -f n --wlink l -wls 0.5 -wlp 0.3 -wln 0.2
 #0927-1430#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls05_wlp03_wln01/ --mod w -f n --wlink l -wls 0.5 -wlp 0.3 -wln 0.1
 #0927-1430#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls05_wlp04_wln03/ --mod w -f n --wlink l -wls 0.5 -wlp 0.4 -wln 0.3
 #0927-1430#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls05_wlp04_wln02/ --mod w -f n --wlink l -wls 0.5 -wlp 0.4 -wln 0.2
 #0927-1430#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls05_wlp04_wln01/ --mod w -f n --wlink l -wls 0.5 -wlp 0.4 -wln 0.1
 #0927-1430#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls04_wlp03_wln03/ --mod w -f n --wlink l -wls 0.4 -wlp 0.3 -wln 0.3
 #0927-1430#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls04_wlp03_wln02/ --mod w -f n --wlink l -wls 0.4 -wlp 0.3 -wln 0.2
 #0927-1430#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls04_wlp03_wln01/ --mod w -f n --wlink l -wls 0.4 -wlp 0.3 -wln 0.1
 #0927-1430#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls03_wlp03_wln03/ --mod w -f n --wlink l -wls 0.3 -wlp 0.3 -wln 0.3
 #0927-1430#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls03_wlp03_wln02/ --mod w -f n --wlink l -wls 0.3 -wlp 0.3 -wln 0.2
 #0927-1430#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls03_wlp02_wln01/ --mod w -f n --wlink l -wls 0.3 -wlp 0.3 -wln 0.1

${eval_script}

python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_m/ --mod w -f n --wlink m
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_m_attr_w_anc09_ang01/ --mod w -f a --wlink m -ar_tgt w -anc 0.9 -ang 0.1
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_m_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink m -ar_tgt w -anc 0.9 -ang 0.1 -al r
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_m_attr_w_anc09_ang01_incl_w/ --mod w -f ai --wlink m -ar_tgt w -anc 0.9 -ang 0.1 -i_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_m_incl_w/ --mod w -f i --wlink m -i_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_m_bl_w/ --mod w -f b --wlink m -bl_tgt w
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_ml/ --mod w -f n --wlink ml
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_ml_attr_w_anc09_ang01/ --mod w -f a --wlink ml -ar_tgt w -anc 0.9 -ang 0.1
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_ml_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink ml -ar_tgt w -anc 0.9 -ang 0.1 -al r
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_ml_attr_w_anc09_ang01_incl_w/ --mod w -f ai --wlink ml -ar_tgt w -anc 0.9 -ang 0.1 -i_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_ml_bl_w/ --mod w -f b --wlink ml -bl_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_ml_incl_w/ --mod w -f i --wlink ml -i_tgt w
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mp/ --mod w -f n --wlink mp
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mp_attr_w_anc09_ang01/ --mod w -f a --wlink mp -ar_tgt w -anc 0.9 -ang 0.1
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mp_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink mp -ar_tgt w -anc 0.9 -ang 0.1 -al r
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mp_attr_w_anc09_ang01_incl_w/ --mod w -f ai --wlink mp -ar_tgt w -anc 0.9 -ang 0.1 -i_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mp_incl_w/ --mod w -f i --wlink mp -i_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mp_bl_w/ --mod w -f b --wlink mp -bl_tgt w
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mpl/ --mod w -f n --wlink mpl
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mpl_attr_w_anc09_ang01/ --mod w -f a --wlink mpl -ar_tgt w -anc 0.9 -ang 0.1
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mpl_attr_w_anc09_ang01_incl_w/ --mod w -f ai --wlink mpl -ar_tgt w -anc 0.9 -ang 0.1 -i_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mpl_bl_w/ --mod w -f b --wlink mpl -bl_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mpl_incl_w/ --mod w -f i --wlink mpl -i_tgt w

${eval_script}

python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r/ --mod w -f n --wlink r
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_attr_w_anc09_ang01/ --mod w --wlink r -f a -ar_tgt w -anc 0.9 -ang 0.1
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_attr_w_anc09_ang01_al_r/ --mod w --wlink r -f a -ar_tgt w -anc 0.9 -ang 0.1 -al r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_incl_w/ --mod w -f i --wlink r -i_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_bl_w/ --mod w -f b --wlink r -bl_tgt w
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl/ --mod w -f n --wlink rl
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_attr_w_anc09_ang01/ --mod w -f a --wlink rl -ar_tgt w -anc 0.9 -ang 0.1
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink rl -ar_tgt w -anc 0.9 -ang 0.1 -al r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bl_w/ --mod w -f b --wlink rl -bl_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_incl_w/ --mod w -f i --wlink rl -i_tgt w
${eval_script}

python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp/ --mod w -f n --wlink rp
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp_attr_w_anc09_ang01/ --mod w -f a --wlink rp -ar_tgt w -anc 0.9 -ang 0.1
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink rp -ar_tgt w -anc 0.9 -ang 0.1 -al r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp_bl_w/ --mod w -f b --wlink rp -bl_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp_incl_w/ --mod w -f i --wlink rp -i_tgt w
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rpl/ --mod w -f n --wlink rpl
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rpl_attr_w_anc09_ang01/ --mod w -f a --wlink rpl -ar_tgt w -anc 0.9 -ang 0.1
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rpl_attr_w_anc09_ang01_al_r/ --mod w -f a --wlink rpl -ar_tgt w -anc 0.9 -ang 0.1 -al r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rpl_attr_w_anc09_ang01_incl_w/ --mod w -f ai --wlink rpl -ar_tgt w -anc 0.9 -ang 0.1 -i_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rpl_incl_w/ --mod w -f i --wlink rpl -i_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rpl_bl_w/ --mod w -f b --wlink rpl -bl_tgt w
${eval_script}


#rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210923/*_pre.tsv
#rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210923/*/*_summary.tsv
#rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210923/*/*_anal.tsv
#rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210923/*/*_fn.tsv
#rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210923/*/Airport.tsv
#rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210923/*/City.tsv
#rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210923/*/Company.tsv
#rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210923/*/Compound.tsv
#rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210923/*/Conference.tsv
#rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210923/*/Lake.tsv
#rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210923/*/Person.tsv
#rm /Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210923/*/*.tsv
#grep 'script' ~/PycharmProjects/linkjpc/linkjpc_all_sample.sh |  awk '{print $6}' | perl -pe 's/\${out_dir_base}//;' | perl -pe 's/\///g;' | sort | uniq > $eval_target
##grep 'script' ~/PycharmProjects/linkjpc/linkjpc_all_sample.sh | grep -v '#' | awk '{print $6}' | perl -pe 's/\${out_dir_base}//;' | perl -pe 's/\///g;' | sort | uniq > $eval_target
#python json2tsv_linkjp.py $out_dir_base $gold_dir $in_dir $eval_target
#python evaluation_linkjp_old.py $out_dir_base $gold_dir $eval_target
#cd $out_dir_base
#cat */all_summary.tsv > all_summary_pre.tsv
#cat ../summary_header.txt all_summary_pre.tsv > all_summary.tsv
#cp all_summary.tsv eval_${now}.txt
#cp ~/PycharmProjects/linkjpc/linkjpc_all_sample.sh env_${now}.txt
#cat ./*/*_summary.tsv | grep -v SYS_ID | grep -v ^e | grep -v ^p | sort -d > summary_category_pre.tsv
#cat ../summary_cat_header.txt summary_category_pre.tsv > summary_category.tsv
#cp summary_category.tsv ${setting_dir}summary_category_${now}.txt
