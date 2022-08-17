'''
    output:
        self_link_info_file
        sys_all_score_stat_var
        sys_all_score_stat_std
    note: sys_all_score
        sample:
            AIPCB_CBI       airport 別名    0.136   0.806   0.074
            AIPCB_CBI       airport 旧称    0.348   0.727   0.229
            ...
            AIPRB_WSM       city    別名    0.992   0.992   0.992
        sel        AIPRB_WSM       city    旧称    0.809   0.809   0.809
'''
import logging
import numpy as np
import pandas as pd
from matplotlib import pyplot
from decimal import Decimal, ROUND_HALF_UP
from ..linkjpc import linkjpc_prep as ljcp

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

metrics = 'f1'
base_dir= '/Users/masako/Documents/SHINRA/2021-LinkJP/'
sys_all_score_dir = base_dir + 'test_out/exp_systems/anal/'
sys_all_score = sys_all_score_dir + 'sys_score_all.tsv'
sys_all_score_stat_desc = sys_all_score_dir + 'sys_score_all_stat_desc_' + metrics + '.tsv'

test_gold_dir = base_dir + 'Download/linkjp-eval-211027/link_annotation/'
test_self_link_info_file = base_dir + 'anal/stats_testdata/test_self_link_info.tsv'

sys_all_tp = sys_all_score_dir + 'sys_all_tp.tsv'


# self_link
with open(test_self_link_info_file, 'r', encoding='utf-8') as sl:
    # selflink ratio
    sdf = pd.read_csv(test_self_link_info_file, delimiter='\t', names=('cat', 'att', 'ratio'))
    logger.info({
        'action': 'anal_stat',
        'sdf': sdf
    })

# var, std
with open(sys_all_score_stat_desc, 'r', encoding='utf-8') as d:
    ddf = pd.read_csv(sys_all_score_stat_desc, delimiter='\t', names=('cat', 'att', 'var'))
    print(ddf)

    att_grouped = ddf.groupby(['cat','att'])

    desc_f1 = att_grouped.desc()['f1']
    # std_f1 = att_grouped.std()['f1']
    std_f1 = [float(Decimal(i).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)) ** 2 for i in att_grouped.std()['f1']]

    df_v = pd.DataFrame(desc_f1)
    df_v.to_csv(sys_all_score_stat_desc, sep='\t')





