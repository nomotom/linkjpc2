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
    """
    import sys
    import csv
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)

    slink_cand_list = []

    self_link_attr_set = set()
    with open(self_link_by_attr_name_file, mode='r', encoding='utf-8') as sp:
        self_link_attr_list = []
        for tmp_a in sp:
            tmp_a = tmp_a.rstrip()
            self_link_attr_list.append(tmp_a)
        self_link_attr_set = set(self_link_attr_list)

    if (cat_attr not in d_self_link) or ('ca_no_show' in d_self_link[cat_attr]):
        if 'est' in slink_prob:
            (cat, attr) = cat_attr.split(':')
            if attr in self_link_attr_set:
                slink_cand_list = [(mention_info.pid, 's', slink_min)]
        else:
            return slink_cand_list

    elif d_self_link[cat_attr]['ratio'] > 0:

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

    return slink_cand_list


def check_slink_info(slink_file, log_info):
    """Get 'self_link' category and attribute pairs.
    Args:
        slink_file (str): self_link info file name
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
            cat_attr = ':'.join([line[0], line[1]])
            d_self_link[cat_attr] = {}
            d_self_link[cat_attr]['ratio'] = float(line[2])
            if int(line[4]) == 0:
                d_self_link[cat_attr]['ca_no_show'] = 1

    return d_self_link
