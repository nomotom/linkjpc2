import linkjpc as ljc
import logging


def check_nil_stop(attr, log_info, **nil_stop_dict):
    """
    :param attr:
    :param log_info:
    :param nil_stop_dict:
    :return: nil_stop_res
     1: nil stop,
     0: not nil stop
    """
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)
    nil_stop_res = 0
    if attr in nil_stop_dict:
        nil_stop_res = 1
        logger.debug({
            'action': 'check_nil_exception_cand',
            'attr': attr,
            'stat': 'stop',
        })
    return nil_stop_res


def check_cand_man(cat_attr, log_info, **cand_man_dict):
    """
    :param cat_attr:
    :param log_info:
    :param cand_man_dict:
    :return: exception_res
     1: candidate of nil detection,
     0: not candidate
    """
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)
    candidate_res = 0
    if cat_attr in cand_man_dict:
        candidate_res = 1
    return candidate_res


def check_nil_stop_attr(nil_stop_file, log_info):
    """
    Register candidate category-attribute pairs to dict
    :param nil_stop_file:
    :param log_info:
    :return: nil_stop_dict:
    """
    import csv
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)

    nil_stop_dict = {}
    with open(nil_stop_file, mode='r', encoding='utf-8') as ns:
        ns_reader = csv.reader(ns, delimiter='\t')
        for attr in ns_reader:
            if '#' in attr:
                continue
            nil_stop_dict[attr] = 1
    return nil_stop_dict


def reg_nil_cand_man(cand_man_file, log_info):
    """
    Register candidate category-attribute pairs to dict
    :param cand_man_file:
    :param log_info:
    :return: nil_cand_dict:
    """
    import csv
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)

    nil_cand_dict = {}
    with open(cand_man_file, mode='r', encoding='utf-8') as ne:
        ne_reader = csv.reader(ne, delimiter='\t')
        for line in ne_reader:
            if '#' in line:
                continue
            cat_attr = ':'.join(line)
            logger.debug({
                'action': 'check_nil_cand_man',
                'cat_attr': cat_attr,
            })
            nil_cand_dict[cat_attr] = 1

    return nil_cand_dict


def estimate_nil(cat_attr, cand_res, stop_attr_res, mention_info, opt_info, log_info, **d_linkable):
    """Create a list of nil candidates based on nil(unlinkable) cat-attr info, nil cand res, nil stop res,
    mention length, and mention pattern
    Args:
        cat_attr
        cand_res
        stop_attr_res
        mention_info
        opt_info
        log_info
        **d_linkable
    Returns:
        res_nil
            1: unlinkable
            0: linkable
    Note:
        linkable info file
            format:  format: 'cat', 'attr', 'ratio', 'linkable_freq', 'all_freq' (*.tsv)
        nil_cond
            how to evaluate nil (unlinkable) for each mention using prob (estimated linkable ratio for '
                   'category-attribute pairs based on sample data), len(minimum length of mention), and desc '
                   '(descriptiveness of mentions).
        nil_desc_exception
            exception to nil -desc- condition. If 'person_works' is specified, desc condition is not evaluated
            for the category attribute pairs(Person:works(作品)).
        len_desc_text_min (int)
            minimum length of mention text regarded as descriptive
        nil_cat_attr_max (float)
            maximum ratio of linkable category attribute pairs in the sample data.
            If nil ratio of the category-attribute pair of a mention is equal or less than the ratio,
            the mention might be judged as 'unlinkable'.
    """
    import sys
    import csv
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)

    nil_cond = opt_info.nil_cond
    nil_desc_exception = opt_info.nil_desc_exception
    len_desc_text_min = opt_info.len_desc_text_min
    nil_cat_attr_max = opt_info.nil_cat_attr_max
    res_nil = 0

    res_prob_cond = 0
    link_prob_cat_attr = 0.0

    tmp_text = mention_info.t_mention
    if d_linkable.get(cat_attr):
        link_prob_info_list = d_linkable[cat_attr]
        all_freq = int(link_prob_info_list[2])
        link_prob_cat_attr = float(link_prob_info_list[0])

        if all_freq >= opt_info.nil_all_freq_min:
            if link_prob_cat_attr <= nil_cat_attr_max:
                res_prob_cond = 1

    res_len_cond = 0
    if 'len' in nil_cond:
        if len(tmp_text) >= len_desc_text_min:
            res_len_cond = 1

    res_cman = 0
    if 'cman' in nil_cond:
        if cand_res:
            res_cman = 1

    res_nostop = 1
    if 'nostop' in nil_cond:
        if stop_attr_res:
            res_nostop = 0

    res_desc_cond = 0
    check_exception_keyword = 0
    if 'desc' in nil_cond:
        for cat_attr_exc in opt_info.nil_desc_exception_def:
            if (cat_attr_exc in nil_desc_exception) and (cat_attr == opt_info.nil_desc_exception_def[cat_attr_exc]):
                check_exception_keyword = 1

        if check_exception_keyword == 0:
            res_desc_cond = evaluate_descriptiveness(tmp_text, log_info)

    if nil_cond == 'and_prob_len_desc':
        if res_prob_cond and res_len_cond and res_desc_cond:
            res_nil = 1
    elif nil_cond == 'and_prob_or_len_desc':
        if res_prob_cond:
            if res_len_cond or res_desc_cond:
                res_nil = 1
    elif nil_cond == 'and_len_or_prob_desc':
        if res_len_cond:
            if res_prob_cond or res_desc_cond:
                res_nil = 1
    elif nil_cond == 'and_desc_or_prob_len':
        if res_desc_cond:
            if (res_prob_cond == 1) or (res_len_cond == 1):
                res_nil = 1
    elif nil_cond == 'two_of_prob_len_desc':
        if (res_prob_cond and res_len_cond) or (res_prob_cond and res_desc_cond) or (res_len_cond and res_desc_cond):
            res_nil = 1
    elif nil_cond == 'and_prob_len_desc_cman':
        if res_prob_cond and res_len_cond and res_desc_cond and res_cman:
            res_nil = 1
    elif nil_cond == 'and_prob_cman_or_len_desc':
        if res_prob_cond and res_cman:
            if res_len_cond or res_desc_cond:
                res_nil = 1
    elif nil_cond == 'and_len_cman_or_prob_desc':
        if res_len_cond and res_cman:
            if res_prob_cond or res_desc_cond:
                res_nil = 1
    elif nil_cond == 'and_desc_cman_or_prob_len':
        if res_desc_cond and res_cman:
            if res_prob_cond or res_len_cond:
                res_nil = 1
    elif nil_cond == 'and_cman_two_of_prob_len_desc':
        if res_cman:
            if (res_prob_cond and res_len_cond) or (res_prob_cond and res_desc_cond) or (res_len_cond and res_desc_cond):
                res_nil = 1
    elif nil_cond == 'cman':
        if res_cman:
            res_nil = 1
    elif nil_cond == 'and_prob_len_desc_nostop':
        if res_prob_cond and res_len_cond and res_desc_cond and res_nostop:
            res_nil = 1
    elif nil_cond == 'and_prob_nostop_or_len_desc':
        if res_prob_cond and res_nostop:
            if res_len_cond or res_desc_cond:
                res_nil = 1
    elif nil_cond == 'and_len_nostop_or_prob_desc':
        if res_len_cond and res_nostop:
            if res_prob_cond or res_desc_cond:
                res_nil = 1
    elif nil_cond == 'and_desc_nostop_or_prob_len':
        if res_desc_cond and res_nostop:
            if res_prob_cond or res_len_cond:
                res_nil = 1
    elif nil_cond == 'and_nostop_two_of_prob_len_desc':
        if res_nostop:
            if (res_prob_cond and res_len_cond) or (res_prob_cond and res_desc_cond) or (res_len_cond and res_desc_cond):
                res_nil = 1

    return res_nil


def evaluate_descriptiveness(text, log_info):
    """evaluate descriptiveness of text
    Args:
        text
        log_info
    Returns:
        1: descriptive
        0: non-descriptive
    """
    import sys
    import re
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)

    # 1)substring
    # symbols (punctuation, colon, reference)
    symbol_list = [',', '。', '、', ':', '\[', '\]']

    # particles (parallel)
    parallel_list = ['[^ぁ-ん]と', '[^ぁ-ん]や', 'および', '及び']

    # other particles, conjunctions
    particles_list = ['[^ぁ-ん]が', '[^ぁ-ん]は', 'を', '[^ぁ-ん]へ', '[^ぁ-ん]に', '[^ぁ-ん]も', '[^ぁ-ん]から', '[^ぁ-ん]まで',
                      '[^ぁ-ん]より', '[^ぁ-ん]よって', '[^ぁ-ん]で', '以後', '以降', '以前', '以来']

    # relaxing expressions
    relaxing_list = ['等の', '等に', 'など', '程度',  'ほぼ', 'おおむね', '大体', 'おそらく']

    # location expressions
    location_list = ['の一部', '囲まれた', '挟まれた', '突き出した', '面した', 'に位置',  'の全域', 'のあたり', '近く', '近郊']

    # demostrative
    demonstrative_list = ['ここ', 'そこ', 'あそこ', 'どこ', 'この', 'その', 'あの', 'どの', 'これ', 'それ', 'あの', 'どの']

    subpat_list = symbol_list + parallel_list + particles_list + relaxing_list + location_list + demonstrative_list

    subpat_pat = '|'.join(subpat_list)

    # 2)prefix + (num)
    prefix_list = ['約[0-9零一二三四五六七八九十百千万億兆]', 'およそ']
    prefix_pat = '|'.join(prefix_list)

    # 3)(num) + suffix
    suffix_list = ['\[0-9\]kg', '\[0-9\]g', '\[0-9\]mg', '\[0-9\]L', '\[0-9\]mm', '℃', '%', '\[0-9\]回', '\[0-9\]位',
                   '\[0-9\]時間', '\[0-9\]分', '\[0-9\]秒', '年\[0-9\]+月']
    suffix_pat = '|'.join(suffix_list)

    subpat_p = re.compile(subpat_pat)
    prefix_p = re.compile(prefix_pat)
    suffix_p = re.compile(suffix_pat)

    res = 0
    if re.search(subpat_p, text) is not None:
        res = 1
    elif re.search(prefix_p, text) is not None:
        res = 1
    elif re.search(suffix_p, text) is not None:
        res = 1
    return res


def check_linkable_info(linkable_info_file, log_info):
    """Get 'linkable' category and attribute pairs and ratio dict.
    Args:
        linkable_info_file (str): linkable info file name
        log_info

    Returns:
        d_linkable: dictionary
            key: <ENE category of the page>:<attribute name>
            val: [linkable ratio, linked_freq, all_freq]
    Note:
         linkable info file
            format: format: 'cat', 'attr', 'ratio', 'linked_freq', 'all_freq' (*.tsv)
            sample:
                Video_Work      別名    1.0     8       8
                Video_Work      監督    0.92    12      13
                Video_Work      脚本    0.4     2       5
    """

    import csv
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)
    d_linkable = {}
    with open(linkable_info_file, 'r', encoding='utf-8') as nl:
        nl_reader = csv.reader(nl, delimiter='\t')

        for line in nl_reader:
            cat_attr = ':'.join([line[0], line[1]])
            d_linkable[cat_attr] = [float(line[2]), line[3], line[4]]
    return d_linkable
