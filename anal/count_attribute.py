# カテゴリ・属性別のmention数、正解数、システム出力数

import logging
# import evaluation_linkjp as el
from glob import glob
import csv
import re

def get_category(fname, dname, extention):
    cat_pre = fname.replace(dname, '')
    cat_new = cat_pre.replace(extention, '')
    return cat_new

# log_info = el.LogInfo()
# logger = el.set_logging(log_info, 'myAnalLogger')
# logger.setLevel(logging.INFO)

ast_tsv = '*.tsv'
ext_tsv = '.tsv'

cat_list = ['Airport', 'City', 'Company', 'Compound', 'Conference', 'Lake', 'Person']

in_dir = '/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-211027/ene_annotation/'
gold_dir = '/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-211027/link_annotation/'

#sys_base_dir = '/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/bert_rulebase_no_slink_attr/'
sys_base_dir = '/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/bert_aiprb_modules/'
# sys_name = 'NAIST_only_bert'
sys_name = 'a_AIPRB_SMWL'
# sys_name = 'b_NAIST_BERT'
sys_dir = sys_base_dir + sys_name + '/'
outfile = sys_dir + 'attribute_cnt.tsv'

in_dir_files = in_dir + ast_tsv
sys_dir_files = sys_dir + ast_tsv
check_rec = {}
count_rec = {}
check_sys = {}
count_sys = {}
check_gold = {}
count_gold = {}

for cat in cat_list:
    e_fname = in_dir + cat + ext_tsv

    with open(e_fname, mode='r', encoding='utf-8') as e:
        ereader = csv.reader(e, delimiter='\t')
        ene_cnt = 0
        for erow in ereader:
            e_att = erow[2]

            e_common_list = erow[:8]
            del e_common_list[1]
            e_common_list.insert(0, cat)
            # logger.debug({
            #     'action': 'count_attribute',
            #     'e_attribute': e_attribute
            # })
            e_key = cat + ':' + e_att
            e_common_key = '\t'.join(e_common_list)


            # マルチリンクは重複カウントしない
            if not check_rec.get(e_common_key):
                # print('e_common_key', e_common_key, 'e_key', e_key)

                if not count_rec.get(e_key):
                    count_rec[e_key] = 1
                else:
                    count_rec[e_key] += 1


    g_fname = gold_dir + cat + ext_tsv

    with open(g_fname, mode='r', encoding='utf-8') as g:
        greader = csv.reader(g, delimiter='\t')
        gold_cnt = 0
        for grow in greader:
            g_att = grow[2]
            g_common_list = grow[:8]
            del g_common_list[1]
            g_common_list.insert(0, cat)
            # logger.debug({
            #     'action': 'count_attribute',
            #     'g_attribute': g_attribute
            # })
            g_key = cat + ':' + g_att
            g_common_key = '\t'.join(g_common_list)

            # print('g_common_key', g_common_key, 'g_key', g_key)
            # マルチリンクは重複カウントしない
            if not check_gold.get(g_common_key):
                if not count_gold.get(g_key):
                    # 入力ファイルの共通キー
                    count_gold[g_key] = 1
                else:
                    count_gold[g_key] += 1

    s_fname = sys_dir + cat + ext_tsv

    with open(s_fname, mode='r', encoding='utf-8') as s:
        sreader = csv.reader(s, delimiter='\t')
        sys_cnt = 0
        for srow in sreader:
            s_att = srow[2]
            s_common_list = srow[:8]
            del s_common_list[1]
            s_common_list.insert(0, cat)

            # logger.debug({
            #     'action': 'count_attribute',
            #     's_attribute': s_attribute
            # })
            s_key = cat + ':' + s_att
            s_common_key = '\t'.join(s_common_list)

            # print('s_common_key', s_common_key, 's_key', s_key)
            # マルチリンクは重複カウントしない
            if not check_sys.get(s_common_key):
                if not count_sys.get(s_key):
                    # 入力ファイルの共通キー
                    count_sys[s_key] = 1
                else:
                    count_sys[s_key] += 1

with open(outfile, mode='w', encoding='utf-8') as o:
    writer = csv.writer(o, delimiter='\t', lineterminator='\n')
    for e_cat_att, e_cnt in count_rec.items():
        s_cnt = 0
        if count_sys.get(e_cat_att):
            s_cnt = count_sys[e_cat_att]
        g_cnt = 0
        if count_gold.get(e_cat_att):
            g_cnt = count_gold[e_cat_att]
        [category, attribute] = re.split(':', e_cat_att)
        print([sys_name, category, attribute, e_cnt, g_cnt, s_cnt])

        writer.writerow([sys_name, category, attribute, e_cnt, g_cnt, s_cnt])

