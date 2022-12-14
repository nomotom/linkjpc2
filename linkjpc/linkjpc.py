import detect_nil as dn
import incl_filtering as il
import matching as mc
import get_wlink as gw
import self_link as sl
import link_prob as lp
import attr_range_filtering as ar
import compile_list as cl
import get_score as gs
import ljc_common as lc
import back_link as bl
from glob import glob
import json
import os
import sys
import click
import copy
import config as cf
import logging
import logging.config


def set_logging(log_info, logger_name):
    from os import path

    logging_ini = log_info.logging_ini
    log_file_path = path.join(path.dirname(path.abspath(__file__)), logging_ini)
    logging.config.fileConfig(log_file_path)

    logger = logging.getLogger(logger_name)
    return logger


@click.command()
@click.argument('common_data_dir', type=click.Path(exists=True))
@click.argument('tmp_data_dir', type=click.Path(exists=True))
@click.argument('in_dir', type=click.Path(exists=True))
@click.argument('sample_gold_dir',  type=click.Path(dir_okay=True))
@click.argument('sample_input_dir',  type=click.Path(dir_okay=True))
@click.argument('out_dir',  type=click.Path(dir_okay=True))
# common
@click.option('--filtering', '-f', type=click.Choice(['a',  'b', 'i', 'n', 'ai', 'ab', 'an', 'bi', 'bn', 'in',
                                                      'abi', 'abn', 'ain', 'bin', 'abin', 'x']), required=True,
              default=cf.OptInfo.filtering_default, show_default=True,
              help='types of filtering used in any module, a: attribute range filtering, i: filtering by incoming link '
                   'num,　b: backlink, n: nil detection filtering, ai, ab, ..., abin: combination of a, b ,i, n, '
                   'x: N/A')
@click.option('--mod', type=click.STRING, required=True,
              help='a comma-separated priority list of module groups'
                   '(denoted by the combination of characters (m, t, w, s, l)) to be used'
                   'eg. m:sw:t (first priority group: m, second priority group:sw, third priority group:t)')
@click.option('--mod_w', type=click.STRING,
              default=cf.OptInfo.mod_w_default, show_default=True,
              help='module group weight list (Float list separated by colon),'
                   'format: mod_group_first_weight:mod_group_second_weight:mod_group_third_weight:'
                   'mod_group_fourth_weight:mod_group_fifth_weight,'
                   'eg: 1.0:0.1:0.01:0.001:0.0001')
@click.option('--ans_max', '-a_max', type=click.INT, required=True,
              default=cf.OptInfo.ans_max_default, show_default=True,
              help='maximum number of output answers for one mention')
@click.option('--score_type', type=click.Choice(['id', 'n']),
              default=cf.OptInfo.score_type_default, show_default=True,
              help='scoring type,'
                   'id: use numerical sort result of candidate pageids if their scores are the same, n: N/A')
@click.option('--f_title2pid_ext', type=click.STRING,
              default=cf.DataInfo.f_title2pid_ext_default, show_default=True,
              help='filename of title2pageid extended information file, in which most of the disambiguation, '
                   'management or format-error pages are deleted and ENEIDs and incoming link num info are added.')
@click.option('--f_target_attr_info', type=click.STRING,
              default=cf.DataInfo.f_target_attr_info_default, show_default=True,
              help='filename of target_attribute info list.')
@click.option('--f_all_cat_info', type=click.STRING,
              default=cf.DataInfo.f_all_cat_info_default, show_default=True,
              help='filename of all cat info list.')
# modules (mint & tinm)
@click.option('--char_match_cand_num_max', '-c_max', type=click.INT,
              default=cf.OptInfo.char_match_cand_num_max_default, show_default=True,
              help='maximum number of candidate link pages for one mention in each string matching module (mint/tinm)')
@click.option('--multi_lang', default=cf.OptInfo.multi_lang_default, type=click.Choice(['j', 'je', 'm']),
              show_default=True,
              help='specify if foreign language titles based on interlanguage links should be used for matching.'
                   'j: use original titles.'
                   'je: add English titles. '
                   'm: add all the foreign language titles.')
# module: mint
@click.option('--mint', type=click.Choice(['e', 'p', 'n']),
              default=cf.OptInfo.mint_default, show_default=True,
              help='mention in title: how to match mentions to titles of candidate pages: '
                   'e: exact match, p: partial match, n: N/A')
@click.option('--mint_min', '-m_min', type=click.FLOAT,
              default=cf.OptInfo.mint_min_default, show_default=True,
              help='minimum length ratio of mentions in titles of candidate Wikipedia pages to be linked.')
@click.option('--f_mint', type=click.STRING,
              default=cf.DataInfo.f_mint_partial_default, show_default=True,
              help='filename of partial match info file (mention in title)')
@click.option('--f_mint_trim', type=click.STRING,
              default=cf.DataInfo.f_mint_trim_partial_default, show_default=True,
              help='filename of partial match info file (mention in title)')
@click.option('--title_matching_mint', '-tmm', type=click.Choice(['trim', 'full']),
              default=cf.OptInfo.title_matching_mint_default, show_default=True,
              help='title matching in mint (title matching in mention in title)')
# module: tinm
@click.option('--tinm', type=click.Choice(['e', 'p', 'n']),
              default=cf.OptInfo.tinm_default, show_default=True,
              help='title in mention: how to match titles of candidate pages to mentions'
                   'e: exact match, p: partial match, n: N/A')
@click.option('--tinm_min', '-t_min', type=click.FLOAT,
              default=cf.OptInfo.tinm_min_default, show_default=True,
              help='minimum length ratio of titles of candidate Wikipedia pages in mentions. ')
@click.option('--f_tinm', type=click.STRING,
              default=cf.DataInfo.f_tinm_partial_default, show_default=True,
              help='filename of partial match info file (title in mention)')
@click.option('--f_tinm_trim', type=click.STRING,
              default=cf.DataInfo.f_tinm_trim_partial_default, show_default=True,
              help='filename of partial match info file (title trimmed in mention)')
@click.option('--title_matching_tinm', '-tmt', type=click.Choice(['trim', 'full']),
              default=cf.OptInfo.title_matching_tinm_default, show_default=True,
              help='title matching in tinm (title matching in title in mention)')
# module: wlink
@click.option('--wlink', '-wl', type=click.STRING, required=True,
              default=cf.OptInfo.wlink_default, show_default=True,
              help='scoring of the wikipedia links in the mentions. combination of the following: '
                   'f: add higher score to the first link in the mention than others,'
                   'r: add higher score to the rightmost link in the mention than others, '
                   'm: give equal score to all the links in the mention'
                   'p: give score to the links of the previous same mentions in the page'
                   'l: give score to the links around the mention in the lines of page specified with '
                   'wl_lines_backward_max and wl_lines_forward_max'
                   'n: N/A. '
                   'Notice that m cannot be used with f or r.')
@click.option('--f_html_info', type=click.STRING,
              default=cf.DataInfo.f_html_info_default, show_default=True,
              help='filename of html tag info file.')
@click.option('--wf_score', '-wf', type=click.FLOAT,
              default=cf.OptInfo.wf_score_default, show_default=True,
              help='score for the first wikipedia link in the mention (when f is specified in wlink).(0.0-1.0)')
@click.option('--wr_score', '-wr', type=click.FLOAT,
              default=cf.OptInfo.wr_score_default, show_default=True,
              help='score for rightmost wikipedia link in the mention (when r is specified in wlink).(0.0-1.0)')
@click.option('--wp_score', '-wp', type=click.FLOAT,
              default=cf.OptInfo.wp_score_default, show_default=True,
              help='score for the links of the previous mentions in the page (when p is specified in wlink). (0.0-1.0)')
@click.option('--wl_score_same', '-wls', type=click.FLOAT,
              default=cf.OptInfo.wl_score_same_default, show_default=True,
              help='score for the links around the mention (same line) in the page (when l is specified in wlink).'
                   ' (0.0-1.0)')
@click.option('--wl_score_backward', '-wlb', type=click.FLOAT,
              default=cf.OptInfo.wl_score_backward_default, show_default=True,
              help='score for the links around the mention (backward lines) in the page (when l is specified in wlink).'
                   '(0.0-1.0)')
@click.option('--wl_score_forward', '-wlf', type=click.FLOAT,
              default=cf.OptInfo.wl_score_forward_default, show_default=True,
              help='score for the links around the mention (forward lines) in the page (when l is specified in wlink).'
                   '(0.0-1.0) ')
@click.option('--wl_break/--no-wl_break', default=cf.OptInfo.wl_break_default, show_default=True,
              help='flag to stop searching candidate wikilinks at the line in which nearest candidate link is found')
@click.option('--wl_lines_backward_max', '-wl_bmax', type=click.INT,
              default=cf.OptInfo.wl_lines_backward_max_default, show_default=True,
              help='maximum number of lines to backward-search wikipedia links in the page (when l is specified in '
                   'wlink)')
@click.option('--wl_lines_forward_max', '-wl_fmax', type=click.INT,
              default=cf.OptInfo.wl_lines_forward_max_default, show_default=True,
              help='maximum number of lines to forward-search wikipedia links in the page (when l is specified in '
                   'wlink)')
@click.option('--wl_lines_backward_ca', '-wl_bca', type=click.Choice(['f', 'r', 'fr',  'n']),
              default=cf.OptInfo.wl_lines_backward_ca_default, show_default=True,
              help='how to specify the maximum number of lines to backward-search Wikipedia links for each '
                   'category-attribute (when l is specified in wlink).'
                   'f: the number specified in f_wl_lines_backward_max_ca, r: the number estimated using the ratio '
                   'specified by wl_lines_backward_ca_ratio, fr: both f and r (f takes precedence), n: N/A')
@click.option('--wl_lines_forward_ca', '-wl_fca', type=click.Choice(['f', 'r', 'fr',  'n']),
              default=cf.OptInfo.wl_lines_forward_ca_default, show_default=True,
              help='how to specify the maximun number of lines to forward-search Wikipedia links for each '
                   'category-attribute (when l is specified in wlink). '
                   'f: the number specified in f_wl_lines_forward_max_ca, r: the number estimated using the ratio '
                   'specified by wl_lines_forward_ca_ratio, fr: both f and r (f takes precedence), n: N/A')
@click.option('--f_wl_lines_backward_ca', '-f_wl_bca', type=click.STRING,
              default=cf.DataInfo.f_wl_lines_backward_ca_default, show_default=True,
              help='the file to specify maximum number of line to backward-search Wikipedia links in the page for '
                   'each category-attribute pairs. Notice: The default file contains just one example.')
@click.option('--f_wl_lines_forward_ca', '-f_wl_fca', type=click.STRING,
              default=cf.DataInfo.f_wl_lines_forward_ca_default, show_default=True,
              help='the file to specify maximum number of line to forward-search Wikipedia links in the page for each '
                   'category-attribute pairs. Notice: The default file contains just one example.')
@click.option('--wl_lines_backward_ca_ratio', '-wl_bca_ratio', type=click.FLOAT,
              default=cf.OptInfo.wl_lines_backward_ca_ratio_default, show_default=True,
              help='maximum ratio of lines to backward-search wikipedia links in the page; the number of candidate'
                   'lines are estimated for each attribute using the sample data')
@click.option('--wl_lines_forward_ca_ratio', '-wl_fca_ratio', type=click.FLOAT,
              default=cf.OptInfo.wl_lines_forward_ca_ratio_default, show_default=True,
              help='maximum ratio of lines to forward-search wikipedia links in the page; the number of candidate'
                   'lines are estimated for each attribute using the sample data')
@click.option('--f_mention_gold_link_dist_info', default=cf.DataInfo.f_mention_gold_link_dist_info_default,
              show_default=True, type=click.STRING, help='f_mention_gold_link_dist_info')
# module: slink
@click.option('--slink_min', '-s_min', type=click.FLOAT,
              default=cf.OptInfo.slink_min_default, show_default=True,
              help='minimum self link ratio of attributes. (0.1-1.0)')
@click.option('--slink_prob', '-s_prb', type=click.Choice(['fixed', 'raw', 'mid', 'f_est', 'm_est', 'r_est']),
              default=cf.OptInfo.slink_prob_default, show_default=True,
              help='slink probability of the category-attribute pairs. '
                   '"fixed": 1.0, '
                   '"raw": ratio based on the sample data, '
                   '"mid": average of fixed and raw, '
                   '"f_est": fixed + estimate ratio for attributes never appeared, '
                   '"r_est": raw + estimate ratio for attributes never appeared, '
                   '"m_est": mid + estimate ratio for attributes never appeared')
@click.option('--f_slink', type=click.STRING,
              default=cf.DataInfo.f_slink_default, show_default=True,
              help='filename of self link ratio file. ')
@click.option('--f_self_link_by_attr_name', type=click.STRING,
              default=cf.DataInfo.f_self_link_by_attr_name_default, show_default=True,
              help='filename of self link by attribute name file. ')
# module: lp
@click.option('--lp_min', '-l_min', type=click.FLOAT,
              default=cf.OptInfo.lp_min_default, show_default=True,
              help='minimum category-attribute-mention link probability in the link prob file (f_link_prob). (0.1-1.0)')
@click.option('--f_link_prob', type=click.STRING,
              default=cf.DataInfo.f_link_prob_default, show_default=True,
              help='filename of link probability info file')
# filtering: incl
@click.option('--incl_max', '-i_max', type=click.INT,
              default=cf.OptInfo.incl_max_default, show_default=True,
              help='maximum number of filtering candidate pages using incoming links')
@click.option('--incl_tgt', '-i_tgt', type=click.STRING,
              default=cf.OptInfo.incl_tgt_default, show_default=True,
              help='target module of incoming link filtering,'
                   'specified as the combination of the following characters'
                   'm: mint, t: tinm, w: wlink, s: slink, l: link_prob, n: N/A')
@click.option('--incl_type', '-i_type', type=click.Choice(['o', 'f', 'a', 'n']),
              default=cf.OptInfo.incl_type_default, show_default=True,
              help='type of incoming link filtering,'
                   'o: ordering by number of incoming links (reciprocal ranking), '
                   'f: filtering (keep the original values unchanged), '
                   'a: adjust value based on ordering by number of incoming links, '
                   'n: N/A')
# filtering: attr
@click.option('--attr_rng_auto_freq_min', '-af_min', type=click.INT,
              default=cf.OptInfo.attr_rng_auto_freq_min_default, show_default=True,
              help='maximum number of range frequencies in the training data')
@click.option('--attr_rng_tgt', '-ar_tgt', type=click.STRING,
              default=cf.OptInfo.attr_rng_tgt_default, show_default=True,
              help='target module of attribute range filtering, specified as the combination of '
                   'the following characters'
                   'm: mint, t: tinm, w: wlink, s: slink, l: link_prob, n: N/A')
@click.option('--f_attr_rng_auto', type=click.STRING,
              default=cf.DataInfo.f_attr_rng_auto_default, show_default=True,
              help='filename of attribute range definition file (auto). The ranges are generated based on statistics of'
                   'sample data.')
@click.option('--f_attr_rng_man', type=click.STRING,
              default=cf.DataInfo.f_attr_rng_man_default, show_default=True,
              help='filename of attribute range definition file (man). The ranges are manually specified using ENEIDs.')
@click.option('--f_attr_rng_merged', type=click.STRING,
              default=cf.DataInfo.f_attr_rng_merged_default, show_default=True,
              help='filename of attribute range definition file (merged). ')
@click.option('--f_enew_info', type=click.STRING,
              default=cf.DataInfo.f_enew_info_default, show_default=True,
              help='filename of enew_info_file.')
@click.option('--attr_na_co', '-anc', type=click.FLOAT,
              default=cf.OptInfo.attr_na_co_default, show_default=True,
              help='attr_na_co (base score (0.1-1.0) for candidate pages which are not given ENEW')
@click.option('--attr_ng_co', '-ang', type=click.FLOAT,
              default=cf.OptInfo.attr_ng_co_default, show_default=True,
              help='attr_ng_co (base score (0.1-1.0) for candidate pages which do not match attribute range')
@click.option('--attr_len', '-al', type=click.Choice(['a', 'r', 'ar', 'am', 'n']),
              default=cf.OptInfo.attr_len_default, show_default=True,
              help='scoring of the ENEID of candidate page on attribute range (eg. matching ratio between ENEIDs of '
                   'candidate pages and that of gold pages),'
                   'n: raw matching ratio,'
                   'a: adjusted matching ratio (adjusted matching ratio to ignore 1st layer of the ENE hierarchy if '
                   'the ENEID begins with 1 (Name)), '
                   'r: raw matching ratio + raw depth (# of layers in the ENE hierarchy) of ENEID of the gold page'
                   '(specified in the attribute range definition file), '
                   'ar: adjusted matching ratio + adjusted depth (adjusted to ignore 1st layer of the ENE hierarchy'
                   'if the ENEID begins with 1 (Name)),'
                   'am: adjusted matching ratio + modified depth (modify the adjusted depth to diminish its influence)')
@click.option('--attr_rng_type', '-art', type=click.Choice(['a', 'm', 'ma', 'am']),
              default=cf.OptInfo.attr_rng_type_default, show_default=True,
              help='attribute range estimation type. '
                   'm: use attribute range definition manually specified'
                   'a: use attribute range definition automatically generated based on sample data'
                   'ma: m + a (m > a) (m is preferred when conflict arises on the ratio),'
                   'am: a + m (a > m) (a is preferred when conflict arises on the ratio)')
# filtering: back_link
@click.option('--back_link_tgt', '-bl_tgt', type=click.STRING,
              default=cf.OptInfo.back_link_tgt_default, show_default=True,
              help='target module of back link filtering,'
                   'specified as the combination of the following characters'
                   'm: mint, t: tinm, w: wlink, s: slink, l: link_prob, n: N/A')
@click.option('--back_link_ng', '-bl_ng', type=click.FLOAT,
              default=cf.OptInfo.back_link_ng_default, show_default=True,
              help='score for not back link')
@click.option('--back_link_ok', '-bl_ok', type=click.FLOAT,
              default=cf.OptInfo.back_link_ok_default, show_default=True,
              help='score for back link')
# filtering: detect_nil
@click.option('--f_linkable_info', type=click.STRING,
              default=cf.DataInfo.f_linkable_info_default, show_default=True,
              help='filename of linkable ratio info file.')
@click.option('--nil_tgt', '-n_tgt', type=click.STRING,
              default=cf.OptInfo.back_link_tgt_default, show_default=True,
              help='target module of nil detection filtering,'
                   'specified as the combination of the following characters'
                   'm: mint, t: tinm, w: wlink, s: slink, l: link_prob, n: N/A')
@click.option('--nil_cond', '-n_cond',
              type=click.Choice([
                  'and_prob_len_desc',
                  'and_prob_or_len_desc',
                  'and_len_or_prob_desc',
                  'and_desc_or_prob_len',
                  'two_of_prob_len_desc',
                  'and_prob_len_desc_cman',
                  'and_prob_cman_or_len_desc',
                  'and_len_cman_or_prob_desc',
                  'and_desc_cman_or_prob_len',
                  'and_cman_two_of_prob_len_desc',
                  'cman',
                  'and_prob_len_desc_nostop',
                  'and_prob_nostop_or_len_desc',
                  'and_len_nostop_or_prob_desc',
                  'and_desc_nostop_or_prob_len',
                  'and_nostop_two_of_prob_len_desc'
              ]),
              default=cf.OptInfo.nil_cond_default, show_default=True,
              help='how to evaluate nil (unlinkable) for each mention using '
                   'prob (estimated linkable ratio for category-attribute pairs based on sample data), '
                   'len(minimum length of mention), '
                   'and desc (descriptiveness of mentions),'
                   'cman (manually created nil cand category attribute pairs), '
                   '(apld) and_prob_len_desc: judge as nil if all conditions (prob, len, desc) are satisfied. '
                   '(apold) and_prob_or_len_desc: judge as nil if prob condition is satisfied and either len condition '
                   'or desc condition is satisfied. '
                   '(alopd) and_len_or_prob_desc: judge as nil if len condition is satisfied and either prob condition '
                   'or desc condition is satisfied. '
                   '(adopl) and_desc_or_prob_len: judge as nil if desc condition is satisfied and either prob '
                   'condition or len condition is satisfied.'
                   '(tpld) two_of_prob_len_desc: judge as nil if at least two of the conditions(prob, len, and desc) '
                   'are satisfied.' 
                   '(apldc) and_prob_len_desc_cman: judge as nil if all conditions (prob, len, desc, cman) are '
                   'satisfied.'
                   '(apcold) and_prob_cman_or_len_desc: judge as nil if prob and cman condition are satisfied and '
                   'either len condition or desc condition is satisfied. '
                   '(alcopd) and_len_cman_or_prob_desc: judge as nil if len condition and cman are satisfied and '
                   'either prob condition or desc condition is satisfied. '
                   '(adcopl) and_desc_cman_or_prob_len: judge as nil if desc condition and cman are satisfied and '
                   'either prob condition or len condition is satisfied.'
                   '(actpld) and_cman_two_of_prob_len_desc: judge as nil if cman is satisfied and at least two of the '
                   'conditions(prob, len, and desc) are satisfied. '
                   '(c) cman'
                   '(apnold) and_prob_nostop_or_len_desc: judge as nil if prob and nostop condition are satisfied and '
                   'either len condition or desc condition is satisfied. '
                   '(alnopd) and_len_nostop_or_prob_desc: judge as nil if len condition and nostop are satisfied and '
                   'either prob condition or desc condition is satisfied. '
                   '(adnopl) and_desc_nostop_or_prob_len: judge as nil if desc condition and nostop are satisfied and '
                   'either prob condition or len condition is satisfied.'
                   '(antpld) and_nostop_two_of_prob_len_desc: judge as nil if nostop is satisfied and at least two of '
                   'the conditions(prob, len, and desc) are satisfied. '
              )
@click.option('--nil_all_freq_min', '-n_af_min', type=click.FLOAT,
              default=cf.OptInfo.nil_all_freq_min_default, show_default=True,
              help='minimum freq of category-attribute to consider category-attribute-mention link probability '
                   'in the link prob file (f_link_prob). (0.1-1.0)')
@click.option('--nil_desc_exception', '-n_exc', type=click.STRING,
              default=cf.OptInfo.nil_desc_exception_default, show_default=True,
              help='a colon-separated exception list of exception of nil -desc- condition. If any of the following is '
                   'specified, desc condition is not evaluated for the corresponding category attribute pairs. '
                   'eg. person_works:company_trade_names'
                   'notice. person_works: (Person:作品)'
                   'company_trade_names: (Company:商品名)'
                   'Specify n (N/A) for no exception.')
@click.option('--nil_cat_attr_max', '-n_max', type=click.FLOAT,
              default=cf.OptInfo.nil_cat_attr_max_default, show_default=True,
              help='maximum ratio of unlinkable category attribute pairs in the sample data. If nil ratio of the '
                   'category-attribute pair of a mention is less than the ratio, the mention might be judged as '
                   'unlinkable. (0.1-1.0)')
@click.option('--len_desc_text_min', '-ld_min', type=click.INT,
              default=cf.OptInfo.len_desc_text_min_default, show_default=True,
              help='minimum length of mention text regarded as descriptive. used for nil detection.')
@click.option('--f_nil_cand_man', type=click.STRING,
              default=cf.DataInfo.f_nil_cand_man_default, show_default=True,
              help='filename of nil cand file (manually created).')
@click.option('--f_nil_stop_attr', type=click.STRING,
              default=cf.DataInfo.f_nil_stop_attr_default, show_default=True,
              help='filename of nil stop attribute file (manually created).')
# ljc_main
def ljc_main(common_data_dir,
             tmp_data_dir,
             in_dir,
             sample_gold_dir,
             sample_input_dir,
             out_dir,
             ans_max,
             attr_na_co,
             attr_ng_co,
             attr_len,
             attr_rng_auto_freq_min,
             attr_rng_tgt,
             attr_rng_type,
             back_link_tgt,
             back_link_ng,
             back_link_ok,
             char_match_cand_num_max,
             f_all_cat_info,
             f_attr_rng_auto,
             f_attr_rng_man,
             f_attr_rng_merged,
             f_enew_info,
             f_html_info,
             f_mention_gold_link_dist_info,
             f_mint,
             f_mint_trim,
             f_nil_cand_man,
             f_nil_stop_attr,
             f_slink,
             f_self_link_by_attr_name,
             f_wl_lines_backward_ca,
             f_wl_lines_forward_ca,
             f_linkable_info,
             f_link_prob,
             f_target_attr_info,
             f_tinm,
             f_tinm_trim,
             f_title2pid_ext,
             filtering,
             incl_max,
             incl_tgt,
             incl_type,
             len_desc_text_min,
             nil_all_freq_min,
             lp_min,
             mint,
             mint_min,
             mod,
             mod_w,
             multi_lang,
             nil_cat_attr_max,
             nil_cond,
             nil_desc_exception,
             nil_tgt,
             score_type,
             slink_min,
             slink_prob,
             tinm,
             tinm_min,
             title_matching_mint,
             title_matching_tinm,
             wlink,
             wl_break,
             wl_lines_backward_max,
             wl_lines_forward_max,
             wl_lines_backward_ca,
             wl_lines_forward_ca,
             wl_lines_backward_ca_ratio,
             wl_lines_forward_ca_ratio,
             wl_score_same,
             wl_score_backward,
             wl_score_forward,
             wr_score,
             wp_score,
             wf_score):
    """
    :param common_data_dir: common data files directory
    :param tmp_data_dir: directory for data specifically used for the test data
    :param in_dir: input directory
    :param sample_gold_dir
    :param sample_input_dir
    :param out_dir: output directory
    :param ans_max:
    :param attr_na_co:
    :param attr_ng_co:
    :param attr_len:
    :param attr_rng_auto_freq_min:
    :param attr_rng_type:
    :param attr_rng_tgt:
    :param back_link_tgt:
    :param back_link_ng:
    :param back_link_ok:
    :param char_match_cand_num_max:
    :param f_all_cat_info:
    :param f_attr_rng_auto:
    :param f_attr_rng_man:
    :param f_attr_rng_merged:
    :param f_enew_info:
    :param f_html_info:
    :param f_mention_gold_link_dist_info:
    :param f_mint:
    :param f_mint_trim:
    :param f_nil_cand_man:
    :param f_nil_stop_attr:
    :param f_slink:
    :param f_self_link_by_attr_name:
    :param f_wl_lines_backward_ca:
    :param f_wl_lines_forward_ca:
    :param f_linkable_info:
    :param f_link_prob:
    :param f_target_attr_info:
    :param f_tinm:
    :param f_tinm_trim:
    :param f_title2pid_ext:
    :param filtering:
    :param incl_max:
    :param incl_tgt:
    :param incl_type:
    :param len_desc_text_min:
    :param nil_all_freq_min:
    :param lp_min:
    :param mint:
    :param mint_min:
    :param mod:
    :param mod_w:
    :param multi_lang:
    :param nil_cat_attr_max:
    :param nil_cond:
    :param nil_desc_exception:
    :param nil_tgt:
    :param score_type:
    :param slink_min:
    :param slink_prob:
    :param tinm:
    :param tinm_min:
    :param title_matching_mint:
    :param title_matching_tinm:
    :param wlink:
    :param wl_break:
    :param wl_lines_backward_max:
    :param wl_lines_forward_max:
    :param wl_lines_backward_ca:
    :param wl_lines_forward_ca:
    :param wl_lines_backward_ca_ratio:
    :param wl_lines_forward_ca_ratio:
    :param wl_score_same:
    :param wl_score_backward:
    :param wl_score_forward:
    :param wr_score:
    :param wp_score:
    :param wf_score:
    :return:
    """

    log_info = cf.LogInfo()
    logger = set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)

    opt_info = cf.OptInfo()
    opt_info.mod = mod
    opt_info.filtering = filtering
    opt_info.attr_rng_auto_freq_min = attr_rng_auto_freq_min
    opt_info.attr_rng_tgt = attr_rng_tgt
    opt_info.attr_rng_type = attr_rng_type
    opt_info.incoming_link_tgt = incl_tgt
    opt_info.back_link_tgt = back_link_tgt
    opt_info.back_link_ng = back_link_ng
    opt_info.back_link_ok = back_link_ok
    opt_info.mod_w = mod_w
    opt_info.ans_max = ans_max
    opt_info.title_matching_mint = title_matching_mint
    opt_info.title_matching_tinm = title_matching_tinm
    opt_info.char_match_cand_num_max = char_match_cand_num_max
    opt_info.len_desc_text_min = len_desc_text_min
    opt_info.nil_cat_attr_max = nil_cat_attr_max
    opt_info.nil_cond = nil_cond
    opt_info.nil_desc_exception = nil_desc_exception
    opt_info.nil_tgt = nil_tgt
    opt_info.mention_in_title = mint
    opt_info.mention_in_title_min = mint_min
    opt_info.multi_lang = multi_lang
    opt_info.wikilink = wlink
    opt_info.title_in_mention = tinm
    opt_info.title_in_mention_min = tinm_min
    opt_info.incoming_link_max = incl_max
    opt_info.incoming_link_type = incl_type
    opt_info.attr_len = attr_len
    opt_info.attr_na_co = attr_na_co
    opt_info.attr_ng_co = attr_ng_co
    opt_info.score_type = score_type
    opt_info.slink_min = slink_min
    opt_info.slink_prob = slink_prob
    opt_info.nil_all_freq_min = nil_all_freq_min
    opt_info.link_prob_min = lp_min
    opt_info.wl_break = wl_break
    opt_info.wl_lines_backward_ca = wl_lines_backward_ca
    opt_info.wl_lines_forward_ca = wl_lines_forward_ca
    opt_info.wl_lines_backward_ca_ratio = wl_lines_backward_ca_ratio
    opt_info.wl_lines_forward_ca_ratio = wl_lines_forward_ca_ratio
    opt_info.wl_lines_backward_max = wl_lines_backward_max
    opt_info.wl_lines_forward_max = wl_lines_forward_max
    opt_info.wl_score_same = wl_score_same
    opt_info.wl_score_backward = wl_score_backward
    opt_info.wl_score_forward = wl_score_forward
    opt_info.wp_score = wp_score
    opt_info.wr_score = wr_score
    opt_info.wf_score = wf_score
    logger.info({
        'action': 'ljc_main',
        'setting': 'opt_info',
        'mod': opt_info.mod,
        'filtering': opt_info.filtering,
        'mod_w': opt_info.mod_w,
        'ans_max': opt_info.ans_max,
        'score_type': opt_info.score_type,
    })
    logger.info({
        'char_match_cand_num_max': opt_info.char_match_cand_num_max,
        'mint': opt_info.mention_in_title,
        'mint_min': opt_info.mention_in_title_min,
        'tinm': opt_info.title_in_mention,
        'tinm_min': opt_info.title_in_mention_min
    })
    logger.info({
        'slink_prob': opt_info.slink_prob,
    })
    logger.info({
        'wlink': opt_info.wikilink,
        'wl_break': opt_info.wl_break,
        'wl_lines_backward_max': opt_info.wl_lines_backward_max,
        'wl_lines_forward_max': opt_info.wl_lines_forward_max,
        'wl_score_same': opt_info.wl_score_same,
        'wl_score_backward': opt_info.wl_score_backward,
        'wl_score_forward': opt_info.wl_score_forward,
        'wp_score': opt_info.wp_score,
        'wr_score': opt_info.wr_score,
        'wf_score': opt_info.wf_score
    })
    logger.info({
        'incl_max': opt_info.incoming_link_max,
        'incl_type': opt_info.incoming_link_type,
    })
    logger.info({
        'attr_len': opt_info.attr_len,
        'attr_rng_auto_freq_min': attr_rng_auto_freq_min,
        'attr_na_co': opt_info.attr_na_co,
        'attr_ng_co': opt_info.attr_ng_co,
    })
    logger.info({
        'back_link_ng': opt_info.back_link_ng,
    })

    data_info = cf.DataInfo(common_data_dir, tmp_data_dir, in_dir, sample_gold_dir, sample_input_dir, out_dir)

    data_info.common_data_dir = common_data_dir
    data_info.all_cat_info_file = data_info.common_data_dir + f_all_cat_info
    data_info.attr_rng_auto_file = data_info.common_data_dir + f_attr_rng_auto
    data_info.attr_rng_man_file = data_info.common_data_dir + f_attr_rng_man
    data_info.attr_rng_merged_file = data_info.common_data_dir + f_attr_rng_merged
    data_info.enew_info_file = data_info.common_data_dir + f_enew_info
    data_info.linkable_info_file = data_info.common_data_dir + f_linkable_info
    data_info.link_prob_file = data_info.common_data_dir + f_link_prob
    data_info.mention_gold_link_dist_info_file = data_info.common_data_dir + f_mention_gold_link_dist_info
    data_info.nil_cand_man_file = data_info.common_data_dir + f_nil_cand_man
    data_info.nil_stop_attr_file = data_info.common_data_dir + f_nil_stop_attr
    data_info.slink_file = data_info.common_data_dir + f_slink
    data_info.self_link_by_attr_name_file = data_info.common_data_dir + f_self_link_by_attr_name
    data_info.target_attr_info_file = data_info.common_data_dir + f_target_attr_info
    data_info.title2pid_ext_file = data_info.common_data_dir + f_title2pid_ext

    data_info.tmp_data_dir = tmp_data_dir
    data_info.in_dir = in_dir
    data_info.out_dir = out_dir
    data_info.html_info_file = data_info.tmp_data_dir + f_html_info
    data_info.mint_partial_match_file = data_info.tmp_data_dir + f_mint
    data_info.mint_trim_partial_match_file = data_info.tmp_data_dir + f_mint_trim
    data_info.tinm_partial_match_file = data_info.tmp_data_dir + f_tinm
    data_info.tinm_trim_partial_match_file = data_info.tmp_data_dir + f_tinm_trim

    data_info.in_ene_dir = in_dir + 'ene_annotation/'

    logger.info({
        'common_data_dir': data_info.common_data_dir,
        'tmp_data_dir': data_info.tmp_data_dir,
        'in_dir': data_info.in_dir,
        'in_ene_dir': data_info.in_ene_dir,
        'out_dir': data_info.out_dir,
        'title2pid_ext_file': data_info.title2pid_ext_file,
    })

    if not os.path.isdir(data_info.common_data_dir):
        logger.error({
            'msg': 'illegal common_data_dir',
            'common_data_dir': data_info.common_data_dir,
        })

    if not os.path.isdir(data_info.in_dir):
        logger.error({
            'msg': 'illegal in_dir',
            'in_dir': data_info.in_dir,
        })
        sys.exit()
    if not os.path.isdir(data_info.in_ene_dir):
        logger.error({
            'msg': 'illegal in_ene_dir',
            'in_ene_dir': data_info.in_ene_dir,
        })
        sys.exit()

    in_files = data_info.in_ene_dir + '*.jsonl'
    os.makedirs(out_dir, exist_ok=True)

    logger.info({
        'action': 'ljc_main',
        'in_ene_dir': data_info.in_ene_dir,
        'in_files': in_files,
        'out_dir': out_dir,
    })
    (cf.d_title2pid, cf.d_pid_title_incoming_eneid) = lc.reg_title2pid_ext(data_info.title2pid_ext_file, log_info)

    d_mint_mention_pid_ratio = {}
    d_tinm_mention_pid_ratio = {}
    d_cat_attr2eneid_prob = {}
    d_self_link = {}
    d_link_prob = {}
    d_back_link = {}
    diff_info = {}
    d_linkable = {}
    d_nil_cand_man = {}
    d_nil_stop_attr = {}

    d_eneid2enlabel = {}
    d_eneid2enlabel = lc.reg_all_cat_info(data_info.all_cat_info_file, log_info)

    # mint
    if (opt_info.mention_in_title == 'e' or opt_info.mention_in_title == 'p') and 'm' not in opt_info.mod:
        logger.error({
            'action': 'ljc_main',
            'error': 'mod m should be specified'
        })
        sys.exit()
    elif (opt_info.title_matching_mint == 'trim') and 'm' not in opt_info.mod:
        logger.error({
            'action': 'ljc_main',
            'error': 'mod m should be specified (trim, non-default)'
        })
        sys.exit()

    elif 'm' in opt_info.mod:
        if opt_info.mention_in_title != 'e' and opt_info.mention_in_title != 'p':
            logger.error({
                'action': 'ljc_main',
                'missing or illegal mint value': opt_info.mention_in_title
            })
            sys.exit()

        elif not opt_info.title_matching_mint:
            logger.error({
                'action': 'ljc_main',
                'missing title matching mint': 'Specify title matching as option (--title matching mint / -tmm)'
            })
            sys.exit()
        else:
            if opt_info.title_matching_mint == 'trim':
                logger.info({
                    'action': 'ljc_main',
                    'run': 'reg_matching_info',
                    'title_matching_mint': opt_info.title_matching_mint,
                    'partial_match_file': data_info.mint_trim_partial_match_file,
                    'mention_in_title_min': opt_info.mention_in_title_min
                })
                d_mint_mention_pid_ratio = mc.reg_matching_info(
                    data_info.mint_trim_partial_match_file,
                    opt_info.mention_in_title_min,
                    opt_info.multi_lang,
                    log_info)

            elif opt_info.title_matching_mint == 'full':
                logger.info({
                    'action': 'ljc_main',
                    'run': 'reg_matching_info',
                    'title_matching_mint': opt_info.title_matching_mint,
                    'partial_match_file': data_info.mint_partial_match_file,
                    'mention_in_title_min': opt_info.mention_in_title_min
                })
                d_mint_mention_pid_ratio = mc.reg_matching_info(
                    data_info.mint_partial_match_file,
                    opt_info.mention_in_title_min,
                    opt_info.multi_lang,
                    log_info)

            else:
                logger.error({
                    'action': 'ljc_main',
                    'error': 'illegal title_matching_mint value'
                })
                sys.exit()
    # tinm
    if (opt_info.title_in_mention == 'e' or opt_info.title_in_mention == 'p') and 't' not in opt_info.mod:
        logger.error({
            'action': 'ljc_main',
            'error': 'mod t should be specified'
        })
        sys.exit()
    elif (opt_info.title_matching_tinm == 'trim') and 't' not in opt_info.mod:
        logger.error({
            'action': 'ljc_main',
            'error': 'mod t should be specified (trim, non-default)'
        })
        sys.exit()
    elif 't' in opt_info.mod:
        if opt_info.title_in_mention != 'e' and opt_info.title_in_mention != 'p':
            logger.error({
                'action': 'ljc_main',
                'missing or illegal tinm value': opt_info.title_in_mention_min
            })
            sys.exit()
        elif not opt_info.title_matching_tinm:
            logger.error({
                'action': 'ljc_main',
                'missing title matching trim': 'Specify title matching as option (--title matching trim/ -tmt)'
            })
            sys.exit()
        else:
            if opt_info.title_matching_tinm == 'trim':
                logger.info({
                    'action': 'ljc_main',
                    'run': 'mc.reg_matching_info',
                    'title_matching_tinm': opt_info.title_matching_tinm,
                    'partial_match_file': data_info.tinm_trim_partial_match_file,
                    'mention_in_title_min': opt_info.title_in_mention_min
                })
                d_tinm_mention_pid_ratio = mc.reg_matching_info(
                    data_info.tinm_trim_partial_match_file,
                    opt_info.title_in_mention_min,
                    opt_info.multi_lang,
                    log_info)

            elif opt_info.title_matching_tinm == 'full':
                logger.info({
                    'action': 'ljc_main',
                    'run': 'mc.reg_matching_info',
                    'title_matching_tinm': opt_info.title_matching_tinm,
                    'partial_match_file': data_info.tinm_partial_match_file,
                    'mention_in_title_min': opt_info.title_in_mention_min
                })
                d_tinm_mention_pid_ratio = mc.reg_matching_info(
                    data_info.tinm_partial_match_file,
                    opt_info.title_in_mention_min,
                    opt_info.multi_lang,
                    log_info)
            else:
                logger.error({
                    'action': 'ljc_main',
                    'error': 'illegal title_matching_tinm value'
                })
                sys.exit()
    # wikilink
    if ('r' in opt_info.wikilink
            or 'f' in opt_info.wikilink
            or 'm' in opt_info.wikilink
            or 'p' in opt_info.wikilink
            or 'l' in opt_info.wikilink) and 'w' not in opt_info.mod:
        logger.error({
            'action': 'ljc_main',
            'error': 'mod w should be specified'
        })
        sys.exit()
    elif 'w' in opt_info.mod:
        if ('r' not in opt_info.wikilink
                and 'f' not in opt_info.wikilink
                and 'm' not in opt_info.wikilink
                and 'p' not in opt_info.wikilink
                and 'l' not in opt_info.wikilink):
            logger.error({
                'action': 'ljc_main',
                'illegal wlink value': opt_info.wikilink
            })
            sys.exit()
        else:
            logger.info({
                'action': 'ljc_main',
                'run': 'gw.reg_tag_info',
                'wikilink': opt_info.wikilink,
                'html_info_file': data_info.html_info_file,
            })
        cf.d_tag_info = gw.reg_tag_info(data_info.html_info_file, log_info)

        if 'r' in opt_info.wl_lines_backward_ca or 'r' in opt_info.wl_lines_forward_ca:
            logger.info({
                'action': 'ljc_main',
                'run': 'gw.reg_mention_gold_distance',
                'dist_file': data_info.mention_gold_link_dist_file,
                'dist_info_file': data_info.mention_gold_link_dist_info_file
            })

            diff_info = gw.reg_mention_gold_distance(data_info.mention_gold_link_dist_file, opt_info,
                                                     data_info.mention_gold_link_dist_info_file, log_info)

        if 'f' in opt_info.wl_lines_backward_ca:
            data_info.wl_lines_backward_ca_file = data_info.common_data_dir + f_wl_lines_backward_ca
            if not os.path.isfile(data_info.wl_lines_backward_ca_file):
                logger.error({
                    'action': 'ljc_main',
                    'error': 'file not found',
                    'file': data_info.wl_lines_backward_ca_file
                })
            cf.diff_info_ca_backward = gw.reg_mention_gold_distance_ca(data_info.wl_lines_backward_ca_file, log_info)
        if 'f' in opt_info.wl_lines_forward_ca:
            data_info.wl_lines_forward_ca_file = data_info.common_data_dir + f_wl_lines_forward_ca
            if not os.path.isfile(data_info.wl_lines_forward_ca_file):
                logger.error({
                    'action': 'ljc_main',
                    'error': 'file not found',
                    'file': data_info.wl_lines_forward_ca_file
                })
            cf.diff_info_ca_forward = gw.reg_mention_gold_distance_ca(data_info.wl_lines_forward_ca_file, log_info)
    # slink
    if 's' in opt_info.mod:
        if not opt_info.slink_prob:
            logger.error({
                'action': 'ljc_main',
                'msg': 'missing slink_prob',
                'mod': opt_info.mod
            })
            sys.exit()

        logger.info({
            'action': 'ljc_main',
            'run': 'sl.check_slink_info',
            'slink_min': opt_info.slink_min,
            'slink_file': data_info.slink_file,
        })
        d_self_link = sl.check_slink_info(data_info.slink_file, log_info)

    # link_prob
    if 'l' in opt_info.mod:
        logger.info({
            'action': 'ljc_main',
            'run': 'lp.get_link_prob_info',
            'link_prob_min': opt_info.link_prob_min,
            'link_prob_file': data_info.link_prob_file
        })
        d_link_prob = lp.get_link_prob_info(data_info.link_prob_file, opt_info.link_prob_min, log_info)

    # incoming_link
    if ('m' in opt_info.incoming_link_tgt or
        't' in opt_info.incoming_link_tgt or
        'w' in opt_info.incoming_link_tgt or
        's' in opt_info.incoming_link_tgt or
        'l' in opt_info.incoming_link_tgt) \
            and 'i' not in opt_info.filtering:
        logger.error({
            'action': 'ljc_main',
            'incl_target': 'missing filtering option (i)'
        })
        sys.exit()

    elif ('o' in opt_info.incoming_link_type or
          'f' in opt_info.incoming_link_type or
          'a' in opt_info.incoming_link_type) \
            and 'i' not in opt_info.filtering:
        logger.error({
            'action': 'ljc_main',
            'backlink': 'missing filtering option (i)'
        })
        sys.exit()
    elif 'i' in opt_info.filtering:
        if not opt_info.incoming_link_tgt:
            logger.error({
                'action': 'ljc_main',
                'filterning': opt_info.filtering,
                'missing incoming_link_tgt': 'opt_info.incoming_link_tgt should be specified'
            })
            sys.exit()
        elif ('m' not in opt_info.incoming_link_tgt and
              't' not in opt_info.incoming_link_tgt and
              'w' not in opt_info.incoming_link_tgt and
              's' not in opt_info.incoming_link_tgt and
              'l' not in opt_info.incoming_link_tgt):
            logger.error({
                'action': 'ljc_main',
                'filtering': opt_info.filtering,
                'illegal incoming_link_tgt': 'illegal opt_info.incoming_link_tgt'
            })
            sys.exit()
        elif ('o' not in opt_info.incoming_link_type and
              'f' not in opt_info.incoming_link_type and
              'a' not in opt_info.incoming_link_type):
            logger.error({
                'action': 'ljc_main',
                'filtering': opt_info.filtering,
                'missing incoming_link_type': 'opt_info.incoming_link_type should be specified'
            })
            sys.exit()
        else:
            logger.info({
                'action': 'ljc_main',
                'filtering': opt_info.filtering,
                'incoming_link_tgt': opt_info.incoming_link_tgt,
                'incoming_link_max': opt_info.incoming_link_max,
            })

    # back_link
    if ('m' in opt_info.back_link_tgt or
        't' in opt_info.back_link_tgt or
        'w' in opt_info.back_link_tgt or
        's' in opt_info.back_link_tgt or
        'l' in opt_info.back_link_tgt) \
            and 'b' not in opt_info.filtering:
        logger.error({
            'action': 'ljc_main',
            'backlink': 'missing filtering option (back link tgt is specified)'
        })
        sys.exit()

    elif 'b' in opt_info.filtering:
        if not opt_info.back_link_tgt:
            logger.error({
                'action': 'ljc_main',
                'filtering': opt_info.filtering,
                'missing back_link_tgt': 'opt_info.back_link_tgt should be specified'
            })
            sys.exit()
        elif ('m' not in opt_info.back_link_tgt and
              't' not in opt_info.back_link_tgt and
              'w' not in opt_info.back_link_tgt and
              's' not in opt_info.back_link_tgt and
              'l' not in opt_info.back_link_tgt):
            logger.error({
                'action': 'ljc_main',
                'filtering': opt_info.filtering,
                'illegal backlink_tgt': 'illegal opt_info.back_link_tgt'
            })
            sys.exit()
        else:
            logger.info({
                'action': 'ljc_main',
                'filtering': opt_info.filtering,
                'back_link_tgt': opt_info.back_link_tgt
            })
            data_info.back_link_file = tmp_data_dir + cf.DataInfo.f_back_link_default
            d_back_link = bl.check_back_link_info(data_info.back_link_file, log_info, **cf.d_title2pid)

    # attr_range
    if ('m' in opt_info.attr_rng_tgt or
        't' in opt_info.attr_rng_tgt or
        'w' in opt_info.attr_rng_tgt or
        's' in opt_info.attr_rng_tgt or
        'l' in opt_info.attr_rng_tgt) \
            and 'a' not in opt_info.filtering:
        logger.error({
            'action': 'ljc_main',
            'option combination error': 'attr_rng_tgt is set, but missing filtering option a'
        })
        sys.exit()
    elif 'a' in opt_info.filtering:
        if not opt_info.attr_rng_tgt:
            logger.error({
                'action': 'ljc_main',
                'msg': 'missing attr_rng_tgt'
            })
            sys.exit()
        elif not opt_info.attr_rng_type:
            logger.error({
                'action': 'ljc_main',
                'msg': 'missing attr_rng_type'
            })
            sys.exit()
        else:
            logger.info({
                'action': 'ljc_main',
                'attr_rng_tgt': opt_info.attr_rng_tgt,
                'attr_rng_type': opt_info.attr_rng_type,
                'enew_info_file:': data_info.enew_info_file,
            })
            d_cat_attr2eneid_prob = ar.get_attr_range(data_info.attr_rng_man_file,
                                                      data_info.attr_rng_auto_file,
                                                      data_info.attr_rng_merged_file,
                                                      opt_info,
                                                      log_info,
                                                      **d_eneid2enlabel)

    # nil_detection
    if ('m' in opt_info.nil_tgt or
        't' in opt_info.nil_tgt or
        'w' in opt_info.nil_tgt or
        's' in opt_info.nil_tgt or
        'l' in opt_info.nil_tgt) \
            and 'n' not in opt_info.filtering:
        logger.error({
            'action': 'ljc_main',
            'option combination error': 'nil_tgt is set, but missing filtering option n'
        })
        sys.exit()

    elif 'n' in opt_info.filtering:
        if not opt_info.nil_tgt:
            logger.error({
                'action': 'ljc_main',
                'missing nil_tgt': 'nil detection is specified, but missing nil_tgt'
            })
            sys.exit()
        elif ('m' not in opt_info.nil_tgt and
              't' not in opt_info.nil_tgt and
              'w' not in opt_info.nil_tgt and
              's' not in opt_info.nil_tgt and
              'l' not in opt_info.nil_tgt):
            logger.error({
                'action': 'ljc_main',
                'illegal nil_tgt': 'nil detection is specified, but illegal nil_tgt'
            })
            sys.exit()
        elif (
            opt_info.nil_cond != 'and_prob_len_desc' and
            opt_info.nil_cond != 'and_prob_or_len_desc' and
            opt_info.nil_cond != 'and_len_or_prob_desc' and
            opt_info.nil_cond != 'and_desc_or_prob_len' and
            opt_info.nil_cond != 'two_of_prob_len_desc' and
            opt_info.nil_cond != 'and_prob_len_desc_cman' and
            opt_info.nil_cond != 'and_prob_cman_or_len_desc' and
            opt_info.nil_cond != 'and_len_cman_or_prob_desc' and
            opt_info.nil_cond != 'and_desc_cman_or_prob_len' and
            opt_info.nil_cond != 'and_cman_two_of_prob_len_desc' and
            opt_info.nil_cond != 'cman' and
            opt_info.nil_cond != 'and_prob_len_desc_nostop' and
            opt_info.nil_cond != 'and_prob_nostop_or_len_desc' and
            opt_info.nil_cond != 'and_len_nostop_or_prob_desc' and
            opt_info.nil_cond != 'and_desc_nostop_or_prob_len' and
            opt_info.nil_cond != 'and_nostop_two_of_prob_len_desc'
        ):
            logger.error({
                'action': 'ljc_main',
                'illegal nil_cond': 'nil detection is specified, but illegal nil_cond'
            })
            sys.exit()
        elif opt_info.nil_desc_exception != 'n':
            if '_' not in opt_info.nil_desc_exception:
                logger.error({
                    'action': 'ljc_main',
                    'illegal nil_desc_exception': 'nil detection is specified, but illegal nil_desc_exception'
                })
                sys.exit()
        elif opt_info.nil_cat_attr_max > 1.0:
            logger.error({
                'action': 'ljc_main',
                'illegal nil_cat_attr_max': 'nil detection is specified, but illegal nil_cat_attr_max'
            })
            sys.exit()
        elif opt_info.len_desc_text_min < 0:
            logger.error({
                'action': 'ljc_main',
                'illegal len_desc_text_min': 'nil detection is specified, but illegal len_desc_text_min'
            })
            sys.exit()

        logger.info({
            'action': 'ljc_main',
            'run': 'dn.check_linkable_info',
            'nil_tgt': opt_info.nil_tgt,
            'nil_cond': opt_info.nil_cond,
            'nil_desc_exception': opt_info.nil_desc_exception,
            'linkable_file': data_info.linkable_info_file,
        })
        d_linkable = dn.check_linkable_info(data_info.linkable_info_file, log_info)
        d_nil_cand_man = dn.reg_nil_cand_man(data_info.nil_cand_man_file, log_info)
        d_nil_stop_attr = dn.reg_nil_cand_man(data_info.nil_stop_attr_file, log_info)

    logger.info({
        'action': 'ljc_main',
        'in_files': in_files,
    })

    for in_file in glob(in_files):

        list_rec_out = []
        logger.info({
            'action': 'ljc_main',
            'in_file': in_file,
        })
        if 'for_view' in in_file:
            logger.info({
                'action': 'ljc_main',
                'msg': 'skipped for_view',
                'in_file': in_file
            })
            continue
        with open(in_file, mode='r', encoding='utf-8') as i:

            fname = in_file.replace(data_info.in_ene_dir, '')

            outfile_pre = out_dir + fname
            if '_dist' in fname:
                outfile = outfile_pre.replace('_dist', '')
            else:
                outfile = outfile_pre
            out_tsv = outfile.replace('.jsonl', '.tsv')

            for i_line in i:
                rec = json.loads(i_line)

                link_info = cf.LinkInfo('linfo')

                mention_info = cf.MentionInfo(
                    rec['page_id'],
                    '',
                    rec['attribute'],
                    rec['text_offset']['start']['line_id'],
                    rec['text_offset']['start']['offset'],
                    rec['text_offset']['end']['line_id'],
                    rec['text_offset']['end']['offset'],
                    rec['text_offset']['text'],
                    rec['html_offset']['start']['line_id'],
                    rec['html_offset']['start']['offset'],
                    rec['html_offset']['end']['line_id'],
                    rec['html_offset']['end']['offset'],
                    rec['html_offset']['text'],
                    ''
                )

                if rec['ENE'] in d_eneid2enlabel:
                    mention_info.ene_cat = d_eneid2enlabel[rec['ENE']]

                mod_info = cf.ModInfo()
                cat_attr = mention_info.ene_cat + ':' + mention_info.attr_label

                # modules (+ filtering)
                # wlink
                if 'w' in opt_info.mod:
                    wlink_cand_list = []
                    if 'n' in opt_info.filtering and 'w' in opt_info.nil_tgt:
                        # nil detection
                        cand_man_res = dn.check_cand_man(cat_attr, log_info, **d_nil_cand_man)
                        stop_attr_res = dn.check_nil_stop(mention_info.attr_label, log_info, **d_nil_stop_attr)

                        dn_res = dn.estimate_nil(
                            cat_attr, cand_man_res, stop_attr_res, mention_info, opt_info, log_info, **d_linkable)
                        if not dn_res:
                            wlink_cand_list = gw.check_wlink(mention_info, opt_info, log_info, **diff_info)
                    else:
                        wlink_cand_list = gw.check_wlink(mention_info, opt_info, log_info, **diff_info)

                    # filtering
                    if len(wlink_cand_list) > 0:
                        w_tmp_cand_list = copy.deepcopy(wlink_cand_list)

                        if 'a' in opt_info.filtering and 'w' in opt_info.attr_rng_tgt:
                            wlink_cand_list_attr_checked = ar.filter_by_attr_range(w_tmp_cand_list,
                                                                                   mention_info,
                                                                                   opt_info,
                                                                                   log_info,
                                                                                   **d_cat_attr2eneid_prob)
                            w_tmp_cand_list = copy.deepcopy(wlink_cand_list_attr_checked)
                        if 'i' in opt_info.filtering and 'w' in opt_info.incoming_link_tgt:
                            wlink_cand_list_incl_checked = il.filter_by_incoming_link(w_tmp_cand_list,
                                                                                      mention_info,
                                                                                      opt_info.incoming_link_max,
                                                                                      opt_info.incoming_link_type,
                                                                                      log_info,
                                                                                      **cf.d_pid_title_incoming_eneid)
                            w_tmp_cand_list = copy.deepcopy(wlink_cand_list_incl_checked)
                        if 'b' in opt_info.filtering and 'w' in opt_info.back_link_tgt:
                            wlink_cand_list_back_link_checked = bl.filter_by_back_link(w_tmp_cand_list,
                                                                                       opt_info,
                                                                                       mention_info,
                                                                                       log_info,
                                                                                       **d_back_link)
                            w_tmp_cand_list = copy.deepcopy(wlink_cand_list_back_link_checked)

                        # filtered candidates
                        if w_tmp_cand_list:
                            cl.append_filtering_cand_info(w_tmp_cand_list, link_info, log_info)

                # slink
                if 's' in opt_info.mod:
                    slink_cand_list = []
                    if 'n' in opt_info.filtering and 's' in opt_info.nil_tgt:
                        # nil detection
                        cand_man_res = dn.check_cand_man(cat_attr, log_info, **d_nil_cand_man)
                        stop_attr_res = dn.check_nil_stop(mention_info.attr_label, log_info, **d_nil_stop_attr)

                        dn_res = dn.estimate_nil(
                            cat_attr, cand_man_res, stop_attr_res, mention_info, opt_info, log_info, **d_linkable)

                        if not dn_res:
                            slink_cand_list = sl.estimate_self_link(cat_attr, opt_info.slink_prob, mention_info,
                                                                    opt_info.slink_min,
                                                                    data_info.self_link_by_attr_name_file,
                                                                    log_info, **d_self_link)
                    else:
                        slink_cand_list = sl.estimate_self_link(cat_attr, opt_info.slink_prob, mention_info,
                                                                opt_info.slink_min,
                                                                data_info.self_link_by_attr_name_file,
                                                                log_info, **d_self_link)

                    # filtering
                    if len(slink_cand_list) > 0:
                        s_tmp_cand_list = copy.deepcopy(slink_cand_list)

                        if 'a' in opt_info.filtering and 's' in opt_info.attr_rng_tgt:
                            slink_cand_list_attr_checked = ar.filter_by_attr_range(s_tmp_cand_list,
                                                                                   mention_info,
                                                                                   opt_info,
                                                                                   log_info,
                                                                                   **d_cat_attr2eneid_prob)
                            s_tmp_cand_list = copy.deepcopy(slink_cand_list_attr_checked)
                        if 'i' in opt_info.filtering and 's' in opt_info.incoming_link_tgt:
                            slink_cand_list_incl_checked = il.filter_by_incoming_link(s_tmp_cand_list,
                                                                                      mention_info,
                                                                                      opt_info.incoming_link_max,
                                                                                      opt_info.incoming_link_type,
                                                                                      log_info,
                                                                                      **cf.d_pid_title_incoming_eneid)
                            s_tmp_cand_list = copy.deepcopy(slink_cand_list_incl_checked)

                        if 'b' in opt_info.filtering and 's' in opt_info.back_link_tgt:
                            slink_cand_list_back_link_checked = bl.filter_by_back_link(s_tmp_cand_list,
                                                                                       opt_info,
                                                                                       mention_info,
                                                                                       log_info,
                                                                                       **d_back_link)
                            s_tmp_cand_list = copy.deepcopy(slink_cand_list_back_link_checked)

                        # filtered candidates
                        if s_tmp_cand_list:
                            cl.append_filtering_cand_info(s_tmp_cand_list, link_info, log_info)
                # mint
                if 'm' in opt_info.mod:
                    mint_cand_list = []
                    mod = 'm'

                    if 'n' in opt_info.filtering and 'm' in opt_info.nil_tgt:
                        # nil detection
                        cand_man_res = dn.check_cand_man(cat_attr, log_info, **d_nil_cand_man)
                        stop_attr_res = dn.check_nil_stop(mention_info.attr_label, log_info, **d_nil_stop_attr)

                        dn_res = dn.estimate_nil(
                            cat_attr, cand_man_res, stop_attr_res, mention_info, opt_info, log_info, **d_linkable)
                        if not dn_res:
                            mint_cand_list = mc.match_mention_title(mod, opt_info, mention_info.t_mention, log_info,
                                                                    **d_mint_mention_pid_ratio)
                    else:
                        mint_cand_list = mc.match_mention_title(mod, opt_info, mention_info.t_mention, log_info,
                                                                **d_mint_mention_pid_ratio)

                    # filtering
                    if len(mint_cand_list) > 0:
                        m_tmp_cand_list = copy.deepcopy(mint_cand_list)

                        if 'a' in opt_info.filtering and 'm' in opt_info.attr_rng_tgt:
                            mint_cand_list_attr_checked = ar.filter_by_attr_range(m_tmp_cand_list,
                                                                                  mention_info,
                                                                                  opt_info,
                                                                                  log_info,
                                                                                  **d_cat_attr2eneid_prob)
                            m_tmp_cand_list = copy.deepcopy(mint_cand_list_attr_checked)
                        if 'i' in opt_info.filtering and 'm' in opt_info.incoming_link_tgt:
                            mint_cand_list_incl_checked = il.filter_by_incoming_link(m_tmp_cand_list,
                                                                                     mention_info,
                                                                                     opt_info.incoming_link_max,
                                                                                     opt_info.incoming_link_type,
                                                                                     log_info,
                                                                                     **cf.d_pid_title_incoming_eneid)
                            m_tmp_cand_list = copy.deepcopy(mint_cand_list_incl_checked)
                        if 'b' in opt_info.filtering and 'm' in opt_info.back_link_tgt:
                            mint_cand_list_back_link_checked = bl.filter_by_back_link(m_tmp_cand_list,
                                                                                      opt_info,
                                                                                      mention_info,
                                                                                      log_info,
                                                                                      **d_back_link)
                            m_tmp_cand_list = copy.deepcopy(mint_cand_list_back_link_checked)

                        # filtered candidates
                        if m_tmp_cand_list:

                            cl.append_filtering_cand_info(m_tmp_cand_list, link_info, log_info)

                # tinm
                if 't' in opt_info.mod:
                    tinm_cand_list = []
                    mod = 't'

                    if 'n' in opt_info.filtering and 't' in opt_info.nil_tgt:
                        # nil detection
                        cand_man_res = dn.check_cand_man(cat_attr, log_info, **d_nil_cand_man)
                        stop_attr_res = dn.check_nil_stop(mention_info.attr_label, log_info, **d_nil_stop_attr)

                        dn_res = dn.estimate_nil(
                            cat_attr, cand_man_res, stop_attr_res, mention_info, opt_info, log_info, **d_linkable)
                        if not dn_res:
                            tinm_cand_list = mc.match_mention_title(mod, opt_info, mention_info.t_mention, log_info,
                                                                    **d_tinm_mention_pid_ratio)
                    else:
                        tinm_cand_list = mc.match_mention_title(mod, opt_info, mention_info.t_mention, log_info,
                                                                **d_tinm_mention_pid_ratio)
                    # filtering
                    if len(tinm_cand_list) > 0:
                        t_tmp_cand_list = copy.deepcopy(tinm_cand_list)
                        if 'a' in opt_info.filtering and 't' in opt_info.attr_rng_tgt:
                            tinm_cand_list_attr_checked = ar.filter_by_attr_range(t_tmp_cand_list,
                                                                                  mention_info,
                                                                                  opt_info,
                                                                                  log_info,
                                                                                  **d_cat_attr2eneid_prob)
                            t_tmp_cand_list = copy.deepcopy(tinm_cand_list_attr_checked)
                        if 'i' in opt_info.filtering and 't' in opt_info.incoming_link_tgt:
                            tinm_cand_list_incl_checked = il.filter_by_incoming_link(t_tmp_cand_list,
                                                                                     mention_info,
                                                                                     opt_info.incoming_link_max,
                                                                                     opt_info.incoming_link_type,
                                                                                     log_info,
                                                                                     **cf.d_pid_title_incoming_eneid)
                            t_tmp_cand_list = copy.deepcopy(tinm_cand_list_incl_checked)

                        if 'b' in opt_info.filtering and 't' in opt_info.back_link_tgt:
                            tinm_cand_list_back_link_checked = bl.filter_by_back_link(t_tmp_cand_list,
                                                                                      opt_info,
                                                                                      mention_info,
                                                                                      log_info,
                                                                                      **d_back_link)
                            t_tmp_cand_list = copy.deepcopy(tinm_cand_list_back_link_checked)

                        # filtered candidates
                        if t_tmp_cand_list:
                            cl.append_filtering_cand_info(t_tmp_cand_list, link_info, log_info)
                # link prob
                if 'l' in opt_info.mod:
                    lp_cand_list = []
                    if 'n' in opt_info.filtering and 'l' in opt_info.nil_tgt:
                        # nil detection
                        cand_man_res = dn.check_cand_man(cat_attr, log_info, **d_nil_cand_man)
                        stop_attr_res = dn.check_nil_stop(mention_info.attr_label, log_info, **d_nil_stop_attr)

                        dn_res = dn.estimate_nil(
                            cat_attr, cand_man_res, stop_attr_res, mention_info, opt_info, log_info, **d_linkable)
                        if not dn_res:
                            lp_cand_list = lp.check_link_prob(opt_info.link_prob_min, mention_info, log_info,
                                                              **d_link_prob)
                    else:
                        lp_cand_list = lp.check_link_prob(opt_info.link_prob_min, mention_info, log_info,
                                                          **d_link_prob)

                    # filtering
                    if len(lp_cand_list) > 0:
                        l_tmp_cand_list = copy.deepcopy(lp_cand_list)
                        if 'a' in opt_info.filtering and 'l' in opt_info.attr_rng_tgt:
                            lp_cand_list_attr_checked = ar.filter_by_attr_range(l_tmp_cand_list,
                                                                                mention_info,
                                                                                opt_info,
                                                                                log_info,
                                                                                **d_cat_attr2eneid_prob)
                            l_tmp_cand_list = copy.deepcopy(lp_cand_list_attr_checked)

                        if 'i' in opt_info.filtering and 'l' in opt_info.incoming_link_tgt:
                            lp_cand_list_incl_checked = il.filter_by_incoming_link(l_tmp_cand_list,
                                                                                   mention_info,
                                                                                   opt_info.incoming_link_max,
                                                                                   opt_info.incoming_link_type,
                                                                                   log_info,
                                                                                   **cf.d_pid_title_incoming_eneid)
                            l_tmp_cand_list = copy.deepcopy(lp_cand_list_incl_checked)

                        if 'b' in opt_info.filtering and 'l' in opt_info.back_link_tgt:
                            lp_cand_list_back_link_checked = bl.filter_by_back_link(l_tmp_cand_list,
                                                                                    opt_info,
                                                                                    mention_info,
                                                                                    log_info,
                                                                                    **d_back_link)
                            l_tmp_cand_list = copy.deepcopy(lp_cand_list_back_link_checked)

                        # filtered candidates
                        if l_tmp_cand_list:
                            cl.append_filtering_cand_info(l_tmp_cand_list, link_info, log_info)

                # scoring link candidates for tmp mention
                final_cand_list = gs.scoring(opt_info, link_info, mention_info, mod_info, log_info)

                logger.debug({
                    'action': 'ljc_main',
                    'mention_info.h_mention': mention_info.h_mention,
                    'mention_info.ene_cat': mention_info.ene_cat,
                    'mention_info.attr_label': mention_info.attr_label,
                    'mention_info.t_start_line_id': mention_info.t_start_line_id,
                    'mention_info.t_start_offset': mention_info.t_start_offset,
                    'mention_info.pid': mention_info.pid,
                    'mod_info.mint_weight': mod_info.mint_weight,
                    'mod_info.tinm_weight': mod_info.tinm_weight,
                    'mod_info.slink_weight': mod_info.slink_weight,
                    'mod_info.wlink_weight': mod_info.wlink_weight,
                    'mod_info.link_prob_weight': mod_info.link_prob_weight,
                    'final_cand_list': final_cand_list
                })
                # add the results of scoring to answer list
                final_cand_cnt = 0

                if len(final_cand_list) == 0:
                    rec['link_page_id'] = None
                    list_rec_out.append(copy.deepcopy(rec))
                else:
                    for final_cand in final_cand_list:
                        rec['link_page_id'] = final_cand[0]
                        ext_title = ''
                        try:
                            ext_title = cf.d_pid_title_incoming_eneid[final_cand[0]][0]
                        except (KeyError, ValueError) as e:
                            logger.warning({
                                'action': 'scoring',
                                'pid': mention_info.pid,
                                'mention': mention_info.t_mention,
                                'error': e,
                            })
                        list_rec_out.append(copy.deepcopy(rec))
                        final_cand_cnt += 1
                        if final_cand_cnt == opt_info.ans_max:
                            break

        with open(outfile, mode='w', encoding='utf-8') as o:
            for tline in list_rec_out:
                json.dump(tline, o, ensure_ascii=False)
                o.write('\n')

    d_mint_mention_pid_ratio.clear()
    d_tinm_mention_pid_ratio.clear()
    d_cat_attr2eneid_prob.clear()
    d_self_link.clear()
    d_link_prob.clear()
    d_back_link.clear()
    diff_info.clear()
    d_linkable.clear()
    d_nil_cand_man.clear()
    d_nil_stop_attr.clear()

    lc.gen_linked_tsv(out_dir, data_info.title2pid_ext_file, log_info, **d_eneid2enlabel)


if __name__ == '__main__':
    ljc_main()
