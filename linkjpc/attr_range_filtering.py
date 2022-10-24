import linkjpc as ljc
import ljc_common as lc
import config as cf
import logging


def filter_by_attr_range(module_cand_list, mention_info, opt_info, log_info, **d_cat_attr2eneid_prob):

    """Filter candidate pages to be linked by attribute range.
    Args:
        module_cand_list:
        mention_info:
        opt_info
        log_info
        **d_cat_attr2eneid_prob:
    Returns:
        new_module_cand_list:
    """
    from decimal import Decimal, ROUND_HALF_UP
    import re
    import sys
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)

    new_module_cand_list = []

    if len(module_cand_list) > 0:
        for cand_info in module_cand_list:
            pid = cand_info[0]
            mod = cand_info[1]
            if not mod:
                logger.error({
                    'action': 'filter_by_attr_range',
                    'error': 'mod is empty',
                    'cand_info missing mod': cand_info,
                })
                sys.exit()
            val = cand_info[2]
            attr = mention_info.attr_label
            cat = mention_info.ene_cat

            cat_attr = cat + '__' + attr
            attr_co = 1.0
            attr_ok_co = opt_info.attr_ok_co
            attr_ng_co = opt_info.attr_ng_co
            attr_na_co = opt_info.attr_na_co

            if cat_attr not in d_cat_attr2eneid_prob:
                if cf.d_pid2eneid.get(pid):
                    cand_eneid = cf.d_pid2eneid[pid]
            else:
                ans_eneid_prob_list = d_cat_attr2eneid_prob[cat_attr]
                attr_co_cand = []

                if not cf.d_pid2eneid.get(pid):
                    tmp_attr_co = attr_na_co
                    attr_co_cand.append(tmp_attr_co)
                else:
                    tmp_eneid = cf.d_pid2eneid[pid]
                    tmp_eneid_split = []
                    tmp_eneid_split = re.split('\.', tmp_eneid)

                    for ans_eneid_prob in ans_eneid_prob_list:
                        ans_eneid = ans_eneid_prob[0]
                        ans_prob = ans_eneid_prob[1]

                        ans_prob_float = float(ans_prob)
                        ans_eneid_split = []
                        ans_eneid_split = re.split('\.', ans_eneid)
                        par_cnt = 0
                        tmp_attr_co = 0
                        for i in range(0, len(ans_eneid_split)):
                            if ans_eneid_split[i] == tmp_eneid_split[i]:
                                if ((i != 0) or (ans_eneid_split[i] != opt_info.eneid_ignore)
                                        or ('a' not in opt_info.attr_len)):
                                    par_cnt += 1
                            else:
                                break
                        if par_cnt > 0:
                            ans_depth = 0
                            if opt_info.attr_len == 'a':
                                if ans_eneid_split[0] == opt_info.eneid_ignore:
                                    tmp_ratio = par_cnt / (len(ans_eneid_split) - 1)
                                    tmp_attr_co_str = str(tmp_ratio * attr_ok_co * ans_prob_float)
                                else:
                                    tmp_ratio = par_cnt / len(ans_eneid_split)
                                    tmp_attr_co_str = str(tmp_ratio * attr_ok_co * ans_prob_float)
                            elif opt_info.attr_len == 'r':
                                ans_depth = len(ans_eneid_split)/opt_info.attr_len_max
                                tmp_ratio = par_cnt / len(ans_eneid_split)
                                tmp_attr_co_str = str(tmp_ratio * ans_depth * attr_ok_co * ans_prob_float)
                            elif opt_info.attr_len == 'ar':
                                if ans_eneid_split[0] == opt_info.eneid_ignore:
                                    ans_depth = (len(ans_eneid_split) - 1) / (opt_info.attr_len_max - 1)
                                    tmp_ratio = par_cnt / (len(ans_eneid_split) - 1)
                                    tmp_attr_co_str = str(tmp_ratio * ans_depth * attr_ok_co * ans_prob_float)
                                else:
                                    tmp_attr_co_str = str((par_cnt/len(ans_eneid_split)) * attr_ok_co * ans_prob_float)
                            elif opt_info.attr_len == 'am':
                                if ans_eneid_split[0] == opt_info.eneid_ignore:
                                    ans_depth = opt_info.attr_depth_base_default + \
                                            (1 - opt_info.attr_depth_base_default) \
                                            * ((len(ans_eneid_split) - 1) / (opt_info.attr_len_max - 1))
                                    tmp_ratio = par_cnt / (len(ans_eneid_split) - 1)
                                else:
                                    ans_depth = opt_info.attr_depth_base_default + \
                                                (1 - opt_info.attr_depth_base_default) \
                                                * (len(ans_eneid_split) / opt_info.attr_len_max)
                                    tmp_ratio = par_cnt / len(ans_eneid_split)
                                tmp_attr_co_str = str(tmp_ratio * ans_depth * attr_ok_co * ans_prob_float)
                            else:
                                tmp_attr_co_str = str((par_cnt/len(ans_eneid_split)) * attr_ok_co * ans_prob_float)

                            tmp_attr_co = float(Decimal(tmp_attr_co_str).quantize(Decimal('0.01'),
                                                                                  rounding=ROUND_HALF_UP))
                        else:
                            tmp_attr_co = attr_ng_co
                        attr_co_cand.append(tmp_attr_co)
                attr_co = max(attr_co_cand)

            new_val = attr_co * val
            new_module_cand_list.append([pid, mod, new_val])

    if len(new_module_cand_list) > 0:
        new_module_cand_list.sort(key=lambda x: x[2], reverse=True)

        if new_module_cand_list[0][2] > 1.0:
            logger.error({
                'action': 'filter_by_attr_range',
                'error': 'score max is more than 0'
            })
            sys.exit()
    return new_module_cand_list


def get_attr_range(attr_range_man_file, attr_range_auto_file, attr_range_merged_file, opt_info,
                   log_info, **d_cnv):
    """Get attribute range probability info that shows which ENE category the attribute values are likely to be
    classified into.
    Args:
        attr_range_man_file (str):
        attr_range_auto_file (str):
        attr_range_merged_file (str):
        # all_cat_file
        opt_info
        log_info
        **d_cnv
    Returns:
        d_cat_attr2eneid_prob: dictionary
    Note:
        d_cnv
            key: ene_id
            value: en_label
        attr_range_man_file
            (format)
                cat(\t)attribute_label(\t)eneid(\t)probability
            (sample)
                Person  国   1.5.1.3 1.0
                Person  国   1.5.1.0 0.5
        attr_range_auto_file
            (format)
                cat(\t)attribute_label(\t)eneid(\t)probability(\t)freq(\t)freq_cat_attr(\n)
            (sample)
                 City    産業    0   0.5     50      100
    """
    import re
    import csv
    import sys
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)

    m_cat_attr2eneid_prob = {}
    if 'm' in opt_info.attr_rng_type:
        with open(attr_range_man_file, 'r', encoding='utf-8') as m:
            m_reader = csv.reader(m, delimiter='\t')

            for m_cat_attr_range_prob in m_reader:
                eneid = m_cat_attr_range_prob[2]
                lc.check_dic_key(eneid, log_info, **d_cnv)
                cat = m_cat_attr_range_prob[0]
                attr = m_cat_attr_range_prob[1]
                prob = float(m_cat_attr_range_prob[4])

                cat_attr = cat + '__' + attr
                if not m_cat_attr2eneid_prob.get(cat_attr):
                    m_cat_attr2eneid_prob[cat_attr] = {}
                m_cat_attr2eneid_prob[cat_attr][eneid] = prob

    a_cat_attr2eneid_prob = {}
    if 'a' in opt_info.attr_rng_type:
        with open(attr_range_auto_file, 'r', encoding='utf-8') as a:
            a_reader = csv.reader(a, delimiter='\t')
            for a_cat_attr_range_prob in a_reader:
                eneid = a_cat_attr_range_prob[2]

                lc.check_dic_key(eneid, log_info, **d_cnv)
                cat = a_cat_attr_range_prob[0]

                attr = a_cat_attr_range_prob[1]
                prob = float(a_cat_attr_range_prob[4])
                freq = int(a_cat_attr_range_prob[5])

                if freq < opt_info.attr_rng_auto_freq_min_default:
                    continue

                cat_attr = cat + '__' + attr
                if not a_cat_attr2eneid_prob.get(cat_attr):
                    a_cat_attr2eneid_prob[cat_attr] = {}
                a_cat_attr2eneid_prob[cat_attr][eneid] = prob

    d_cat_attr2eneid_prob = {}
    if opt_info.attr_rng_type == 'a' or opt_info.attr_rng_type == 'am':
        for a_cat_attr in a_cat_attr2eneid_prob:
            for aid, aprob in a_cat_attr2eneid_prob[a_cat_attr].items():
                if a_cat_attr not in d_cat_attr2eneid_prob:
                    d_cat_attr2eneid_prob[a_cat_attr] = {}
                d_cat_attr2eneid_prob[a_cat_attr][aid] = aprob
        if opt_info.attr_rng_type == 'am':
            for m_cat_attr in m_cat_attr2eneid_prob:
                for mid, mprob in m_cat_attr2eneid_prob[m_cat_attr].items():
                    if m_cat_attr not in d_cat_attr2eneid_prob:
                        d_cat_attr2eneid_prob[m_cat_attr] = {}
                        d_cat_attr2eneid_prob[m_cat_attr][mid] = mprob
                    elif (mid not in d_cat_attr2eneid_prob[m_cat_attr]) or \
                            (d_cat_attr2eneid_prob[m_cat_attr][mid] == 0):
                        d_cat_attr2eneid_prob[m_cat_attr][mid] = mprob

    if opt_info.attr_rng_type == 'm' or opt_info.attr_rng_type == 'ma':
        for h_cat_attr in m_cat_attr2eneid_prob:
            for hid, hprob in m_cat_attr2eneid_prob[h_cat_attr].items():
                if h_cat_attr not in d_cat_attr2eneid_prob:
                    d_cat_attr2eneid_prob[h_cat_attr] = {}
                d_cat_attr2eneid_prob[h_cat_attr][hid] = hprob
        if opt_info.attr_rng_type == 'ma':
            for i_cat_attr in a_cat_attr2eneid_prob:
                for iid, iprob in a_cat_attr2eneid_prob[i_cat_attr].items():
                    if i_cat_attr not in d_cat_attr2eneid_prob:
                        d_cat_attr2eneid_prob[i_cat_attr] = {}
                        d_cat_attr2eneid_prob[i_cat_attr][iid] = iprob
                    elif (iid not in d_cat_attr2eneid_prob[i_cat_attr]) or \
                            (d_cat_attr2eneid_prob[i_cat_attr][iid] == 0):
                        d_cat_attr2eneid_prob[i_cat_attr][iid] = iprob

    with open(attr_range_merged_file, mode='w', encoding='utf-8') as arm:
        writer = csv.writer(arm, delimiter='\t', lineterminator='\n')
        for ca in d_cat_attr2eneid_prob:
            for eid in d_cat_attr2eneid_prob[ca]:
                writer.writerow([ca, eid, d_cat_attr2eneid_prob[ca]])

    return d_cat_attr2eneid_prob


def reg_enew_info(enew_info, log_info):
    """Create a dictionary and store enew info.
    Args:
        enew_info
        log_info
    Returns:
        d_pid2eneid (dict)
    Note:
        enew_info
            ENEW info of pages extracted from Wikipedia cirrus dump and modified.
    """
    import re
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)

    d_pid2eneid = {}
    with open(enew_info, 'r', encoding='utf-8') as em:
        for line in em:
            (pageid, eneid, title) = re.split('\t', line)

            if pageid not in d_pid2eneid:
                d_pid2eneid[pageid] = eneid
    return d_pid2eneid
