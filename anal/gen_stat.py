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
# import linkjpc.linkjpc_prep as ljcp

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


metrics = 'f1'
base_dir= '/Users/masako/Documents/SHINRA/2021-LinkJP/'
sys_all_score_dir = base_dir + 'test_out/exp_systems/anal/'
sys_all_score = sys_all_score_dir + 'sys_score_all.tsv'
# sys_all_score_stat_var = sys_all_score_dir + 'sys_score_all_stat_var_' + metrics + '.tsv'
sys_all_score_stat_desc = sys_all_score_dir + 'sys_score_all_stat_desc_' + metrics + '.tsv'
sys_all_score_stat_desc_sl = sys_all_score_dir + 'sys_score_all_stat_desc_sl' + metrics + '.tsv'


test_gold_dir = base_dir + 'Download/linkjp-eval-211027/link_annotation/'
test_self_link_info_file = base_dir + 'anal/stats_testdata/test_self_link_info.tsv'


def main():
    log_info = LogInfo()
    logger = set_logging(log_info, 'myAnalLogger')
    logger.setLevel(logging.INFO)

    # self_link
    with open(test_self_link_info_file, 'w', encoding='utf-8') as slw:
        # selflink ratio
        gen_self_link_info(test_gold_dir, test_self_link_info_file, log_info)

    with open(test_self_link_info_file, 'r', encoding='utf-8') as slr:
        df_sl = pd.read_csv(test_self_link_info_file, delimiter='\t', names=('cat', 'att', 'sl'))
        print(df_sl)
    # var, std
    with open(sys_all_score,'r', encoding='utf-8') as f, open(sys_all_score_stat_desc, 'w', encoding='utf-8') as d:
        df = pd.read_csv(sys_all_score, delimiter='\t', names=('sys', 'cat', 'att', 'f1', 'prec', 'rec'))
        #print(df)

        att_grouped = df.groupby(['cat','att'])
        #var_f1 = [float(Decimal(i).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)) ** 2 for i in att_grouped.var()['f1']]

        # var_f1 = att_grouped.var()['f1']
        # std_f1 = att_grouped.std()['f1']
        #std_f1 = [float(Decimal(i).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)) ** 2 for i in att_grouped.desc()['f1']]
        desc_f1 = att_grouped.describe()['f1']

        df_d = pd.DataFrame(desc_f1)
        df_d.to_csv(sys_all_score_stat_desc, sep='\t')
        # df_s = pd.DataFrame(std_f1)
        # df_s.to_csv(sys_all_score_stat_std, sep='\t')
        print(df_d)

    df_all = pd.merge(df_sl, df_d, on=['cat', 'att'], how='outer')
    df_all.to_csv(sys_all_score_stat_desc_sl, sep='\t')

# logger以外はlinkjpc_prepと同じ
def gen_self_link_info(gold_dir, self_link_info_file, log_info):
    """Generate self link info
    args:
        gold_dir
        self_link_info_file:
        log_info:
    return:
    output:
        self_link_info_file
    Note:
        gold file
            Gold files (eg. sample gold files) used for self link estimation should be located in gold_dir.
            sample
                3623607	下半山村	合併市区町村	三間ノ川村	61	39	61	44	29489	高岡郡
                3623607	下半山村	合併市区町村	三間ノ川村	61	39	61	44	3623607	下半山村
    """
    import logging
    from glob import glob
    import pandas as pd
    import re
    import csv

    logger = set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)
    logger.info({
        'action': 'ljc_prep_main',
        'start': 'gen_self_link_info',
        'gold_dir': gold_dir,
        'self_link_info_file': self_link_info_file
    })
    prt_list = []
    ext = '.tsv'

    gold = gold_dir + '*.tsv'

    sumup_cat_attr = {}
    sumup_self_cat_attr = {}

    for g_fname in glob(gold):
        cat = get_category(g_fname, gold_dir, ext, log_info)
        logger.info({
            'action': 'gen_self_link_info',
            'cat': cat,
            'g_fname': g_fname
        })
        check_gold = {}
        check_self_gold = {}

        with open(g_fname, mode='r', encoding='utf-8') as f:
            greader = csv.reader(f, delimiter='\t')

            for grow in greader:
                gold_key = '\t'.join(grow[0:8])
                if not check_gold.get(gold_key):
                    check_gold[gold_key] = 1

                # self-link
                if check_self(grow, log_info):
                    if not check_self_gold.get(gold_key):
                        check_self_gold[gold_key] = 1
                    else:
                        check_self_gold[gold_key] += 1

        for common_key in check_gold:
            common_key_list = re.split('\t', common_key)
            cat_attr = cat + '\t' + common_key_list[2]

            if not sumup_cat_attr.get(cat_attr):
                sumup_cat_attr[cat_attr] = check_gold[common_key]
            else:
                sumup_cat_attr[cat_attr] += check_gold[common_key]

            if check_self_gold.get(common_key):
                if not sumup_self_cat_attr.get(cat_attr):
                    sumup_self_cat_attr[cat_attr] = check_self_gold[common_key]
                else:
                    sumup_self_cat_attr[cat_attr] += check_self_gold[common_key]

    for t_cat_attr in sumup_cat_attr:
        (t_cat, t_attr) = re.split('\t', t_cat_attr)
        if sumup_self_cat_attr.get(t_cat_attr):
            t_ratio_str = sumup_self_cat_attr[t_cat_attr] / sumup_cat_attr[t_cat_attr]
            t_ratio = float(Decimal(t_ratio_str).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
        else:
            t_ratio = 0.0

        prt_list.append([t_cat, t_attr, t_ratio])

    sdf = pd.DataFrame(prt_list, columns=['cat', 'attr', 'ratio'])
    sdf.to_csv(self_link_info_file, sep='\t', header=False, index=False)

def check_self(row, log_info):
    """check if self-link
    :param row:
    :param log_info:
    :return: 1 (self), 0 (non-self)
    """
    import logging
    logger = set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)

    if row[0] == row[8]:
        return 1
    else:
        return 0

def get_category(fname, dname, ext, log_info):
    """ get category label from the file name
    :param fname:
    :param dname:
    :param ext:
    :param log_info
    :return: cat
    """
    import logging
    logger = set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)

    cat_pre = fname.replace(dname, '')
    cat_new = cat_pre.replace(ext, '')
    return cat_new


if __name__ == '__main__':
    main()