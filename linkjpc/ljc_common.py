import linkjpc as ljc
import config as cf
import logging
import csv
import sys


def check_dic_key(keyword, log_info, **dic):
    """
    :param keyword:
    :param log_info:
    :param dic:
    :return:
    """
    import logging
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)

    if keyword not in dic:
        logger.error({
            'action': 'check_dic_key',
            'msg': 'key not found',
            'key': keyword,
        })
        sys.exit()


def linkedjson2tsv(linked_json_dir, title2pid_org_file, log_info):
    """Convert linked json file　(with no title) to linked tsv file
        add title info based on title2pid_org_file

    args:
        linked_json_dir
        title2pid_org_file
        log_info
    output:
        linked_tsv (tsv)
            format
                pageid, title, attribute, text, start_line_id, start_offset, end_line_id, end_offset, link_pageid,
                link_page_title
    notice
        '\n' in text(mention) has been converted to '\\n'.
    """

    import json
    import pandas as pd
    from glob import glob

    import logging
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)

    logger.info({
        'action': 'linkedjson2tsv',
        'linked_json_dir': linked_json_dir,
        'title2pid_org_file': title2pid_org_file,
    })
    get_title = {}
    with open(title2pid_org_file, mode='r', encoding='utf-8') as r:
        for rline in r:
            rd = {}
            pid = ''
            title = ''
            rd = json.loads(rline)
            check_dic_key('page_id', log_info, **rd)

            if not rd['page_id']:
                logger.error({
                    'action': 'linkedjson2tsv',
                    'error': 'page_id null'
                })
                sys.exit()
            else:
                pid = str(rd['page_id'])
            check_dic_key('title', log_info, **rd)

            if not rd['title']:
                logger.error({
                    'action': 'linkedjson2tsv',
                    'error': 'no title redirect to',
                    'rline': rline
                })
                sys.exit()
            else:
                title = rd['title']
                get_title[pid] = title
            rd.clear()

    linked_json_files = linked_json_dir + '*.jsonl'

    for linked_json in glob(linked_json_files):
        if 'for_view' in linked_json:
            logger.error({
                'action': 'cnv_ene_pageid',
                'msg': 'illegal file: for_view',
            })
            sys.exit()
        go_list = []
        if '_dist.jsonl' in linked_json:
            linked_tsv = linked_json.replace('_dist.jsonl', '.tsv')
        else:
            linked_tsv = linked_json.replace('.jsonl', '.tsv')

        with open(linked_json, mode='r', encoding='utf-8') as g, open(linked_tsv, 'w', encoding='utf-8') as o:
            for g_line in g:
                d_gline = json.loads(g_line)
                g_key_list = get_key_list(log_info, **d_gline)
                g_link_pageid = g_key_list[7]
                text_pre = g_key_list[3]
                g_key_list[3] = '\\n'.join(text_pre.splitlines())

                if get_title.get(g_link_pageid):
                    g_link_title = get_title[g_link_pageid]
                    g_key_list.insert(8, g_link_title)
                g_title_pageid = g_key_list[0]
                if get_title.get(g_title_pageid):
                    g_org_title = get_title[g_title_pageid]
                    g_key_list.insert(1, g_org_title)

                go_list.append(g_key_list)

            df_go = pd.DataFrame(go_list)
            df_go.to_csv(o, sep='\t', header=False, index=False)


def get_key_list_with_title(log_info, **tr):
    """get key list from input json dictionary to distinguish each record
       The dictionary should include title of the page as key
    args:
        log_info
        **tr
    return:
        tmp_list
            format: [pageid, title, attribute, text, start_line_id, start_offset, end_line_id, end_offset, link_id]
    """

    import sys
    import logging
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)

    try:
        pid = tr['page_id']
    except (KeyError, ValueError) as ex:
        logger.error({
            'action': 'get_key_list_with_title',
            'error': ex,
            'tr': tr
        })
        sys.exit()
    try:
        title = tr['title']
    except (KeyError, ValueError) as ex:
        logger.error({
            'action': 'get_key_list_with_title',
            'error': ex,
            'tr': tr
        })
        sys.exit()
    try:
        at = tr['attribute']
    except (KeyError, ValueError) as ex:
        logger.error({
            'action': 'get_key_list_with_title',
            'error': ex,
            'tr': tr
        })
        sys.exit()

    if 'text_offset' not in tr:
        logger.error({
            'action': 'get_key_list_with_title',
            'error': 'format_error: text_offset',
            'tr': tr
        })
        sys.exit()
    else:
        if 'start' not in tr['text_offset']:
            logger.error({
                'action': 'get_key_list_with_title',
                'error': 'format_error: start(text_offset)',
                'tr': tr
            })
            sys.exit()
        else:
            if 'line_id' not in tr['text_offset']['start']:
                logger.error({
                    'action': 'get_key_list_with_title',
                    'error': 'format_error: line_id(start)',
                    'tr': tr
                })
                sys.exit()
            else:
                start_line_id = str(tr['text_offset']['start']['line_id'])

            if 'offset' not in tr['text_offset']['start']:
                logger.error({
                    'action': 'get_key_list_with_title',
                    'error': 'format_error: offset(start)',
                    'tr': tr
                })
                sys.exit()
            else:
                start_offset = str(tr['text_offset']['start']['offset'])

        if 'end' not in tr['text_offset']:
            logger.error({
                'action': 'get_key_list_with_title',
                'error': 'format_error: end(text_offset)',
                'tr': tr
            })
            sys.exit()
        else:
            if 'line_id' not in tr['text_offset']['end']:
                logger.error({
                    'action': 'get_key_list_with_title',
                    'error': 'format_error: line_id(end)',
                    'tr': tr
                })
                sys.exit()
            else:
                end_line_id = str(tr['text_offset']['end']['line_id'])

            if 'offset' not in tr['text_offset']['end']:
                logger.error({
                    'action': 'get_key_list_with_title',
                    'error': 'format_error: offset(end)',
                    'tr': tr
                })
                sys.exit()
            else:
                end_offset = str(tr['text_offset']['end']['offset'])

            if 'text' not in tr['text_offset']:
                logger.error({
                    'action': 'get_key_list_with_title',
                    'error': 'format_error: text(text_offset)',
                    'tr': tr
                })
                sys.exit()
            else:
                text = tr['text_offset']['text']

    if 'link_page_id' not in tr:
        link_id = None
    else:
        link_id = tr['link_page_id']

    tmp_list = [pid, title, at, text, start_line_id, start_offset, end_line_id, end_offset, link_id]
    return tmp_list


def get_key_list(log_info, **tr):
    """get key list from input json dictionary to distinguish each record
    args:
        log_info
        **tr
    return:
        tmp_list
            format: [pageid, attribute, text, start_line_id, start_offset, end_line_id, end_offset, link_id]
    """

    import sys
    import logging
    logger = ljc.set_logging(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    try:
        pid = tr['page_id']
    except (KeyError, ValueError) as ex:
        logger.error({
            'action': 'get_key_list',
            'error': ex,
            'tr': tr
        })
        sys.exit()

    try:
        at = tr['attribute']
    except (KeyError, ValueError) as ex:
        logger.error({
            'action': 'get_key_list',
            'error': ex,
            'tr': tr
        })
        sys.exit()

    if 'text_offset' not in tr:
        logger.error({
            'action': 'get_key_list',
            'error': 'format_error: text_offset',
            'tr': tr
        })
        sys.exit()
    else:
        if 'start' not in tr['text_offset']:
            logger.error({
                'action': 'get_key_list',
                'error': 'format_error: start(text_offset)',
                'tr': tr
            })
            sys.exit()
        else:
            if 'line_id' not in tr['text_offset']['start']:
                logger.error({
                    'action': 'get_key_list',
                    'error': 'format_error: line_id(start)',
                    'tr': tr
                })
                sys.exit()
            else:
                start_line_id = str(tr['text_offset']['start']['line_id'])

            if 'offset' not in tr['text_offset']['start']:
                logger.error({
                    'action': 'get_key_list',
                    'error': 'format_error: offset(start)',
                    'tr': tr
                })
                sys.exit()
            else:
                start_offset = str(tr['text_offset']['start']['offset'])

        if 'end' not in tr['text_offset']:
            logger.error({
                'action': 'get_key_list',
                'error': 'format_error: end(text_offset)',
                'tr': tr
            })
            sys.exit()
        else:
            if 'line_id' not in tr['text_offset']['end']:
                logger.error({
                    'action': 'get_key_list',
                    'error': 'format_error: line_id(end)',
                    'tr': tr
                })
                sys.exit()
            else:
                end_line_id = str(tr['text_offset']['end']['line_id'])

            if 'offset' not in tr['text_offset']['end']:
                logger.error({
                    'action': 'get_key_list',
                    'error': 'format_error: offset(end)',
                    'tr': tr
                })
                sys.exit()
            else:
                end_offset = str(tr['text_offset']['end']['offset'])

            if 'text' not in tr['text_offset']:
                logger.error({
                    'action': 'get_key_list',
                    'error': 'format_error: text(text_offset)',
                    'tr': tr
                })
                sys.exit()
            else:
                text = tr['text_offset']['text']

    if 'link_page_id' not in tr:
        link_id = ''
    else:
        link_id = tr['link_page_id']
    tmp_list = [pid, at, text, start_line_id, start_offset, end_line_id, end_offset, link_id]
    return tmp_list


def setstr2list(set_str, log_info):
    """
    convert set-like string to link
    :param set_str:
    :param log_info:
    :return:
    """
    import re
    import logging
    logger = ljc.set_logging(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    new_string = re.sub('[{}\' ]', '', set_str)
    new_list = new_string.split(',')
    return new_list


def liststr2list(list_str, log_info):
    """
    convert list-like string to list
    :param list_str:
    :param log_info:
    :return:
    """
    import re
    import logging
    logger = ljc.set_logging(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    new_string = re.sub('[\[\]\' ]', '', list_str)
    new_list = new_string.split(',')
    return new_list


def gen_linked_tsv(linked_json_dir, title2pid_ext_file, log_info, **d_cnv):
    """Convert linked json file (with title) to linked tsv file
       add ene category of page, title of linked page, ene category of linked paged using title2pid_ext_file

    args:
        linked_json_dir
        title2pid_ext_file
        log_info
        **d_cnv

    output:
        linked_tsv (tsv)
            format
                cat, pageid, title, attribute, text, start_line_id, start_offset, end_line_id, end_offset, link_pageid,
                link_page_title, linked_cat
    notice
    　　basically the same as gen_linked_tsv_mod except filtering by mod_list_file
        '\n' in text(mention) has been converted to '\\n'.
    """

    import json
    import pandas as pd
    from glob import glob
    import re
    import datetime

    import logging
    logger = ljc.set_logging(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    logger.info({
        'action': 'gen_linked_tsv',
        'linked_json_dir': linked_json_dir,
    })
    get_title = {}
    get_eneid_set = {}

    with open(title2pid_ext_file, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        for rows in reader:
            # to_pid_str -> to_title
            get_title[rows[1]] = rows[2]
            # to_pid_str -> to_eneid_setstr
            get_eneid_set[rows[1]] = rows[4]

    linked_json_files = linked_json_dir + '*.jsonl'

    print(datetime.datetime.now())

    for linked_json in glob(linked_json_files):
        if 'for_view' in linked_json:
            logger.error({
                'action': 'cnv_ene_pageid',
                'msg': 'illegal file: for_view',
            })
            sys.exit()
        go_list = []
        if '_dist.jsonl' in linked_json:
            linked_tsv = linked_json.replace('_dist.jsonl', '.tsv')
        else:
            linked_tsv = linked_json.replace('.jsonl', '.tsv')

        with open(linked_json, mode='r', encoding='utf-8') as g, open(linked_tsv, 'w', encoding='utf-8') as o:
            for g_line in g:
                g_key_list = []
                d_gline = json.loads(g_line)
                g_key_list = get_key_list_with_ene_title(log_info, **d_gline)

                ene_label = ''
                cat = ''
                check_dic_key(g_key_list[0], log_info, **d_cnv)
                cat = d_cnv[g_key_list[0]]
                g_key_list[0] = cat

                text_pre = g_key_list[4]
                g_key_list[4] = '\\n'.join(text_pre.splitlines())

                g_link_pageid = g_key_list[9]
                g_link_title = ''
                g_link_ene = ''
                if get_title.get(g_link_pageid):
                    g_link_title = get_title[g_link_pageid]

                g_key_list.insert(10, g_link_title)
                g_link_ecat_list = []

                g_link_eneid_list = []
                if g_link_pageid:
                    if get_eneid_set.get(g_link_pageid):
                        g_link_eneid_list = setstr2list(get_eneid_set[g_link_pageid], log_info)

                        for g_link_eneid in g_link_eneid_list:
                            check_dic_key(g_link_eneid, log_info, **d_cnv)

                            g_link_ecat = d_cnv[g_link_eneid]
                            g_link_ecat_list.append(g_link_ecat)

                g_key_list.insert(11, g_link_ecat_list)
                g_key_list.insert(11, g_link_eneid_list)

                go_list.append(g_key_list)

            df_go = pd.DataFrame(go_list)
            df_go.to_csv(o, sep='\t', header=False, index=False)


def get_key_list_with_ene_title(log_info, **tr):
    """get key list from input json dictionary to distinguish each record
       The dictionary should include title of the page as key
    args:
        log_info
        **tr
    return:
        tmp_list
            format: [eneid, pageid, title, attribute, text, start_line_id, start_offset, end_line_id, end_offset,
            link_id]
    """

    import sys
    import logging
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)

    try:
        pid = tr['page_id']
    except (KeyError, ValueError) as ex:
        logger.error({
            'action': 'get_key_list_with_ene_title',
            'error(pid)': ex,
            'tr': tr
        })
        sys.exit()
    try:
        title = tr['title']
    except (KeyError, ValueError) as ex:
        logger.error({
            'action': 'get_key_list_with_ene_title',
            'error(title)': ex,
            'tr': tr
        })
        sys.exit()
    try:
        eneid = tr['ENE']
    except (KeyError, ValueError) as ex:
        logger.error({
            'action': 'get_key_list_with_ene_title',
            'error(ene)': ex,
            'tr': tr
        })
        sys.exit()
    try:
        at = tr['attribute']
    except (KeyError, ValueError) as ex:
        logger.error({
            'action(attribute)': 'get_key_list_with_ene_title',
            'error': ex,
            'tr': tr
        })
        sys.exit()

    if 'text_offset' not in tr:
        logger.error({
            'action': 'get_key_list_with_ene_title',
            'error': 'format_error: text_offset',
            'tr': tr
        })
        sys.exit()
    else:
        if 'start' not in tr['text_offset']:
            logger.error({
                'action': 'get_key_list_with_ene_title',
                'error': 'format_error: start(text_offset)',
                'tr': tr
            })
            sys.exit()
        else:
            if 'line_id' not in tr['text_offset']['start']:
                logger.error({
                    'action': 'get_key_list_with_ene_title',
                    'error': 'format_error: line_id(start)',
                    'tr': tr
                })
                sys.exit()
            else:
                start_line_id = str(tr['text_offset']['start']['line_id'])

            if 'offset' not in tr['text_offset']['start']:
                logger.error({
                    'action': 'get_key_list_with_ene_title',
                    'error': 'format_error: offset(start)',
                    'tr': tr
                })
                sys.exit()
            else:
                start_offset = str(tr['text_offset']['start']['offset'])

        if 'end' not in tr['text_offset']:
            logger.error({
                'action': 'get_key_list_with_ene_title',
                'error': 'format_error: end(text_offset)',
                'tr': tr
            })
            sys.exit()
        else:
            if 'line_id' not in tr['text_offset']['end']:
                logger.error({
                    'action': 'get_key_list_with_ene_title',
                    'error': 'format_error: line_id(end)',
                    'tr': tr
                })
                sys.exit()
            else:
                end_line_id = str(tr['text_offset']['end']['line_id'])

            if 'offset' not in tr['text_offset']['end']:
                logger.error({
                    'action': 'get_key_list_with_ene_title',
                    'error': 'format_error: offset(end)',
                    'tr': tr
                })
                sys.exit()
            else:
                end_offset = str(tr['text_offset']['end']['offset'])

            if 'text' not in tr['text_offset']:
                logger.error({
                    'action': 'get_key_list_with_ene_title',
                    'error': 'format_error: text(text_offset)',
                    'tr': tr
                })
                sys.exit()
            else:
                text = tr['text_offset']['text']

    if 'link_page_id' not in tr:
        link_id = None
    else:
        link_id = tr['link_page_id']

    tmp_list = [eneid, pid, title, at, text, start_line_id, start_offset, end_line_id, end_offset, link_id]
    return tmp_list


def reg_all_cat_info(all_cat_info, log_info):
    """
    register eneid and en_label to dictionary
    :param all_cat_info:
    :param log_info:
    :return: ene_dict
    :notice:
    all_cat_info
        format: eneid, enlabel_ja, enlabel_en
    """
    import csv
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)

    with open(all_cat_info, mode='r', encoding='utf-8') as ta:
        ta_reader = csv.reader(ta, delimiter='\t')

        ene_dict = {}
        for ta_line in ta_reader:
            en_label = ta_line[2]
            eid = ta_line[0]
            ene_dict[eid] = en_label

        return ene_dict


def reg_target_attr_info(target_attr_info, log_info):
    """
    register eneid and en_label to dictionary
    :param target_attr_info:
    :param log_info:
    :return: ene_dict
    """
    import csv
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)

    with open(target_attr_info, mode='r', encoding='utf-8') as ta:
        ta_reader = csv.reader(ta, delimiter='\t')

        ene_dict = {}
        for ta_line in ta_reader:
            en_label = ta_line[2]
            eid = ta_line[0]
            ene_dict[eid] = en_label
        return ene_dict


def extract_cat(filename, log_info):
    """Extract category name from filename(*.json/*.jsonl)

    :param filename:
    :param log_info:
    :return:
        cat
    """
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)
    cat = ''
    if 'dist.jsonl' in filename:
        cat = filename.replace('_dist.jsonl', '')
    elif '.jsonl' in filename:
        cat = filename.replace('.jsonl', '')
    elif 'dist.json' in filename:
        cat = filename.replace('_dist.json', '')
    elif '.json' in filename:
        cat = filename.replace('_dist.json', '')

    if cat == '':
        logger.error({
            'action': 'lc.extract_cat',
            'msg': 'file name error (neither json nor jsonl)'
        })
    return cat


def reg_title2pid_ext(title2pid_ext_file, log_info):
    """Register title2pid_info pages info.
    Args:
        title2pid_ext_file
        log_info
    Returns:
        d_title2pid
            # format
                key: from_title
                val: to_pid
        d_pid_title_incoming_eneid
            # format
                key: to_pid
                val: to_title, to_incoming, to_eneid
    Notice:
        - title2pid_title_ex
            format: 'from_title'\t'to_pid'\t'to_title'\t'to_incoming\t'to_eneid'

    """
    import csv
    logger = ljc.set_logging(log_info, 'myLogger')
    logger.setLevel(logging.INFO)

    d_title2pid = {}
    d_pid_title_incoming_eneid = {}

    with open(title2pid_ext_file, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            from_title = row[0]
            to_pid = str(row[1])
            to_title = row[2]
            to_incoming = row[3]
            to_eneid = str(row[4])
            d_title2pid[from_title] = to_pid

            d_pid_title_incoming_eneid[to_pid] = [to_title, to_incoming, to_eneid]

    return d_title2pid, d_pid_title_incoming_eneid


def list2tsv(filename, two_d_list):
    with open(filename, mode='w', encoding='utf-8') as ef:
        e_writer = csv.writer(ef, delimiter='\t', lineterminator='\n')
        e_writer.writerows(two_d_list)


def dict2tsv(filename, **d):
    with open(filename, mode='w', encoding='utf-8') as ff:
        d_writer = csv.writer(ff, delimiter='\t', lineterminator='\n')
        for k, v in d.items():
            d_writer.writerow([k, v])
