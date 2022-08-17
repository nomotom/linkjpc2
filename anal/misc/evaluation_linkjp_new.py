# evaluation_linkjp_new.py
'''
    Args:
        sys_dir
        gold_dir
        in_dir
        target_file
'''
# FP is not supported
# ゼロ割りの際には何もしない

import linkjpc as ljc
from glob import glob
import sys
import csv
import os
import pandas as pd
import re
import logging
import config as cf


log_info = cf.LogInfo('verbose')
logger = ljc.set_logging(log_info, 'myEvalLogger')
#logger = ljc.logging.getLogger('myLogger')
#logger = ljc.set_logging(log_info, 'myLogger')

sys_dir = sys.argv[1]
# eg. "/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/anal_multi_20211104/"

gold_dir = sys.argv[2]
# eg. "/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-211027/link_annotation/"

in_dir = sys.argv[3]
# eg. "/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-211027/ene_annotation/"

# list of systems
target_file = sys.argv[4]
# eval_target="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/anal_multi_20211104/eval_test_target12345"


ast_tsv = '*.tsv'
ext_tsv = '.tsv'
ext_json = '.json'
ext_anal_tsv = '_anal.tsv'
ext_summary_tsv = '_summary.tsv'
ext_fn_tsv = '_fn.tsv'

logger.debug({
    'action': 'evaluation_linkjp',
    'sys_dir': sys_dir,
    'gold_dir': gold_dir,
    'target_file': target_file
})

sys_files = []
# system outputs
with open(target_file, mode='r', encoding='utf-8')as t:

    linelist = t.readlines()
    for line in linelist:
        sys_name = line.replace('\n', '')
        sys_file = sys_dir + sys_name + '/'
        # print('(eval_linkjp)sys_name, sys_file', sys_name, sys_file)
        sys_files.append([sys_name, sys_file])
        logger.debug({
            'action': 'evaluation_linkjp',
            'sys_name': sys_name,
            'sys_files': sys_files,
            'sys_file': sys_file,
        })

def get_category(fname, dname, exte):
    cat_pre = fname.replace(dname, '')
    cat_new = cat_pre.replace(exte, '')
    return cat_new


def tag_cat(row):
    tkey = '\t'.join(row)
    return tkey

gold = gold_dir + ast_tsv
# TP, FP, TN, FN of all categories
count_sys_all = {}
get_sys_dir = {}
in_dir_files = in_dir + ast_tsv

for e_fname in glob(in_dir_files):
    cat = get_category(e_fname, in_dir, ext_tsv)

    # dictionary to register gold info including linked page ( 0 or pid)
    check_gold_link = {}

    #e_fname = in_dir + cat + ext_tsv
    g_fname = gold_dir + cat + ext_tsv
    logger.debug({
        'action': 'evaluation_linkjp',
        'cat': cat,
        'g_fname': g_fname,
        'e_fname': e_fname,
    })
    # gold with linked page
    gold_link_cnt = 0
    # gold without linked page
    gold_nolink_cnt = 0
    # gold with/without linked page
    gold_cnt = 0

    # input
    ene_cnt = 0

    #check_input = {}

    get_gold_link = {}
    get_gold_nolink = {}

    get_gold = {}

    # gold with link page
    with open(g_fname, mode='r', encoding='utf-8') as f:
        greader = csv.reader(f, delimiter='\t')

        for grow in greader:
            # delete title of the page, which is not included in ene_annotation and sys output files.
            grow.pop(1)

            gold_link_key = tag_cat(grow)
            if '工藤阿須加' in gold_link_key:
                logger.debug({
                    'action': 'evaluation_linkjp',
                    'grow': grow,
                    # '89052', '家族', '工藤阿須加', '69', '6', '69', '11', '2734114', '工藤阿須加'
                    'gold_link_key': gold_link_key
                    # '89052\t家族\t工藤阿須加\t69\t6\t69\t11\t2734114\t工藤阿須加'
                })

            gold_link_cnt += 1
            if gold_link_key not in check_gold_link:
                check_gold_link[gold_link_key] = 1
                # gold_link_cnt += 1


                common_key = '\t'.join(grow[0:7])
                # check_common[common_key] = 1

                #ID
                gold_val = '\t'.join(grow[7:9])

                if not get_gold_link.get(common_key):
                    get_gold_link[common_key] = []
                get_gold_link[common_key].append(gold_val)
                if '工藤阿須加' in common_key:
                    logger.debug({
                        'action': 'evaluation_linkjp',
                        'common_key(get_gold_link)': common_key,
                        #  '89052\t家族\t工藤阿須加\t69\t6\t69\t11'
                        'gold_val': gold_val
                        # 'gold_val': '2734114'
                    })
                logger.debug({
                    'action': 'evaluation_linkjp',
                    'common_key': common_key,
                    'gold_val': gold_val
                })
    # get_gold_nolink = {}

    check_rec = {}
    with open(e_fname, mode='r', encoding='utf-8') as e:
        ereader = csv.reader(e, delimiter='\t')
        for erow in ereader:
            ene_cnt += 1
            gold_ekey_pre = tag_cat(erow)

            # remove the rightmost tab
            gold_ekey = gold_ekey_pre.rstrip()

            if '928404' in gold_ekey:
                logger.debug({
                    'action': 'evaluation_linkjp',
                    'gold_ekey': gold_ekey
                })
            logger.debug({
                'action': 'evaluation_linkjp',
                'gold_ekey': gold_ekey
            })

            if gold_ekey not in get_gold_link:
                get_gold_nolink[gold_ekey] = 1
                logger.debug({
                    'action': 'evaluation_linkjp',
                    'phase': 'get_gold_nolink',
                    'gold_ekey': gold_ekey
                    # 928404\t特性\t色は白か透明\t72\t27\t72\t33
                })
                gold_nolink_cnt += 1

            e_common_key = '\t'.join(erow[0:7])
            logger.debug({
                'action': 'evaluation_linkjp',
                'e_common_key': e_common_key
                # '928404\t特性\t色は白か透明\t72\t27\t72\t33'
            })

            if not check_rec.get(e_common_key):
                check_rec[e_common_key] = 1
        logger.debug({
            'action': 'evaluation_linkjp',
            'e_fname': e_fname,
            '# of get_gold_nolink': len(get_gold_nolink)
        })

    cnt = 0
    # system list
    for sys_list in sys_files:
        cnt += 1
        logger.debug({
            'action': 'evaluation_linkjp',
            'sys_list': sys_list
        })
        s_name = sys_list[0]
        if not s_name:
            logger.error({
                'action': 'evaluation_linkjp',
                'no sname found': sys_list,
                'cnt': sys_list
            })
            continue
        s_dir = sys_list[1]
        get_sys_dir[s_name] = s_dir
        logger.debug({
            'action': 'evaluation_linkjp',
            's_name': s_name,
            's_dir': s_dir
        })

        s_fname = s_dir + cat + ext_tsv
        s_anal_fname = s_fname.replace(ext_tsv, ext_anal_tsv)
        s_summary_fname = s_fname.replace(ext_tsv, ext_summary_tsv)
        fn_fname = s_fname.replace(ext_tsv, ext_fn_tsv)

        if os.path.isfile(s_fname):
            # sys rec
            check_sys_link = {}
            get_sys_link = {}
            with open(s_fname, mode='r', encoding='utf-8') as f, open(s_summary_fname, 'w', encoding='utf-8') as so, open(fn_fname, 'w', encoding='utf-8') as fnf:

                logger.debug({
                    'action': 'evaluation_linkjp',
                    's_fname': s_fname,
                    's_name': s_name
                })
                sreader = csv.reader(f, delimiter='\t')
                all_srow = []
                sys_tp_cnt = 0
                sys_fp_cnt = 0
                sys_fn_cnt = 0
                sys_tn_cnt = 0
                fn_list = []

                cat_attr_tp = {}
                cat_attr_fp = {}
                cat_attr_fn = {}
                sys_cnt = 0

                for srow in sreader:
                    # delete title
                    del srow[1]
                    system_key = tag_cat(srow)
                    sys_cnt += 1

                    logger.debug({
                        'action': 'evaluation_linkjp',
                        'phase': 'before',
                        'system_key': system_key,
                        # '89052\t家族\t工藤阿須加\t69\t6\t69\t11\t2734114\t工藤阿須加'
                    })
                    if system_key not in check_sys_link:
                        check_sys_link[system_key] = 1

                    sys_common_key = '\t'.join(srow[0:7])
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
                    if not get_sys_link.get(sys_common_key):
                        get_sys_link[sys_common_key] = sys_val


                # print(fn_list)
                found = 0

                for tmp_key in get_gold_link:
                    logger.debug({
                        'action': 'evaluation_linkjp',
                        'tmp_key': tmp_key
                        #'73944\t両親\t平経盛\t67\t342\t67\t345'
                        # '90312\t合併市区町村\t新居町\t85\t59\t85\t62'
                    })
                    if not get_sys_link.get(tmp_key):
                        judge = 'FN'
                        found = 1
                        sys_fn_cnt += 1
                        continue
                    else:
                        cand_gold_link_list = get_gold_link[tmp_key]
                        found = 0
                        for gold_link in cand_gold_link_list:
                            (gid, gtitle) = re.split('\t', gold_link)
                            logger.debug({
                                'action': 'evaluation_linkjp',
                                'gold_link': gold_link,
                                # 521068\tチーム青森
                                # '280846\t新居町_(静岡県)'
                                'gid': gid
                            })
                            logger.debug({
                                'action': 'evaluation_linkjp',
                                'get_sys_link[tmp_key]': get_sys_link[tmp_key],
                                # 280846\t新居町_(静岡県)
                                'gold_link': gold_link
                                # '280846\t新居町_(静岡県)'
                            })
                            (sid, stitle) = re.split('\t', get_sys_link[tmp_key])
                            if sid == gid:
                                found = 1
                                judge = 'TP'
                                sys_tp_cnt += 1
                                break
                        if found == 1:
                            continue
                        else:
                            judge = 'FP'
                            sys_fp_cnt += 1
                            found = 1
                            continue
                for tmp_nkey in get_gold_nolink:
                    logger.debug({
                        'action': 'evaluation_linkjp',
                        'tmp_nkey': tmp_nkey,
                        's_name': s_name,
                        's_dir': s_dir
                    })
                    if not get_sys_link.get(tmp_nkey):
                        logger.debug({
                            'action': 'evaluation_linkjp',
                            'tmp_nkey': tmp_nkey,
                            'value': get_gold_nolink[tmp_nkey]
                        })
                        judge = 'TN'
                        sys_tn_cnt += 1
                        found = 1
                        continue
                    else:
                        judge = 'FP'
                        sys_fp_cnt += 1
                        found = 1
                        continue

                    # # evaluate if system output is correct
                    # for s_key in check_sys_link:
                    #     cat_attr = cat + ':' + s_key[2]
                    #     if check_gold_link.get(s_key):
                    #         sys_tp_cnt += 1
                    #         # 2021/10/4
                    #         if not cat_attr_tp.get(cat_attr):
                    #             cat_attr_tp[cat_attr] = 1
                    #         else:
                    #             cat_attr_tp[cat_attr] += 1
                    #     else:
                    #         sys_fp_cnt += 1
                    #         # cat_attr_fp[cat_attr] += 1
                    #
                    # # evaluate if gold is output
                    # for c_key in get_gold_link:
                    #     cat_attr = cat + ':' + c_key[2]
                    #     if get_gold_link[c_key][0] == 0 and c_key not in check_sys_output:
                    #         sys_tn_cnt += 1
                    #     elif get_gold_link[c_key][0] != 0 and c_key not in check_sys_output:
                    #         sys_fn_cnt += 1
                    #        fn_list.append(c_key)

                # 評価指標
                # リンク先がない場合は考慮していない
                prec = 0
                recall = 0
                f1 = 0

                try:
                    prec = sys_tp_cnt / (sys_tp_cnt + sys_fp_cnt)
                except ZeroDivisionError:
                    pass
                try:
                    recall = sys_tp_cnt / (sys_tp_cnt + sys_fn_cnt)
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
                gold_cnt = gold_link_cnt + gold_nolink_cnt
                summary_list = [
                    'CAT', 'SYS_ID', 'F1', 'Precision', 'Recall',
                    'ENE', 'GOLD','GOLD_LINK', 'GOLD_NOLINK', 'SYS_LINK',
                    'TP', 'FP', 'TN', 'FN'
                ]
                val_list = [
                    cat, s_name,
                    str(f1), str(prec), str(recall),
                    str(ene_cnt), str(gold_cnt), str(gold_link_cnt), str(gold_nolink_cnt),  str(sys_cnt),
                    str(sys_tp_cnt), str(sys_fp_cnt), str(sys_tn_cnt), str(sys_fn_cnt)
                ]

                summary_str = '\t'.join(summary_list) + '\n'
                val_str = '\t'.join(val_list) + '\n'
                all_str = summary_str + val_str
                logger.debug({
                    'action': 'evaluation_linkjp',
                    'all_str': all_str,
                })
                so.write(all_str)

                if s_name not in count_sys_all:
                    count_sys_all[s_name] = {}
                if 'tp' not in count_sys_all[s_name]:
                    count_sys_all[s_name]['tp'] = 0
                if 'fp' not in count_sys_all[s_name]:
                    count_sys_all[s_name]['fp'] = 0
                if 'tn' not in count_sys_all[s_name]:
                    count_sys_all[s_name]['tn'] = 0
                if 'fn' not in count_sys_all[s_name]:
                    count_sys_all[s_name]['fn'] = 0
                if 'ene' not in count_sys_all[s_name]:
                    count_sys_all[s_name]['ene'] = 0
                if 'gold' not in count_sys_all[s_name]:
                    count_sys_all[s_name]['gold'] = 0
                if 'gold_link' not in count_sys_all[s_name]:
                    count_sys_all[s_name]['gold_link'] = 0
                if 'gold_nolink' not in count_sys_all[s_name]:
                    count_sys_all[s_name]['gold_nolink'] = 0
                if 'sys_link' not in count_sys_all[s_name]:
                    count_sys_all[s_name]['sys_link'] = 0


                count_sys_all[s_name]['tp'] += sys_tp_cnt
                count_sys_all[s_name]['fp'] += sys_fp_cnt
                count_sys_all[s_name]['tn'] += sys_tn_cnt
                count_sys_all[s_name]['fn'] += sys_fn_cnt
                count_sys_all[s_name]['ene'] += ene_cnt
                count_sys_all[s_name]['gold_link'] += gold_link_cnt
                count_sys_all[s_name]['gold_nolink'] += gold_nolink_cnt
                count_sys_all[s_name]['gold'] += gold_cnt

                count_sys_all[s_name]['sys_link'] += sys_cnt

for sid_a, v in count_sys_all.items():
    logger.debug({
        'action': 'evaluation_linkjp',
        'sid_a': sid_a,
        'v': v
    })
    sys_allcat_summary = get_sys_dir[sid_a] + 'all_summary.tsv'
    with open(sys_allcat_summary, 'w', encoding='utf-8') as aa:

        tp_a = v['tp']
        # print('tp', tp_a)
        fp_a = v['fp']
        # print('fp', fp_a)
        tn_a = v['tn']
        # print('tn', tn_a)
        fn_a = v['fn']
        # print('fn', fn_a)
        ene_a = v['ene']
        gold_a = v['gold']
        gold_link_a = v['gold_link']
        gold_nolink_a = v['gold_nolink']
        # print('gold_link', gold_link_a)
        sys_link_a = v['sys_link']
        # print('sys_link', sys_link_a)

        prec_a = 0
        recall_a = 0
        f1_a = 0
        try:
            prec_a = tp_a / (tp_a + fp_a)
        except (NameError, ValueError, ZeroDivisionError):
            pass
        try:
            recall_a = tp_a / (tp_a + fn_a)
        except ZeroDivisionError:
            pass
        try:
            f1_a = (2 * prec_a * recall_a) / (prec_a + recall_a)

        except ZeroDivisionError:
            pass

        print_list = '\t'.join([str(sid_a), str(f1_a), str(prec_a), str(recall_a), str(ene_a), str(gold_a), str(gold_link_a),
                                str(gold_nolink_a),str(sys_link_a), str(tp_a), str(fp_a), str(tn_a), str(fn_a)])

        print(print_list)
        logger.info({
            'action': 'evaluation_linkjp',
            'print_list': print_list,
        })
        print_char = print_list + '\n'
        aa.write(print_char)
