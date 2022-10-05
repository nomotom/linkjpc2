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
    notice:
        d_cat_attr2eneid_prob:
            'Amphibia__分布地': {'1.5.1.2': 0.64},
    """
    from decimal import Decimal, ROUND_HALF_UP
    import re
    import sys
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)

    new_module_cand_list = []

    # # print(d_cat_attr2eneid_prob)
    # for tmp in d_cat_attr2eneid_prob:
    #     tmp_string = '(' + tmp + ')'
    #     print(tmp_string)

    if len(module_cand_list) > 0:
        for cand_info in module_cand_list:
            logger.debug({
                'action': 'filter_by_attr_range',
                'cand_info': cand_info,
            })
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
                # たまたま現れなかった＆人手でルールを書いていなかった
                if cat_attr == 'Bridge__終点':
                    logger.debug({
                        'action': 'filter_by_attr_range',
                        'msg(1)': 'cat attr not defined in d_cat_attr2eneid_prob',
                        'attr_rng_type': opt_info.attr_rng_type,
                        'cat_attr': cat_attr,
                        'cand_info': cand_info,
                        'mention_pid': mention_info.pid,
                        'mention_enecat': mention_info.ene_cat,
                        'mention_text': mention_info.t_mention,
                        'link_page_id': mention_info.link_page_id,
                    })
                if cf.d_pid2eneid.get(pid):
                    cand_eneid = cf.d_pid2eneid[pid]
                    logger.debug({
                        'action': 'filter_by_attr_range',
                        'co_type': 'cat attr not defined in d_cat_attr2eneid_prob',
                        'cat_attr': cat_attr,
                        'cand_eneid': cand_eneid,
                        'mention': mention_info.t_mention,
                        'title': cf.d_pid_title_incoming_eneid[pid][0],
                        'attr_co': attr_co
                    })
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
                        logger.debug({
                            'action': 'filter_by_attr_range',
                            'ans_prob': ans_prob,
                        })
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
    # def get_attr_range(attr_range_man_file, attr_range_auto_file, attr_range_merged_file, all_cat_file, opt_info,
    #                    log_info, **d_cnv):
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

        d_cat_attr2eneid_prob: dictionary
         (format)
            (key: <cat>__<attr>, val:[[<eneid>, <prob>], [<eneid>, <prob>],...])
                cat: ene_label_en
                attr: attribute_name
         (sample)
            {'City__国': [['1.5.1.0', 1.0], ['1.5.1.3',0.5], 'Airport__国': [['1.5.1.0', 1.0], ['1.5.1.3', 0.5]], ....}
    """
    import re
    import csv
    import sys
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)
    # all_cat_set = set()
    # with open(all_cat_file, mode='r', encoding='utf-8') as ac:
    #     ac_reader = csv.reader(ac, delimiter='\t')
    #     #  `1.0	名前＿その他	Name_Other`
    #     for ac_line in ac_reader:
    #         all_cat_set.add(ac_line[2])
    # for eid, en_label in d_cnv.items():
    #     all_cat_set.add(en_label)

    m_cat_attr2eneid_prob = {}
    if 'm' in opt_info.attr_rng_type:
        with open(attr_range_man_file, 'r', encoding='utf-8') as m:
            m_reader = csv.reader(m, delimiter='\t')
            #  - `School  理事長  1.1 Person      1.0`
            # cat_attr_range_prob_list = [cat_attr_range_prob for cat_attr_range_prob in m_reader]

            for m_cat_attr_range_prob in m_reader:
                # 202210/5 comment out from here
                # if len(cat_attr_range_prob) < opt_info.attr_len_max:
                #     logger.error({
                #         'action': 'get_attr_range',
                #         'cat_attr_range_prob too short': cat_attr_range_prob,
                #     })
                #     sys.exit()
                # till here
                # try:
                #     eneid = re.sub('ene:', '', cat_attr_range_prob[2])
                # except (KeyError, ValueError) as e:
                #     logger.error({
                #         'action': 'get_attr_range',
                #         'error': e
                #     })
                # 20221002
                eneid = m_cat_attr_range_prob[2]
                logger.debug({
                    'action': 'get_attr_range',
                    'eneid(1)': eneid,
                    'cat_att_range_prob': m_cat_attr_range_prob
                })
                lc.check_dic_key(eneid, log_info, **d_cnv)
                cat = m_cat_attr_range_prob[0]
                # if cat not in opt_info.cat_set:
                # if cat not in all_cat_set:
                #     logger.error({
                #         'action': 'get_attr_range',
                #         'error': 'illegal cat: not defined in attr_range_man_file',
                #         'cat': cat
                #     })
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
            #  Music   プロデューサー  1.1   Person  1.0  10   10`
            # for cat_attr_range_prob in a_reader:

            # cat_attr_range_prob_list = [cat_attr_range_prob for cat_attr_range_prob in a_reader]
            # for cat_attr_range_prob in cat_attr_range_prob_list:

            for a_cat_attr_range_prob in a_reader:
                # comment out 10/5 fromhere
                # if len(cat_attr_range_prob) < opt_info.attr_len_max:
                #     logger.error({
                #         'action': 'get_attr_range',
                #         'cat_attr_range_prob too short': cat_attr_range_prob,
                #     })
                #     sys.exit()
                # till here
                # try:
                #     eneid = re.sub('ene:', '', cat_attr_range_prob[2])
                # except (KeyError, ValueError) as e:
                #     logger.error({
                #         'action': 'get_attr_range',
                #         'error': e
                #     })
                # 20221002
                eneid = a_cat_attr_range_prob[2]
                logger.debug({
                    'action': 'get_attr_range',
                    'a_cat_attr_range_prob': a_cat_attr_range_prob,
                })
                lc.check_dic_key(eneid, log_info, **d_cnv)
                cat = a_cat_attr_range_prob[0]

                # if cat_attr_range_prob[0] in d_cnv:
                #     cat = cat_attr_range_prob[0]
                #     logger.info({
                #         'action': 'get_attr_range',
                #         'cat_attr_range_prob[0]': cat_attr_range_prob[0],
                #     })
                # if cat not in all_cat_set:
                # # # if cat not in opt_info.cat_set:
                #     logger.error({
                #         'action': 'get_attr_range',
                #         'error': 'illegal cat: not defined in attr_range_auto_file',
                #         'cat_attr_range_prob[0]': cat_attr_range_prob[0],
                #         'cat': cat
                #     })
                #     sys.exit()
                attr = a_cat_attr_range_prob[1]
                # 20221005
                prob = float(a_cat_attr_range_prob[4])
                freq = int(a_cat_attr_range_prob[5])

                if freq < opt_info.attr_rng_auto_freq_min_default:
                    continue

                cat_attr = cat + '__' + attr
                if not a_cat_attr2eneid_prob.get(cat_attr):
                    a_cat_attr2eneid_prob[cat_attr] = {}
                a_cat_attr2eneid_prob[cat_attr][eneid] = prob

                # logger.info({
                #     'action': 'get_attr_rng',
                #     'a_cat_attr2eneid_prob[cat_attr][eneid] ': a_cat_attr2eneid_prob[cat_attr][eneid]
                # })

                # 20220929
                # if 'ma' in opt_info.attr_rng_type:
                #     if cat_attr not in m_cat_attr2eneid_prob:
                #         m_cat_attr2eneid_prob[cat_attr] = {}
                #
                #     m_cat_attr2eneid_prob[cat_attr][eneid] = prob

    d_cat_attr2eneid_prob = {}
    if opt_info.attr_rng_type == 'a' or opt_info.attr_rng_type == 'am':
        for a_cat_attr in a_cat_attr2eneid_prob:
            for aid, aprob in a_cat_attr2eneid_prob[a_cat_attr].items():
                if a_cat_attr not in d_cat_attr2eneid_prob:
                    d_cat_attr2eneid_prob[a_cat_attr] = {}
                d_cat_attr2eneid_prob[a_cat_attr][aid] = aprob
                # d_cat_attr2eneid_prob[cat_attr].append([eneid, prob])
        if opt_info.attr_rng_type == 'am':
            for m_cat_attr in m_cat_attr2eneid_prob:
                for mid, mprob in m_cat_attr2eneid_prob[m_cat_attr].items():
                    if m_cat_attr not in d_cat_attr2eneid_prob:
                        d_cat_attr2eneid_prob[m_cat_attr] = {}
                        d_cat_attr2eneid_prob[m_cat_attr][mid] = mprob
                    # 20221005
                    elif (mid not in d_cat_attr2eneid_prob[m_cat_attr]) or \
                            (d_cat_attr2eneid_prob[m_cat_attr][mid] == 0):
                        d_cat_attr2eneid_prob[m_cat_attr][mid] = mprob

                    # d_cat_attr2eneid_prob[cat_attr].append([eneid, prob])

    if opt_info.attr_rng_type == 'm' or opt_info.attr_rng_type == 'ma':
        for h_cat_attr in m_cat_attr2eneid_prob:
            for hid, hprob in m_cat_attr2eneid_prob[h_cat_attr].items():
                if h_cat_attr not in d_cat_attr2eneid_prob:
                    d_cat_attr2eneid_prob[h_cat_attr] = {}
                d_cat_attr2eneid_prob[h_cat_attr][hid] = hprob
                # d_cat_attr2eneid_prob[cat_attr].append([eneid, prob])
        if opt_info.attr_rng_type == 'ma':
            for i_cat_attr in a_cat_attr2eneid_prob:
                for iid, iprob in a_cat_attr2eneid_prob[i_cat_attr].items():
                    if i_cat_attr not in d_cat_attr2eneid_prob:
                        d_cat_attr2eneid_prob[i_cat_attr] = {}
                        d_cat_attr2eneid_prob[i_cat_attr][iid] = iprob
                    # 20221005
                    elif (iid not in d_cat_attr2eneid_prob[i_cat_attr]) or \
                            (d_cat_attr2eneid_prob[i_cat_attr][iid] == 0):
                        d_cat_attr2eneid_prob[i_cat_attr][iid] = iprob

                    # d_cat_attr2eneid_prob[cat_attr].append([eneid, prob])

    with open(attr_range_merged_file, mode='w', encoding='utf-8') as arm:
        writer = csv.writer(arm, delimiter='\t', lineterminator='\n')
        for ca in d_cat_attr2eneid_prob:
            for eid in d_cat_attr2eneid_prob[ca]:
                if ca == 'Bridge__終点':
                    logger.info({
                        'ca': ca,
                        'eid': eid,
                        'd_cat_attr2eneid_prob[ca]':d_cat_attr2eneid_prob[ca]
                    })
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
