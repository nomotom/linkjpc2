#eval_linkjp.py <sys_dir> <target_list>
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

logger = ljc.logging.getLogger('myLogger')

sys_dir = sys.argv[1]
sys_tail = '/*.tsv'
gold_dir = sys.argv[2]
target_file = sys.argv[3]
ext = '.tsv'
anal_ext = '_anal.tsv'
summary_ext = '_summary.tsv'
fn_ext = '_fn.tsv'

logger.info({
    'action':'evaluation_linkjp',
    'sys_dir':sys_dir,
    'gold_dir': gold_dir,
    'target_file': target_file
})

sys_files = []
with open(target_file, mode='r', encoding='utf-8')as t:

    linelist = t.readlines()
    for line in linelist:
        sys_name = line.replace('\n', '')
        sys_file = sys_dir + sys_name + '/'
        print('(eval_linkjp)sys_name, sys_file', sys_name, sys_file)
        sys_files.append([sys_name, sys_file])
        logger.debug({
            'action':'evaluation_linkjp',
            'sys_name':sys_name,
            'sys_file': sys_file,
        })

gold = gold_dir + '*.tsv'

def get_category(fname, dname, exte):
    cat_pre = fname.replace(dname, '')
    cat_new = cat_pre.replace(exte, '')
    return cat_new

def tag_cat(row):
    tkey = '\t'.join(row)
    return tkey

# TP, FP, TN, FN of all categories
count_sys_all = {}
get_sys_dir = {}

for g_fname in glob(gold):
    cat = get_category(g_fname, gold_dir, ext)
    check_gold = {}
    g_fname = gold_dir + cat + ext
    logger.info({
        'action': 'evaluation_linkjp',
        'cat': cat,
        'g_fname': g_fname,
    })

    gold_cnt = 0
    get_gold = {}

    with open(g_fname, mode='r', encoding='utf-8') as f:
        greader = csv.reader(f, delimiter='\t')

        for grow in greader:
            gold_key = tag_cat(grow)

            if gold_key not in check_gold:
                check_gold[gold_key] = 1
                gold_cnt += 1

                common_key = '\t'.join(grow[0:8])
                gold_val = '\t'.join(grow[8:])

                get_gold[common_key] = gold_val
                # print('(diff_tsv)common_key, gold_val', common_key, gold_val)

    cnt = 0
    for sys_list in sys_files:
        check_sys = {}

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

        s_fname = s_dir + cat + ext
        s_anal_fname = s_fname.replace(ext, anal_ext)
        s_summary_fname =  s_fname.replace(ext, summary_ext)
        fn_fname = s_fname.replace(ext, fn_ext)

        if os.path.isfile(s_fname):
            with open(s_fname, mode='r', encoding='utf-8') as f:
                sreader = csv.reader(f, delimiter='\t')
                all_srow = []
                sys_cnt = 0

                for srow in sreader:
                    system_key = tag_cat(srow)

                    sys_cnt += 1

                    if system_key not in check_sys:
                        check_sys[system_key] = 1

                    if system_key in check_gold:
                        judge = 'TP'
                    else:
                        judge = 'FP'
                    srow.append(judge)

                    common_key = '\t'. join(srow[0:8])
                    if get_gold.get(common_key):
                        gold_val = get_gold[common_key]
                        srow.append(gold_val)

                    srow = [str(n) for n in srow]
                    srow_str = '\t'.join(srow)
                    all_srow.append(srow_str)

                with open(s_anal_fname, 'w', encoding='utf-8') as ao:

                    ao.write('\n'.join(all_srow))
                    all_srow = []

                sys_tp_cnt = 0
                sys_fp_cnt = 0
                sys_fn_cnt = 0
                sys_tn_cnt = 0
                fn_list = []

                cat_attr_tp = {}
                cat_attr_fp = {}
                cat_attr_fn = {}
                # print(fn_list)
                with open(s_summary_fname, 'w', encoding='utf-8') as so, open(fn_fname, 'w', encoding='utf-8') as fnf:

                    # evaluate if system output is correct
                    for s_key in check_sys:
                        cat_attr = cat + ':' + s_key[2]
                        if s_key in check_gold:
                            sys_tp_cnt += 1
                            # 2021/10/4
                            if not cat_attr_tp.get(cat_attr):
                                cat_attr_tp[cat_attr] = 1
                            else:
                                cat_attr_tp[cat_attr] += 1
                        else:
                            sys_fp_cnt += 1
                            #cat_attr_fp[cat_attr] += 1

                    # evaluate if gold is output
                    for g_key in check_gold:
                        cat_attr = cat + ':' + g_key[2]
                        if g_key not in check_sys:
                            sys_fn_cnt += 1
                            #cat_attr_fn[cat_attr] += 1
                            fn_list.append(g_key)

                    # 評価指標
                    # リンク先がない場合は考慮していない
                    prec = 0
                    recall = 0
                    f1 = 0
                    # print('sys_cnt', sys_cnt)
                    # print('gold_cnt', gold_cnt)
                    # print('sys_tp_cnt', sys_tp_cnt)
                    # print('sys_fp_cnt', sys_fp_cnt)
                    # print('sys_fn_cnt', sys_fn_cnt)
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
                    logger.info({
                        'action': 'evaluation_linkjp',
                        'cat': cat,
                        'f1': f1,
                        'precision': prec,
                        'recall': recall
                    })
                    summary_list = [
                        'CAT', 'SYS_ID',
                        'F1', 'Precision', 'Recall',
                        'SYS_LINK', 'GOLD_LINK',
                        'TP', 'FP', 'TN', 'FN'
                    ]
                    val_list = [
                        cat, s_name,
                        str(f1), str(prec), str(recall),
                        str(sys_cnt), str(gold_cnt),
                        str(sys_tp_cnt), str(sys_fp_cnt), str(sys_tn_cnt), str(sys_fn_cnt)
                    ]

                    summary_str = '\t'.join(summary_list) + '\n'
                    val_str = '\t'.join(val_list) + '\n'
                    all_str = summary_str + val_str
                    logger.info({
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
                    if 'sys_link' not in count_sys_all[s_name]:
                        count_sys_all[s_name]['sys_link'] = 0
                    if 'gold_link' not in count_sys_all[s_name]:
                        count_sys_all[s_name]['gold_link'] = 0

                    count_sys_all[s_name]['tp'] += sys_tp_cnt
                    count_sys_all[s_name]['fp'] += sys_fp_cnt
                    count_sys_all[s_name]['tn'] += sys_tn_cnt
                    count_sys_all[s_name]['fn'] += sys_fn_cnt
                    count_sys_all[s_name]['sys_link'] += sys_cnt
                    count_sys_all[s_name]['gold_link'] += gold_cnt

                    fn_df = pd.DataFrame(fn_list)
                    fn_df.to_csv(fnf, sep='\t')


for sid_a, v in count_sys_all.items():
    # print(sid_a, v)
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
        sys_link_a = v['sys_link']
        # print('sys_link', sys_link_a)
        gold_link_a = v['gold_link']
        # print('gold_link', gold_link_a)

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

        print_list = '\t'.join([str(sid_a), str(f1_a), str(prec_a), str(recall_a), str(sys_link_a), str(gold_link_a), str(tp_a), str(fp_a), str(tn_a), str(fn_a)])

        logger.info({
            'action': 'evaluation_linkjp',
            'print_list': print_list,
        })
        print_char = print_list + '\n'
        aa.write(print_char)
