# dictionaries shared by multiple modules
d_pid2eneid = {}
d_title2pid = {}
d_pid_title_incoming_eneid = {}
d_tag_info = {}
diff_info_ca_backward = {}
diff_info_ca_forward = {}


class LogInfo(object):
    log_file_name_default = 'test.log'
    logging_ini_default = './logging.ini'

    def __init__(self,
                 logging_ini=logging_ini_default):
        self.logging_ini = logging_ini


class OptInfo(object):
    # (scoring) weights of grouped modules
    mod_group_weight_first_default = 1
    mod_group_weight_second_default = 0.1
    mod_group_weight_third_default = 0.01
    mod_group_weight_fourth_default = 0.001
    mod_group_weight_fifth_default = 0.0001
    mod_w_default = ':'.join([str(mod_group_weight_first_default),
                              str(mod_group_weight_second_default),
                              str(mod_group_weight_third_default),
                              str(mod_group_weight_fourth_default),
                              str(mod_group_weight_fifth_default)])
    # common
    ans_max_default = 1
    score_type_default = 'id'
    mod_default = 'n'
    pre_matching_default = 'n'

    # mint/tinm
    mint_default = 'n'
    tinm_default = 'n'
    tinm_min_default = 0.5
    mint_min_default = 0.5
    title_matching_mint_default = 'full'
    title_matching_tinm_default = 'full'
    char_match_cand_num_max_default = 1000
    char_match_min_default = 0.3
    multi_lang_default = 'm'

    # slink
    slink_prob_default = 'fixed'
    slink_min_default = 0.5

    # wlink
    wlink_default = 'n'
    wf_score_default = 0.6
    wl_score_forward_default = 0.2
    wl_score_backward_default = 0.3
    wl_score_same_default = 0.5
    wr_score_default = 0.8
    wp_score_default = 0.7
    wl_lines_backward_max_default = 1
    wl_lines_forward_max_default = 1
    wl_lines_backward_ca_default = 'r'
    wl_lines_forward_ca_default = 'r'
    wl_lines_backward_ca_ratio_default = 0.9
    wl_lines_forward_ca_ratio_default = 0.9
    wl_break_default = True

    # link_prob
    lp_min_default = 0.5

    # filtering
    filtering_default = 'n'

    # attr_range
    attr_rng_auto_freq_min_default = 5
    attr_len_max = 4
    attr_depth_base_default = 0.5
    attr_len_default = 'n'
    attr_rng_tgt_default = 'n'
    attr_ok_co_default = 1.0
    attr_na_co_default = 0.9
    attr_ng_co_default = 0.1
    # the first layer (string)
    eneid_ignore = '1'

    # attr rng
    attr_rng_type_default = 'a'

    # back link
    back_link_tgt_default = 'n'
    back_link_ok_default = 1.0
    back_link_ng_default = 0.7

    # incl
    incl_tgt_default = 'n'
    incl_type_default = 'n'
    incl_max_default = 1

    # detect nil
    nil_tgt_default = 'n'
    nil_all_freq_min_default = 7

    nil_cat_attr_max_default = 0.01
    len_desc_text_min_default = 7
    nil_cond_default = 'and_prob_or_len_desc'
    nil_desc_exception_default = 'n'
    nil_desc_exception_def = {'person_works':'Person:??????', 'company_trade_names':'Company:?????????'}

    min_illegal_title_len = 500

    def __init__(self,
                 ans_max=ans_max_default,
                 attr_rng_auto_freq_min=attr_rng_auto_freq_min_default,
                 attr_len=attr_len_default,
                 attr_na_co=attr_na_co_default,
                 attr_ng_co=attr_ng_co_default,
                 attr_ok_co=attr_ok_co_default,
                 attr_rng_tgt=attr_rng_tgt_default,
                 attr_rng_type=attr_rng_type_default,
                 incl_max=incl_max_default,
                 incl_tgt=incl_tgt_default,
                 incl_type=incl_type_default,
                 back_link_ng=back_link_ng_default,
                 back_link_ok=back_link_ok_default,
                 back_link_tgt=back_link_tgt_default,
                 char_match_cand_num_max=char_match_cand_num_max_default,
                 char_match_min=char_match_min_default,
                 filtering=filtering_default,
                 len_desc_text_min=len_desc_text_min_default,
                 nil_all_freq_min=nil_all_freq_min_default,
                 lp_min=lp_min_default,
                 mint=mint_default,
                 mint_min=mint_min_default,
                 mod=mod_default,
                 mod_w=mod_w_default,
                 multi_lang=multi_lang_default,
                 nil_cat_attr_max=nil_cat_attr_max_default,
                 nil_cond=nil_cond_default,
                 nil_desc_exception=nil_desc_exception_default,
                 nil_target=nil_tgt_default,
                 score_type=score_type_default,
                 slink_min=slink_min_default,
                 slink_prob=slink_prob_default,
                 tinm=tinm_default,
                 tinm_min=tinm_min_default,
                 title_matching_mint=title_matching_mint_default,
                 title_matching_tinm=title_matching_tinm_default,
                 wl_break=wl_break_default,
                 wl_score_forward=wl_score_forward_default,
                 wl_score_backward=wl_score_backward_default,
                 wl_score_same=wl_score_same_default,
                 wl_lines_backward_max=wl_lines_backward_max_default,
                 wl_lines_forward_max=wl_lines_forward_max_default,
                 wl_lines_backward_ca=wl_lines_backward_ca_default,
                 wl_lines_forward_ca=wl_lines_forward_ca_default,
                 wl_lines_backward_ca_ratio=wl_lines_backward_ca_ratio_default,
                 wl_lines_forward_ca_ratio=wl_lines_forward_ca_ratio_default,
                 wlink=wlink_default,
                 wp_score=wp_score_default,
                 wr_score=wr_score_default,
                 wf_score=wf_score_default,
                 ):
        self.ans_max = ans_max
        self.attr_rng_auto_freq_min_default = attr_rng_auto_freq_min
        self.attr_len = attr_len
        self.attr_na_co = attr_na_co
        self.attr_ng_co = attr_ng_co
        self.attr_ok_co = attr_ok_co
        self.attr_rng_tgt = attr_rng_tgt
        self.attr_rng_type = attr_rng_type
        self.back_link_ng = back_link_ng
        self.back_link_ok = back_link_ok
        self.back_link_tgt = back_link_tgt
        self.char_match_cand_num_max = char_match_cand_num_max
        self.char_match_min = char_match_min
        self.incoming_link_max = incl_max
        self.incoming_link_tgt = incl_tgt
        self.incoming_link_type = incl_type
        self.filtering = filtering
        self.len_desc_text_min = len_desc_text_min
        self.link_prob_min = lp_min
        self.mention_in_title = mint
        self.mention_in_title_min = mint_min
        self.mod = mod
        self.mod_w = mod_w
        self.multi_lang = multi_lang
        self.nil_all_freq_min = nil_all_freq_min
        self.nil_cat_attr_max = nil_cat_attr_max
        self.nil_cond = nil_cond
        self.nil_desc_exception = nil_desc_exception
        self.nil_target = nil_target
        self.score_type = score_type
        self.slink_min = slink_min
        self.slink_prob = slink_prob
        self.title_in_mention = tinm
        self.title_in_mention_min = tinm_min
        self.title_matching_mint = title_matching_mint
        self.title_matching_tinm = title_matching_tinm
        self.wikilink = wlink
        self.wl_break = wl_break
        self.wl_lines_backward_max = wl_lines_backward_max
        self.wl_lines_forward_max = wl_lines_forward_max
        self.wl_lines_backward_ca = wl_lines_backward_ca
        self.wl_lines_forward_ca = wl_lines_forward_ca
        self.wl_lines_backward_ca_ratio = wl_lines_backward_ca_ratio
        self.wl_lines_forward_ca_ratio = wl_lines_forward_ca_ratio
        self.wl_score_forward = wl_score_forward
        self.wl_score_backward = wl_score_backward
        self.wl_score_same = wl_score_same
        self.wp_score = wp_score
        self.wr_score = wr_score
        self.wf_score = wf_score


class DataInfo(object):
    # (0) project SHINRA data distribution (common_data_dir)
    # [CD1]
    f_cirrus_content_default = 'wikipedia-ja-20210823-json.gz'
    #
    # [CD2]
    f_ene_def_for_task_default = 'ene_definition_v9.0.0-with-attributes-and-shinra-tasks-20220714.jsonl'

    # [CD3]
    f_enew_org_default = 'shinra2022_Categorization_train_20220616.jsonl'

    # (1) manually created data (common_data_dir)
    # [CM1]
    f_disambiguation_pat_default = 'wikipat_dis.tsv'

    # [CM2]
    f_self_link_pat_default = 'self_link_pat.tsv'

    # [CM3]
    f_attr_rng_man_org_default = 'attr_rng_man_org_ene90_20221010.tsv'
    #
    # [CM4]
    f_back_link_dump_org_default = 'jawiki-20210820-pagelinks_dmp.tsv'

    # [CM5]
    f_redirect_dump_org_default = 'jawiki-20210820-redirect_dmp.tsv'

    # [CM6]
    f_redirect_dump_default = 'jawiki-20210820-redirect_dmp_rev.tsv'

    # [CM7]
    f_page_dump_org_default = 'jawiki-20210820-page_dmp.tsv'

    # [CM8]
    f_page_dump_default = 'jawiki-20210820-page_dmp_rev.tsv'

    # [CM9]
    f_page_dump_old_org_default = 'jawiki-20190120-page_dmp.tsv'

    # [CM10]
    f_lang_link_dump_org_default = 'jawiki-20210820-langlinks_dmp.tsv'

    # [CM11]
    f_enew_mod_list_default = 'shinra2022_Categorization_train_20220616_stoplist.tsv'

    # [CM12]
    f_wl_lines_backward_ca_default = 'wl_lines_backward_ca.tsv'

    # [CM13]
    f_wl_lines_forward_ca_default = 'wl_lines_forward_ca.tsv'

    # [CM14]
    f_sample_gold_mod_list_default = 'train-link-20221004_stoplist_all.tsv'
    #
    # [CM15]
    f_nil_cand_man_default = 'cat_attr_nil_cand_man.tsv'

    # [CM16]
    f_nil_stop_attr_default = 'nil_stop_attr_man.tsv'

    # (2) preprocessing
    # (2-1) sample_gold_data_dir
    # [SP1] (sample gold data info)

    # (2-2) common_data_dir

    # [CP1]
    f_common_html_info_default = 'common_html_tag_info.tsv'

    # [CP2]
    f_wikipedia_page_change_info_default = 'jawiki-20190120_20210820_page_change_info.tsv'

    # [CP3]
    f_disambiguation_default = 'jawiki-20210823-cirrussearch-content_disambiguation.tsv'

    # [CP4]
    f_redirect_info_default = 'jawiki-20210823_title2pageid_20210820_nodis.tsv'

    # [CP5]
    f_incoming_default = 'jawiki-20210823-cirrussearch-content_incoming_link.tsv'

    # [CP6]
    f_enew_info_default = 'shinra2022_Categorization_train_20220616_mod.tsv'

    # [CP7]
    f_slink_default = 'cat_attr_self_link.tsv'

    # [CP8]
    f_self_link_by_attr_name_default = 'self_link_by_attr_name.txt'

    # [CP9]
    f_link_prob_default = 'sample_cat_attr_mention_linkcand.tsv'

    # [CP10]
    f_linkable_info_default = 'cat_attr_linkable.tsv'

    # [CP11]
    f_mention_gold_link_dist_default = 'mention_gold_link_dist.tsv'

    # [CP12]
    f_attr_rng_man_default = 'attr_rng_man.tsv'

    # [CP13]
    f_attr_rng_auto_default = 'attr_rng_auto.tsv'

    # [CP14]
    f_target_attr_info_default = 'ene_definition_v9.0.0-20220714_target_attr.tsv'

    # [CP15]
    f_all_cat_info_default = 'ene_definition_v9.0.0-20220714_all_cat.tsv'

    # [CP16]
    f_lang_link_info_default = 'jawiki-20210820-langlinks_info.tsv'

    # [CP17]
    f_title2pid_ext_default = 'jawiki-20210823_title2pageid_20210820_ext.tsv'

    # [CP19]
    f_title2pid_org_default = 'jawiki-20210820-title2pageid.jsonl'

    # (2-3) tmp_data_dir
    # [TP1]
    f_input_title_default = 'input_title.txt'

    # [TP2]
    f_back_link_default = 'back_link_full.tsv'

    # [TP3]
    f_mint_partial_default = 'mint_partial_match.tsv'

    # [TP4]
    f_mint_trim_partial_default = 'mint_trim_partial_match.tsv'

    # [TP5]
    f_tinm_partial_default = 'tinm_partial_match.tsv'

    # [TP6]
    f_tinm_trim_partial_default = 'tinm_trim_partial_match.tsv'

    # [TP7]
    f_html_info_default = 'html_tag_info.tsv'

    # (3) entity linking
    # (3-1) common_data_dir

    # [CL1]
    f_mention_gold_link_dist_info_default = 'mention_gold_link_dist_info.tsv'

    # [CL2]
    f_attr_rng_merged_default = 'attr_rng_merged.tsv'

    def __init__(self,
                 common_data_dir,
                 tmp_data_dir,
                 in_dir,
                 sample_gold_dir,
                 sample_input_dir,
                 out_dir,
                 f_attr_rng_man=f_attr_rng_man_default,
                 f_attr_rng_man_org=f_attr_rng_man_org_default,
                 f_attr_rng_auto=f_attr_rng_auto_default,
                 f_cirrus_content=f_cirrus_content_default,
                 f_ene_def_for_task=f_ene_def_for_task_default,
                 f_enew_info=f_enew_info_default,
                 f_enew_org=f_enew_org_default,
                 f_enew_mod_list=f_enew_mod_list_default,
                 f_redirect_info=f_redirect_info_default,
                 f_title2pid_ext=f_title2pid_ext_default,
                 f_title2pid_org=f_title2pid_org_default,
                 f_disambiguation=f_disambiguation_default,
                 f_disambiguation_pat=f_disambiguation_pat_default,
                 f_back_link=f_back_link_default,
                 f_common_html_info=f_common_html_info_default,
                 f_html_info=f_html_info_default,
                 f_input_title=f_input_title_default,
                 f_lang_link_info=f_lang_link_info_default,
                 f_lang_link_dump_org=f_lang_link_dump_org_default,
                 f_linkable_info=f_linkable_info_default,
                 f_mention_gold_link_dist_info=f_mention_gold_link_dist_info_default,
                 f_mention_gold_link_dist=f_mention_gold_link_dist_default,
                 f_mint_partial=f_mint_partial_default,
                 f_mint_trim_partial=f_mint_trim_partial_default,
                 f_nil_cand_man=f_nil_cand_man_default,
                 f_page_dump=f_page_dump_default,
                 f_page_dump_org=f_page_dump_org_default,
                 f_redirect_dump=f_redirect_dump_default,
                 f_redirect_dump_org=f_redirect_dump_org_default,
                 f_tinm_partial=f_tinm_partial_default,
                 f_tinm_trim_partial=f_tinm_trim_partial_default,
                 f_link_prob=f_link_prob_default,
                 f_slink=f_slink_default,
                 f_self_link_by_attr_name=f_self_link_by_attr_name_default,
                 f_wl_lines_forward_ca=f_wl_lines_forward_ca_default,
                 f_wl_lines_backward_ca=f_wl_lines_backward_ca_default
                 ):
        self.common_data_dir = common_data_dir
        self.tmp_data_dir = tmp_data_dir
        self.in_dir = in_dir
        self.in_ene_dir = in_dir + 'ene_annotation/'
        self.in_html_dir = in_dir + 'html/'

        self.out_dir = out_dir

        # common_data_dir
        self.sample_gold_dir = sample_gold_dir
        self.sample_input_dir = sample_input_dir

        self.attr_rng_man_file = common_data_dir + f_attr_rng_man
        self.attr_rng_man_org_file = common_data_dir + f_attr_rng_man_org

        self.attr_rng_auto_file = common_data_dir + f_attr_rng_auto
        self.cirrus_content_file = common_data_dir + f_cirrus_content
        self.common_html_info_file = common_data_dir + f_common_html_info
        self.disambiguation_file = common_data_dir + f_disambiguation
        self.disambiguation_pat_file = common_data_dir + f_disambiguation_pat
        self.ene_def_for_task_file = common_data_dir + f_ene_def_for_task
        self.enew_info_file = common_data_dir + f_enew_info
        self.enew_org_file = common_data_dir + f_enew_org
        self.enew_mod_list_file = common_data_dir + f_enew_mod_list
        self.lang_link_info_file = common_data_dir + f_lang_link_info
        self.lang_link_dump_org_file = common_data_dir + f_lang_link_dump_org
        self.link_prob_file = common_data_dir + f_link_prob
        self.linkable_info_file = common_data_dir + f_linkable_info
        self.mention_gold_link_dist_info_file = common_data_dir + f_mention_gold_link_dist_info
        self.mention_gold_link_dist_file = common_data_dir + f_mention_gold_link_dist
        self.nil_cand_man_file = common_data_dir + f_nil_cand_man
        self.page_dump_file = common_data_dir + f_page_dump
        self.page_dump_org_file = common_data_dir + f_page_dump_org
        self.redirect_dump_file = common_data_dir + f_redirect_dump
        self.redirect_dump_org_file = common_data_dir + f_redirect_dump_org
        self.redirect_info_file = common_data_dir + f_redirect_info
        self.slink_file = common_data_dir + f_slink
        self.self_link_by_attr_name_file = common_data_dir + f_self_link_by_attr_name
        self.title2pid_ext_file = common_data_dir + f_title2pid_ext
        self.title2pid_org_file = common_data_dir + f_title2pid_org
        self.wl_lines_forward_ca_file = common_data_dir + f_wl_lines_forward_ca
        self.wl_lines_backward_ca_file = common_data_dir + f_wl_lines_backward_ca

        # tmp_data_dir
        self.back_link_file = tmp_data_dir + f_back_link
        self.html_info_file = tmp_data_dir + f_html_info
        self.input_title_file = tmp_data_dir + f_input_title
        self.mint_partial_match_file = tmp_data_dir + f_mint_partial
        self.mint_trim_partial_match_file = tmp_data_dir + f_mint_trim_partial
        self.tinm_partial_match_file = tmp_data_dir + f_tinm_partial
        self.tinm_trim_partial_match_file = tmp_data_dir + f_tinm_trim_partial


class MentionInfo(object):
    # Note: Never change the order
    def __init__(self,
                 pid,
                 ene_cat,
                 attr_label,
                 t_start_line_id,
                 t_start_offset,
                 t_end_line_id,
                 t_end_offset,
                 t_mention,
                 h_start_line_id,
                 h_start_offset,
                 h_end_line_id,
                 h_end_offset,
                 h_mention,
                 link_page_id,
                 ):
        self.attr_label = attr_label
        self.ene_cat = ene_cat
        self.h_end_line_id = h_end_line_id
        self.h_end_offset = h_end_offset
        self.h_mention = h_mention
        self.h_start_line_id = h_start_line_id
        self.h_start_offset = h_start_offset
        self.link_page_id = link_page_id
        self.pid = pid
        self.t_start_line_id = t_start_line_id
        self.t_start_offset = t_start_offset
        self.t_end_line_id = t_end_line_id
        self.t_end_offset = t_end_offset
        self.t_mention = t_mention


class MentionInfoTask2(object):
    def __init__(self,
                 pid,
                 ene_cat,
                 attr_label,
                 t_start_line_id,
                 t_start_offset,
                 t_end_line_id,
                 t_end_offset,
                 t_mention,
                 h_start_line_id,
                 h_start_offset,
                 h_end_line_id,
                 h_end_offset,
                 h_mention,
                 link_page_id,
                 link_type_last_name,
                 link_type_part_of,
                 link_type_derivation_of
                 ):
        self.pid = pid
        self.ene_cat = ene_cat
        self.attr_label = attr_label
        self.t_start_line_id = t_start_line_id
        self.t_start_offset = t_start_offset
        self.t_end_line_id = t_end_line_id
        self.t_end_offset = t_end_offset
        self.t_mention = t_mention
        self.h_start_line_id = h_start_line_id
        self.h_start_offset = h_start_offset
        self.h_end_line_id = h_end_line_id
        self.h_end_offset = h_end_offset
        self.h_mention = h_mention
        self.link_page_id = link_page_id
        self.link_type_last_name = link_type_last_name
        self.link_type_part_of = link_type_part_of
        self.link_type_derivation_of = link_type_derivation_of


class LinkInfo(object):
    def __init__(self, name):
        self.name = name
        self.cand_dic_mint = {}
        self.cand_dic_tinm = {}
        self.cand_dic_wlink = {}
        self.cand_dic_slink = {}
        self.cand_dic_link_prob = {}


class ModInfo(object):
    mint_weight_init = 0
    tinm_weight_init = 0
    wlink_weight_init = 0
    slink_weight_init = 0
    link_prob_weight_init = 0

    def __init__(self,
                 mint_weight=mint_weight_init,
                 tinm_weight=tinm_weight_init,
                 wlink_weight=wlink_weight_init,
                 slink_weight=slink_weight_init,
                 link_prob_weight=link_prob_weight_init
                 ):
        self.mint_weight = mint_weight
        self.tinm_weight = tinm_weight
        self.wlink_weight = wlink_weight
        self.slink_weight = slink_weight
        self.link_prob_weight = link_prob_weight


class AnalDataInfo(object):
    f_target_default = 'eval_target.txt'
    f_diff_judge_info_default = 'diff_judge.tsv'
    f_ok_freq_info_default = 'diff_judge_ok_freq.tsv'
    f_ng_freq_info_default = 'diff_judge_ng_freq.tsv'
    f_eval_info_default = 'diff_judge_eval.tsv'

    def __init__(self,
                 gold_dir,
                 sys_dir_common,
                 sys_dir_version,
                 f_target=f_target_default,
                 f_diff_judge=f_diff_judge_info_default,
                 f_ok_freq_info=f_ok_freq_info_default,
                 f_ng_freq_info=f_ng_freq_info_default,
                 f_eval_info=f_eval_info_default):
        self.gold_dir = gold_dir
        self.sys_dir_common = sys_dir_common
        self.sys_dir_version = sys_dir_version
        self.f_target = f_target
        self.f_diff_judge = f_diff_judge
        self.f_ok_freq_info = f_ok_freq_info
        self.f_ng_freq_info = f_ng_freq_info
        self.f_eval_info = f_eval_info
