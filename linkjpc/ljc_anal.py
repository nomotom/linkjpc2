import csv
import os
import sys
from glob import glob
import ljc_common as lc
import logging
import config as cf
import click
import logging.config


def set_logging(log_info, logger_name):
    from os import path

    logging_ini = log_info.logging_ini
    log_file_path = path.join(path.dirname(path.abspath(__file__)), logging_ini)
    logging.config.fileConfig(log_file_path)

    logger = logging.getLogger(logger_name)
    return logger


@click.command()
@click.argument('gold_dir', type=click.Path(exists=True))
@click.argument('anal_dir_version', type=click.Path(exists=True))
@click.argument('sys_dir_common', type=click.Path(exists=True))
@click.argument('sys_dir_version', type=click.Path(exists=True))
@click.argument('data_dir_common', type=click.Path(exists=True))
@click.option('--f_target', default=cf.AnalDataInfo.f_target_default, show_default=True, type=click.STRING,
              help='target_fle.')
@click.option('--f_diff_judge', default=cf.AnalDataInfo.f_diff_judge_info_default, show_default=True, type=click.STRING,
              help='diff_judge_fle.')
@click.option('--f_ok_freq_info', default=cf.AnalDataInfo.f_ok_freq_info_default, show_default=True, type=click.STRING,
              help='ok_freq_info_fle.')
@click.option('--f_ng_freq_info', default=cf.AnalDataInfo.f_ng_freq_info_default, show_default=True, type=click.STRING,
              help='ng_freq_info_fle.')
@click.option('--f_eval_info', default=cf.AnalDataInfo.f_eval_info_default, show_default=True, type=click.STRING,
              help='eval_info_fle.')
@click.option('--f_title2pid_ext', default=cf.DataInfo.f_title2pid_ext_default, show_default=True, type=click.STRING,
              help='from_title_to_pageid_extended_information. Filter out disambiguation, management, '
                   'or format-error pages, and add eneid, incoming link num info.')
@click.option('--f_enew_info', default=cf.DataInfo.f_enew_info_default, show_default=True, type=click.STRING,
              help='f_enew_info')
@click.option('--f_target_attr_info', default=cf.DataInfo.f_target_attr_info_default, show_default=True,
              type=click.STRING, help='f_target_attr_info')
@click.option('--f_all_cat_info', default=cf.DataInfo.f_all_cat_info_default, show_default=True, type=click.STRING,
              help='f_all_cat_info')
def ljc_anal_main(gold_dir,
                  anal_dir_version,
                  sys_dir_common,
                  sys_dir_version,
                  data_dir_common,
                  f_target,
                  f_diff_judge,
                  f_ok_freq_info,
                  f_ng_freq_info,
                  f_eval_info,
                  f_title2pid_ext,
                  f_enew_info,
                  f_target_attr_info,
                  f_all_cat_info):
    class AnalDataInfo(object):
        f_target_default = 'eval_target.txt'
        f_diff_judge_default = 'diff_judge.tsv'
        f_ok_freq_info_default = 'diff_judge_ok_freq.tsv'
        f_ng_freq_info_default = 'diff_judge_ng_freq.tsv'
        f_eval_info_default = 'diff_judge_eval.tsv'
        f_title2pid_ext_default = 'jawiki-20210823_title2pageid_20210820_ext.tsv'
        f_enew_info_default = 'shinra2022_Categorization_train_20220616_mod.tsv'
        f_target_attr_info_default = 'ene_definition_v9.0.0-20220714_target_attr.tsv'
        f_all_cat_info_default = 'ene_definition_v9.0.0-20220714_all_cat.tsv'

        def __init__(self,
                     a_gold_dir,
                     a_anal_dir_version,
                     a_sys_dir_common,
                     a_sys_dir_version,
                     a_data_dir_common,
                     a_f_target=f_target_default,
                     a_f_diff_judge=f_diff_judge_default,
                     a_f_ok_freq_info=f_ok_freq_info_default,
                     a_f_ng_freq_info=f_ng_freq_info_default,
                     a_f_eval_info=f_eval_info_default,
                     a_f_title2pid_ext=f_title2pid_ext_default,
                     a_f_enew_info=f_enew_info_default,
                     a_f_target_attr_info=f_target_attr_info_default,
                     a_f_all_cat_info=f_all_cat_info_default):
            self.gold_dir = a_gold_dir
            self.anal_dir_version = a_anal_dir_version
            self.sys_dir_common = a_sys_dir_common
            self.sys_dir_version = a_sys_dir_version
            self.data_dir_common = a_data_dir_common
            self.target_file = a_f_target
            self.diff_judge_file = a_f_diff_judge
            self.ok_freq_info_file = a_f_ok_freq_info
            self.ng_freq_info_file = a_f_ng_freq_info
            self.eval_info_file = a_f_eval_info
            self.title2pid_ext_file = a_f_title2pid_ext
            self.enew_info_file = a_f_enew_info
            self.target_attr_info_file = a_f_target_attr_info
            self.all_cat_info_file = a_f_all_cat_info

    csv.field_size_limit(1000000000)
    log_info = cf.LogInfo()
    logger = set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)

    anal_data_info = AnalDataInfo(gold_dir, anal_dir_version, sys_dir_common, sys_dir_version, data_dir_common)

    anal_data_info.target_file = sys_dir_version + f_target
    anal_data_info.diff_judge_file = anal_dir_version + f_diff_judge
    anal_data_info.ok_freq_info_file = anal_dir_version + f_ok_freq_info
    anal_data_info.ng_freq_info_file = anal_dir_version + f_ng_freq_info
    anal_data_info.eval_info_file = anal_dir_version + f_eval_info
    anal_data_info.title2pid_ext_file = data_dir_common + f_title2pid_ext
    anal_data_info.enew_info_file = data_dir_common + f_enew_info
    anal_data_info.target_attr_info_file = data_dir_common + f_target_attr_info
    anal_data_info.all_cat_info_file = data_dir_common + f_all_cat_info

    sys_list = []
    # system outputs
    with open(anal_data_info.target_file, mode='r', encoding='utf-8') as t:
        linelist = t.readlines()
        for line in linelist:
            sys_name = line.replace('\n', '')
            sys_list.append(sys_name)
    d_eneid2enlabel = lc.reg_all_cat_info(anal_data_info.all_cat_info_file, log_info)

    check_title = {}
    all_reg = {}
    cnt_gold_tsv = 0
    ext_tsv = '*.tsv'
    ext_json = '*.jsonl'
    gold_json = anal_data_info.gold_dir + ext_json
    gold_tsv = anal_data_info.gold_dir + ext_tsv

    check_cat = {}
    with open(anal_data_info.all_cat_info_file, mode='r', encoding='utf-8') as ac:
        ac_reader = csv.reader(ac, delimiter='\t')
        for line in ac_reader:
            en_label = line[2]
            check_cat[en_label] = 1

    for g_json in glob(gold_json):
        if os.path.isfile(g_json):
            if not os.path.isfile(g_json):
                print('not found gold_json', g_json)
                sys.exit()
            if 'for_view' in g_json:
                continue

        else:
            print('not found json', g_json)
            continue

        if '_dist.json' in g_json:
            g_tsv = g_json.replace('_dist.jsonl', '.tsv')
        else:
            g_tsv = g_json.replace('.jsonl', '.tsv')

        if not os.path.isfile(g_tsv):
            lc.gen_linked_tsv(anal_data_info.gold_dir, anal_data_info.title2pid_ext_file, log_info, **d_eneid2enlabel)

        else:
            with open(g_tsv, 'r', encoding='utf-8') as j:
                reader = csv.reader(j, delimiter='\t')
                ans = ''
                for gold_out in reader:
                    cnt_gold_tsv += 1
                    gold_out_cp = gold_out.copy()

                    del gold_out_cp[9:]
                    gold_out_common_str = '\t'.join(gold_out_cp)

                    # null
                    if len(gold_out[9]) == 0:
                        ans = 'null'
                    else:
                        ans = gold_out[9]
                        check_title[gold_out[9]] = gold_out[10]

                    if gold_out_common_str not in all_reg:
                        all_reg[gold_out_common_str] = {}
                        all_reg[gold_out_common_str]['ok'] = {}

                    if ans not in all_reg[gold_out_common_str]['ok']:
                        all_reg[gold_out_common_str]['ok'][ans] = set()
                    all_reg[gold_out_common_str]['ok'][ans].add('gold')

    sys_cnt = 0
    for s_name in sys_list:
        sys_cnt += 1

        for cat in check_cat:
            s_fname = sys_dir_version + s_name + '/' + cat + '.tsv'

            if os.path.isfile(s_fname):
                with open(s_fname, 'r', encoding='utf-8') as j:
                    reader = csv.reader(j, delimiter='\t')

                    for sys_out in reader:
                        sys_out_cp = sys_out.copy()

                        del sys_out_cp[9:]

                        sys_out_common_str = '\t'.join(sys_out_cp)

                        if len(sys_out[9]) == 0:
                            sys_ans = 'null'
                        else:
                            sys_ans = sys_out[9]
                            check_title[sys_out[9]] = sys_out[10]

                        if sys_out_common_str not in all_reg:
                            print('illegal_sys_out_common_str', sys_out_common_str)
                            sys.exit()
                        if sys_ans in all_reg[sys_out_common_str]['ok']:
                            all_reg[sys_out_common_str]['ok'][sys_ans].add(s_name)
                        else:
                            if 'ng' not in all_reg[sys_out_common_str]:
                                all_reg[sys_out_common_str]['ng'] = {}
                            if sys_ans not in all_reg[sys_out_common_str]['ng']:
                                all_reg[sys_out_common_str]['ng'][sys_ans] = set()
                            all_reg[sys_out_common_str]['ng'][sys_ans].add(s_name)

    check_ene_label = {}
    with open(anal_data_info.all_cat_info_file, 'r', encoding='utf-8') as ac:
        ac_reader = csv.reader(ac, delimiter='\t')
        for ac_line in ac_reader:
            id = ac_line[0]
            label = ac_line[1]
            if id not in check_ene_label:
                check_ene_label[id] = label

    check_enew = {}
    with open(anal_data_info.enew_info_file, 'r', encoding='utf-8') as ew:
        ew_reader = csv.reader(ew, delimiter='\t')
        for ew_line in ew_reader:
            pid = ew_line[0]
            ene_id = ew_line[1]
            if pid in check_title:
                check_enew[pid] = ene_id + ':' + check_ene_label[ene_id]
    ok_sys_cnt = {}
    ng_sys_cnt = {}
    with open(anal_data_info.diff_judge_file, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='\t', lineterminator='\n')

        for common_str, j_dic in all_reg.items():
            for judge in j_dic:

                prt_list = []
                ok_sysname_list = []

                ok_ans_set = set()
                ok_sys_list = []
                ok_sys_set = set()
                ok_enew_set = set()
                ng_ans_set = set()
                ng_sys_list = []
                ng_sys_set = set()
                ng_enew_set = set()
                ok_sys_num = 0
                ng_sys_num = 0

                if judge == 'ok':
                    for ot_sys_ans, ot_sys_set in j_dic['ok'].items():
                        ot_sys_ans_cat = ''
                        if ot_sys_ans == 'null':
                            ot_sys_ans_title = ot_sys_ans
                        else:
                            if ot_sys_ans in check_title:
                                ot_sys_ans_title = ot_sys_ans + '(' + check_title[ot_sys_ans] + ')'
                            if ot_sys_ans in check_enew:
                                ot_sys_ans_cat = ot_sys_ans + '(' + check_enew[ot_sys_ans] + ')'
                        ok_ans_set.add(ot_sys_ans_title)
                        ok_enew_set.add(ot_sys_ans_cat)
                        ok_sys_set.update(ot_sys_set)
                        ok_sys_list.append([ot_sys_ans, ot_sys_set])
                        ok_sys_num += len(ot_sys_set)

                        for tmp_sys_name in ot_sys_set:
                            if tmp_sys_name not in ok_sys_cnt:
                                ok_sys_cnt[tmp_sys_name] = 0
                            ok_sys_cnt[tmp_sys_name] += 1
                    prt_list = [common_str, 'ok', ok_sys_num, ok_ans_set, ok_enew_set, ok_sys_set, ok_sys_list]
                else:

                    for on_sys_ans, on_sys_set in j_dic['ng'].items():
                        on_sys_ans_cat = ''
                        if on_sys_ans == 'null':
                            on_sys_ans_title = on_sys_ans
                        else:
                            if on_sys_ans in check_title:
                                on_sys_ans_title = on_sys_ans + check_title[on_sys_ans]
                            if on_sys_ans in check_enew:
                                on_sys_ans_cat = on_sys_ans + '(' + check_enew[on_sys_ans] + ')'
                        ng_ans_set.add(on_sys_ans_title)
                        ng_enew_set.add(on_sys_ans_cat)
                        ng_sys_set.update(on_sys_set)
                        ng_sys_list.append([on_sys_ans, on_sys_set])
                        ng_sys_num += len(on_sys_set)
                        for temp_sys_name in on_sys_set:
                            if temp_sys_name not in ng_sys_cnt:
                                ng_sys_cnt[temp_sys_name] = 0
                            ng_sys_cnt[temp_sys_name] += 1
                    prt_list = [common_str, 'ng', ng_sys_num, ng_ans_set, ng_enew_set, ng_sys_set, ng_sys_list]

                writer.writerow(prt_list)

    lc.dict2tsv(anal_data_info.ok_freq_info_file, **ok_sys_cnt)
    lc.dict2tsv(anal_data_info.ng_freq_info_file, **ng_sys_cnt)

    plist = []
    header = ['sys', 'prec', 'recall', 'f1']
    plist.append(header)

    for tmp_sys in sys_list:
        ok = 0
        ng = 0
        prec = 0.0
        recall = 0.0
        f1 = 0.0
        if tmp_sys in ok_sys_cnt:
            ok = ok_sys_cnt[tmp_sys]
        if tmp_sys in ng_sys_cnt:
            ng = ng_sys_cnt[tmp_sys]
        try:
            prec = ok/(ok+ng)
        except ZeroDivisionError:
            pass
        try:
            recall = ok/cnt_gold_tsv
        except ZeroDivisionError:
            pass
        try:
            f1 = (2 * prec * recall) / (prec + recall)
        except ZeroDivisionError:
            pass
        plist.append([tmp_sys, prec, recall, f1])

    lc.list2tsv(anal_data_info.eval_info_file, plist)


if __name__ == '__main__':
    ljc_anal_main()

