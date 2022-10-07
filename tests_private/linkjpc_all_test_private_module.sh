#!/bin/sh -x

# 実行前
# scoreファイルを作成
# evalファイルをコピー
# 実行結果ディレクトリを修正

#評価対象から外すものは##をつける
#script="./linkjpc_org.py"
#common_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/common/"
#tmp_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/test/"
#gold_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-211027/link_annotation/"
#in_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-211027/ene_annotation/"
#out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/anal_20211125/"
##out_dir_tmp_base="/Users/masako/tmp/test/tmp_test/"

script="./linkjpc/linkjpc.py"
# base_dir_shinra2021="/Users/masako/Documents/SHINRA/2021-LinkJP/"
base_dir_shinra2022="/Users/masako/Documents/SHINRA/2022-LinkJP/"

# base_data_dir_shinra2021="${base_dir_shinra2021}Download/"
# base_dir_ljp2022="/Users/masako/Documents/SHINRA/2022-LinkJP/"
base_data_dir_ljp2022="${base_dir_shinra2022}Download/"

common_data_dir="${base_data_dir_ljp2022}ljc_data/common/"

#########################################################################################
# 入力とtmp_data, out　を以下のいずれかにセットする
# 1) formal
# in_dir="${base_data_dir_ljp2022}formal-link-ans-20220816/"
# tmp_data_dir="${base_data_dir_ljp2022}ljc_data/test_formal/"
# out_dir_base="${base_dir_shinra2022}test_out_formal/out_formal_20220830/"

# 2) training
# 20220909
#in_dir="${base_data_dir_ljp2022}ljc_data/train-link-20220712/"
## tmp_data_dir="${base_data_dir_ljp2022}ljc_data/test_training/"
## out_dir_base="${base_dir_shinra2022}test_out_training/out_training_20220909/"
#out_dir_base="${base_dir_shinra2022}test_out_training/out_training_20220909_test/"

# sample_gold_dir_ljp2022="${base_dir_shinra2022}Download/ljc_data/train-link-20220712/"

# sample_gold_dir="${sample_gold_dir_ljp2022}"
# sample_input_dir="${base_dir_ljp2022}Download/ljc_data/train-link-20220712/ene_annotation/"
# 20220822
# sample_input_dir="${base_dir_shinra2022}Download/ljc_data/train-link-20220712/"

# 3) leaderboard
in_dir="${base_data_dir_ljp2022}leaderboard-link-ans-20220826/"
tmp_data_dir="${base_data_dir_ljp2022}ljc_data/test_leaderboard/"
#out_dir_base="${base_dir_shinra2022}test_out_leaderboard/out_leaderboard_20220907/"
# out_dir_base="${base_dir_shinra2022}test_out_leaderboard/out_leaderboard_20220917/"
# 20220923
out_dir_base="${base_dir_shinra2022}test_out_leaderboard/out_leaderboard_20220925/"
sample_gold_dir_ljp2022="${base_dir_shinra2022}Download/ljc_data/train-link-20220712/"

sample_gold_dir="${sample_gold_dir_ljp2022}"
# sample_input_dir="${base_dir_ljp2022}Download/ljc_data/train-link-20220712/ene_annotation/"
# 20220822
sample_input_dir="${base_dir_shinra2022}Download/ljc_data/train-link-20220712/conv/"
#########################################################################################


# tmp_data_dir="${base_data_dir_shinra2022}ljc_data/test/"

# 20220822
# in_dir="${base_data_dir_shinra2022}leaderboard-link-ans-20220816/"

# 20220829 sample data
# in_dir="${base_data_dir_shinra2022}ljc_data/train-link-20220712/"

# in_dir="${base_data_dir_shinra2022}leaderboard-link-ans-20220816/ene_annotation/"
# in_dir="${base_data_dir_shinra2022}linkjp-eval-211027/ene_annotation/"
# out_dir_base="${base_dir_shinra2022}test_out/shinra2021base_20220829/"




# python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wl_bmax10_fmax2/ --mod w -f n --wlink l -wl_bmax 10 -wl_fmax 2
# python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wl_bmax10_fmax2/ --mod w -f n --wlink l -wl_bmax 10 -wl_fmax 2
# python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_frpl_bmax_5_attr_w_art_a_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frpl -wl_bmax 5 -ar_tgt w -al am -bl_tgt w

# 20220818
# python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w -l_min 0.6
# python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w -l_min 0.6

# 20220819
#
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7


# 昨年改良
# 20220824
# 20220826
# 20220830
# leaderboard

# leaderboard1
## （１）9/5リーダーボード投稿分と一緒に実行　ここから
## leaderboard-1: 1位：full nil判定 Wのみ：9/6　1回目投稿分
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#
### leaderboard-2: 1位：full nil判定 Wのみ, exc_woなし: 9/6 2回目投稿分　→　現在のベース
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#
##
## 被リンク
##python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_ncond_w_two_of_pld_02_7_exc_wo_incl_m_imax1_o/ --mod m -f in --mint e -i_tgt m -i_max 1 -i_type o -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#
#　9/25ここから整理
# 1 module ###
# (m)
# (mint -e) 2022/9/25
## no filtering
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e/ --mod m --mint e -f x
## nil filtering
## n_cond
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_nc_topld_nm_02_ld_7/ --mod m --mint e -f n -n_tgt m -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_nc_apld_nm_02_ld_7/ --mod m --mint e -f n -n_tgt m -n_cond and_prob_len_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_nc_alopd_nm_02_ld_7/ --mod m --mint e -f n -n_tgt m -n_cond and_len_or_prob_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_nc_adopl_nm_02_ld_7/ --mod m --mint e -f n -n_tgt m -n_cond and_desc_or_prob_len -n_max 0.2 -ld_min 7
### ld_min
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_nc_topld_nm_02_ld_7/ --mod m --mint e -f n -n_tgt m -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 8
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_nc_apld_nm_02_ld_7/ --mod m --mint e -f n -n_tgt m -n_cond and_prob_len_desc -n_max 0.2 -ld_min 8
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_nc_alopd_nm_02_ld_7/ --mod m --mint e -f n -n_tgt m -n_cond and_len_or_prob_desc -n_max 0.2 -ld_min 8
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_nc_adopl_nm_02_ld_7/ --mod m --mint e -f n -n_tgt m -n_cond and_desc_or_prob_len -n_max 0.2 -ld_min 8

python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_nc_topld_nm_02_ld_9/ --mod m --mint e -f n -n_tgt m -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 9
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_nc_apld_nm_02_ld_9/ --mod m --mint e -f n -n_tgt m -n_cond and_prob_len_desc -n_max 0.2 -ld_min 9
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_nc_alopd_nm_02_ld_9/ --mod m --mint e -f n -n_tgt m -n_cond and_len_or_prob_desc -n_max 0.2 -ld_min 9
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_nc_adopl_nm_02_ld_9/ --mod m --mint e -f n -n_tgt m -n_cond and_desc_or_prob_len -n_max 0.2 -ld_min 9

### n_max
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_nc_topld_nm_01_ld_7/ --mod m --mint e -f n -n_tgt m -n_cond two_of_prob_len_desc -n_max 0.1 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_nc_apld_nm_01_ld_7/ --mod m --mint e -f n -n_tgt m -n_cond and_prob_len_desc -n_max 0.1 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_nc_alopd_nm_01_ld_7/ --mod m --mint e -f n -n_tgt m -n_cond and_len_or_prob_desc -n_max 0.1 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_nc_adopl_nm_01_ld_7/ --mod m --mint e -f n -n_tgt m -n_cond and_desc_or_prob_len -n_max 0.1 -ld_min 7
#
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_nc_topld_nm_03_ld_7/ --mod m --mint e -f n -n_tgt m -n_cond two_of_prob_len_desc -n_max 0.3 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_nc_apld_nm_03_ld_7/ --mod m --mint e -f n -n_tgt m -n_cond and_prob_len_desc -n_max 0.3 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_nc_alopd_nm_03_ld_7/ --mod m --mint e -f n -n_tgt m -n_cond and_len_or_prob_desc -n_max 0.3 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_nc_adopl_nm_03_ld_7/ --mod m --mint e -f n -n_tgt m -n_cond and_desc_or_prob_len -n_max 0.3 -ld_min 7

# (mint -p)
# no filtering
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_02/ --mod m --mint p -m_min 0.2 -f x
# m_min
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_03/ --mod m --mint p -m_min 0.3 -f x
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_04/ --mod m --mint p -m_min 0.4 -f x
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_05/ --mod m --mint p -m_min 0.5 -f x
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_06/ --mod m --mint p -m_min 0.6 -f x
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_07/ --mod m --mint p -m_min 0.7 -f x
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_08/ --mod m --mint p -m_min 0.8 -f x
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_09/ --mod m --mint p -m_min 0.9 -f x

## nil filtering
## n_cond
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_02_nc_topld_nm_02_ld_7/ --mod m --mint p -m_min 0.2 -f n -n_tgt m -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_02_nc_apld_nm_02_ld_7/ --mod m --mint p -m_min 0.2 -f n -n_tgt m -n_cond and_prob_len_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_02_nc_alopd_nm_02_ld_7/ --mod m --mint p -m_min 0.2 -f n -n_tgt m -n_cond and_len_or_prob_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_02_nc_adopl_nm_02_ld_7/ --mod m --mint p -m_min 0.2 -f n -n_tgt m -n_cond and_desc_or_prob_len -n_max 0.2 -ld_min 7

python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_03_nc_topld_nm_02_ld_7/ --mod m --mint p -m_min 0.3 -f n -n_tgt m -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_03_nc_apld_nm_02_ld_7/ --mod m --mint p -m_min 0.3 -f n -n_tgt m -n_cond and_prob_len_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_03_nc_alopd_nm_02_ld_7/ --mod m --mint p -m_min 0.3 -f n -n_tgt m -n_cond and_len_or_prob_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_03_nc_adopl_nm_02_ld_7/ --mod m --mint p -m_min 0.3 -f n -n_tgt m -n_cond and_desc_or_prob_len -n_max 0.2 -ld_min 7

python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_04_nc_topld_nm_02_ld_7/ --mod m --mint p -m_min 0.4 -f n -n_tgt m -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_04_nc_apld_nm_02_ld_7/ --mod m --mint p -m_min 0.4 -f n -n_tgt m -n_cond and_prob_len_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_04_nc_alopd_nm_02_ld_7/ --mod m --mint p -m_min 0.4 -f n -n_tgt m -n_cond and_len_or_prob_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_04_nc_adopl_nm_02_ld_7/ --mod m --mint p -m_min 0.4 -f n -n_tgt m -n_cond and_desc_or_prob_len -n_max 0.2 -ld_min 7

python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_05_nc_topld_nm_02_ld_7/ --mod m --mint p -m_min 0.5 -f n -n_tgt m -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_05_nc_apld_nm_02_ld_7/ --mod m --mint p -m_min 0.5 -f n -n_tgt m -n_cond and_prob_len_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_05_nc_alopd_nm_02_ld_7/ --mod m --mint p -m_min 0.5 -f n -n_tgt m -n_cond and_len_or_prob_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_05_nc_adopl_nm_02_ld_7/ --mod m --mint p -m_min 0.5 -f n -n_tgt m -n_cond and_desc_or_prob_len -n_max 0.2 -ld_min 7

python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_06_nc_topld_nm_02_ld_7/ --mod m --mint p -m_min 0.6 -f n -n_tgt m -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_06_nc_apld_nm_02_ld_7/ --mod m --mint p -m_min 0.6 -f n -n_tgt m -n_cond and_prob_len_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_06_nc_alopd_nm_02_ld_7/ --mod m --mint p -m_min 0.6 -f n -n_tgt m -n_cond and_len_or_prob_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_06_nc_adopl_nm_02_ld_7/ --mod m --mint p -m_min 0.6 -f n -n_tgt m -n_cond and_desc_or_prob_len -n_max 0.2 -ld_min 7

python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_07_nc_topld_nm_02_ld_7/ --mod m --mint p -m_min 0.7 -f n -n_tgt m -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_07_nc_apld_nm_02_ld_7/ --mod m --mint p -m_min 0.7 -f n -n_tgt m -n_cond and_prob_len_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_07_nc_alopd_nm_02_ld_7/ --mod m --mint p -m_min 0.7 -f n -n_tgt m -n_cond and_len_or_prob_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_07_nc_adopl_nm_02_ld_7/ --mod m --mint p -m_min 0.7 -f n -n_tgt m -n_cond and_desc_or_prob_len -n_max 0.2 -ld_min 7

python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_08_nc_topld_nm_02_ld_7/ --mod m --mint p -m_min 0.8 -f n -n_tgt m -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_08_nc_apld_nm_02_ld_7/ --mod m --mint p -m_min 0.8 -f n -n_tgt m -n_cond and_prob_len_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_08_nc_alopd_nm_02_ld_7/ --mod m --mint p -m_min 0.8 -f n -n_tgt m -n_cond and_len_or_prob_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_08_nc_adopl_nm_02_ld_7/ --mod m --mint p -m_min 0.8 -f n -n_tgt m -n_cond and_desc_or_prob_len -n_max 0.2 -ld_min 7

python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_09_nc_topld_nm_02_ld_7/ --mod m --mint p -m_min 0.9 -f n -n_tgt m -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_09_nc_apld_nm_02_ld_7/ --mod m --mint p -m_min 0.9 -f n -n_tgt m -n_cond and_prob_len_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_09_nc_alopd_nm_02_ld_7/ --mod m --mint p -m_min 0.9 -f n -n_tgt m -n_cond and_len_or_prob_desc -n_max 0.2 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_09_nc_adopl_nm_02_ld_7/ --mod m --mint p -m_min 0.9 -f n -n_tgt m -n_cond and_desc_or_prob_len -n_max 0.2 -ld_min 7

## ld_min








## n_max
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_02_nc_topld_nm_01_ld_7/ --mod m --mint p -m_min 0.2 -f n -n_tgt m -n_cond two_of_prob_len_desc -n_max 0.1 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_02_nc_apld_nm_01_ld_7/ --mod m --mint p -m_min 0.2 -f n -n_tgt m -n_cond and_prob_len_desc -n_max 0.1 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_02_nc_alopd_nm_01_ld_7/ --mod m --mint p -m_min 0.2 -f n -n_tgt m -n_cond and_len_or_prob_desc -n_max 0.1 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_02_nc_adopl_nm_01_ld_7/ --mod m --mint p -m_min 0.2 -f n -n_tgt m -n_cond and_desc_or_prob_len -n_max 0.1 -ld_min 7

python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_02_nc_topld_nm_03_ld_7/ --mod m --mint p -m_min 0.2 -f n -n_tgt m -n_cond two_of_prob_len_desc -n_max 0.3 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_02_nc_apld_nm_03_ld_7/ --mod m --mint p -m_min 0.2 -f n -n_tgt m -n_cond and_prob_len_desc -n_max 0.3 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_02_nc_alopd_nm_03_ld_7/ --mod m --mint p -m_min 0.2 -f n -n_tgt m -n_cond and_len_or_prob_desc -n_max 0.3 -ld_min 7
python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_p_mm_02_nc_adopl_nm_03_ld_7/ --mod m --mint p -m_min 0.2 -f n -n_tgt m -n_cond and_desc_or_prob_len -n_max 0.3 -ld_min 7


# (l)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}l_06/ --mod l -l_min 0.6 -f x
# (s)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_mid/ --mod s -s_min 0.5 -s_prb mid -f x
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_fixed/ --mod s -s_min 0.5 -s_prb fixed -f x
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_raw/ --mod s -s_min 0.5 -s_prb raw -f x
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_r_est/ --mod s -s_min 0.5 -s_prb r_est -f x
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est/ --mod s -s_min 0.5 -s_prb m_est -f x
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_f_est/ --mod s -s_min 0.5 -s_prb f_est -f x
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_06_mid/ --mod s -s_min 0.6 -s_prb mid -f x
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_06_fixed/ --mod s -s_min 0.6 -s_prb fixed -f x
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_06_raw/ --mod s -s_min 0.6 -s_prb raw -f x
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_06_r_est/ --mod s -s_min 0.6 -s_prb r_est -f x
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_06_m_est/ --mod s -s_min 0.6 -s_prb m_est -f x
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_06_f_est/ --mod s -s_min 0.6 -s_prb f_est -f x

# 1 module (フィルタあり) ###
# (m)
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e/ --mod m --mint -f x

# (m) + nil
# (l)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}l_06/ --mod l -l_min 0.6 -f x
# (s)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_mid/ --mod s -s_min 0.5 -s_prb mid -f x
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_fixed/ --mod s -s_min 0.5 -s_prb fixed -f x
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_raw/ --mod s -s_min 0.5 -s_prb raw -f x
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_r_est/ --mod s -s_min 0.5 -s_prb r_est -f x
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est/ --mod s -s_min 0.5 -s_prb m_est -f x
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_f_est/ --mod s -s_min 0.5 -s_prb f_est -f x
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_06_mid/ --mod s -s_min 0.6 -s_prb mid -f x
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_06_fixed/ --mod s -s_min 0.6 -s_prb fixed -f x
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_06_raw/ --mod s -s_min 0.6 -s_prb raw -f x
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_06_r_est/ --mod s -s_min 0.6 -s_prb r_est -f x
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_06_m_est/ --mod s -s_min 0.6 -s_prb m_est -f x
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_06_f_est/ --mod s -s_min 0.6 -s_prb f_est -f x


# (w)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}wlink_rp_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod w -f abn --wlink rp -ar_tgt w -art a -al am -bl_tgt w -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}wlink_rp_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_m_al_am_bl_w/ --mod w -f abn --wlink rp -ar_tgt w -art m -al am -bl_tgt w -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}wlink_rp_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_ma_al_am_bl_w/ --mod w -f abn --wlink rp -ar_tgt w -art ma -al am -bl_tgt w -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works

#   ## 3 module
#   ### self linkなし (m:lw)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod m:lw -f abn --mint e --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ### リンク確率なし (s:m:w)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod s:m:w -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ### wlinkなし (s:m:l)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__l_06/ --mod s:m:l --mint e -s_min 0.5 -s_prb m_est -l_min 0.6 -f x
#   ### mintなし (s:lw)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__wlink_rp_l_06_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod s:lw -f abn -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ##
#   ## 2 module ここから
#   ## (m:l)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e__l_06/ --mod m:l --mint e -l_min 0.6 -f x
#   ## (m:w)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e__wlink_rp_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod m:w -f abn --mint e --wlink rp -ar_tgt w -art a -al am -bl_tgt w -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ## (lw)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}wlink_rp_l_06_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod lw -f abn --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ### (s:m)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e/ --mod s:m --mint e -s_min 0.5 -s_prb m_est -f x
#   ### (s:w)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__wlink_rp_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod s:w -f abn -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ### (s:l)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__l_06/ --mod s:l -s_min 0.5 -s_prb m_est -l_min 0.6 -f x
#   #



   ## (w)(attrなし)
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}wlink_rp_ncond_w_two_of_pld_02_7_exc_wo_bl_w/ --mod w -f bn --wlink rp -bl_tgt w -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -n_exc person_works -ld_min 7
   ## (w)(blなし)
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}wlink_rp_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am/ --mod w -f an --wlink rp -ar_tgt w -art a -al am -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works

## 9/7
#### leaderboard1ベース ###################################
###
#### (1)
#### leaderboard-1: 1位：full nil判定 Wのみ, exc_woあり：9/6　1回目投稿分 exact match
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
# 比較：slink オプション
#   ## slink 新オプション　m_est
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   #
#   ## slink 新オプション　r_est
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_r_est__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb r_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   #
#   #
# 比較用

# 比較用  filterなし
# nil判定なし
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f ab --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6
#   ### blなし
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am/ --mod s:m:lw -f an --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -n_exc person_works -ld_min 7　
#   ### attrなし
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_exc_wo_bl_w/ --mod s:m:lw -f bn --mint e -s_min 0.5 -s_prb m_est --wlink rp -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -n_exc person_works -ld_min 7　
#   ##
#   ## nil判定の対象モジュールのバリエーション　
#   ## full nil判定 M, S, W, L
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_smwl_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt smwl -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   #
#   ### full nil判定 M, S, Wのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_msw_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt msw -l_min 0.6 -n_tgt msw -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ##
#   ### full nil判定 S, W, Lのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_swl_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt msw -l_min 0.6 -n_tgt swl -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ##
#   ### full nil判定 M, Wのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_mw_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt mw -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ##
#   ### full nil判定 S, Wのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_sw_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt sw -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ##
#   ### full nil判定 L, Wのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_lw_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt lw -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ##
#   ### full nil判定 Mのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_m_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt m -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ##
#   ### full nil判定 Sのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_s_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt s -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ##
#   ### full nil判定 Lのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_l_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt l -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ##
#   #
#  module ablation
  #
   ####
   # attr_rng_type: auto
   # (1)
   # leaderboard-1: 1位：full nil判定 Wのみ, exc_woあり：9/6　1回目投稿分 exact match
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   #
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   #
#   ## slink 新オプション　m_est
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_attr_w_art_a_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   #
#   ## slink 新オプション　r_est
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_r_est__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_attr_w_art_a_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb r_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   #
#   #
#   ### nil判定なし
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_attr_w_art_a_art_a_al_am_bl_w/ --mod s:m:lw -f ab --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6
#   ### 実施済　ここまで
#   #
#   ## filterなし
#   ### blなし
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_art_a_al_am/ --mod s:m:lw -f an --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   ##
#   ## nil判定の対象モジュールのバリエーション　
#   ## full nil判定 M, S, W, L
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_smwl_two_of_pld_02_7_exc_wo_attr_w_art_a_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6 -n_tgt smwl -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   #
#   ### full nil判定 M, S, Wのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_msw_two_of_pld_02_7_exc_wo_attr_w_art_a_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt msw -l_min 0.6 -n_tgt msw -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ##
#   ### full nil判定 S, W, Lのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_swl_two_of_pld_02_7_exc_wo_attr_w_art_a_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt msw -l_min 0.6 -n_tgt swl -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ##
#   ### full nil判定 M, Wのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_mw_two_of_pld_02_7_exc_wo_attr_w_art_a_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6 -n_tgt mw -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ##
#   ### full nil判定 S, Wのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_sw_two_of_pld_02_7_exc_wo_attr_w_art_a_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6 -n_tgt sw -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ##
#   ### full nil判定 L, Wのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_lw_two_of_pld_02_7_exc_wo_attr_w_art_a_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6 -n_tgt lw -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ##
#   ### full nil判定 Mのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_m_two_of_pld_02_7_exc_wo_attr_w_art_a_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6 -n_tgt m -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ##
#   ### full nil判定 Sのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_s_two_of_pld_02_7_exc_wo_attr_w_art_a_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6 -n_tgt s -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ##
#   ### full nil判定 Lのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_l_two_of_pld_02_7_exc_wo_attr_w_art_a_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6 -n_tgt l -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ##
#   #
### module ablation
### 3 module
#### self linkなし (m:lw)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_art_a_al_am_bl_w/ --mod m:lw -f abn --mint e --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ### リンク確率なし (s:m:w)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_art_a_al_am_bl_w/ --mod s:m:w -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ### mintなし (s:lw)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__wlink_rp_l_06_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_art_a_al_am_bl_w/ --mod s:lw -f abn -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ##
#   ## 2 module ここから
#   ## (m:w)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e__wlink_rp_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_art_a_al_am_bl_w/ --mod m:w -f abn --mint e --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ## (lw)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}wlink_rp_l_06_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_art_a_al_am_bl_w/ --mod lw -f abn --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ### (s:w)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__wlink_rp_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_art_a_al_am_bl_w/ --mod s:w -f abn -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   #
#   ## 1 module
#   ## (w)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}wlink_rp_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_art_a_al_am_bl_w/ --mod w -f abn --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   ## (w)(blなし)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}wlink_rp_ncond_w_two_of_pld_02_7_exc_wo_attr_w_art_a_art_a_al_am/ --mod w -f an --wlink rp -ar_tgt w -art a -art a -al am -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works
#   #
#   #
#   ## leaderboard2ベース###################################
#   ## (1)
#   ### leaderboard-2: 1位：full nil判定 Wのみ, exc_woなし: 9/6 2回目投稿分　→　現在のベース
#   #
#   #9/14 exact match
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   #
#   ##9/14
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   #
#   ##slink 新オプション　m_est
#   ##9/14
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   #
#   ##slink 新オプション　r_est
#   ##9/14
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_r_est__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb r_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   #
#   #
#   ### nil判定なし
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_attr_w_art_a_al_am_bl_w/ --mod s:m:lw -f ab --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6
#   ### 実施済　ここまで
#   #
#   ## filterなし
#   ### blなし
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_attr_w_art_a_al_am/ --mod s:m:lw -f an --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   ### attrなし
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_bl_w/ --mod s:m:lw -f bn --mint e -s_min 0.5 -s_prb m_est --wlink rp -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   ##
#   ### module ablation
#   ## 3 module
#   ### self linkなし (m:lw)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ --mod m:lw -f abn --mint e --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   ### リンク確率なし (s:m:w)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_ncond_w_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ --mod s:m:w -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   ### wlinkなし (s:m:l)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__l_06/ --mod s:m:l --mint e -s_min 0.5 -s_prb m_est -l_min 0.6 -f x
#   ### mintなし (s:lw)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__wlink_rp_l_06_ncond_w_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ --mod s:lw -f abn -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   ##
#   ## 2 module ここから
#   ## (m:l)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e__l_06/ --mod m:l --mint e -l_min 0.6 -f x
#   ## (m:w)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e__wlink_rp_ncond_w_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ --mod m:w -f abn --mint e --wlink rp -ar_tgt w -art a -al am -bl_tgt w -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   ## (lw)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}wlink_rp_l_06_ncond_w_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ --mod lw -f abn --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   ### (s:m)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e/ --mod s:m --mint e -s_min 0.5 -s_prb m_est -f x
#   ### (s:w)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__wlink_rp_ncond_w_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ --mod s:w -f abn -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   ### (s:l)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__l_06/ --mod s:l -s_min 0.5 -s_prb m_est -l_min 0.6 -f x
#   #
#   ## 1 module
#   ## (m)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e/ --mod m --mint e -f x
#   ## (l)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}l_06/ --mod l -l_min 0.6 -f x
#   ## (s)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est/ --mod s -s_min 0.5 -s_prb m_est -f x
#
#   ## (w)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}wlink_rp_ncond_w_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ --mod w -f abn --wlink rp -ar_tgt w -art a -al am -bl_tgt w -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#
#
#
#
#   ## (w)(attrなし)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}wlink_rp_ncond_w_two_of_pld_02_7_bl_w/ --mod w -f bn --wlink rp -bl_tgt w -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   ## (w)(blなし)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}wlink_rp_ncond_w_two_of_pld_02_7_attr_w_art_a_al_am/ --mod w -f an --wlink rp -ar_tgt w -art a -al am -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   #
#   #
#   ## (5) 9/7 追加　leaderboard-2(exec_woなし)のnil判定の対象モジュールのバリエーション　
#   ## full nil判定 M, S, W, L
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_smwl_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ -n_tgt smwl -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7  --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6
#   #
#   ### full nil判定 M, S, Wのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_msw_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ -n_tgt msw -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7  --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt msw -l_min 0.6
#   ##
#   ### full nil判定 S, W, Lのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_swl_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ -n_tgt swl -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7  --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt msw -l_min 0.6
#   ##
#   ### full nil判定 M, Wのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_mw_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ -n_tgt mw -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7  --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6
#   ##
#   ### full nil判定 S, Wのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_sw_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ -n_tgt sw -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7  --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6
#   ##
#   ### full nil判定 L, Wのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_lw_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ -n_tgt lw -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7  --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6
#   ##
#   ### full nil判定 Mのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_m_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ -n_tgt m -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7  --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6
#   ##
#   ### full nil判定 Sのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_s_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ -n_tgt s -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7  --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6
#   ##
#   ### full nil判定 Lのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_l_two_of_pld_02_7_attr_w_art_a_al_am_bl_w/ -n_tgt l -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7  --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -al am -bl_tgt w -l_min 0.6
#   ##
#   #
#   ####
#   # attr_rng_type: auto
#   ## leaderboard2ベース###################################
#   ## (1)
#   ### leaderboard-2: 1位：full nil判定 Wのみ, exc_woなし: 9/6 2回目投稿分　→　現在のベース
#   #
#   #9/14 exact match
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_attr_w_art_a_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   #
#   ##9/14
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_attr_w_art_a_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   #
#   ##slink 新オプション　m_est
#   ##9/14
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_attr_w_art_a_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   #
#   ##slink 新オプション　r_est
#   ##9/14
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_r_est__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_attr_w_art_a_art_a_al_am_bl_w/ --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb r_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   #
#   #
#   ### nil判定なし
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_attr_w_art_a_art_a_al_am_bl_w/ --mod s:m:lw -f ab --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6
#   ### 実施済　ここまで
#   #
#   ## filterなし
#   ### blなし
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_attr_w_art_a_art_a_al_am/ --mod s:m:lw -f an --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   #
#   ### module ablation
#   ## 3 module
#   ### self linkなし (m:lw)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_attr_w_art_a_art_a_al_am_bl_w/ --mod m:lw -f abn --mint e --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   ### リンク確率なし (s:m:w)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_ncond_w_two_of_pld_02_7_attr_w_art_a_art_a_al_am_bl_w/ --mod s:m:w -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   ### mintなし (s:lw)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__wlink_rp_l_06_ncond_w_two_of_pld_02_7_attr_w_art_a_art_a_al_am_bl_w/ --mod s:lw -f abn -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   ##
#   ## 2 module ここから
#   ## (m:w)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e__wlink_rp_ncond_w_two_of_pld_02_7_attr_w_art_a_art_a_al_am_bl_w/ --mod m:w -f abn --mint e --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   ## (lw)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}wlink_rp_l_06_ncond_w_two_of_pld_02_7_attr_w_art_a_art_a_al_am_bl_w/ --mod lw -f abn --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   ### (s:w)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__wlink_rp_ncond_w_two_of_pld_02_7_attr_w_art_a_art_a_al_am_bl_w/ --mod s:w -f abn -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   #
#   ## 1 module
#   ## (w)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}wlink_rp_ncond_w_two_of_pld_02_7_attr_w_art_a_art_a_al_am_bl_w/ --mod w -f abn --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   ## (w)(blなし)
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}wlink_rp_ncond_w_two_of_pld_02_7_attr_w_art_a_art_a_al_am/ --mod w -f an --wlink rp -ar_tgt w -art a -art a -al am -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7
#   #
#   #
#   ## (5) 9/7 追加　leaderboard-2(exec_woなし)のnil判定の対象モジュールのバリエーション　
#   ## full nil判定 M, S, W, L
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_smwl_two_of_pld_02_7_attr_w_art_a_art_a_al_am_bl_w/ -n_tgt smwl -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7  --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6
#   #
#   ### full nil判定 M, S, Wのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_msw_two_of_pld_02_7_attr_w_art_a_art_a_al_am_bl_w/ -n_tgt msw -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7  --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt msw -l_min 0.6
#   ##
#   ### full nil判定 S, W, Lのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_swl_two_of_pld_02_7_attr_w_art_a_art_a_al_am_bl_w/ -n_tgt swl -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7  --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt msw -l_min 0.6
#   ##
#   ### full nil判定 M, Wのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_mw_two_of_pld_02_7_attr_w_art_a_art_a_al_am_bl_w/ -n_tgt mw -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7  --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6
#   ##
#   ### full nil判定 S, Wのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_sw_two_of_pld_02_7_attr_w_art_a_art_a_al_am_bl_w/ -n_tgt sw -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7  --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6
#   ##
#   ### full nil判定 L, Wのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_lw_two_of_pld_02_7_attr_w_art_a_art_a_al_am_bl_w/ -n_tgt lw -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7  --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6
#   ##
#   ### full nil判定 Mのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_m_two_of_pld_02_7_attr_w_art_a_art_a_al_am_bl_w/ -n_tgt m -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7  --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6
#   ##
#   ### full nil判定 Sのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_s_two_of_pld_02_7_attr_w_art_a_art_a_al_am_bl_w/ -n_tgt s -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7  --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6
#   ##
#   ### full nil判定 Lのみ
#python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_m_est__mint_e__wlink_rp_l_06_ncond_l_two_of_pld_02_7_attr_w_art_a_art_a_al_am_bl_w/ -n_tgt l -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7  --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art a -art a -al am -bl_tgt w -l_min 0.6
#   ##











# training
# full
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_exc_wo_attr_w_al_am_bl_w/ -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w -l_min 0.6
# exc_woなし
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_attr_w_al_am_bl_w/ -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 --mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w -l_min 0.6
# nil判定なし
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_l_06_attr_w_al_am_bl_w/ --mod s:m:lw -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w -l_min 0.6
# blなし
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_exc_wo_attr_w_al_am/ -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works --mod s:m:lw -f an --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -l_min 0.6
# attrなし
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_exc_wo_bl_w/ -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works --mod s:m:lw -f bn --mint e -s_min 0.5 -s_prb mid --wlink rp -bl_tgt w -l_min 0.6
# module ablation
# self linkなし
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mid__mint_e__wlink_rp_l_06_ncond_w_two_of_pld_02_7_exc_wo_attr_w_al_am_bl_w/ -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works --mod m:lw -f abn --mint e --wlink rp -ar_tgt w -al am -bl_tgt w -l_min 0.6
# リンク確率なし
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_ncond_w_two_of_pld_02_7_exc_wo_attr_w_al_am_bl_w/ -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works --mod s:m:w -f abn --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w
# wlinkなし（attrもなし)
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_mid__mint_e__l_06_ncond_w_two_of_pld_02_7_exc_wo_bl_w/ -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works --mod s:m:l -f abn --mint e -s_min 0.5 -s_prb mid -l_min 0.6
# mintなし
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}slink_05_mid__wlink_rp_l_06_ncond_w_two_of_pld_02_7_exc_wo_attr_w_al_am_bl_w/ -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works --mod s:lw -f abn -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w -l_min 0.6



# 被リンク
# 20220827
# 20220829
# full
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_ncond_w_two_of_pld_02_7_exc_wo_incl_m_imax1_o/ -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 -n_exc person_works --mod m -f in --mint e -i_tgt m -i_max 1 -i_type o
# exc_woなし
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_ncond_w_two_of_pld_02_7_incl_m_imax1_o/ -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.2 -ld_min 7 --mod m -f in --mint e -i_tgt m -i_max 1 -i_type o
# 20220830
# n_maxなし
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_ncond_w_two_of_pld_7_exc_wo_incl_m_imax1_o/ -n_tgt w -n_cond two_of_prob_len_desc -ld_min 7 -n_exc person_works --mod m -f in --mint e -i_tgt m -i_max 1 -i_type o
# nil判定なし
# python $script $common_data_dir $tmp_data_dir $in_dir $sample_gold_dir $sample_input_dir ${out_dir_base}mint_e_incl_m_imax1_o/ --mod m -f in --mint e -i_tgt m -i_max 1 -i_type o


## 実験 #############################
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_09_fcar_09/ --mod w -f n --wlink l -wl_bca r -wl_bca_ratio 0.9 -wl_fca r -wl_fca_ratio 0.9
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_08_fcar_08/ --mod w -f n --wlink l -wl_bca r -wl_bca_ratio 0.8 -wl_fca r -wl_fca_ratio 0.8
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_07_fcar_07/ --mod w -f n --wlink l -wl_bca r -wl_bca_ratio 0.7 -wl_fca r -wl_fca_ratio 0.7
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_06_fcar_06/ --mod w -f n --wlink l -wl_bca r -wl_bca_ratio 0.6 -wl_fca r -wl_fca_ratio 0.6
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_05_fcar_05/ --mod w -f n --wlink l -wl_bca r -wl_bca_ratio 0.5 -wl_fca r -wl_fca_ratio 0.5
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_04_fcar_04/ --mod w -f n --wlink l -wl_bca r -wl_bca_ratio 0.4 -wl_fca r -wl_fca_ratio 0.4
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_03_fcar_03/ --mod w -f n --wlink l -wl_bca r -wl_bca_ratio 0.3 -wl_fca r -wl_fca_ratio 0.3
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_02_fcar_02/ --mod w -f n --wlink l -wl_bca r -wl_bca_ratio 0.2 -wl_fca r -wl_fca_ratio 0.2
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_01_fcar_01/ --mod w -f n --wlink l -wl_bca r -wl_bca_ratio 0.1 -wl_fca r -wl_fca_ratio 0.1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_09_fcar_01/ --mod w -f n --wlink l -wl_bca r -wl_bca_ratio 0.9 -wl_fca r -wl_fca_ratio 0.9
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_08_fcar_01/ --mod w -f n --wlink l -wl_bca r -wl_bca_ratio 0.8 -wl_fca r -wl_fca_ratio 0.8
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_07_fcar_01/ --mod w -f n --wlink l -wl_bca r -wl_bca_ratio 0.7 -wl_fca r -wl_fca_ratio 0.7
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_06_fcar_01/ --mod w -f n --wlink l -wl_bca r -wl_bca_ratio 0.6 -wl_fca r -wl_fca_ratio 0.6
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_05_fcar_01/ --mod w -f n --wlink l -wl_bca r -wl_bca_ratio 0.5 -wl_fca r -wl_fca_ratio 0.5
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_04_fcar_01/ --mod w -f n --wlink l -wl_bca r -wl_bca_ratio 0.4 -wl_fca r -wl_fca_ratio 0.4
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_03_fcar_01/ --mod w -f n --wlink l -wl_bca r -wl_bca_ratio 0.3 -wl_fca r -wl_fca_ratio 0.3
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bcar_02_fcar_01/ --mod w -f n --wlink l -wl_bca r -wl_bca_ratio 0.2 -wl_fca r -wl_fca_ratio 0.2
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_09_fcar_09/ --mod w -f n --wlink rl -wl_bca r -wl_bca_ratio 0.9 -wl_fca r -wl_fca_ratio 0.9
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_08_fcar_08/ --mod w -f n --wlink rl -wl_bca r -wl_bca_ratio 0.8 -wl_fca r -wl_fca_ratio 0.8
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_07_fcar_07/ --mod w -f n --wlink rl -wl_bca r -wl_bca_ratio 0.7 -wl_fca r -wl_fca_ratio 0.7
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_06_fcar_06/ --mod w -f n --wlink rl -wl_bca r -wl_bca_ratio 0.6 -wl_fca r -wl_fca_ratio 0.6
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_05_fcar_05/ --mod w -f n --wlink rl -wl_bca r -wl_bca_ratio 0.5 -wl_fca r -wl_fca_ratio 0.5
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_04_fcar_04/ --mod w -f n --wlink rl -wl_bca r -wl_bca_ratio 0.4 -wl_fca r -wl_fca_ratio 0.4
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_03_fcar_03/ --mod w -f n --wlink rl -wl_bca r -wl_bca_ratio 0.3 -wl_fca r -wl_fca_ratio 0.3
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_02_fcar_02/ --mod w -f n --wlink rl -wl_bca r -wl_bca_ratio 0.2 -wl_fca r -wl_fca_ratio 0.2
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_01_fcar_01/ --mod w -f n --wlink rl -wl_bca r -wl_bca_ratio 0.1 -wl_fca r -wl_fca_ratio 0.1
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_09_fcar_01/ --mod w -f n --wlink rl -wl_bca r -wl_bca_ratio 0.9 -wl_fca r -wl_fca_ratio 0.9
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_08_fcar_01/ --mod w -f n --wlink rl -wl_bca r -wl_bca_ratio 0.8 -wl_fca r -wl_fca_ratio 0.8
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_07_fcar_01/ --mod w -f n --wlink rl -wl_bca r -wl_bca_ratio 0.7 -wl_fca r -wl_fca_ratio 0.7
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_06_fcar_01/ --mod w -f n --wlink rl -wl_bca r -wl_bca_ratio 0.6 -wl_fca r -wl_fca_ratio 0.6
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_05_fcar_01/ --mod w -f n --wlink rl -wl_bca r -wl_bca_ratio 0.5 -wl_fca r -wl_fca_ratio 0.5
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_04_fcar_01/ --mod w -f n --wlink rl -wl_bca r -wl_bca_ratio 0.4 -wl_fca r -wl_fca_ratio 0.4
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_03_fcar_01/ --mod w -f n --wlink rl -wl_bca r -wl_bca_ratio 0.3 -wl_fca r -wl_fca_ratio 0.3
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_02_fcar_01/ --mod w -f n --wlink rl -wl_bca r -wl_bca_ratio 0.2 -wl_fca r -wl_fca_ratio 0.2
#
#
#
#### 単一モジュールのtop
##### 5モジュール
#### 5module
#### 5module: F1 mint_e_tinm_p_09_slink_05_wlink_frp_l_06
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_09_slink_05_wlink_frp_l_06/ --mod mtswl -f n --mint e --tinm p -t_min 0.9 -s_min 0.5 --wlink frp -l_min 0.6
#### 5module: prec mint_e_tinm_e_slink_10_wlink_p_l_09
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_slink_10_wlink_p_l_09/ --mod mtswl -f n --mint e --tinm e -s_min 1.0 --wlink p -l_min 0.9
#### 5module: recall mint_e_tinm_p_02_slink_05_wlink_frp_l_06
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_02_slink_05_wlink_frp_l_06/ --mod mtswl -f n --mint e --tinm p -t_min 0.2 -s_min 0.5 --wlink frp -l_min 0.6
###
#### 4モジュール
####
#### 4module: F1 mint_e_tinm_p_09_slink_05_wlink_frp_l_06
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_09_slink_05_wlink_frp/ --mod mtsw -f n --mint e --tinm p -t_min 0.9 -s_min 0.5 --wlink frp
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_09_slink_05_l_06/ --mod mtsl -f n --mint e --tinm p -t_min 0.9 -s_min 0.5 -l_min 0.6
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_09_wlink_frp_l_06/ --mod mtwl -f n --mint e --tinm p -t_min 0.9 --wlink frp -l_min 0.6
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_frp_l_06/ --mod mswl -f n --mint e -s_min 0.5 --wlink frp -l_min 0.6
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_09_slink_05_wlink_frp_l_06/ --mod tswl -f n --tinm p -t_min 0.9 -s_min 0.5 --wlink frp -l_min 0.6
###
#### 4module: prec mint_e_tinm_e_slink_10_wlink_p_l_09
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_slink_10_wlink_p/ --mod mtsw -f n --mint e --tinm e -s_min 1.0 --wlink p
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_slink_10_l_09/ --mod mtsl -f n --mint e --tinm e -s_min 1.0 -l_min 0.9
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_wlink_p_l_09/ --mod mtwl -f n --mint e --tinm e --wlink p -l_min 0.9
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_10_wlink_p_l_09/ --mod mswl -f n --mint e -s_min 1.0 --wlink p -l_min 0.9
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_slink_10_wlink_p_l_09/ --mod tswl -f n --tinm e -s_min 1.0 --wlink p -l_min 0.9
###
#### 4module: recall mint_e_tinm_p_02_slink_05_wlink_frp_l_06
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_02_slink_05_wlink_frp/ --mod mtsw -f n --mint e --tinm p -t_min 0.2 -s_min 0.5 --wlink frp
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_02_slink_05_l_06/ --mod mtsl -f n --mint e --tinm p -t_min 0.2 -s_min 0.5 -l_min 0.6
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_02_wlink_frp_l_06/ --mod mtwl -f n --mint e --tinm p -t_min 0.2 --wlink frp -l_min 0.6
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_frp_l_06/ --mod mswl -f n --mint e -s_min 0.5 --wlink frp -l_min 0.6
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_02_slink_05_wlink_frp_l_06/ --mod tswl -f n --tinm p -t_min 0.2 -s_min 0.5 --wlink frp -l_min 0.6
###
#### 3module
#### 3module:F1 mint_e_tinm_p_09_slink_05_wlink_frp_l_06
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_09_slink_05/ --mod mts -f n --mint e --tinm p -t_min 0.9 -s_min 0.5
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_09_wlink_frp/ --mod mtw -f n --mint e --tinm p -t_min 0.9 --wlink frp
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_09_l_06/ --mod mtl -f n --mint e --tinm p -t_min 0.9 -l_min 0.6
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_frp/ --mod msw -f n --mint e --wlink frp -s_min 0.5
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_l_06/ --mod msl -f n --mint e -s_min 0.5 -l_min 0.6
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_wlink_frp_l_06/ --mod mwl -f n --mint e --wlink frp -l_min 0.6
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_09_slink_05_wlink_frp/ --mod tsw -f n --tinm p -t_min 0.9 -s_min 0.5 --wlink frp
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_09_slink_05_l_06/ --mod tsl -f n --tinm p -t_min 0.9 -s_min 0.5 -l_min 0.6
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_wlink_frp_l_06/ --mod swl -f n -s_min 0.5 --wlink frp -l_min 0.6
###
#### 3module: prec mint_e_tinm_e_slink_10_wlink_p_l_09
####done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_slink_10/ --mod mts -f n --mint e --tinm e -s_min 1.0
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_wlink_p/ --mod mtw -f n --mint e --tinm e --wlink p
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_l_09/ --mod mtl -f n --mint e --tinm e -l_min 0.9
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_10_wlink_p/ --mod msw -f n --mint e -s_min 1.0 --wlink p
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_10_l_09/ --mod msl -f n --mint e -s_min 1.0 -l_min 0.9
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_wlink_p_l_09/ --mod mwl -f n --mint e --wlink p -l_min 0.9
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_slink_10_wlink_p/ --mod tsw -f n --tinm e -s_min 1.0 --wlink p
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_slink_10_l_09/ --mod tsl -f n --tinm e -s_min 1.0 -l_min 0.9
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_10_wlink_p_l_09/ --mod swl -f n -s_min 1.0 --wlink p -l_min 0.9
###
#### 3module: recall mint_e_tinm_p_02_slink_05_wlink_frp_l_06
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_02_slink_05/ --mod mts -f n --mint e --tinm p -t_min 0.2 -s_min 0.5
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_02_wlink_frp/ --mod mtw -f n --mint e --tinm p -t_min 0.2 --wlink frp
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_02_l_06/ --mod mtl -f n --mint e --tinm p -t_min 0.2 -l_min 0.6
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_frp/ --mod msw -f n --mint e -s_min 0.5 --wlink frp
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_l_06/ --mod msl -f n --mint e -s_min 0.5 -l_min 0.6
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_wlink_frp_l_06/ --mod mwl -f n --mint e --wlink frp -l_min 0.6
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_02_slink_05_wlink_frp/ --mod tsw -f n --tinm p -t_min 0.2 -s_min 0.5 --wlink frp
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_02_slink_05_l_06/ --mod tsl -f n --tinm p -t_min 0.2 -s_min 0.5 -l_min 0.6
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_wlink_frp_l_06/ --mod swl -f n -s_min 0.5 --wlink frp -l_min 0.6
###
####2module
#### 2module: F1 mint_e_tinm_p_09_slink_05_wlink_frp_l_06
####done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_09/ --mod mt -f n --mint e --tinm p -t_min 0.9
####done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05/ --mod ms -f n --mint e -s_min 0.5
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_wlink_frp/ --mod mw -f n --mint e --wlink frp
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_l_06/ --mod ml -f n --mint e -l_min 0.6
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_09_slink_05/ --mod ts -f n --tinm p -t_min 0.9 -s_min 0.5
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_09_wlink_frp/ --mod tw -f n --tinm p -t_min 0.9 --wlink frp
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_09_l_06/ --mod tl -f n --tinm p -t_min 0.9 -l_min 0.6
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_wlink_frp/ --mod sw -f n -s_min 0.5 --wlink frp
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_l_06/ --mod sl -f n -s_min 0.5 -l_min 0.6
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp_l_06/ --mod wl -f n --wlink frp -l_min 0.6
###
#### 2module: prec mint_e_tinm_e_slink_10_wlink_p_l_09
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e/ --mod mt -f n --mint e --tinm e
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_10/ --mod ms -f n --mint e -s_min 1.0
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_wlink_p/ --mod mw -f n --mint e --wlink p
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_l_09/ --mod ml -f n --mint e -l_min 0.9
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_slink_10/ --mod ts -f n --tinm e -s_min 1.0
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_wlink_p/ --mod tw -f n --tinm e --wlink p
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_l_09/ --mod tl -f n --tinm e -l_min 0.9
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_10_wlink_p/ --mod sw -f n -s_min 1.0 --wlink p
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_10_l_09/ --mod sl -f n -s_min 1.0 -l_min 0.9
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p_l_09/ --mod wl -f n --wlink p -l_min 0.9
###
#### 2module: recall mint_e_tinm_p_02_slink_05_wlink_frp_l_06
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_02/ --mod mt -f n --mint e --tinm p -t_min 0.2
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05/ --mod ms -f n --mint e -s_min 0.5
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_wlink_frp/ --mod mw -f n --mint e --wlink frp
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_l_06/ --mod ml -f n --mint e -l_min 0.6
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_02_slink_05/ --mod ts -f n --tinm p -t_min 0.2 -s_min 0.5
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_02_wlink_frp/ --mod tw -f n --tinm p -t_min 0.2 --wlink frp
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_02_l_06/ --mod tl -f n --tinm p -t_min 0.2 -l_min 0.6
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_wlink_frp/ --mod sw -f n -s_min 0.5 --wlink frp
### python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_l_06/ --mod sl -f n -s_min 0.5 -l_min 0.6
###done#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp_l_06/ --mod wl -f n --wlink frp -l_min 0.6
##
### 1module: F1 mint_e_tinm_p_09_slink_05_wlink_frp_l_06
### 1module: precision mint_e_tinm_e_slink_10_wlink_p_l_09
### 1module: recall mint_e_tinm_p_02_slink_05_wlink_frp_l_06
### 1moduleのバリエーション
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e/ --mod m -f n --mint e
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim/ --mod m -f n --mint e -tmm trim
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e/ --mod m -f n --mint
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_01/ --mod m -f n --mint e -m_min 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_02/ --mod m -f n --mint e -m_min 0.2
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_03/ --mod m -f n --mint e -m_min 0.3
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_04/ --mod m -f n --mint e -m_min 0.4
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_06/ --mod m -f n --mint e -m_min 0.6
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_07/ --mod m -f n --mint e -m_min 0.7
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_08/ --mod m -f n --mint e -m_min 0.8
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_09/ --mod m -f n --mint e -m_min 0.9
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_10/ --mod m -f n --mint e -m_min 1.0
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim/ --mod m -f n --mint e -tmm trim
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_01/ --mod m -f n --mint e -tmm trim -m_min 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_02/ --mod m -f n --mint e -tmm trim -m_min 0.2
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_03/ --mod m -f n --mint e -tmm trim -m_min 0.3
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_04/ --mod m -f n --mint e -tmm trim -m_min 0.4
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_05/ --mod m -f n --mint e -tmm trim -m_min 0.5
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_06/ --mod m -f n --mint e -tmm trim -m_min 0.6
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_07/ --mod m -f n --mint e -tmm trim -m_min 0.7
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_08/ --mod m -f n --mint e -tmm trim -m_min 0.8
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_09/ --mod m -f n --mint e -tmm trim -m_min 0.9
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_10/ --mod m -f n --mint e -tmm trim -m_min 1.0
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_01/ --mod s -f n -s_min 0.1
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
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05/ --mod s -f n -s_min 0.5
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid/ --mod s -f n -s_min 0.5 -s_prb mid
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_raw/ --mod s -f n -s_min 0.5 -s_prb raw
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
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e/ --mod t -f n --tinm e
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_trim/ --mod t -f n --tinm p -tmt trim
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p/ --mod t -f n --tinm p
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_01/ --mod t -f n --tinm p -t_min 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_02/ --mod t -f n --tinm p -t_min 0.2
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_03/ --mod t -f n --tinm p -t_min 0.3
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_04/ --mod t -f n --tinm p -t_min 0.4
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_05/ --mod t -f n --tinm p -t_min 0.5
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_06/ --mod t -f n --tinm p -t_min 0.6
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_07/ --mod t -f n --tinm p -t_min 0.7
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_08/ --mod t -f n --tinm p -t_min 0.8
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_09/ --mod t -f n --tinm p -t_min 0.9
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_10/ --mod t -f n --tinm p -t_min 1.0
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim/ --mod t -f n --tinm p -tmt trim
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_01/ --mod t -f n --tinm p -tmt trim -t_min 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_02/ --mod t -f n --tinm p -tmt trim -t_min 0.2
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_03/ --mod t -f n --tinm p -tmt trim -t_min 0.3
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_04/ --mod t -f n --tinm p -tmt trim -t_min 0.4
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_05/ --mod t -f n --tinm p -tmt trim -t_min 0.5
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_06/ --mod t -f n --tinm p -tmt trim -t_min 0.6
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_07/ --mod t -f n --tinm p -tmt trim -t_min 0.7
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_08/ --mod t -f n --tinm p -tmt trim -t_min 0.8
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_09/ --mod t -f n --tinm p -tmt trim -t_min 0.9
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim_10/ --mod t -f n --tinm p -tmt trim -t_min 1.0
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_f/ --mod w -f n --wlink f
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
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fl/ --mod w -f n --wlink fl
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fp/ --mod w -f n --wlink fp
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_fr/ --mod w -f n --wlink fr
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frl/ --mod w -f n --wlink frl
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp/ --mod w -f n --wlink frp
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl/ --mod w -f n --wlink frpl
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l/ --mod w -f n --wlink l
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bmax_5/ --mod w -f n --wlink l --wl_bmax 5
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bmax_20/ --mod w -f n --wlink l --wl_bmax 20
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bmax_60_fmax_60/ --mod w -f n --wlink l --wl_bmax 60 --wl_fmax 60
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_bmax_100_fmax_100/ --mod w -f n --wlink l --wl_bmax 100 --wl_fmax 100
##
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls_01/ --mod w -f n --wlink l -wls 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls_02/ --mod w -f n --wlink l -wls 0.2
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls_03/ --mod w -f n --wlink l -wls 0.3
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls_04/ --mod w -f n --wlink l -wls 0.4
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls_05/ --mod w -f n --wlink l -wls 0.5
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls_06/ --mod w -f n --wlink l -wls 0.6
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls_07/ --mod w -f n --wlink l -wls 0.7
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls_08/ --mod w -f n --wlink l -wls 0.8
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls_09/ --mod w -f n --wlink l -wls 0.9
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wls_10/ --mod w -f n --wlink l -wls 1.0
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wl_bca_f/ --mod w -f n --wlink l -wl_bca f -wl_fca f
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wl_fca_f/ --mod w -f n --wlink l -wl_bca r -wl_bca_ratio 0.1 -wl_fca f
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlf_01/ --mod w -f n --wlink l -wlf 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlf_02/ --mod w -f n --wlink l -wlf 0.2
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlf_03/ --mod w -f n --wlink l -wlf 0.3
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlf_04/ --mod w -f n --wlink l -wlf 0.4
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlf_05/ --mod w -f n --wlink l -wlf 0.5
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlf_06/ --mod w -f n --wlink l -wlf 0.6
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlf_07/ --mod w -f n --wlink l -wlf 0.7
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlf_08/ --mod w -f n --wlink l -wlf 0.8
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlf_09/ --mod w -f n --wlink l -wlf 0.9
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wl_bmax10_fmax2/ --mod w -f n --wlink l -wl_bmax 10 -wl_fmax 2
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlb_01/ --mod w -f n --wlink l -wlb 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlb_02/ --mod w -f n --wlink l -wlb 0.2
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlb_03/ --mod w -f n --wlink l -wlb 0.3
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlb_04/ --mod w -f n --wlink l -wlb 0.4
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlb_05/ --mod w -f n --wlink l -wlb 0.5
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlb_06/ --mod w -f n --wlink l -wlb 0.6
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlb_07/ --mod w -f n --wlink l -wlb 0.7
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlb_08/ --mod w -f n --wlink l -wlb 0.8
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlb_09/ --mod w -f n --wlink l -wlb 0.9
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_l_wlb_10/ --mod w -f n --wlink l -wlb 1.0
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_m/ --mod w -f n --wlink m
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_ml/ --mod w -f n --wlink ml
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mp/ --mod w -f n --wlink mp
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_mpl/ --mod w -f n --wlink mpl
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p/ --mod w -f n --wlink p
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p_01/ --mod w -f n --wlink p -wp 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p_02/ --mod w -f n --wlink p -wp 0.2
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p_03/ --mod w -f n --wlink p -wp 0.3
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p_04/ --mod w -f n --wlink p -wp 0.4
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p_05/ --mod w -f n --wlink p -wp 0.5
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p_06/ --mod w -f n --wlink p -wp 0.6
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p_07/ --mod w -f n --wlink p -wp 0.7
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p_08/ --mod w -f n --wlink p -wp 0.8
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p_09/ --mod w -f n --wlink p -wp 0.9
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_p_10/ --mod w -f n --wlink p -wp 1.0
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_pl/ --mod w -f n --wlink pl
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r/ --mod w -f n --wlink r
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_01/ --mod w -f n --wlink r -wr 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_02/ --mod w -f n --wlink r -wr 0.2
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_03/ --mod w -f n --wlink r -wr 0.3
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_04/ --mod w -f n --wlink r -wr 0.4
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_05/ --mod w -f n --wlink r -wr 0.5
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_06/ --mod w -f n --wlink r -wr 0.6
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_07/ --mod w -f n --wlink r -wr 0.7
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_08/ --mod w -f n --wlink r -wr 0.8
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_09/ --mod w -f n --wlink r -wr 0.9
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_r_10/ --mod w -f n --wlink r -wr 1.0
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl/ --mod w -f n --wlink rl
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp/ --mod w -f n --wlink rp
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rpl/ --mod w -f n --wlink rpl
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_01/ --mod l -f n -l_min 0.1
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_02/ --mod l -f n -l_min 0.2
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_03/ --mod l -f n -l_min 0.3
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_04/ --mod l -f n -l_min 0.4
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_05/ --mod l -f n -l_min 0.5
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_06/ --mod l -f n -l_min 0.6
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_07/ --mod l -f n -l_min 0.7
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_08/ --mod l -f n -l_min 0.8
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_09/ --mod l -f n -l_min 0.9
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l_10/ --mod l -f n -l_min 1.0
##
##
### FINAL ##########################
#######
###ここから上のコメントを外す
##
#### AIPRB_SMW
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_frpl_bmax_5_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frpl --wl_bmax 5 -ar_tgt w -al am -bl_tgt w
##
##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_frpl_bmax_60_fmax_60_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frpl --wl_bmax 60 --wl_fmax 60 -ar_tgt w -al am -bl_tgt w
##
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_frp_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
#
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rl_bcar_01_fcar_01_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink rl -wl_bca r -wl_bca_ratio 0.1 -wl_fca r -wl_fca_ratio 0.1 -ar_tgt w -al am -bl_tgt w
##
####
##### AIPRB_WSM
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl_bmax_5__slink__mint_e_attr_w/ --mod w:s:m -f a --mint e --wlink frpl --wl_bmax 5 -ar_tgt w
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl__slink__mint_e_attr_w/ --mod w:s:m -f a --mint e --wlink frpl -ar_tgt w
#
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rl_bcar_01_fcar_01__slink__mint_e_attr_w/ --mod w:s:m -f a --mint e --wlink rl -wl_bca r -wl_bca_ratio 0.1 -wl_fca r -wl_fca_ratio 0.1 -ar_tgt w
##
##
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frpl_bmax_60_fmax_60__slink__mint_e_attr_w/ --mod w:s:m -f a --mint e --wlink frpl --wl_bmax 60 --wl_fmax 60 -ar_tgt w
##
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink__mint_e_attr_w/ --mod w:s:m -f a --mint e --wlink frp -ar_tgt w
###
#### AIPCB_CBI
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_incl_m_imax1_o/ --mod m -f i --mint e -i_tgt m -i_max 1 -i_type o
##
#####
###サンプルデータで良いもの (lが入っているため）###############
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_frp_l_06_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink frp -l_min 0.6 -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_frp_l_06_attr_w_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink frp -l_min 0.6 -ar_tgt w -bl_tgt w -i_tgt w -i_max 5 -i_type f
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_rp_l_06_attr_w_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink rp -l_min 0.6 -ar_tgt w -bl_tgt w -i_tgt w -i_max 5 -i_type f
##
#############################################################################
### フィルタあり imax3_f, imax3_aはskip 未調査
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_incl_m_imax1_o/ --mod m -f i --mint e -i_tgt m -i_max 1 -i_type o
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_incl_m_imax1_f/ --mod m -f i --mint e -i_tgt m -i_max 1 -i_type f
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_incl_m_imax1_a/ --mod m -f i --mint e -i_tgt m -i_max 1 -i_type a
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_incl_m_imax3_o/ --mod m -f i --mint e -i_tgt m -i_max 3 -i_type o
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_incl_m_imax3_f/ --mod m -f i --mint e -i_tgt m -i_max 3 -i_type f
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_incl_m_imax3_a/ --mod m -f i --mint e -i_tgt m -i_max 3 -i_type a
##
#############################################################################
##
###
###
######Sep29AM- (ただしinclはSep29PM-)
######msw
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_frp_attr_w_al_am_bl_w_incl_w_imax5_io/ --mod msw -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type o
####
######mswl
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_frp_l_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_frp_l_attr_w_al_am_bl_w_incl_w_imax5_io/ --mod mswl -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type o
####
######mtsw
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink_05_wlink_frp_attr_tw_al_am_bl_tw/ --mod mtsw -f ab --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -ar_tgt tw -al am -bl_tgt tw
####
######mtswl
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink_05_wlink_frp_l_attr_tw_al_am_bl_tw/ --mod mtswl -f ab --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -ar_tgt tw -al am -bl_tgt tw
####
######smtw
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05__mint_e__tinm_p_wlink_frp_attr_w_al_am_bl_w/ --mod s:m:tw -f ab --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mint_e_l__tinm_p_wlink_frp_attr_w_al_am_bl_w/ --mod msl:tw -f ab --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
####
######smw **
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05__mint_e__wlink_frp_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05__mint_e__wlink_frp_l_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_frp_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp__attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w
####
####
####
######mslw
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mint_e_l__wlink_frp_tinm_p_attr_w_al_am_bl_w/ --mod msl:w:t -f ab --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
####
######smtw
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e_wlink_rp__tinm_e_trim_attr_tw_al_am_bl_tw/ --mod s:mw:t -f ab --mint e --tinm e -tmt trim -s_min 0.5 -s_prb mid --wlink rp -ar_tgt tw -al am -bl_tgt tw
####
######smw
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_frp_attr_w_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -bl_tgt w
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_frp_attr_w_bl_mw/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -bl_tgt mw
####
####
######swm **
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05__wlink_frp__mint_e__attr_w_al_am_bl_w/ --mod s:w:m -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__wlink_rp__mint_e_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod s:w:m -f abi --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__wlink_frp__mint_e__attr_w_al_am_bl_w/ --mod s:w:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__wlink_rp__mint_e__attr_w_al_am_bl_w/ --mod s:w:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__wlink_frp__mint_e_attr_w_bl_w/ --mod s:w:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -bl_tgt w
####
####
######wsm ***
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_05__mint_e__attr_w_al_am_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_05_mid__mint_e_attr_w_al_am_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
######best
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink_05_mid__mint_e_attr_w_al_am_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink_05_mid__mint_e_attr_w_al_am_bl_w_incl_w_imax5_if/ --mod w:s:m -f abi --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink_05_mid__mint_e_attr_w_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w
####
######wms *
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__mint_e__slink_05_mid_attr_w_al_am_bl_w/ --mod w:m:s -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__mint_e_mid__slink_05_attr_w_al_am_bl_w/ --mod w:m:s -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__mint_e_slink_05_mid__tinm_e_trim_attr_tw_al_am_bl_tw/ --mod w:ms:t -f ab --mint e --tinm e -tmt trim -s_min 0.5 -s_prb mid --wlink rp -ar_tgt tw -al am -bl_tgt tw
####
######wmst
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__mint_e_slink_05_mid__tinm_e_trim_attr_tw_al_am_bl_tw/ --mod w:ms:t -f ab --mint e --tinm e -tmt trim -s_min 0.5 -s_prb mid --wlink frp -ar_tgt tw -al am -bl_tgt tw
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__mint_e_slink_05_mid__tinm_e_trim_attr_w_al_am_bl_t/ --mod w:ms:t -f ab --mint e --tinm e -tmt trim -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt t
####
####
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_frp_modw_1_05_03_02_01_attr_w_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -bl_tgt w
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_modw_1_05_03_02_01_attr_w_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -bl_tgt w
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_frp_modw_1_05_03_02_01_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am -bl_tgt w
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e__wlink_rp_modw_1_05_03_02_01_attr_w_al_am_bl_w/ --mod s:m:w -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am -bl_tgt w
######
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_05_mid__mint_e_modw_1_05_03_02_01_attr_w/ --mod w:s:m -f a --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_05_mid__mint_e_modw_1_05_03_02_01_attr_w_al_am/ --mod w:s:m -f a --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_05_mid__mint_e_modw_1_05_03_02_01_attr_w_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -bl_tgt w
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_05_mid__mint_e_modw_1_05_03_02_01_attr_w_al_am_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am -bl_tgt w
######
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink_05_mid__mint_e_modw_1_05_03_02_01_attr_w/ --mod w:s:m -f a --mint e -s_min 0.5 -s_prb mid --wlink rp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink_05_mid__mint_e_modw_1_05_03_02_01_attr_w_al_am/ --mod w:s:m -f a --mint e -s_min 0.5 -s_prb mid --wlink rp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink_05_mid__mint_e_modw_1_05_03_02_01_attr_w_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -bl_tgt w
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_rp__slink_05_mid__mint_e_modw_1_05_03_02_01_attr_w_al_am_bl_w/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am -bl_tgt w
####
####
####
########final cand
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__wlink_frp__mint_e_modw_1_05_03_02_01_attr_w_al_am_bl_w/ --mod s:w:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -al am -bl_tgt w
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_05_mid__mint_e_modw_1_05_03_02_01/ --mod w:s:m -f n --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1
######
########s_prbが抜けていた
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_05_mid__mint_e_modw_1_05_03_02_01_attr_w_bl_mw/ --mod w:s:m -f ab --mint e -s_min 0.5 -s_prb mid --wlink frp --mod_w 1.0:0.5:0.3:0.2:0.1 -ar_tgt w -bl_tgt mw
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_mid__mint_e_attr_w/ --mod w:s:m -f a --mint e --wlink frp -s_prb mid -ar_tgt w
######
######
######${eval_script}
########baseline
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_incl_w_imax_5_if/ --mod m -f i --mint e -i_tgt m -i_max 5 -i_type f
######${eval_script}
####
########################
####frp
####latestSep29##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_frp_attr_w_al_am_bl_w/ --mod msw -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
####latestSep29##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_frp_l_attr_w_al_am_bl_w/ --mod mswl -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
####
####here
####retry
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_frp_attr_w_al_am_bl_w_incl_w_imax_5_if/ --mod msw -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
####
####
####priority
####
####
####
####swm
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__wlink_frp__mint_e_attr_w_al_am_bl_w_incl_w_imax_5_if/ --mod s:w:m -f abi --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
####
####wsm
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}wlink_frp__slink_05_mid__mint_e_attr_w_al_am_bl_w_incl_w_imax_5_if/ --mod w:s:m -f abi --mint e -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
####
####smwt
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mid__mint_e_wlink_frp__tinm_e_trim_attr_w_al_am_bl_w/ --mod s:mw:t -f ab --mint e --tinm e -tmt trim -s_min 0.5 -s_prb mid --wlink frp -ar_tgt w -al am -bl_tgt w
####
####
####${eval_script}
############
####till here
############
####
####
####
####latestSep29##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_frp_attr_w_bl_w/ --mod msw -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt w
####latestSep29##python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_frp_l_attr_w_bl_w/ --mod mswl -f ab --mint e -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt w
####
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_frp_attr_w_bl_w_incl_w_imax_5_if/ --mod msw -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt w -i_tgt w -i_max 5 -i_type f
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_frp_l_attr_w_bl_w_incl_w_imax_5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt w -i_tgt w -i_max 5 -i_type f
####
######rp
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_mid_wlink_rp_attr_w_al_am_bl_w/ --mod msw -f ab --mint e -s_min 0.5 -s_prb mid --wlink rp -ar_tgt w -al am -bl_tgt w
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_rp_attr_w_al_am_bl_w/ --mod msw -f ab --mint e -s_min 0.5 --wlink rp -ar_tgt w -al am -bl_tgt w
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_rp_l_attr_w_al_am_bl_w/ --mod mswl -f ab --mint e -s_min 0.5 --wlink rp -ar_tgt w -al am -bl_tgt w
######
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_rp_attr_w_al_am_bl_w_incl_w_imax_5_if/ --mod msw -f abi --mint e -s_min 0.5 --wlink rp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_rp_l_attr_w_al_am_bl_w_incl_w_imax_5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink rp -ar_tgt w -al am -bl_tgt w -i_tgt w -i_max 5 -i_type f
######
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_rp_attr_w_bl_w/ --mod msw -f ab --mint e -s_min 0.5 --wlink rp -ar_tgt w -bl_tgt w
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_rp_l_attr_w_bl_w/ --mod mswl -f ab --mint e -s_min 0.5 --wlink rp -ar_tgt w -bl_tgt w
######
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_rp_attr_w_bl_w_incl_w_imax_5_if/ --mod msw -f abi --mint e -s_min 0.5 --wlink rp -ar_tgt w -bl_tgt w -i_tgt w -i_max 5 -i_type f
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_slink_05_wlink_rp_l_attr_w_bl_w_incl_w_imax_5_if/ --mod mswl -f abi --mint e -s_min 0.5 --wlink rp -ar_tgt w -bl_tgt w -i_tgt w -i_max 5 -i_type f
####
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink_05_mid_wlink_frp_attr_tw_al_am_bl_tw/ --mod mtsw -f ab --mint e --tinm e -tmt trim -s_min 0.5 -s_prb mid --wlink frp -ar_tgt tw -al am -bl_tgt tw
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink_05_wlink_frp_attr_tw_al_am_bl_tw_incl_tw_imax_5_if/ --mod mtsw -f abi --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -ar_tgt tw -al am -bl_tgt tw -i_tgt tw -i_max 5 -i_type f
####
######from here(sample)
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink_05_wlink_frp_attr_tw_al_am_bl_tw_incl_tw_imax_5_if/ --mod mtsw -f abi --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -ar_tgt tw -al am -bl_tgt tw -i_tgt tw -i_max 5 -i_type f
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink_05_wlink_frp_attr_tw_al_am_bl_tw_incl_tw_imax_5_of/ --mod mtsw -f abi --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -ar_tgt tw -al am -bl_tgt tw -i_tgt tw -i_max 5 -i_type o
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink_05_wlink_frp_l_attr_tw_al_am_bl_tw_incl_tw_imax_5_if/ --mod mtswl -f abi --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -ar_tgt tw -al am -bl_tgt tw -i_tgt tw -i_max 5 -i_type f
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim_slink_05_wlink_frp_l_attr_tw_al_am_bl_tw_incl_tw_imax_5_of/ --mod mtswl -f abi --mint e --tinm e -tmt trim -s_min 0.5 --wlink frp -ar_tgt tw -al am -bl_tgt tw -i_tgt tw -i_max 5 -i_type o
####
########mint_e_tinm_p, frp
###### mint_e_tinm_　＋　attr: ok
###### timp_p + incl: ng > 要検討
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink_05_wlink_frp_attr_w/ --mod mtsw -f ab --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink_05_wlink_frp_attr_w_al_am/ --mod mtsw -f ab --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink_05_wlink_frp_attr_w_al_am_bl_tw/ --mod mtsw -f ab --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt tw
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink_05_wlink_frp_attr_w_al_am_bl_w/ --mod mtsw -f ab --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt w
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink_05_wlink_frp_attr_w_al_am_bl_tw_incl_w_imax_5_if/ --mod mtsw -f abi --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt tw -i_tgt w -i_max 5 -i_type f
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink_05_wlink_frp_attr_w_al_am_bl_tw_incl_w_imax_5_of/ --mod mtsw -f abi --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt tw -i_tgt w -i_max 5 -i_type o
####
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink_05_wlink_frp_attr_w_bl_tw/ --mod mtsw -f ab --mint e --tinm p -tmt trim -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt tw
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink_05_wlink_frp_l_attr_w_al_am_bl_tw/ --mod mtswl -f ab --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt tw
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink_05_wlink_frp_l_attr_w_al_am_bl_tw_incl_w_imax_5_if/ --mod mtswl -f abi --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -al am -bl_tgt tw -i_tgt w -i_max 5 -i_type f
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink_05_wlink_frp_l_attr_w_bl_tw/ --mod mtswl -f ab --mint e --tinm p -tmt trim -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt tw
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_p_slink_05_wlink_frp_l_attr_w_bl_tw_incl_w_imax_5_if/ --mod mtsw -f abi --mint e --tinm p -s_min 0.5 --wlink frp -ar_tgt w -bl_tgt tw -i_tgt w -i_max 5 -i_type f
########
######mint_e_trim_tinm_e, frp
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink_05_wlink_frp_attr_mw/ --mod mtsw -f ab --mint e --tinm e -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink_05_wlink_frp_attr_mw_al_am/ --mod mtsw -f ab --mint e --tinm e -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -al am
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink_05_wlink_frp_attr_mw_al_am_bl_tw/ --mod mtsw -f ab --mint e --tinm e -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -al am -bl_tgt tw
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink_05_wlink_frp_attr_mw_al_am_bl_tw_incl_tw_imax__if/ --mod mtsw -f abi --mint e --tinm e -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -al am -bl_tgt tw -i_tgt tw -i_max 5 -i_type f
####
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink_05_wlink_frp_l_attr_mw/ --mod mtswl -f a --mint e --tinm e -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink_05_wlink_frp_l_attr_mw_al_am/ --mod mtswl -f a --mint e --tinm e -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -al am
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink_05_wlink_frp_l_attr_mw_al_am_bl_tw/ --mod mtswl -f ab --mint e --tinm e -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -al am -bl_tgt tw
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink_05_wlink_frp_l_attr_mw_al_am_bl_tw_incl_tw_imax_5_if/ --mod mtswl -f abi --mint e --tinm e -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -al am -bl_tgt tw -i_tgt tw -i_max 5 -i_type f
####
######mint_e_trim_tinm_e, rp mint+ar ok
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink_05_wlink_rp_attr_mw/ --mod mtsw -f a --mint e --tinm e -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink_05_wlink_rp_attr_mtw/ --mod mtsw -f a --mint e --tinm e -tmm trim -s_min 0.5 --wlink rp -ar_tgt mtw
####
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink_05_wlink_rp_attr_mw_al_am/ --mod mtsw -f ab --mint e --tinm e -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw -al am
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink_05_wlink_rp_attr_mw_al_am_bl_tw/ --mod mtsw -f ab --mint e --tinm e -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw -al am -bl_tgt tw
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink_05_wlink_rp_attr_mw_al_am_bl_tw_incl_tw_imax_5_if/ --mod mtsw -f abi --mint e --tinm e -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw -al am -bl_tgt tw -i_tgt tw -i_max 5 -i_type f
####
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink_05_wlink_rp_l_attr_mw/ --mod mtswl -f a --mint e --tinm e -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink_05_wlink_rp_l_attr_mw_al_am/ --mod mtswl -f a --mint e --tinm e -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw -al am
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink_05_wlink_rp_l_attr_mw_al_am_bl_tw/ --mod mtswl -f ab --mint e --tinm e -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw -al am -bl_tgt tw
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_e_slink_05_wlink_rp_l_attr_mw_al_am_bl_tw_incl_tw_imax_5_if/ --mod mtswl -f abi --mint e --tinm e -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw -al am -bl_tgt tw -i_tgt tw -i_max 5 -i_type f
####
######(mint_e_trim_tinm_p, frp) mint e trim: +ar ok
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink_05_wlink_frp_attr_mw/ --mod mtsw -f a --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink_05_wlink_frp_attr_mtw/ --mod mtsw -f a --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mtw
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink_05_wlink_frp_attr_mw_al_am/ --mod mtsw -f a --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -al am
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink_05_wlink_frp_attr_mtw_al_am/ --mod mtsw -f a --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mtw -al am
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink_05_wlink_frp_attr_mw_al_am_bl_tw/ --mod mtsw -f ab --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -al am -bl_tgt tw
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink_05_wlink_frp_attr_mtw_al_am_bl_tw/ --mod mtsw -f ab --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mtw -al am -bl_tgt tw
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink_05_wlink_frp_attr_mw_bl_tw_incl_w_imax_5_if/ --mod mtsw -f abi --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -bl_tgt tw -i_tgt w -i_max 5 -i_type f
######python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink_05_wlink_frp_attr_mtw_bl_tw_incl_w_imax_5_if/ --mod mtsw -f abi --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mtw -bl_tgt tw -i_tgt w -i_max 5 -i_type f
####
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink_05_wlink_frp_l_attr_mw/ --mod mtswl -f a --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink_05_wlink_frp_l_attr_mw_al_am/ --mod mtswl -f a --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -al am
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink_05_wlink_frp_l_attr_mw_al_am_bl_tw/ --mod mtswl -f ab --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -al am -bl_tgt tw
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink_05_wlink_frp_l_attr_mw_al_am_bl_tw_incl_w_imax_5_if/ --mod mtswl -f abi --mint e --tinm p -tmm trim -s_min 0.5 --wlink frp -ar_tgt mw -al am -bl_tgt tw -i_tgt w -i_max 5 -i_type f
####
######mint_e_trim_tinm_p, rp: mint+attr:ok tinm+attr:ng
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink_05_wlink_rp_attr_mw/ --mod mtsw -f a --mint e --tinm p -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink_05_wlink_rp_attr_mw_al_am/ --mod mtsw -f a --mint e --tinm p -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw -al am
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink_05_wlink_rp_attr_mw_al_am_bl_tw/ --mod mtsw -f ab --mint e --tinm p -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw -al am -bl_tgt tw
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink_05_wlink_rp_attr_mw_bl_tw_incl_w_imax_5_if/ --mod mtsw -f abi --mint e --tinm p -tmm trim -s_min 0.5 --wlink rp -ar_tgt mw -bl_tgt tw -i_tgt w -i_max 5 -i_type f
####
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink_05_wlink_rp_l_attr_mw/ --mod mtswl -f ab --mint e --tinm p -tmm trim -s_min 0.5 --wlink rp -al am -ar_tgt mw
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink_05_wlink_rp_l_attr_mw_al_am/ --mod mtswl -f ab --mint e --tinm p -tmm trim -s_min 0.5 --wlink rp -al am -ar_tgt mw -al am
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink_05_wlink_rp_l_attr_mw_al_am_bl_tw/ --mod mtswl -f ab --mint e --tinm p -tmm trim -s_min 0.5 --wlink rp -al am -ar_tgt mw -bl_tgt tw
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim_tinm_p_slink_05_wlink_rp_l_attr_mw_al_am_bl_tw_incl_w_imax_5_if/ --mod mtswl -f abi --mint e --tinm p -tmm trim -s_min 0.5 --wlink rp -al am -ar_tgt mw -bl_tgt tw -i_tgt w -i_max 5 -i_type f
####
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l/ --mod l -f n -a_max 1
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e/ --mod m
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim/ --mod m -f n --mint e -tmm trim
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e/ --mod mt -f n --mint e --tinm e
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_tinm_e_trim/ --mod mt -f n --mint e --tinm e -tmt trim
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e/ --mod m -f n --mint e
####
####
#### mint p trim: +attr ok
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_trim/ --mod m -f n --mint e -tmm trim
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05/ --mod s -f n -s_min 0.5
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e/ --mod t -f n --tinm e
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_trim/ --mod t -f n --tinm e -tmt trim
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p/ --mod t -f n --tinm p
####python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_trim/ --mod t -f n --tinm p -tmt trim
####
####
####
####rm -i ${out_dir_base}*.tsv
####rm ${out_dir_base}*_pre.tsv
####rm ${out_dir_base}*/*_summary.tsv
####rm ${out_dir_base}*/*_anal.tsv
####rm ${out_dir_base}*/*_fn.tsv
####rm ${out_dir_base}*/Airport.tsv
####rm ${out_dir_base}*/City.tsv
####rm ${out_dir_base}*/Company.tsv
####rm ${out_dir_base}*/Compound.tsv
####rm ${out_dir_base}*/Conference.tsv
####rm ${out_dir_base}*/Lake.tsv
####rm ${out_dir_base}*/Person.tsv
####rm ${out_dir_base}*/*.tsv
####grep 'script' ~/PycharmProjects/linkjpc/linkjpc_all_test.sh |  awk '{print $6}' | perl -pe 's/\${out_dir_base}//;' | perl -pe 's/\///g;' | sort | uniq > $eval_target
######grep 'script' ~/PycharmProjects/linkjpc/linkjpc_all_sample.sh | grep -v '##' | awk '{print $6}' | perl -pe 's/\${out_dir_base}//;' | perl -pe 's/\///g;' | sort | uniq > $eval_target
####python json2tsv_linkjp.py $out_dir_base $gold_dir $in_dir $eval_target
####python evaluation_linkjp_old.py $out_dir_base $gold_dir $eval_target
####cd $out_dir_base
####cat */all_summary.tsv > all_summary_pre.tsv
####cat ../summary_header.txt all_summary_pre.tsv > all_summary.tsv
####cp all_summary.tsv eval_$$.txt
####cp ~/PycharmProjects/linkjpc/linkjpc_all_sample.sh env_$$.txt
####cat ./*/*_summary.tsv | grep -v SYS_ID | grep -v ^e | grep -v ^p | sort -d > summary_category_pre.tsv
####cat ../summary_cat_header.txt summary_category_pre.tsv > summary_category.tsv
####cp summary_category.tsv ${setting_dir}summary_category_$$.txt