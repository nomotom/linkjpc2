'''
 gen_nearest_link_info
 tag_info
    #cat     pid     line_id html_text_start html_text_end   html_text       title
    #City    3692278 34      148     150     日本    日本
 gold_files
    #1013693 ルイス・ムニョス・マリン国際空港        別名    Aeropuerto Internacional Luis Muñoz Marín
    42      16      42      57      1013693 ルイス・ムニョス・マリン国際空港
 参考ページ
　https://docs.pyq.jp/python/pydata/scipy/ttest.html
'''

import csv
import pandas as pd
import numpy as np
from scipy.stats import t, ttest_1samp, ttest_rel, ttest_ind
from glob import glob
import re
import math


#
minus_check = 1
plus_check = 1
# conf = 0.95
minus_cand_ratio_max = 0.9
plus_cand_ratio_max = 0.9

# 同じ行の場合を無視するか
ignore_zero = 1

# sample data
#gold_dir = '/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/link_annotation/'
#tmp_dir = '/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/sample/'
#out_dir = '/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/common/'

# test data
gold_dir = '/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-210825/link_annotation/'
tmp_dir = '/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/test/'
out_dir = '/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/test/'


gold_files = gold_dir + '*.tsv'

tag_info = tmp_dir + 'html_tag_info.tsv'

outfile = tmp_dir + 'mention_gold_link_dist.tsv'

with open(tag_info, 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')

    cat_pid_title_dic = {}
    check_cat_pid_title_line = {}
    for row in reader:
        cat = row[0]
        if cat == 'cat':
            continue
        pid = row[1]
        line_start = row[2]
        html_text_start = row[3]
        html_text_end = row[4]
        html_text = row[5]
        title = row[6]
        cat_pid_title_line = ':'.join([cat, pid, title, line_start])
        cat_pid_title = ':'.join([cat, pid, title])

        if not check_cat_pid_title_line.get(cat_pid_title_line):
            cat_pid_title_dic[cat_pid_title] = []
        cat_pid_title_dic[cat_pid_title].append(int(line_start))
        check_cat_pid_title_line[cat_pid_title_line] = 1

out_raw_list = []
for gfile in glob(gold_files):
    list_rec_out = []
    gfile_part = gfile.replace(gold_dir,'')
    ene_cat = gfile_part.replace('.tsv', '')
    # print(gfile)
    with open(gfile, 'r', encoding='utf-8') as g:
        greader = csv.reader(g, delimiter='\t')

        for grow in greader:
            g_org_pid = grow[0]
            g_attr = grow[2]
            g_mention_line_start = grow[4]
            g_gold_title = grow[9]
            g_cat_attr = ':'.join([ene_cat, g_attr])
            g_cat_pid_title = ':'.join([ene_cat, g_org_pid, g_gold_title])
            # print('g_cat_pid_title', g_cat_pid_title)

            if cat_pid_title_dic.get(g_cat_pid_title):

                tmp_lineid_list = cat_pid_title_dic[g_cat_pid_title]
                # print('tmp_lineid_list', tmp_lineid_list)

                found = 0
                for lineid in tmp_lineid_list:
                    # print('lineid', lineid)
                    # print('g_line_start', g_line_start)

                    if int(g_mention_line_start) == lineid:
                        if ignore_zero:
                            continue
                        else:
                            diff_min = 0
                            found = 1
                            break
                    else:
                        if found == 0:
                            diff_min = lineid - int(g_mention_line_start)
                        elif abs(lineid - int(g_mention_line_start) < abs(diff_min)):
                            diff_min = lineid - int(g_mention_line_start)
                            found = 1

                # print(ene_cat, g_attr, diff_min, grow)
                out_raw_list.append([ene_cat, g_attr, diff_min])

df = pd.DataFrame(out_raw_list, columns=['cat', 'attr', 'diff_min'])
df.to_csv(outfile, sep='\t',  index=False)
#
#
#
# #minus_cand_max_str = str(minus_cand_ratio_max * 100).replace('.0', '')
# #plus_cand_max_str = str(plus_cand_ratio_max * 100).replace('.0', '')
#
# # if minus_check and plus_check:
# #     out_limit = out_dir + 'gold_link_limit_' + plus_cand_max_str + '_' + minus_cand_max_str + '.tsv'
# # elif minus_check and not plus_check:
# #     out_limit = out_dir + 'gold_link_limit_'  + minus_cand_max_str + '.tsv'
# # elif plus_check and not minus_check:
# #     out_limit = out_dir + 'gold_link_limit_' + minus_cand_max_str + '.tsv'
#
#
# non_zero_thresh = 0.1
# diff_zero_dic = {}
# diff_plus_dic = {}
# diff_minus_dic = {}
# diff_all_dic = {}
#
# if not diff_all_dic.get(g_cat_attr):
#     diff_all_dic[g_cat_attr] = []
# diff_all_dic[g_cat_attr].append(diff_min)
#
# if diff_min > 0:
#     if not diff_plus_dic.get(g_cat_attr):
#         diff_plus_dic[g_cat_attr] = []
#     # diff_dic[g_cat_attr].append(diff_min)
#     diff_plus_dic[g_cat_attr].append(diff_min)
# elif diff_min < 0:
#     if not diff_minus_dic.get(g_cat_attr):
#         diff_minus_dic[g_cat_attr] = []
#     # diff_dic[g_cat_attr].append(diff_min)
#     diff_minus_dic[g_cat_attr].append(diff_min)
# else:
#     if not diff_zero_dic.get(g_cat_attr):
#         diff_zero_dic[g_cat_attr] = []
#     # diff_dic[g_cat_attr].append(diff_min)
#     diff_zero_dic[g_cat_attr].append(diff_min)
#
# diff_all_list = []
# for cat_attr, lid_list in diff_all_dic.items():
#     (cat, attr) = re.split(':', cat_attr)
#     diff_all_num = 0
#     diff_minus_num = 0
#     diff_zero_num = 0
#     diff_plus_num = 0
#
#     if diff_all_dic.get(cat_attr):
#         diff_all_num = len(diff_all_dic[cat_attr])
#     if diff_minus_dic.get(cat_attr):
#         diff_minus_num = len(diff_minus_dic[cat_attr])
#     if diff_zero_dic.get(cat_attr):
#         diff_zero_num = len(diff_zero_dic[cat_attr])
#     if diff_plus_dic.get(cat_attr):
#         diff_plus_num = len(diff_plus_dic[cat_attr])
#
#     minus_limit = 0
#     if (diff_minus_num / diff_all_num) > non_zero_thresh:
#         #lid_list.sort()
#         minus_list = diff_minus_dic[cat_attr]
#         minus_list.sort(reverse=True)
#         minus_cand_max_num = math.ceil(minus_cand_ratio_max * diff_minus_num)
#         del minus_list[(minus_cand_max_num -1):]
#         print(minus_list)
#         if len(minus_list) > 0:
#             minus_limit = minus_list[-1]
#     print(minus_limit)
#
#     plus_limit = 0
#     if (diff_plus_num / diff_all_num) > non_zero_thresh:
#         plus_list = diff_plus_dic[cat_attr]
#         plus_list.sort()
#         plus_cand_max_num = math.ceil(plus_cand_ratio_max * diff_plus_num)
#         del plus_list[(plus_cand_max_num - 1):]
#         print(plus_list)
#         if len(plus_list) > 0:
#             plus_limit = plus_list[-1]
#
#     print(plus_limit)
#
#     diff_all_list.append([cat, attr, minus_limit, plus_limit, diff_zero_num, diff_minus_num, diff_plus_num, diff_all_num])
#
#     # interval_list.append([cat, attr, n, lo_mod, up_mod])
#
# i_df = pd.DataFrame(diff_all_list, columns=['cat', 'attr', 'minus_limit', 'plus_limit', 'zero_num', 'minus_num', 'plus_num', 'all_num'])
# i_df.to_csv(out_limit, sep='\t', index=False)


# '''
#  tag_info
#     #cat     pid     line_id html_text_start html_text_end   html_text       title
#     #City    3692278 34      148     150     日本    日本
#  gold_files
#     #1013693 ルイス・ムニョス・マリン国際空港        別名    Aeropuerto Internacional Luis Muñoz Marín
#     42      16      42      57      1013693 ルイス・ムニョス・マリン国際空港
#  参考ページ
# 　https://docs.pyq.jp/python/pydata/scipy/ttest.html
# '''
#
# import csv
# import pandas as pd
# import numpy as np
# from scipy.stats import t, ttest_1samp, ttest_rel, ttest_ind
# from glob import glob
# import re
#
# # 信頼水準
# conf = 0.95
#
# # 同じ行の場合を無視するか
# ignore_zero = 1
#
# # sample data
# #gold_dir = '/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-sample-210428/link_annotation/'
# #tmp_dir = '/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/sample/'
# #out_dir = '/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/common/'
#
# # test data
# gold_dir = '/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-210825/link_annotation/'
# tmp_dir = '/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/test/'
# out_dir = '/Users/masako/Documents/SHINRA/2021-LinkJP/Download/ljc_data/test/'
#
#
# gold_files = gold_dir + '*.tsv'
#
# tag_info = tmp_dir + 'html_tag_info.tsv'
#
# out_raw = tmp_dir + 'gold_link_info.tsv'
# #out_raw = out_dir + 'gold_link_info.tsv'
#
# #out_interval = tmp_dir + 'gold_link_interval.tsv'
#
# conf_str = str(conf * 100)
# conf_mod = conf_str.replace('.0', '')
# if ignore_zero:
#     out_interval = out_dir + 'gold_link_interval_conf_' + 'ignore_zero' + str(conf_mod) + '.tsv'
# else:
#     out_interval = out_dir + 'gold_link_interval_conf_' + str(conf_mod) + '.tsv'
#
#
#
# with open(tag_info, 'r', encoding='utf-8') as f:
#     reader = csv.reader(f, delimiter='\t')
#
#     cat_pid_title_dic = {}
#     check_cat_pid_title_line = {}
#     for row in reader:
#         cat = row[0]
#         if cat == 'cat':
#             continue
#         pid = row[1]
#         line_start = row[2]
#         html_text_start = row[3]
#         html_text_end = row[4]
#         html_text = row[5]
#         title = row[6]
#         cat_pid_title_line = ':'.join([cat, pid, title, line_start])
#         cat_pid_title = ':'.join([cat, pid, title])
#
#         if not check_cat_pid_title_line.get(cat_pid_title_line):
#             cat_pid_title_dic[cat_pid_title] = []
#         cat_pid_title_dic[cat_pid_title].append(int(line_start))
#         check_cat_pid_title_line[cat_pid_title_line] = 1
#
#     prior_cnt = {}
#     next_cnt = {}
#
# base = 1000000
# out_raw_list = []
# diff_dic = {}
# for gfile in glob(gold_files):
#     list_rec_out = []
#     gfile_part = gfile.replace(gold_dir,'')
#     ene_cat = gfile_part.replace('.tsv', '')
#     # print(gfile)
#     with open(gfile, 'r', encoding='utf-8') as g:
#         greader = csv.reader(g, delimiter='\t')
#
#         for grow in greader:
#             g_org_pid = grow[0]
#             g_attr = grow[2]
#             g_mention_line_start = grow[4]
#             g_gold_title = grow[9]
#             g_cat_attr = ':'.join([ene_cat, g_attr])
#             g_cat_pid_title = ':'.join([ene_cat, g_org_pid, g_gold_title])
#             # print('g_cat_pid_title', g_cat_pid_title)
#
#             if cat_pid_title_dic.get(g_cat_pid_title):
#
#                 tmp_lineid_list = cat_pid_title_dic[g_cat_pid_title]
#                 # print('tmp_lineid_list', tmp_lineid_list)
#
#                 found = 0
#                 for lineid in tmp_lineid_list:
#                     # print('lineid', lineid)
#                     # print('g_line_start', g_line_start)
#
#                     if int(g_mention_line_start) == lineid:
#                         if ignore_zero:
#                             continue
#                         else:
#                             diff_min = 0
#                             found = 1
#                             break
#                     else:
#                         if found == 0:
#                             diff_min = lineid - int(g_mention_line_start)
#                         elif abs(lineid - int(g_mention_line_start) < abs(diff_min)):
#                             diff_min = lineid - int(g_mention_line_start)
#                             found = 1
#
#                 # print(ene_cat, g_attr, diff_min, grow)
#                 out_raw_list.append([ene_cat, g_attr, diff_min])
#                 if not diff_dic.get(g_cat_attr):
#                     diff_dic[g_cat_attr] = []
#                 #diff_dic[g_cat_attr].append(diff_min)
#                 diff_dic[g_cat_attr].append(base + diff_min)
#
#
# df = pd.DataFrame(out_raw_list, columns=['cat', 'attr', 'diff_min'])
# df.to_csv(out_raw, sep='\t',  index=False)
#
#
# interval_list = []
# for cat_attr in diff_dic:
#     (cat, attr) = re.split(':', cat_attr)
#
#     print(cat_attr, diff_dic[cat_attr])
#     # 標本サイズ
#     n = len(diff_dic[cat_attr])
#     # 自由度
#     k = n -1
#     # 平均
#     m = np.mean(diff_dic[cat_attr])
#     # 不偏分散
#     s2 = np.var(diff_dic[cat_attr], ddof=1)
#     # 標準誤差
#     se = np.sqrt(s2 / n)
#     # 信頼区間
#     lo, up = t.interval(conf, k, m, se)
#
#     # 別解
#     tvalue = t.ppf((1+conf)/2, (n-1))
#     t_lo = m - tvalue * se
#     t_up = m + tvalue * se
#
#     lo_mod = 0
#     up_mod = 0
#     if np.isnan(lo):
#         lo_mod = 0
#     else:
#         lo_mod = lo -base
#     if np.isnan(up):
#         up_mod = 0
#     else:
#         up_mod = up - base
#
#     print(cat_attr, 'n', n, 'm', m, 's2', s2, 'se', se, 'lo_mod', lo_mod, 'lo', lo, 't_lo', t_lo,  'up_mod', up_mod, 'up', up, 't_up', t_up)
#     # interval_list.append([cat, attr, n, lo_mod, up_mod])
#     interval_list.append([cat, attr, n, lo_mod, up_mod])
# i_df = pd.DataFrame(interval_list, columns=['cat', 'attr', 'size', 'pre', 'next'])
# i_df.to_csv(out_interval, sep='\t', index=False)





