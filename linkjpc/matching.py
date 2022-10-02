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
    Notice:
        d_mention_pid_ratio
            sample
                key: 鎮痛薬
                val: [('818157', 1.0), ('548022', 0.38)]
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
    # check = {}
    check_list = {}
    # check if partial match
    if d_mention_pid_ratio.get(mention):
        cand_cnt = 0

        for pid_ratio_list in d_mention_pid_ratio[mention]:
            pid = pid_ratio_list[0]
            ratio = float(pid_ratio_list[1])
            # if pid == '1593456':
            #     logger.info({
            #         'action': 'match_mention_title',
            #         'pid': pid,
            #         'mention': mention,
            #         'ratio': ratio,
            #         'char_match_min': char_match_min,
            #         'char_match_cand_num_mint': opt_info.char_match_cand_num_max
            #     })
            # 'action': 'match_mention_title', 'pid': '774353', 'mention': '千葉', 'ratio': 0.67,
            # 'char_match_min': 0.2, 'char_match_cand_num_mint': 1000}
            if ratio > 1.0:
                logger.error({
                    'action': 'match_mention_title',
                    'error': 'illegal ratio',
                    'mention': mention,
                    'pid_ratio_list': pid_ratio_list,
                })
                sys.exit()
            # if mention == '千葉' and pid == '774353':
            #     logger.info({
            #         'action': 'match_mention_title',
            #         'check': 'before_if_ratio',
            #         'mention': mention,
            #         'pid': pid,
            #         'mod': mod,
            #         'ratio': ratio
            #     })
            #  'action': 'match_mention_title', 'check': 'before_if_ratio', 'mention': '千葉', 'pid': '774353',
            #  'mod': 'm', 'ratio': 0.67}
            if ratio:
                # if mention == '千葉' and pid == '774353':
                #     logger.info({
                #         'action': 'match_mention_title',
                #         'check': 'if_ratio',
                #         'mention': mention,
                #         'pid': pid,
                #         'mod': mod,
                #         'ratio': ratio
                #     })
                # 'action': 'match_mention_title', 'check': 'if_ratio', 'mention': '千葉', 'pid': '774353',
                # 'mod': 'm', 'ratio': 0.67}
                # partial match
                if ratio < 1.0:
                    if ratio < char_match_min:
                        logger.debug({
                            'action': 'match_mention_title',
                            'msg': 'skipped ratio is less than char_match_min',
                            'mention': mention,
                            'ratio': ratio,
                            'char_match_min': char_match_min,
                        })
                        continue
                    elif match_type == 'e':
                        logger.debug({
                            'action': 'match_mention_title',
                            'msg': 'skipped match_type is e and ratio is less than 1',
                            'mention': mention,
                            'ratio': ratio,
                            'match_type': match_type,
                        })
                        continue
            # logger.info({
            #     'action': 'match_mention_title',
            #     'check': 'before_check_list',
            #     'check_list': check_list,
            # })
            if pid not in check_list:
                # if mention == '千葉' and pid == '774353':
                #     logger.info({
                #         'action': 'match_mention_title',
                #         'check': 'before_append',
                #         'mention': mention,
                #         'cand_list': cand_list,
                #         'pid': pid,
                #         'mod': mod,
                #         'ratio': ratio
                #     })
                cand_list.append([pid, mod, ratio])
                # check_list[pid] = 1
                # if mention == '千葉' and pid == '774353':
                #     logger.info({
                #         'action': 'match_mention_title',
                #         'check': 'after_append',
                #         'mention': mention,
                #         'cand_list': cand_list,
                #         'pid': pid,
                #         'mod': mod,
                #         'ratio': ratio
                #     })
                if cand_cnt == opt_info.char_match_cand_num_max:
                    break
                else:
                    cand_cnt += 1
        # if mention == '千葉':
        #     logger.info({
        #         'action': 'match_mention_title',
        #         'mention': mention,
        #         'cand_list(final)': cand_list
        #     })
            # 'action': 'match_mention_title', 'mention': '千葉', 'cand_list(final)': []}
        if len(cand_list) > 0:
            new_cand_list = sorted(cand_list, key=itemgetter(2), reverse=True)

            # if mention == '千葉':
            #     logger.info({
            #         'action': 'match_mention_title',
            #         'mention': mention,
            #         'new_cand_list': new_cand_list
            #     })

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
            sample:
                key:'湖'
                val: [('401', '0.5'), ('132068', '0.33'), ('9322', '0.25'), ('1431634', '1.0'),...]
        matching_info_file
            format: mention(\t)pid(\t)title(\t)ratio(\n)
                sorted by ratio
            sample(tinm)
                エチオピア      1443906 エチオピア      1.0
                エチオピア北西  1443906 エチオピア      0.71
            sample(mint)
                湖      401     湖国    0.5
                湖      132068  湖南省  0.33
                勾玉	298108	勾玉	1.0
                勾玉	1410287	空色勾玉	0.5
                勾玉	1593456	八坂瓊勾玉	0.4
                勾玉	1593456	八尺瓊勾玉	0.4
                勾玉	710567	翡翠製勾玉	0.4
                勾玉	1593456	八尺瓊の勾玉	0.33
                勾玉	710567	ヒスイ製勾玉	0.33
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
            # print(check_highest_ratio[word][link_pid], type(check_highest_ratio[word][link_pid]))

    for tmp_word in check_highest_ratio:

        if not d_mention_pid_ratio.get(tmp_word):
            d_mention_pid_ratio[tmp_word] = []
        for l_pid in check_highest_ratio[tmp_word]:
            l_ratio = check_highest_ratio[tmp_word][l_pid]
            # print(l_ratio, type(l_ratio))
            # if 'tmp_word' == 'Blue Note' or 'tmp_word' == 'Chanel':
            #     logger.info({
            #        'action': 'reg_matching_info',
            #        'tmp_word': tmp_word,
            #        'l_pid': l_pid,
            #        'l_ratio': l_ratio
            #     })
            d_mention_pid_ratio[tmp_word].append((l_pid, l_ratio))

            # if rows[0] == '千葉' and rows[1] == '774353':
            #     logger.info({
            #         'action': 'reg_matching_info',
            #         'rows': rows,
            #         # 'action': 'reg_matching_info', 'rows': ['千葉', '774353', '千葉県', '0.67']}
            #     })
    return d_mention_pid_ratio
