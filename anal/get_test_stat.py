# eneファイルのmentionのカテゴリ・属性別平均と標準偏差
# from .. import linkjpc as ljc
from glob import glob
import sys
import csv
import os
# import pandas as pd
import re
import logging
# from .. linkjpc import config as cf
from decimal import Decimal, ROUND_HALF_UP
import statistics
import math


anal_base_dir = "/Users/masako/Documents/SHINRA/2021-LinkJP/anal/"

gold_dir = "/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-211027/link_annotation/"

in_dir =  "/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-211027/ene_annotation/"

outfile = anal_base_dir + 'cat_att_mention_len_mean_pstdev.tsv'
ast_tsv = '*.tsv'
ext_tsv = '.tsv'

ext_json = '.json'
ext_anal_tsv = '_anal.tsv'
ext_summary_tsv = '_summary.tsv'
ext_fn_tsv = '_fn.tsv'

def get_category(fname, dname, extention):
    cat_pre = fname.replace(dname, '')
    cat_new = cat_pre.replace(extention, '')
    return cat_new


def tag_cat(ln):
    tkey = '\t'.join(ln)
    # tkey_mod = tkey.replace('\r', '')
    # tkey = tkey_mod.replace('\n', '')
    return tkey


in_dir_files = in_dir + ast_tsv
check_cat_att_mention_len = {}
# ene_annotation
for e_fname in glob(in_dir_files):
    cat = get_category(e_fname, in_dir, ext_tsv)

    # リンク先(バリエーションに展開)を含めた正解情報 ( 0 or pid)
    # check_gold_full = {}

    # 入力ファイル（リンクなし）
    with open(e_fname, mode='r', encoding='utf-8') as e:

        ereader = csv.reader(e, delimiter='\t')
        for erow in ereader:
            att = erow[2]
            mention = erow[3]
            mention_len = len(mention)
            cat_att = cat + ':' + att
            if cat_att not in check_cat_att_mention_len:
                check_cat_att_mention_len[cat_att] = []

            check_cat_att_mention_len[cat_att].append(mention_len)

with open(outfile, 'w', encoding='utf-8') as o:
    writer = csv.writer(o, delimiter='\t', lineterminator='\n')
    for ca, m_len_list in check_cat_att_mention_len.items():
        mean_str = str(statistics.mean(m_len_list))
        pstdev_str = str(statistics.pstdev(m_len_list))
        ca_cnt = len(check_cat_att_mention_len)
        [category, attribute] = re.split(':', ca)
        mean = float(Decimal(mean_str).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
        pstdev = float(Decimal(pstdev_str).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

        writer.writerow([category, attribute, mean, pstdev])
