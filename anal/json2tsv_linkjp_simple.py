# function
# - 入力と正解の識別用情報をtsvに変換
# - 正解にはlink先のタイトルをつける
# output
# - 入力ファイル(ene_annotation/*.json)をtsv化したファイル
# - 正解ファイルをtsv化したファイル
# 　- りんくタイプ含む(該当すれば文字列の1）
# 　- sample 360328	グアム国際空港	名称由来人物の地位職業名	アメリカ合衆国下院議員	115	56	115	67	7341	議員		1
#
# notice
# - text(mention)部分\nを含む場合エスケープ(\\n)
# - get_key_plus:     tmp_list = [pid, at, text, start_line_id, start_offset, end_line_id, end_offset, link_id]
# - get_key_full:     tmp_list = [pid, at, text, start_line_id, start_offset, end_line_id, end_offset, link_id,
# later_name, part_of, derivation_of]

import json
import pandas as pd
from glob import glob
import sys
# import csv
import re
import os
# import sample_test as sc
import logging
# from ..linkjpc import config as cf
# import linkjpc as ljc
# import evaluation_linkjp as el


class LogInfo(object):
    log_file_name_default = 'anal.log'
    logging_ini_default = './logging_anal.ini'

    def __init__(self,
                 logging_ini=logging_ini_default):
        self.logging_ini = logging_ini


def set_logging(log_info, logger_name):
    from os import path
    from logging import getLogger, config

    logging_ini = log_info.logging_ini
    log_file_path = path.join(path.dirname(path.abspath(__file__)), logging_ini)
    logging.config.fileConfig(log_file_path)

    logger = logging.getLogger(logger_name)
    return logger

# def get_key_full(log_info, **tr):
def get_key_full(**tr):

    # 準一致の情報も取得

    # print('(get_key_full)tr', tr )
    # print('(get_key_full)tr', tr )
    # import evaluation_linkjp as el
    import sys
    # import logging

    # logger = set_logging(log_info, 'myAnalLogger')
    # logger = el.set_logging(log_info, 'myAnalLogger')
    # logger.setLevel(logging.INFO)

    try:
        pid = tr['page_id']
    except (KeyError, ValueError) as ex:
        print("{}".format(ex), 'page_id', tr)
        sys.exit()

    try:
        at = tr['attribute']
    except (KeyError, ValueError) as ex:
        print("{}".format(ex), 'attribute', tr)
        sys.exit()

    if 'text_offset' not in tr:
        raise KeyError('(get_key_full)format_error: text_offset', tr)
        # sys.exit()
    else:
        if 'start' not in tr['text_offset']:
            raise KeyError('(get_key_full)format_error: start', tr)
        else:
            if 'line_id' not in tr['text_offset']['start']:
                raise KeyError('(get_key_full)format_error: line_id', tr)
            else:
                start_line_id = str(tr['text_offset']['start']['line_id'])

            if 'offset' not in tr['text_offset']['start']:
                raise KeyError('(get_key_full)format_error: offset', tr)
            else:
                start_offset = str(tr['text_offset']['start']['offset'])

        if 'end' not in tr['text_offset']:
            raise KeyError('(get_key_full)format_error: end', tr)
        else:
            if 'line_id' not in tr['text_offset']['end']:
                raise KeyError('(get_key_full)format_error: line_id', tr)
            else:
                end_line_id = str(tr['text_offset']['end']['line_id'])

            if 'offset' not in tr['text_offset']['end']:
                raise KeyError('(get_key_full)format_error: offset', tr)
            else:
                end_offset = str(tr['text_offset']['end']['offset'])

            if 'text' not in tr['text_offset']:
                raise KeyError('(get_key_full)format_error: text', tr)
            else:
                text = tr['text_offset']['text']
                # logger.debug({
                #     'action': 'get_key_full',
                #     'pid': pid,
                #     'text': text,
                #     'tr': tr
                # })
    link_id = ''
    later_name = ''
    part_of = ''
    derivation_of = ''
    if 'link_page_id' in tr:
        link_id = tr['link_page_id']

        if 'link_type' not in tr:
            # logger.error({
            #     'action': 'get_key_full',
            #     'error': '(get_key_full)format_error: link_type',
            #     'tr': tr
            # })
            raise KeyError('(get_key_full)format_error: link_type', tr)
            # sys.exit()
        else:
            # if 'later_name' not in tr['link_type']:
            #     # logger.error({
            #     #     'action': 'get_key_full',
            #     #     'error': '(get_key_full)format_error: later_name',
            #     #     'tr': tr
            #     # })
            #     # sys.exit()
            #     pass

            if tr['link_type'].get('later_name'):
                if tr['link_type']['later_name']:
                    later_name = '1'
            # if 'part_of' not in tr['link_type']:
            #     # logger.error({
            #     #     'action': 'get_key_full',
            #     #     'error': '(get_key_full)format_error: part_of',
            #     #     'tr': tr
            #     # })
            #     sys.exit()
            # else:
            if tr['link_type'].get('part_of'):
                if tr['link_type']['part_of']:
                    part_of = '1'
            # if 'derivation_of' not in tr:
            #     # logger.error({
            #     #     'action': 'get_key_full',
            #     #     'error': '(get_key_full)format_error: derivation_of',
            #     #     'tr': tr
            #     # })
            #     sys.exit()
            # else:
            if tr['link_type'].get('derivation_of'):
                if tr['link_type']['derivation_of']:
                    derivation_of = '1'
    tmp_list = [pid, at, text, start_line_id, start_offset, end_line_id, end_offset, link_id, later_name, part_of, derivation_of]

    tmp_str = '\t'.join(tmp_list)
    return tmp_str


# def get_key_plus(log_info, **tr):
def get_key_plus(**tr):

    # print('(get_key_plus)tr', tr )
    # print('(get_key_plus)tr', tr )
    #import evaluation_linkjp as el
    # import sys
    # import logging

    #logger = el.set_logging(log_info, 'myAnalLogger')
    # logger = set_logging(log_info, 'jLogger')
    # logger.setLevel(logging.INFO)

    try:
        pid = tr['page_id']
    except (KeyError, ValueError) as ex:
        print("{}".format(ex), 'page_id', tr)
        sys.exit()

    try:
        at = tr['attribute']
    except (KeyError, ValueError) as ex:
        print("{}".format(ex), 'attribute', tr)
        sys.exit()

    if 'text_offset' not in tr:
        raise KeyError('(get_key_plus)format_error: text_offset', tr)
        # sys.exit()
    else:
        if 'start' not in tr['text_offset']:
            raise KeyError('(get_key_plus)format_error: start', tr)
        else:
            if 'line_id' not in tr['text_offset']['start']:
                raise KeyError('(get_key_plus)format_error: line_id', tr)
            else:
                start_line_id = str(tr['text_offset']['start']['line_id'])

            if 'offset' not in tr['text_offset']['start']:
                raise KeyError('(get_key_plus)format_error: offset', tr)
            else:
                start_offset = str(tr['text_offset']['start']['offset'])

        if 'end' not in tr['text_offset']:
            raise KeyError('(get_key_plus)format_error: end', tr)
        else:
            if 'line_id' not in tr['text_offset']['end']:
                raise KeyError('(get_key_plus)format_error: line_id', tr)
            else:
                end_line_id = str(tr['text_offset']['end']['line_id'])

            if 'offset' not in tr['text_offset']['end']:
                raise KeyError('(get_key_plus)format_error: offset', tr)
            else:
                end_offset = str(tr['text_offset']['end']['offset'])

            if 'text' not in tr['text_offset']:
                raise KeyError('(get_key_plus)format_error: text', tr)
            else:
                text = tr['text_offset']['text']
                # logger.debug({
                #     'action': 'get_key_plus',
                #     'pid': pid,
                #     'text': text,
                #     'tr': tr
                # })

    if 'link_page_id' not in tr:
        link_id = ''
    else:
        link_id = tr['link_page_id']

    tmp_list = [pid, at, text, start_line_id, start_offset, end_line_id, end_offset, link_id]

    tmp_str = '\t'.join(tmp_list)
    return tmp_str


def get_key(**tr):
# def get_key(log_info, **tr):

    # print('(get_key)tr', tr )
    # print('(get_key)tr', tr )
    # import evaluation_linkjp as el
    import sys
    # import logging
    # logger = el.set_logging(log_info, 'myAnalLogger')
    # logger.setLevel(logging.INFO)

    try:
        pid = tr['page_id']
    except (KeyError, ValueError) as ex:
        # logger.error({
        #     'action': 'get_key',
        #     'error': ex,
        #     'tr': tr
        # })
        sys.exit()

    try:
        at = tr['attribute']
    except (KeyError, ValueError) as ex:
        # logger.error({
        #     'action': 'get_key',
        #     'error': ex,
        #     'tr': tr
        # })
        sys.exit()

    if 'text_offset' not in tr:
        # logger.error({
        #     'action': 'get_key',
        #     'error': 'format_error: text_offset',
        #     'tr': tr
        # })
        sys.exit()
    else:
        if 'start' not in tr['text_offset']:
            # logger.error({
            #     'action': 'get_key',
            #     'error': 'format_error: start(text_offset)',
            #     'tr': tr
            # })
            sys.exit()
        else:
            if 'line_id' not in tr['text_offset']['start']:
                # logger.error({
                #     'action': 'get_key',
                #     'error': 'format_error: line_id(start)',
                #     'tr': tr
                # })
                sys.exit()
            else:
                start_line_id = str(tr['text_offset']['start']['line_id'])

            if 'offset' not in tr['text_offset']['start']:
                # logger.error({
                #     'action': 'get_key',
                #     'error': 'format_error: offset(start)',
                #     'tr': tr
                # })
                sys.exit()
            else:
                start_offset = str(tr['text_offset']['start']['offset'])

        if 'end' not in tr['text_offset']:
            # logger.error({
            #     'action': 'get_key',
            #     'error': 'format_error: end(text_offset)',
            #     'tr': tr
            # })
            sys.exit()
        else:
            if 'line_id' not in tr['text_offset']['end']:
                # logger.error({
                #     'action': 'get_key',
                #     'error': 'format_error: line_id(end)',
                #     'tr': tr
                # })
                sys.exit()
            else:
                end_line_id = str(tr['text_offset']['end']['line_id'])

            if 'offset' not in tr['text_offset']['end']:
                # logger.error({
                #     'action': 'get_key',
                #     'error': 'format_error: offset(end)',
                #     'tr': tr
                # })
                sys.exit()
            else:
                end_offset = str(tr['text_offset']['end']['offset'])

            if 'text' not in tr['text_offset']:
                # logger.error({
                #     'action': 'get_key',
                #     'error': 'format_error: text(text_offset)',
                #     'tr': tr
                # })
                sys.exit()
            else:
                text = tr['text_offset']['text']

    tmp_list = [pid, at, text, start_line_id, start_offset, end_line_id, end_offset]

    tmp_str = '\t'.join(tmp_list)
    return tmp_str
# log_info = el.LogInfo()
# logger = el.set_logging(log_info, 'myAnalLogger')
# logger.setLevel(logging.INFO)
log_info = LogInfo()
logger = set_logging(log_info, 'myJLogger')
logger.setLevel(logging.INFO)

# pageIDとタイトルと転送
title_file = '/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/common/jawiki-20190120-title2pageid.json'

gold_dir = sys.argv[1]
# GOLDファイルのディレクトリ
# gold_dir = '/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/link_annotation/'
# print('(diff)gold_dir', gold_dir)

# ENEファイルのディレクトリ
in_dir = sys.argv[2]
# in_dir = '/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/ene_annotation/'

# ENEファイル
ene_files = in_dir + '*.json'

# 2021/12/23 再帰リンクの属性を除いた評価に対応
# attr_type: 'all'/'del_slink'
# attr_type = sys.argv[5]
# # 2021/12/23
# # サンプルデータで再帰リンク率0.5以上の属性
# del_attr_list = "/Users/masako/Documents/SHINRA/2021-LinkJP/anal/cat_att_selflink_equal_or_more_05.tsv"

# GOLDファイル
# gold_files = '/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/link_annotation/*.json'
gold_files = gold_dir + '*.json'

# check_del = {}
# if attr_type == 'del_slink':
#     with open(del_attr_list, 'r', encoding='utf-8') as dl:
#         reader = csv.reader(dl, delimiter='\t')
#         for row in reader:
#             tmp_cat = row[0]
#             tmp_attr = row[1]
#             # print(tmp_cat, tmp_attr)
#             if not check_del.get(tmp_cat):
#                 check_del[tmp_cat] = []
#             check_del[tmp_cat].append(tmp_attr)
#
# print(check_del)

# sys_dir = '/Users/masako/Documents/SHINRA/2021-LinkJP/sample_out/20210824/'
# sys_tail = '/*.json'
logger.info({
    'action': 'json2tsv_linkjp',
    'gold_dir': gold_dir,
})

# jsonファイル(正解とシステム出力)のリスト
json_sys_files = []
json_gold_files = []

# with open(eval_target) as e:
#     elist = e.readlines()
#     line_list = []
#     for e_line in elist:
#         line = e_line.replace('\n', '')
#
#         line_list.append(line)
#         # print('line', line_list)
#
#     gold_file = gold_dir + '*.json'
#     json_gold_files.append(gold_file)
#     for t in line_list:
#         t_line = sys_dir + t + sys_tail
#         # print('t_line', t_line)
#         json_sys_files.append(t_line)

# ページIDに対するタイトルを登録
get_title = {}
with open(title_file, mode='r', encoding='utf-8') as r:
    for rline in r:
        # rd = {}

        pid = ''
        title = ''
        # 現在の行を登録した辞書
        rd = json.loads(rline)

        # ページIDがない
        if 'page_id' not in rd:
            logger.error({
                'action': 'json2tsv_linkjp',
                'error': 'missing page_id'
            })
            sys.exit()

        # ページIDがNULL
        elif not rd['page_id']:
            logger.error({
                'action': 'json2tsv_linkjp',
                'error': 'page_id null'
            })
            sys.exit()

        else:
            pid = str(rd['page_id'])
            # print('from', from_pid)

        if 'title' not in rd:
            logger.error({
                'action': 'json2tsv_linkjp',
                'error': 'title not in rd',
                'rline': rline
            })
            sys.exit()

        # タイトルがNULL
        elif not rd['title']:
            logger.error({
                'action': 'json2tsv_linkjp',
                'error': 'no title redirect to',
                'rline': rline
            })
            sys.exit()

        else:
            title = rd['title']
            get_title[pid] = title

        rd.clear()

for ename in glob(ene_files):
    eo_list = []
    fname_after = ename.replace('.json', '.tsv')
    e_cat_pre = ename.replace(in_dir, '')
    e_cat = e_cat_pre.replace('.json', '')
    with open(ename, mode='r', encoding='utf-8') as e, open(fname_after, 'w', encoding='utf-8') as eo:
        # print(ename, '\n', fname_after)
        for eline in e:
            d_eline = json.loads(eline)
            e_key = get_key_plus(**d_eline)
            # e_key = sc.get_key_plus(log_info, **d_eline)

            e_key_list = re.split('\t', e_key)

            # 2021/12/24
            title = get_title[e_key_list[0]]
            e_key_list.insert(1, title)

            # print(e_key_list)
            logger.debug({
                'action': 'json2tsv_linkjp',
                'e_key_list': e_key_list,
                'eline': eline
            })
            # 'e_key_list': ['928404', 'テオブロミン', '特性', '粉末', '72', '21', '72', '23', ''],
            # 'eline': '{"page_id":"928404","title":attribute":"特性","html_offset":{"start":{"line_id":72,"offset":24},
            # "end":{"line_id":72,"offset":26},"text":"粉末"},"text_offset":{"start":{"line_id":72,"offset":21},
            # "end":{"line_id":72,"offset":23},"text":"粉ENE":"1.10.2"}\n'
            # 2021/12/23
            # attr_type がdel_slinkの場合スキップ
            # if attr_type == 'del_slink':
            #     e_attr = e_key_list[1]
            #     if check_del.get(e_cat):
            #         if e_attr in check_del[e_cat]:
            #             # print('del_attr', e_cat, e_attr)
            #             continue

            # PID, title, redirectのファイルではタイトルが'_'で穴埋めされている
            # titleとlink pageのtitleの表記のミスマッチを防ぐためPIDから取得
            # print(e_key_list)
            # tmp_pid = e_key_list[0]
            # # tmp_link_pid = e_key_list[6]
            # if not tmp_pid:
            #     logger.error({
            #         'action': 'json2tsv_linkjp',
            #         'error': 'no tmp_id',
            #         'eline': eline
            #     })
            #     sys.exit()
            # elif tmp_pid not in get_title:
            #     logger.error({
            #         'action': 'json2tsv_linkjp',
            #         'error': 'tmp_pid not in get_title',
            #         'rline': eline
            #
            #     })
            #     sys.exit()
            # else:
            #     title = get_title[tmp_pid]
            eo_list.append(e_key_list)

        df_eo = pd.DataFrame(eo_list)
        # print(df_eo)
        df_eo.to_csv(eo, sep='\t', header=False, index=False)

prt_dic = {}
for gold_list in json_gold_files:
    for gname in glob(gold_list):
        if not os.path.isfile(gname):
            logger.error({
                'action': 'json2tsv_linkjp',
                'error': 'file not found',
                'gname': gname
            })
            sys.exit()
        else:
            # 識別情報のみ　元の形式
            go_list = []
            # リンクタイプ情報も含む
            go_full_list = []
            gname_after = gname.replace('.json', '.tsv')
            g_cat_pre = gname.replace(gold_dir, '')
            g_cat = g_cat_pre.replace('.json', '')
            # print('g_cat', g_cat)

            with open(gname, mode='r', encoding='utf-8') as g, open(gname_after, 'w', encoding='utf-8') as go:
                # with open(gname_after, 'w', encoding='utf-8') as fo,
                # open(gname_full, 'w', encoding='utf-8') as ff:
                for gline in g:
                    # logger.info({
                    # 'action': 'json2tsv_linkjp',
                    # 'gline': gline
                    # })
                    # g_key_list = []
                    # g_key_full_list = []
                    d_gline = json.loads(gline)
                    # 見出しのタイトルはない
                    # リンク先のIDまで
                    # g_key = sc.get_key_plus(log_info, **d_gline)

                    # 準一致情報も含む
                    # g_key_full = sc.get_key_full(log_info, **d_gline)
                    g_key_full = get_key_full(**d_gline)

                    # g_key_list = re.split('\t', g_key)
                    g_key_full_list = re.split('\t', g_key_full)
                    # new_g_key_list = []
                    logger.debug({
                        'action': 'json2tsv_linkjp',
                        'g_key_full': g_key_full,
                        'g_key_full_list': g_key_full_list
                    })
                    # tmp_pid = g_key_list[0]
                    # tmp_link_pid = g_key_list[7]
                    tmp_pid = g_key_full_list[0]
                    tmp_link_pid = g_key_full_list[7]
                    if not tmp_pid:
                        logger.error({
                            'action': 'json2tsv_linkjp',
                            'error': 'tmp_pid undefined',
                            'gline': gline
                        })
                        sys.exit()
                    # 2021/6/10
                    elif tmp_pid not in get_title:
                        logger.error({
                            'action': 'json2tsv_linkjp',
                            'error': 'tmp_pid not in get_title',
                            'gline': gline
                        })
                        sys.exit()
                    else:
                        title = get_title[tmp_pid]

                    if not tmp_link_pid:
                        logger.error({
                            'action': 'json2tsv_linkjp',
                            'error': 'tmp_link_pid none',
                            'gline': gline
                        })
                        # link_title = ''
                        # 2021/6/14
                        sys.exit()

                    elif tmp_link_pid not in get_title:
                        logger.warning({
                            'action': 'json2tsv_linkjp',
                            'error': 'tmp_link_pid not in get_title',
                            'eline': eline
                        })
                        link_title = ''
                    else:
                        link_title = get_title[tmp_link_pid]
                        if not link_title:
                            logger.warning({
                                'action': 'json2tsv_linkjp',
                                'error': 'no link title',
                                'gline': gline
                            })
                    # g_key_list.insert(1, title)
                    g_key_full_list.insert(1, title)

                    # g_key_list.append(link_title)
                    # g_key_full_list.append(link_title)
                    g_key_full_list.insert(9, link_title)

                    # textが複数行の場合、改行コード'\n'を'\\n'に変換する
                    # text_pre = g_key_list[3]
                    text_pre = g_key_full_list[3]

                    # g_key_list[3] = '\\n'.join(text_pre.splitlines())
                    g_key_full_list[3] = '\\n'.join(text_pre.splitlines())

                    # new_g_key_list = g_key_list[:10]
                    # print('g_key_list', g_key_list)
                    # print('new_g_key_list', new_g_key_list)
                    logger.debug({
                        'action': 'json2tsv_linkjp',
                        # 'g_key_list': g_key_list,
                        'g_key_full_list': g_key_full_list
                    })
                    # go_list.append(g_key_list)
                    go_full_list.append(g_key_full_list)

                df_fo = pd.DataFrame(go_full_list)
                # df_fo = pd.DataFrame(go_list)
                # print(df_fo)
                df_fo.to_csv(go, sep='\t', header=False, index=False)

                # df_ff = pd.DataFrame(go_full_list)
                # print(df_fo)
                # df_ff.to_csv(ff, sep='\t', header=False, index=False)

