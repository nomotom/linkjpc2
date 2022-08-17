# evaluation_linkjp_with_tn.py
#    Args:
#        sys_dir
#        gold_dir
#        in_dir
#        target_file
#    Output:
#        judge_file(*_judge.tsv)
#        diff_file mentionの長さを追加
#    Notice:
#        judge ファイルはFPの場合、最初の要素だけを対象

# from .. import linkjpc as ljc
from glob import glob
import sys
import csv
import os
# import pandas as pd
import re
import logging
# from .. linkjpc import config as cf


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


log_info = LogInfo()
logger = set_logging(log_info, 'myAnalLogger')
logger.setLevel(logging.INFO)

print('argv', sys.argv)

sys_base_dir = sys.argv[1]
# eg. "/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/anal_multi_20211104/"

gold_dir = sys.argv[2]
# eg. "/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-211027/link_annotation/"

in_dir = sys.argv[3]
# eg. "/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-211027/ene_annotation/"

# list of systems
target_file = sys.argv[4]
# wlink_l_bcar_01_fcar_01_amax_1M
# wlink_l_bcar_02_fcar_01_amax_1

# 2021/12/23 再帰リンクの属性を除いた評価に対応
# attr_type: 'all'/'del_slink'
attr_type = sys.argv[5]
logger.info({
    'action': 'evaluation_linkjp',
    'target_file': target_file,
})
# 2021/12/23
# サンプルデータで再帰リンク率0.5以上の属性
del_attr_list = "/Users/masako/Documents/SHINRA/2021-LinkJP/anal/cat_att_selflink_equal_or_more_05.tsv"

# 転送情報
# forward_list = \
   #  "/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/common/jawiki-20190120-title2pageid_ext.tsv"
# check_forward = {}

# mint
# mint_list = '/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/test/mint_partial_match.tsv'
# tinm
# tinm_list = '/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/test/tinm_partial_match.tsv'

ast_tsv = '*.tsv'
ext_tsv = '.tsv'

ext_json = '.json'
ext_anal_tsv = '_anal.tsv'
ext_summary_tsv = '_summary.tsv'
ext_fn_tsv = '_fn.tsv'
sys_judge_tsv = '_judge.tsv'

get_title = {}
get_semi_match = {}

logger.debug({
    'action': 'evaluation_linkjp',
    'sys_base_dir': sys_base_dir,
    'gold_dir': gold_dir,
    'target_file': target_file
})

# from_title_to_id = {}
# with open(forward_list, mode='r', encoding='utf-8')as fw:
#     fw_reader = csv.reader(fw, delimiter='\t')
#     for fw_row in fw_reader:
#         from_title = fw_row[0]
#         to_pid = fw_row[3]
#         from_title_to_id[from_title] = to_pid

# get_mint_ratio = {}
# with open(mint_list, mode='r', encoding='utf-8')as ml:
#     ml_reader = csv.reader(ml, delimiter='\t')
#     for ml_row in ml_reader:
#         ml_mention = ml_row[0]
#         ml_lid = ml_row[1]
#         ml_ratio = ml_row[3]

        # mention_lid = ml_mention + ':'ml_lid

        # if not get_mint_ratio.get(ml_mention):
        #     get_mint_ratio[ml_mention] = {}
        # get_mint_ratio[ml_mention][ml_lid] = ml_ratio

# get_tinm_ratio = {}
# with open(tinm_list, mode='r', encoding='utf-8') as tl:
#     tl_reader = csv.reader(tl, delimiter='\t')
#     for tl_row in tl_reader:
#         tl_mention = tl_row[0]
#         tl_lid = tl_row[1]
#         tl_ratio = tl_row[3]
#
#         # mention_lid = ml_mention + ':'ml_lid
#
#         if not get_tinm_ratio.get(tl_mention):
#             get_tinm_ratio[tl_mention] = {}
#         get_tinm_ratio[tl_mention][tl_lid] = tl_ratio

sys_info_list = []
# system outputs
with open(target_file, mode='r', encoding='utf-8')as t:
    linelist = t.readlines()
    for line in linelist:
        sys_name = line.replace('\n', '')
        sys_path = sys_base_dir + sys_name + '/'
        sys_info_list.append([sys_name, sys_path])
        logger.debug({
            'action': 'evaluation_linkjp',
            'sys_info_list': sys_info_list,
            'sys_name': sys_name,
            'sys_path': sys_path,
        })


def get_category(fname, dname, extention):
    cat_pre = fname.replace(dname, '')
    cat_new = cat_pre.replace(extention, '')
    return cat_new


def tag_cat(ln):
    tkey = '\t'.join(ln)
    # tkey_mod = tkey.replace('\r', '')
    # tkey = tkey_mod.replace('\n', '')
    return tkey


# = gold_dir + ast_tsv
# TP, FP, TN, FN of all categories
count_sys_all = {}
get_sys_base_dir = {}
in_dir_files = in_dir + ast_tsv

check_del = {}
if attr_type == 'del_slink':
    with open(del_attr_list, 'r', encoding='utf-8') as dl:
        reader = csv.reader(dl, delimiter='\t')
        for row in reader:
            tmp_cat = row[0]
            tmp_attr = row[1]
            # print(tmp_cat, tmp_attr)
            if not check_del.get(tmp_cat):
                check_del[tmp_cat] = []
            check_del[tmp_cat].append(tmp_attr)

# ene_annotation
for e_fname in glob(in_dir_files):
    cat = get_category(e_fname, in_dir, ext_tsv)

    # リンク先(バリエーションに展開)を含めた正解情報 ( 0 or pid)
    check_gold_full = {}

    g_fname = gold_dir + cat + ext_tsv
    logger.debug({
        'action': 'evaluation_linkjp',
        'cat': cat,
        'g_fname': g_fname,
        'e_fname': e_fname,
    })

    # check_input = {}

    # multi gold answer (gold_common_key -> link1, link2 )
    get_gold_links = {}
    get_gold_nolink = {}
    # get_mention_len = {}

    # get_gold = {}
    # 入力ファイルの正解情報の数　→　正解ありのレコード数（入力ファイルで正解のある共通キー数）に変更
    gold_link_cnt = 0
    # 正解なしのレコード数（入力ファイルで正解のない共通キー数）
    gold_nolink_cnt = 0
    # gold with/without linked page
    gold_cnt = 0

    # リンクのある正解を登録(複数正解あり）
    with open(g_fname, mode='r', encoding='utf-8') as f:
        greader = csv.reader(f, delimiter='\t')

        for grow_full in greader:
            # grow_full ['928404', 'テオブロミン', '別称', '3,7-ジメチルキサンチン', '40', '130', '40', '143', '928404', 'テオブロミン']
            # print('grow_full', grow_full)
            logger.debug({
                'action': 'evaluation_linkjp',
                'grow_full': grow_full
            })
            if attr_type == 'del_slink':
                g_attr = grow_full[2]

                if check_del.get(cat):
                    if g_attr in check_del[cat]:
                        logger.debug({
                            'action': 'evaluation_linkjp',
                            'attr_type': attr_type,
                            'cat': cat,
                            'g_attr': g_attr,
                        })
                        continue

            tmp_mention = grow_full[3]
            tmp_to_id = grow_full[8]

            # 見出しのタイトルを削除
            grow_full.pop(1)

            # link_typeを除去
            grow = grow_full[:9]

            # 正解情報(見出しのタイトル以外, リンク先、リンクの種類含む)
            gold_link_key = tag_cat(grow)
            logger.debug({
                'action': 'evaluation_linkjp',
                'grow': grow,
                # '89052', '所属組織', 'ダイエー', '67', '33', '67', '37', '1568612', '福岡ソフトバンクホークス'
                'gold_link_key': gold_link_key,
                #  '89052\t所属組織\tダイエー\t67\t33\t67\t37\t1568ll
                'grow_full': grow_full,
                #  '89052', '所属組織', 'ダイエー', '67', '33', '67', '37', '1568612', '福岡ソフトバンクホークス', '1', '', ''
                # '807400', '三臭化リン', '生成化合物', '臭化アルキル', '256', '39', '256', '45', '59985', 'ハロゲン化アルキル', '', '1', '']
                'tmp_mention': tmp_mention,
                'tmp_to_id': tmp_to_id
            })

            # gold with linked page
            # gold_link_cnt += 1
            if gold_link_key not in check_gold_full:
                check_gold_full[gold_link_key] = 1
                # gold_link_cnt += 1

                # no linked info
                gold_common_key = '\t'.join(grow[0:7])
                # check_common[gold_common_key] = 1

                # linked ID, linked title
                gold_val = '\t'.join(grow_full[7:9])
                # gold_val = '\t'.join(grow[7:9])

                if not get_gold_links.get(gold_common_key):
                    get_gold_links[gold_common_key] = []
                # multi gold answers
                get_gold_links[gold_common_key].append(gold_val)
                logger.debug({
                    'action': 'evaluation_linkjp',
                    'gold_common_key(get_gold_link)': gold_common_key,
                    #  '89052\t家族\t工藤阿須加\t69\t6\t69\t11'
                    'gold_val': gold_val
                    # 'gold_val': '2734114'
                })

                # tmp_list = [pid, at, text, start_line_id, start_offset, end_line_id, end_offset, link_id, later_name,
                # part_of, derivation_of]
                if not get_semi_match.get(gold_common_key):
                    get_semi_match[gold_common_key] = []
                    get_semi_match[gold_common_key] = [grow_full[9], grow_full[10], grow_full[11]]
                    # get_mention_len = len(grow[2])

                # if from_title_to_id.get(tmp_mention):
                #     if from_title_to_id[tmp_mention] == tmp_to_id:
                #         mention_id = tmp_mention + ':' + tmp_to_id
                #         check_forward[mention_id] = 1

    # 入力ファイルの共通キー
    check_rec = {}

    # 入力ファイルのレコード数
    ene_cnt = 0

    # 入力ファイル（リンクなし）
    with open(e_fname, mode='r', encoding='utf-8') as e:
        ereader = csv.reader(e, delimiter='\t')
        for erow in ereader:
            # 2021/12/25
            # 見出しのタイトルを登録
            if not get_title.get(erow[0]):
                eid = erow[0]
                etitle = erow[1]
                get_title[eid] = etitle
                logger.debug({
                    'action': 'evaluation_linkjp',
                    'eid': eid,
                    'etitle': etitle,
                })
            # 2021/12/24
            # 見出しのタイトルを除去
            erow.pop(1)

            if attr_type == 'del_slink':
                # e_attr = erow[1]
                e_attr = erow[1]

                if check_del.get(cat):
                    if e_attr in check_del[cat]:
                        logger.debug({
                            'action': 'evaluation_linkjp',
                            'attr_type': attr_type,
                            'cat': cat,
                            'e_attr': e_attr,
                        })
                        continue
            ene_cnt += 1
            # 余計なタブがついている
            e_common_key_pre = tag_cat(erow)
            logger.debug({
                'action': 'evaluation_linkjp',
                'e_common_key_pre': e_common_key_pre
            })
            e_common_key = e_common_key_pre.rstrip()

            if not check_rec.get(e_common_key):
                # 入力ファイルの共通キー
                check_rec[e_common_key] = 1

            logger.debug({
                'action': 'evaluation_linkjp',
                'e_common_key': e_common_key
            })
            # 正解がリンクありの場合
            if e_common_key in get_gold_links:
                # リンクありのレコード数
                gold_link_cnt += 1
                logger.debug({
                    'action': 'evaluation_linkjp',
                    'e_fname': e_fname,
                    'gold_link_cnt': gold_link_cnt
                })

            # 正解がリンクなしの場合
            else:
                # リンクなし正解として登録
                get_gold_nolink[e_common_key] = 1
                # リンクなしのレコード数
                gold_nolink_cnt += 1
                logger.debug({
                    'action': 'evaluation_linkjp',
                    'cat': cat,
                    # 'e_fname': e_fname,
                    'e_common_key': e_common_key,
                    'gold_nolink_cnt': gold_nolink_cnt
                })

    cnt = 0
    # system list
    for sys_info in sys_info_list:
        cnt += 1
        logger.debug({
            'action': 'evaluation_linkjp',
            'sys_info': sys_info,
            'cnt': cnt
        })
        # システム名
        s_name = sys_info[0]
        if not s_name:
            logger.error({
                'action': 'evaluation_linkjp',
                'no sname found': sys_info,
                'cnt': cnt
            })
            continue
        # ディレクトリ
        s_dir = sys_info[1]
        get_sys_base_dir[s_name] = s_dir
        logger.debug({
            'action': 'evaluation_linkjp',
            's_name': s_name,
            's_dir': s_dir
        })

        s_fname = s_dir + cat + ext_tsv
        # s_fname_log = s_dir + cat + '_log' + ext_tsv
        s_anal_fname = s_fname.replace(ext_tsv, ext_anal_tsv)
        s_summary_fname = s_fname.replace(ext_tsv, ext_summary_tsv)
        fn_fname = s_fname.replace(ext_tsv, ext_fn_tsv)
        sys_judge_fname = s_fname.replace(ext_tsv, sys_judge_tsv)

        if os.path.isfile(s_fname):
            # システム出力（元ページタイトル除く）のキーを登録
            check_sys_full = {}

            get_sys_links = {}
            with open(s_fname, mode='r', encoding='utf-8') as f, open(s_summary_fname, 'w', encoding='utf-8') as so, \
                    open(fn_fname, 'w', encoding='utf-8') as fnf, open(sys_judge_fname, 'w', encoding='utf-8') as sj:

                logger.debug({
                    'action': 'evaluation_linkjp',
                    's_fname': s_fname,
                    's_name': s_name
                })
                sreader = csv.reader(f, delimiter='\t')
                all_srow = []
                sys_tp_cnt = 0
                sys_fp_cnt = 0

                sys_fp1_cnt = 0
                sys_fp2_cnt = 0

                sys_fn_cnt = 0
                sys_tn_cnt = 0
                fn_list = []
                sys_judge_list = []

                cat_attr_tp = {}
                cat_attr_fp = {}
                cat_attr_fn = {}
                sys_output_cnt = 0

                # 実行結果をtsvに変換したファイル
                for srow in sreader:

                    if attr_type == 'del_slink':
                        s_attr = srow[1]

                        if check_del.get(cat):
                            if s_attr in check_del[cat]:
                                print('del_attr', cat, s_attr)
                                continue

                    # if not get_title.get(srow[0]):
                    #     get_title[srow[0]] = srow[1]
                    # get_title[srow[0]] = srow[1]
                    # delete title
                    del srow[1]
                    # with linking info
                    system_key = tag_cat(srow)
                    sys_output_cnt += 1

                    # later_name = ''
                    # part_of = ''
                    # derivation_of = ''
                    # if get_semi_match.get(system_key):
                    #     later_name = get_semi_match[system_key][0]
                    #     part_of = get_semi_match[system_key][1]
                    #     derivation_of = get_semi_match[system_key][2]

                    logger.debug({
                        'action': 'evaluation_linkjp',
                        'phase': 'before',
                        'system_key': system_key,
                        # '89052\t家族\t工藤阿須加\t69\t6\t69\t11\t2734114\t工藤阿須加'
                    })
                    # システム出力（見出しページのタイトル以外）を登録
                    if system_key not in check_sys_full:
                        check_sys_full[system_key] = 1

                    sys_common_key = '\t'.join(srow[0:7])
                    # リンク先のページIDとタイトル
                    sys_val = '\t'.join(srow[7:9])

                    logger.debug({
                        'action': 'evaluation_linkjp',
                        'system_key': system_key,
                        # '89052\t家族\t工藤阿須加\t69\t6\t69\t11\t2734114\t工藤阿須加'
                        'sys_common_key': sys_common_key,
                        # '89052\t家族\t工藤阿須加\t69\t6\t69\t11'
                        'sys_val': sys_val
                        # '2734114\t工藤阿須加'
                    })

                    # sys_mention_len = len(srow[2])

                    # システム出力のリンク先（IDとタイトル)を共通キーで登録(複数出力も許す)
                    if not get_sys_links.get(sys_common_key):
                        get_sys_links[sys_common_key] = []
                    get_sys_links[sys_common_key].append(sys_val)

                # found = 0

                # リンクあり正解
                for tmp_key in get_gold_links:

                    # get_tinm_ratio
                    tmp_mention = srow[2]
                    # tmp_to_id = get_gold_links[tmp_key][0]
                    # logger.info({
                    #     'action': 'evaluation_linkjp',
                    #     'tmp_key': tmp_key,
                    #     'tmp_mention': tmp_mention,
                    #     'tmp_to_id': tmp_to_id
                    #     # '73944\t両親\t平経盛\t67\t342\t67\t345'
                    #     # '90312\t合併市区町村\t新居町\t85\t59\t85\t62'
                    # })
                    # tinm_ratio = 0
                    # if get_tinm_ratio.get(tmp_mention):
                    #     if get_tinm_ratio.get(tmp_mention).get(tmp_to_id):
                    #         tinm_ratio = get_tinm_ratio[tmp_mention][tmp_to_id]
                    # get_mint_ratio
                    # mint_ratio = 0
                    # if get_mint_ratio.get(tmp_mention):
                    #     if get_mint_ratio.get(tmp_mention).get(tmp_to_id):
                    #         mint_ratio = get_mint_ratio[tmp_mention][tmp_to_id]
                    later_name = ''
                    part_of = ''
                    derivation_of = ''
                    if get_semi_match.get(tmp_key):
                        later_name = get_semi_match[tmp_key][0]
                        part_of = get_semi_match[tmp_key][1]
                        derivation_of = get_semi_match[tmp_key][2]
                    # tmp_key にタイトルを挿入する
                    tmp_key_list = re.split('\t', tmp_key)
                    tmp_key_list.insert(1, get_title[tmp_key_list[0]])
                    tmp_key_with_title = '\t'.join(tmp_key_list)
                    # tmp_mention_len = len(tmp_key_list[2])
                    tmp_key_with_title_list = re.split('\t', tmp_key_with_title)
                    # tmp_mention = tmp_key_with_title_list[3]


                    # FN(システム出力なし)
                    if not get_sys_links.get(tmp_key):
                        judge = 'FN'
                        # found = 1
                        sys_fn_cnt += 1
                        tmp_key_extend = '\t'.join([cat, tmp_key_with_title])
                        fn_list.append(tmp_key_extend)
                        # sys_judge_list.append('\t'.join([cat, tmp_key, '', '', judge]))
                        continue
                    # システム出力あり
                    else:
                        # 複数正解のリンク先リスト
                        cand_gold_link_list = get_gold_links[tmp_key]
                        # multi gold answer
                        tp_found = 0
                        tmp_gold_sys_link = ''
                        tmp_gold_title = ''
                        # tmp_mention_len = len(tmp_mention)
                        # print('tmp_mention', tmp_mention, tmp_mention_len)

                        for gold_link in cand_gold_link_list:
                            (gid, gtitle) = re.split('\t', gold_link)
                            logger.debug({
                                'action': 'evaluation_linkjp',
                                'get_sys_links[tmp_key]': get_sys_links[tmp_key],
                                'gold_link': gold_link,
                                'gid': gid,
                                'gtitle': gtitle
                            })
                            # tmp_mint_ratio = 0
                            # tmp_tinm_ratio = 0
                            tmp_mention_len = len(tmp_key_with_title_list[3])
                            # if get_mint_ratio.get(tmp_mention):
                            #     if get_mint_ratio.get(gid):
                            #         tmp_mint_ratio = get_mint_ratio[tmp_mention][gid]
                            #         logger.info({
                            #             'action': 'evaluation_linkjp',
                            #             'tmp_key': tmp_key,
                            #             'tmp_mention': tmp_mention,
                            #             'gid': gid,
                            #             'gtitle': gtitle,
                            #             'tmp_mint_ratio': tmp_mint_ratio,
                            #         })
                            # if get_tinm_ratio.get(tmp_mention):
                            #     if get_tinm_ratio.get(gid):
                            #         tmp_tinm_ratio = get_tinm_ratio[tmp_mention][gid]
                            #         logger.info({
                            #             'action': 'evaluation_linkjp',
                            #             'tmp_key': tmp_key,
                            #             'tmp_mention': tmp_mention,
                            #             'gid': gid,
                            #             'gtitle': gtitle,
                            #             'tmp_tinm_ratio': tmp_tinm_ratio
                            #         })

                            # 転送の可能性があるか
                            # forward = ''
                            # tmp_mention_id = tmp_mention + ':' + gid
                            # print('tmp_mention_id', tmp_mention_id)

                            # if check_forward.get(tmp_mention_id):
                            #     forward = '1'
                            #     logger.info({
                            #         'action': 'evaluation_linkjp',
                            #         'tmp_key': tmp_key,
                            #         'tmp_mention': tmp_mention,
                            #         'tmp_mention_id': tmp_mention_id,
                            #         'tmp_to_id': tmp_to_id,
                            #         'forward': forward
                            #         # '73944\t両親\t平経盛\t67\t342\t67\t345'
                            #         # '90312\t合併市区町村\t新居町\t85\t59\t85\t62'
                            #     })
                            sys_link_list = get_sys_links[tmp_key]
                            # 'sys_common_key': sys_common_key,
                            # '89052\t家族\t工藤阿須加\t69\t6\t69\t11'
                            # 'sys_val': sys_val
                            # '2734114\t工藤阿須加'

                            sys_link_found = 0
                            for sys_link in sys_link_list:
                                (sid, stitle) = re.split('\t', sys_link)
                                if sid == gid:
                                    sys_link_found = 1
                                    tmp_gold_id = sid
                                    tmp_gold_title = stitle
                                    sys_judge_list.append('\t'.join([s_name, cat, tmp_key_with_title, sys_link,
                                                                     tmp_gold_id, tmp_gold_title, 'TP', later_name,
                                                                     part_of, derivation_of, str(tmp_mention_len)]))

                                    # print('semi_match', get_semi_match[tmp_key][0], get_semi_match[tmp_key][1],
                                    # get_semi_match[tmp_key][2])
                                    break
                            if sys_link_found == 1:
                                tp_found = 1
                                break

                                # 'FP1', later_name, part_of, derivation_of, forward, str(tmp_mention_len)]))

                                # TP (システム出力が正解のいずれかと一致）
                        if tp_found == 1:
                            judge = 'TP'
                            sys_tp_cnt += 1
                            continue
                        # FP (システム出力が全ての正解と不一致)
                        else:
                            judge = 'FP1'
                            sys_fp1_cnt += 1
                            # found = 1

                            sys_judge_list.append('\t'.join([s_name, cat, tmp_key_with_title,
                                                             get_sys_links[tmp_key][0], get_gold_links[tmp_key][0],
                                                             'FP1', later_name, part_of, derivation_of, str(tmp_mention_len)]))
                            continue

                # リンクなしが正解
                for tmp_nkey in get_gold_nolink:
                    logger.debug({
                        'action': 'evaluation_linkjp',
                        'tmp_nkey': tmp_nkey,
                        's_name': s_name,
                        's_dir': s_dir
                    })
                    # tmp_mint_ratio = ''
                    # tmp_tinm_ratio = ''
                    # 転送の可能性があるか
                    # forward = ''
                    # if check_forward.get(tmp_nkey):
                    #     forward = check_forward[tmp_key]

                    later_name = ''
                    part_of = ''
                    derivation_of = ''
                    if get_semi_match.get(tmp_nkey):
                        later_name = get_semi_match[tmp_nkey][0]
                        part_of = get_semi_match[tmp_nkey][1]
                        derivation_of = get_semi_match[tmp_nkey][2]
                    # tmp_nkey': '89052\t作品\tゆうどきネットワーク - 「あのときを忘れない」\t1332\t1\t1332\t25', 'judge': 'FP2', 'value': 1
                    # tmp_nkey にタイトルを挿入する
                    tmp_nkey_list = re.split('\t', tmp_nkey)
                    tmp_nkey_list.insert(1, get_title[tmp_nkey_list[0]])
                    tmp_nkey_with_title = '\t'.join(tmp_nkey_list)
                    tmp_nkey_with_title_list = re.split('\t', tmp_nkey_with_title)
                    t_mention_len = len(tmp_nkey_with_title_list[3])

                    # TN(システム出力なし)
                    if not get_sys_links.get(tmp_nkey):
                        logger.debug({
                            'action': 'evaluation_linkjp',
                            'tmp_nkey': tmp_nkey,
                            'value': get_gold_nolink[tmp_nkey]
                        })

                        judge = 'TN'
                        sys_tn_cnt += 1
                        # found = 1
                        # lf_list.append('\t'.join(['TN', cat, tmp_key]))
                        # sys_judge_list.append('\t'.join([s_name, cat, tmp_nkey_with_title, '', '',
                        #                                  '', '', 'TN', later_name, part_of, derivation_of,
                        #                                  str(0)]))
                        continue
                    # FP(システム出力あり)
                    else:
                        judge = 'FP2'
                        logger.debug({
                            'tmp_nkey': tmp_nkey,
                            'judge': judge,
                            'value': get_gold_nolink[tmp_nkey],
                            'mention': tmp_nkey_list[3],
                            'len': tmp_mention_len
                        })
                        # {'tmp_nkey': '384083\t特性\t変異原性\t320\t8\t320\t12', 'judge': 'FP2', 'value': 1}
                        # 94555 - 2021-12-25 23:47:41,396 - myAnalLogger INFO
                        sys_fp2_cnt += 1

                        # get_sys_links
                        # 'sys_common_key': sys_common_key,
                        # '89052\t家族\t工藤阿須加\t69\t6\t69\t11'
                        # 'sys_val': sys_val
                        # '2734114\t工藤阿須加'

                        sys_judge_list.append('\t'.join([s_name, cat, tmp_nkey_with_title, get_sys_links[tmp_nkey][0],
                                                         '', '', 'FP2', later_name, part_of, derivation_of,
                                                         str(t_mention_len)]))
                                                        # '', '', 'FP2', later_name, part_of, derivation_of, forward,

                        # found = 1
                        # lf_list.append('\t'.join(['FP', cat, tmp_key]))
                        continue

                # 評価指標
                # リンク先がない場合は考慮していない
                prec = 0
                recall = 0
                f1 = 0
                sys_fp_cnt = sys_fp1_cnt + sys_fp2_cnt

                try:
                    prec = sys_tp_cnt / (sys_tp_cnt + sys_fp_cnt)
                except ZeroDivisionError:
                    pass
                try:
                    # 2021-LinkJPではリンク先ありの正解のみを分母とする
                    recall = sys_tp_cnt / gold_link_cnt
                    # recall = sys_tp_cnt / (sys_tp_cnt + sys_fp_cnt + sys_fn_cnt)
                    # recall = sys_tp_cnt / (sys_tp_cnt + sys_fn_cnt)

                except ZeroDivisionError:
                    pass
                try:
                    f1 = (2 * prec * recall) / (prec + recall)
                except ZeroDivisionError:
                    pass
                # print(prec, recall, f1)
                logger.debug({
                    'action': 'evaluation_linkjp',
                    'cat': cat,
                    'f1': f1,
                    'precision': prec,
                    'recall': recall
                })
                # gold_cnt = gold_link_cnt + gold_nolink_cnt
                logger.debug({
                    'action': 'evaluation_linkjp',
                    'cat': cat,
                    'ene_cnt': ene_cnt,
                    # 'gold_cnt': gold_cnt,
                    'gold_link_cnt': gold_link_cnt,
                    'gold_nolink': gold_nolink_cnt,
                })
                summary_list = ['CAT', 'SYS_ID', 'F1', 'Precision', 'Recall', 'ENE', 'GOLD_LINK', 'GOLD_NOLINK',
                                'SYS_LINK', 'TP', 'FP', 'TN', 'FN', 'FP1', 'FP2']
                val_list = [cat, s_name, str(f1), str(prec), str(recall), str(ene_cnt), str(gold_link_cnt),
                            str(gold_nolink_cnt),  str(sys_output_cnt), str(sys_tp_cnt), str(sys_fp_cnt),
                            str(sys_tn_cnt), str(sys_fn_cnt), str(sys_fp1_cnt), str(sys_fp2_cnt)]

                summary_str = '\t'.join(summary_list) + '\n'
                val_str = '\t'.join(val_list) + '\n'
                all_str = summary_str + val_str
                logger.debug({
                    'action': 'evaluation_linkjp',
                    'summary_str': summary_str,
                    'all_str': all_str,
                })
                so.write(all_str)

                fn_list_str = '\n'.join(fn_list)
                fnf.write(fn_list_str)

                # print('sys_judge_list_before', sys_judge_list)

                # # titleを挿入 →　これはtmp_keyまたはtmp_nkeyに対して早い段階で行う
                # for sjl in sys_judge_list:
                #     # print('sjl', sjl)
                #     # sjl AIPRB_SMWL  Person  2140566 国籍    大韓民国        46      7       46      11
                #     382006  大韓民国        382006  大韓民国        TP
                #     sjl_list = re.split('\t', sjl)
                #     print(sjl_list)
                #     te_pid = sjl_list[2]
                #     if get_title.get(te_pid):
                #         te_title = get_title[te_pid]
                #     sys_judge_list.insert(3, te_title)
                #     # print('sys_judge_list_after', sys_judge_list)

                sys_judge_list_str = '\n'.join(sys_judge_list) + '\n'

                sj.write(sys_judge_list_str)
                # lf_list_str = '\n'.join(lf_list)
                #
                # lf.write(lf_list_str)

                if s_name not in count_sys_all:
                    count_sys_all[s_name] = {}
                if 'tp' not in count_sys_all[s_name]:
                    count_sys_all[s_name]['tp'] = 0
                if 'fp' not in count_sys_all[s_name]:
                    count_sys_all[s_name]['fp'] = 0
                if 'fp1' not in count_sys_all[s_name]:
                    count_sys_all[s_name]['fp1'] = 0
                if 'fp2' not in count_sys_all[s_name]:
                    count_sys_all[s_name]['fp2'] = 0
                if 'tn' not in count_sys_all[s_name]:
                    count_sys_all[s_name]['tn'] = 0
                if 'fn' not in count_sys_all[s_name]:
                    count_sys_all[s_name]['fn'] = 0
                if 'ene' not in count_sys_all[s_name]:
                    count_sys_all[s_name]['ene'] = 0
                # if 'gold' not in count_sys_all[s_name]:
                    # count_sys_all[s_name]['gold'] = 0
                if 'gold_link' not in count_sys_all[s_name]:
                    count_sys_all[s_name]['gold_link'] = 0
                if 'gold_nolink' not in count_sys_all[s_name]:
                    count_sys_all[s_name]['gold_nolink'] = 0
                if 'sys_link' not in count_sys_all[s_name]:
                    count_sys_all[s_name]['sys_link'] = 0

                count_sys_all[s_name]['tp'] += sys_tp_cnt
                count_sys_all[s_name]['fp'] += sys_fp_cnt
                count_sys_all[s_name]['fp1'] += sys_fp1_cnt
                count_sys_all[s_name]['fp2'] += sys_fp2_cnt

                count_sys_all[s_name]['tn'] += sys_tn_cnt
                count_sys_all[s_name]['fn'] += sys_fn_cnt
                # 入力ファイルのレコード数
                count_sys_all[s_name]['ene'] += ene_cnt
                # リンクありの正解数
                count_sys_all[s_name]['gold_link'] += gold_link_cnt
                # リンクなしの正解数
                count_sys_all[s_name]['gold_nolink'] += gold_nolink_cnt
                # 正解数
                # count_sys_all[s_name]['gold'] += gold_cnt
                # システム出力数
                count_sys_all[s_name]['sys_link'] += sys_output_cnt

for sys_name, stat_dic in count_sys_all.items():
    logger.debug({
        'action': 'evaluation_linkjp',
        'sys_name': sys_name,
        'stat_dic': stat_dic
    })
    sys_allcat_summary = get_sys_base_dir[sys_name] + 'all_summary.tsv'
    with open(sys_allcat_summary, 'w', encoding='utf-8') as aa:

        tp_all = stat_dic['tp']
        fp_all = stat_dic['fp']
        fp1_all = stat_dic['fp1']
        fp2_all = stat_dic['fp2']

        tn_all = stat_dic['tn']
        fn_all = stat_dic['fn']
        ene_all = stat_dic['ene']
        # gold_all = stat_dic['gold']
        gold_link_all = stat_dic['gold_link']
        gold_nolink_all = stat_dic['gold_nolink']
        sys_link_all = stat_dic['sys_link']

        prec_all = 0
        recall_all = 0
        f1_all = 0
        try:
            prec_all = tp_all / (tp_all + fp_all)
        except (NameError, ValueError, ZeroDivisionError):
            pass
        try:
            # recall_all = tp_all / (tp_all + fp_all + fn_all)
            recall_all = tp_all / gold_link_all

        except ZeroDivisionError:
            pass
        try:
            f1_all = (2 * prec_all * recall_all) / (prec_all + recall_all)

        except ZeroDivisionError:
            pass

        print_list = '\t'.join([str(sys_name), str(f1_all), str(prec_all), str(recall_all), str(ene_all),
                                str(gold_link_all), str(gold_nolink_all), str(sys_link_all),
                                str(tp_all), str(fp_all), str(tn_all), str(fn_all),
                                str(fp1_all), str(fp2_all)])
        logger.info({
            'action': 'evaluation_linkjp',
            'print_list': print_list,
        })
        # {'action': 'evaluation_linkjp',
        # 'print_list': 'AIPRB_SMW\t0.8260371109507028\t0.8307284994448715\t0.8213984124303327\t17253\t11842
        # \t5411\t13779\t9727\t1982\t4037\t1507\t608\t1374'}

        print_char = print_list + '\n'
        aa.write(print_char)
