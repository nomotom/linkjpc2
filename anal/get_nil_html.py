# get_nil.py
#    入力ファイルのうち正解nilだけを出力
#    Output:
#        nil_file(*_nil.tsv)


# from .. import linkjpc as ljc
from glob import glob
import sys
import csv
import os
# import pandas as pd
import re

gold_dir = "/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/link_annotation/"
in_dir = "/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/ene_annotation/"

ast_tsv = '*_html.tsv'
ext_tsv = '_html.tsv'

gold_nil_tsv = 'gold_nil_html.tsv'

out_file = gold_dir + gold_nil_tsv


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
in_dir_files = in_dir + ast_tsv

# 正解なし
nil_list = []
# ene_annotation
for e_fname in glob(in_dir_files):
    cat = get_category(e_fname, in_dir, ext_tsv)

    #正解情報
    check_gold = {}

    g_fname = gold_dir + cat + ext_tsv
    # check_input = {}


    # リンクのある正解のキーを登録(複数正解あり）
    with open(g_fname, mode='r', encoding='utf-8') as f:
        greader = csv.reader(f, delimiter='\t')

        for grow_full in greader:
            # link情報を除去
            grow = grow_full[:8]
            #print('grow', grow)

            gold_common_key = tag_cat(grow)

            if not check_gold.get(gold_common_key):
                check_gold[gold_common_key] = 1

    # 入力ファイル（リンクなし）
    with open(e_fname, mode='r', encoding='utf-8') as e:
        ereader = csv.reader(e, delimiter='\t')
        for erow_full in ereader:
            erow = erow_full[:8]
            # print('erow', erow)

            e_common_key = tag_cat(erow)

            if not check_gold.get(e_common_key):
                check_gold[e_common_key] = 1
                erow.insert(0, cat)
                erow_expand_key= tag_cat(erow)
                nil_list.append(erow_expand_key)
                # print('nil_list', nil_list)

with open(out_file, mode='w', encoding='utf-8') as o:
    nil_list_str = '\n'.join(nil_list)
    o.write(nil_list_str)

