import linkjpc as ljc
import logging

def estimate_self_link(cat_attr, slink_prob, mention_info, slink_min, self_link_by_attr_name_file, log_info, **d_self_link):
    """Create a list of self link based on self link info and attribute name.

    Args:
        cat_attr
        slink_prob (fixed/raw/mid/r_est/m_est/f_est)
        mention_info
        slink_min
        self_link_by_attr_name_file
        log_info
        **d_self_link
            self link info in the sample data
            if appeared:
              d_self_link[cat_attr]['ratio'] = float(self link ratio)
            if not appeared:
              d_self_link[cat_attr]['ca_no_show'] = 1

    Returns:
        slink_cand_list
            format: [(pid, mod, score)]
    Note:
        The self link ratio of attributes in self_link_by_attr_name_file is set to slink_min.
        self_link info file
            format: (cat(\t)att(\t)self_link ratio(\t)self link num(\t)freq
            sample: Compound 商標名 0.75  75 100
            notice: Currently the ratio in the file is based on small sample data and highly recommended to be modified.
        self_link_by_attr_name_file
            format: attr(\n)
            sample: 別名・旧称
                    別名
                    旧称
    """
    import sys
    import csv
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)
    logger.debug({
        'action': 'estimate_self_link',
        'slink_prob': 'slink_prob',
        'cat_attr': cat_attr,
    })
    slink_cand_list = []

    self_link_attr_list = []
    with open(self_link_by_attr_name_file, mode='r', encoding='utf-8') as sp:
        for tmp_a in sp:
            tmp_a = tmp_a.rstrip()
            self_link_attr_list.append(tmp_a)
        self_link_attr_set = set(self_link_attr_list)
        logger.debug({
            'action': 'estimate_self_link',
            'self_link_attr_set': self_link_attr_set,
        })

    # if cat_attr in d_self_link:
    #     if d_self_link[cat_attr]['ratio'] == 0:
    #         logger.info({
    #             'action': 'estimate_self_link',
    #             'msg': 'should be cand++++++++++++++++++++++++++++',
    #         })


    if (cat_attr not in d_self_link) or ('ca_no_show' in d_self_link[cat_attr]):

        if 'est' in slink_prob:
            (cat, attr) = cat_attr.split(':')
            logger.debug({
                'action': 'estimate_self_link',
                'attr': attr,
            })
            if attr in self_link_attr_set:
                slink_cand_list = [(mention_info.pid, 's', slink_min)]
                logger.debug({
                    'action': 'estimate_self_link',
                    'msg': 'applicable',
                    'slink_min': slink_min,
                    'slink_prob': slink_prob,
                    'attr': attr,
                    'slink_cand_list': slink_cand_list,
                })
            # else:
            #     logger.info({
            #         'action': 'estimate_self_link',
            #         'msg': 'not applicable',
            #         'slink_prob': slink_prob,
            #         'cat_attr': cat_attr,
            #         'slink_cand_list': slink_cand_list,
            #     })
        # else:
        #     logger.info({
        #         'action': 'estimate_self_link',
        #         'msg': 'not est',
        #     })

    else:
        if slink_prob == 'fixed' or slink_prob == 'f_est':
            slink_cand_list = [(mention_info.pid, 's', 1.0)]
        elif slink_prob == 'raw' or slink_prob == 'r_est':
            if d_self_link[cat_attr]['ratio'] > 1.0:
                logger.error({
                    'action': 'estimate_self_link',
                    'error': 'slink_score_max is more than 1.0',
                    'slink_score_max': d_self_link[cat_attr]['ratio'],
                })
                sys.exit()

            slink_cand_list = [(mention_info.pid, 's', d_self_link[cat_attr]['ratio'])]
            if cat_attr == 'Person:別名':
                logger.debug({
                    'action': 'estimate_self_link',
                    'slink_prob': slink_prob,
                    'cat_attr': cat_attr,
                    'slink_cand_list': slink_cand_list,
                })
        elif slink_prob == 'mid' or slink_prob == 'm_est':
            score = (1 + d_self_link[cat_attr]['ratio'])/2

            if score > 1.0:
                logger.error({
                    'action': 'estimate_self_link',
                    'error': 'slink_score_max is more than 1.0',
                    'slink_score_max': score,
                })
                sys.exit()
            slink_cand_list = [(mention_info.pid, 's', score)]
            logger.debug({
                'action': 'estimate_self_link',
                'slink_prob': slink_prob,
                'cat_attr': cat_attr,
                'score': score,
                'd_self_link[cat_attr][ratio]': d_self_link[cat_attr]['ratio'],
                'slink_cand_list': slink_cand_list,
            })
        logger.debug({
            'action': 'estimate_self_link',
            'slink_prob': slink_prob,
            'cat_attr': cat_attr,
            'd_self_link[cat_attr][ratio]': d_self_link[cat_attr]['ratio'],
            'slink_cand_list': slink_cand_list,
        })

    return slink_cand_list

def check_slink_info(slink_file, log_info):
# def check_slink_info(slink_file, slink_min, log_info):
    """Get 'self_link' category and attribute pairs.
    Args:
        slink_file (str): self_link info file name
        slink_min(float): minimum ratio to apply 'self_link' to the above category and attribute pair
        log_info

    Returns:
        d_self_link: dictionary
            key: <ENE category of the page>:<attribute name>
            val: self_link_ratio
    Note:
        slink_file
            (format) cat, attr, self link ratio, self link num, cat_attr_freq (tsv)
            (sample) School  別名    1.0     4       4

    """

    import csv
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)
    d_self_link = {}
    with open(slink_file, 'r', encoding='utf-8') as sl:
        sl_reader = csv.reader(sl, delimiter='\t')

        for line in sl_reader:
            # case: the category/attribute does not appear in training data
            # if line[4] == 0:
            #     continue

            # if float(line[2]) >= slink_min:
            #     cat_attr = ':'.join([line[0], line[1]])
            #     d_self_link[cat_attr] = float(line[2])

            cat_attr = ':'.join([line[0], line[1]])
            # d_self_link[cat_attr] = float(line[2])
            # 20220924
            d_self_link[cat_attr] = {}
            # 20220907
            d_self_link[cat_attr]['ratio'] = float(line[2])
            # print(type(line[4]), line[4], int(line[4]))
            if int(line[4]) == 0:
                # d_self_link[cat_attr]['ca_no_show'] = 1
                # 20220914

                d_self_link[cat_attr]['ca_no_show'] = 1

    return d_self_link
