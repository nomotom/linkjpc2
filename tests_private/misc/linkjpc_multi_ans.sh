#!/bin/sh -x

#評価対象から外すものは#をつける
script="./linkjpc.py"
common_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/common/"
tmp_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/test/"
gold_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-211027/link_annotation/"
in_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-211027/ene_annotation/"
out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/anal_multi_20211104/"
#out_dir_tmp_base="/Users/masako/tmp/test/tmp_test/"




#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_br_09_fr_09_amax_100M/ --mod w -f n --wlink l -wl_ratio bf -wl_bratio 0.9 -wl_fratio 0.9 -a_max 100000000


##### 5module: recall mint_p_tinm_p_02_slink_05_wlink_frp_l_06
####
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_01_cmax_100M_tinm_p_trim_01_slink_01_wlink_pl_l_01_amax_100M/ --mod mtswl -f n --mint p -m_min 0.1 -c_max 100000000 --tinm p -tmt trim -t_min 0.1 -s_min 0.1 --wlink pl -l_min 0.1 -a_max 100000000
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_01_cmax_100M_tinm_p_trim_01_slink_01_wlink_pl_pmax_100_nmax_100_l_01_amax_100M/ --mod mtswl -f n --mint p -m_min 0.1 -c_max 100000000 --tinm p -tmt trim -t_min 0.1 -s_min 0.1 --wlink pl --wl_lines_pre_max 100 --wl_lines_next_max 100 -l_min 0.1 -a_max 100000000
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_01_cmax_100M_tinm_p_trim_01_slink_01_wlink_pl_pmax_60_nmax_60_l_01_amax_100M/ --mod mtswl -f n --mint p -m_min 0.1 -c_max 100000000 --tinm p -tmt trim -t_min 0.1 -s_min 0.1 --wlink pl --wl_lines_pre_max 60 --wl_lines_next_max 60 -l_min 0.1 -a_max 100000000
#
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_01_cmax_100M_tinm_p_trim_01_slink_01_wlink_rpl_l_01_amax_100M/ --mod mtswl -f n --mint p -m_min 0.1 -c_max 100000000 --tinm p -tmt trim -t_min 0.1 -s_min 0.1 --wlink rpl -l_min 0.1 -a_max 100000000
#
#
#
####1 module
### 2021/10/20 from here
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_01/ --mod l -f n -l_min 0.1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_01_amax_1K/ --mod l -f n -l_min 0.1 -a_max 1000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_01_amax_10K/ --mod l -f n -l_min 0.1 -a_max 10000
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_01_amax_100M/ --mod l -f n -l_min 0.1 -a_max 100000000
#
### till here
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_02/ --mod l -f n -l_min 0.2
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_03/ --mod l -f n -l_min 0.3
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_04/ --mod l -f n -l_min 0.4
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_05/ --mod l -f n -l_min 0.5
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_06/ --mod l -f n -l_min 0.6
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_07/ --mod l -f n -l_min 0.7
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_08/ --mod l -f n -l_min 0.8
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_09/ --mod l -f n -l_min 0.9
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_10/ --mod l -f n -l_min 1.0
##
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e/ --mod m -f n --mint e
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_cmax_1K_amax_1K/ --mod m -f n --mint e -c_max 1000 -a_max 1000
#
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim/ --mod m -f n --mint e -tmm trim
### 2021/10/20 from here
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_cmax_1K_amax_1K/ --mod m -f n --mint e -tmm trim -c_max 1000 -a_max 1000
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_cmax_10K_amax_10K/ --mod m -f n --mint e -tmm trim -c_max 10000 -a_max 10000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_cmax_1M_amax_1M/ --mod m -f n --mint e -tmm trim -c_max 1000000 -a_max 1000000
#
### till here
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p/ --mod m -f n --mint
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_01_cmax_100_amax_100/ --mod m -f n --mint p -m_min 0.1 -c_max 100 -a_max 100
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_01_cmax_1K_amax_1K/ --mod m -f n --mint p -m_min 0.1 -c_max 1000 -a_max 1000
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_01_cmax_10K_amax_10K/ --mod m -f n --mint p -m_min 0.1 -c_max 10000 -a_max 10000
### 2021/10/20 from here
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_01_cmax_100K_amax_100K/ --mod m -f n --mint p -m_min 0.1 -c_max 100000 -a_max 100000
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_01_cmax_1M_amax_1M/ --mod m -f n --mint p -m_min 0.1 -c_max 1000000 -a_max 1000000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_01_cmax_10M_amax_10M/ --mod m -f n --mint p -m_min 0.1 -c_max 10000000 -a_max 10000000
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_01_cmax_100M_amax_100M/ --mod m -f n --mint p -m_min 0.1 -c_max 100000000 -a_max 100000000
### till here
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_02/ --mod m -f n --mint p -m_min 0.2
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_03/ --mod m -f n --mint p -m_min 0.3
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_04/ --mod m -f n --mint p -m_min 0.4
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_06/ --mod m -f n --mint p -m_min 0.6
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_07/ --mod m -f n --mint p -m_min 0.7
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_08/ --mod m -f n --mint p -m_min 0.8
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_09/ --mod m -f n --mint p -m_min 0.9
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_10/ --mod m -f n --mint p -m_min 1.0
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim/ --mod m -f n --mint p -tmm trim
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_01/ --mod m -f n --mint p -tmm trim -m_min 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_01_cmax_1K_amax_1K/ --mod m -f n --mint p -tmm trim -m_min 0.1 -a_max 1000
### 2021/10/20 done from here
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_01_cmax_10K_amax_10K/ --mod m -f n --mint p -tmm trim -m_min 0.1 -c_max 10000 -a_max 10000
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_01_cmax_100K_amax_100K/ --mod m -f n --mint p -tmm trim -m_min 0.1 -c_max 100000 -a_max 100000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_01_cmax_1M_amax_1M/ --mod m -f n --mint p -tmm trim -m_min 0.1 -c_max 1000000 -a_max 1000000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_01_cmax_10M_amax_10M/ --mod m -f n --mint p -tmm trim -m_min 0.1 -c_max 10000000 -a_max 10000000
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_01_cmax_100M_amax_100M/ --mod m -f n --mint p -tmm trim -m_min 0.1 -c_max 100000000 -a_max 100000000
#
### till here
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_02/ --mod m -f n --mint p -tmm trim -m_min 0.2
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_03/ --mod m -f n --mint p -tmm trim -m_min 0.3
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_04/ --mod m -f n --mint p -tmm trim -m_min 0.4
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_05/ --mod m -f n --mint p -tmm trim -m_min 0.5
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_06/ --mod m -f n --mint p -tmm trim -m_min 0.6
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_07/ --mod m -f n --mint p -tmm trim -m_min 0.7
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_08/ --mod m -f n --mint p -tmm trim -m_min 0.8
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_09/ --mod m -f n --mint p -tmm trim -m_min 0.9
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_trim_10/ --mod m -f n --mint p -tmm trim -m_min 1.0
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_01/ --mod s -f n -s_min 0.1
### later
#### 2021/10/20 done from here
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_01_amax_1K/ --mod s -f n -s_min 0.1 -a_max 1000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_01_amax_10K/ --mod s -f n -s_min 0.1 -a_max 10000
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_01_amax_100M/ --mod s -f n -s_min 0.1 -a_max 100000000
#
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_01_mid_amax_1K/ --mod s -f n -s_min 0.1 -s_prb mid -a_max 1000
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_01_mid_amax_10K/ --mod s -f n -s_min 0.1 -s_prb mid -a_max 10000
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_01_raw_amax_1K/ --mod s -f n -s_min 0.1 -s_prb raw -a_max 1000
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_01_raw_amax_10K/ --mod s -f n -s_min 0.1 -s_prb raw -a_max 10000
#
### till here
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_01_mid/ --mod s -f n -s_min 0.1 -s_prb mid
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_01_raw/ --mod s -f n -s_min 0.1 -s_prb raw
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_02/ --mod s -f n -s_min 0.2
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_02_mid/ --mod s -f n -s_min 0.2 -s_prb mid
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_02_raw/ --mod s -f n -s_min 0.2 -s_prb raw
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_03/ --mod s -f n -s_min 0.3
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_03_mid/ --mod s -f n -s_min 0.3 -s_prb mid
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_03_raw/ --mod s -f n -s_min 0.3 -s_prb raw
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_04/ --mod s -f n -s_min 0.4
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_04_mid/ --mod s -f n -s_min 0.4 -s_prb mid
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_04_raw/ --mod s -f n -s_min 0.4 -s_prb raw
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05/ --mod s -f n -s_min 0.5
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid/ --mod s -f n -s_min 0.5 -s_prb mid
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_raw/ --mod s -f n -s_min 0.5 -s_prb raw
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_06/ --mod s -f n -s_min 0.6
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_06_mid/ --mod s -f n -s_min 0.6 -s_prb mid
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_06_raw/ --mod s -f n -s_min 0.6 -s_prb raw
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_07/ --mod s -f n -s_min 0.7
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_07_mid/ --mod s -f n -s_min 0.7 -s_prb mid
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_07_raw/ --mod s -f n -s_min 0.7 -s_prb raw
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_08/ --mod s -f n -s_min 0.8
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_08_mid/ --mod s -f n -s_min 0.8 -s_prb mid
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_08_raw/ --mod s -f n -s_min 0.8 -s_prb raw
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_09/ --mod s -f n -s_min 0.9
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_09_mid/ --mod s -f n -s_min 0.9 -s_prb mid
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_09_raw/ --mod s -f n -s_min 0.9 -s_prb raw
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_10/ --mod s -f n -s_min 1.0
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_10_mid/ --mod s -f n -s_min 1.0 -s_prb mid
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_10_raw/ --mod s -f n -s_min 1.0 -s_prb raw
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e/ --mod t -f n --tinm e
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_cmax_1K_amax_1K/ --mod t -f n --tinm e -c_max 1000 -a_max 1000
#
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_trim/ --mod t -f n --tinm p -tmt trim
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_trim_cmax_1K_amax_1K/ --mod t -f n --tinm e -tmt trim -c_max 1000 -a_max 1000
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_trim_cmax_10K_amax_10K/ --mod t -f n --tinm e -tmt trim -c_max 10000 -a_max 10000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_trim_cmax_100K_amax_100K/ --mod t -f n --tinm e -tmt trim -c_max 100000 -a_max 100000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_trim_cmax_1M_amax_1M/ --mod t -f n --tinm p -tmt trim -c_max 1000000 -a_max 1000000
#
##
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p/ --mod t -f n --tinm p
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_01/ --mod t -f n --tinm p -t_min 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_01_cmax_1K_amax_1K/ --mod t -f n --tinm p -t_min 0.1 -c_max 1000 -a_max 1000
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_01_cmax_10K_amax_10K/ --mod t -f n --tinm p -t_min 0.1 -c_max 10000 -a_max 10000
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_01_cmax_100K_amax_100K/ --mod t -f n --tinm p -t_min 0.1 -c_max 100000 -a_max 100000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_01_cmax_1M_amax_1M/ --mod t -f n --tinm p -t_min 0.1 -c_max 1000000 -a_max 1000000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_01_cmax_10M_amax_10M/ --mod t -f n --tinm p -t_min 0.1 -c_max 10000000 -a_max 10000000
##
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_02/ --mod t -f n --tinm p -t_min 0.2
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_03/ --mod t -f n --tinm p -t_min 0.3
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_04/ --mod t -f n --tinm p -t_min 0.4
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_05/ --mod t -f n --tinm p -t_min 0.5
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_06/ --mod t -f n --tinm p -t_min 0.6
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_07/ --mod t -f n --tinm p -t_min 0.7
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_08/ --mod t -f n --tinm p -t_min 0.8
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_09/ --mod t -f n --tinm p -t_min 0.9
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_10/ --mod t -f n --tinm p -t_min 1.0
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim/ --mod t -f n --tinm p -tmt trim
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_01/ --mod t -f n --tinm p -tmt trim -t_min 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_01_cmax_1K_amax_1K/ --mod t -f n --tinm p -tmt trim -t_min 0.1 -c_max 1000 -a_max 1000
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_01_cmax_10K_amax_10K/ --mod t -f n --tinm p -tmt trim -t_min 0.1 -c_max 10000 -a_max 10000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_01_cmax_100K_amax_100K/ --mod t -f n --tinm p -tmt trim -t_min 0.1 -c_max 100000 -a_max 100000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_01_cmax_1M_amax_1M/ --mod t -f n --tinm p -tmt trim -t_min 0.1 -c_max 1000000 -a_max 1000000
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_01_cmax_100M_amax_100M/ --mod t -f n --tinm p -tmt trim -t_min 0.1 -c_max 100000000 -a_max 100000000
#
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_02/ --mod t -f n --tinm p -tmt trim -t_min 0.2
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_03/ --mod t -f n --tinm p -tmt trim -t_min 0.3
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_04/ --mod t -f n --tinm p -tmt trim -t_min 0.4
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_05/ --mod t -f n --tinm p -tmt trim -t_min 0.5
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_06/ --mod t -f n --tinm p -tmt trim -t_min 0.6
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_07/ --mod t -f n --tinm p -tmt trim -t_min 0.7
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_08/ --mod t -f n --tinm p -tmt trim -t_min 0.8
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_09/ --mod t -f n --tinm p -tmt trim -t_min 0.9
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_10/ --mod t -f n --tinm p -tmt trim -t_min 1.0
### 2021/10/20 done from here
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f/ --mod w -f n --wlink f
### later
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_amax_1K/ --mod w -f n --wlink f -a_max 1000
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_amax_1M/ --mod w -f n --wlink f -a_max 1000000
#
###till here
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_01/ --mod w -f n --wlink f -wf 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_02/ --mod w -f n --wlink f -wf 0.2
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_03/ --mod w -f n --wlink f -wf 0.3
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_04/ --mod w -f n --wlink f -wf 0.4
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_05/ --mod w -f n --wlink f -wf 0.5
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_06/ --mod w -f n --wlink f -wf 0.6
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_07/ --mod w -f n --wlink f -wf 0.7
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_08/ --mod w -f n --wlink f -wf 0.8
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_09/ --mod w -f n --wlink f -wf 0.9
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f_10/ --mod w -f n --wlink f -wf 1.0
### 20211020 done from here
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fl/ --mod w -f n --wlink fl
###later
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fl_amax_1K/ --mod w -f n --wlink fl -a_max 1000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fl_amax_1M/ --mod w -f n --wlink fl -a_max 1000000
#
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fp/ --mod w -f n --wlink fp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fp_amax_1K/ --mod w -f n --wlink fp -a_max 1000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fp_amax_1M/ --mod w -f n --wlink fp -a_max 1000000
#
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fr/ --mod w -f n --wlink fr
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fr_amax_1K/ --mod w -f n --wlink fr -a_max 1000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fr_amax_1M/ --mod w -f n --wlink fr -a_max 1000000
#
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frl/ --mod w -f n --wlink frl
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frl_amax_1K/ --mod w -f n --wlink frl -a_max 1000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frl_amax_1M/ --mod w -f n --wlink frl -a_max 1000000
#
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp/ --mod w -f n --wlink frp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp_amax_1K/ --mod w -f n --wlink frp -a_max 1000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp_amax_1M/ --mod w -f n --wlink frp -a_max 1000000
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl/ --mod w -f n --wlink frpl
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl_amax_1K/ --mod w -f n --wlink frpl -a_max 1000
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl_amax_10K/ --mod w -f n --wlink frpl -a_max 10000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl_amax_100K/ --mod w -f n --wlink frpl -a_max 100000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl_amax_1M/ --mod w -f n --wlink frpl -a_max 1000000
#
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l/ --mod w -f n --wlink l
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_amax_1K/ --mod w -f n --wlink l -a_max 1000
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_amax_1M/ --mod w -f n --wlink l -a_max 1000000
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_09_fcar_09_amax_1M/ --mod w -f n --wlink l -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.9 -wl_fca r -wl_fca_ratio 0.9 -a_max 1000000
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_09_fcar_09_amax_1M/ --mod w -f n --wlink l -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.9 -wl_fca r -wl_fca_ratio 0.9
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_08_fcar_08_amax_1M/ --mod w -f n --wlink l -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.8 -wl_fca r -wl_fca_ratio 0.8
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_07_fcar_07_amax_1M/ --mod w -f n --wlink l -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.7 -wl_fca r -wl_fca_ratio 0.7
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_06_fcar_06_amax_1M/ --mod w -f n --wlink l -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.6 -wl_fca r -wl_fca_ratio 0.6
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_05_fcar_05_amax_1M/ --mod w -f n --wlink l -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.5 -wl_fca r -wl_fca_ratio 0.5
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_04_fcar_04_amax_1M/ --mod w -f n --wlink l -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.4 -wl_fca r -wl_fca_ratio 0.4
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_03_fcar_03_amax_1M/ --mod w -f n --wlink l -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.3 -wl_fca r -wl_fca_ratio 0.3
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_02_fcar_02_amax_1M/ --mod w -f n --wlink l -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.2 -wl_fca r -wl_fca_ratio 0.2
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_01_fcar_01_amax_1M/ --mod w -f n --wlink l -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.1 -wl_fca r -wl_fca_ratio 0.1
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_09_fcar_01_amax_1M/ --mod w -f n --wlink l -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.9 -wl_fca r -wl_fca_ratio 0.9
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_08_fcar_01_amax_1M/ --mod w -f n --wlink l -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.8 -wl_fca r -wl_fca_ratio 0.8
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_07_fcar_01_amax_1M/ --mod w -f n --wlink l -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.7 -wl_fca r -wl_fca_ratio 0.7
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_06_fcar_01_amax_1M/ --mod w -f n --wlink l -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.6 -wl_fca r -wl_fca_ratio 0.6
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_05_fcar_01_amax_1M/ --mod w -f n --wlink l -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.5 -wl_fca r -wl_fca_ratio 0.5
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_04_fcar_01_amax_1M/ --mod w -f n --wlink l -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.4 -wl_fca r -wl_fca_ratio 0.4
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_03_fcar_01_amax_1M/ --mod w -f n --wlink l -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.3 -wl_fca r -wl_fca_ratio 0.3
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_02_fcar_01_amax_1M/ --mod w -f n --wlink l -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.2 -wl_fca r -wl_fca_ratio 0.2
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_09_fcar_09_amax_1M/ --mod w -f n --wlink lr -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.9 -wl_fca r -wl_fca_ratio 0.9
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_08_fcar_08_amax_1M/ --mod w -f n --wlink lr -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.8 -wl_fca r -wl_fca_ratio 0.8
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_07_fcar_07_amax_1M/ --mod w -f n --wlink lr -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.7 -wl_fca r -wl_fca_ratio 0.7
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_06_fcar_06_amax_1M/ --mod w -f n --wlink lr -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.6 -wl_fca r -wl_fca_ratio 0.6
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_05_fcar_05_amax_1M/ --mod w -f n --wlink lr -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.5 -wl_fca r -wl_fca_ratio 0.5
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_04_fcar_04_amax_1M/ --mod w -f n --wlink lr -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.4 -wl_fca r -wl_fca_ratio 0.4
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_03_fcar_03_amax_1M/ --mod w -f n --wlink lr -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.3 -wl_fca r -wl_fca_ratio 0.3
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_02_fcar_02_amax_1M/ --mod w -f n --wlink lr -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.2 -wl_fca r -wl_fca_ratio 0.2
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_01_fcar_01_amax_1M/ --mod w -f n --wlink lr -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.1 -wl_fca r -wl_fca_ratio 0.1
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_09_fcar_01_amax_1M/ --mod w -f n --wlink lr -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.9 -wl_fca r -wl_fca_ratio 0.9
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_08_fcar_01_amax_1M/ --mod w -f n --wlink lr -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.8 -wl_fca r -wl_fca_ratio 0.8
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_07_fcar_01_amax_1M/ --mod w -f n --wlink lr -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.7 -wl_fca r -wl_fca_ratio 0.7
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_06_fcar_01_amax_1M/ --mod w -f n --wlink lr -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.6 -wl_fca r -wl_fca_ratio 0.6
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_05_fcar_01_amax_1M/ --mod w -f n --wlink lr -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.5 -wl_fca r -wl_fca_ratio 0.5
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_04_fcar_01_amax_1M/ --mod w -f n --wlink lr -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.4 -wl_fca r -wl_fca_ratio 0.4
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_03_fcar_01_amax_1M/ --mod w -f n --wlink lr -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.3 -wl_fca r -wl_fca_ratio 0.3
python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_02_fcar_01_amax_1M/ --mod w -f n --wlink lr -a_max 1000000 --wl_break 0 -wl_bca r -wl_bca_ratio 0.2 -wl_fca r -wl_fca_ratio 0.2

#### till here
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls_01/ --mod w -f n --wlink l -wls 0.1
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls_02/ --mod w -f n --wlink l -wls 0.2
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls_03/ --mod w -f n --wlink l -wls 0.3
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls_04/ --mod w -f n --wlink l -wls 0.4
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls_05/ --mod w -f n --wlink l -wls 0.5
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls_06/ --mod w -f n --wlink l -wls 0.6
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls_07/ --mod w -f n --wlink l -wls 0.7
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls_08/ --mod w -f n --wlink l -wls 0.8
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls_09/ --mod w -f n --wlink l -wls 0.9
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls_10/ --mod w -f n --wlink l -wls 1.0
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlf_01/ --mod w -f n --wlink l -wlf 0.1
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlf_02/ --mod w -f n --wlink l -wlf 0.2
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlf_03/ --mod w -f n --wlink l -wlf 0.3
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlf_04/ --mod w -f n --wlink l -wlf 0.4
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlf_05/ --mod w -f n --wlink l -wlf 0.5
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlf_06/ --mod w -f n --wlink l -wlf 0.6
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlf_07/ --mod w -f n --wlink l -wlf 0.7
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlf_08/ --mod w -f n --wlink l -wlf 0.8
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlf_09/ --mod w -f n --wlink l -wlf 0.9
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlf_10/ --mod w -f n --wlink l -wlf 1.0
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlb_01/ --mod w -f n --wlink l -wlb 0.1
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlb_02/ --mod w -f n --wlink l -wlb 0.2
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlb_03/ --mod w -f n --wlink l -wlb 0.3
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlb_04/ --mod w -f n --wlink l -wlb 0.4
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlb_05/ --mod w -f n --wlink l -wlb 0.5
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlb_06/ --mod w -f n --wlink l -wlb 0.6
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlb_07/ --mod w -f n --wlink l -wlb 0.7
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlb_08/ --mod w -f n --wlink l -wlb 0.8
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlb_09/ --mod w -f n --wlink l -wlb 0.9
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlb_10/ --mod w -f n --wlink l -wlb 1.0
#### 2020/10/20　from here
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_m/ --mod w -f n --wlink m
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_m_amax_1K/ --mod w -f n --wlink m -a_max 1000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_m_amax_1M/ --mod w -f n --wlink m -a_max 1000000
#
###
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_ml/ --mod w -f n --wlink ml
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_ml_amax_1K/ --mod w -f n --wlink ml -a_max 1000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_ml_amax_1M/ --mod w -f n --wlink ml -a_max 1000000
#
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mp/ --mod w -f n --wlink mp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mp_amax_1K/ --mod w -f n --wlink mp -a_max 1000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mp_amax_1M/ --mod w -f n --wlink mp -a_max 1000000
#
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mpl/ --mod w -f n --wlink mpl
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mpl_amax_1K/ --mod w -f n --wlink mpl -a_max 1000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mpl_amax_100K/ --mod w -f n --wlink mpl -a_max 100000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mpl_amax_1M/ --mod w -f n --wlink mpl -a_max 1000000
#
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p/ --mod w -f n --wlink p
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p_amax_1K/ --mod w -f n --wlink p -a_max 1000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p_amax_1M/ --mod w -f n --wlink p -a_max 1000000
#### till here
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p_01/ --mod w -f n --wlink p -wp 0.1
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p_02/ --mod w -f n --wlink p -wp 0.2
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p_03/ --mod w -f n --wlink p -wp 0.3
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p_04/ --mod w -f n --wlink p -wp 0.4
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p_05/ --mod w -f n --wlink p -wp 0.5
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p_06/ --mod w -f n --wlink p -wp 0.6
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p_07/ --mod w -f n --wlink p -wp 0.7
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p_08/ --mod w -f n --wlink p -wp 0.8
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p_09/ --mod w -f n --wlink p -wp 0.9
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p_10/ --mod w -f n --wlink p -wp 1.0
#### 2020/10/20　from here
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_pl/ --mod w -f n --wlink pl
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_pl_amax_1K/ --mod w -f n --wlink pl -a_max 1000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_pl_amax_1M/ --mod w -f n --wlink pl -a_max 1000000
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_pl_amax_100M/ --mod w -f n --wlink pl -a_max 100000000
#
####
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r/ --mod w -f n --wlink r
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_amax_1K/ --mod w -f n --wlink r -a_max 1000
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_amax_1M/ --mod w -f n --wlink r -a_max 1000000
#
#### till here
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_01/ --mod w -f n --wlink r -wr 0.1
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_02/ --mod w -f n --wlink r -wr 0.2
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_03/ --mod w -f n --wlink r -wr 0.3
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_04/ --mod w -f n --wlink r -wr 0.4
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_05/ --mod w -f n --wlink r -wr 0.5
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_06/ --mod w -f n --wlink r -wr 0.6
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_07/ --mod w -f n --wlink r -wr 0.7
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_08/ --mod w -f n --wlink r -wr 0.8
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_09/ --mod w -f n --wlink r -wr 0.9
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_10/ --mod w -f n --wlink r -wr 1.0
###
#### 2021/10/20 from here
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl/ --mod w -f n --wlink rl
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_amax_1K/ --mod w -f n --wlink rl -a_max 1000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_amax_1M/ --mod w -f n --wlink rl -a_max 1000000
#
####
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp/ --mod w -f n --wlink rp
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp_amax_1K/ --mod w -f n --wlink rp -a_max 1000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp_amax_1M/ --mod w -f n --wlink rp -a_max 1000000
#
####
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rpl/ --mod w -f n --wlink rpl
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rpl_amax_1K/ --mod w -f n --wlink rpl -a_max 1000
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rpl_amax_10K/ --mod w -f n --wlink rpl -a_max 10000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rpl_amax_100K/ --mod w -f n --wlink rpl -a_max 100000
##done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rpl_amax_1M/ --mod w -f n --wlink rpl -a_max 1000000
#
#### till here
###
