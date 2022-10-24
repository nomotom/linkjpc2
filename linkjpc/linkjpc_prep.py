from glob import glob
import json
import click
import config as cf
import csv
from decimal import Decimal, ROUND_HALF_UP
import logging
import logging.config
import sys
# import string
import re
import datetime
import ljc_common as lc
import os


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
@click.option('--gen_target_attr', is_flag=True, default=False, show_default=True)
@click.option('--gen_attr_rng', is_flag=True, default=False, show_default=True)
@click.option('--gen_change_wikipedia_info', is_flag=True, default=False, show_default=True)
@click.option('--gen_enew', is_flag=True, default=False, show_default=True)
@click.option('--gen_enew_rev_year', is_flag=True, default=False, show_default=True)
@click.option('--gen_lang_link', is_flag=True, default=False, show_default=True)
@click.option('--gen_sample_gold_tsv', is_flag=True, default=False, show_default=True)
@click.option('--gen_title2pid', is_flag=True, default=False, show_default=True)
@click.option('--gen_redirect', is_flag=True, default=False, show_default=True)
@click.option('--pre_matching', type=click.Choice(['mint', 'tinm', 'n']), default=cf.OptInfo.pre_matching_default,
              show_default=True)
@click.option('--title_matching_mint', '-tmm', type=click.Choice(['trim', 'full']),
              default=cf.OptInfo.title_matching_mint_default, show_default=True)
@click.option('--title_matching_tinm', '-tmt', type=click.Choice(['trim', 'full']),
              default=cf.OptInfo.title_matching_tinm_default, show_default=True)
@click.option('--char_match_min', default=cf.OptInfo.char_match_min_default, show_default=True, type=click.FLOAT)
@click.option('--gen_title2pid_ext', is_flag=True, default=False, show_default=True)
@click.option('--gen_html', is_flag=True, default=False, show_default=True)
@click.option('--gen_html_conv_year', is_flag=True, default=False, show_default=True)
@click.option('--gen_common_html', is_flag=True, default=False, show_default=True)
@click.option('--gen_common_html_conv_year', is_flag=True, default=False, show_default=True)
@click.option('--gen_link_prob', is_flag=True, default=False, show_default=True)
@click.option('--gen_linkable', is_flag=True, default=False, show_default=True)
@click.option('--gen_slink', is_flag=True, default=False, show_default=True)
@click.option('--gen_back_link', is_flag=True, default=False, show_default=True)
@click.option('--gen_link_dist', is_flag=True, default=False, show_default=True)
@click.option('--gen_incoming_link', is_flag=True, default=False, show_default=True)
@click.option('--f_self_link_by_attr_name', default=cf.DataInfo.f_self_link_by_attr_name_default, show_default=True,
              type=click.STRING, help='lists of attributes whose values are supposed to refer to the original entity, '
                                      'judging from the name of attributes.')
@click.option('--f_self_link_pat', default=cf.DataInfo.f_self_link_pat_default, show_default=True, type=click.STRING,
              help='lists of matching pattern and position to find self link attributes by attribute names.')
@click.option('--f_title2pid_ext', default=cf.DataInfo.f_title2pid_ext_default, show_default=True, type=click.STRING,
              help='from_title_to_pageid_extended_information. Filter out disambiguation, management, '
                   'or format-error pages, and add eneid, incoming link num info.')
@click.option('--f_title2pid_ext_obs', default=cf.DataInfo.f_title2pid_ext_obs_default, show_default=True,
              type=click.STRING,
              help='from_title_to_pageid_extended_information based on obsolete Wikipedia. Filter out disambiguation, '
                   'management or format-error pages, and add eneid, incoming link num info.')
@click.option('--f_title2pid_org', default=cf.DataInfo.f_title2pid_org_default, show_default=True, type=click.STRING,
              help='from_title_to_pageid_information_original.')
@click.option('--f_cirrus_content', default=cf.DataInfo.f_cirrus_content_default, show_default=True, type=click.STRING,
              help='cirrus dump (content) (.')
@click.option('--f_disambiguation', default=cf.DataInfo.f_disambiguation_default, show_default=True, type=click.STRING,
              help='disambiguation page list.')
@click.option('--f_disambiguation_pat', default=cf.DataInfo.f_disambiguation_pat_default, show_default=True,
              type=click.STRING, help='disambiguation pattern file.')
@click.option('--f_lang_link_dump_org', default=cf.DataInfo.f_lang_link_dump_org_default, show_default=True,
              type=click.STRING, help='langlinks dump org file')
@click.option('--f_lang_link_info', default=cf.DataInfo.f_lang_link_info_default, show_default=True,
              type=click.STRING, help='langlinks info file')
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
@click.option('--f_ene_def_for_task', default=cf.DataInfo.f_ene_def_for_task_default, show_default=True,
              type=click.STRING, help='f_ene_def_for_task')
@click.option('--f_enew_info', default=cf.DataInfo.f_enew_info_default, show_default=True, type=click.STRING,
              help='f_enew_info')
@click.option('--f_enew_org', default=cf.DataInfo.f_enew_org_default, show_default=True, type=click.STRING,
              help='f_enew_org')
@click.option('--f_enew_mod_list', default=cf.DataInfo.f_enew_mod_list_default, show_default=True, type=click.STRING,
              help='f_enew_mod_list')
@click.option('--f_sample_gold_mod_list', default=cf.DataInfo.f_sample_gold_mod_list_default, show_default=True,
              type=click.STRING, help='f_sample_gold_mod_list')
@click.option('--f_incoming', default=cf.DataInfo.f_incoming_default, show_default=True, type=click.STRING,
              help='f_incoming')
@click.option('--f_link_prob', default=cf.DataInfo.f_link_prob_default, show_default=True, type=click.STRING,
              help='f_link_prob')
@click.option('--f_linkable_info', type=click.STRING,
              default=cf.DataInfo.f_linkable_info_default, show_default=True,
              help='filename of linkable ratio info file.')
@click.option('--f_attr_rng_auto', default=cf.DataInfo.f_attr_rng_auto_default, show_default=True, type=click.STRING,
              help='f_attr_rng_auto')
@click.option('--f_attr_rng_man_org', default=cf.DataInfo.f_attr_rng_man_org_default, show_default=True,
              type=click.STRING, help='f_attr_rng_man_org')
@click.option('--f_attr_rng_man', default=cf.DataInfo.f_attr_rng_man_default, show_default=True, type=click.STRING,
              help='f_attr_rng_man')
@click.option('--f_slink', default=cf.DataInfo.f_slink_default, show_default=True, type=click.STRING,
              help='f_slink')
@click.option('--f_input_title', default=cf.DataInfo.f_input_title_default, show_default=True, type=click.STRING,
              help='f_input_title')
@click.option('--f_back_link', default=cf.DataInfo.f_back_link_default, show_default=True, type=click.STRING,
              help='f_back_link')
@click.option('--f_back_link_dump_org', default=cf.DataInfo.f_back_link_dump_org_default, show_default=True,
              type=click.STRING, help='f_back_link_dump_org')
@click.option('--f_page_dump', default=cf.DataInfo.f_page_dump_default, show_default=True, type=click.STRING,
              help='f_page_dump')
@click.option('--f_redirect_dump', default=cf.DataInfo.f_redirect_dump_default, show_default=True, type=click.STRING,
              help='f_redirect_dump')
@click.option('--f_page_dump_org', default=cf.DataInfo.f_page_dump_org_default, show_default=True, type=click.STRING,
              help='f_page_dump_org')
@click.option('--f_page_dump_old_org', default=cf.DataInfo.f_page_dump_old_org_default, show_default=True,
              type=click.STRING, help='f_page_dump_old_org')
@click.option('--f_redirect_dump_org', default=cf.DataInfo.f_redirect_dump_org_default, show_default=True,
              type=click.STRING, help='f_redirect_dump_org')
@click.option('--f_mention_gold_link_dist', default=cf.DataInfo.f_mention_gold_link_dist_default, show_default=True,
              type=click.STRING, help='f_mention_gold_link_dist')
@click.option('--f_target_attr_info', default=cf.DataInfo.f_target_attr_info_default, show_default=True,
              type=click.STRING, help='f_target_attr_info')
@click.option('--f_all_cat_info', default=cf.DataInfo.f_all_cat_info_default, show_default=True,
              type=click.STRING, help='f_all_cat_info')
@click.option('--f_wikipedia_page_change_info', default=cf.DataInfo.f_wikipedia_page_change_info_default,
              show_default=True, type=click.STRING, help='f_target_attr')
def ljc_prep_main(common_data_dir,
                  tmp_data_dir,
                  in_dir,
                  sample_gold_dir,
                  sample_input_dir,
                  char_match_min,
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
                  gen_lang_link,
                  gen_linkable,
                  gen_link_dist,
                  gen_link_prob,
                  gen_slink,
                  gen_target_attr,
                  gen_title2pid,
                  gen_title2pid_ext,
                  gen_sample_gold_tsv,
                  pre_matching,
                  gen_redirect,
                  title_matching_mint,
                  title_matching_tinm,
                  f_all_cat_info,
                  f_back_link,
                  f_back_link_dump_org,
                  f_attr_rng_auto,
                  f_attr_rng_man,
                  f_attr_rng_man_org,
                  f_cirrus_content,
                  f_common_html_info,
                  f_disambiguation,
                  f_disambiguation_pat,
                  f_ene_def_for_task,
                  f_enew_info,
                  f_enew_mod_list,
                  f_enew_org,
                  f_html_info,
                  f_incoming,
                  f_input_title,
                  f_lang_link_info,
                  f_lang_link_dump_org,
                  f_linkable_info,
                  f_link_prob,
                  f_mention_gold_link_dist,
                  f_mint_partial,
                  f_mint_trim_partial,
                  f_page_dump,
                  f_page_dump_old_org,
                  f_page_dump_org,
                  f_redirect_dump,
                  f_redirect_dump_org,
                  f_redirect_info,
                  f_sample_gold_mod_list,
                  f_self_link_by_attr_name,
                  f_self_link_pat,
                  f_slink,
                  f_target_attr_info,
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
                     prep_f_all_cat_info=f_all_cat_info,
                     prep_f_back_link=f_back_link,
                     prep_f_back_link_dump_org=f_back_link_dump_org,
                     prep_f_attr_rng_man_org=f_attr_rng_man_org,
                     prep_f_attr_rng_man=f_attr_rng_man,
                     prep_f_attr_rng_auto=f_attr_rng_auto,
                     prep_f_cirrus_content=f_cirrus_content,
                     prep_f_common_html_info=f_common_html_info,
                     prep_f_disambiguation=f_disambiguation,
                     prep_f_disambiguation_pat=f_disambiguation_pat,
                     prep_f_ene_def_for_task=f_ene_def_for_task,
                     prep_f_enew_info=f_enew_info,
                     prep_f_enew_mod_list=f_enew_mod_list,
                     prep_f_enew_org=f_enew_org,
                     prep_f_html_info=f_html_info,
                     prep_f_incoming=f_incoming,
                     prep_f_input_title=f_input_title,
                     prep_f_lang_link_dump_org=f_lang_link_dump_org,
                     prep_f_lang_link_info=f_lang_link_info,
                     prep_f_linkable=f_linkable_info,
                     prep_f_link_prob=f_link_prob,
                     prep_f_mention_gold_link_dist=f_mention_gold_link_dist,
                     prep_f_mint_partial=f_mint_partial,
                     prep_f_mint_trim_partial=f_mint_trim_partial,
                     prep_f_page_dump=f_page_dump,
                     prep_f_page_dump_old_org=f_page_dump_old_org,
                     prep_f_page_dump_org=f_page_dump_org,
                     prep_f_redirect_dump=f_redirect_dump,
                     prep_f_redirect_dump_org=f_redirect_dump_org,
                     prep_f_redirect_info=f_redirect_info,
                     prep_f_sample_gold_mod_list=f_sample_gold_mod_list,
                     prep_f_self_link_by_attr_name=f_self_link_by_attr_name,
                     prep_f_self_link_pat=f_self_link_pat,
                     prep_f_slink=f_slink,
                     prep_f_target_attr_info=f_target_attr_info,
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
            self.attr_rng_man_file = prep_common_data_dir + prep_f_attr_rng_man
            self.attr_rng_man_org_file = prep_common_data_dir + prep_f_attr_rng_man_org

            self.all_cat_info_file = prep_common_data_dir + prep_f_all_cat_info
            self.cirrus_content_file = prep_common_data_dir + prep_f_cirrus_content
            self.disambiguation_file = prep_common_data_dir + prep_f_disambiguation
            self.disambiguation_pat_file = prep_common_data_dir + prep_f_disambiguation_pat
            self.ene_def_for_task_file = prep_common_data_dir + prep_f_ene_def_for_task
            self.enew_info_file = prep_common_data_dir + prep_f_enew_info
            self.enew_mod_list_file = prep_common_data_dir + prep_f_enew_mod_list
            self.enew_org_file = prep_common_data_dir + prep_f_enew_org
            self.common_html_info_file = prep_common_data_dir + prep_f_common_html_info
            self.incoming_file = prep_common_data_dir + prep_f_incoming
            self.lang_link_info_file = prep_common_data_dir + prep_f_lang_link_info
            self.lang_link_dump_org_file = prep_common_data_dir + prep_f_lang_link_dump_org
            self.linkable_file = prep_common_data_dir + prep_f_linkable
            self.link_prob_file = prep_common_data_dir + prep_f_link_prob
            self.mention_gold_link_dist_file = prep_common_data_dir + prep_f_mention_gold_link_dist
            self.page_dump_file = prep_common_data_dir + prep_f_page_dump
            self.page_dump_old_org_file = prep_common_data_dir + prep_f_page_dump_old_org
            self.page_dump_org_file = prep_common_data_dir + prep_f_page_dump_org
            self.sample_gold_mod_list_file = prep_common_data_dir + prep_f_sample_gold_mod_list
            self.redirect_dump_file = prep_common_data_dir + prep_f_redirect_dump
            self.redirect_dump_org_file = prep_common_data_dir + prep_f_redirect_dump_org
            self.title2pid_ext_file = prep_common_data_dir + prep_f_title2pid_ext
            self.title2pid_ext_obs_file = prep_common_data_dir + prep_f_title2pid_ext_obs
            self.title2pid_org_file = prep_common_data_dir + prep_f_title2pid_org
            self.redirect_info_file = prep_common_data_dir + prep_f_redirect_info
            self.slink_file = prep_common_data_dir + prep_f_slink
            self.self_link_pat_file = prep_common_data_dir + prep_f_self_link_pat
            self.self_link_by_attr_name_file = prep_common_data_dir + prep_f_self_link_by_attr_name
            self.target_attr_info_file = prep_common_data_dir + prep_f_target_attr_info
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
    data_info_prep.back_link_dump_org_file = data_info_prep.common_data_dir + f_back_link_dump_org
    data_info_prep.cirrus_content_file = data_info_prep.common_data_dir + f_cirrus_content
    data_info_prep.disambiguation_file = data_info_prep.common_data_dir + f_disambiguation
    data_info_prep.disambiguation_pat_file = data_info_prep.common_data_dir + f_disambiguation_pat
    data_info_prep.ene_def_for_task_file = data_info_prep.common_data_dir + f_ene_def_for_task
    data_info_prep.enew_info_file = data_info_prep.common_data_dir + f_enew_info
    data_info_prep.enew_org_file = data_info_prep.common_data_dir + f_enew_org
    data_info_prep.enew_mod_list_file = data_info_prep.common_data_dir + f_enew_mod_list
    data_info_prep.common_html_info_file = data_info_prep.common_data_dir + f_common_html_info
    data_info_prep.incoming_file = data_info_prep.common_data_dir + f_incoming
    data_info_prep.lang_link_dump_org_file = data_info_prep.common_data_dir + f_lang_link_dump_org
    data_info_prep.linkable_file = data_info_prep.common_data_dir + f_linkable_info
    data_info_prep.link_prob_file = data_info_prep.common_data_dir + f_link_prob
    data_info_prep.mention_gold_link_dist_file = data_info_prep.common_data_dir + f_mention_gold_link_dist
    data_info_prep.sample_gold_mod_list_file = data_info_prep.common_data_dir + f_sample_gold_mod_list

    data_info_prep.title2pid_ext_file = data_info_prep.common_data_dir + f_title2pid_ext
    data_info_prep.title2pid_ext_obs_file = data_info_prep.common_data_dir + f_title2pid_ext_obs
    data_info_prep.title2pid_org_file = data_info_prep.common_data_dir + f_title2pid_org
    data_info_prep.redirect_info_file = data_info_prep.common_data_dir + f_redirect_info
    data_info_prep.slink_file = data_info_prep.common_data_dir + f_slink
    data_info_prep.self_link_pat_file = data_info_prep.common_data_dir + f_self_link_pat
    data_info_prep.self_link_attribute_by_name_file = data_info_prep.common_data_dir + f_self_link_by_attr_name
    data_info_prep.target_attr_info_file = data_info_prep.common_data_dir + f_target_attr_info
    data_info_prep.redirect_dump_file = data_info_prep.common_data_dir + f_redirect_dump
    data_info_prep.redirect_dump_org_file = data_info_prep.common_data_dir + f_redirect_dump_org
    data_info_prep.page_dump_file = data_info_prep.common_data_dir + f_page_dump
    data_info_prep.page_dump_org_file = data_info_prep.common_data_dir + f_page_dump_org

    # tmp_data_dir
    data_info_prep.back_link_file = data_info_prep.tmp_data_dir + f_back_link
    data_info_prep.html_info_file = data_info_prep.tmp_data_dir + f_html_info
    data_info_prep.input_title_file = data_info_prep.tmp_data_dir + f_input_title
    data_info_prep.mint_partial_file = data_info_prep.tmp_data_dir + f_mint_partial
    data_info_prep.mint_trim_partial_file = data_info_prep.tmp_data_dir + f_mint_trim_partial
    data_info_prep.tinm_partial_file = data_info_prep.tmp_data_dir + f_tinm_partial
    data_info_prep.tinm_trim_partial_file = data_info_prep.tmp_data_dir + f_tinm_trim_partial

    # sample_gold_dir
    sample_gold_linked_dir = data_info_prep.sample_gold_dir + 'link_annotation/'
    sample_gold_linked_dir_conv = data_info_prep.sample_gold_dir + 'link_annotation/conv/'

    sample_input_ene_dir = data_info_prep.sample_input_dir + 'ene_annotation/'
    sample_input_ene_dir_conv = data_info_prep.sample_input_dir + 'ene_annotation/conv/'

    data_info_prep.in_ene_dir = data_info_prep.in_dir + 'ene_annotation/'
    data_info_prep.in_html_dir = data_info_prep.in_dir + 'html/'

    if conv_year:
        tmp_input_ene_dir = data_info_prep.in_ene_dir + 'conv/'
        tmp_sample_input_ene_dir = sample_input_ene_dir_conv
        tmp_sample_gold_linked_dir = sample_gold_linked_dir_conv
    else:
        tmp_input_ene_dir = data_info_prep.in_ene_dir
        tmp_sample_input_ene_dir = sample_input_ene_dir
        tmp_sample_gold_linked_dir = sample_gold_linked_dir

    sample_input_html_dir = data_info_prep.sample_input_dir + 'html/'

    logger.info({
        'action': 'ljc_prep_main',
        'tmp_input_ene_dir': tmp_input_ene_dir,
        'tmp_sample_input_ene_dir': tmp_sample_input_ene_dir,
        'tmp_sample_gold_linked_dir': tmp_sample_gold_linked_dir,
        'sample_input_html_dir': sample_input_html_dir,
    })

    if gen_target_attr:
        logger.info({
            'action': 'gen_target_attr',
        })
        gen_target_attr_info(
            data_info_prep.ene_def_for_task_file,
            data_info_prep.target_attr_info_file,
            data_info_prep.all_cat_info_file,
            log_info)

    if conv_sample_json_pageid:
        logger.info({
            'action': 'conv_sample_pageid',
        })
        conv_input_pageid(
            sample_input_ene_dir,
            sample_input_ene_dir_conv,
            data_info_prep.wikipedia_page_change_info_file,
            log_info)
        conv_link_pageid(
            sample_gold_linked_dir,
            sample_gold_linked_dir_conv,
            data_info_prep.wikipedia_page_change_info_file,
            log_info)

    if gen_change_wikipedia_info:
        logger.info({
            'action': 'gen_change_wikipedia_info',
        })
        gen_change_wikipage_list(data_info_prep.page_dump_old_org_file, data_info_prep.page_dump_org_file,
                                 data_info_prep.wikipedia_page_change_info_file, log_info)

    if gen_sample_gold_tsv:
        d_eneid2enlabel = lc.reg_all_cat_info(data_info_prep.all_cat_info_file, log_info)
        logger.info({
            'action': 'gen_sample_gold_tsv',
            'tmp_sample_gold_linked_dir': tmp_sample_gold_linked_dir,
        })
        gen_linked_tsv_mod(
            tmp_sample_gold_linked_dir,
            data_info_prep.title2pid_ext_file,
            data_info_prep.sample_gold_mod_list_file,
            log_info,
            **d_eneid2enlabel)

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

    if gen_title2pid:
        logger.info({
            'run': 'gen_title2pid',
            'title2pid_org_file': data_info_prep.title2pid_org_file,
        })

        gen_title2pid_file(data_info_prep.redirect_dump_file, data_info_prep.page_dump_file,
                           data_info_prep.title2pid_org_file, cf.OptInfo.min_illegal_title_len, log_info)

    if gen_enew:
        gen_enew_info_file(data_info_prep.enew_org_file, data_info_prep.enew_mod_list_file,
                           data_info_prep.enew_info_file, log_info)

    if gen_enew_rev_year:
        gen_enew_info_rev_file(data_info_prep.enew_org_file,
                               data_info_prep.enew_mod_list_file,
                               data_info_prep.wikipedia_page_change_info_file,
                               data_info_prep.enew_info_file, log_info)

    if gen_lang_link:
        logger.info({
            'action': 'ljc_prep_main',
            'run': 'gen_lang_link',
            'title2pid_ext_file': data_info_prep.title2pid_ext_file,
            'lang_link_dump_org_file': data_info_prep.lang_link_dump_org_file,
            'lang_link_info_file': data_info_prep.lang_link_info_file,
        })
        gen_lang_link_info(
            data_info_prep.lang_link_dump_org_file,
            data_info_prep.title2pid_ext_file,
            data_info_prep.lang_link_info_file,
            log_info)

    if gen_title2pid_ext:
        logger.info({
            'action': 'ljc_prep_main',
            'run': 'gen_title2pid_ext',
            'title2pid_ext_file': data_info_prep.title2pid_ext_file,
            'incoming_file': data_info_prep.incoming_file,
            'enew_info_file': data_info_prep.enew_info_file,
            'redirect_info_file': data_info_prep.redirect_info_file,
        })
        gen_title2pid_ext_file(data_info_prep.title2pid_ext_file, data_info_prep.incoming_file,
                               data_info_prep.enew_info_file, data_info_prep.redirect_info_file,
                               log_info)

    if gen_back_link:
        logger.info({
            'run': 'gen_back_link',
            'tmp_input_ene_dir': tmp_input_ene_dir,
            'input_title_file': data_info_prep.input_title_file,
            'back_link_dump_org': data_info_prep.back_link_dump_org_file,
            'back_link_file': data_info_prep.back_link_file,
        })

        gen_input_title_file(tmp_input_ene_dir, data_info_prep.input_title_file, log_info)
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

    if gen_common_html:
        logger.info({
            'run': 'gen_common_html',
            'sample_input_html_dir': sample_input_html_dir,
            'common_html_info_file': data_info_prep.common_html_info_file
        })
        gen_html_info_file(sample_input_html_dir, data_info_prep.common_html_info_file, log_info)

    if gen_common_html_conv_year:
        logger.info({
            'run': 'gen_common_html_cnv_year',
            'sample_input_html_dir': sample_input_html_dir,
            'common_html_info_cnv_year_file': data_info_prep.common_html_info_file
        })
        gen_html_info_file_conv_year(
            sample_input_html_dir,
            data_info_prep.common_html_info_file,
            data_info_prep.wikipedia_page_change_info_file, log_info)

    if gen_link_dist:
        logger.info({
            'run': 'gen_link_dist',
            'common_html_info_file': data_info_prep.common_html_info_file,
            'tmp_sample_gold_linked_dir': tmp_sample_gold_linked_dir,
            'common_data_dir': data_info_prep.common_data_dir,
            'mention_gold_link_dist_file': data_info_prep.mention_gold_link_dist_file,
        })

        gen_mention_gold_link_dist(
            data_info_prep.common_html_info_file,
            tmp_sample_gold_linked_dir,
            data_info_prep.mention_gold_link_dist_file,
            log_info)

    if pre_matching == 'mint':

        if not title_matching_mint:
            logger.error({
                'action': 'ljc_prep_main',
                'error': 'title_matching_mint should be specified',
            })
            sys.exit()
        else:
            prematch_mention_title(
                tmp_input_ene_dir,
                data_info_prep,
                pre_matching,
                title_matching_mint,
                char_match_min,
                data_info_prep.lang_link_dump_org_file,
                log_info)

    elif pre_matching == 'tinm':
        if not title_matching_tinm:
            logger.error({
                'action': 'ljc_prep_main',
                'error': 'title_matching_tinm should be specified',
            })
            sys.exit()
        else:
            prematch_mention_title(
                tmp_input_ene_dir,
                data_info_prep,
                pre_matching,
                title_matching_tinm,
                char_match_min,
                data_info_prep.lang_link_dump_org_file,
                log_info)

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
        gen_html_info_file_conv_year(
            data_info_prep.in_html_dir,
            data_info_prep.html_info_file,
            data_info_prep.wikipedia_page_change_info_file,
            log_info)

    if gen_link_prob:
        logger.info({
            'run': 'gen_link_prob',
            'link_prob_file': data_info_prep.link_prob_file,
            'tmp_sample_gold_linked_dir': tmp_sample_gold_linked_dir
        })
        gen_link_prob_file(tmp_sample_gold_linked_dir, data_info_prep.link_prob_file, log_info)

    if gen_attr_rng:
        logger.info({
            'run': 'gen_attr_rng',
            'tmp_sample_gold_linked_dir': tmp_sample_gold_linked_dir,
            'attr_rng_auto_file': data_info_prep.attr_rng_auto_file,
        })
        d_eneid2enlabel = lc.reg_all_cat_info(data_info_prep.all_cat_info_file, log_info)

        gen_attr_rng_auto(tmp_sample_gold_linked_dir, data_info_prep.attr_rng_auto_file, log_info)

        gen_attr_rng_man(data_info_prep.attr_rng_man_org_file, data_info_prep.attr_rng_man_file, log_info,
                         **d_eneid2enlabel)

    if gen_slink:
        logger.info({
            'run': 'gen_slink',
            'tmp_sample_gold_linked_dir': tmp_sample_gold_linked_dir,
            'slink_file': data_info_prep.slink_file
        })
        gen_self_link_info(tmp_sample_gold_linked_dir, data_info_prep.slink_file, log_info)

        gen_self_link_by_attr_name(
            data_info_prep.self_link_pat_file,
            data_info_prep.target_attr_info_file,
            data_info_prep.self_link_by_attr_name_file,
            log_info)

    if gen_linkable:
        d_eneid2enlabel = {}
        d_eneid2enlabel = lc.reg_all_cat_info(data_info_prep.all_cat_info_file, log_info)
        logger.info({
            'run': 'gen_linkable',
            'tmp_sample_input_ene_dir': tmp_sample_input_ene_dir,
            'tmp_sample_gold_linked_dir': tmp_sample_gold_linked_dir,
            'linkable_file': data_info_prep.linkable_file
        })
        gen_linkable_info(tmp_sample_input_ene_dir, tmp_sample_gold_linked_dir, data_info_prep.linkable_file,
                          log_info, **d_eneid2enlabel)


def gen_linked_tsv_mod(linked_json_dir, title2pid_ext_file, mod_list_file, log_info, **d_cnv):
    """Convert linked json file (with title) to linked tsv file
       add ene category of page, title of linked page, ene category of linked paged using title2pid_ext_file
       filter some records based on stoplist

    args:
        linked_json_dir
        title2pid_ext_file
        mod_list_file
        log_info
        **d_cnv

    output:
        linked_tsv (tsv)
            format
                cat, pageid, title, attribute, text, start_line_id, start_offset, end_line_id, end_offset, link_pageid,
                link_page_title, linked_cat
            sample
                Person 2392906	桐谷華	地位職業	声優	38	20	38	22	1192	声優　　　地位職業名
    notice
        '\n' in text(mention) has been converted to '\\n'.
        f_title2pid_ext
            format
                (title(from page))\t(pageid(to page))\t(title(to page)\t(maximum number of incoming links(to page))
                \t(eneid_set(to_page))
            sample
                VIAF    2503159 バーチャル国際典拠ファイル      212754  {'1.7.0'}

        linked_json
            sample
            {"page_id": "1008136", "title": "ジェイ・デメリット", "attribute": "国籍", "ENE": "1.1",
            "text_offset": {"start": {"line_id": 45, "offset": 26}, "end": {"line_id": 45, "offset": 32},
            "text": "イングランド"}, "html_offset": {"start": {"line_id": 45, "offset": 478},
            "end": {"line_id": 45, "offset": 484}, "text": "イングランド"}, "link_page_id": "16627",
            "link_type": {"later_name": false, "part_of": false, "derivation_of": false}}
        mod_list_file
            stoplist

    """

    import json
    import pandas as pd
    from glob import glob
    import re

    import logging
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    logger.info({
        'action': 'gen_linked_tsv_mod',
        'linked_json_dir': linked_json_dir,
    })
    get_title = {}
    get_eneid_set = {}

    check_mod = {}
    with open(mod_list_file, 'r', encoding='utf-8') as ml:
        ml_reader = csv.reader(ml, delimiter='\t')
        for ml_line in ml_reader:
            cat = ml_line[0]
            pid = ml_line[1]
            attr = ml_line[3]
            mention = ml_line[4]
            link_pid = ml_line[9]

            tmp_key = ':'.join([cat, pid, attr, mention])

            check_mod[tmp_key] = link_pid

    with open(title2pid_ext_file, mode='r', encoding='utf-8') as f:

        reader = csv.reader(f, delimiter='\t')
        for rows in reader:
            to_title = rows[2]
            to_pid_str = rows[1]

            get_title[rows[1]] = rows[2]
            get_eneid_set[rows[1]] = rows[4]

    linked_json_files = linked_json_dir + '*.jsonl'

    for linked_json in glob(linked_json_files):
        if 'for_view' in linked_json:
            logger.error({
                'action': 'cnv_ene_pageid',
                'msg': 'illegal file: for_view',
            })
            sys.exit()
        go_list = []
        if '_dist.jsonl' in linked_json:
            linked_tsv = linked_json.replace('_dist.jsonl', '.tsv')
        else:
            linked_tsv = linked_json.replace('.jsonl', '.tsv')

        with open(linked_json, mode='r', encoding='utf-8') as g, open(linked_tsv, 'w', encoding='utf-8') as o:
            for g_line in g:
                g_key_list = []
                d_gline = json.loads(g_line)
                g_key_list = lc.get_key_list_with_ene_title(log_info, **d_gline)

                ene_label = ''
                cat = ''
                g_link_title = ''
                g_link_ene = ''
                lc.check_dic_key(g_key_list[0], log_info, **d_cnv)
                cat = d_cnv[g_key_list[0]]
                g_key_list[0] = cat

                text_pre = g_key_list[4]
                g_key_list[4] = '\\n'.join(text_pre.splitlines())

                tmp_cat_pid_attr_mention = ':'.join([cat, g_key_list[1], g_key_list[3], g_key_list[4]])

                g_link_pageid = g_key_list[9]

                if tmp_cat_pid_attr_mention in check_mod:
                    if check_mod[tmp_cat_pid_attr_mention] == g_link_pageid:
                        continue

                if get_title.get(g_link_pageid):
                    g_link_title = get_title[g_link_pageid]

                g_key_list.insert(10, g_link_title)

                g_link_ecat_list = []
                g_link_eneid_list = []
                if g_link_pageid:
                    if get_eneid_set.get(g_link_pageid):
                        g_link_eneid_list = lc.setstr2list(get_eneid_set[g_link_pageid], log_info)

                        for g_link_eneid in g_link_eneid_list:
                            lc.check_dic_key(g_link_eneid, log_info, **d_cnv)

                            g_link_ecat = d_cnv[g_link_eneid]
                            g_link_ecat_list.append(g_link_ecat)

                g_key_list.insert(11, g_link_ecat_list)
                g_key_list.insert(11, g_link_eneid_list)

                go_list.append(g_key_list)

            df_go = pd.DataFrame(go_list)
            df_go.to_csv(o, sep='\t', header=False, index=False)


def gen_lang_link_info(langlinks_dump, title2pid_ext, lang_link_info, log_info):
    """
    generate language link info
    :param langlinks_dump:
    :param title2pid_ext:
    :param lang_link_info:
    :param log_info:
    :return:
    """
    # import codecs

    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    check = {}
    with open(title2pid_ext, mode='r', encoding='utf-8') as t:
        t_reader = csv.reader(t, delimiter='\t')
        for t_line in t_reader:
            pid = t_line[1]
            check[pid] = 1

    # with codecs.open(langlinks_dump, encoding='utf-8', errors='replace') as ld,
    with open(langlinks_dump, encoding='utf-8', errors='replace') as ld, \
            open(lang_link_info, mode='w', encoding='utf-8') as o:
        ld_reader = csv.reader(ld, delimiter='\t')
        for ld_line in ld_reader:
            ja_pid_str = ld_line[0]
            # lang_code = ld_line[1]
            # f_title = ld_line[2]
            if ja_pid_str in check:
                writer = csv.writer(o, delimiter='\t', lineterminator='\n')
                writer.writerow(ld_line)


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
        if 'for_view' in in_file:
            logger.error({
                'action': 'cnv_ene_pageid',
                'msg': 'illegal file: for_view',
            })
            sys.exit()
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


def gen_target_attr_info(def_file, target_attr_info_file, all_cat_info_file, log_info):
    """
    gen target attribute info and cat info file
    :param def_file:
    :param target_attr_info_file:
    :param all_cat_info_file:
    :param log_info:
    :return:
    :output: target_attr_info_file, all_cat_info_file
    """
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)
    target_attr_prt_list = []
    all_cat_prt_list = []

    with open(def_file, mode='r', encoding='utf-8') as de:
        for d_line in de:
            d = json.loads(d_line)
            eneid = ''
            en_label = ''
            ja_label = ''
            attr_label = ''
            lc.check_dic_key('ENE_id', log_info, **d)

            eneid = d['ENE_id']
            if 'en' in d['name']:
                en_label = d['name']['en']
            if 'ja' in d['name']:
                ja_label = d['name']['ja']
            if 'attributes' in d:
                for at_dict in d['attributes']:
                    if 'linking_task' in at_dict:
                        if at_dict['linking_task']:
                            attr_label = at_dict['name']
                            target_attr_prt_list.append([eneid, ja_label, en_label, attr_label])

            all_cat_prt_list.append([eneid, ja_label, en_label])

    with open(target_attr_info_file, mode='w', encoding='utf8') as ta:
        t_writer = csv.writer(ta, delimiter='\t', lineterminator='\n')
        t_writer.writerows(target_attr_prt_list)

    with open(all_cat_info_file, mode='w', encoding='utf8') as ac:
        a_writer = csv.writer(ac, delimiter='\t', lineterminator='\n')
        a_writer.writerows(all_cat_prt_list)


def conv_input_pageid(input_dir, conv_dir, page_change_list, log_info):
    """
    Convert pageids in input files into new pageids and output new json files
    :param input_dir:
    :param conv_dir:
    :param page_change_list:
    :param log_info:
    :return:
    """
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
        if 'for_view' in in_file:
            logger.error({
                'action': 'cnv_ene_pageid',
                'msg': 'illegal file: for_view',
            })
            sys.exit()
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


def gen_input_title_file(tmp_in_dir, input_title_file, log_info):
    """extract page titles from input files
    args:
        tmp_in_dir
        input_title_file
        log_info
    output:
        input_title_file
    """
    import pandas as pd

    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    in_files = tmp_in_dir + '*.jsonl'
    check = {}
    for in_file in glob(in_files):
        if 'for_view' in in_file:
            logger.error({
                'action': 'cnv_ene_pageid',
                'msg': 'skipped for_view',
            })
            continue
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

def prematch_mention_title(in_ene_dir, data_info_prep, pre_matching, title_matching, char_match_min,
                           lang_link_info, log_info):
    """Pre-matching mention title.
       titles include foreign titles based on language links.
    args:
        in_ene_dir,
        data_info_prep:
        pre_matching
        title_matching
        char_match_min
        lang_link_info
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
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    if not os.path.exists(in_ene_dir):
        logger.error({
            'action': 'prematch_mention_title',
            'msg': 'illegal in_ene_dir',
            'in_ene_dir': in_ene_dir
        })

    in_files = in_ene_dir + '*.jsonl'
    logger.info({
        'action': 'prematch_mention_title',
        'in_files': in_files,
    })
    d_pid2fromtitle = reg_pid2title(data_info_prep.title2pid_ext_file, lang_link_info, log_info)

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
        if 'for_view' in in_file:
            logger.error({
                'action': 'cnv_ene_pageid',
                'msg': 'skipped for_view',
            })
            continue
        logger.info({
            'action': 'prematch_mention_title',
            'in_file': in_file,
        })
        with open(in_file, mode='r', encoding='utf-8') as i:
            fname = in_file.replace(in_ene_dir, '')

            for i_line in i:
                rec = json.loads(i_line)
                mention = rec['text_offset']['text']
                for pid, title_list in d_pid2fromtitle.items():
                    for (title, lang_code) in title_list:
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
                                    pass
                                else:
                                    trimmed_list.pop()
                                    tmp_title = ' ('.join(trimmed_list)
                                    # single characters (num, jsymbol, kana)
                                    if num_jsymbol_kana_pat.fullmatch(tmp_title):
                                        continue
                                    else:
                                        if len(trimmed_list) > 2:
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
                                df = df.append(
                                    {'mention': mention, 'pid': pid, 'title': title, 'ratio': ratio,
                                     'lang_code': lang_code}, ignore_index=True)
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

        if fname in check_new_id:
            fname = check_new_id[fname]

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

                for link in links:
                    tmp_title = ''
                    try:
                        href_char = link.get('href')
                        if href_char:
                            if ('action=edit' in href_char) or ('returntoquery' in href_char) or (
                                    'en.wikipedia.org' in href_char):
                                continue

                    except(NameError, ValueError):
                        continue

                    if 'rel' in link.attrs and 'nofollow' in link.attrs['rel']:
                        continue
                    if 'accesskey' in link.attrs:
                        continue
                    if 'class' in link.attrs:
                        tmp_class = link.attrs['class']
                        if len(tmp_class[0]) > 0 and 'mw-redirect' not in tmp_class[0]:
                            continue
                    if 'title' not in link.attrs:
                        continue
                    tmp_title = link.attrs['title']
                    if len(tmp_title) == 0:
                        continue
                    elif tmp_title.startswith(dis_pat_title_head):
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
                    regex_pat = re.escape('>' + link.text + '<')

                    try:
                        taglist = list(re.finditer(regex_pat, line))
                    except ValueError:
                        continue
                    for tag in taglist:
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
                    try:
                        href_char = link.get('href')

                        if href_char:
                            if ('action=edit' in href_char) or ('returntoquery' in href_char) or (
                                    'en.wikipedia.org' in href_char):
                                continue

                    except(NameError, ValueError):
                        continue

                    if 'rel' in link.attrs and 'nofollow' in link.attrs['rel']:
                        continue
                    if 'accesskey' in link.attrs:
                        continue
                    if 'class' in link.attrs:
                        tmp_class = link.attrs['class']
                        if len(tmp_class[0]) > 0 and 'mw-redirect' not in tmp_class[0]:
                            continue
                    if 'title' not in link.attrs:
                        continue
                    tmp_title = link.attrs['title']

                    if len(tmp_title) == 0:
                        continue
                    elif tmp_title.startswith(dis_pat_title_head):
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
                    regex_pat = re.escape('>' + link.text + '<')

                    try:
                        taglist = list(re.finditer(regex_pat, line))
                    except ValueError:
                        continue
                    for tag in taglist:

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

    labels = ['cat', 'pid', 'line_id', 'html_text_start', 'html_text_end', 'html_text', 'title']

    with open(html_info_file, 'w') as o:
        writer = csv.DictWriter(o, fieldnames=labels, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        for elem in html_info_list:
            writer.writerow(elem)


def reg_pid2title(title2pid_ext_file, lang_link_info, log_info):

    """Register title2pid_info pages info.
    Args:
        title2pid_ext_file
        lang_link_info
        log_info
    Returns:
        d_pid2fromtitle dict
            {pid: [(title1,ja) (title2,en) ....]}

    Notice:
        - title2pid_ext_file
            format: 'from_title'\t'to_pid'\t'to_title'\t'to_incoming\t'{to_eneid1, to_eneid2, ...}'
       　　　sample:
            ロメオとジュリエット 28783 ロミオとジュリエット 806 {'1.7.13.4', '1.7.13.5'}
            日本國  1864744 日本    345455  {'1.5.1.3'}
            フジテレビジョン        4058860 フジテレビジョン        38288   {'1.4.6.2', '1.7.24.1'}


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
            d_pid2fromtitle[to_pid_str].append((from_title, 'ja'))

    with open(lang_link_info, mode='r', encoding='utf-8', errors='replace') as ll:
        l_reader = csv.reader(ll, delimiter='\t')

        for l_line in l_reader:
            ja_pid_str = l_line[0]
            lang_code = l_line[1]
            f_title = l_line[2]

            if not d_pid2fromtitle.get(ja_pid_str):
                d_pid2fromtitle[ja_pid_str] = []
            d_pid2fromtitle[ja_pid_str].append((f_title, lang_code))
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
                \t(eneid_set(to_page))
            sample
                ユナイテッドステイツ    1698838 アメリカ合衆国  116818  {'1.5.1.3'}
                VIAF (識別子)   2503159 バーチャル国際典拠ファイル      212754  {'1.7.0'}

     Notice:
         - redirect info
            - In the redirect info,
                - white spaces in Wikipedia titles are replaced by '_'.
                - Some records with illegal formats (eg. lack of to_pageid) are deleted.
                - Disambiguation pages are deleted (although not always completely).
            - sample 安倍晋三/log20200516	4136738
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
    get_to_eneid = {}
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
            if to_pid not in get_to_eneid:
                get_to_eneid[to_pid] = set()
            get_to_eneid[to_pid].add(to_eneid)
            if to_pid not in get_to_title:
                get_to_title[to_pid] = to_title

    get_to_incoming = {}
    with open(incoming, mode='r', encoding='utf-8') as i:
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

            if not get_to_title.get(to_pid):
                get_to_title[to_pid] = to_title

    with open(redirect_info, mode='r', encoding='utf-8') as e:
        reader = csv.reader(e, delimiter='\t')
        rec_list = []
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
            if get_to_title.get(to_pid):
                to_title = get_to_title[to_pid]

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

            if get_to_eneid.get(to_pid):
                to_eneid_set = get_to_eneid[to_pid]
                if not to_eneid_set:
                    logger.warning({
                        'action': 'gen_title2pid_ext_file',
                        'msg': 'missing to_eneid',
                        'to_eneid_set': to_eneid_set
                    })

            rec = [from_title, to_pid, to_title, to_incoming, to_eneid_set]
            rec_list.append(rec)

        df = pd.DataFrame(rec_list, columns=['from_title', 'to_pid', 'to_title', 'to_incoming', 'to_eneid_set'])
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
    :notice:
       sample row
       'grow': ['Person', '1115527', 'ヴォルフガング・オヴェラート', '国籍', 'ドイツ', '44', '6', '44', '9', '1698878',
       'ドイツ', 'Country']}

    """
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    if row[1] == row[9]:
        return 1
    else:
        return 0


def gen_linkable_info(sample_e_dir, sample_g_dir, linkable_info_file, log_info, **d_cnv):
    """Generate linkable info
    args:
        sample_in_ene_dir
        sample_gold_linked_dir
        linkable_info_file:
        log_info:
        d_cnv:
    return:
    output:
        linkable_info_file
        format: 'cat', 'attr', 'ratio', 'linkable_freq', 'all_freq' (*.tsv)
    Note:
        gold file
            Gold files (eg. sample gold files) used for linkable estimation should be located in gold_dir.
            sample
                Person	1061108	松田秀知	所属組織	フジテレビ	36	52	36	57	4058860	フジテレビジョン
                ['1.4.6.2', '1.7.24.1']	['Company', 'Channel']
    """
    import pandas as pd
    import re
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)
    logger.info({
        'action': 'gen_linkable_info',
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
        if 'for_view' in ene_file:
            logger.error({
                'action': 'gen_linkable_info',
                'msg': 'skipped for_view',
            })
            continue
        with open(ene_file, mode='r', encoding='utf-8') as ef:
            e_fname = ene_file.replace(sample_e_dir, '')

            e_cat = ''
            for e_line in ef:
                erec = json.loads(e_line)

                lc.check_dic_key('attribute', log_info, **erec)
                e_attr = erec['attribute']
                lc.check_dic_key('ENE', log_info, **erec)
                e_cat = d_cnv[erec['ENE']]
                e_cat_attr = e_cat + ':' + e_attr

                if not count_e_cat_attr.get(e_cat_attr):
                    count_e_cat_attr[e_cat_attr] = 1
                else:
                    count_e_cat_attr[e_cat_attr] += 1

    for g_file in glob(gold):
        if 'for_view' in g_file:
            logger.error({
                'action': 'gen_linkable_info',
                'msg': 'illegal file: for_view',
            })
            sys.exit()
        with open(g_file, mode='r', encoding='utf-8') as gf:
            g_cat = ''
            g_fname = g_file.replace(sample_g_dir, '')

            for g_line in gf:
                grec = json.loads(g_line)
                lc.check_dic_key('attribute', log_info, **grec)

                g_attr = grec['attribute']
                lc.check_dic_key('ENE', log_info, **grec)
                g_cat = d_cnv[grec['ENE']]
                g_cat_attr = g_cat + ':' + g_attr

                if grec['link_page_id']:
                    if not count_g_cat_attr.get(g_cat_attr):
                        count_g_cat_attr[g_cat_attr] = 1
                    else:
                        count_g_cat_attr[g_cat_attr] += 1

    for cat_attr in count_e_cat_attr:
        (t_cat, t_attr) = re.split(':', cat_attr)
        linked_freq = 0
        all_freq = 0
        if count_g_cat_attr.get(cat_attr):
            t_ratio_str = count_g_cat_attr[cat_attr]/count_e_cat_attr[cat_attr]
            t_ratio = float(Decimal(t_ratio_str).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
            linked_freq = count_g_cat_attr[cat_attr]
            all_freq = count_e_cat_attr[cat_attr]
        else:
            t_ratio = 0.0

        prt_list.append([t_cat, t_attr, t_ratio, linked_freq, all_freq])

    sdf = pd.DataFrame(prt_list, columns=['cat', 'attr', 'ratio', 'linked_freq', 'all_freq'])
    sdf.to_csv(linkable_info_file, sep='\t', header=False, index=False)


def gen_self_link_info(gold_dir, self_link_info_file, log_info):

    """Generate self link info
    args:
        gold_dir
        self_link_info_file:
        log_info:
    return:
    output: (2)
        self_link_info_file

        School  別名    1.0       10    10
        School  標語    0.0        0     1
        School  種類    0.0        0     2

    Note:
        gold file
            sample
                ['Galaxy', '1243163', 'M61 (天体)', '種類', 'フェイスオン銀河', '259', '45', '259', '53', '', '', '[]',
                '[]']}
                ['Galaxy', '1243163', 'M61 (天体)', '属する天体', 'おとめ座銀河団', '260', '0', '260', '7', '279791',
                'おとめ座銀河['Galaxy']"]}
    """

    import pandas as pd
    import re
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    prt_list = []
    ext = '.tsv'

    gold = gold_dir + '*.tsv'

    sumup_cat_attr = {}
    sumup_self_cat_attr = {}

    sumup_self_attr = {}

    for g_fname in glob(gold):
        check_gold = {}
        check_self_gold = {}
        cat = ''
        with open(g_fname, mode='r', encoding='utf-8') as f:
            greader = csv.reader(f, delimiter='\t')

            for grow in greader:

                cat = grow[0]
                gold_key = '\t'.join(grow[1:9])

                if not check_gold.get(gold_key):
                    check_gold[gold_key] = 1

                if check_self(grow, log_info):
                    if not check_self_gold.get(gold_key):
                        check_self_gold[gold_key] = 1
                    else:
                        check_self_gold[gold_key] += 1

        for common_key in check_gold:
            common_key_list = re.split('\t', common_key)

            attr = common_key_list[2]
            cat_attr = cat + '\t' + attr

            if not sumup_cat_attr.get(cat_attr):
                sumup_cat_attr[cat_attr] = check_gold[common_key]
            else:
                sumup_cat_attr[cat_attr] += check_gold[common_key]

            if check_self_gold.get(common_key):
                if not sumup_self_cat_attr.get(cat_attr):
                    sumup_self_cat_attr[cat_attr] = check_self_gold[common_key]
                else:
                    sumup_self_cat_attr[cat_attr] += check_self_gold[common_key]

    for t_cat_attr in sumup_cat_attr:
        (t_cat, t_attr) = re.split('\t', t_cat_attr)
        self_link_freq = 0
        cat_attr_freq = sumup_cat_attr[t_cat_attr]
        t_ratio = 0.0
        if sumup_self_cat_attr.get(t_cat_attr):
            self_link_freq = sumup_self_cat_attr[t_cat_attr]
            t_ratio_str = sumup_self_cat_attr[t_cat_attr]/sumup_cat_attr[t_cat_attr]
            t_ratio = float(Decimal(t_ratio_str).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

        prt_list.append([t_cat, t_attr, t_ratio, self_link_freq, cat_attr_freq])

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
    get back link info and save in back link info file
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
                if d_pid_title_incoming_eneid.get(from_pageid):
                    from_title = d_pid_title_incoming_eneid[from_pageid][0]
                back_link_list.append([org_title, from_pageid, from_title])

    df = pd.DataFrame(back_link_list, columns=['org_title', 'from_pageid', 'from_title'])
    df.to_csv(back_link, sep='\t', header=False, index=False)


def gen_link_prob_file(gold_dir, link_prob_file, log_info):
    """
    create link probability info file based on link statistics in sample gold file
    :param:gold_dir (eg. sample_gold_linked_dir)
    :param:link_prob_file
    :param:log_info
    :output: link_prob_file
    :notice
        gold file
        (sample)
         - `Person	1058520	竹内えり	作品	白い巨塔	79	0	79	4	29582
        白い巨塔 (2003年のテレビドラマ)	['1.7.13.2']　['Broadcast_Program']`
         - `Person	990044	細井雄二	作品	快傑ズバット	107	1	107	7	130767	快傑ズバット	['1.7.12', '1.7.13.2']
        ['Character', 'Broadcast_Program']`
        - Person	1061108	松田秀知	所属組織	フジテレビ	36	52	36	57	4058860	フジテレビジョン
        ['1.4.6.2', '1.7.24.1']	['Company', 'Channel']
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

            cat = ''
            reader = csv.reader(g, delimiter='\t')

            for line in reader:
                if len(line) < 10:
                    logger.warning({
                        'action': 'gen_link_prob_file',
                        'warning': 'format error list too short (skipped)',
                        'line': line,
                    })
                    continue

                cat = line[0]
                attr_name = line[3]
                attr_value = line[4]
                link_pid = line[9]
                cat_attname_attval = cat + '\t' + attr_name + '\t' + attr_value
                if not d.get(cat_attname_attval):
                    d[cat_attname_attval] = {}
                if not d[cat_attname_attval].get(link_pid):
                    d[cat_attname_attval][link_pid] = 1
                else:
                    d[cat_attname_attval][link_pid] += 1

    d_new = {}
    for cat_attr_val, link_pid_info in d.items():
        if cat_attr_val not in d_new:
            d_new[cat_attr_val] = []
        link_pid_info_sorted = sorted(link_pid_info.items(), key=lambda x: x[1], reverse=True)

        if len(link_pid_info_sorted) >= 1:
            link_sum = 0
            for tmp_lpinfo in link_pid_info_sorted:
                link_sum += tmp_lpinfo[1]

            for tmp_lpinfo in link_pid_info_sorted:
                ratio_str = str(tmp_lpinfo[1] / link_sum)
                ratio = float(Decimal(ratio_str).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
                link_pid_info_string = tmp_lpinfo[0] + ':' + str(ratio) + ':' + str(tmp_lpinfo[1])
                d_new[cat_attr_val].append(link_pid_info_string)
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
        tag_info (with header
            format
                cat     pid     line_id html_text_start html_text_end   html_text       title
            sample
                cat     pid     line_id html_text_start html_text_end   html_text       title
                Insect  2524837 54      136     138     分類    生物の分類
                Insect  2524837 69      145     146     界      界 (分類学)
        gold_file
            sample
            Person	1061108	松田秀知	所属組織	フジテレビ	36	52	36	57	4058860	フジテレビジョン
            ['1.4.6.2', '1.7.24.1']	['Company', 'Channel']
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
        cat = ''
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

            if not check_cat_pid_title_line.get(cat_pid_title_line):
                cat_pid_title_dic[cat_pid_title] = []
            cat_pid_title_dic[cat_pid_title].append(int(line_start))
            check_cat_pid_title_line[cat_pid_title_line] = 1

    out_raw_list = []
    for gfile in glob(gold_files):
        list_rec_out = []

        ene_cat = ''
        with open(gfile, 'r', encoding='utf-8') as g:
            greader = csv.reader(g, delimiter='\t')

            for grow in greader:
                ene_cat = grow[0]
                g_org_pid = grow[1]
                g_org_title = grow[2]
                g_attr = grow[3]
                g_mention_line_start = grow[5]
                g_gold_title = grow[10]
                g_cat_pid_title = ':'.join([ene_cat, g_org_pid, g_gold_title])

                if cat_pid_title_dic.get(g_cat_pid_title):
                    tmp_lineid_list = cat_pid_title_dic[g_cat_pid_title]
                    found = 0
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


# def check_pageid(pageid, log_info, **d_dis):
def check_pageid(pageid, **d_dis):
    """ check pageid if it can be a candidate link page (disambiguation, isdigit)
    Args:
        pageid
        **d_dis
    Returns:
        1: ok (can be candidate)
        0: disambiguation
        -1: ng
    """
    if not pageid:
        return -1
    elif not str(pageid).isdigit():
        return -1
    elif d_dis.get(str(pageid)):
        return 0
    else:
        return 1


def gen_title2pid_file(redirect_dump, page_dump, title2pageid_org, illegal_title_len, log_info):
    """
    :param redirect_dump:
    :param page_dump:
    :param title2pageid_org:
    :param illegal_title_len:
    :param log_info:
    :return:

    cf. title2pid(org)
    {"page_id": 871214, "title": "日就社", "is_redirect": true, "redirect_to": {"page_id": 1526294,
    "title": "読売新聞", "is_redirect": false}}
    {"page_id": 2238511, "title": "読売争議", "is_redirect": true, "redirect_to": {"page_id": 1526294,
    "title": "読売新聞", "is_redirect": false}}
    {"page_id": 1526294, "title": "読売新聞", "is_redirect": false}
    {"page_id": 1262543, "title": "読売新聞縮刷版", "is_redirect": true, "redirect_to": {"page_id": 1526294,
    "title": "読売新聞", "is_redirect": false}}
    {"page_id": 158932, "title": "讀賣新聞", "is_redirect": true, "redirect_to": {"page_id": 1526294,
    "title": "読売新聞", "is_redirect": false}}

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

    from_pid_to_title = {}
    with open(redirect_dump, mode='r', encoding='utf-8') as rd:
        r_reader = csv.reader(rd, delimiter='\t')
        for r_row in r_reader:
            from_pid_str = str(r_row[0])
            to_title = r_row[1]
            namespace_char = str(r_row[2])

            if len(to_title) >= illegal_title_len:
                if namespace_char == '0':
                    sys.exit()

            if namespace_char != '0':
                continue

            from_pid_to_title[from_pid_str] = to_title

    pid2title = {}
    title2pid = {}
    check_namespace = {}
    check_redirect = {}
    with open(page_dump, mode='r', encoding='utf-8') as pd:
        p_reader = csv.reader(pd, delimiter='\t')
        for p_row in p_reader:

            pid_str = str(p_row[0])
            title = p_row[1]

            redirect = str(p_row[2])
            namespace_char = str(p_row[3])

            if namespace_char != '0':
                continue
            check_namespace[pid_str] = namespace_char
            if len(title) >= illegal_title_len:
                sys.exit()

            if redirect == '1':
                check_redirect[pid_str] = 1

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
        d = {}
        tmp_char = ''
        d['page_id'] = tmp_id_str

        if tmp_title != '\\':
            if '\\' in tmp_title:
                tmp_title_pre = tmp_title
                tmp_title = re.sub(r'\\', '', tmp_title_pre)
        d['title'] = tmp_title

        if tmp_id_str not in check_redirect:
            d['is_redirect'] = False
        else:
            d['is_redirect'] = True

            if tmp_id_str not in from_pid_to_title:
                continue
            else:
                redirect_to_title = from_pid_to_title[tmp_id_str]

                if redirect_to_title not in title2pid:
                    continue

                else:
                    tmp_to_pid_str = title2pid[redirect_to_title]
                    if tmp_to_pid_str in check_namespace:
                        if check_namespace[tmp_to_pid_str] != '0':
                            continue

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
            t.write('\n')


def gen_change_wikipage_list(old_page_dump_org_file, page_dump_org_file, change_id_list, log_info):
    check_old_pageid = {}
    prt_list = []
    with open(old_page_dump_org_file, mode='r', encoding='utf-8') as op:
        op_reader = csv.reader(op, delimiter='\t')
        for op_line in op_reader:
            old_pageid = op_line[0]
            old_title = op_line[1]
            old_namespace = op_line[3]

            if old_namespace == '0':
                check_old_pageid[old_title] = old_pageid

    with open(page_dump_org_file, mode='r', encoding='utf-8') as np:
        np_reader = csv.reader(np, delimiter='\t')
        for np_line in np_reader:
            new_pageid = np_line[0]
            new_title = np_line[1]
            new_namespace = np_line[3]
            if new_namespace == '0':
                if new_title in check_old_pageid:
                    if check_old_pageid[new_title] != new_pageid:
                        prt_list.append([check_old_pageid[new_title], new_pageid])

    with open(change_id_list, mode='w', encoding='utf-8') as cl:
        writer = csv.writer(cl, delimiter='\t', lineterminator='\n')
        writer.writerows(prt_list)


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
            if not rd['title']:
                continue
            from_pid = rd['page_id']
            if check_pageid(from_pid, **d_dis) != 1:
                continue
            from_title = rd['title'].replace('_', ' ')
            if rd['is_redirect']:
                if 'redirect_to' not in rd:
                    logging.warning({
                        'run': 'gen_redirect_info_file',
                        'msg': 'redirect_to not found',
                        'rd': rd
                    })
                    continue
                if 'page_id' not in rd['redirect_to']:
                    continue
                to_pid = rd['redirect_to']['page_id']
                if check_pageid(to_pid, **d_dis) != 1:
                    continue
                title_apid[from_title] = str(to_pid)
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
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    check_pos = {}
    with open(self_link_patfile, mode='r', encoding='utf-8') as p:
        p_reader = csv.reader(p, delimiter='\t')
        for p_line in p_reader:
            pos = p_line[0]
            pat = p_line[1]
            check_pos[pat] = pos
    check_target_attr = {}
    with open(target_attr_file, mode='r', encoding='utf-8') as ta:
        ta_reader = csv.reader(ta, delimiter='\t')

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

            pat_pos = pat + '\t' + pos
            if 'cat' in field:
                check_cat[pat] = pos
            if 'title' in field:
                check_title[pat] = pos

    with gzip.open(cirrus, mode='rt', encoding='utf-8') as c:

        id_title = []
        for c_line in c:
            check_dis = 0
            d = json.loads(c_line)
            if 'index' in d:
                tmp_id = str(d['index']['_id'])
            else:
                if 'namespace' in d:
                    if d['namespace'] != 0:
                        continue
                lc.check_dic_key('title', log_info, **d)
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
                    lc.check_dic_key('category', log_info, **d)
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
            if 'pageid' in t:
                pageid = t['pageid']
            elif 'page_id' in t:
                pageid = t['page_id']
            title = t['title']

            if t['ENEs']:
                for k, v in t['ENEs'].items():
                    for m in v:
                        if 'ENE' in m:
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
                lc.check_dic_key('title', log_info, **d)
                tmp_title = d['title']

                lc.check_dic_key('incoming_links', log_info, **d)
                tmp_link_num = d['incoming_links']
                id_title_link.append([tmp_id, tmp_title, tmp_link_num])

    with open(outfile, 'w', encoding='utf-8') as o:
        writer = csv.writer(o, delimiter='\t', lineterminator='\n')
        writer.writerows(id_title_link)


def gen_attr_rng_auto(gold_tsv_dir, attr_rng_auto_file, log_info):
    """
    generate attribute range info (auto)
    :param gold_tsv_dir:
    :param attr_rng_auto_file:
    :param log_info:
    # :param d_cnv:
    :return:
    :output:
        attr_rng_info_file
        - Music	プロデューサー	1.1	Person	0.5	1	2
        - Music	プロデューサー	1.4.2	Show_Organization	0.5	1	2
    :notice:   リンク先がカテゴリに変更されている！
       gold_tsv
            sample:
            `Person	990044	細井雄二	作品	快傑ズバット	107	1	107	7	130767	快傑ズバット	['1.7.12', '1.7.13.2']
['Character', 'Broadcast_Program']`
    """
    import pandas as pd
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    gold_files = gold_tsv_dir + '*.tsv'

    prt_list = []
    for gold_file in glob(gold_files):
        cnt_cat_attr = {}
        logger.info({
            'action': 'gen_attr_rng_auto',
            'gold_file': gold_file
        })
        cnt_cat_attr_linked_eneid_cat = {}
        with open(gold_file, mode='r', encoding='utf-8') as ar:
            ar_reader = csv.reader(ar, delimiter='\t')
            cat = ''
            for ar_line in ar_reader:
                cat = ar_line[0]
                attr = ar_line[3]
                cat_attr = cat + '\t' + attr
                if cat_attr not in cnt_cat_attr:
                    cnt_cat_attr[cat_attr] = 0
                cnt_cat_attr[cat_attr] += 1

                linked_eneid_list = lc.liststr2list(ar_line[11], log_info)
                linked_cat_list = lc.liststr2list(ar_line[12], log_info)

                cat_attr_linked_eneid_cat = ''
                for i in range(len(linked_eneid_list)):
                    linked_eneid = linked_eneid_list[i]
                    linked_cat = linked_cat_list[i]
                    cat_attr_linked_eneid_cat = '\t'.join([cat, attr, linked_eneid, linked_cat])
                    if cat_attr_linked_eneid_cat not in cnt_cat_attr_linked_eneid_cat:
                        cnt_cat_attr_linked_eneid_cat[cat_attr_linked_eneid_cat] = 0
                    cnt_cat_attr_linked_eneid_cat[cat_attr_linked_eneid_cat] += 1

            for t_cat_attr_eneid_cat in cnt_cat_attr_linked_eneid_cat:
                cat_attr_eneid_cat_freq = cnt_cat_attr_linked_eneid_cat[t_cat_attr_eneid_cat]
                (t_cat, t_attr, t_linked_eneid, t_linked_cat) = re.split('\t', t_cat_attr_eneid_cat)

                if not t_linked_eneid:
                    continue

                t_cat_attr = t_cat + '\t' + t_attr

                cat_attr_freq = 0
                if t_cat_attr in cnt_cat_attr:
                    cat_attr_freq = cnt_cat_attr[t_cat_attr]

                    t_ratio_str = cat_attr_eneid_cat_freq / cat_attr_freq
                    t_ratio = float(Decimal(t_ratio_str).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
                else:
                    t_ratio = 0.0
                prt_list.append([t_cat, t_attr, t_linked_eneid, t_linked_cat, t_ratio, cat_attr_eneid_cat_freq,
                                 cat_attr_freq])

    sdf = pd.DataFrame(prt_list, columns=['cat', 'attr', 'eneid', 'en_label', 'ratio', 'freq', 'sum'])
    sdf.to_csv(attr_rng_auto_file, sep='\t', header=False, index=False)


def gen_attr_rng_man(attr_rng_man_org_file, attr_rng_man_file, log_info, **d_cnv):
    """

    :param attr_rng_man_org_file:
    :param attr_rng_man_file:
    :param log_info:
    :param d_cnv:
    :return:
    :notice:
    attr_rng_man_file
        header: yes
    attr_rng_man_org_file
    format:  cat, attr, rng_eneid, rng_cat, ratio
    sample:
        Music   アーティスト    1.1 Person 1
        Music   スタッフ        1.1 Person 1
    """

    import pandas as pd
    logger = set_logging_pre(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    prt_list = []
    with open(attr_rng_man_org_file, mode='r', encoding='utf-8') as am:
        am_reader = csv.reader(am, delimiter='\t')
        for am_line in am_reader:
            cat = am_line[0]
            attr = am_line[1]
            rng_eneid = am_line[2]
            rng_ratio = am_line[3]
            lc.check_dic_key(rng_eneid, log_info, **d_cnv)
            rng_en_label = d_cnv[rng_eneid]

            prt_list.append([cat, attr, rng_eneid, rng_en_label, rng_ratio])

    sdm = pd.DataFrame(prt_list, columns=['cat', 'attr', 'eneid', 'en_label', 'ratio'])
    sdm.to_csv(attr_rng_man_file, sep='\t', header=False, index=False)


if __name__ == '__main__':
    ljc_prep_main()
