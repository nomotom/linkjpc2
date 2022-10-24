import config as cf
import linkjpc as ljc
import logging


def match_mention_title(mod, opt_info, mention, log_info, **d_mention_pid_ratio):
    """match mention to title.
    Args:
        mod
        opt_info
        mention
        log_info
        **d_mention_pid_ratio
    Returns:
        cand_list
    """
    from operator import itemgetter
    import sys
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)

    match_type = ''
    char_match_min = 0
    if mod == 'm':
        match_type = opt_info.mention_in_title
        char_match_min = opt_info.mention_in_title_min
    elif mod == 't':
        match_type = opt_info.title_in_mention
        char_match_min = opt_info.title_in_mention_min

    cand_list = []
    new_cand_list = []
    check_list = {}
    # check if partial match
    if d_mention_pid_ratio.get(mention):
        cand_cnt = 0

        for pid_ratio_list in d_mention_pid_ratio[mention]:
            pid = pid_ratio_list[0]
            ratio = float(pid_ratio_list[1])

            if ratio > 1.0:
                logger.error({
                    'action': 'match_mention_title',
                    'error': 'illegal ratio',
                    'mention': mention,
                    'pid_ratio_list': pid_ratio_list,
                })
                sys.exit()
            if ratio:
                if ratio < 1.0:
                    if ratio < char_match_min:
                        continue
                    elif match_type == 'e':
                        continue
            if pid not in check_list:
                cand_list.append([pid, mod, ratio])
                if cand_cnt == opt_info.char_match_cand_num_max:
                    break
                else:
                    cand_cnt += 1

        if len(cand_list) > 0:
            new_cand_list = sorted(cand_list, key=itemgetter(2), reverse=True)

            if len(new_cand_list) > 0:
                cand_limit = min(opt_info.char_match_cand_num_max, len(new_cand_list))
                del new_cand_list[cand_limit:]
    return new_cand_list


def reg_matching_info(matching_info_file, ratio_min, multi_lang, log_info):
    """Register matching ratio of title-mention pairs if the ratio is equal or greater than the minimum ratio.
    Args:
        matching_info_file
        ratio_min
        multi_lang
        log_info
    Returns:
        dict: d_mention_pid_ratio
    Note:
        tinm:
            title length / mention length
        mint:
            mention length / title length
        d_mention_pid_ratio
            format:
                key: mention
                val: [(pid, ratio), (pid, ratio), .....)
        matching_info_file
            format: mention(\t)pid(\t)title(\t)ratio(\n)
                sorted by ratio
    """
    import csv
    import sys
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)

    csv.field_size_limit(1000000000)

    if not ((0 <= ratio_min) and (ratio_min <= 1.0)):
        logger.error({
            'action': 'reg_matching_info',
            'illegal ratio': ratio_min
        })
        sys.exit()

    d_mention_pid_ratio = {}
    check_highest_ratio = {}

    with open(matching_info_file, mode='r', encoding='utf-8') as r:
        reader = csv.reader(r, delimiter='\t')

        for rows in reader:
            word = rows[0]
            link_pid = rows[1]
            link_ratio = float(rows[3])
            lang_code = rows[4]
            if multi_lang == 'j' and lang_code != 'ja':
                continue
            elif multi_lang == 'je' and not (lang_code == 'en' or lang_code == 'ja'):
                continue
            if word in check_highest_ratio:
                if link_pid in check_highest_ratio[word]:
                    if link_ratio <= check_highest_ratio[word][link_pid]:
                        continue
            else:
                check_highest_ratio[word] = {}
            check_highest_ratio[word][link_pid] = link_ratio

    for tmp_word in check_highest_ratio:

        if not d_mention_pid_ratio.get(tmp_word):
            d_mention_pid_ratio[tmp_word] = []
        for l_pid in check_highest_ratio[tmp_word]:
            l_ratio = check_highest_ratio[tmp_word][l_pid]
            d_mention_pid_ratio[tmp_word].append((l_pid, l_ratio))

    return d_mention_pid_ratio
