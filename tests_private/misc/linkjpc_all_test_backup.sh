#!/bin/sh -x
script="./linkjpc.py"
common_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/common/"
tmp_data_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/test/"
gold_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-210825/link_annotation/"
in_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-210825/ene_annotation/"
out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/20210905/"
eval_target="./eval_target_test.txt"
out_dir_tmp_base="/Users/masako/tmp/"
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}l/ --mod l -f n -a_max 1
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_02/ --mod m -f n --mint e -a_max 1 -m_min 0.2 -c_max 1000
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_02_attr_m/ --mod m -f a --mint e -a_max 1 -m_min 0.2 -c_max 1000 -ar_tgt m
###python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_02_incl_1/ --mod m -f i -i_tgt m --mint e -a_max 1 -i_max 1 -m_min 0.2 -c_max 1000
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_02_slink_05/ --mod ms -f n --mint e -a_max 1 -m_min 0.2 -c_max 1000 -s_min 0.5
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_02_slink_05_winm_r/ --mod msw -f n --mint e -a_max 1 -m_min 0.2 -c_max 1000 -s_min 0.5 --winm r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_02__slink_05__winm_r/ --mod m:s:w -f n --mint e -a_max 1 -m_min 0.2 -c_max 1000 -s_min 0.5 --winm r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_02_winm_r/ --mod mw -f n --mint e -a_max 1 -m_min 0.2 -c_max 1000 --winm r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_e_02__winm_r/ --mod m:w -f n --mint e -a_max 1 -m_min 0.2 -c_max 1000 --winm r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_02/ --mod m -f n --mint p -a_max 1 -m_min 0.2 -c_max 1000
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_02_incl_1/ --mod m -f i -i_tgt m --mint p -a_max 1 -i_max 1 -m_min 0.2 -c_max 1000
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_02_slink_05/ --mod ms -f n --mint p -a_max 1 -m_min 0.2 -c_max 1000 -s_min 0.5
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_02_slink_05_winm_r/ --mod msw -f n --mint p -a_max 1 -m_min 0.2 -c_max 1000 -s_min 0.5 --winm r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_02_winm_r/ --mod mw -f n --mint p -a_max 1 -m_min 0.2 -c_max 1000 --winm r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_02_winm_r__slink_05/ --mod mw:s -f n --mint p -a_max 1 -m_min 0.2 -c_max 1000 -s_min 0.5 --winm r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_02__winm_r__slink_05/ --mod m:w:s -f n --mint p -a_max 1 -m_min 0.2 -c_max 1000 --winm r -s_min 0.5
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}mint_p_02_winm_r_slink_05/ --mod mws -f n --mint p -a_max 1 -m_min 0.2 -c_max 1000 --winm r -s_min 0.5
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05/ --mod s -f n -s_min 0.5
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05__mint_e_02__winm_r/ --mod s:m:w -f n --mint e -a_max 1 -m_min 0.2 -c_max 1000 -s_min 0.5 --winm r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05__winm_r__mint_e_02/ --mod s:w:m -f n --mint e -a_max 1 -m_min 0.2 -c_max 1000 -s_min 0.5 --winm r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_winm_r__mint_e_02/ --mod sw:m -f n --mint e -a_max 1 -m_min 0.2 -c_max 1000 -s_min 0.5 --winm r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}slink_05_mint_e_02_winm_r/ --mod smw -f n --mint e -a_max 1 -m_min 0.2 -c_max 1000 -s_min 0.5 --winm r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_02/ --mod t -f n --tinm e -a_max 1 -t_min 0.2 -c_max 1000
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_02__winm_r/ --mod t:w -f n --tinm e -a_max 1 -m_min 0.2 -c_max 1000 --winm r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_02_slink_05/ --mod ts -f n --tinm e -a_max 1 -m_min 0.2 -c_max 1000 -s_min 0.5
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_e_02_winm_r/ --mod tw -f n --tinm e -a_max 1 -m_min 0.2 -c_max 1000 --winm r --winm r -a_max 1
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_02/ --mod t -f n --tinm p -a_max 1 -t_min 0.2 -c_max 1000
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}tinm_p_02_incl_1/ --mod t -f i -i_tgt t --tinm p -a_max 1 -i_max 1 -t_min 0.2 -c_max 1000
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}winm_r/ --mod w -f n --winm r -a_max 1
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}winm_r__mint_e_02/ --mod w:m -f n --mint e -a_max 1 -m_min 0.2 -c_max 1000 --winm r
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}winm_r__slink_05__mint_e_02/ --mod w:s:m -f n --mint e -a_max 1 -m_min 0.2 -c_max 1000 --winm r -s_min 0.5
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}winm_r__slink_05_mint_e_02/ --mod ws:m -f n --mint e -a_max 1 -m_min 0.2 -c_max 1000 --winm r -s_min 0.5
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}winm_r__mint_e_02__slink_05/ --mod w:m:s -f n --mint e -a_max 1 -m_min 0.2 -c_max 1000 --winm r -s_min 0.5
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}winm_u/ --mod w -f n --winm u -a_max 1
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}winm_u__slink_05__mint_e_02/ --mod w:s:m: -f n --mint e -a_max 1 -m_min 0.2 -c_max 1000 -s_min 0.5 --winm u
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}winm_u__slink_05_mint_e_02/ --mod w:sm: -f n --mint e -a_max 1 -m_min 0.2 -c_max 1000 -s_min 0.5 --winm u
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}winm_u__mint_e_02__slink_05/ --mod w:m:s: -f n --mint e -a_max 1 -m_min 0.2 -c_max 1000 -s_min 0.5 --winm u
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}winm_u_slink_05__mint_e_02/ --mod ws:m: -f n --mint e -a_max 1 -m_min 0.2 -c_max 1000 -s_min 0.5 --winm u
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}winm_u_slink_05_mint_e_02/ --mod wsm: -f n --mint e -a_max 1 -m_min 0.2 -c_max 1000 -s_min 0.5 --winm u
#python $script $common_data_dir $tmp_data_dir $in_dir ${out_dir_base}winm_u_mint_e_02_slink_05/ --mod wms -f n --mint e -a_max 1 -m_min 0.2 -c_max 1000 -s_min 0.5 --winm u
rm -i /Users/masako/Documents/SHINRA/2021-LinkJP/test_out/20210905/*.tsv
rm /Users/masako/Documents/SHINRA/2021-LinkJP/test_out/20210905/*/*.tsv
python CnvJson2TsvLinkJP.py $out_dir_base $gold_dir $in_dir $eval_target
python DiffTsvLinkJPAll.py $out_dir_base $gold_dir $eval_target
cd $out_dir_base
cat */all_summary.tsv > all_summary_pre.tsv
cat ../summary_header.txt all_summary_pre.tsv > all_summary.tsv
cat ./*/*_summary.tsv | grep -v SYS_ID | grep -v ^e | grep -v ^p | sort -d > summary_category_pre.tsv
cat ../summary_cat_header.txt summary_category_pre.tsv > summary_category.tsv