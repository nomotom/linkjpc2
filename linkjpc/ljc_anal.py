import csv
import os
import sys
from glob import glob
# import linkjpc as ljc
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
            # sys_info_list.append([sys_name, sys_path])
            sys_list.append(sys_name)

    # d_target_eneid2enlabel = {}
    # d_target_eneid2enlabel = reg_target_attr_info(target_attr_info)
    d_eneid2enlabel = lc.reg_all_cat_info(anal_data_info.all_cat_info_file, log_info)

    check_title = {}
    # gold_reg = {}
    all_reg = {}
    cnt_gold_tsv = 0
    ext_tsv = '*.tsv'
    ext_json = '*.jsonl'
    gold_json = anal_data_info.gold_dir + ext_json
    # sys_json = anal_data_info.sys_dir_common + sys_dir_var
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
                # print('gen_tsv')
                print('not found gold_json', g_json)
                sys.exit()
            # linkedjson2tsv_add_linked_title(gold_dir, title2pid_ext)
            if 'for_view' in g_json:
                continue

        else:
            print('not found json', g_json)
            continue

        if '_dist.json' in g_json:
            g_tsv = g_json.replace('_dist.jsonl', '.tsv')
        else:
            g_tsv = g_json.replace('.jsonl', '.tsv')

        # g_fname = gold_dir + cat + ext_tsv

        if not os.path.isfile(g_tsv):
            lc.gen_linked_tsv(anal_data_info.gold_dir, anal_data_info.title2pid_ext_file, log_info, **d_eneid2enlabel)

        else:
            # common_keyでsystem を登録
            with open(g_tsv, 'r', encoding='utf-8') as j:
                reader = csv.reader(j, delimiter='\t')
                # Person	1008136	ジェイ・デメリット	国籍	アメリカ合衆国	45	10	45	17	10664	アメリカ合衆国
                ans = ''
                for gold_out in reader:
                    cnt_gold_tsv += 1
                    # sys = gold_out[0]
                    # print('sys', sys)
                    gold_out_cp = gold_out.copy()

                    logger.debug({
                        'action': 'ljc_anal.py',
                        'gold_out_cp(before)': gold_out_cp
                    })

                    del gold_out_cp[9:]
                    # Person	1008136	ジェイ・デメリット	国籍	アメリカ合衆国	45	10	45	17	アメリカ合衆国

                    # del gold_out_cp[9]
                    # Person	1008136	ジェイ・デメリット	国籍	アメリカ合衆国	45	10	45	17

                    gold_out_common_str = '\t'.join(gold_out_cp)
                    # gold_out_common_str = gold_out_common_str.rstrip('\n')

                    # null
                    if len(gold_out[9]) == 0:
                        ans = 'null'
                    else:
                        ans = gold_out[9]
                        check_title[gold_out[9]] = gold_out[10]

                    # gold_reg[gold_out_common_str] = ans

                    if gold_out_common_str not in all_reg:
                        all_reg[gold_out_common_str] = {}
                        all_reg[gold_out_common_str]['ok'] = {}

                    if ans not in all_reg[gold_out_common_str]['ok']:
                        all_reg[gold_out_common_str]['ok'][ans] = set()
                    all_reg[gold_out_common_str]['ok'][ans].add('gold')
    logger.debug({
        'action': 'ljc_anal.py',
        'sys_list': 'sys_list'
    })
    sys_cnt = 0
    for s_name in sys_list:
        sys_cnt += 1

        # sys_dir = sys_dir_common + s_name + '/' + cat + ext_tsv
        # sys_dir = sys_dir_common + s_name + '/' + s_json
        # sys_json =sys_dir_version + s_name + '/' + ext_json

        # s_json = sys_dir + sys_json
        # for cat in cat_list:

        for cat in check_cat:
            s_fname = sys_dir_version + s_name + '/' + cat + '.tsv'
            logger.debug({
                'action': 'ljc_anal.py',
                's_fname': s_fname,
                'cat': cat
            })
            # o_fname = sys_dir_version_path + sys_dir + '/' + cat + ext_out
            if os.path.isfile(s_fname):
                with open(s_fname, 'r', encoding='utf-8') as j:
                    reader = csv.reader(j, delimiter='\t')

                    for sys_out in reader:
                        sys_out_cp = sys_out.copy()
                        logger.debug({
                            'action': 'ljc_anal.py',
                            'sys_out': sys_out,
                            'len(sys_out[9])': len(sys_out[9]),
                            'sys_out_cp(before)': sys_out_cp,
                        })
                        del sys_out_cp[9:]
                        # del sys_out_cp[9]
                        logger.debug({
                            'action': 'ljc_anal.py',
                            'sys_out_cp(after)': sys_out_cp,
                        })
                        sys_out_common_str = '\t'.join(sys_out_cp)
                        # sys_out_common_str = sys_out_common_str.rstrip('\n')
                        logger.debug({
                            'action': 'ljc_anal.py',
                            'sys_out_common_str(before)': sys_out_common_str,
                        })
                        if len(sys_out[9]) == 0:
                            sys_ans = 'null'
                        else:
                            sys_ans = sys_out[9]
                            check_title[sys_out[9]] = sys_out[10]
                        logger.debug({
                            'action': 'ljc_anal.py',
                            'sys_out_common_str': sys_out_common_str,
                            'sys_ans': sys_ans,
                            'len(sys_ans)': len(sys_ans)
                        })
                        # print('new_row_str', new_row_str)
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
            else:
                logger.warning({
                    'action': 'ljc_anal.py',
                    'msg': 'not found s_fname',
                    's_fname': s_fname
                })

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
            # print(k, v)
            for judge in j_dic:

                # print('judge', judge)
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
                            logger.info({
                                'action': 'ljc_anal',
                                'ot_sys_ans(null)': ot_sys_ans,
                            })
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
                        # print('ans', ans)
                        # print('sys_num', sys_num)

                        for tmp_sys_name in ot_sys_set:
                            if tmp_sys_name not in ok_sys_cnt:
                                ok_sys_cnt[tmp_sys_name] = 0
                            ok_sys_cnt[tmp_sys_name] += 1
                        logger.debug({
                            'action': 'ljc_anal',
                            'judge': judge,
                            'sys_ans': sys_ans,
                            'ok_sys_num': ok_sys_num,
                            'ok_ans_set': ok_ans_set
                        })
                        #  'sys_ans': '1476287', 'ok_sys_num': 210, 'ok_ans_set': {'1476287(カッコネン)'}}
                        # sys_ans': 'null', 'ok_sys_num': 208, 'ok_ans_set': {'null'}}
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
                        # print('ans', ans)
                        # print('sys_num', sys_num)
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

# with open(ng_freq_info_file, mode='r', encoding='utf-8') as nf:
#     writer = csv.writer(nf, delimiter='\t', lineterminator='\n')
#     for k, v in ng_sys_cnt.items():
#         writer.writerow([k,v])

# # 個別の辞書を出力
# t_cnt = 0
# for out_head in out_list:
#     t_cnt += 1
#     t_idx = t_cnt -1
#
#     for cat in cat_list:
#         out_file = out_head + cat + ext_tsv
#         # print(out_file)
#         with open(out_file, 'w', encoding='utf-8') as f:
#             writer = csv.writer(f)
#             for k, v in dict_list[t_idx].items():
#                 print(k, v)
#                 writer.writerow([k, v])

# for k, sys_name in sys_all_reg:
#     if len(sys_all_reg[k]) > 1:
#         dupli_list.append()
#         if not dupli_dict.get(k):
#             dupli_dict[k] = []
#         dupli_dict[k].append(v)

# def reg_all_cat_info(all_cat_info, log_info):
#     """
#     register eneid and en_label to dictionary
#     :param all_cat_info:
#     :param log_info:
#     :return: ene_dict
#     :notice:
#     all_cat_info
#         format: eneid, enlabel_ja, enlabel_en
#         sample: 1.4.4.1 国籍名  Nationality
#     """
#     import csv
#     logger = set_logging(log_info, 'myLogger')
#     logger.setLevel(logging.INFO)
#
#     with open(all_cat_info, mode='r', encoding='utf-8') as ta:
#         ta_reader = csv.reader(ta, delimiter='\t')
#
#         ene_dict = {}
#         for ta_line in ta_reader:
#             en_label = ta_line[2]
#             eid = ta_line[0]
#             ene_dict[eid] = en_label
#             logging.info({
#                 'action': 'reg_all_cat_info',
#                 'eid': eid,
#                 'en_label': en_label
#             })
#         return ene_dict
#
# def get_key_list_with_title_plus_eneid(**tr):
#     """get key list from input json dictionary to distinguish each record
#        The dictionary should include title of the page as key
#     args:
#         **tr
#     return:
#         tmp_list
#             format: [pageid, title, attribute, text, start_line_id, start_offset, end_line_id, end_offset, link_id]
#     """
#
#     import sys
#     # import logging
#     # logger = set_logging_pre(log_info, 'myPreLogger')
#     # logger.setLevel(logging.INFO)
#
#     try:
#         eneid = tr['ene']
#     except (KeyError, ValueError) as ex:
#         # logger.error({
#         #     'action': 'get_key_list_with_title',
#         #     'error': ex,
#         #     'tr': tr
#         # })
#         sys.exit()
#
#     try:
#         page_id = tr['page_id']
#     except (KeyError, ValueError) as ex:
#         # logger.error({
#         #     'action': 'get_key_list_with_title',
#         #     'error': ex,
#         #     'tr': tr
#         # })
#         sys.exit()
#     try:
#         title = tr['title']
#     except (KeyError, ValueError) as ex:
#         # logger.error({
#         #     'action': 'get_key_list_with_title',
#         #     'error': ex,
#         #     'tr': tr
#         # })
#         sys.exit()
#     try:
#         at = tr['attribute']
#     except (KeyError, ValueError) as ex:
#         # logger.error({
#         #     'action': 'get_key_list_with_title',
#         #     'error': ex,
#         #     'tr': tr
#         # })
#         sys.exit()
#
#     if 'text_offset' not in tr:
#         # logger.error({
#         #     'action': 'get_key_list_with_title',
#         #     'error': 'format_error: text_offset',
#         #     'tr': tr
#         # })
#         sys.exit()
#     else:
#         if 'start' not in tr['text_offset']:
#             # logger.error({
#             #     'action': 'get_key_list_with_title',
#             #     'error': 'format_error: start(text_offset)',
#             #     'tr': tr
#             # })
#             sys.exit()
#         else:
#             if 'line_id' not in tr['text_offset']['start']:
#                 # logger.error({
#                 #     'action': 'get_key_list_with_title',
#                 #     'error': 'format_error: line_id(start)',
#                 #     'tr': tr
#                 # })
#                 sys.exit()
#             else:
#                 start_line_id = str(tr['text_offset']['start']['line_id'])
#
#             if 'offset' not in tr['text_offset']['start']:
#                 # logger.error({
#                 #     'action': 'get_key_list_with_title',
#                 #     'error': 'format_error: offset(start)',
#                 #     'tr': tr
#                 # })
#                 sys.exit()
#             else:
#                 start_offset = str(tr['text_offset']['start']['offset'])
#
#         if 'end' not in tr['text_offset']:
#             # logger.error({
#             #     'action': 'get_key_list_with_title',
#             #     'error': 'format_error: end(text_offset)',
#             #     'tr': tr
#             # })
#             sys.exit()
#         else:
#             if 'line_id' not in tr['text_offset']['end']:
#                 # logger.error({
#                 #     'action': 'get_key_list_with_title',
#                 #     'error': 'format_error: line_id(end)',
#                 #     'tr': tr
#                 # })
#                 sys.exit()
#             else:
#                 end_line_id = str(tr['text_offset']['end']['line_id'])
#
#             if 'offset' not in tr['text_offset']['end']:
#                 # logger.error({
#                 #     'action': 'get_key_list_with_title',
#                 #     'error': 'format_error: offset(end)',
#                 #     'tr': tr
#                 # })
#                 sys.exit()
#             else:
#                 end_offset = str(tr['text_offset']['end']['offset'])
#
#             if 'text' not in tr['text_offset']:
#                 # logger.error({
#                 #     'action': 'get_key_list_with_title',
#                 #     'error': 'format_error: text(text_offset)',
#                 #     'tr': tr
#                 # })
#                 sys.exit()
#             else:
#                 text = tr['text_offset']['text']
#
#     if 'link_page_id' not in tr:
#         link_id = None
#     else:
#         link_id = tr['link_page_id']
#     #
#     # logger.debug({
#     #     'action': 'get_key_list_with_title',
#     #     'pid': pid,
#     #     'title': title,
#     #     'at': at,
#     #     'text': text,
#     #     'start_line_id': start_line_id,
#     #     'start_offset': start_offset,
#     #     'end_line_id': end_line_id,
#     #     'end_offset': end_offset,
#     #     'link_id': link_id
#     # })
#     tmp_list = [eneid, page_id, title, at, text, start_line_id, start_offset, end_line_id, end_offset, link_id]
#     return tmp_list
#
#
# def linkedjson2tsv_add_linked_title_ene(linked_json_dir, title2pid_ext_file, **d_eid2label):
#     """Convert linked json file (with title) to linked tsv file
#        add title of linked page and ene using title2pid_ext_file
#
#     args:
#         linked_json_dir
#         title2pid_ext_file
#         target_attr_info_file
#         **d_eid2label
#         log_info
#     output:
#         linked_tsv (tsv)
#             format
#                 cat, pageid, title, attribute, text, start_line_id, start_offset, end_line_id, end_offset,
#                 link_pageid,
#                 link_page_title, ene
#             sample
#                 Person 2392906	桐谷華	地位職業	声優	38	20	38	22	1192	声優
#     notice
#         '\n' in text(mention) has been converted to '\\n'.
#         f_title2pid_ext
#             format
#                 (title(from page))\t(pageid(to page))\t(title(to page)\t(maximum number of incoming links(to page))
#                 \t(eneid(to_page))
#             sample
#                 アメリカ合衆国  1698838 アメリカ合衆国  116818  1.5.1.3
#                 ユナイテッドステイツ    1698838 アメリカ合衆国  116818  1.5.1.3
#     """
#
#     import json
#     import pandas as pd
#     # from glob import glob
#
#     # import logging
#     # # logger = set_logging_pre(log_info, 'myPreLogger')
#     # # logger.setLevel(logging.INFO)
#     #
#     # logger.info({
#     #     'action': 'linkedjson2tsv_add_linked_title_ene',
#     #     'linked_json_dir': linked_json_dir,
#     #     # 'title2pid_org_file': title2pid_org_file,
#     # })
#     get_title = {}
#     get_ene = {}
#
#     with open(title2pid_ext_file, mode='r', encoding='utf-8') as tf:
#         tf_reader = csv.reader(tf, delimiter='\t')
#         for rows in tf_reader:
#             to_title = rows[2]
#             to_pid_str = rows[1]
#             # 20220921
#             to_ene = rows[4]
#
#             get_title[to_pid_str] = to_title
#             get_ene[to_pid_str] = to_ene
#             # # 20220916
#             # get_pid[to_title] = to_pid_str
#     # linked_json_files = linked_json_dir + '*.json'
#     linked_json_files = linked_json_dir + '*.jsonl'
#
#     for linked_json in glob(linked_json_files):
#         if 'for_view' in linked_json:
#             continue
#         go_list = []
#         # linked_tsv = linked_json.replace('.json', '.tsv')
#         if '_dist.jsonl' in linked_json:
#             linked_tsv = linked_json.replace('_dist.jsonl', '.tsv')
#         else:
#             linked_tsv = linked_json.replace('.jsonl', '.tsv')
#         # 20220825
#         # 20220929
#         # cat_pre = linked_tsv.replace(linked_json_dir, '')
#         # cat = cat_pre.replace('.tsv', '')
#
#         with open(linked_json, mode='r', encoding='utf-8') as g, open(linked_tsv, 'w', encoding='utf-8') as o:
#             for g_line in g:
#                 g_key_list = []
#                 d_gline = json.loads(g_line)
#                 g_key_list = get_key_list_with_title_plus_eneid(**d_gline)
#                 # g_key_list = [eneid, pid, title, at, text, start_line_id, start_offset, end_line_id, end_offset,
#                 # link_id]
#
#                 e_label = ''
#                 if g_key_list[0] in d_eneid2enlabel:
#                     g_cat = d_eneid2enlabel[g_key_list[0]]
#
#                     g_key_list[0] = g_cat
#                 # else:
#                 #     logger.debug({
#                 #         'action': 'linkedjson2tsv_add_linked_title_ene',
#                 #         'msg': 'illegal ene',
#                 #         'g_key_list': g_key_list
#                 #     })
#
#                 # in case of multiple lines
#                 # text_pre = g_key_list[4]
#                 text_pre = g_key_list[4]
#
#                 # 20220826
#                 # g_key_list[4] = '\\n'.join(text_pre.splitlines())
#                 g_key_list[3] = '\\n'.join(text_pre.splitlines())
#
#                 # g_key_list[4] = '\n'.join(text_pre.splitlines())
#                 # till here
#                 # if 'つまり' in g_key_list[3] or '要するに' in g_key_list[3] or 'たとえば' in g_key_list[3]:
#                 #     print('key_list_3', g_key_list[3])
#
#                 # 20220826
#                 g_link_pageid = g_key_list[9]
#                 g_link_title = ''
#                 g_link_ene = ''
#                 if get_title.get(g_link_pageid):
#                     g_link_title = get_title[g_link_pageid]
#                 g_key_list.insert(10, g_link_title)
#                 # 20220921
#                 if get_ene.get(g_link_pageid):
#                     g_link_ene = get_ene[g_link_pageid]
#                 g_key_list.insert(11, g_link_ene)
#
#                 # 20220825
#                 # g_key_list.insert(0, cat)
#
#                 # logger.debug({
#                 #     'action': 'linkedjson2tsv_add_linked_title_ene',
#                 #     'g_key_list': g_key_list,
#                 # })
#                 go_list.append(g_key_list)
#
#             df_go = pd.DataFrame(go_list)
#             df_go.to_csv(o, sep='\t', header=False, index=False)

#
# def linkedjson2tsv_add_linked_title(linked_json_dir, title2pid_ext_file):
#     """Convert linked json file (with title) to linked tsv file
#        add title of linked page using title2pid_ext_file
#     args:
#         linked_json_dir
#         title2pid_ext_file
#     output:
#         linked_tsv (tsv)
#             format
#                 cat, pageid, title, attribute, text, start_line_id, start_offset,
#                 end_line_id, end_offset, link_pageid,
#                 link_page_title
#             sample
#                 Person 2392906	桐谷華	地位職業	声優	38	20	38	22	1192	声優
#                 Person	125414	窪田まり子	誕生地	日本東京都福生市	42	15	42	23	63930	福生市
#     notice
#         '\n' in text(mention) has been converted to '\\n'.
#     """
#
#     import json
#     import pandas as pd
#     from glob import glob
#
#     # import logging
#     # import re
#     # logger = set_logging_pre(log_info, 'myPreLogger')
#     # logger.setLevel(logging.INFO)
#
#     # logger.info({
#     #     'action': 'linkedjson2tsv_add_linked_title',
#     #     'linked_json_dir': linked_json_dir,
#     #     # 'title2pid_org_file': title2pid_org_file,
#     # })
#     get_title = {}
#
#     with open(title2pid_ext_file, mode='r', encoding='utf-8') as tf:
#         tf_reader = csv.reader(tf, delimiter='\t')
#         for rows in tf_reader:
#             to_title = rows[2]
#             to_pid_str = rows[1]
#             get_title[to_pid_str] = to_title
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
#         tf_cat = cat_pre.replace('.tsv', '')
#
#         with open(linked_json, mode='r', encoding='utf-8') as g, open(linked_tsv, 'w', encoding='utf-8') as o:
#             for g_line in g:
#                 g_key_list = []
#                 d_gline = json.loads(g_line)
#                 g_key_list = get_key_list_with_title(**d_gline)
#                 # g_key_list = [pid, title, at, text, start_line_id, start_offset, end_line_id, end_offset, link_id]
#
#                 # logger.debug({
#                 #     'action': 'linkedjson2tsv_add_linked_title',
#                 #     'g_key_list': g_key_list,
#                 # })
#
#                 g_link_pageid = g_key_list[8]
#
#                 # in case of multiple lines
#                 # text_pre = g_key_list[4]
#                 text_pre = g_key_list[3]
#
#                 # 20220826
#                 # g_key_list[4] = '\\n'.join(text_pre.splitlines())
#                 g_key_list[3] = '\\n'.join(text_pre.splitlines())
#
#                 # g_key_list[4] = '\n'.join(text_pre.splitlines())
#                 # till here
#                 # if 'つまり' in g_key_list[3] or '要するに' in g_key_list[3] or 'たとえば' in g_key_list[3]:
#                 #     print('key_list_3', g_key_list[3])
#
#                 # 20220826
#                 g_link_pageid = g_key_list[8]
#                 g_link_title = ''
#                 if get_title.get(g_link_pageid):
#                     g_link_title = [g_link_pageid]
#                 g_key_list.insert(9, g_link_title)
#                 # 20220825
#                 g_key_list.insert(0, cat)
#
#                 # g_title_pageid = g_key_list[0]
#                 # if .get(g_title_pageid):
#                 #      g_org_title = get_title[g_title_pageid]
#                 #      g_key_list.insert(1, g_org_title)
#                 # logger.debug({
#                 #     'action': 'linkedjson2tsv_add_linked_title',
#                 #     'text_pre': text_pre,
#                 #     'cat': cat,
#                 #     'g_link_pageid': g_link_pageid,
#                 #     # 'g_link_title': g_link_title,
#                 #     # 'g_org_title': g_org_title,
#                 # })
#                 # logger.debug({
#                 #     'action': 'linkedjson2tsv_add_linked_title',
#                 #     'g_key_list': g_key_list,
#                 # })
#                 #  'g_key_list': ['Style', '2847831', '為我流', '活動地域', '茨城県', '56', '0', '56', '3', '774349', '茨城県']}
#                 # 'g_key_list': ['Style', '2847831', '為我流', '統括組織', '為我流和術保存会', '56', '6', '56', '14', None, '']}
#                 go_list.append(g_key_list)
#                 # g_key_list = [cat, pid, title, at, text, start_line_id,
#                 start_offset, end_line_id, end_offset, link_id]
#
#             df_go = pd.DataFrame(go_list)
#             df_go.to_csv(o, sep='\t', header=False, index=False)
#

# log_info = LogInfo()
# logger = set_logging(log_info, 'myAnalLogger')
# logger.setLevel(logging.INFO)

    # cat_list = [
    # 'Person',
    # 'God',
    # 'Individual_Animal_Other',
    # 'Racehorse',
    # 'Individual_Flora',
    # 'Organization_Other',
    # 'International_Organization',
    # 'Show_Organization',
    # 'Family',
    # 'Ethnic_Group_Other',
    # 'Nationality',
    # 'Sports_Federation',
    # 'Sports_League',
    # 'Sports_Team',
    # 'Nonprofit_Organization',
    # 'Company',
    # 'Company_Group',
    # 'Political_Organization_Other',
    # 'Government',
    # 'Political_Party',
    # 'Cabinet',
    # 'Military',
    # 'Location_Other',
    # 'GPE_Other',
    # 'City',
    # 'Province',
    # 'Country',
    # 'Continental_Region',
    # 'Domestic_Region',
    # 'Geological_Region_Other',
    # 'Spa',
    # 'Mountain',
    # 'Island',
    # 'River',
    # 'Lake',
    # 'Sea',
    # 'Bay',
    # 'Astronomical_Object_Other',
    # 'Astronomical_Object_Part',
    # 'Galaxy',
    # 'Star',
    # 'Planet_Satellite',
    # 'Constellation',
    # 'Facility_Other',
    # 'Facility_Part',
    # 'Dam',
    # 'Archaeological_Place_Other',
    # 'Cemetery',
    # 'FOE_Other',
    # 'Military_Base',
    # 'Castle',
    # 'Palace',
    # 'Public_Institution',
    # 'Accommodation',
    # 'Medical_Institution',
    # 'School',
    # 'Research_Institute',
    # 'Market',
    # 'Power_Plant',
    # 'Park',
    # 'Shopping_Complex',
    # 'Sports_Facility',
    # 'Museum',
    # 'Zoo',
    # 'Amusement_Park',
    # 'Theater',
    # 'Worship_Place',
    # 'Car_Stop',
    # 'Station',
    # 'Airport',
    # 'Port',
    # 'Road_Facility',
    # 'Railway_Facility',
    # 'Line_Other',
    # 'Road',
    # 'Railroad',
    # 'Water_Route',
    # 'Canal',
    # 'Tunnel',
    # 'Bridge',
    # 'Product_Other',
    # 'Service',
    # 'Brand',
    # 'Software',
    # 'Information_Appliance',
    # 'Toy',
    # 'Musical_Instrument',
    # 'Drug',
    # 'Character',
    # 'Art_Other',
    # 'Painting',
    # 'Broadcast_Program',
    # 'Movie',
    # 'Show',
    # 'Music',
    # 'Video_Work',
    # 'Printing_Other',
    # 'Newspaper',
    # 'Magazine',
    # 'Book',
    # 'Game_Other',
    # 'Digital_Game',
    # 'Food_Other',
    # 'Dish',
    # 'Weapon_Other',
    # 'Firearms',
    # 'Vehicle_Other',
    # 'Car',
    # 'Train',
    # 'Aircraft',
    # 'Ship',
    # 'Spaceship',
    # 'Military_Vehicle',
    # 'Military_Aircraft',
    # 'Military_Ship',
    # 'Doctrine_Method_Other',
    # 'Offense',
    # 'Award',
    # 'Decoration',
    # 'Money_Form',
    # 'Technology',
    # 'Standard',
    # 'System',
    # 'Examination',
    # 'Doctrine_Thought',
    # 'Culture',
    # 'Religion',
    # 'Academic',
    # 'Theory',
    # 'Style',
    # 'Sport',
    # 'Plan',
    # 'Rule_Other',
    # 'Treaty',
    # 'Law',
    # 'Position_Vocation',
    # 'Language_Other',
    # 'National_Language',
    # 'Currency',
    # 'Virtual_Address_Other',
    # 'Channel',
    # 'Event_Other',
    # 'Natural_Phenomenon',
    # 'Natural_Disaster_Other',
    # 'Earthquake',
    # 'Flood_Damage',
    # 'Occasion_Other',
    # 'Religious_Festival',
    # 'Election',
    # 'Competition',
    # 'Exhibition',
    # 'Conference',
    # 'Incident_Other',
    # 'Traffic_Accident',
    # 'Political_Incident',
    # 'War',
    # 'Natural_Object_Other',
    # 'Compound',
    # 'Mineral',
    # 'Living_Thing_Other',
    # 'Fictional_Species',
    # 'Bacteria_Virus',
    # 'Fungus',
    # 'Mollusk',
    # 'Arthropod',
    # 'Insect',
    # 'Fish',
    # 'Amphibia',
    # 'Dinosaur',
    # 'Reptile',
    # 'Bird',
    # 'Mammal',
    # 'Flora',
    # 'Living_Thing_Part_Other',
    # 'Animal_Part',
    # 'Flora_Part',
    # 'Animal_Disease',
    # 'Color'
    # ]
