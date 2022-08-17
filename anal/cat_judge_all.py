'''
  cat_judge
    1) cat, attr, mentionごとに正解したシステムをまとめて出力
        出力：judge_mention 　（'sys_all_judge_mention.tsv'）

    2) 正解リンクのあるcat, attrごとに正答システムの組み合わせを数える　
        出力：judge_cat_attr （'sys_all_judge_mention_by_cat_attr.tsv'）
'''

import pandas as pd
from glob import glob
import csv
import re
import operator



base_dir= '/Users/masako/Documents/SHINRA/2021-LinkJP/'
#sys_all_base_dir = base_dir + 'test_out/exp/'
#sys_all_base_dir = base_dir + 'test_out/aiprb/'
sys_all_base_dir = base_dir + 'test_out/exp_systems/'

sys_judged = sys_all_base_dir + '*/*_judge.tsv'
# sys_all_judge_tp = sys_all_base_dir + 'sys_all_judge_tp.tsv'

eval_target = sys_all_base_dir + 'eval_target.txt'
# eval_target = sys_all_base_dir + 'eval_target.txt'
# with open(judge_file, 'r', encoding='utf-8') as j, open(sys_all_judge_tp, 'w', encoding='utf-8'):
    # '89052\t家族\t工藤阿須加\t69\t6\t69\t11\t2734114\t工藤阿須加'

#属性のリンク先のあるメンション数
mention_with_link = base_dir + 'anal/stats_testdata/test_att_freq_all.txt'

stats = sys_all_base_dir + 'sys_all_cat_att_stat.tsv'

judge_mention = sys_all_base_dir + 'sys_all_judge_mention.tsv'

judge_mention_stat = sys_all_base_dir + 'sys_all_judge_mention_stat.tsv'
judge_cat_attr = sys_all_base_dir + 'sys_all_judge_mention_by_cat_attr.tsv'

judge_mention_df = sys_all_base_dir + 'sys_all_judge_mention_df.tsv'

#scat_list = ['airport', 'city', 'company', 'compound', 'conference', 'lake', 'person']

cat_list = ['Airport', 'City', 'Company', 'Compound', 'Conference', 'Lake', 'Person']
# 評価対象のシステムを登録
check = {}
with open(eval_target, 'r', encoding='utf-8') as et:
    for eline in et:
        new_eline = eline.rstrip('\n')
        # print(new_eline)
        check[new_eline] = 1

cols = [ 'cat', 'att','pageid',  'mention', 'sl', 'sp', 'el', 'ep',  'judge', 's_name']

df_all = pd.DataFrame(index=[], columns=cols)
# print(df_all)
# print(df))
#for judge_file in glob(sys_judged):
# reg = {}


#各属性のリンク先のあるメンション数
cnt_cat_attr = {}

with open(mention_with_link, 'r', encoding='utf-8') as m:

    mreader = csv.reader(m, delimiter='\t')
    for mline in mreader:
        cat = mline[0]
        attr= mline[1]
        freq_str = mline[4].rstrip('\n')

        c_a = cat + '\t' + attr

        # 頻度が0の場合は登録しない　分母が0になるため
        if int(freq_str) != 0:
            cnt_cat_attr[c_a] = int(freq_str)
            #print(c_a, cnt_cat_attr[c_a])

for sys in check:
    tmp_sys_dir = sys_all_base_dir + sys + '/'
    for cat in cat_list:
        tmp_judge_file = tmp_sys_dir + cat + '_judge.tsv'
        # print(tmp_judge_file)
        df = pd.read_csv(tmp_judge_file, delimiter='\t', usecols=(0,1,2,3,4,5,6,7,8,13),
        names=('sys', 'cat', 'pageid', 'att', 'mention', 'sl', 'sp', 'el', 'ep', 'judge'), dtype={'sl': str, 'sp': str, 'el': str, 'ep': str, 'pageid':str})
        #names=('sys', 'cat', 'pageid', 'att', 'mention', 'sl', 'sp', 'el', 'ep', 'judge'), dtype={'sl': str, 'sp': str, 'el': str, 'ep': str, 'pageid':str})

        #names = ('s_name', 'cat','pageid', 'att', 'mention', 'sl', 'sp', 'el', 'ep', 'judge'))
        # names=('s_name', 'cat', 'pageid', 'att', 'mention', 'sl', 'sp', 'el', 'ep', 'link_pageid',
                        #        'link_title', 'gold_pageid', 'gold_title', 'judge'))

        #df.replace(sys, 1, inplace=True)

        #print(df)
        df_all = df_all.append(df, ignore_index=True)
        #df_all = df_all.append(df, ignore_index=True)


# s_list = []
# for sl in check:
#     s_list.append(sl)
# print(sl, s_list)
# df_all.fillna('Z', inplace=True)

# df_all['sys_list'] = df_all['AIPRB_SMWL'] + ';'+ \
#                      df_all['AIPRB_SMW'] + ';'+ \
#                      df_all['AIPRB_WSM'] + ';'+ \
#                      df_all['NAIST_baseline_plus_bert'] + ';'+ \
#                      +df_all['NAIST_only_bert'] + ';'+ \
#                      df_all['ATID_ATAG'] + ';'+ \
#                      +df_all['ATID_ATAG_SEARCH'] + ';'+ \
#                      +df_all['AIPCB_CBI'] + ';'+ \
#                      +df_all['amano_genre']

#df_all['sys_list'] = [df_all['AIPRB_SMWL']+ df_all['AIPRB_SMW']+ df_all['AIPRB_WSM']+df_all['NAIST_baseline_plus_bert']+df_all['NAIST_only_bert']+df_all['ATID_ATAG']+df_all['ATID_ATAG_SEARCH']+df_all['AIPCB_CBI']+df_all['amano_genre']

df_all['common_key'] = df_all[['cat', 'att', 'pageid', 'mention', 'sl', 'sp', 'el', 'ep', 'judge']].agg(';'.join, axis=1)

df_all = df_all.drop(['cat', 'att', 's_name', 'pageid', 'mention', 'sl', 'sp', 'el', 'ep', 'judge'], axis=1)
check_common_key = {}
df_all.to_csv(judge_mention_df, sep='\t', index=False)
with open(judge_mention_df, 'r', encoding='utf-8') as dd:
    dreader = csv.reader(dd, delimiter='\t')
    for dline in dreader:
        print(dline)
        sys = dline[0]
        common_key = dline[1]


        # TPのみ
        if ';TP' in common_key:
            if not check.get(common_key):
                check_common_key[common_key] = []
            check_common_key[common_key].append(sys)
            print('sys', sys)
            print('common_key', common_key)
            print('check_common', check_common_key[common_key])

cnt_cv = {}
for ck, cv in check_common_key.items():
    # print(cv)
    cv_str = ';'.join(cv)
    if not cnt_cv.get(cv_str):
        cnt_cv[cv_str] = 1
    else:
        cnt_cv[cv_str] += 1

with open(stats, 'w', encoding='utf-8') as sf:
    writer = csv.writer(sf, delimiter='\t', lineterminator='\n')
    for sfk, sfv in cnt_cv.items():
        writer.writerow([sfk, sfv])
#print(df_all)
#grouped = df_all.groupby('common_key').size()
#print(grouped)

#for st in check:
    #df_all = df_all.drop([st], axis=1)

#df_all = df_all.drop(s_list, axis=1)
#for l in check:
    #df_all.drop(l)
#print(df_all)




#df_grouped = df_all.groupby('common_key').describe()
#print(df_grouped)



#print(df_all.groupby('common_key')['sys'].count())
# print(df_all['s_name'].value_counts())
# print(df_all['cat','pageid', 'att', 'mention', 'sl', 'sp', 'el', 'ep', 'judge'].value_counts())
# del(df_all)
# dic_judge_mention = {}
# dic_judge_mention_sys_check = {}
# for sys in check:
#     tmp_sys_dir = sys_all_base_dir + sys + '/'
#     for cat in cat_list:
#         tmp_judge_file = tmp_sys_dir + cat + '_judge.tsv'
#         with open(tmp_judge_file, 'r', encoding='utf-8') as j:
#             reader = csv.reader(j, delimiter='\t')
#             for row in reader:
#                 # print(row)
#                 common_key = '\t'.join([row[1],row[3],row[2],row[4],row[5],row[6],row[7],row[8]])
#                 # print(common_key)
#                 if common_key not in dic_judge_mention:
#                     dic_judge_mention[common_key] = []
#                 sys = row[0]
#                 if not dic_judge_mention_sys_check.get(common_key):
#                     dic_judge_mention_sys_check[common_key] = {}
#                 if not dic_judge_mention_sys_check[common_key].get(sys):
#                     dic_judge_mention[common_key].append(sys)
#                     dic_judge_mention_sys_check[common_key][sys] = 1
#
# dic_judge_cat_attr = {}
#
# with open(judge_mention, 'w', encoding='utf-8') as jm:
#     writer = csv.writer(jm)
#     for c_key,sys_list in dic_judge_mention.items():
#         writer.writerow([c_key,sys_list])
#         sys_list_str = ';'.join(sys_list)
#
#         c_key_list = re.split('\t',c_key)
#         cat_attr = c_key_list[0] + '\t' + c_key_list[1]
#         if not cat_attr in dic_judge_cat_attr:
#             dic_judge_cat_attr[cat_attr] = {}
#         if not dic_judge_cat_attr[cat_attr].get(sys_list_str):
#             dic_judge_cat_attr[cat_attr][sys_list_str] = 1
#         else:
#             dic_judge_cat_attr[cat_attr][sys_list_str] += 1
#
#
# with open(judge_cat_attr,'w', encoding='utf-8') as jca:
#     writer = csv.writer(jca)
#     ptr = {}
#     for tmp_cat_attr in dic_judge_cat_attr:
#         for tmp_sys_str, cnt in dic_judge_cat_attr[tmp_cat_attr].items():
#             ratio = cnt/(cnt_cat_attr[tmp_cat_attr])
#             #print('ratio', ratio, 'cnt', cnt,'cnt_cat_attr[tmp_cat_attr]',cnt_cat_attr[tmp_cat_attr] )
#             if not ptr.get(tmp_cat_attr):
#                 ptr[tmp_cat_attr] = {}
#             if not ptr[tmp_cat_attr].get(cnt):
#                 ptr[tmp_cat_attr][cnt] = []
#             tmp_sys_str_list = re.split(';', tmp_sys_str)
#
#             #ptr[tmp_cat_attr][cnt].append([len(tmp_sys_str_list), ratio, tmp_sys_str])
#             ptr[tmp_cat_attr][cnt].append([ratio, len(tmp_sys_str_list), tmp_sys_str])
#
#
#     for tca, tmp_cnt in ptr.items():
#         for cnt_key in tmp_cnt:
#             tmp_cnt[cnt_key] = sorted(tmp_cnt[cnt_key], reverse=True)
#             # tmp_cnt[cnt_key] = sorted(tmp_cnt[cnt_key], key=operator.itemgetter(1), reverse=True)
#         #writer.writerow([tca, new_tmp_cnt])
#         writer.writerow([tca, tmp_cnt])
#
#
#
#
#
#
