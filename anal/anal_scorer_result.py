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


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from decimal import Decimal, ROUND_HALF_UP
import os
import sys
import re
import logging
# import evaluation_linkjp as el


log_info = LogInfo()
logger = set_logging(log_info, 'myAnalLogger')
logger.setLevel(logging.INFO)

###
#python ${script_anal_scorer_result} ${score_dir_base} ${anal} ${tmp_target_key} ${scatter_out} ${heatmap_out}

# 都度設定　linkjpc_scorer_test.sh, mod_scorer_resultも合わせて修正すること
# scatter_out or heatmap_out
# tmp_target_key
# score_dir_base
###
# print ('0', sys.argv[0])
score_dir_base = sys.argv[1]
anal = sys.argv[2]
tmp_target_key = sys.argv[3]
scatter_out = sys.argv[4]
heatmap_out = sys.argv[5]
x_rotation = sys.argv[6]
x_rotation_list = re.split(',', x_rotation)

logger.info({
    'action': 'anal_scorer_result',
    'score_dir_base': score_dir_base,
    'anal': anal,
    'tmp_target_key': tmp_target_key,
    'scatter_out': scatter_out,
    'heatmap_out': heatmap_out,
    'x_rotation': x_rotation
})


# print('type(x_rotation)', type(x_rotation), x_rotation)

# anal = '1_module'
# target_precision_key="top_precision"
# target_recall_key="top_recall"
# target_f1_key="top_f1"
# tmp_target_key = target_recall_key


target = anal + '_' + tmp_target_key

# score_dir_base = '/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/anal_20211009/'
###

score_all_file = 'sys_score_all.tsv'
score_ma_all_file = 'sys_score_ma_all.tsv'

target_dir_base = score_dir_base + 'eval/'
eval_target = target_dir_base + anal + '_' + tmp_target_key + '/'

infile = eval_target + score_all_file
ma_infile = eval_target + score_ma_all_file

out_dir = eval_target
try:
    os.makedirs(out_dir)
except FileExistsError:
    pass
pid = os.getpid()
stat_file = out_dir + 'stat_' + str(pid) + '.tsv'
ma_stat_file = out_dir + 'ma_stat_' + str(pid) + '.tsv'


print_list = []
cat_list = ['airport', 'city', 'company', 'compound', 'conference', 'lake', 'person']
metrics_list = ['f1', 'prec', 'rec']
df = pd.read_csv(infile, delimiter='\t', names= ('sys', 'cat', 'attribute', 'f1', 'prec', 'rec'))

# print(df)
# print(df.count())

# 対象外のscoreを削除
# ndf = df[~(df['f1'].isin(['-']))]

logger.info({
    'action': 'anal_scorer_res',
    'df': df,
    'df.count()': df.count()
})

grouped = df.groupby('cat')
for met in metrics_list:
    logger.info({
        'action': 'anal_scorer_res',
        'met': met,
        #'grouped.describe()[met]': grouped.describe()[met]
    })

df_airport = grouped.get_group('airport')
df_lake = grouped.get_group('lake')
df_city = grouped.get_group('city')
df_company = grouped.get_group('company')
df_compound = grouped.get_group('compound')
df_conference = grouped.get_group('conference')
df_person = grouped.get_group('person')
df_list = [df_airport, df_city, df_company, df_compound, df_conference, df_lake, df_person]
cat_df_list = [['airport', df_airport],
               ['city', df_city],
               ['company', df_company],
               ['compound', df_compound],
               ['conference', df_conference],
               ['lake', df_lake],
               ['person', df_person]]

sns.set(style='darkgrid')

for cat_df in cat_df_list:
    # print('+++++++++\ncat_df', cat_df)
    # print('type(cat_df)', type(cat_df))
    cat = cat_df[0]
    # print('cat_df[0]',cat_df[0] )
    tmp_df = cat_df[1]

    logger.debug({
        'action': 'anal_scorer_result',
        'cat_df': cat_df,
        'cat_df[0]': cat_df[0],
        'duplicate': tmp_df.duplicated(),
        'tmp_df': tmp_df
    })
    for met in metrics_list:
        gtitle = cat + ':' + met

        if scatter_out == 'Y':
            sname = out_dir + 'scatter/' + cat + '_scatter_' + met + '.png'
            try:
                os.makedirs(out_dir + 'scatter/')
            except FileExistsError:
                pass
            sns.relplot(x='att', y=met, data=tmp_df, hue='sys', height=20, aspect=1).set(title=gtitle)
            # p = sns.relplot(data=tmp_df)
            # p.set_xlabel('att', fontsize = 8)
            # p.set_ylabel(met, fontsize = 10)
            # p.set_title(gtitle, fontsize = 10)

            plt.savefig(sname)

        if heatmap_out == 'Y':
            hname = out_dir + 'heatmap/' + cat + '_heatmap_' + met + '.png'
            try:
                os.makedirs(out_dir + 'heatmap/')
            except FileExistsError:
                pass

            tmp_df_heat = tmp_df.pivot('attribute', 'sys', met)
            logger.debug({
                'action': 'anal_scorer_result',
                'tmp_df_heat': tmp_df_heat
            })
            print('tmp_df_heat', tmp_df_heat)
            sns.heatmap(tmp_df_heat, annot=True, fmt=".2f", cmap="Blues", cbar=False).set(title=gtitle)
            #sns.heatmap(tmp_df_heat, annot=True, fmt="1.1f", cmap="Blues").set(title=gtitle)
            #plt.show()
            # x軸のラベルはxticklabelsで設定
            # rotation
            rotation = 0
            for keyword in x_rotation_list:
                # print('keyword, out_dir', keyword, out_dir)
                if keyword in out_dir:
                    rotation = 1
                    break
            if rotation:
                plt.xticks(rotation=30)
            plt.yticks(fontsize=10)

            #ax = sns.barplot(x='sys', y='attribute', data=tmp_df_heat)
            #plt.yticks(rotation=30)

            # y軸のラベルは属性名
            # y軸のラベルが切れるのを防ぐ
            # bbox_inches, pad_inches
            # カラーバーを表示しない場合　
            # sns.heatmap(flights, cbar=False)
            plt.savefig(hname,bbox_inches='tight', pad_inches=0)
            # plt.close('all')

df_new = pd.DataFrame(print_list)
df_new.to_csv(stat_file, sep='\t', header=False, index=False)
# fontを格納するフォルダを調べる
# font_names = matplotlib.matplotlib_fname()
# print(font_names)
# IPAフォントの入れ方はMatplot lib 実装ハンドブック参照
# cashファイルのあるフォルダを調べる
#print(matplotlib.get_configdir())
# fontList.json
# フォントを調べる
#print(matplotlib.rcParams['font.family'])
#seabornはrcmod.pyの修正も必要

mdf = pd.read_csv(ma_infile, delimiter='\t', names= ('sys', 'cat', 'f1', 'prec', 'rec'))

# print(mdf)
# print(mdf.count())

# 対象外のscoreを削除
# nmdf = mdf[~(mdf['f1'].isin(['-']))]

logger.info({
    'action': 'anal_scorer_res',
    'mdf': mdf,
    'mdf.count()': mdf.count()
})

# # m_grouped = mdf.groupby('attribute')
# # logger.info({
# #    'action': 'anal_scorer_res',
# #    'm_grouped': m_grouped,
# #})
# # mdf_micro_average = m_grouped.get_group('micro-average')
# # mdf_lake = m_grouped.get_group('lake')
# # mdf_city = m_grouped.get_group('city')
# # mdf_company = m_grouped.get_group('company')
# # mdf_compound = m_grouped.get_group('compound')
# # mdf_conference = m_grouped.get_group('conference')
# # mdf_person = m_grouped.get_group('person')
# #mdf_list = [mdf_airport, mdf_city, mdf_company, mdf_compound, mdf_conference, mdf_lake, mdf_person]
#
# # mdf_list = [mdf_airport, mdf_city, mdf_company, mdf_compound, mdf_conference, mdf_lake, mdf_person]
# # mdf_list = [mdf_micro_average]
# #att_mdf = mdf['attribute']
# att = 'micro-average'
# # cat_mdf_list = [['airport', mdf_airport],
# #                ['city', mdf_city],
# #                ['company', mdf_company],
# #                ['compound', mdf_compound],
# #                ['conference', mdf_conference],
# #                ['lake', mdf_lake],
# #                ['person', mdf_person]]
#
# sns.set(style='darkgrid')
# #att = att_mdf[0]
# # print('att_mdf[0]',att_mdf[0] )
# # tmp_mdf = att_mdf[1]
#
# logger.debug({
#     'action': 'anal_scorer_result',
#     # 'att_mdf': att_mdf,
#     'att': att,
#     'mdf': mdf
# })
# for met in metrics_list:
#     ctitle = att + ':' + met
#
#     if scatter_out == 'Y':
#         msname = out_dir + 'scatter/' + att + '_scatter_' + met + '.png'
#         try:
#             os.makedirs(out_dir + 'scatter/')
#         except FileExistsError:
#             pass
#         sns.relplot(x='att', y=met, data=mdf, hue='sys', height=20, aspect=1).set(title=ctitle)
#         # p = sns.relplot(data=tmp_mdf)
#         # p.set_xlabel('att', fontsize = 8)
#         # p.set_ylabel(met, fontsize = 10)
#         # p.set_title(gtitle, fontsize = 10)
#
#         plt.savefig(msname)
#
#     if heatmap_out == 'Y':
#         mhname = out_dir + 'heatmap/' + att + '_heatmap_' + met + '.png'
#         try:
#             os.makedirs(out_dir + 'heatmap/')
#         except FileExistsError:
#             pass
#
#         tmp_mdf_heat = mdf.pivot('cat', 'sys', met)
#         logger.debug({
#             'action': 'anal_scorer_result',
#             'tmp_mdf_heat': tmp_mdf_heat
#         })
#         sns.heatmap(tmp_mdf_heat, annot=True, fmt=".2f", cmap="Blues", cbar=False).set(title=ctitle)
#         #sns.heatmap(tmp_mdf_heat, annot=True, fmt="1.1f", cmap="Blues").set(title=gtitle)
#         #plt.show()
#         # x軸のラベルはxticklabelsで設定
#         # rotation
#         rotation = 0
#         for keyword in x_rotation_list:
#             # print('keyword, out_dir', keyword, out_dir)
#             if keyword in out_dir:
#                 rotation = 1
#                 break
#         if rotation:
#             plt.xticks(rotation=30)
#         plt.yticks(fontsize=10)
#
#         #ax = sns.barplot(x='sys', y='attribute', data=tmp_mdf_heat)
#         #plt.yticks(rotation=30)
#
#         # y軸のラベルは属性名
#         # y軸のラベルが切れるのを防ぐ
#         # bbox_inches, pad_inches
#         # カラーバーを表示しない場合　
#         # sns.heatmap(flights, cbar=False)
#         plt.savefig(mhname,bbox_inches='tight', pad_inches=0)
#         plt.close('all')
#
# mdf_new = pd.DataFrame(print_list)
# mdf_new.to_csv(ma_stat_file, sep='\t', header=False, index=False)
# # fontを格納するフォルダを調べる
# # font_names = matplotlib.matplotlib_fname()
# # print(font_names)
# # IPAフォントの入れ方はMatplot lib 実装ハンドブック参照
# # cashファイルのあるフォルダを調べる
# #print(matplotlib.get_configdir())
# # fontList.json
# # フォントを調べる
# #print(matplotlib.rcParams['font.family'])
# #seabornはrcmod.pyの修正も必要
