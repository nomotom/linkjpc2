from glob import glob
import json
import click
import config as cf
import csv
from decimal import Decimal, ROUND_HALF_UP
import logging
import logging.config
import sys
import string
import re


def set_logging_pre(log_info, logger_name):
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
@click.argument('sample_gold_dir', type=click.Path(exists=True))
@click.argument('sample_input_dir', type=click.Path(exists=True))
@click.option('--conv_year', is_flag=True, default=False, show_default=True)
@click.option('--conv_sample_json_pageid', is_flag=True, default=False, show_default=True)
@click.option('--gen_attr_rng', is_flag=True, default=False, show_default=True)
@click.option('--gen_change_wikipedia_info', is_flag=True, default=False, show_default=True)
@click.option('--gen_enew', is_flag=True, default=False, show_default=True)
@click.option('--gen_enew_rev_year', is_flag=True, default=False, show_default=True)
@click.option('--gen_sample_gold_tsv', is_flag=True, default=False, show_default=True)
@click.option('--gen_sample_gold_tsv_cnv_year', is_flag=True, default=False, show_default=True)
@click.option('--gen_title2pid', is_flag=True, default=False, show_default=True)
@click.option('--gen_redirect', is_flag=True, default=False, show_default=True)
# @click.option('--gen_redirect2', is_flag=True, default=False, show_default=True)
@click.option('--pre_matching', type=click.Choice(['mint', 'tinm', 'n']), default=cf.OptInfo.pre_matching_default,
              show_default=True)
@click.option('--title_matching_mint', '-tmm', type=click.Choice(['trim', 'full']),
              default=cf.OptInfo.title_matching_mint_default, show_default=True)
@click.option('--title_matching_tinm', '-tmt', type=click.Choice(['trim', 'full']),
              default=cf.OptInfo.title_matching_tinm_default, show_default=True)
@click.option('--char_match_min', default=cf.OptInfo.char_match_min_default, show_default=True, type=click.FLOAT)
# @click.option('--cnv_dump_file', is_flag=True, default=False, show_default=True)
@click.option('--gen_title2pid_ext', is_flag=True, default=False, show_default=True)
@click.option('--gen_html', is_flag=True, default=False, show_default=True)
@click.option('--gen_html_conv_year', is_flag=True, default=False, show_default=True)
@click.option('--gen_common_html', is_flag=True, default=False, show_default=True)
@click.option('--gen_common_html_conv_year', is_flag=True, default=False, show_default=True)
@click.option('--gen_link_prob', is_flag=True, default=False, show_default=True)
@click.option('--gen_linkable', is_flag=True, default=False, show_default=True)
@click.option('--gen_nil', is_flag=True, default=False, show_default=True)
@click.option('--gen_slink', is_flag=True, default=False, show_default=True)
@click.option('--gen_back_link', is_flag=True, default=False, show_default=True)
@click.option('--gen_link_dist', is_flag=True, default=False, show_default=True)
@click.option('--gen_incoming_link', is_flag=True, default=False, show_default=True)
@click.option('--page_conv', is_flag=True, default=False, show_default=True)
@click.option('--f_self_link_by_attr_name', default=cf.DataInfo.f_self_link_by_attr_name_default, show_default=True, type=click.STRING,
              help='lists of attributes whose values are supposed to refer to the original entity, judging from the name of attributes.')
@click.option('--f_self_link_pat', default=cf.DataInfo.f_self_link_pat_default, show_default=True, type=click.STRING,
              help='lists of matching pattern and position to find self link attributes by attribute names.')
@click.option('--f_title2pid_ext', default=cf.DataInfo.f_title2pid_ext_default, show_default=True, type=click.STRING,
              help='from_title_to_pageid_extended_information. Filter out disambiguation, management, '
                   'or format-error pages, and add eneid, incoming link num info.')
# 20220916
@click.option('--f_title2pid_ext_obs', default=cf.DataInfo.f_title2pid_ext_obs_default, show_default=True, type=click.STRING,
              help='from_title_to_pageid_extended_information based on obsolete Wikipedia. Filter out disambiguation, management, '
                   'or format-error pages, and add eneid, incoming link num info.')
@click.option('--f_title2pid_org', default=cf.DataInfo.f_title2pid_org_default, show_default=True, type=click.STRING,
              help='from_title_to_pageid_information_original.')
@click.option('--f_cirrus_content', default=cf.DataInfo.f_cirrus_content_default, show_default=True, type=click.STRING,
              help='cirrus dump (content) (.')
@click.option('--f_disambiguation', default=cf.DataInfo.f_disambiguation_default, show_default=True, type=click.STRING,
              help='disambiguation page list.')
@click.option('--f_disambiguation_pat', default=cf.DataInfo.f_disambiguation_pat_default, show_default=True,
              type=click.STRING, help='disambiguation pattern file.')
@click.option('--f_mint_partial', default=cf.DataInfo.f_mint_partial_default, show_default=True, type=click.STRING,
              help='mint_partial')
@click.option('--f_mint_trim_partial', default=cf.DataInfo.f_mint_trim_partial_default, show_default=True,
              type=click.STRING, help='mint_trim_partial')
@click.option('--f_tinm_partial', default=cf.DataInfo.f_tinm_partial_default, show_default=True, type=click.STRING,
              help='tinm_partial')
@click.option('--f_tinm_trim_partial', default=cf.DataInfo.f_tinm_trim_partial_default, show_default=True,
              type=click.STRING, help='tinm_trim_partial')
@click.option('--f_common_html_info', default=cf.DataInfo.f_common_html_info_default, show_default=True,
              type=click.STRING, help='html_info_file')
@click.option('--f_html_info', default=cf.DataInfo.f_html_info_default, show_default=True, type=click.STRING,
              help='html_info_file')
@click.option('--f_redirect_info', default=cf.DataInfo.f_redirect_info_default, show_default=True, type=click.STRING,
              help='f_redirect_info')
@click.option('--f_enew_info', default=cf.DataInfo.f_enew_info_default, show_default=True, type=click.STRING,
              help='f_enew_info')
@click.option('--f_enew_org', default=cf.DataInfo.f_enew_org_default, show_default=True, type=click.STRING,
              help='f_enew_org')
@click.option('--f_enew_mod_list', default=cf.DataInfo.f_enew_mod_list_default, show_default=True, type=click.STRING,
              help='f_enew_mod_list')
@click.option('--f_incoming', default=cf.DataInfo.f_incoming_default, show_default=True, type=click.STRING,
              help='f_incoming')
@click.option('--f_link_prob', default=cf.DataInfo.f_link_prob_default, show_default=True, type=click.STRING,
              help='f_link_prob')
@click.option('--f_linkable_info', type=click.STRING,
              default=cf.DataInfo.f_linkable_info_default, show_default=True,
              help='filename of linkable ratio info file.')
@click.option('--f_nil', default=cf.DataInfo.f_nil_default, show_default=True, type=click.STRING,
              help='f_nil')
@click.option('--f_attr_rng_auto', default=cf.DataInfo.f_attr_rng_auto_default, show_default=True, type=click.STRING,
              help='f_attr_rng_auto')
# @click.option('--f_attr_rng_merged', default=cf.DataInfo.f_attr_rng_merged_default, show_default=True, type=click.STRING,
#               help='f_attr_rng_merged')
# @click.option('--f_attr_rng_man', default=cf.DataInfo.f_attr_rng_man_default, show_default=True, type=click.STRING,
#               help='f_attr_rng_man')
@click.option('--f_slink', default=cf.DataInfo.f_slink_default, show_default=True, type=click.STRING,
              help='f_slink')
@click.option('--f_input_title', default=cf.DataInfo.f_input_title_default, show_default=True, type=click.STRING,
              help='f_input_title')
@click.option('--f_back_link', default=cf.DataInfo.f_back_link_default, show_default=True, type=click.STRING,
              help='f_back_link')
@click.option('--f_back_link_dump_org', default=cf.DataInfo.f_back_link_dump_org_default, show_default=True, type=click.STRING,
              help='f_back_link_dump_org')
@click.option('--f_page_dump', default=cf.DataInfo.f_page_dump_default, show_default=True, type=click.STRING,
              help='f_page_dump')
@click.option('--f_redirect_dump', default=cf.DataInfo.f_redirect_dump_default, show_default=True, type=click.STRING,
              help='f_redirect_dump')
@click.option('--f_page_dump_org', default=cf.DataInfo.f_page_dump_org_default, show_default=True, type=click.STRING,
              help='f_page_dump_org')
@click.option('--f_page_dump_old_org', default=cf.DataInfo.f_page_dump_old_org_default, show_default=True, type=click.STRING,
              help='f_page_dump_old_org')
@click.option('--f_redirect_dump_org', default=cf.DataInfo.f_redirect_dump_org_default, show_default=True, type=click.STRING,
              help='f_redirect_dump_org')
@click.option('--f_mention_gold_link_dist', default=cf.DataInfo.f_mention_gold_link_dist_default, show_default=True,
              type=click.STRING, help='f_mention_gold_link_dist')
@click.option('--f_target_attr', default=cf.DataInfo.f_target_attr_default, show_default=True,
              type=click.STRING, help='f_target_attr')
@click.option('--f_wikipedia_page_change_info', default=cf.DataInfo.f_wikipedia_page_change_info_default, show_default=True,
              type=click.STRING, help='f_target_attr')
# @click.option('--f_title_pid_db', default=cf.DataInfo.f_mention_gold_link_dist_default, show_default=True,
#               type=click.STRING, help='f_mention_gold_link_dist')
def ljc_prep_main(common_data_dir,
                  tmp_data_dir,
                  in_dir,
                  sample_gold_dir,
                  sample_input_dir,
                  char_match_min,
                  # cnv_dump_file,
                  conv_year,
                  conv_sample_json_pageid,
                  gen_attr_rng,
                  gen_change_wikipedia_info,
                  gen_back_link,
                  gen_common_html,
                  gen_common_html_conv_year,
                  gen_enew,
                  gen_enew_rev_year,
                  gen_html,
                  gen_html_conv_year,
                  gen_incoming_link,
                  gen_linkable,
                  gen_link_dist,
                  gen_link_prob,
                  gen_nil,
                  gen_slink,
                  gen_title2pid,
                  gen_title2pid_ext,
                  gen_sample_gold_tsv,
                  gen_sample_gold_tsv_cnv_year,
                  pre_matching,
                  gen_redirect,
                  page_conv,
                  title_matching_mint,
                  title_matching_tinm,
                  f_back_link,
                  f_back_link_dump_org,
                  f_attr_rng_auto,
                  # f_attr_rng_merged,
                  # f_attr_rng_man,
                  f_cirrus_content,
                  f_common_html_info,
                  f_disambiguation,
                  f_disambiguation_pat,
                  f_enew_info,
                  f_enew_mod_list,
                  f_enew_org,
                  f_html_info,
                  f_incoming,
                  f_input_title,
                  f_linkable_info,
                  f_link_prob,
                  f_mention_gold_link_dist,
                  f_mint_partial,
                  f_mint_trim_partial,
                  f_nil,
                  f_page_dump,
                  f_page_dump_old_org,
                  f_page_dump_org,
                  f_redirect_dump,
                  f_redirect_dump_org,
                  f_redirect_info,
                  f_self_link_by_attr_name,
                  f_self_link_pat,
                  f_slink,
                  f_target_attr,
                  f_tinm_partial,
                  f_tinm_trim_partial,
                  f_title2pid_ext,
                  f_title2pid_ext_obs,
                  f_title2pid_org,
                  f_wikipedia_page_change_info):
    class DataInfoPrep(object):
        def __init__(self,
                     prep_common_data_dir,
                     prep_tmp_data_dir,
                     prep_in_dir,
                     prep_sample_gold_dir,
                     prep_sample_input_dir,
                     prep_f_back_link=f_back_link,
                     prep_f_back_link_dump_org=f_back_link_dump_org,
                     # prep_f_attr_rng_man=f_attr_rng_man,
                     prep_f_attr_rng_auto=f_attr_rng_auto,
                     # prep_f_attr_rng_merged=f_attr_rng_merged,
                     prep_f_cirrus_content=f_cirrus_content,
                     prep_f_common_html_info=f_common_html_info,
                     prep_f_disambiguation=f_disambiguation,
                     prep_f_disambiguation_pat=f_disambiguation_pat,
                     prep_f_enew_info=f_enew_info,
                     prep_f_enew_mod_list=f_enew_mod_list,
                     prep_f_enew_org=f_enew_org,
                     prep_f_html_info=f_html_info,
                     prep_f_incoming=f_incoming,
                     prep_f_input_title=f_input_title,
                     prep_f_linkable=f_linkable_info,
                     prep_f_link_prob=f_link_prob,
                     prep_f_mention_gold_link_dist=f_mention_gold_link_dist,
                     prep_f_mint_partial=f_mint_partial,
                     prep_f_mint_trim_partial=f_mint_trim_partial,
                     prep_f_nil=f_nil,
                     prep_f_page_dump=f_page_dump,
                     prep_f_page_dump_old_org=f_page_dump_old_org,
                     prep_f_page_dump_org=f_page_dump_org,
                     prep_f_redirect_dump=f_redirect_dump,
                     prep_f_redirect_dump_org=f_redirect_dump_org,
                     prep_f_redirect_info=f_redirect_info,
                     prep_f_self_link_by_attr_name=f_self_link_by_attr_name,
                     prep_f_self_link_pat=f_self_link_pat,
                     prep_f_slink=f_slink,
                     prep_f_target_attr=f_target_attr,
                     prep_f_tinm_partial=f_tinm_partial,
                     prep_f_tinm_trim_partial=f_tinm_trim_partial,
                     prep_f_title2pid_ext=f_title2pid_ext,
                     prep_f_title2pid_ext_obs=f_title2pid_ext_obs,
                     prep_f_title2pid_org=f_title2pid_org,
                     prep_f_wikipedia_page_change_info=f_wikipedia_page_change_info):
            self.common_data_dir = prep_common_data_dir
            self.tmp_data_dir = prep_tmp_data_dir
            self.in_dir = prep_in_dir
            self.sample_gold_dir = prep_sample_gold_dir
            self.sample_input_dir = prep_sample_input_dir
            self.back_link_file = prep_tmp_data_dir + prep_f_back_link
            self.back_link_dump_org_file = prep_common_data_dir + prep_f_back_link_dump_org
            self.attr_rng_auto_file = prep_common_data_dir + prep_f_attr_rng_auto
            # self.attr_rng_man_file = prep_common_data_dir + prep_f_attr_rng_man
            # self.attr_rng_merged_file = prep_common_data_dir + prep_f_attr_rng_merged

            self.cirrus_content_file = prep_common_data_dir + prep_f_cirrus_content
            self.disambiguation_file = prep_common_data_dir + prep_f_disambiguation
            self.disambiguation_pat_file = prep_common_data_dir + prep_f_disambiguation_pat
            self.enew_info_file = prep_common_data_dir + prep_f_enew_info
            self.enew_mod_list_file = prep_common_data_dir + prep_f_enew_mod_list
            self.enew_org_file = prep_common_data_dir + prep_f_enew_org
            self.common_html_info_file = prep_common_data_dir + prep_f_common_html_info
            self.incoming_file = prep_common_data_dir + prep_f_incoming
            self.linkable_file = prep_common_data_dir + prep_f_linkable
            self.link_prob_file = prep_common_data_dir + prep_f_link_prob
            self.nil_file = prep_common_data_dir + prep_f_nil
            self.mention_gold_link_dist_file = prep_common_data_dir + prep_f_mention_gold_link_dist
            self.page_dump_file = prep_common_data_dir + prep_f_page_dump
            self.page_dump_old_org_file = prep_common_data_dir + prep_f_page_dump_old_org
            self.page_dump_org_file = prep_common_data_dir + prep_f_page_dump_org
            self.redirect_dump_file = prep_common_data_dir + prep_f_redirect_dump
            # self.redirect_dump_old_org_file = prep_common_data_dir + prep_f_redirect_dump_old_org
            self.redirect_dump_org_file = prep_common_data_dir + prep_f_redirect_dump_org
            self.title2pid_ext_file = prep_common_data_dir + prep_f_title2pid_ext
            self.title2pid_ext_obs_file = prep_common_data_dir + prep_f_title2pid_ext_obs
            self.title2pid_org_file = prep_common_data_dir + prep_f_title2pid_org
            # self.title2pid_dbase_file = prep_common_data_dir + prep_f_title2pid_dbase
            self.redirect_info_file = prep_common_data_dir + prep_f_redirect_info
            self.slink_file = prep_common_data_dir + prep_f_slink
            self.self_link_pat_file = prep_common_data_dir + prep_f_self_link_pat
            self.self_link_by_attr_name_file = prep_common_data_dir + prep_f_self_link_by_attr_name
            self.target_attr_file = prep_common_data_dir + prep_f_target_attr
            self.wikipedia_page_change_info_file = prep_common_data_dir + prep_f_wikipedia_page_change_info

            self.html_info_file = prep_tmp_data_dir + prep_f_html_info
            self.input_title_file = prep_tmp_data_dir + prep_f_input_title
            self.mint_partial_file = prep_tmp_data_dir + prep_f_mint_partial
            self.mint_trim_partial_file = prep_tmp_data_dir + prep_f_mint_trim_partial
            self.tinm_partial_file = prep_tmp_data_dir + prep_f_tinm_partial
            self.tinm_trim_partial_file = prep_tmp_data_dir + prep_f_tinm_trim_partial
    csv.field_size_limit(1000000000)
    log_info = cf.LogInfo()
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    data_info_prep = DataInfoPrep(common_data_dir, tmp_data_dir, in_dir, sample_gold_dir, sample_input_dir)

    # common_data_dir
    data_info_prep.attr_rng_auto_file = data_info_prep.common_data_dir + f_attr_rng_auto
    # data_info_prep.attr_rng_man_file = data_info_prep.common_data_dir + f_attr_rng_man
    # data_info_prep.attr_rng_merged_file = data_info_prep.common_data_dir + f_attr_rng_merged
    data_info_prep.back_link_dump_org_file = data_info_prep.common_data_dir + f_back_link_dump_org
    data_info_prep.cirrus_content_file = data_info_prep.common_data_dir + f_cirrus_content
    data_info_prep.disambiguation_file = data_info_prep.common_data_dir + f_disambiguation
    data_info_prep.disambiguation_pat_file = data_info_prep.common_data_dir + f_disambiguation_pat
    data_info_prep.enew_info_file = data_info_prep.common_data_dir + f_enew_info
    data_info_prep.enew_org_file = data_info_prep.common_data_dir + f_enew_org
    data_info_prep.enew_mod_list_file = data_info_prep.common_data_dir + f_enew_mod_list
    data_info_prep.common_html_info_file = data_info_prep.common_data_dir + f_common_html_info
    data_info_prep.incoming_file = data_info_prep.common_data_dir + f_incoming
    data_info_prep.linkable_file = data_info_prep.common_data_dir + f_linkable_info
    data_info_prep.link_prob_file = data_info_prep.common_data_dir + f_link_prob
    data_info_prep.mention_gold_link_dist_file = data_info_prep.common_data_dir + f_mention_gold_link_dist
    data_info_prep.nil_file = data_info_prep.common_data_dir + f_nil
    data_info_prep.title2pid_ext_file = data_info_prep.common_data_dir + f_title2pid_ext
    data_info_prep.title2pid_ext_obs_file = data_info_prep.common_data_dir + f_title2pid_ext_obs
    data_info_prep.title2pid_org_file = data_info_prep.common_data_dir + f_title2pid_org
    # data_info_prep.title2pid_dbase_file = data_info_prep.common_data_dir + f_title2pid_dbase
    data_info_prep.redirect_info_file = data_info_prep.common_data_dir + f_redirect_info
    data_info_prep.slink_file = data_info_prep.common_data_dir + f_slink
    data_info_prep.self_link_pat_file = data_info_prep.common_data_dir + f_self_link_pat
    data_info_prep.self_link_attribute_by_name_file = data_info_prep.common_data_dir + f_self_link_by_attr_name
    data_info_prep.target_attr_file = data_info_prep.common_data_dir + f_target_attr
    data_info_prep.redirect_dump_file = data_info_prep.common_data_dir + f_redirect_dump
    data_info_prep.redirect_dump_org_file = data_info_prep.common_data_dir + f_redirect_dump_org
    data_info_prep.page_dump_file = data_info_prep.common_data_dir + f_page_dump
    data_info_prep.page_dump_org_file = data_info_prep.common_data_dir + f_page_dump_org

    # [tmp_data_dir] ############################################################################
    data_info_prep.back_link_file = data_info_prep.tmp_data_dir + f_back_link
    data_info_prep.html_info_file = data_info_prep.tmp_data_dir + f_html_info
    data_info_prep.input_title_file = data_info_prep.tmp_data_dir + f_input_title
    data_info_prep.mint_partial_file = data_info_prep.tmp_data_dir + f_mint_partial
    data_info_prep.mint_trim_partial_file = data_info_prep.tmp_data_dir + f_mint_trim_partial
    data_info_prep.tinm_partial_file = data_info_prep.tmp_data_dir + f_tinm_partial
    data_info_prep.tinm_trim_partial_file = data_info_prep.tmp_data_dir + f_tinm_trim_partial

    # sample_gold_data
    # 20220822
    sample_gold_linked_dir = data_info_prep.sample_gold_dir + 'link_annotation/'
    sample_gold_linked_dir_conv = data_info_prep.sample_gold_dir + 'link_annotation/conv/'

    # 20220822 fromhere
    # sample_data_dir_pre = data_info_prep.sample_gold_dir
    # sample_data_dir = sample_data_dir_pre.replace('link_annotation/', '')
    sample_input_ene_dir = data_info_prep.sample_input_dir + 'ene_annotation/'
    sample_input_ene_dir_conv = data_info_prep.sample_input_dir + 'ene_annotation/conv/'

    sample_input_html_dir = data_info_prep.sample_input_dir + 'html/'
    sample_input_html_dir_conv = data_info_prep.sample_input_dir + 'html/conv/'

    # data_info_prep.html_dir = data_info_prep.tmp_data_dir + 'html/'
    # data_info_prep.in_dir = data_info_prep.in_dir
    data_info_prep.in_ene_dir = data_info_prep.in_dir + 'ene_annotation/'
    data_info_prep.in_html_dir = data_info_prep.in_dir + 'html/'
    input_ene_dir = data_info_prep.in_ene_dir
    input_ene_dir_conv = input_ene_dir + 'conv/'

    # 20220822 till here

    logger.info({
        'action': 'ljc_prep_main',
        'id': 'start',
        'data_info_prep.common_data_dir': data_info_prep.common_data_dir,
        'tmp_data_dir': data_info_prep.tmp_data_dir,
        'in_dir': data_info_prep.in_dir,
        'in_ene_dir': data_info_prep.in_ene_dir,
        'in_html_dir': data_info_prep.in_html_dir,
        'sample_gold_linked_dir': sample_gold_linked_dir,
        'sample_input_html_dir': sample_input_html_dir,
        'sample_input_dir': sample_input_dir
    })

    # # 20220920
    if conv_sample_json_pageid:
        logger.info({
            'action': 'conv_sample_pageid',
        })
        conv_input_pageid(sample_input_ene_dir,
                          sample_input_ene_dir_conv,
                          data_info_prep.wikipedia_page_change_info_file,
                          log_info)
        conv_link_pageid(sample_gold_linked_dir,
                        sample_gold_linked_dir_conv,
                        data_info_prep.wikipedia_page_change_info_file,
                        log_info)

    # 20220920
    if gen_change_wikipedia_info:
        logger.info({
            'action': 'gen_change_wikipedia_info',
        })
        gen_change_wikipage_list(data_info_prep.page_dump_old_org_file, data_info_prep.page_dump_org_file,
                                 data_info_prep.wikipedia_page_change_info_file, log_info)

    # # 20220916  →　これはいらなくなる
    # if gen_sample_gold_tsv_cnv_year:
    #     # logger.info({
    #     #     'action': 'gen_sample_gold_tsv_cnv_year',
    #     #     'sample_gold_linked_dir': sample_gold_linked_dir,
    #     #     'title2pid_org_file': data_info_prep.title2pid_org_file,
    #     # })
    #
    #     logger.info({
    #         'action': 'gen_sample_gold_tsv_cnv_year',
    #         'sample_gold_linked_dir': sample_gold_linked_dir,
    #     })
    #     linkedjson2tsv_add_linked_title_cnv_year(sample_gold_linked_dir, data_info_prep.title2pid_ext_file, data_info_prep.title2pid_ext_obs_file, log_info)

    if gen_sample_gold_tsv:
        # logger.info({
        #     'action': 'gen_sample_gold_tsv',
        #     'sample_gold_linked_dir': sample_gold_linked_dir,
        #     'title2pid_org_file': data_info_prep.title2pid_org_file,
        # })

        # 暫定対応　20220824
        logger.info({
            'action': 'gen_sample_gold_tsv',
            'sample_gold_linked_dir': sample_gold_linked_dir,
        })
        # 20220921 修正
        if conv_year:
            linkedjson2tsv_add_linked_title_ene(sample_gold_linked_dir_conv, data_info_prep.title2pid_ext_file, log_info)
        else:
            linkedjson2tsv_add_linked_title_ene(sample_gold_linked_dir, data_info_prep.title2pid_ext_file, log_info)

        # linkedjson2tsv_simple(sample_gold_linked_dir, data_info_prep.title2pid_ext_file, log_info)

        # linkedjson2tsv(sample_gold_linked_dir, data_info_prep.title2pid_org_file, log_info)

    # if gen_redirect2:
    #
    #     logger.info({
    #         'action': 'gen_redirect2',
    #         'disambiguation_pat_file': data_info_prep.disambiguation_pat_file,
    #         'cirrus_content_file': data_info_prep.cirrus_content_file,
    #     })
    #     gen_disambiguation_file(data_info_prep.disambiguation_pat_file, data_info_prep.cirrus_content_file,
    #                             data_info_prep.disambiguation_file, log_info)
    #     logger.info({
    #         'action': 'ljc_prep_main',
    #         'run': 'gen_redirect_info_file',
    #         'incoming_file': data_info_prep.incoming_file,
    #         'title2pid_org_file': data_info_prep.title2pid_org_file,
    #         'disambiguation_file': data_info_prep.disambiguation_file,
    #         'redirect_info_file': data_info_prep.redirect_info_file,
    #     })
    #     gen_redirect_info_file2(
    #         data_info_prep.incoming_file,
    #         data_info_prep.title2pid_org_file,
    #         data_info_prep.disambiguation_file,
    #         data_info_prep.redirect_info_file, log_info)

    if gen_redirect:
        logger.info({
            'run': 'gen_redirect',
            'disambiguation_pat_file': data_info_prep.disambiguation_pat_file,
            'cirrus_content_file': data_info_prep.cirrus_content_file,
            'disambiguation_file': data_info_prep.disambiguation_file,
        })
        gen_disambiguation_file(data_info_prep.disambiguation_pat_file, data_info_prep.cirrus_content_file,
                                data_info_prep.disambiguation_file, log_info)
        logger.info({
            'action': 'ljc_prep_main',
            'run': 'gen_redirect_info_file',
            'title2pid_org_file': data_info_prep.title2pid_org_file,
            'disambiguation_file': data_info_prep.disambiguation_file,
            'redirect_info_file': data_info_prep.redirect_info_file,
        })
        gen_redirect_info_file(data_info_prep.title2pid_org_file, data_info_prep.disambiguation_file,
                               data_info_prep.redirect_info_file, log_info)

    if gen_incoming_link:
        logger.info({
            'action': 'gen_incoming_link',
            'cirrus_content_file': data_info_prep.cirrus_content_file,
            'incoming_file': data_info_prep.incoming_file
        })
        gen_incoming_link_file(data_info_prep.cirrus_content_file, data_info_prep.incoming_file, log_info)

    # if cnv_dump_file:
    # #     # 20220919
    #     cnv_dump(data_info_prep.redirect_dump_org_file, data_info_prep.redirect_dump_file, log_info)
    # #
    # #     # 20220919
    #     cnv_dump(data_info_prep.page_dump_org_file, data_info_prep.page_dump_file, log_info)

    # if merge_title2pid:
    #     logger.info({
    #         'run': 'merge_title2pid',
    #         'title2pid_obs_file': data_info_prep.title2pid_merge_file,
    #
    #         'title2pid_file': data_info_prep.title2pid_merge_file,
    #     })

        # gen_title2pid_file(data_info_prep.redirect_dump_file, data_info_prep.page_dump_file,
        #                    data_info_prep.title2pid_org_file, log_info)

        # gen_title2pid_file(data_info_prep.redirect_dump_file, data_info_prep.page_dump_file,
        #                    data_info_prep.title2pid_org_file, cf.OptInfo.min_illegal_title_len, log_info)

    if gen_title2pid:
        logger.info({
            'run': 'gen_title2pid',
            'title2pid_org_file': data_info_prep.title2pid_org_file,
            # 'incoming_file': data_info_prep.incoming_file,
            # 'enew_info_file': data_info_prep.enew_info_file,
            # 'redirect_info_file': data_info_prep.redirect_info_file,
        })

        # gen_title2pid_file(data_info_prep.redirect_dump_file, data_info_prep.page_dump_file,
        #                    data_info_prep.title2pid_org_file, log_info)

        gen_title2pid_file(data_info_prep.redirect_dump_file, data_info_prep.page_dump_file,
                           data_info_prep.title2pid_org_file, cf.OptInfo.min_illegal_title_len, log_info)

    # 2022/9/21
    # if conv_year gen_enew_info_rev_file
    # else gen_enew

    if gen_enew:
        gen_enew_info_file(data_info_prep.enew_org_file, data_info_prep.enew_mod_list_file,
                           data_info_prep.enew_info_file, log_info)

    if gen_enew_rev_year:
        gen_enew_info_rev_file(data_info_prep.enew_org_file,
                               data_info_prep.enew_mod_list_file,
                               data_info_prep.wikipedia_page_change_info_file,
                               data_info_prep.enew_info_file, log_info)

    if gen_title2pid_ext:
        logger.info({
            'run': 'gen_title2pid_ext',
            'enew_org_file': data_info_prep.enew_org_file,
            'enew_mod_list_file': data_info_prep.enew_mod_list_file,
            'enew_info_file': data_info_prep.enew_info_file,
        })

        logger.info({
            'action': 'ljc_prep_main',
            'run': 'gen_title2pid_ext',
            'title2pid_ext_file': data_info_prep.title2pid_ext_file,
            'incoming_file': data_info_prep.incoming_file,
            'enew_info_file': data_info_prep.enew_info_file,
            'redirect_info_file': data_info_prep.redirect_info_file,
        })
        gen_title2pid_ext_file(data_info_prep.title2pid_ext_file, data_info_prep.incoming_file,
                               data_info_prep.enew_info_file, data_info_prep.redirect_info_file, log_info)

    if gen_back_link:
        logger.info({
            'run': 'gen_back_link',
            # 20220822
            'input_ene_dir': input_ene_dir,
            'input_ene_dir_conv': input_ene_dir_conv,
            'input_title_file': data_info_prep.input_title_file,
            'back_link_dump_org': data_info_prep.back_link_dump_org_file,
            'back_link_file': data_info_prep.back_link_file,
        })
        if conv_year:
            gen_input_title_file(input_ene_dir_conv, data_info_prep.input_title_file, log_info)
        else:
            gen_input_title_file(input_ene_dir, data_info_prep.input_title_file, log_info)
        logger.info({
            'action': 'ljc_prep_main',
            'run': 'gen_back_link_info_file',
            'in_ene_dir': data_info_prep.in_ene_dir,
            'input_title_file': data_info_prep.input_title_file,
            'back_link_file': data_info_prep.back_link_file,
            'back_link_dump_org_file': data_info_prep.back_link_dump_org_file,
            'title2pid_ext_file': data_info_prep.title2pid_ext_file,
        })
        gen_back_link_info_file(data_info_prep.input_title_file, data_info_prep.back_link_file,
                                data_info_prep.back_link_dump_org_file, data_info_prep.title2pid_ext_file, log_info)

    # if conv_year:
    # gen_common_html_conv_year
    # else
    # gen_common_html

    if gen_common_html:
        logger.info({
            'run': 'gen_common_html',
            # 20220822
            'sample_input_html_dir': sample_input_html_dir,
            'common_html_info_file': data_info_prep.common_html_info_file
        })
        # 20220822
        gen_html_info_file(sample_input_html_dir, data_info_prep.common_html_info_file, log_info)

    if gen_common_html_conv_year:
        logger.info({
            'run': 'gen_common_html_cnv_year',
            # 20220822
            'sample_input_html_dir': sample_input_html_dir,
            'common_html_info_cnv_year_file': data_info_prep.common_html_info_file
        })
        # 20220822
        gen_html_info_file_conv_year(sample_input_html_dir,
                                    data_info_prep.common_html_info_file,
                                    data_info_prep.wikipedia_page_change_info_file, log_info)

    if gen_link_dist:
        logger.info({
            'run': 'gen_link_dist',
            'common_html_info_file': data_info_prep.common_html_info_file,
            'sample_gold_linked_dir': sample_gold_linked_dir,
            'common_data_dir': data_info_prep.common_data_dir,
            'mention_gold_link_dist_file': data_info_prep.mention_gold_link_dist_file,
        })
        if conv_year:
            gen_mention_gold_link_dist(data_info_prep.common_html_info_file, sample_gold_linked_dir_conv,
                                       data_info_prep.mention_gold_link_dist_file, log_info)
        else:
            gen_mention_gold_link_dist(data_info_prep.common_html_info_file, sample_gold_linked_dir,
                                       data_info_prep.mention_gold_link_dist_file, log_info)

    if pre_matching == 'mint':

        if not title_matching_mint:
            logger.error({
                'action': 'ljc_prep_main',
                'error': 'title_matching_mint should be specified',
            })
            sys.exit()
        else:
            logger.info({
                'action': 'ljc_prep_main',
                'run': 'prematch_mention_title',

            })
            # 20220822
            if conv_year:
                logger.info({
                    'action': 'ljc_prep_main',
                    'run': 'prematch_mention_title',
                    'input_ene_dir_conv': input_ene_dir_conv
                })
                prematch_mention_title(
                    input_ene_dir_conv,
                    data_info_prep,
                    pre_matching,
                    title_matching_mint,
                    char_match_min,
                    log_info)
            else:
                prematch_mention_title(
                    input_ene_dir,
                    data_info_prep,
                    pre_matching,
                    title_matching_mint,
                    char_match_min,
                    log_info)

            # prematch_mention_title(data_info_prep, pre_matching, title_matching_mint, char_match_min, log_info)
    elif pre_matching == 'tinm':
        if not title_matching_tinm:
            logger.error({
                'action': 'ljc_prep_main',
                'error': 'title_matching_tinm should be specified',
            })
            sys.exit()
        else:
            if conv_year:
                prematch_mention_title(
                    input_ene_dir_conv,
                    data_info_prep,
                    pre_matching,
                    title_matching_tinm,
                    char_match_min,
                    log_info)
            # 20220822
            else:
                prematch_mention_title(
                    input_ene_dir,
                    data_info_prep,
                    pre_matching,
                    title_matching_tinm,
                    char_match_min,
                    log_info)
            # prematch_mention_title(data_info_prep, pre_matching, title_matching_tinm, char_match_min, log_info)

    elif pre_matching != 'n':
        logger.error({
            'action': 'ljc_prep_main',
            'error': 'illegal pre_matching',
        })
        sys.exit()

    if gen_html:
        logger.info({
            'run': 'gen_html',
            'html_dir': data_info_prep.in_html_dir,
            'html_info_file': data_info_prep.html_info_file
        })
        gen_html_info_file(data_info_prep.in_html_dir, data_info_prep.html_info_file, log_info)

    if gen_html_conv_year:
        logger.info({
            'run': 'gen_html',
            'html_dir': data_info_prep.in_html_dir,
            'html_info_file': data_info_prep.html_info_file
        })
        gen_html_info_file_conv_year(data_info_prep.in_html_dir,
                                     data_info_prep.html_info_file,
                                     data_info_prep.wikipedia_page_change_info_file,
                                     log_info)

    if gen_link_prob:

        if conv_year:
            logger.info({
                'run': 'gen_link_prob',
                'link_prob_file': data_info_prep.link_prob_file,
                'sample_gold_linked_dir_conv': sample_gold_linked_dir_conv
            })
            gen_link_prob_file(sample_gold_linked_dir_conv, data_info_prep.link_prob_file, log_info)
        else:
            logger.info({
                'run': 'gen_link_prob',
                'link_prob_file': data_info_prep.link_prob_file,
                'sample_gold_linked_dir': sample_gold_linked_dir
            })
            gen_link_prob_file(sample_gold_linked_dir, data_info_prep.link_prob_file, log_info)

    if gen_nil:

        if conv_year:
            logger.info({
                'run': 'gen_nil',
                'sample_gold_linked_dir_conv': sample_gold_linked_dir_conv,
                'nil_file': data_info_prep.nil_file
            })
            gen_nil_info(sample_gold_linked_dir_conv, data_info_prep.nil_file, log_info)
        else:
            logger.info({
                'run': 'gen_nil',
                'sample_gold_linked_dir': sample_gold_linked_dir,
                'nil_file': data_info_prep.nil_file
            })
            gen_nil_info(sample_gold_linked_dir, data_info_prep.nil_file, log_info)

    if gen_attr_rng:

        if conv_year:
            # gen_attr_rng_info(sample_gold_linked_dir_conv, data_info_prep.attr_rng_auto_file,
            #                   data_info_prep.attr_rng_man_file, data_info_prep.attr_rng_merged_file, log_info)
            gen_attr_rng_info(sample_gold_linked_dir_conv, data_info_prep.attr_rng_auto_file, log_info)
            logger.info({
                'run': 'gen_attr_rng',
                'sample_gold_linked_dir_conv': sample_gold_linked_dir_conv,
                'attr_rng_auto_file': data_info_prep.attr_rng_auto_file,
                # 'attr_rng_man_file': data_info_prep.attr_rng_man_file,
                # 'attr_rng_merged_file': data_info_prep.attr_rng_merged_file,
            })
        else:
            # gen_attr_rng_info(sample_gold_linked_dir, data_info_prep.attr_rng_auto_file,
            #                   data_info_prep.attr_rng_man_file, data_info_prep.attr_rng_merged_file,  log_info)
            gen_attr_rng_info(sample_gold_linked_dir, data_info_prep.attr_rng_auto_file, log_info)
            logger.info({
                'run': 'gen_attr_rng',
                'sample_gold_linked_dir': sample_gold_linked_dir,
                'attr_rng_auto_file': data_info_prep.attr_rng_auto_file,
                # 'attr_rng_man_file': data_info_prep.attr_rng_man_file,
                # 'attr_rng_merged_file': data_info_prep.attr_rng_merged_file,
            })

    if gen_slink:

        if conv_year:
            logger.info({
                'run': 'gen_slink',
                'sample_gold_linked_dir_conv': sample_gold_linked_dir_conv,
                'slink_file': data_info_prep.slink_file
            })
            gen_self_link_info(sample_gold_linked_dir_conv, data_info_prep.slink_file, log_info)
        else:
            logger.info({
                'run': 'gen_slink',
                'sample_gold_linked_dir': sample_gold_linked_dir,
                'slink_file': data_info_prep.slink_file
            })
            gen_self_link_info(sample_gold_linked_dir, data_info_prep.slink_file, log_info)

        gen_self_link_by_attr_name(data_info_prep.self_link_pat_file, data_info_prep.target_attr_file,
                                  data_info_prep.self_link_by_attr_name_file, log_info)

    if gen_linkable:

        if conv_year:
            logger.info({
                'run': 'gen_linkable',
                'sample_input_ene_dir': sample_input_ene_dir,
                'sample_gold_linked_dir_conv': sample_gold_linked_dir_conv,
                'linkable_file': data_info_prep.linkable_file
            })
            gen_linkable_info(sample_input_ene_dir_conv, sample_gold_linked_dir_conv, data_info_prep.linkable_file, log_info)
        else:
            logger.info({
                'run': 'gen_linkable',
                'sample_input_ene_dir': sample_input_ene_dir,
                'sample_gold_linked_dir': sample_gold_linked_dir,
                'linkable_file': data_info_prep.linkable_file
            })
            gen_linkable_info(sample_input_ene_dir, sample_gold_linked_dir, data_info_prep.linkable_file, log_info)


def conv_link_pageid(linked_dir, conv_dir, page_change_list, log_info):
    """
    Convert pageids in input files into new pageids and output new json files
    :param linked_dir:
    :param conv_dir:
    :param page_change_list:
    :param log_info:
    :return:
    """
    import os
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    check_new_id = {}
    with open(page_change_list, mode='r', encoding='utf-8') as ci:
        ci_reader = csv.reader(ci, delimiter='\t')
        for ci_line in ci_reader:
            old_id = ci_line[0]
            new_id = ci_line[1]
            check_new_id[old_id] = new_id

    in_files = linked_dir + '*.jsonl'

    for in_file in glob(in_files):
        logger.info({
            'action': 'cnv_ene_pageid',
            'in_file': in_file,
        })
        dic_list = []
        with open(in_file, mode='r', encoding='utf-8') as i:
            for i_line in i:
                d = json.loads(i_line)
                pid = d['page_id']
                if pid in check_new_id:
                    d['page_id'] = check_new_id[pid]
                lid = d['link_page_id']
                if lid in check_new_id:
                    d['link_page_id'] = check_new_id[lid]
                dic_list.append(d)

        out_file_name = in_file.replace(linked_dir, '')
        out_file_path = conv_dir + out_file_name
        os.makedirs(conv_dir, exist_ok=True)

        with open(out_file_path, mode='w', encoding='utf-8') as o:
            for dic in dic_list:
                json.dump(dic, o, ensure_ascii=False)
                o.write('\n')


def conv_input_pageid(input_dir, conv_dir, page_change_list, log_info):
    """
    Convert pageids in input files into new pageids and output new json files
    :param input_dir:
    :param conv_dir:
    :param page_change_list:
    :param log_info:
    :return:
    """
    import os
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    check_new_id = {}
    with open(page_change_list, mode='r', encoding='utf-8') as ci:
        ci_reader = csv.reader(ci, delimiter='\t')
        for ci_line in ci_reader:
            old_id = ci_line[0]
            new_id = ci_line[1]
            check_new_id[old_id] = new_id

    in_files = input_dir + '*.jsonl'

    for in_file in glob(in_files):
        logger.info({
            'action': 'cnv_ene_pageid',
            'in_file': in_file,
        })
        dic_list = []
        with open(in_file, mode='r', encoding='utf-8') as i:

            for i_line in i:
                d = json.loads(i_line)
                pid = d['page_id']
                if pid in check_new_id:
                    d['page_id'] = check_new_id[pid]
                dic_list.append(d)

        out_file_name = in_file.replace(input_dir, '')
        out_file_path = conv_dir + out_file_name
        os.makedirs(conv_dir, exist_ok=True)
        with open(out_file_path, mode='w', encoding='utf-8') as o:
            for dic in dic_list:
                json.dump(dic, o, ensure_ascii=False)
                o.write('\n')


def gen_input_title_file(in_ene_dir, input_title_file, log_info):
    """extract page titles from input files
    args:
        in_ene_dir
        input_title_file
        log_info
    output:
        input_title_file
    """
    import pandas as pd

    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    in_files = in_ene_dir + '*.jsonl'
    check = {}
    for in_file in glob(in_files):
        logger.info({
            'action': 'extract_input_title',
            'in_file': in_file,
        })
        with open(in_file, mode='r', encoding='utf-8') as i:
            for i_line in i:
                rec = json.loads(i_line)
                title = rec['title']
                if not check.get(title):
                    check[title] = 1

    title_list = list(check.keys())
    df = pd.DataFrame(title_list)
    df.to_csv(input_title_file, sep='\t', header=False, index=False)

# def gen_sample_pid_title_file(sample_in_ene_dir, sample_pid_title_file, log_info):
#     """extract pageid and page titles from sample files
#     args:
#         sample_in_ene_dir
#         input_title_file
#         log_info
#     output:
#         input_title_file
#     """
#     import pandas as pd
#
#     logger = set_logging_pre(log_info, 'myPreLogger')
#     logger.setLevel(logging.INFO)
#
#     in_files = in_ene_dir + '*.jsonl'
#     check = {}
#     for in_file in glob(in_files):
#         logger.info({
#             'action': 'extract_input_title',
#             'in_file': in_file,
#         })
#         with open(in_file, mode='r', encoding='utf-8') as i:
#             for i_line in i:
#                 rec = json.loads(i_line)
#                 title = rec['title']
#                 if not check.get(title):
#                     check[title] = 1
#
#     title_list = list(check.keys())
#     df = pd.DataFrame(title_list)
#     df.to_csv(input_title_file, sep='\t', header=False, index=False)


# 20220822
# def prematch_mention_title(data_info_prep, pre_matching, title_matching, char_match_min, log_info):
def prematch_mention_title(in_ene_dir, data_info_prep, pre_matching, title_matching, char_match_min, log_info):
    """Pre-matching mention title.
    args:
        in_ene_dir,
        data_info_prep:
        pre_matching
        title_matching
        char_match_min
        log_info
    output:
        match_info_file
       　　 format:
                mention(\t)pid(\t)title(\t)ratio
           sample(mint):
                湖      401     湖国    0.5
                湖      9322    琵琶湖  0.33
                湖      1431634 湖      1.0
    Note:
        pre_matching
            tinm: partial match (title in mention text)
            mint: partial match (mention text in title)
        char_match_min
            minimum ratio of matching
            (tinm)  title length / mention length
            (mint)  mention length / title length
        title_matching
            If title_matching option is set to 'trim',
            the ratio is calculated based on title_trimmed.
        Titles composed of single kana characters are ignored.

    """
    import re
    import os
    import pandas as pd
    import ljc_common as lc
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    # in_files = data_info_prep.in_dir + '*.jsonl'

    if not os.path.exists(in_ene_dir):
        logger.error({
            'action': 'prematch_mention_title',
            'msg': 'illegal in_ene_dir',
            'in_ene_dir': in_ene_dir
        })

    # 20220822
    in_files = in_ene_dir + '*.jsonl'
    logger.info({
        'action': 'prematch_mention_title',
        'in_files': in_files,
    })
    d_pid2fromtitle = reg_pid2title(data_info_prep.title2pid_ext_file, log_info)

    tinm_partial_file = ''
    mint_partial_file = ''
    if pre_matching == 'tinm':
        if title_matching == 'trim':
            tinm_partial_file = data_info_prep.tinm_trim_partial_file
        else:
            tinm_partial_file = data_info_prep.tinm_partial_file
        logger.info({
            'action': 'prematch_mention_title',
            'pre_matching': pre_matching,
            'title_matching': title_matching,
            'tinm_partial_file': tinm_partial_file
        })
    elif pre_matching == 'mint':
        if title_matching == 'trim':
            mint_partial_file = data_info_prep.mint_trim_partial_file
        else:
            mint_partial_file = data_info_prep.mint_partial_file
        logger.info({
            'action': 'prematch_mention_title',
            'pre_matching': pre_matching,
            'title_matching': title_matching,
            'mint_partial_file': mint_partial_file
        })

    d_mention_pid_title_check = {}
    num_jsymbol_kana_pat = re.compile('^[\u0030-\u0039\u3000-\u303F\u3041-\u309F\u30A1-\u30FF]$')
    cols = ['mention', 'pid', 'title', 'ratio']

    df = pd.DataFrame(columns=cols)

    for in_file in glob(in_files):
        logger.info({
            'action': 'prematch_mention_title',
            'in_file': in_file,
        })
        with open(in_file, mode='r', encoding='utf-8') as i:
            fname = in_file.replace(in_ene_dir, '')
            # fname = in_file.replace(data_info_prep.in_dir, '')
            # ene_cat = fname.replace('.json', '')

            ene_cat = lc.extract_cat(fname, log_info)
            if ene_cat == '':
                logger.error({
                    'action': 'prematch_mention_title',
                    'msg': 'illegal file name',
                    'fname': fname
                })

            for i_line in i:
                rec = json.loads(i_line)
                mention = rec['text_offset']['text']
                for pid, title_list in d_pid2fromtitle.items():
                    for title in title_list:
                        # single character (num, jsymbol, kana)
                        if num_jsymbol_kana_pat.fullmatch(title):
                            continue
                        tmp_title = title
                        if title_matching == 'trim':
                            if ' (' in title:
                                title_trimmed = title
                                title_trimmed = title_trimmed.replace(' (', '\t')
                                trimmed_list = re.split('\t', title_trimmed)
                                if trimmed_list[-1].endswith('年'):
                                    logger.debug({
                                        'action': 'prematch_mention_title',
                                        'title_matching': title_matching,
                                        'org_title': title,
                                        'warning': 'title has multiple pairs of braces but ignored for it ends with 年',
                                        'title_list': trimmed_list,
                                    })
                                    pass
                                else:
                                    trimmed_list.pop()
                                    tmp_title = ' ('.join(trimmed_list)
                                    # single characters (num, jsymbol, kana)
                                    if num_jsymbol_kana_pat.fullmatch(tmp_title):
                                        continue
                                    else:
                                        if len(trimmed_list) > 2:
                                            logger.debug({
                                                'action': 'prematch_mention_title',
                                                'mention': mention,
                                                'debug': 'title has multiple pairs of braces'
                                                         ' (only the last has deleted)',
                                                'org_title': title,
                                                'tmp_title (trimmed for ratio)': tmp_title,
                                                'title_list': trimmed_list
                                            })
                                            pass
                        ratio = 0.0
                        if pre_matching == 'tinm' and tmp_title in mention:
                            ratio_str = str(len(tmp_title) / len(mention))
                            ratio = float(Decimal(ratio_str).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
                        elif pre_matching == 'mint' and mention in tmp_title:
                            ratio_str = str(len(mention) / len(tmp_title))
                            ratio = float(Decimal(ratio_str).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
                        else:
                            continue
                        if ratio < char_match_min:
                            continue
                        else:
                            mention_pid_title = mention + '\t' + pid + '\t' + title
                            if not d_mention_pid_title_check.get(mention_pid_title):
                                df = df.append({'mention': mention, 'pid': pid, 'title': title, 'ratio': ratio},
                                               ignore_index=True)
                                d_mention_pid_title_check[mention_pid_title] = 1
    df_new = df.sort_values(['mention', 'ratio'], ascending=[True, False])

    if pre_matching == 'tinm':
        df_new.to_csv(tinm_partial_file, sep='\t', header=False, index=False)

    if pre_matching == 'mint':
        df_new.to_csv(mint_partial_file, sep='\t', header=False, index=False)

def gen_html_info_file_conv_year(html_dir, html_info_file, change_id_list, log_info):
    """Analyse given html files and extract WikiLink info. Convert old pageids to new ones.
    Args:
        html_dir(str)
        html_info_file(str)
        change_id_list
        log_info
    Returns:

    Output:
        html_info_file
    Notice:
        html_info_file
            format
                cat(\t)pid(\t)line_id(\t)start(\t)end(\t)text(\t)title(\n)
    Notice:
        - line_id = line number - 1
        - html_files(*.html) should be located at html_dir/*/.
        - disambiguation pattern (dis_pat_title_head) includes 'jawiki-20190120' should be revised when using data
        based on other Wikipedia dumps.
    """
    import re
    from bs4 import BeautifulSoup
    from glob import glob
    import csv
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    html_files = html_dir + '*/*.html'
    logger.info({
        'action': 'gen_html_info_file_conv_year',
        'html_files': html_files,
    })
    dis_pat_title_head = ('jawiki-20190120:', '特別:', 'Wikipedia_Dump', 'Wikipedia Dump', 'ファイル:', 'テンプレート:',
                          'プロジェクト:', 'カテゴリ:', 'ヘルプ:', 'Portal:',  'wikipedia:', '節を編集', 'このページ')
    dis_pat_title_partial = ('\/', '言語間リンクを追加する', '情報を得る場所', 'プロジェクトについて', 'スタブ項目', 'に移動する',
                             'あるページ', 'ある記事')

    check_new_id = {}
    with open(change_id_list, mode='r', encoding='utf-8') as ci:
        ci_reader = csv.reader(ci, delimiter='\t')
        for ci_line in ci_reader:
            old_id = ci_line[0]
            new_id = ci_line[1]
            check_new_id[old_id] = new_id

    html_info_list = []

    for filename in glob(html_files):
        cat_pre = re.split('/', filename.replace(html_dir, ''))
        cat = cat_pre[0]
        fname = cat_pre[1]
        fname = fname.replace('.html', '')

        logger.info({
            'action': 'gen_html_info_file_conv_year',
            'filename': filename,
            'fname': fname,
        })

        if fname in check_new_id:
            fname = check_new_id[fname]
            logger.info({
                'action': 'gen_html_info_file_conv_year',
                'msg': 'pageid changed',
                'filename': filename,
                'fname(new_pageid)': fname,
            })

        with open(filename, 'r', encoding='utf-8') as f:
            logger.info({
                'action': 'gen_html_info_file_conv_year',
                'filename': filename,
            })
            check_elm = {}

            line_num = 0
            for line in f:

                line_num += 1
                line_id = line_num - 1

                soup = BeautifulSoup(line, 'html.parser')
                try:
                    links = soup.find_all('a')
                except(NameError, ValueError):
                    continue

                # start = 0
                for link in links:
                    tmp_title = ''
                    logger.debug({
                        'action': 'gen_html_info_file_conv_year',
                        'link': link,
                    })
                    try:
                        # href_char = link.get('href_char')
                        href_char = link.get('href')

                        if href_char:
                            logger.debug({
                                'action': 'gen_html_info_file_conv_year',
                                'href_char(before)': href_char
                            })
                            # 20220819 tag for edition
                            # <a href="/w/index.php?title=%E7%89%B9%E5%88%A5:%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E4%BD%9C%E6%88%90&amp;returnto=.tw&amp;returntoquery=curid%3D1357468" class="vector-menu-content-item user-links-collapsible-item" title="アカウントを作成してログインすることをお勧めしますが、必須ではありません">
                            if ('action=edit' in href_char) or ('returntoquery' in href_char) or (
                                    'en.wikipedia.org' in href_char):
                                continue
                            # elif 'index' not in href_char:
                            #     logger.info({
                            #         'action': 'gen_html_info_file_conv_year',
                            #         'no index in href_char': href_char
                            #     })
                            #     continue
                            # included in action=edit
                            # elif 'redlink' in href_char:
                            #     continue
                            logger.debug({
                                'action': 'gen_html_info_file_conv_year',
                                'href_char(after)': href_char
                            })

                    except(NameError, ValueError):
                        continue

                    if 'rel' in link.attrs and 'nofollow' in link.attrs['rel']:
                        logger.debug({
                            'action': 'gen_html_info_file_conv_year',
                            'attrs(rel)': link.attrs,
                            'rel(nofollow)': link.attrs['rel']
                        })
                        continue
                    if 'accesskey' in link.attrs:
                        logger.debug({
                            'action': 'gen_html_info_file_conv_year',
                            'attrs(accesskey)': link.attrs,
                        })
                        continue
                    if 'class' in link.attrs:
                        tmp_class = link.attrs['class']
                        if len(tmp_class[0]) > 0 and 'mw-redirect' not in tmp_class[0]:
                            logger.debug({
                                'action': 'gen_html_info_file_conv_year',
                                'not mw-redirect': tmp_class[0],
                            })
                            continue
                    if 'title' not in link.attrs:
                        logger.debug({
                            'action': 'gen_html_info_file_conv_year',
                            'attrs(no title)': link.attrs,
                        })
                        continue
                    tmp_title = link.attrs['title']
                    logger.debug({
                        'action': 'gen_html_info_file_conv_year',
                        'tmp_title': tmp_title,
                    })
                    if len(tmp_title) == 0:
                        logger.debug({
                            'action': 'gen_html_info_file_conv_year',
                            'len(tmp_title) zero': len(tmp_title),
                            'tmp_title': tmp_title
                        })
                        continue
                    elif tmp_title.startswith(dis_pat_title_head):
                        logger.debug({
                            'action': 'gen_html_info_file_conv_year',
                            'tmp_title(start)': tmp_title
                        })
                        continue
                    else:
                        check_hit = 0
                        for t in dis_pat_title_partial:
                            if t in tmp_title:
                                check_hit = 1
                                break
                        if check_hit == 1:
                            continue
                    if not link.text:
                        continue
                    if len(link.text) == 0:
                        continue
                    elif link.text == '^':
                        continue
                    elif link.text not in line:
                        continue
                    # wikipedia link pattern (including symbols)
                    regex_pat = re.escape('>' + link.text + '<')

                    try:
                        taglist = list(re.finditer(regex_pat, line))
                    except ValueError:
                        continue
                    for tag in taglist:
                        logger.debug({
                            'action': 'gen_html_info_file_conv_year',
                            'tag': tag
                        })
                        # excluding symbols
                        text_start = tag.start() + 1
                        text_end = tag.end() - 1
                        if text_start >= 1:
                            tmp_dict = {'cat': cat, 'pid': fname, 'line_id': str(line_id),
                                        'html_text_start': str(text_start), 'html_text_end': str(text_end),
                                        'html_text': link.text, 'title': tmp_title}
                            elm = '_'.join([str(line_id), str(text_start), str(text_end)])
                            if not check_elm.get(elm):
                                check_elm[elm] = 1
                                html_info_list.append(tmp_dict)
                                logger.debug({
                                    'action': 'gen_html_info_file_conv_year',
                                    'cat': cat,
                                    'pid': fname,
                                    'line_id': str(line_id),
                                    'html_text_start': str(text_start),
                                    'html_text_end': str(text_end),
                                    'html_text': link.text,
                                    'title': tmp_title
                                })

    labels = ['cat', 'pid', 'line_id', 'html_text_start', 'html_text_end', 'html_text', 'title']

    with open(html_info_file, 'w') as o:
        writer = csv.DictWriter(o, fieldnames=labels, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        for elem in html_info_list:
            writer.writerow(elem)


def gen_html_info_file(html_dir, html_info_file, log_info):
    """Analyse given html files and extract WikiLink info.
    Args:
        html_dir(str)
        html_info_file(str)
        log_info
    Returns:

    Output:
        html_info_file
    Notice:
        html_info_file
            format
                cat(\t)pid(\t)line_id(\t)start(\t)end(\t)text(\t)title(\n)
    Notice:
        - line_id = line number - 1
        - html_files(*.html) should be located at html_dir/*/.
        - disambiguation pattern (dis_pat_title_head) includes 'jawiki-20190120' should be revised when using data
        based on other Wikipedia dumps.
    """
    import re
    from bs4 import BeautifulSoup
    from glob import glob
    import csv
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    html_files = html_dir + '*/*.html'
    logger.info({
        'action': 'gen_html_info_file',
        'html_files': html_files,
    })
    dis_pat_title_head = ('jawiki-20190120:', '特別:', 'Wikipedia_Dump', 'Wikipedia Dump', 'ファイル:', 'テンプレート:',
                          'プロジェクト:', 'カテゴリ:', 'ヘルプ:', 'Portal:',  'wikipedia:', '節を編集', 'このページ')
    dis_pat_title_partial = ('\/', '言語間リンクを追加する', '情報を得る場所', 'プロジェクトについて', 'スタブ項目', 'に移動する',
                             'あるページ', 'ある記事')
    html_info_list = []

    for filename in glob(html_files):
        cat_pre = re.split('/', filename.replace(html_dir, ''))
        cat = cat_pre[0]
        fname = cat_pre[1]
        fname = fname.replace('.html', '')

        logger.info({
            'action': 'gen_html_info_file',
            'filename': filename,
            'fname': fname,
        })


        with open(filename, 'r', encoding='utf-8') as f:
            logger.info({
                'action': 'gen_html_info_file',
                'filename': filename,
            })
            check_elm = {}

            line_num = 0
            for line in f:

                line_num += 1
                line_id = line_num - 1

                soup = BeautifulSoup(line, 'html.parser')
                try:
                    links = soup.find_all('a')
                except(NameError, ValueError):
                    continue

                # start = 0
                for link in links:
                    tmp_title = ''
                    logger.debug({
                        'action': 'gen_html_info_file',
                        'link': link,
                    })
                    try:
                        # href_char = link.get('href_char')
                        href_char = link.get('href')

                        if href_char:
                            logger.debug({
                                'action': 'gen_html_info_file',
                                'href_char(before)': href_char
                            })
                            # 20220819 tag for edition
                            # <a href="/w/index.php?title=%E7%89%B9%E5%88%A5:%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E4%BD%9C%E6%88%90&amp;returnto=.tw&amp;returntoquery=curid%3D1357468" class="vector-menu-content-item user-links-collapsible-item" title="アカウントを作成してログインすることをお勧めしますが、必須ではありません">
                            if ('action=edit' in href_char) or ('returntoquery' in href_char) or (
                                    'en.wikipedia.org' in href_char):
                                continue
                            # elif 'index' not in href_char:
                            #     logger.info({
                            #         'action': 'gen_html_info_file',
                            #         'no index in href_char': href_char
                            #     })
                            #     continue
                            # included in action=edit
                            # elif 'redlink' in href_char:
                            #     continue
                            logger.debug({
                                'action': 'gen_html_info_file',
                                'href_char(after)': href_char
                            })

                    except(NameError, ValueError):
                        continue

                    if 'rel' in link.attrs and 'nofollow' in link.attrs['rel']:
                        logger.debug({
                            'action': 'gen_html_info_file',
                            'attrs(rel)': link.attrs,
                            'rel(nofollow)': link.attrs['rel']
                        })
                        continue
                    if 'accesskey' in link.attrs:
                        logger.debug({
                            'action': 'gen_html_info_file',
                            'attrs(accesskey)': link.attrs,
                        })
                        continue
                    if 'class' in link.attrs:
                        tmp_class = link.attrs['class']
                        if len(tmp_class[0]) > 0 and 'mw-redirect' not in tmp_class[0]:
                            logger.debug({
                                'action': 'gen_html_info_file',
                                'not mw-redirect': tmp_class[0],
                            })
                            continue
                    if 'title' not in link.attrs:
                        logger.debug({
                            'action': 'gen_html_info_file',
                            'attrs(no title)': link.attrs,
                        })
                        continue
                    tmp_title = link.attrs['title']
                    logger.debug({
                        'action': 'gen_html_info_file',
                        'tmp_title': tmp_title,
                    })
                    if len(tmp_title) == 0:
                        logger.debug({
                            'action': 'gen_html_info_file',
                            'len(tmp_title) zero': len(tmp_title),
                            'tmp_title': tmp_title
                        })
                        continue
                    elif tmp_title.startswith(dis_pat_title_head):
                        logger.debug({
                            'action': 'gen_html_info_file',
                            'tmp_title(start)': tmp_title
                        })
                        continue
                    else:
                        check_hit = 0
                        for t in dis_pat_title_partial:
                            if t in tmp_title:
                                check_hit = 1
                                break
                        if check_hit == 1:
                            continue
                    if not link.text:
                        continue
                    if len(link.text) == 0:
                        continue
                    elif link.text == '^':
                        continue
                    elif link.text not in line:
                        continue
                    # wikipedia link pattern (including symbols)
                    regex_pat = re.escape('>' + link.text + '<')

                    try:
                        taglist = list(re.finditer(regex_pat, line))
                    except ValueError:
                        continue
                    for tag in taglist:
                        logger.debug({
                            'action': 'gen_html_info_file',
                            'tag': tag
                        })
                        # excluding symbols
                        text_start = tag.start() + 1
                        text_end = tag.end() - 1
                        if text_start >= 1:
                            tmp_dict = {'cat': cat, 'pid': fname, 'line_id': str(line_id),
                                        'html_text_start': str(text_start), 'html_text_end': str(text_end),
                                        'html_text': link.text, 'title': tmp_title}
                            elm = '_'.join([str(line_id), str(text_start), str(text_end)])
                            if not check_elm.get(elm):
                                check_elm[elm] = 1
                                html_info_list.append(tmp_dict)
                                logger.debug({
                                    'action': 'gen_html_info_file',
                                    'cat': cat,
                                    'pid': fname,
                                    'line_id': str(line_id),
                                    'html_text_start': str(text_start),
                                    'html_text_end': str(text_end),
                                    'html_text': link.text,
                                    'title': tmp_title
                                })

    labels = ['cat', 'pid', 'line_id', 'html_text_start', 'html_text_end', 'html_text', 'title']

    with open(html_info_file, 'w') as o:
        writer = csv.DictWriter(o, fieldnames=labels, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        for elem in html_info_list:
            writer.writerow(elem)


def reg_pid2title(title2pid_ext_file, log_info):

    """Register title2pid_info pages info.
    Args:
        title2pid_ext_file
        log_info
    Returns:
        d_pid2fromtitle dict
            {pid: [title1, title2, ....]}

    Notice:
        - title2pid_ext_file
            format: 'from_title'\t'to_pid'\t'to_title'\t'to_incoming\t'to_eneid'
       　　　sample:
            エチオピア人民民主共和国	1443906	エチオピア	2427	1.5.1.3
            エチオピア連邦民主共和国	1443906	エチオピア	2427	1.5.1.3
            社会主義エチオピア	1443906	エチオピア	2427	1.5.1.3
            エティオピア	1443906	エチオピア	2427	1.5.1.3
            エチオピア人	1443906	エチオピア	2427	1.5.1.3
            Ethiopia	1443906	エチオピア	2427	1.5.1.3
            エチオピア	1443906	エチオピア	2427	1.5.1.3

    """
    import csv
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    d_pid2fromtitle = {}

    with open(title2pid_ext_file, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        for rows in reader:
            from_title = rows[0]
            to_pid_str = rows[1]
            if not d_pid2fromtitle.get(to_pid_str):
                d_pid2fromtitle[to_pid_str] = []
            d_pid2fromtitle[to_pid_str].append(from_title)
    return d_pid2fromtitle


def gen_title2pid_ext_file(exfile, incoming, enew_info, redirect_info, log_info):
    """gen_title2pid_ext_filemerge title2pid info.
     Args:
         exfile
         incoming
         enew_info
         redirect_info
         log_info
     output:
        f_title2pid_ext
            format
                (title(from page))\t(pageid(to page))\t(title(to page)\t(maximum number of incoming links(to page))
                \t(eneid(to_page))
            sample
                アメリカ合衆国  1698838 アメリカ合衆国  116818  1.5.1.3
                ユナイテッドステイツ    1698838 アメリカ合衆国  116818  1.5.1.3
                亜米利加合衆国  1698838 アメリカ合衆国  116818  1.5.1.3
                U.S.    1698838 アメリカ合衆国  116818  1.5.1.3
                USA     1698838 アメリカ合衆国  116818  1.5.1.3
                アメリカ        1698838 アメリカ合衆国  116818  1.5.1.3
     Notice:
         - redirect info
        　　
            - The from_title to_page pairs in the redirect file are originally defined in
            jawiki-202190120-title2pageid.json.
            - In the redirect info,
                - white spaces in Wikipedia titles are replaced by '_'.
                - Some records with illegal formats (eg. lack of to_pageid) are deleted.
                - Disambiguation pages are deleted (although not always completely).
        -incoming: pageid, title, maximum number of incoming_links
                   ('jawiki-20190121-cirrussearch-content_incoming_link.tsv')
            -format: <pageid>\t<title>\t<maximum num of incoming_links>
            -sample
                2264978 マーキング      23
                662923  ノワール        32
        -enew_info: ENEW info(based on slightly modified version of ENEW 20210427）
            - format: <pageid>\t<ENEID>\t<page title>
            - sample
                72942  1.2     バックス (ローマ神話)
                401755  1.1     覚信尼
            - modification list: ENEW_ENEtag_20200427_stoplist.tsv (ENEID, pid, title)
        - Some pages lack incoming info or enew info.

    """
    import pandas as pd
    import csv
    import sys
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    redirect_info = redirect_info
    enew_info = enew_info
    incoming = incoming
    exfile = exfile

    logger.info({
        'action': 'gen_title2pid_ext_file',
        'enew_info': enew_info,
        'incoming': incoming,
        'exfile': exfile,
    })
    get_to_ene = {}
    get_to_title = {}

    with open(enew_info) as e:
        reader = csv.reader(e, delimiter='\t')
        for row in reader:
            try:
                to_pid = row[0]
                to_eneid = row[1]
                to_title = row[2]
            except ValueError as e:
                logger.error({
                    'action': 'gen_title2pid_ext_file',
                    'file': enew_info,
                    'error': e,
                    'row': row
                })
                sys.exit()
            get_to_ene[to_pid] = to_eneid
            get_to_title[to_pid] = to_title

    get_to_incoming = {}
    with open(incoming) as i:
        reader = csv.reader(i, delimiter='\t')

        for row in reader:
            try:
                to_pid = row[0]
                to_title = row[1]
                to_incoming = row[2]
            except ValueError as ie:
                logger.error({
                    'action': 'gen_title2pid_ext_file',
                    'file': incoming,
                    'to_pid': to_pid,
                    'error': ie,
                    'row': row
                })
                sys.exit()
            get_to_incoming[to_pid] = to_incoming

            # Complement titles for ENEW file lacks some pages.
            if not get_to_title.get(to_pid):
                get_to_title[to_pid] = to_title

    with open(redirect_info) as e:
        reader = csv.reader(e, delimiter='\t')
        rec_list = []
        # Some pages lack incoming or ENEW information
        for row in reader:
            rec = []
            from_title = ''
            to_incoming = 0
            to_eneid = ''
            from_title = row[0]
            to_pid = row[1]
            if not from_title:
                logger.error({
                    'action': 'gen_title2pid_ext_file',
                    'missing from_title': row
                })
                sys.exit()
            if not to_pid:
                logger.error({
                    'action': 'gen_title2pid_ext_file',
                    'missing to_pid': row
                })
                sys.exit()
            # Complement titles for ENEW file lacks some pages.
            if get_to_title.get(to_pid):
                to_title = get_to_title[to_pid]
                if not to_title:
                    logger.warning({
                        'action': 'gen_title2pid_ext_file',
                        'missing to_title': to_pid
                    })
            if get_to_incoming.get(to_pid):
                to_incoming = get_to_incoming[to_pid]
                if not to_incoming:
                    logger.error({
                        'action': 'gen_title2pid_ext_file',
                        'to_pid': to_pid,
                        'error': 'invalid incoming'
                    })
                    sys.exit()
                else:
                    to_incoming = int(to_incoming)

            if get_to_ene.get(to_pid):
                to_eneid = get_to_ene[to_pid]
                if not to_eneid:
                    logger.warning({
                        'action': 'gen_title2pid_ext_file',
                        'missing to_eneid': to_eneid
                    })

            rec = [from_title, to_pid, to_title, to_incoming, to_eneid]
            rec_list.append(rec)

        df = pd.DataFrame(rec_list, columns=['from_title', 'to_pid', 'to_title', 'to_incoming', 'to_eneid'])
        new_df = df.sort_values('to_incoming', ascending=False)
        new_df.to_csv(exfile, sep='\t', header=False, index=False)


def get_category(fname, dname, ext, log_info):
    """ get category label from the file name
    :param fname:
    :param dname:
    :param ext:
    :param log_info
    :return: cat
    """
    import logging
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    cat_pre = fname.replace(dname, '')
    cat_new = cat_pre.replace(ext, '')
    return cat_new


def check_self(row, log_info):
    """check if self-link
    :param row:
    :param log_info:
    :return: 1 (self), 0 (non-self)
    """
    import logging
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    # 20220825 from here
    if row[1] == row[9]:
        # if row[0] == row[8]:
        # till here
        return 1
    else:
        return 0


def gen_linkable_info(sample_e_dir, sample_g_dir, linkable_info_file, log_info):
    """Generate linkable info
    args:
        sample_in_ene_dir
        sample_gold_linked_dir
        linkable_info_file:
        log_info:
    return:
    output:
        linkable_info_file
    Note:
        gold file
            Gold files (eg. sample gold files) used for linkable estimation should be located in gold_dir.
            sample
                City 3623607	下半山村	合併市区町村	三間ノ川村	61	39	61	44	29489	高岡　1.5.1.1
                City 3623607	下半山村	合併市区町村	三間ノ川村	61	39	61	44	3623607	下半山村　1.5.1.1
    """
    import logging
    import ljc_common as lc

    import pandas as pd
    import re
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)
    logger.info({
        'action': 'ljc_prep_main',
        'start': 'gen_linkable_info',
        'sample_dir': sample_e_dir,
        'gold_dir': sample_g_dir,
        'linkable_info_file': linkable_info_file
    })
    prt_list = []

    ene = sample_e_dir + '*.jsonl'
    gold = sample_g_dir + '*.jsonl'

    count_e_cat_attr = {}
    count_g_cat_attr = {}

    for ene_file in glob(ene):
        with open(ene_file, mode='r', encoding='utf-8') as ef:
            e_fname = ene_file.replace(sample_e_dir, '')
            # e_cat = e_fname.replace('.json', '')

            e_cat = lc.extract_cat(e_fname, log_info)
            if e_cat == '':
                logger.error({
                    'action': 'prematch_mention_title',
                    'msg': 'illegal file name',
                    'fname': e_fname
                })
                # 20220830
                sys.exit()

            logger.debug({
                'action': 'ljc_main',
                'ene_cat': e_cat,
                'e_fname': e_fname,
            })

            for e_line in ef:
                erec = json.loads(e_line)
                e_attr = erec['attribute']

                e_cat_attr = e_cat + ':' + e_attr

                if not count_e_cat_attr.get(e_cat_attr):
                    count_e_cat_attr[e_cat_attr] = 1
                else:
                    count_e_cat_attr[e_cat_attr] += 1

    for g_file in glob(gold):
        with open(g_file, mode='r', encoding='utf-8') as gf:
            g_fname = g_file.replace(sample_g_dir, '')
            # g_cat = g_fname.replace('.json', '')
            g_cat = lc.extract_cat(g_fname, log_info)
            if g_cat == '':
                logger.error({
                    'action': 'prematch_mention_title',
                    'msg': 'illegal file name',
                    'g_fname': g_fname
                })
                sys.exit()

            logger.debug({
                'action': 'ljc_main',
                'g_cat': g_cat,
                'g_fname': g_fname,
            })

            for g_line in gf:
                grec = json.loads(g_line)
                g_attr = grec['attribute']

                g_cat_attr = g_cat + ':' + g_attr

                # 20220831
                # check if link_pageid exists
                if grec['link_page_id']:
                    if not count_g_cat_attr.get(g_cat_attr):
                        count_g_cat_attr[g_cat_attr] = 1
                    else:
                        count_g_cat_attr[g_cat_attr] += 1

    for cat_attr in count_e_cat_attr:
        (t_cat, t_attr) = re.split(':', cat_attr)
        if count_g_cat_attr.get(cat_attr):
            t_ratio_str = count_g_cat_attr[cat_attr]/count_e_cat_attr[cat_attr]
            t_ratio = float(Decimal(t_ratio_str).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
        else:
            t_ratio = 0.0

        prt_list.append([t_cat, t_attr, t_ratio])

    sdf = pd.DataFrame(prt_list, columns=['cat', 'attr', 'ratio'])
    sdf.to_csv(linkable_info_file, sep='\t', header=False, index=False)


def gen_nil_info(gold_dir, nil_info_file, log_info):
    """Generate nil info
    args:
        gold_dir
        nil_info_file:
        log_info:
    return:
    output:
        nil_info_file
    Note:
        gold file
            Gold files (eg. sample gold files) used for self link estimation should be located in gold_dir.
            sample
                City 3623607	下半山村	合併市区町村	三間ノ川村	61	39	61	44	29489	高岡郡　1.5.1.1
                City 3623607	下半山村	合併市区町村	三間ノ川村	61	39	61	44	3623607	下半山村　1.5.1.1
    """
    import logging

    import pandas as pd
    import re
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)
    logger.info({
        'run': 'gen_nil_info',
        'gold_dir': gold_dir,
        'nil_info_file': nil_info_file
    })
    prt_list = []
    ext = '.tsv'

    gold = gold_dir + '*.tsv'
    logger.debug({
        'action': 'gen_nil_info',
        'gold': gold,
    })
    sumup_cat_attr = {}
    sumup_nil_cat_attr = {}

    for g_fname in glob(gold):
        cat = get_category(g_fname, gold_dir, ext, log_info)
        logger.debug({
            'action': 'gen_nil_info',
            'cat': cat,
            'g_fname': g_fname
        })
        check_gold = {}
        check_nil_gold = {}

        with open(g_fname, mode='r', encoding='utf-8') as f:
            greader = csv.reader(f, delimiter='\t')

            for grow in greader:
                # [cat, pid, title, at, text, start_line_id, start_offset, end_line_id, end_offset, link_id, link_title,
                # ene]

                # 20220825 from here
                # gold_key = '\t'.join(grow[0:8])
                gold_key = '\t'.join(grow[1:9])
                # till here
                logger.debug({
                    'action': 'gen_nil_info',
                    'gold_key': gold_key,
                })
                if not check_gold.get(gold_key):
                    check_gold[gold_key] = 1

                # nil
                if grow[9] == '':
                    if not check_nil_gold.get(gold_key):
                        check_nil_gold[gold_key] = 1
                    else:
                        check_nil_gold[gold_key] += 1

        for common_key in check_gold:
            common_key_list = re.split('\t', common_key)
            cat_attr = cat + '\t' + common_key_list[2]
            logger.debug({
                'action': 'gen_nil_info',
                'cat_attr': cat_attr,
                'common_key': common_key
            })
            #  'cat_attr': 'Academic\t種類', 'common_key': '10807\t工学\t種類\t学問\t65\t74\t65\t76'}

            if not sumup_cat_attr.get(cat_attr):
                sumup_cat_attr[cat_attr] = check_gold[common_key]
            else:
                sumup_cat_attr[cat_attr] += check_gold[common_key]

            if check_nil_gold.get(common_key):
                if not sumup_nil_cat_attr.get(cat_attr):
                    sumup_nil_cat_attr[cat_attr] = check_nil_gold[common_key]
                else:
                    sumup_nil_cat_attr[cat_attr] += check_nil_gold[common_key]

    for t_cat_attr in sumup_cat_attr:
        (t_cat, t_attr) = re.split('\t', t_cat_attr)
        if sumup_nil_cat_attr.get(t_cat_attr):
            t_ratio_str = sumup_nil_cat_attr[t_cat_attr]/sumup_cat_attr[t_cat_attr]
            t_ratio = float(Decimal(t_ratio_str).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
        else:
            t_ratio = 0.0
        logger.debug({
            'action': 'gen_nil_info',
            't_cat': t_cat,
            't_attr': t_attr,
            't_ratio': t_ratio
        })
        # 'action': 'gen_nil_info', 't_cat': 'Market', 't_attr': '旧称・前身', 't_ratio': 0.0}
        prt_list.append([t_cat, t_attr, t_ratio])

    sdf = pd.DataFrame(prt_list, columns=['cat', 'attr', 'ratio'])
    sdf.to_csv(nil_info_file, sep='\t', header=False, index=False)


# def gen_self_link_info(gold_dir, target_cat_attr_file, self_link_info_file, self_link_attr_info_file, log_info):
def gen_self_link_info(gold_dir, self_link_info_file, log_info):

    """Generate self link info
    args:
        gold_dir
        # target_cat_attr_file:
        self_link_info_file:
        # self_link_attr_info_file:
        log_info:
    return:
    output: (2)
        self_link_info_file

        School  別名    1.0       10    10
        School  標語    0.0        0     1
        School  種類    0.0        0     2
        
        # self_link_attr_info_file
        # 別名  1.0   100  100
        # 標語　0.0     0   10
        # 種類　0.0     0   20
    Note:
        gold file
            Gold files (eg. sample gold files) used for self link estimation should be located in gold_dir.
            sample
                City 3623607	下半山村	合併市区町村	三間ノ川村	61	39	61	44	29489	高岡郡 1.5.1.1
                City 3623607	下半山村	合併市区町村	三間ノ川村	61	39	61	44	3623607	下半山村 1.5.1.1

    """
    import logging

    import pandas as pd
    import re
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)
    logger.debug({
        'run': 'gen_self_link_info',
        'gold_dir': gold_dir,
        # 'target_cat_attr_file': target_cat_attr_file,
        'self_link_info_file': self_link_info_file
    })
    prt_list = []
    ext = '.tsv'

    gold = gold_dir + '*.tsv'
    logger.debug({
        'action': 'gen_self_link_info',
        'gold': gold,
    })
    sumup_cat_attr = {}
    sumup_self_cat_attr = {}

    # 20220905
    sumup_self_attr = {}

    # 20220905
    # dict to check the target cat-attr combination
    # check_target_cat_attr = {}
    # with open(target_cat_attr_file, mode='r', encoding='utf-8') as tca:
    #     treader = csv.reader(tca, delimiter='\t')
    #
    #     for tline in treader:
    #         t_cat = tline[0]
    #         t_attr = tline[1]
    #         check_target_cat_attr[t_cat] = t_attr

    for g_fname in glob(gold):
        cat = get_category(g_fname, gold_dir, ext, log_info)
        logger.debug({
            'action': 'gen_self_link_info',
            'cat': cat,
            'g_fname': g_fname
        })
        check_gold = {}
        check_self_gold = {}

        with open(g_fname, mode='r', encoding='utf-8') as f:
            greader = csv.reader(f, delimiter='\t')

            for grow in greader:
                # 20220825 from here
                # gold_key = '\t'.join(grow[0:8])
                gold_key = '\t'.join(grow[1:9])
                # till here
                logger.debug({
                    'action': 'gen_self_link_info',
                    'gold_key': gold_key,
                })
                if not check_gold.get(gold_key):
                    check_gold[gold_key] = 1

                # self-link
                if check_self(grow, log_info):
                    if not check_self_gold.get(gold_key):
                        check_self_gold[gold_key] = 1
                    else:
                        check_self_gold[gold_key] += 1

        for common_key in check_gold:
            common_key_list = re.split('\t', common_key)
            attr = common_key_list[2]
            cat_attr = cat + '\t' + attr
            logger.debug({
                'action': 'gen_self_link_info',
                'cat_attr': cat_attr,
                'common_key': common_key
            })
            #  'cat_attr': 'Academic\t種類', 'common_key': '10807\t工学\t種類\t学問\t65\t74\t65\t76'}

            if not sumup_cat_attr.get(cat_attr):
                sumup_cat_attr[cat_attr] = check_gold[common_key]
            else:
                sumup_cat_attr[cat_attr] += check_gold[common_key]

            if check_self_gold.get(common_key):
                # sumup (cat, attr)
                if not sumup_self_cat_attr.get(cat_attr):
                    sumup_self_cat_attr[cat_attr] = check_self_gold[common_key]
                else:
                    sumup_self_cat_attr[cat_attr] += check_self_gold[common_key]

                # 20220905
                # sumup (attr)
                if not sumup_self_attr.get(attr):
                    sumup_self_attr[attr] = check_gold[common_key]
                else:
                    sumup_self_attr[attr] += check_gold[common_key]

    for t_cat_attr in sumup_cat_attr:
        (t_cat, t_attr) = re.split('\t', t_cat_attr)
        self_link_freq = 0
        cat_attr_freq = 0
        if sumup_self_cat_attr.get(t_cat_attr):
            self_link_freq = sumup_self_cat_attr[t_cat_attr]
            cat_attr_freq = sumup_cat_attr[t_cat_attr]
            t_ratio_str = sumup_self_cat_attr[t_cat_attr]/sumup_cat_attr[t_cat_attr]
            t_ratio = float(Decimal(t_ratio_str).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
        else:
            t_ratio = 0.0
        logger.debug({
            'action': 'gen_self_link_info',
            't_cat': t_cat,
            't_attr': t_attr,
            't_ratio': t_ratio
        })
        # 'action': 'gen_self_link_info', 't_cat': 'Market', 't_attr': '旧称・前身', 't_ratio': 0.0}
        # prt_list.append([t_cat, t_attr, t_ratio])
        # 20220905
        tmp_cat_attr = t_cat + '\t' + t_attr

        # prt_list.append([t_cat, t_attr, t_ratio, sumup_self_cat_attr[tmp_cat_attr], sumup_cat_attr[tmp_cat_attr]])
        prt_list.append([t_cat, t_attr, t_ratio, self_link_freq, cat_attr_freq])

    # for target_cat, target_attr in check_target_cat_attr.items():
    #     target_cat_attr = target_cat + '\t' + target_attr
    #     if target_cat_attr not in sumup_cat_attr:
    #         prt_list.append([target_cat, target_attr, '', 0, 0 ])

    sdf = pd.DataFrame(prt_list, columns=['cat', 'attr', 'ratio', 'freq', 'sum'])
    sdf.to_csv(self_link_info_file, sep='\t', header=False, index=False)


def get_to_pid_to_title_incoming_eneid(title2pid_ext_file, log_info):
    """Register title2pid_info pages info.
    Args:
        title2pid_ext_file
        #eg. イギリス語      3377    英語    95319   1.7.24.1
        log_info
    Returns:
        d_pid_title_incoming_eneid
            format
                key: to_pid
                val: to_title, to_incoming, to_eneid
            sample
                {'3377': ['英語', 95319','1.7.24.1'])
    Notice:
        - title2pid_title_ex
            format: 'from_title'\t'to_pid'\t'to_title'\t'to_incoming\t'to_eneid'

    """
    import csv
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    d_pid_title_incoming_eneid = {}

    with open(title2pid_ext_file, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            to_pid = str(row[1])
            to_title = row[2]
            to_incoming = row[3]
            to_eneid = str(row[4])
            d_pid_title_incoming_eneid[to_pid] = [to_title, to_incoming, to_eneid]
    return d_pid_title_incoming_eneid


def gen_back_link_info_file(ptitle_list, back_link, back_link_dump_org, ext_file, log_info):
    """
    get back link info and save in back link file
    :param ptitle_list: page title list of input files
    :param back_link:
    :param back_link_dump_org:
    :param ext_file:
    :param log_info:
    :return:
    :output: back_link_file
    :notice:
        back_link_dump_org:
            based on jawiki-20190120-pagelinks.sql
            lines including characters other than utf-8 are skipped.
            Some records of back_link_file may lack from titles.
            sample
                41246	1975年度新人選手選択会議_(日本プロ野球)
                92044	1975年度新人選手選択会議_(日本プロ野球)
                95956	1975年度新人選手選択会議_(日本プロ野球)
                143952	1975年度新人選手選択会議_(日本プロ野球)
        back_link_file:
            sample
                1975年度新人選手選択会議 (日本プロ野球) 41246   プロ野球ドラフト会議
                1975年度新人選手選択会議 (日本プロ野球) 92044   北別府学
                1975年度新人選手選択会議 (日本プロ野球) 95956   篠塚和典
                1975年度新人選手選択会議 (日本プロ野球) 143952  中畑清
    """
    import pandas as pd
    import csv
    import codecs
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    back_link_list = []
    d_title = {}
    d_pid_title_incoming_eneid = get_to_pid_to_title_incoming_eneid(ext_file, log_info)
    with open(ptitle_list, 'r', encoding='utf-8') as fp:
        for row in fp:
            row = row.replace('\n', '')
            ptitle = row.replace('_', ' ')
            d_title[ptitle] = 1

    with codecs.open(back_link_dump_org, 'r', 'utf-8', 'ignore') as dp:
        reader = csv.reader(dp, delimiter='\t')
        for drow in reader:
            org_title = drow[1]
            org_title = org_title.replace('_', ' ')
            from_pageid = drow[0]
            if d_title.get(org_title):
                from_title = ''
                # notice: not all pageids are found in d_pid_title_incoming_eneid (eg.template pages)
                if d_pid_title_incoming_eneid.get(from_pageid):
                    from_title = d_pid_title_incoming_eneid[from_pageid][0]
                back_link_list.append([org_title, from_pageid, from_title])

    df = pd.DataFrame(back_link_list, columns=['org_title', 'from_pageid', 'from_title'])
    df.to_csv(back_link, sep='\t', header=False, index=False)


def gen_link_prob_file(gold_dir, link_prob_file, log_info):
    """
    create probability info file based on link statistics in sample gold file
    :param:gold_dir (eg. sample_gold_linked_dir)
    :param:link_prob_file
    :param:log_info
    :output: link_prob_file
    """

    from glob import glob
    import re
    import sys
    import csv
    import pandas as pd
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    gold_files = gold_dir + '*.tsv'

    logger.info({
        'action': 'gen_link_prob_file',
        'gold_files': gold_files,
        'link_prob_file': link_prob_file
    })
    d = {}
    for gname in glob(gold_files):
        with open(gname, mode='r', encoding='utf-8') as g:
            # 20220825 fromhere
            # cat = gname.replace(gold_dir, '')
            # cat = cat.replace('.tsv', '')
            # till here

            reader = csv.reader(g, delimiter='\t')
            for line in reader:
                if len(line) < 10:
                    logger.warning({
                        'action': 'gen_link_prob_file',
                        'warning': 'format error list too short (skipped)',
                        'line': line,
                    })
                    continue
                # 20220825 from here
                # attr_name = line[2]
                # attr_value = line[3]
                # link_pid = line[8]
                cat = line[0]
                attr_name = line[3]
                attr_value = line[4]
                link_pid = line[9]
                # till here
                cat_attname_attval = cat + '\t' + attr_name + '\t' + attr_value
                if not d.get(cat_attname_attval):
                    d[cat_attname_attval] = {}
                if not d[cat_attname_attval].get(link_pid):
                    d[cat_attname_attval][link_pid] = 1
                else:
                    d[cat_attname_attval][link_pid] += 1
                logger.debug({
                    'action': 'gen_link_prob_file',
                    'line': line,
                    'cat_attname_attval': cat_attname_attval,
                    'link_pid': link_pid,
                    'd[cat_attname_attval][link_pid]': d[cat_attname_attval][link_pid]
                })

    d_new = {}
    for cat_attr_val, link_pid_info in d.items():
        if cat_attr_val not in d_new:
            d_new[cat_attr_val] = []
        link_pid_info_sorted = sorted(link_pid_info.items(), key=lambda x: x[1], reverse=True)
        logger.debug({
            'action': 'gen_link_prob_file',
            'link_pid_info_sorted': link_pid_info_sorted
        })
        if len(link_pid_info_sorted) >= 1:
            link_sum = 0
            for tmp_lpinfo in link_pid_info_sorted:
                link_sum += tmp_lpinfo[1]
                logger.debug({
                    'action': 'gen_link_prob_file',
                    'tmp_lpinfo': tmp_lpinfo,
                    'tmp_lpinfo[1]': tmp_lpinfo[1]
                })

            for tmp_lpinfo in link_pid_info_sorted:
                ratio_str = str(tmp_lpinfo[1] / link_sum)
                ratio = float(Decimal(ratio_str).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
                link_pid_info_string = tmp_lpinfo[0] + ':' + str(ratio) + ':' + str(tmp_lpinfo[1])
                d_new[cat_attr_val].append(link_pid_info_string)
                logger.debug({
                    'action': 'gen_link_prob_file',
                    'ratio_str': ratio_str,
                    'link_sum': link_sum,
                    'link_pid_info_string': link_pid_info_string
                })
        else:
            logger.error({
                'action': 'gen_link_prob_file',
                'error': 'format error link_pid_info too short'
            })
            sys.exit()

    print_list = []
    for cat_attr_val, link_pid_info_string in d_new.items():
        tmp_print_list = re.split('\t', cat_attr_val)
        v_str = ';'.join(link_pid_info_string)
        tmp_print_list.append(v_str)
        print_list.append(tmp_print_list)

    df_a = pd.DataFrame(print_list)
    df_a.to_csv(link_prob_file, sep='\t', header=False, index=False)


def gen_mention_gold_link_dist(html_info, sample_gold_linked_dir, outfile, log_info):
    """get mention nearest gold link distance from sample gold html files and create mention_gold_link_dist file.
    args
        html_info
        sample_gold_linked_dir
        outfile
        log_info
    output
        mention_gold_link_dist
            format
                category, attribute, distance between mention and gold embedded link

            sample
                Person  作品    17
                Person  作品    81
                Person  作品    81
                Person  作品    -1
                Person  作品    -1
    note
        tag_info
            format
                cat     pid     line_id html_text_start html_text_end   html_text       title
            sample
                City    3692278 34      148     150     日本    日本
        gold_files
            Airport	1013693	ルイス・ムニョス・マリン国際空港	ＩＡＴＡ（空港コード）	SJU	44	6	44	9	1013693
            ルイス・ムニョス・マリン国際空港
    """

    import csv
    import pandas as pd
    from glob import glob
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    # ignore if in the same line
    ignore_zero = 1
    gold_files = sample_gold_linked_dir + '*.tsv'
    logger.info({
        'action': 'gen_mention_gold_link_dist',
        'gold_dir': sample_gold_linked_dir,
        'html_info': html_info
    })
    with open(html_info, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')

        cat_pid_title_dic = {}
        check_cat_pid_title_line = {}
        for row in reader:
            cat = row[0]
            # header
            if cat == 'cat':
                continue
            pid = row[1]
            line_start = row[2]
            title = row[6]
            cat_pid_title_line = ':'.join([cat, pid, title, line_start])
            cat_pid_title = ':'.join([cat, pid, title])

            logger.debug({
                'action': 'gen_mention_gold_link_dist',
                'line_start': line_start,
                'cat_pid_title': cat_pid_title,
            })

            if not check_cat_pid_title_line.get(cat_pid_title_line):
                cat_pid_title_dic[cat_pid_title] = []
            cat_pid_title_dic[cat_pid_title].append(int(line_start))
            check_cat_pid_title_line[cat_pid_title_line] = 1

    out_raw_list = []
    for gfile in glob(gold_files):
        list_rec_out = []
        # 20220825 from here
        # gfile_part = gfile.replace(sample_gold_linked_dir, '')
        # ene_cat = gfile_part.replace('.tsv', '')
        # till here
        with open(gfile, 'r', encoding='utf-8') as g:
            greader = csv.reader(g, delimiter='\t')

            for grow in greader:
                # g_org_pid = grow[0]
                # g_org_title = grow[1]
                # g_attr = grow[2]
                # g_mention_line_start = grow[4]
                # g_gold_title = grow[9]
                # 20220825 fromhere
                ene_cat = grow[0]
                g_org_pid = grow[1]
                g_org_title = grow[2]
                g_attr = grow[3]
                g_mention_line_start = grow[5]
                g_gold_title = grow[10]
                # till here
                logger.debug({
                    'action': 'gen_mention_gold_link_dist',
                    'ene_cat': ene_cat,
                    'g_org_title': g_org_title,
                    'g_attr': g_attr,
                    'g_mention_line_start': g_mention_line_start,
                    'g_gold_title': g_gold_title,
                    'msg': 'skipped',
                })

                # skip if no link title
                # 20220819
                # if g_gold_title == '':
                #     logger.debug({
                #         'action': 'gen_mention_gold_link_dist',
                #         'g_gold_title': g_gold_title,
                #         'msg': 'skipped',
                #     })
                #     continue
                g_cat_pid_title = ':'.join([ene_cat, g_org_pid, g_gold_title])

                # check 20210819
                logger.debug({
                    'action': 'gen_mention_gold_link_dist',
                    'g_org_tile': g_org_title,
                    'g_cat_pid_title': g_cat_pid_title,
                    'g_mention_line_start': g_mention_line_start
                })

                if cat_pid_title_dic.get(g_cat_pid_title):
                    tmp_lineid_list = cat_pid_title_dic[g_cat_pid_title]
                    found = 0
                    # 20220819
                    # if len(tmp_lineid_list) > 0:
                    diff_min = 0
                    for lineid in tmp_lineid_list:
                        if int(g_mention_line_start) == lineid:
                            if ignore_zero:
                                continue
                            else:
                                diff_min = 0
                                found = 1
                                break
                        else:
                            if found == 0:
                                diff_min = lineid - int(g_mention_line_start)
                            elif abs(lineid - int(g_mention_line_start)) < abs(diff_min):
                                diff_min = lineid - int(g_mention_line_start)
                                found = 1

                    out_raw_list.append([ene_cat, g_attr, diff_min])
                    logger.debug({
                        'action': 'gen_mention_gold_link_dist',
                        'found': found,
                        'lineid': lineid,
                        'diff_min': diff_min
                    })

    df = pd.DataFrame(out_raw_list, columns=['cat', 'attr', 'diff_min'])
    df.to_csv(outfile, sep='\t',  index=False)


def get_disambiguation_info(dis_file, log_info):
    """Get disambiguation info.
    Args:
        dis_file (str): disambiguation info file name
        log_info
    Returns:
        d_pid_title (dict)
    Note:
        dis_file:
            dis_file is created from cirrus dump, using some patterns of category or title of Wikipedia pages
                eg. Wikipedia category ends with '曖昧さ回避'
                    Wikipedia category starts with '同名の'
                    Wikipedia category ends with '（曖昧さ回避）'
                sample:
                    2264978     マーキング
                    662923      ノワール
                    134999      スコア
                    ....
        d_pid_title:
            format:
                key: pageid of disambiguation page
                val: 1
            sample:
                {'2264978': 1, '662923': 1, '134999': 1, .....}
    """
    import csv
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    with open(dis_file, 'r', encoding='utf-8') as da:
        da_reader = csv.reader(da, delimiter='\t')
        pid_title_list = [da_row for da_row in da_reader]

        d_pid_title = {str(pid_title[0]): 1 for pid_title in pid_title_list}
    return d_pid_title


def check_pageid(pageid, log_info, **d_dis):
    """ check pageid if it can be a candidate link page (disambiguation, isdigit)
    Args:
        pageid
        log_info
        **d_dis
    Returns:
        1: ok
        -1: ng
    """
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    if not pageid:
        logging.error({
            'action': 'check_pageid',
            'judge': 'ng (pageid null)'
        })
        return -1
    elif not str(pageid).isdigit():
        logging.error({
            'action': 'check_pageid',
            'pageid': pageid,
            'judge': 'ng (not digit)'
        })
        return -1
    elif d_dis.get(str(pageid)):
        return -1
    else:
        return 1


def gen_title2pid_file(redirect_dump, page_dump, title2pageid_org, illegal_title_len, log_info):
# def gen_title2pid_file(redirect_dump, page_dump, title2pageid_org, log_info):
    """
    :param redirect_dump:
    :param page_dump:
    :param title2pageid_org:
    :param illegal_title_len:
    :param log_info:
    :return:

    cf. title2pid(org)
    {"page_id": 871214, "title": "日就社", "is_redirect": true, "redirect_to": {"page_id": 1526294, "title": "読売新聞", "is_redirect": false}}
    {"page_id": 2238511, "title": "読売争議", "is_redirect": true, "redirect_to": {"page_id": 1526294, "title": "読売新聞", "is_redirect": false}}
    {"page_id": 1526294, "title": "読売新聞", "is_redirect": false}
    {"page_id": 1262543, "title": "読売新聞縮刷版", "is_redirect": true, "redirect_to": {"page_id": 1526294, "title": "読売新聞", "is_redirect": false}}
    {"page_id": 158932, "title": "讀賣新聞", "is_redirect": true, "redirect_to": {"page_id": 1526294, "title": "読売新聞", "is_redirect": false}}

    redirect.dump:
    (rd from)  (rd title) (namespace)
    557692	宮下杏菜	0
    557693	宮下杏菜	0
    158932	読売新聞  0
    871214	読売新聞  0
    1262543	読売新聞  0
    2238511	読売新聞  0
    10664	ニューヨーク市	0
    23829	アメリカ合衆国	0
    3475368	ニューヨーク市	102
    2187855	アメリカ合衆国	103
    10664	ニューヨーク	0

    page.dump:
    # page_id, page_title, page_is_redirect, page_namespace
    517804	宮下杏菜	0	0
    557692	宮下杏奈	1	0
    557693	広末由依	1	0
    158932	讀賣新聞	1  0
    871214	日就社	1  0
    1262543	読売新聞縮刷版	1  0
    2238511	読売争議	1  0

    379778	読売新聞	0  (ノート:読売新聞)
    1476808	読売新聞	0  (Category‐ノート:読売新聞)
    1483425	読売新聞	0  (Category:読売新聞)
    1526294	読売新聞	0　　　# link to

    3475368	PJ:NY	1	0
    10664	ニューヨーク市	1	0
    1698838	アメリカ合衆国	0	0
    28330	ニューヨーク	0	1
    507175	ニューヨーク	0	0
    1124110	ニューヨーク	0	10
    3099506	ニューヨーク	0	3

    Notice:
    delete one letter punctuation title
    """
    # min_illegal_title_len = 500

    from_pid_to_title = {}
    with open(redirect_dump, mode='r', encoding='utf-8') as rd:
        # cnt += 1
        r_reader = csv.reader(rd, delimiter='\t')
        for r_row in r_reader:
            # if cnt == 1000:
            #     break
            from_pid_str = str(r_row[0])
            to_title = r_row[1]
            namespace_char = str(r_row[2])

            # 20220914
            if len(to_title) >= illegal_title_len:
                if namespace_char == '0':
                    logging.debug({
                        'action': 'gen_title2pid',
                        'mesg': 'illegal long redirect title ( equal to or more than 500)',
                        'to_title': to_title,
                    })
                    sys.exit()

            # many to one
            logging.debug({
                'action': 'gen_title2pid',
                'from_pid_str': from_pid_str,
                'to_title': to_title,
                'namespace_char': namespace_char,
                'r_row': r_row
            })

            if namespace_char != '0':
                logging.debug({
                    'action': 'gen_title2pid',
                    'mesg': 'name space (redirect_to) not zero',
                    'r_row': r_row,
                })
                if from_pid_str == '3475368':
                    logging.info({
                        'action': 'gen_title2pid',
                        'from_pid_str': from_pid_str,
                        'to_title': to_title,
                        'namespace_char': namespace_char,
                        'r_row': r_row
                    })

                # 20220919 skip
                continue
            #

            # 20220919
            # if '\"' in to_title:
            #     to_title_pre = to_title
            #     to_title = to_title_pre.replace('\"', '\"\"')
            #     logging.info({
            #         'action': 'gen_title2pid',
            #         'to_title_pre': to_title_pre,
            #         'to_title': to_title
            #     })

            from_pid_to_title[from_pid_str] = to_title
            logging.debug({
                'action': 'gen_title2pid',
                'step': 'from_pid_to_title',
                'from_pid_str': from_pid_str,
                'to_title': to_title,
            })

    pid2title = {}
    title2pid = {}
    check_namespace = {}
    check_redirect = {}
    with open(page_dump, mode='r', encoding='utf-8') as pd:
        # for p_line in pd:
        # cnt += 1
        p_reader = csv.reader(pd, delimiter='\t')
        for p_row in p_reader:
            # ['126', '液晶', '0', '0']

            pid_str = str(p_row[0])
            title = p_row[1]
            # if '人間と性' in title:
            #     print(title, p_row)
            redirect = str(p_row[2])
            # redirect = str(p_row[2])
            namespace_char = str(p_row[3])

            # if pid_str == '3475368':
            #     logging.info({
            #         'action': 'gen_title2pid',
            #         'stage': 'before namespace_non_zero',
            #         'pid_str': pid_str,
            #         'title': title,
            #         'namespace_char': namespace_char,
            #         'p_row': p_row
            #     })
            # namespace (redirect_to)
            if namespace_char != '0':
                logging.debug({
                    'action': 'gen_title2pid',
                    'mesg': 'skipped name space not zero',
                    'p_row': p_row
                })

                continue
            check_namespace[pid_str] = namespace_char
            if len(title) >= illegal_title_len:
                logging.debug({
                    'action': 'gen_title2pid',
                    'mesg': 'illegal long title ( equal to or more than 500)',
                    'p_row': p_row,
                })
                sys.exit()

            # 20220919
            # if '"' in title:
            #     title_pre = title
            #     title = title_pre.replace('\"', '\"\"')
            #     logging.info({
            #         'action': 'gen_title2pid',
            #         'title_pre': title_pre,
            #         'title': title
            #     })

            if redirect == '1':
                check_redirect[pid_str] = 1

            # 20220919
            # check dupli of pids
            if pid_str in pid2title:
                logging.error({
                    'action': 'gen_title2pid',
                    'mesg': 'duplicate pids',
                    'p_row': p_row,
                    'pid2title': pid2title
                })
                sys.exit()
            else:
                pid2title[pid_str] = title

            # 20220919
            # check dupli of titles
            if title in title2pid:
                logging.error({
                    'action': 'gen_title2pid',
                    'mesg': 'duplicate titles',
                    'p_row': p_row,
                    'title': title,
                    'title2pid': title2pid[title]
                })
                sys.exit()
            else:
                title2pid[title] = pid_str

    dic_list = []
    for tmp_id_str, tmp_title in pid2title.items():
        logging.debug({
            'tmp_id': tmp_id_str,
            'tmp_title': tmp_title
        })
        d = {}
        # redirect
        tmp_char = ''
        d['page_id'] = tmp_id_str

        # 20220920
        # There is a page with title '\\'
        if tmp_title != '\\':
            if '\\' in tmp_title:
                tmp_title_pre = tmp_title
                tmp_title = re.sub(r'\\', '', tmp_title_pre)
        d['title'] = tmp_title

        if tmp_id_str not in check_redirect:
            logging.debug({
                'run': 'gen_title2_pid',
                'info': 'tmp_id_str not in check_redirect',
                'tmp_id_str': tmp_id_str,
                'tmp_title': tmp_title,
            })

            d['is_redirect'] = False
        else:
            d['is_redirect'] = True

            # redirect to
            if tmp_id_str not in from_pid_to_title:
                logging.debug({
                    'run': 'gen_title2_pid',
                    'info': 'tmp_id_str not in from_pid_to_title',
                    'tmp_id_str': tmp_id_str,
                    'tmp_title': tmp_title
                })
                # 20220920
                continue
            else:
                redirect_to_title = from_pid_to_title[tmp_id_str]

                # to title is not registered
                if redirect_to_title not in title2pid:
                    # jawiki-20210820-page_dmp.tsv 名前空間0 (redirect)
                    # 茨城ショッピングタウン -> イオンスタイル新茨城
                    # 4423080	茨木ショッピングタウン	1	0
                    # jawiki-20210820-redirect_dmp.tsv
                    # 4423080	イオンスタイル新茨木	0
                    logging.debug({
                        'run': 'gen_title2_pid',
                        'info': 'tmp_to_title not in title_pid',
                        'msg': 'skipped',
                        'tmp_id_str': tmp_id_str,
                        'tmp_title': tmp_title,
                        'redirect_to_title': redirect_to_title,
                    })
                    continue

                else:
                    tmp_to_pid_str = title2pid[redirect_to_title]
                    # 20220920
                    if tmp_to_pid_str in check_namespace:
                        if check_namespace[tmp_to_pid_str] != '0':
                            continue
                    # prt_list.append([tmp_id, tmp_from_title, from_pid_from_title[]])
                    # 20220920
                    if '\\' in redirect_to_title:
                        redirect_to_title_pre = redirect_to_title
                        redirect_to_title = re.sub(r'\\', '', redirect_to_title_pre)
                    d['redirect_to'] = {}
                    d['redirect_to']['page_id'] = tmp_to_pid_str
                    d['redirect_to']['title'] = redirect_to_title
                    d['redirect_to']['is_redirect'] = False

        dic_list.append(d)

    with open(title2pageid_org, mode='w', encoding='utf-8') as t:
        for dic in dic_list:
            json.dump(dic, t, ensure_ascii=False)
            # json.dump(dic, t, indent=4, ensure_ascii=False)
            t.write('\n')
            # t.write(all_char)


def gen_change_wikipage_list(old_page_dump_org_file, page_dump_org_file, change_id_list, log_info):
    check_old_pageid = {}
    prt_list = []
    with open(old_page_dump_org_file, mode='r', encoding='utf-8') as op:
        op_reader = csv.reader(op, delimiter='\t')
        for op_line in op_reader:
            # page_id, page_title, page_is_redirect, page_namespace
            old_pageid = op_line[0]
            old_title = op_line[1]
            old_namespace = op_line[3]
            logging.debug({
                'run': 'gen_change_wikipage_list',
                'op_line': op_line
            })
            if old_namespace == '0':
                check_old_pageid[old_title] = old_pageid

    with open(page_dump_org_file, mode='r', encoding='utf-8') as np:
        np_reader = csv.reader(np, delimiter='\t')
        for np_line in np_reader:
            # page_id, page_title, page_is_redirect, page_namespace
            new_pageid = np_line[0]
            new_title = np_line[1]
            new_namespace = np_line[3]
            logging.debug({
                'run': 'gen_change_wikipage_list',
                'np_line': np_line
            })
            if new_namespace == '0':
                if new_title in check_old_pageid:
                    if check_old_pageid[new_title] != new_pageid:
                        prt_list.append([check_old_pageid[new_title], new_pageid])

    with open(change_id_list, mode='w', encoding='utf-8') as cl:
        writer = csv.writer(cl, delimiter='\t', lineterminator='\n')
        writer.writerows(prt_list)


# def gen_redirect_info_file2(incoming, title2pageid, dis, redirect_info, log_info):
#     """ get title2pid from incoming file, and remove disambiguation pages and wrong-formatted pages from title2pageid and
#     create redirect info default file
#     Args:
#         incoming
#         title2pageid
#         dis
#         redirect_info
#         log_info
#     Returns:
#     Output:
#         redirect_info
#         Notice:
#             - In the title2pageid file,some 'redirect-to' pages lack page_ids.
#                  {"page_id": 1218449, "title": "岡山県の旧制教育機関", "is_redirect": true,
#                   "redirect_to": {"page_id": null, "title": null, "is_redirect": false}}
#               - white spaces in Wikipedia titles are replaced by '_'.
#     """
#     import csv
#     import json
#
#     logger = set_logging_pre(log_info, 'myPreLogger')
#     logger.setLevel(logging.INFO)
#
#     title_apid = {}
#     d_dis = get_disambiguation_info(dis, log_info)
#     logger.debug({
#         'action': 'gen_redirect_info_file2',
#         'status': 'read title and pageid from incoming',
#     })
#     title_apid = {}
#     with open(incoming, mode='r', encoding='utf-8') as ic:
#         # cnt = 0
#         # for ic_line in ic:
#             # cnt += 1
#         ic_reader = csv.reader(ic, delimiter='\t')
#         for ic_row in ic_reader:
#             # if cnt == 1000:
#             #     break
#             ic_pid = ic_row[0]
#             ic_title = ic_row[1]
#             logger.debug({
#                 'action': 'gen_redirect_info_file2',
#                 'ic_pid': ic_title,
#             })
#             # 20220901
#             if check_pageid(ic_pid, log_info, **d_dis) != 1:
#                 continue
#             else:
#                 title_apid[ic_title] = str(ic_pid)
#             title_apid[ic_title] = str(ic_pid)
#     logger.debug({
#         'action': 'gen_redirect_info_file2',
#         'status': 'title2pageid start',
#         'ic_pid': ic_title,
#     })
#     with open(title2pageid, mode='r', encoding='utf-8') as r:
#         for r_line in r:
#             rd = json.loads(r_line)
#
#             from_pid = rd['page_id']
#
#             # disambiguation
#             if check_pageid(from_pid, log_info, **d_dis) != 1:
#                 continue
#             from_title = rd['title'].replace('_', ' ')
#             # redirect page
#             if rd['is_redirect']:
#                 if not rd['redirect_to']['page_id']:
#                     continue
#                 else:
#                     to_pid = rd['redirect_to']['page_id']
#                     if check_pageid(to_pid, log_info, **d_dis) != 1:
#                         continue
#                     else:
#                         title_apid[from_title] = str(to_pid)
#             # non-redirect page
#             else:
#                 title_apid[from_title] = str(from_pid)
#
#         with open(redirect_info, 'w') as o:
#             writer = csv.writer(o, delimiter='\t', lineterminator='\n')
#             for k, v in title_apid.items():
#                 writer.writerow([k, v])


def gen_redirect_info_file(title2pageid, dis, redirect_info, log_info):
    """ remove disambiguation pages and wrong-formatted pages from title2pageid and
    create redirect info default file
    Args:
        title2pageid
        dis
        redirect_info
        log_info
    Returns:
    Output:
        redirect_info
        Notice:
            - In the title2pageid file,some 'redirect-to' pages lack page_ids.
                 {"page_id": 1218449, "title": "岡山県の旧制教育機関", "is_redirect": true,
                  "redirect_to": {"page_id": null, "title": null, "is_redirect": false}}
              - white spaces in Wikipedia titles are replaced by '_'.
    """
    import csv
    import json

    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    title_apid = {}
    d_dis = get_disambiguation_info(dis, log_info)

    title_apid = {}
    with open(title2pageid, mode='r', encoding='utf-8') as r:
        for r_line in r:
            rd = json.loads(r_line)

            from_pid = rd['page_id']

            # disambiguation
            if check_pageid(from_pid, log_info, **d_dis) != 1:
                continue
            from_title = rd['title'].replace('_', ' ')

            # 20220922
            if from_title == '':
                continue

            # redirect page
            if rd['is_redirect']:
                # 20220904
                if 'redirect_to' not in rd:
                    logging.warning({
                        'run': 'gen_redirect_info_file',
                        'msg': 'redirect_to not found',
                        'rd': rd
                    })
                    continue
                if 'page_id' not in rd['redirect_to']:
                    continue
                else:
                    to_pid = rd['redirect_to']['page_id']
                    if check_pageid(to_pid, log_info, **d_dis) != 1:
                        continue
                    else:
                        title_apid[from_title] = str(to_pid)
            # non-redirect page
            else:
                title_apid[from_title] = str(from_pid)

        with open(redirect_info, 'w') as o:
            writer = csv.writer(o, delimiter='\t', lineterminator='\n')
            for k, v in title_apid.items():
                writer.writerow([k, v])


def gen_self_link_by_attr_name(self_link_patfile, target_attr_file, self_link_by_attr_name_file, log_info):
    """Generate list of self_link cand attribute based on hand-written pattern
    :param self_link_patfile:
    :param target_attr_file:
    :param self_link_by_attr_name_file:
    :param log_info:
    :return:

    :notice:
    """
    import re
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    check_pos = {}
    with open(self_link_patfile, mode='r', encoding='utf-8') as p:
        p_reader = csv.reader(p, delimiter='\t')
        for p_line in p_reader:
            pos = p_line[0]
            pat = p_line[1]
            logger.debug({
                'action': 'gen_self_link_by_attr_name',
                'pos': pos,
                'pat': pat
            })
            check_pos[pat] = pos
    check_target_attr = {}
    with open(target_attr_file, mode='r', encoding='utf-8') as ta:
        ta_reader = csv.reader(ta, delimiter='\t')
        # 1.1     人名    Person  別名・旧称
        # 1.1     人名    Person  国籍
        # 1.1     人名    Person  地位職業

        for ta_line in ta_reader:
            attr_name = ta_line[3]
            if attr_name not in check_target_attr:
                check_target_attr[attr_name] = 1

    prt_list = []
    for attr in check_target_attr:
        for tmp_pat, tmp_pos in check_pos.items():
            check_aself = 0
            if tmp_pat in attr:
                if tmp_pos == 'start':
                    if attr.startswith(tmp_pat):
                        check_aself = 1
                elif tmp_pos == 'end':
                    if attr.endswith(tmp_pat):
                        check_aself = 1
                elif tmp_pos == 'middle':
                    check_aself = 1
            if check_aself:
                prt_list.append(attr)
    with open(self_link_by_attr_name_file, 'w', encoding='utf-8') as sa:
        sa.write('\n'.join(prt_list))
        sa.write('\n')


def gen_disambiguation_file(patfile, cirrus, outfile, log_info):
    """Extract Wikipedia pages which satisfies the matching patterns specified in the pattern file
    arg:
        patfile
        cirrus (.gz)
        outfile
        log_info
    note
        patfile
            format
                <field>\t<match_position>_<pat>\n
                <field>   cat|title
                <match_position>    start|middle|end
                <pat>
                Notice: Matching patterns are interpreted as 'OR' conditions
            sample:
                cat     end 曖昧さ回避
                cat     start 同名の
                 - category: endswith '曖昧さ回避'
                 - category: startswith '同名の'
        title with one punct character is deleted

    """

    import re
    import json
    import gzip
    import sys
    import csv
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)
    id_title = []

    check_cat = {}
    check_title = {}
    with open(patfile, mode='r', encoding='utf-8') as p:
        for p_line in p:
            p_line_new = p_line.rstrip()
            (field, pos, pat) = re.split('\t', p_line_new)
            logger.debug({
                'action': 'gen_disambiguation_file',
                'field': field,
                'pos': pos,
                'pat': pat
            })
            pat_pos = pat + '\t' + pos
            if 'cat' in field:
                check_cat[pat] = pos
            if 'title' in field:
                check_title[pat] = pos

    with gzip.open(cirrus, mode='rt', encoding='utf-8') as c:

        id_title = []
        # cnt = 0
        for c_line in c:
            # cnt += 1
            # if cnt == 1000:
            #     break
            check_dis = 0
            d = json.loads(c_line)
            if 'index' in d:
                tmp_id = str(d['index']['_id'])

            # information other than index
            else:
                if 'namespace' in d:
                    if d['namespace'] != 0:
                        continue
                if 'title' not in d:
                    logger.error({
                        'action': 'gen_disambiguation_file',
                        'error': 'title not found in d',
                        'c_line': c_line
                    })
                    sys.exit()
                # 20220905
                # if len(d['title']) == 1 and d['title'] in string.punctuation:
                #     logger.info({
                #         'action': 'gen_disambiguation_file',
                #         'error': 'skipped punctuation title',
                #         'c_line': c_line
                #     })
                #     continue
                # else:
                tmp_title = d['title']

                for tmp_pat, tmp_pos in check_title.items():
                    if tmp_pat in tmp_title:
                        if tmp_pos == 'start':
                            if tmp_title.startswith(tmp_pat):
                                check_dis = 1
                        elif tmp_pos == 'end':
                            if tmp_title.endswith(tmp_pat):
                                check_dis = 1
                        elif tmp_pos == 'middle':
                            check_dis = 1

                if check_dis != 1:
                    if 'category' not in d:
                        logger.error({
                            'action': 'gen_disambiguation_file',
                            'error': 'category not found in d',
                            'c_line': c_line
                        })
                        sys.exit()

                    d_cat = {cat: 1 for cat in d['category']}

                    for tmp_dcat in d_cat:
                        for tmp_pat, tmp_pos in check_cat.items():
                            if tmp_pat in tmp_dcat:
                                if tmp_pos == 'start':
                                    if tmp_dcat.startswith(tmp_pat):
                                        check_dis = 1
                                elif tmp_pos == 'end':
                                    if tmp_dcat.endswith(tmp_pat):
                                        check_dis = 1
                                elif tmp_pos == 'middle':
                                    check_dis = 1

                if check_dis == 1:
                    id_title.append([tmp_id, tmp_title])

    with open(outfile, 'w', encoding='utf-8') as o:
        writer = csv.writer(o, delimiter='\t', lineterminator='\n')
        writer.writerows(id_title)

def gen_enew_info_rev_file(enew_org, mod_list, wikipedia_change_list, enew_info, log_info):
    """
    args:
        enew_org
        mod_list
        wikipedia_change_list
        enew_info
        log_info
    output:
        enew_info
    note:
        mod_list
            sample
                1.5.1.3 1419479 フランス陸軍参謀総長
                1.5.1.3 2092622 クウェートの首相
                1.5.1.3 2242121 アディゲの首長
    """
    import re
    import json
    import csv
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    check_page_change = {}
    with open(wikipedia_change_list, 'r', encoding='utf-8') as cl:
        cl_reader = csv.reader(cl, delimiter='\t')
        for cl_line in cl_reader:
            old_id = cl_line[0]
            new_id = cl_line[1]

            check_page_change[old_id] = new_id

    plist = []

    check_mod = {}
    with open(mod_list, 'r', encoding='utf-8') as ml:
        ml_reader = csv.reader(ml, delimiter='\t')
        for ml_line in ml_reader:
            eneid = ml_line[0]
            pid = ml_line[1]
            if pid in check_page_change:
                pid = check_page_change[pid]
            tmp_key = pid + ':' + eneid
            if tmp_key not in check_mod:
                check_mod[tmp_key] = 1
    plist = []
    with open(enew_org, 'r', encoding="utf-8") as e:
        for line in e:
            t = json.loads(line)
            if 'pageid' in t:
                pageid = t['pageid']
            elif 'page_id' in t:
                pageid = t['page_id']
            if pageid in check_page_change:
                pageid = check_page_change[pageid]
            title = t['title']

            if t['ENEs']:
                for k, v in t['ENEs'].items():
                    for m in v:
                        # if 'ENE' in m:
                        #     # if 'ENE_id' in m:
                        #     # eid = m['ENE_id']
                        if 'ENE_id' in m:
                            eid = m['ENE_id']
                        elif 'ENE' in m:
                            eid = m['ENE']

                        t_key = str(pageid) + ':' + eid
                        if t_key not in check_mod:
                            plist.append([str(pageid), eid, title])

    with open(enew_info, 'w', encoding='utf-8') as o:
        writer = csv.writer(o, delimiter='\t', lineterminator='\n')
        writer.writerows(plist)


def gen_enew_info_file(enew_org, mod_list, enew_info, log_info):
    """
    args:
        data_info_prep
        log_info
    output:
        enew_info
    note:
        mod_list
            sample
                1.5.1.3 1419479 フランス陸軍参謀総長
                1.5.1.3 2092622 クウェートの首相
                1.5.1.3 2242121 アディゲの首長
    """
    import re
    import json
    import csv
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    check_mod = {}
    with open(mod_list, 'r', encoding='utf-8') as ml:
        ml_reader = csv.reader(ml, delimiter='\t')
        for ml_line in ml_reader:
            eneid = ml_line[0]
            pid = ml_line[1]
            tmp_key = pid + ':' + eneid
            if tmp_key not in check_mod:
                check_mod[tmp_key] = 1
    plist = []
    with open(enew_org, 'r', encoding="utf-8") as e:
        for line in e:
            t = json.loads(line)
            # pageid = t['pageid']
            if 'pageid' in t:
                pageid = t['pageid']
            elif 'page_id' in t:
                pageid = t['page_id']
            title = t['title']

            if t['ENEs']:
                for k, v in t['ENEs'].items():
                    for m in v:
                        if 'ENE' in m:
                            # if 'ENE_id' in m:
                            # eid = m['ENE_id']
                            eid = m['ENE']

                            t_key = str(pageid) + ':' + eid
                            if t_key not in check_mod:
                                plist.append([str(pageid), eid, title])

    with open(enew_info, 'w', encoding='utf-8') as o:
        writer = csv.writer(o, delimiter='\t', lineterminator='\n')
        writer.writerows(plist)


def gen_incoming_link_file(cirrus_content, outfile, log_info):
    """Get num of incoming links from cirrus dump and create incoming_link_file
    args:
        cirrus_content:
        outfile:
        log_info:
    output:
        incoming_link_file
    """
    import json
    import gzip
    import sys
    import csv
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)
    logger.info({
        'action': 'get_incoming_link_file',
        'cirrus_content': cirrus_content,
        'outfile': outfile
    })
    with gzip.open(cirrus_content, mode='rt', encoding='utf-8') as c:
        id_title_link = []
        for c_line in c:
            d = json.loads(c_line)
            if 'index' in d:
                tmp_id = str(d['index']['_id'])
            else:
                if 'namespace' in d:
                    if d['namespace'] != 0:
                        print('error:namespace', c_line)
                        continue
                if 'title' not in d:
                    logger.error({
                        'action': 'get_incoming_link_file',
                        'error': 'title not found',
                        'c_line': c_line
                    })
                    sys.exit()
                else:
                    tmp_title = d['title']
                if 'incoming_links' not in d:
                    logger.error({
                        'action': 'get_incoming_link_file',
                        'error': 'incoming links not found',
                        'c_line': c_line
                        })
                    sys.exit()
                else:
                    tmp_link_num = d['incoming_links']
                    id_title_link.append([tmp_id, tmp_title, tmp_link_num])

    with open(outfile, 'w', encoding='utf-8') as o:
        writer = csv.writer(o, delimiter='\t', lineterminator='\n')
        writer.writerows(id_title_link)


# def linkedjson2tsv2(linked_json_dir, title2pid_ext_file, log_info):
#     """Convert linked json file (with title) to linked tsv file
#         add title info based on title2pid_ext_file
#     args:
#         linked_json_dir
#         title2pid_ext_file
#         log_info
#     output:
#         linked_tsv (tsv)
#             format
#                 cat, pageid, title, attribute, text, start_line_id, start_offset, end_line_id, end_offset, link_pageid,
#                 link_page_title ENE
#             sample
#                 Person 2392906	桐谷華	地位職業	声優	38	20	38	22	1192	声優 　1.7.21.1
#     notice
#         '\n' in text(mention) has been converted to '\\n'.
#     """
#
#     import json
#     import pandas as pd
#     from glob import glob
#
#     import logging
#     import re
#     logger = set_logging_pre(log_info, 'myPreLogger')
#     logger.setLevel(logging.INFO)
#
#     logger.info({
#         'action': 'linkedjson2tsv2',
#         'linked_json_dir': linked_json_dir,
#         # 'title2pid_org_file': title2pid_org_file,
#     })
#     get_title = {}
#
#     with open(title2pid_ext_file, mode='r', encoding='utf-8') as f:
#         reader = csv.reader(f, delimiter='\t')
#         for rows in reader:
#             to_title = rows[2]
#             to_pid_str = rows[1]
#             get_title[to_pid_str] = to_title
#
#     # with open(title2pid_org_file, mode='r', encoding='utf-8') as r:
#     #     for rline in r:
#     #         rd = {}
#     #         pid = ''
#     #         title = ''
#     #         rd = json.loads(rline)
#     #         if 'page_id' not in rd:
#     #             logger.error({
#     #                 'action': 'linkedjson2tsv',
#     #                 'error': 'missing page_id'
#     #             })
#     #             sys.exit()
#     #         elif not rd['page_id']:
#     #             logger.error({
#     #                 'action': 'linkedjson2tsv',
#     #                 'error': 'page_id null'
#     #             })
#     #             sys.exit()
#     #         else:
#     #             pid = str(rd['page_id'])
#     #         # title (not forwarded page)
#     #         if 'title' not in rd:
#     #             logger.error({
#     #                 'action': 'linkedjson2tsv',
#     #                 'error': 'title not in rd',
#     #                 'rline': rline
#     #             })
#     #             sys.exit()
#     #         elif not rd['title']:
#     #             logger.error({
#     #                 'action': 'linkedjson2tsv',
#     #                 'error': 'no title redirect to',
#     #                 'rline': rline
#     #             })
#     #             sys.exit()
#     #         else:
#     #             title = rd['title']
#     #             get_title[pid] = title
#     #         rd.clear()
#
#     # linked_json_files = linked_json_dir + '*.json'
#     linked_json_files = linked_json_dir + '*.jsonl'
#
#     for linked_json in glob(linked_json_files):
#         go_list = []
#         # linked_tsv = linked_json.replace('.json', '.tsv')
#         if '_dist.jsonl' in linked_json:
#             linked_tsv = linked_json.replace('_dist.jsonl', '.tsv')
#         else:
#             linked_tsv = linked_json.replace('.jsonl', '.tsv')
#         # 20220825
#         cat_pre = linked_tsv.replace(linked_json_dir, '')
#         cat = cat_pre.replace('.tsv', '')
#
#         with open(linked_json, mode='r', encoding='utf-8') as g, open(linked_tsv, 'w', encoding='utf-8') as o:
#             for g_line in g:
#                 g_key_list = []
#                 d_gline = json.loads(g_line)
#                 g_key_list = get_key_list_with_title(log_info, **d_gline)
#
#                 logger.debug({
#                     'action': 'linkedjson2tsv2',
#                     'g_key_list': g_key_list,
#                 })
#                 g_link_pageid = g_key_list[8]
#                 # in case of multiple lines
#                 text_pre = g_key_list[4]
#                 g_key_list[4] = '\\n'.join(text_pre.splitlines())
#
#                 if get_title.get(g_link_pageid):
#                     g_link_title = get_title[g_link_pageid]
#                     g_key_list.insert(9, g_link_title)
#                 # 20220825
#                 g_key_list.insert(0, cat)
#                 # g_title_pageid = g_key_list[0]
#                 # if get_title.get(g_title_pageid):
#                 #      g_org_title = get_title[g_title_pageid]
#                 #      g_key_list.insert(1, g_org_title)
#                 logger.debug({
#                     'action': 'linkedjson2tsv2',
#                     'text_pre': text_pre,
#                     'cat': cat,
#                     'g_link_pageid': g_link_pageid,
#                     # 'g_link_title': g_link_title,
#                     # 'g_org_title': g_org_title,
#                 })
#                 go_list.append(g_key_list)
#
#             df_go = pd.DataFrame(go_list)
#             df_go.to_csv(o, sep='\t', header=False, index=False)

# def gen_attr_rng_info(gold_tsv_dir, attr_rng_info_auto_file, attr_rng_info_man_file, attr_rng_info_merged_file, log_info):
#     '''
#
#     :param gold_tsv_dir:
#     :param attr_rng_info_auto_file:
#     :param attr_rng_info_man_file
#     :param attr_rng_info_merged_file
#     :param log_info:
#     :return:
#     :output:
#         attr_rng_info_file:
#         City    産業    ene:0   0.5     50      100
#
#     :notice:
#        linked_json_file:
#             sample: Person 2392906	桐谷華	地位職業	声優	38	20	38	22	1192	声優 　1.7.21.1
#     '''
#     import pandas as pd
#     logger = set_logging_pre(log_info, 'myPreLogger')
#     logger.setLevel(logging.INFO)
#
#     gold_files = gold_tsv_dir + '*.tsv'
#
#     for gold_file in glob(gold_files):
#         cnt_cat_attr_eneid = {}
#         cnt_cat_attr = {}
#         logger.info({
#             'action': 'gen_attr_rng_info',
#             'gold_file': gold_file
#         })
#         with open(gold_file, mode='r', encoding='utf-8') as ar:
#             ar_reader = csv.reader(ar, delimiter='\t')
#
#             for ar_line in ar_reader:
#                 logger.debug({
#                     'action': 'gen_attr_rng_info',
#                     'ar_line': ar_line
#                 })
#                 cat = ar_line[0]
#                 attr = ar_line[3]
#                 eneid = ar_line[11]
#
#                 cat_attr = cat + '\t' + attr
#                 cat_attr_eneid = cat_attr + '\t' + eneid
#
#                 if cat_attr_eneid not in cnt_cat_attr_eneid:
#                     cnt_cat_attr_eneid[cat_attr_eneid] = 0
#                 cnt_cat_attr_eneid[cat_attr_eneid] += 1
#
#                 if cat_attr not in cnt_cat_attr:
#                     cnt_cat_attr[cat_attr] = 0
#                 cnt_cat_attr[cat_attr] += 1
#
#             prt_list = []
#             for t_cat_attr_eneid in cnt_cat_attr_eneid:
#                 cat_attr_eneid_freq = cnt_cat_attr_eneid[t_cat_attr_eneid]
#                 (t_cat, t_attr, t_eneid) = re.split('\t', t_cat_attr_eneid)
#
#                 if not t_eneid:
#                     continue
#
#                 t_cat_attr = t_cat + '\t' + t_attr
#                 logger.debug({
#                     'action': 'gen_attr_rng_info',
#                     't_cat': t_cat,
#                     't_attr': t_attr,
#                     't_cat_attr': t_cat_attr
#                 })
#                 cat_attr_freq = 0
#                 if t_cat_attr in cnt_cat_attr:
#                     cat_attr_freq = cnt_cat_attr[t_cat_attr]
#
#                     t_ratio_str = cat_attr_eneid_freq / cat_attr_freq
#                     t_ratio = float(Decimal(t_ratio_str).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
#                 else:
#                     t_ratio = 0.0
#                 logger.debug({
#                     'action': 'gen_attr_rng_info',
#                     't_cat': t_cat,
#                     't_attr': t_attr,
#                     't_ratio': t_ratio
#                 })
#
#                 t_eneid_expand = 'ene:' + t_eneid
#                 # prt_list.append([t_cat, t_attr, t_ratio, sumup_self_cat_attr[tmp_cat_attr], sumup_cat_attr[tmp_cat_attr]])
#                 prt_list.append([t_cat, t_attr, t_eneid_expand, t_ratio, cat_attr_eneid_freq, cat_attr_freq])
#
#             # for target_cat, target_attr in check_target_cat_attr.items():
#             #     target_cat_attr = target_cat + '\t' + target_attr
#             #     if target_cat_attr not in sumup_cat_attr:
#             #         prt_list.append([target_cat, target_attr, '', 0, 0 ])
#
#             sdf = pd.DataFrame(prt_list, columns=['cat', 'attr', 'eneid', 'ratio', 'freq', 'sum'])
#             sdf.to_csv(attr_rng_info_auto_file, sep='\t', header=False, index=False)

def gen_attr_rng_info(gold_tsv_dir, attr_rng_info_auto_file, log_info):
    '''

    :param gold_tsv_dir:
    :param attr_rng_info_auto_file:
    :param log_info:
    :return:
    :output:
        attr_rng_info_file:
        City    産業    ene:0   0.5     50      100

    :notice:
       linked_json_file:
            sample: Person 2392906	桐谷華	地位職業	声優	38	20	38	22	1192	声優 　1.7.21.1
    '''
    import pandas as pd
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    gold_files = gold_tsv_dir + '*.tsv'
    prt_list = []
    for gold_file in glob(gold_files):
        cnt_cat_attr_eneid = {}
        cnt_cat_attr = {}
        logger.info({
            'action': 'gen_attr_rng_info',
            'gold_file': gold_file
        })
        with open(gold_file, mode='r', encoding='utf-8') as ar:
            ar_reader = csv.reader(ar, delimiter='\t')

            for ar_line in ar_reader:
                logger.debug({
                    'action': 'gen_attr_rng_info',
                    'ar_line': ar_line
                })
                cat = ar_line[0]
                attr = ar_line[3]
                eneid = ar_line[11]

                cat_attr = cat + '\t' + attr
                cat_attr_eneid = cat_attr + '\t' + eneid

                if cat_attr_eneid not in cnt_cat_attr_eneid:
                    cnt_cat_attr_eneid[cat_attr_eneid] = 0
                cnt_cat_attr_eneid[cat_attr_eneid] += 1

                if cat_attr not in cnt_cat_attr:
                    cnt_cat_attr[cat_attr] = 0
                cnt_cat_attr[cat_attr] += 1


            for t_cat_attr_eneid in cnt_cat_attr_eneid:
                cat_attr_eneid_freq = cnt_cat_attr_eneid[t_cat_attr_eneid]
                (t_cat, t_attr, t_eneid) = re.split('\t', t_cat_attr_eneid)

                if not t_eneid:
                    continue

                t_cat_attr = t_cat + '\t' + t_attr
                logger.debug({
                    'action': 'gen_attr_rng_info',
                    't_cat': t_cat,
                    't_attr': t_attr,
                    't_cat_attr': t_cat_attr
                })
                cat_attr_freq = 0
                if t_cat_attr in cnt_cat_attr:
                    cat_attr_freq = cnt_cat_attr[t_cat_attr]

                    t_ratio_str = cat_attr_eneid_freq / cat_attr_freq
                    t_ratio = float(Decimal(t_ratio_str).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
                else:
                    t_ratio = 0.0
                logger.debug({
                    'action': 'gen_attr_rng_info',
                    't_cat': t_cat,
                    't_attr': t_attr,
                    't_ratio': t_ratio
                })

                t_eneid_expand = 'ene:' + t_eneid
                # prt_list.append([t_cat, t_attr, t_ratio, sumup_self_cat_attr[tmp_cat_attr], sumup_cat_attr[tmp_cat_attr]])
                prt_list.append([t_cat, t_attr, t_eneid_expand, t_ratio, cat_attr_eneid_freq, cat_attr_freq])

            # for target_cat, target_attr in check_target_cat_attr.items():
            #     target_cat_attr = target_cat + '\t' + target_attr
            #     if target_cat_attr not in sumup_cat_attr:
            #         prt_list.append([target_cat, target_attr, '', 0, 0 ])

    sdf = pd.DataFrame(prt_list, columns=['cat', 'attr', 'eneid', 'ratio', 'freq', 'sum'])
    logger.info({
        'action': 'gen_attr_rng_info',
        'prt_list': prt_list
    })
    sdf.to_csv(attr_rng_info_auto_file, sep='\t', header=False, index=False)


def linkedjson2tsv_add_linked_title_cnv_year(linked_json_dir, title2pid_ext_file, title2pid_ext_obs_file, log_info):
    """Convert linked json file (with title) to linked tsv file
       add title of linked page using title2pid_ext_file
       Wikipedia pid of gold link should be modified from title2pid_ext_obs_file to title2pid_ext_file,

    args:
        linked_json_dir
        title2pid_ext_file
        title2pid_ext_obs_file
        log_info
    output:
        linked_tsv (tsv)
            format
                cat, pageid, title, attribute, text, start_line_id, start_offset, end_line_id, end_offset, link_pageid,
                link_page_title
            sample
                Person 2392906	桐谷華	地位職業	声優	38	20	38	22	1192	声優
    notice
        '\n' in text(mention) has been converted to '\\n'.
        f_title2pid_ext
            format
                (title(from page))\t(pageid(to page))\t(title(to page)\t(maximum number of incoming links(to page))
                \t(eneid(to_page))
            sample
                アメリカ合衆国  1698838 アメリカ合衆国  116818  1.5.1.3
                ユナイテッドステイツ    1698838 アメリカ合衆国  116818  1.5.1.3
    """

    import json
    import pandas as pd
    from glob import glob

    import logging
    import re
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    logger.info({
        'action': 'linkedjson2tsv_add_linked_title_cnv_year',
        'linked_json_dir': linked_json_dir,
        # 'title2pid_org_file': title2pid_org_file,
    })
    get_title = {}
    get_from_title_to_title = {}
    wikipedia_cnv = 0
    obs_ext_file = title2pid_ext_obs_file
    new_ext_file = title2pid_ext_file

    get_pid_new = {}
    cnv_obs_pid_new_pid = {}

    with open(new_ext_file, mode='r', encoding='utf-8') as nf:
        reader = csv.reader(nf, delimiter='\t')
        for rows in reader:
            # from_title_new = rows[0]
            to_pid_new_str = rows[1]
            to_title_new = rows[2]

            get_title[to_pid_new_str] = to_title_new

            # 20220916
            get_pid_new[to_title_new] = to_pid_new_str
            # get_pid_new[from_title_new] = to_pid_new_str

    with open(obs_ext_file, mode='r', encoding='utf-8') as of:

        reader = csv.reader(of, delimiter='\t')
        for rows in reader:
            #    - from_title, to_pid, to_title, to_incoming, to_eneid (*.tsv)

            # from_title = rows[0]
            to_pid_str = rows[1]
            to_title = rows[2]

            if to_title in get_pid_new:
                to_pid_str_rev = get_pid_new[to_title]
                cnv_obs_pid_new_pid[to_pid_str] = to_pid_str_rev

                logger.debug({
                    'to_title': to_title,
                    'to_pid_str': to_pid_str,
                    'to_pid_str_rev': to_pid_str_rev,
                    'cnv_obs_pid_new_pid[to_pid_str]': cnv_obs_pid_new_pid[to_pid_str],
                })

    # linked_json_files = linked_json_dir + '*.json'
    linked_json_files = linked_json_dir + '*.jsonl'

    for linked_json in glob(linked_json_files):
        go_list = []
        # linked_tsv = linked_json.replace('.json', '.tsv')
        if '_dist.jsonl' in linked_json:
            linked_tsv = linked_json.replace('_dist.jsonl', '.tsv')
        else:
            linked_tsv = linked_json.replace('.jsonl', '.tsv')
        # 20220825
        cat_pre = linked_tsv.replace(linked_json_dir, '')
        cat = cat_pre.replace('.tsv', '')

        with open(linked_json, mode='r', encoding='utf-8') as g, open(linked_tsv, 'w', encoding='utf-8') as o:
            for g_line in g:
                g_key_list = []
                d_gline = json.loads(g_line)
                g_key_list = get_key_list_with_title(log_info, **d_gline)
                # g_key_list = [pid, title, at, text, start_line_id, start_offset, end_line_id, end_offset, link_id]

                # if '鹿島アントラーズ' in g_key_list:
                #     logger.info({
                #         'action': 'linkedjson2tsv_add_linked_title',
                #         'g_key_list': g_key_list,
                #     })
                # 'g_key_list': ['2332490', 'マルセリーナ', '別名', 'Marcellina', '46', '7', '46', '17', '2332490']}
                # 'g_key_list': ['1665409', '大迫勇也', '所属組織', '鹿島アントラーズ', '82', '4', '82', '12', '4670']}

                # g_link_pageid = g_key_list[8]

                # in case of multiple lines
                # text_pre = g_key_list[4]
                text_pre = g_key_list[3]

                # 20220826
                # g_key_list[4] = '\\n'.join(text_pre.splitlines())
                g_key_list[3] = '\\n'.join(text_pre.splitlines())

                # g_key_list[4] = '\n'.join(text_pre.splitlines())
                # till here
                # if 'つまり' in g_key_list[3] or '要するに' in g_key_list[3] or 'たとえば' in g_key_list[3]:
                #     print('key_list_3', g_key_list[3])

                # 20220826
                g_link_obs_pageid = g_key_list[8]

                if g_link_obs_pageid and g_link_obs_pageid in cnv_obs_pid_new_pid:
                    g_link_new_pageid = cnv_obs_pid_new_pid[g_link_obs_pageid]
                    logger.debug({
                        'action': 'linkedjson2tsv_add_linked_title_cnv_year',
                        'g_key_list': g_key_list,
                        'g_link_new_pageid': g_link_new_pageid
                    })
                else:
                    g_link_new_pageid = g_link_obs_pageid
                g_link_title = ''
                if get_title.get(g_link_new_pageid):
                    g_link_title = get_title[g_link_new_pageid]
                    logger.debug({
                        'action': 'linkedjson2tsv_add_linked_title_cnv_year',
                        'g_link_title': g_link_title
                    })
                    #  'g_link_title': '機動戦士ガンダム エコール・デュ・シエル'}
                g_key_list[8] = g_link_new_pageid
                g_key_list.insert(9, g_link_title)
                # 20220825
                g_key_list.insert(0, cat)

                logger.debug({
                    'action': 'linkedjson2tsv_add_linked_title',
                    'g_key_list': g_key_list,
                })

                go_list.append(g_key_list)

            df_go = pd.DataFrame(go_list)
            df_go.to_csv(o, sep='\t', header=False, index=False)


def linkedjson2tsv_add_linked_title_ene(linked_json_dir, title2pid_ext_file, log_info):
    """Convert linked json file (with title) to linked tsv file
       add title of linked page and ene using title2pid_ext_file

    args:
        linked_json_dir
        title2pid_ext_file
        log_info
    output:
        linked_tsv (tsv)
            format
                cat, pageid, title, attribute, text, start_line_id, start_offset, end_line_id, end_offset, link_pageid,
                link_page_title, ene
            sample
                Person 2392906	桐谷華	地位職業	声優	38	20	38	22	1192	声優
    notice
        '\n' in text(mention) has been converted to '\\n'.
        f_title2pid_ext
            format
                (title(from page))\t(pageid(to page))\t(title(to page)\t(maximum number of incoming links(to page))
                \t(eneid(to_page))
            sample
                アメリカ合衆国  1698838 アメリカ合衆国  116818  1.5.1.3
                ユナイテッドステイツ    1698838 アメリカ合衆国  116818  1.5.1.3
    """

    import json
    import pandas as pd
    from glob import glob

    import logging
    import re
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    logger.info({
        'action': 'linkedjson2tsv_add_linked_title_ene',
        'linked_json_dir': linked_json_dir,
        # 'title2pid_org_file': title2pid_org_file,
    })
    get_title = {}
    get_ene = {}

    with open(title2pid_ext_file, mode='r', encoding='utf-8') as f:

        reader = csv.reader(f, delimiter='\t')
        for rows in reader:
            to_title = rows[2]
            to_pid_str = rows[1]
            # 20220921
            to_ene = rows[4]

            get_title[to_pid_str] = to_title
            get_ene[to_pid_str] = to_ene
            # # 20220916
            # get_pid[to_title] = to_pid_str
    # linked_json_files = linked_json_dir + '*.json'
    linked_json_files = linked_json_dir + '*.jsonl'

    for linked_json in glob(linked_json_files):
        go_list = []
        # linked_tsv = linked_json.replace('.json', '.tsv')
        if '_dist.jsonl' in linked_json:
            linked_tsv = linked_json.replace('_dist.jsonl', '.tsv')
        else:
            linked_tsv = linked_json.replace('.jsonl', '.tsv')
        # 20220825
        cat_pre = linked_tsv.replace(linked_json_dir, '')
        cat = cat_pre.replace('.tsv', '')

        with open(linked_json, mode='r', encoding='utf-8') as g, open(linked_tsv, 'w', encoding='utf-8') as o:
            for g_line in g:
                g_key_list = []
                d_gline = json.loads(g_line)
                g_key_list = get_key_list_with_title(log_info, **d_gline)
                # g_key_list = [pid, title, at, text, start_line_id, start_offset, end_line_id, end_offset, link_id]

                logger.debug({
                    'action': 'linkedjson2tsv_add_linked_title_ene',
                    'g_key_list': g_key_list,
                })

                g_link_pageid = g_key_list[8]

                # in case of multiple lines
                # text_pre = g_key_list[4]
                text_pre = g_key_list[3]

                # 20220826
                # g_key_list[4] = '\\n'.join(text_pre.splitlines())
                g_key_list[3] = '\\n'.join(text_pre.splitlines())

                # g_key_list[4] = '\n'.join(text_pre.splitlines())
                # till here
                # if 'つまり' in g_key_list[3] or '要するに' in g_key_list[3] or 'たとえば' in g_key_list[3]:
                #     print('key_list_3', g_key_list[3])

                # 20220826
                g_link_pageid = g_key_list[8]
                g_link_title = ''
                g_link_ene = ''
                if get_title.get(g_link_pageid):
                    g_link_title = get_title[g_link_pageid]
                g_key_list.insert(9, g_link_title)
                # 20220921
                if get_ene.get(g_link_pageid):
                    g_link_ene = get_ene[g_link_pageid]
                g_key_list.insert(10, g_link_ene)

                # 20220825
                g_key_list.insert(0, cat)

                logger.debug({
                    'action': 'linkedjson2tsv_add_linked_title_ene',
                    'g_key_list': g_key_list,
                })
                go_list.append(g_key_list)

            df_go = pd.DataFrame(go_list)
            df_go.to_csv(o, sep='\t', header=False, index=False)


def linkedjson2tsv_add_linked_title(linked_json_dir, title2pid_ext_file, log_info):
    """Convert linked json file (with title) to linked tsv file
       add title of linked page using title2pid_ext_file

    args:
        linked_json_dir
        title2pid_ext_file
        log_info
    output:
        linked_tsv (tsv)
            format
                cat, pageid, title, attribute, text, start_line_id, start_offset, end_line_id, end_offset, link_pageid,
                link_page_title
            sample
                Person 2392906	桐谷華	地位職業	声優	38	20	38	22	1192	声優
    notice
        '\n' in text(mention) has been converted to '\\n'.
        f_title2pid_ext
            format
                (title(from page))\t(pageid(to page))\t(title(to page)\t(maximum number of incoming links(to page))
                \t(eneid(to_page))
            sample
                アメリカ合衆国  1698838 アメリカ合衆国  116818  1.5.1.3
                ユナイテッドステイツ    1698838 アメリカ合衆国  116818  1.5.1.3
    """

    import json
    import pandas as pd
    from glob import glob

    import logging
    import re
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    logger.info({
        'action': 'linkedjson2tsv_add_linked_title',
        'linked_json_dir': linked_json_dir,
        # 'title2pid_org_file': title2pid_org_file,
    })
    get_title = {}

    with open(title2pid_ext_file, mode='r', encoding='utf-8') as f:

        reader = csv.reader(f, delimiter='\t')
        for rows in reader:
            to_title = rows[2]
            to_pid_str = rows[1]

            get_title[to_pid_str] = to_title
            # # 20220916
            # get_pid[to_title] = to_pid_str
    # linked_json_files = linked_json_dir + '*.json'
    linked_json_files = linked_json_dir + '*.jsonl'

    for linked_json in glob(linked_json_files):
        go_list = []
        # linked_tsv = linked_json.replace('.json', '.tsv')
        if '_dist.jsonl' in linked_json:
            linked_tsv = linked_json.replace('_dist.jsonl', '.tsv')
        else:
            linked_tsv = linked_json.replace('.jsonl', '.tsv')
        # 20220825
        cat_pre = linked_tsv.replace(linked_json_dir, '')
        cat = cat_pre.replace('.tsv', '')

        with open(linked_json, mode='r', encoding='utf-8') as g, open(linked_tsv, 'w', encoding='utf-8') as o:
            for g_line in g:
                g_key_list = []
                d_gline = json.loads(g_line)
                g_key_list = get_key_list_with_title(log_info, **d_gline)
                # g_key_list = [pid, title, at, text, start_line_id, start_offset, end_line_id, end_offset, link_id]

                logger.debug({
                    'action': 'linkedjson2tsv_add_linked_title',
                    'g_key_list': g_key_list,
                })

                # in case of multiple lines
                # text_pre = g_key_list[4]
                text_pre = g_key_list[3]

                # 20220826
                # g_key_list[4] = '\\n'.join(text_pre.splitlines())
                g_key_list[3] = '\\n'.join(text_pre.splitlines())

                # g_key_list[4] = '\n'.join(text_pre.splitlines())
                # till here
                # if 'つまり' in g_key_list[3] or '要するに' in g_key_list[3] or 'たとえば' in g_key_list[3]:
                #     print('key_list_3', g_key_list[3])

                # 20220826
                g_link_pageid = g_key_list[8]
                g_link_title = ''
                if get_title.get(g_link_pageid):
                    g_link_title = get_title[g_link_pageid]
                g_key_list.insert(9, g_link_title)
                # 20220825
                g_key_list.insert(0, cat)

                # g_title_pageid = g_key_list[0]
                # if get_title.get(g_title_pageid):
                #      g_org_title = get_title[g_title_pageid]
                #      g_key_list.insert(1, g_org_title)
                # logger.debug({
                #     'action': 'linkedjson2tsv_add_linked_title',
                #     'text_pre': text_pre,
                #     'cat': cat,
                #     'g_link_pageid': g_link_pageid,
                #     # 'g_link_title': g_link_title,
                #     # 'g_org_title': g_org_title,
                # })
                logger.debug({
                    'action': 'linkedjson2tsv_add_linked_title',
                    'g_key_list': g_key_list,
                })
                #  'g_key_list': ['Style', '2847831', '為我流', '活動地域', '茨城県', '56', '0', '56', '3', '774349',
                #  '茨城県']}
                # 'g_key_list': ['Styl_orge', '2847831', '為我流', '統括組織', '為我流和術保存会', '56', '6', '56', '14',
                # None, '']}
                # g_key_list = [cat, pid, title, at, text, start_line_id, start_offset, end_line_id, end_offset,
                # link_id]
                go_list.append(g_key_list)

            df_go = pd.DataFrame(go_list)
            df_go.to_csv(o, sep='\t', header=False, index=False)


def linkedjson2tsv(linked_json_dir, title2pid_org_file, log_info):
    """Convert linked json file　(with no title) to linked tsv file
        add title info based on title2pid_org_file

    args:
        linked_json_dir
        title2pid_org_file
        log_info
    output:
        linked_tsv (tsv)
            format
                pageid, title, attribute, text, start_line_id, start_offset, end_line_id, end_offset, link_pageid,
                link_page_title
            sample
                2392906	桐谷華	地位職業	声優	38	20	38	22	1192	声優
    notice
        '\n' in text(mention) has been converted to '\\n'.
    """

    import json
    import pandas as pd
    from glob import glob

    import logging
    import re
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    logger.info({
        'action': 'linkedjson2tsv',
        'linked_json_dir': linked_json_dir,
        'title2pid_org_file': title2pid_org_file,
    })
    get_title = {}
    with open(title2pid_org_file, mode='r', encoding='utf-8') as r:
        for rline in r:
            rd = {}
            pid = ''
            title = ''
            rd = json.loads(rline)
            if 'page_id' not in rd:
                logger.error({
                    'action': 'linkedjson2tsv',
                    'error': 'missing page_id'
                })
                sys.exit()
            elif not rd['page_id']:
                logger.error({
                    'action': 'linkedjson2tsv',
                    'error': 'page_id null'
                })
                sys.exit()
            else:
                pid = str(rd['page_id'])
            # title (not forwarded page)
            if 'title' not in rd:
                logger.error({
                    'action': 'linkedjson2tsv',
                    'error': 'title not in rd',
                    'rline': rline
                })
                sys.exit()
            elif not rd['title']:
                logger.error({
                    'action': 'linkedjson2tsv',
                    'error': 'no title redirect to',
                    'rline': rline
                })
                sys.exit()
            else:
                title = rd['title']
                get_title[pid] = title
            rd.clear()

    # linked_json_files = linked_json_dir + '*.json'
    linked_json_files = linked_json_dir + '*.jsonl'

    for linked_json in glob(linked_json_files):
        go_list = []
        # linked_tsv = linked_json.replace('.json', '.tsv')
        if '_dist.jsonl' in linked_json:
            linked_tsv = linked_json.replace('_dist.jsonl', '.tsv')
        else:
            linked_tsv = linked_json.replace('.jsonl', '.tsv')

        with open(linked_json, mode='r', encoding='utf-8') as g, open(linked_tsv, 'w', encoding='utf-8') as o:
            for g_line in g:
                d_gline = json.loads(g_line)
                # titleがある場合はg_key_list_with_titleを使う
                g_key_list = get_key_list(log_info, **d_gline)
                g_link_pageid = g_key_list[7]
                # in case of multiple lines
                text_pre = g_key_list[3]
                g_key_list[3] = '\\n'.join(text_pre.splitlines())

                if get_title.get(g_link_pageid):
                    g_link_title = get_title[g_link_pageid]
                    g_key_list.insert(8, g_link_title)
                g_title_pageid = g_key_list[0]
                if get_title.get(g_title_pageid):
                    g_org_title = get_title[g_title_pageid]
                    g_key_list.insert(1, g_org_title)

                go_list.append(g_key_list)

            df_go = pd.DataFrame(go_list)
            df_go.to_csv(o, sep='\t', header=False, index=False)


def get_key_list_with_title(log_info, **tr):
    """get key list from input json dictionary to distinguish each record
       The dictionary should include title of the page as key
    args:
        log_info
        **tr
    return:
        tmp_list
            format: [pageid, title, attribute, text, start_line_id, start_offset, end_line_id, end_offset, link_id]
    """

    import sys
    import logging
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    try:
        pid = tr['page_id']
    except (KeyError, ValueError) as ex:
        logger.error({
            'action': 'get_key_list_with_title',
            'error': ex,
            'tr': tr
        })
        sys.exit()
    try:
        title = tr['title']
    except (KeyError, ValueError) as ex:
        logger.error({
            'action': 'get_key_list_with_title',
            'error': ex,
            'tr': tr
        })
        sys.exit()
    try:
        at = tr['attribute']
    except (KeyError, ValueError) as ex:
        logger.error({
            'action': 'get_key_list_with_title',
            'error': ex,
            'tr': tr
        })
        sys.exit()

    if 'text_offset' not in tr:
        logger.error({
            'action': 'get_key_list_with_title',
            'error': 'format_error: text_offset',
            'tr': tr
        })
        sys.exit()
    else:
        if 'start' not in tr['text_offset']:
            logger.error({
                'action': 'get_key_list_with_title',
                'error': 'format_error: start(text_offset)',
                'tr': tr
            })
            sys.exit()
        else:
            if 'line_id' not in tr['text_offset']['start']:
                logger.error({
                    'action': 'get_key_list_with_title',
                    'error': 'format_error: line_id(start)',
                    'tr': tr
                })
                sys.exit()
            else:
                start_line_id = str(tr['text_offset']['start']['line_id'])

            if 'offset' not in tr['text_offset']['start']:
                logger.error({
                    'action': 'get_key_list_with_title',
                    'error': 'format_error: offset(start)',
                    'tr': tr
                })
                sys.exit()
            else:
                start_offset = str(tr['text_offset']['start']['offset'])

        if 'end' not in tr['text_offset']:
            logger.error({
                'action': 'get_key_list_with_title',
                'error': 'format_error: end(text_offset)',
                'tr': tr
            })
            sys.exit()
        else:
            if 'line_id' not in tr['text_offset']['end']:
                logger.error({
                    'action': 'get_key_list_with_title',
                    'error': 'format_error: line_id(end)',
                    'tr': tr
                })
                sys.exit()
            else:
                end_line_id = str(tr['text_offset']['end']['line_id'])

            if 'offset' not in tr['text_offset']['end']:
                logger.error({
                    'action': 'get_key_list_with_title',
                    'error': 'format_error: offset(end)',
                    'tr': tr
                })
                sys.exit()
            else:
                end_offset = str(tr['text_offset']['end']['offset'])

            if 'text' not in tr['text_offset']:
                logger.error({
                    'action': 'get_key_list_with_title',
                    'error': 'format_error: text(text_offset)',
                    'tr': tr
                })
                sys.exit()
            else:
                text = tr['text_offset']['text']

    if 'link_page_id' not in tr:
        link_id = None
    else:
        link_id = tr['link_page_id']

    logger.debug({
        'action': 'get_key_list_with_title',
        'pid': pid,
        'title': title,
        'at': at,
        'text': text,
        'start_line_id': start_line_id,
        'start_offset': start_offset,
        'end_line_id': end_line_id,
        'end_offset': end_offset,
        'link_id': link_id
    })
    tmp_list = [pid, title, at, text, start_line_id, start_offset, end_line_id, end_offset, link_id]
    return tmp_list


def get_key_list(log_info, **tr):
    """get key list from input json dictionary to distinguish each record
    args:
        log_info
        **tr
    return:
        tmp_list
            format: [pageid, attribute, text, start_line_id, start_offset, end_line_id, end_offset, link_id]
    """

    import sys
    import logging
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    try:
        pid = tr['page_id']
    except (KeyError, ValueError) as ex:
        logger.error({
            'action': 'get_key_list',
            'error': ex,
            'tr': tr
        })
        sys.exit()

    try:
        at = tr['attribute']
    except (KeyError, ValueError) as ex:
        logger.error({
            'action': 'get_key_list',
            'error': ex,
            'tr': tr
        })
        sys.exit()

    if 'text_offset' not in tr:
        logger.error({
            'action': 'get_key_list',
            'error': 'format_error: text_offset',
            'tr': tr
        })
        sys.exit()
    else:
        if 'start' not in tr['text_offset']:
            logger.error({
                'action': 'get_key_list',
                'error': 'format_error: start(text_offset)',
                'tr': tr
            })
            sys.exit()
        else:
            if 'line_id' not in tr['text_offset']['start']:
                logger.error({
                    'action': 'get_key_list',
                    'error': 'format_error: line_id(start)',
                    'tr': tr
                })
                sys.exit()
            else:
                start_line_id = str(tr['text_offset']['start']['line_id'])

            if 'offset' not in tr['text_offset']['start']:
                logger.error({
                    'action': 'get_key_list',
                    'error': 'format_error: offset(start)',
                    'tr': tr
                })
                sys.exit()
            else:
                start_offset = str(tr['text_offset']['start']['offset'])

        if 'end' not in tr['text_offset']:
            logger.error({
                'action': 'get_key_list',
                'error': 'format_error: end(text_offset)',
                'tr': tr
            })
            sys.exit()
        else:
            if 'line_id' not in tr['text_offset']['end']:
                logger.error({
                    'action': 'get_key_list',
                    'error': 'format_error: line_id(end)',
                    'tr': tr
                })
                sys.exit()
            else:
                end_line_id = str(tr['text_offset']['end']['line_id'])

            if 'offset' not in tr['text_offset']['end']:
                logger.error({
                    'action': 'get_key_list',
                    'error': 'format_error: offset(end)',
                    'tr': tr
                })
                sys.exit()
            else:
                end_offset = str(tr['text_offset']['end']['offset'])

            if 'text' not in tr['text_offset']:
                logger.error({
                    'action': 'get_key_list',
                    'error': 'format_error: text(text_offset)',
                    'tr': tr
                })
                sys.exit()
            else:
                text = tr['text_offset']['text']

    if 'link_page_id' not in tr:
        link_id = ''
    else:
        link_id = tr['link_page_id']
    tmp_list = [pid, at, text, start_line_id, start_offset, end_line_id, end_offset, link_id]
    return tmp_list

# def cnv_dump(dump_org, dump_rev, log_info):
#     import re
#     with open(dump_org, mode='r', encoding='utf-8') as do, open(dump_rev, mode='w', encoding='utf-8') as dr:
#         for dline in do:
#             dline = re.sub(r'"', '""', dline)
#             dr.write(dline)


if __name__ == '__main__':
    ljc_prep_main()
