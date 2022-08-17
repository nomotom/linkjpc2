from glob import glob
import re
import pandas as pd
import sys
import logging
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


log_info = LogInfo()
logger = set_logging(log_info, 'myAnalLogger')
logger.setLevel(logging.INFO)

# 設定が必要なもの > 引数
# anal, tmp_target_key, score_dir_base

# (1) 入力ファイルの親ディレクトリ （スコアラーの出力）
score_dir_base = sys.argv[1]
#score_dir_base = "/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/anal_20211009/"
target_dir_base = score_dir_base + 'eval/'

# (2)評価方法
anal = sys.argv[2]
#anal = '1_module'

# (3) 評価対象分類

# 評価対象分類
tmp_target_key = sys.argv[3]
# target_precision_key="top_precision"
# target_recall_key="top_recall"
# target_f1_key="top_f1"
# tmp_target_key = target_recall_key


#scorerの出力 （この下のシステムディレクトリの下にCategory_score.txt)
eval_target = target_dir_base + anal + '_' + tmp_target_key + '/'
# eval_target = sys.argv[3]
# eval_target_fname = sys.argv[4]

# システムリスト
eval_target_list = eval_target + 'target.txt'

logger.debug({
    'action': 'mod_scorer_result',
    'eval_target': eval_target,
    'eval_target_list': eval_target_list
})



#(4) 出力ファイル
#
#
# target = anal + '_' +  tmp_target_key
# 出力ファイル
#score_all_file =  eval_target + score_file_name
score_all_file =  eval_target + 'sys_score_all.tsv'

#


####

# score_file_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/final_rev4/*/" + anal + "/*_score.txt"
#####
#common_dir = '/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/'
#target_file = 'scorer_target_' + target

#####
org_ext = '_score.txt'
new_ext = '_score.tsv'
sys_all_list = []
cat_list = ['Airport', 'City', 'Company', 'Compound', 'Conference', 'Lake', 'Person']
del_att_list_city = ['国内位置']
del_att_list_company = ['業界内地位・規模','コーポレートスローガン']
del_att_list_conference = ['賞','地位・規模','名前の謂れ']

#with open(eval_target_list, mode='r', encoding='utf-8') as tf:
    #for tline in tf:
        #target_system = tline.rstrip('\n')

with open(eval_target_list, mode='r', encoding='utf-8') as ef:
    for sys_pre in ef:
        sys = sys_pre.rstrip()
        print('sys', sys)
        for cat in cat_list:
            score_file = eval_target + sys + '/' + cat + org_ext
            print('score_file', score_file)

            with open(score_file, mode='r', encoding='utf-8') as f:
                tmp_file_full = score_file
                #
                # tmp_file_mod = tmp_file_full.replace(target_dir_base, '')
                # replace_str = anal + '/'
                # pre = tmp_file_mod.replace(replace_str, '')
                # (sys, fname) = re.split('/', pre)
                # print('sys', sys)

                for line_pre in f:
                    line = line_pre.rstrip()
                    print('line', line)
                    if 'micro-average' in line or 'macro-average' in line or 'precision' in line:
                        continue
                    (cat, prec, recall, f1, attribute) = line.split()
                    logger.info({
                        'action': 'mod_scorer_result.py',
                        'f1': f1,
                    })
                    if '\-' in f1:
                        logger.info({
                            'action': 'mod_scorer_result.py',
                            'skipped': 1,
                            'attribute': attribute,
                        })
                        continue
                    else:
                        sys_all_list.append([sys, cat, attribute, f1, prec, recall])
                    # check_del = 0
                    # if cat == 'city':
                    #     for city_att in del_att_list_city:
                    #         logger.info({
                    #             'action': 'mod_scorer_result.py',
                    #             'cat': cat,
                    #             'attribute': attribute,
                    #             'city_att': city_att
                    #         })
                    #         print(cat, attribute, city_att)
                    #         if attribute == city_att:
                    #             check_del = 1
                    #             break
                    # elif cat == 'company':
                    #     for company_att in del_att_list_company:
                    #         logger.debug({
                    #             'action': 'mod_scorer_result.py',
                    #             'cat': cat,
                    #             'attribute': attribute,
                    #             'company_att': company_att
                    #         })
                    #         if attribute == company_att:
                    #             check_del = 1
                    #             break
                    # elif cat == 'conference':
                    #     for conference_att in del_att_list_conference:
                    #         logger.debug({
                    #             'action': 'mod_scorer_result.py',
                    #             'cat': cat,
                    #             'attribute': attribute,
                    #             'conference_att': conference_att
                    #         })
                    #         if attribute == conference_att:
                    #             check_del = 1
                    #             break
                    # if check_del:
                    #     logger.debug({
                    #         'action': 'mod_scorer_result.py',
                    #         'check_del': check_del,
                    #         'attribute': attribute,
                    #     })
                    #     continue
                    # else:
                    #     sys_all_list.append([sys, cat, attribute, f1, prec, recall])

df = pd.DataFrame(sys_all_list)
#df.to_csv(score_all_file, sep='\t', header=False, index=False)
df.to_csv(score_all_file, sep='\t', index=False)




