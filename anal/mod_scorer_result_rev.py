import pandas as pd
import logging
import sys
import csv

#scorerの出力からの変更
# カテゴリ名は先頭大文字にする
# テストデータの属性の正解リンクありの頻度を出力する場合は　set_att_freq = 1  とする

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



# scorerの出力ファイルの親ディレクトリ
org_score_dir = sys.argv[1]
# "/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/exp_systems/score/"

# 評価対象のシステムリストとスコアをまとめた出力ファイルを置くディレクトリ
anal_target_dir = sys.argv[2]
# /Users/masako/Documents/SHINRA/2021-LinkJP/test_out/exp_systems/anal/

anal_target_list = sys.argv[3]
# anal_target_list="${anal_target_dir}anal_target.txt"

set_att_freq = sys.argv[4]


# カテゴリの属性別システムスコアをまとめた出力ファイル
score_file_name = 'sys_score_all.tsv'
score_all_file = anal_target_dir + score_file_name

# カテゴリのmicro averageをまとめた出力ファイル
score_ma_file_name = 'sys_score_ma_all.tsv'
score_ma_all_file = anal_target_dir + score_ma_file_name

logger.info({
    'action': 'mod_scorer_result_rev',
    'anal_target': anal_target_dir,
    'anal_target_list': anal_target_list
})
org_ext = '_score.txt'
new_ext = '_score.tsv'
sys_all_list = []
sys_all_ma_list = []

cat_list = ['Airport', 'City', 'Company', 'Compound', 'Conference', 'Lake', 'Person']
# カテゴリ別スコアシートでは単に指標の値が0になるだけで正解リンクなしかどうか判定できない
del_att_list_city = ['国内位置']
del_att_list_company = ['業界内地位・規模','コーポレートスローガン']
del_att_list_conference = ['賞','地位・規模','名前の謂れ']

#テストデータの属性の正解リンクありの頻度
base_dir= '/Users/masako/Documents/SHINRA/2021-LinkJP/'
mention_with_link = base_dir + 'anal/stats_testdata/test_att_freq_all.txt'

cnt_cat_attr = {}
if set_att_freq:
    with open(mention_with_link, 'r', encoding='utf-8') as mwl:
        mreader = csv.reader(mwl, delimiter='\t')
        for mline in mreader:
            cat = mline[0]
            attr = mline[1]
            freq_str = mline[4].rstrip('\n')

            c_a = cat + '_' + attr

            # 頻度が0の場合は登録しない　分母が0になるため
            if int(freq_str) != 0:
                cnt_cat_attr[c_a] = freq_str
                print(c_a, cnt_cat_attr[c_a])


with open(anal_target_list, mode='r', encoding='utf-8') as ef:
    for sys_pre in ef:
        sys = sys_pre.rstrip()
        logger.info({
            'action': 'mod_scorer_result_rev',
            'sys': sys
        })

        for cat in cat_list:
            score_file = org_score_dir + sys + '/' + cat + org_ext
            logger.info({
                'action': 'mod_scorer_result_rev',
                'score_file': score_file
            })
            with open(score_file, mode='r', encoding='utf-8') as f:
                tmp_file_full = score_file
                for line_pre in f:
                    line = line_pre.rstrip()
                    logger.info({
                        'action': 'mod_scorer_result_rev',
                        'line': line
                    })

                    (cat, prec, recall, f1, attribute) = line.split()
                    logger.info({
                        'action': 'mod_scorer_result_rev',
                        'cat': cat,
                        'f1': f1,
                    })

                    if 'macro-average' in line or 'attribute' in line:
                        continue
                    elif 'micro-average' in line:
                        sys_all_ma_list.append([sys, cat, f1, prec, recall])
                    else:
                        check_del = 0
                        if cat == 'City':
                            for city_att in del_att_list_city:
                                if attribute == city_att:
                                    check_del = 1
                                    logger.info({
                                        'action': 'mod_scorer_result.py',
                                        'cat': cat,
                                        'attribute': attribute,
                                        'city_att': city_att
                                    })
                                    break
                        elif cat == 'Company':
                            for company_att in del_att_list_company:
                                if attribute == company_att:
                                    check_del = 1
                                    logger.info({
                                        'action': 'mod_scorer_result.py',
                                        'cat': cat,
                                        'attribute': attribute,
                                        'company_att': company_att
                                    })
                                    break
                        elif cat == 'Conference':
                            for conference_att in del_att_list_conference:
                                if attribute == conference_att:
                                    check_del = 1
                                    logger.info({
                                        'action': 'mod_scorer_result.py',
                                        'cat': cat,
                                        'attribute': attribute,
                                        'conference_att': conference_att
                                    })
                                    break
                        if check_del:
                            logger.info({
                                'action': 'mod_scorer_result.py',
                                'check_del': check_del,
                                'attribute': attribute,
                            })
                            continue
                        else:

                            ca = cat + '_' + attribute
                            # att_new = attribute + ':' + cnt_cat_attr[ca]
                            att_freq = attribute + ':' + cnt_cat_attr[ca]
                            freq = int(cnt_cat_attr[ca])

                            sys_all_list.append([sys, cat, att_freq, attribute, freq, f1, prec, recall])

                            # if set_att_freq:
                            #     ca = cat + '_' + attribute
                            #     # att_new = attribute + ':' + cnt_cat_attr[ca]
                            #     att_new = cnt_cat_attr[ca] + ':' + attribute
                            #
                            #     sys_all_list.append([sys, cat, att_new, cnt_cat_attr[ca], f1, prec, recall])
                            #
                            #     sys_all_list.append([sys, cat, att_new, f1, prec, recall])
                            # else:
                            #     sys_all_list.append([sys, cat, attribute, f1, prec, recall])

df_pp = pd.DataFrame(sys_all_list, columns=['sys', 'cat', 'att_freq', 'attribute', 'freq', 'f1', 'prec', 'recall'])
df_p = df_pp.sort_values('freq', ascending=False)
print(df_p)
if set_att_freq:
    df = df_p.drop(columns=['attribute','freq'])
else:
    df = df_p.drop(columns=['att_freq','freq'])

# df['cat'] = df['cat'].map({'airport': 'Airport',
#                            'city': 'City',
#                            'company': 'Company',
#                            'compound': 'Compound',
#                            'conference': 'Conference',
#                            'lake': 'Lake',
#                            'person': 'Person'
#                            },
#                           na_action=None)

df.to_csv(score_all_file, sep='\t', index=False, header=False)

mdf = pd.DataFrame(sys_all_ma_list)
mdf.to_csv(score_ma_all_file, sep='\t', index=False, header=False)



