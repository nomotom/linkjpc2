import linkjpc as ljc
import config as cf
import logging
import csv
import sys

# def check_dic_key(keyword, **dic):
def check_dic_key(keyword, log_info, **dic):
    """
    :param keyword:
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
# def linkedjson2tsv_add_linked_title(linked_json_dir, title2pid_ext_file, log_info):
#     """Convert linked json file (with title) to linked tsv file
#        add title of linked page using title2pid_ext_file
#
#     args:
#         linked_json_dir
#         title2pid_ext_file
#         log_info
#     output:
#         linked_tsv (tsv)
#             format
#                 cat, pageid, title, attribute, text, start_line_id, start_offset, end_line_id, end_offset,
#                 link_pageid, link_page_title
#             sample
#                 Person 2392906	桐谷華	地位職業	声優	38	20	38	22	1192	声優
#     notice
#         '\n' in text(mention) has been converted to '\\n'.
#         f_title2pid_ext
#             format
#                 (title(from page))\t(pageid(to page))\t(title(to page)\t(maximum number of incoming links(to page))
#                 \t(eneid(to_page))
#             sample
#                 アメリカ合衆国  1698838 アメリカ合衆国  116818  1.5.1.3
#                 ユナイテッドステイツ    1698838 アメリカ合衆国  116818  1.5.1.3
#     """
#
#     import json
#     import pandas as pd
#     from glob import glob
#
#     import logging
#     logger = set_logging_pre(log_info, 'myPreLogger')
#     logger.setLevel(logging.INFO)
#
#     logger.info({
#         'action': 'linkedjson2tsv_add_linked_title',
#         'linked_json_dir': linked_json_dir,
#         # 'title2pid_org_file': title2pid_org_file,
#     })
#     get_title = {}
#
#     with open(title2pid_ext_file, mode='r', encoding='utf-8') as f:
#
#         reader = csv.reader(f, delimiter='\t')
#         for rows in reader:
#             to_title = rows[2]
#             to_pid_str = rows[1]
#
#             get_title[to_pid_str] = to_title
#             # # 20220916
#             # get_pid[to_title] = to_pid_str
#     # linked_json_files = linked_json_dir + '*.json'
#     linked_json_files = linked_json_dir + '*.jsonl'
#
#     for linked_json in glob(linked_json_files):
#         if 'for_view' in linked_json:
#             logger.error({
#                 'action': 'cnv_ene_pageid',
#                 'msg': 'illegal file: for_view',
#             })
#             sys.exit()
#         go_list = []
#         # linked_tsv = linked_json.replace('.json', '.tsv')
#         if '_dist.jsonl' in linked_json:
#             linked_tsv = linked_json.replace('_dist.jsonl', '.tsv')
#         else:
#             linked_tsv = linked_json.replace('.jsonl', '.tsv')
#         # 20220825
#         cat_pre = linked_tsv.replace(linked_json_dir, '')
#         cat = cat_pre.replace('.tsv', '')
#
#         with open(linked_json, mode='r', encoding='utf-8') as g, open(linked_tsv, 'w', encoding='utf-8') as o:
#             for g_line in g:
#                 g_key_list = []
#                 d_gline = json.loads(g_line)
#                 g_key_list = get_key_list_with_title(log_info, **d_gline)
#                 # g_key_list = [pid, title, at, text, start_line_id, start_offset, end_line_id, end_offset, link_id]
#
#                 logger.debug({
#                     'action': 'linkedjson2tsv_add_linked_title',
#                     'g_key_list': g_key_list,
#                 })
#
#                 # in case of multiple lines
#                 # text_pre = g_key_list[4]
#                 text_pre = g_key_list[3]
#
#                 # 20220826
#                 # g_key_list[4] = '\\n'.join(text_pre.splitlines())
#                 g_key_list[3] = '\\n'.join(text_pre.splitlines())
#
#                 # g_key_list[4] = '\n'.join(text_pre.splitlines())
#                 # till here
#                 # if 'つまり' in g_key_list[3] or '要するに' in g_key_list[3] or 'たとえば' in g_key_list[3]:
#                 #     print('key_list_3', g_key_list[3])
#
#                 # 20220826
#                 g_link_pageid = g_key_list[8]
#                 g_link_title = ''
#                 if get_title.get(g_link_pageid):
#                     g_link_title = get_title[g_link_pageid]
#                 g_key_list.insert(9, g_link_title)
#                 # 20220825
#                 g_key_list.insert(0, cat)
#
#                 # g_title_pageid = g_key_list[0]
#                 # if get_title.get(g_title_pageid):
#                 #      g_org_title = get_title[g_title_pageid]
#                 #      g_key_list.insert(1, g_org_title)
#                 # logger.debug({
#                 #     'action': 'linkedjson2tsv_add_linked_title',
#                 #     'text_pre': text_pre,
#                 #     'cat': cat,
#                 #     'g_link_pageid': g_link_pageid,
#                 #     # 'g_link_title': g_link_title,
#                 #     # 'g_org_title': g_org_title,
#                 # })
#                 logger.debug({
#                     'action': 'linkedjson2tsv_add_linked_title',
#                     'g_key_list': g_key_list,
#                 })
#                 #  'g_key_list': ['Style', '2847831', '為我流', '活動地域', '茨城県', '56', '0', '56', '3', '774349',
#                 #  '茨城県']}
#                 # 'g_key_list': ['Styl_orge', '2847831', '為我流', '統括組織', '為我流和術保存会', '56', '6', '56', '14',
#                 # None, '']}
#                 # g_key_list = [cat, pid, title, at, text, start_line_id, start_offset, end_line_id, end_offset,
#                 # link_id]
#                 go_list.append(g_key_list)
#
#             df_go = pd.DataFrame(go_list)
#             df_go.to_csv(o, sep='\t', header=False, index=False)


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
            sample
                2392906	桐谷華	地位職業	声優	38	20	38	22	1192	声優
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
            # if 'page_id' not in rd:
            #     logger.error({
            #         'action': 'linkedjson2tsv',
            #         'error': 'missing page_id'
            #     })
            #     sys.exit()
            if not rd['page_id']:
                logger.error({
                    'action': 'linkedjson2tsv',
                    'error': 'page_id null'
                })
                sys.exit()
            else:
                pid = str(rd['page_id'])
            # title (not forwarded page)
            check_dic_key('title', log_info, **rd)
            # if 'title' not in rd:
            #     logger.error({
            #         'action': 'linkedjson2tsv',
            #         'error': 'title not in rd',
            #         'rline': rline
            #     })
            #     sys.exit()
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

    # linked_json_files = linked_json_dir + '*.json'
    linked_json_files = linked_json_dir + '*.jsonl'

    for linked_json in glob(linked_json_files):
        if 'for_view' in linked_json:
            logger.error({
                'action': 'cnv_ene_pageid',
                'msg': 'illegal file: for_view',
            })
            sys.exit()
        go_list = []
        # linked_tsv = linked_json.replace('.json', '.tsv')
        if '_dist.jsonl' in linked_json:
            linked_tsv = linked_json.replace('_dist.jsonl', '.tsv')
        else:
            linked_tsv = linked_json.replace('.jsonl', '.tsv')

        with open(linked_json, mode='r', encoding='utf-8') as g, open(linked_tsv, 'w', encoding='utf-8') as o:
            for g_line in g:
                d_gline = json.loads(g_line)
                # titleがある場合はg_key_list_with_titleを使う
                g_key_list = get_key_list(log_info, **d_gline)
                g_link_pageid = g_key_list[7]
                # in case of multiple lines
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

    logger.debug({
        'action': 'get_key_list_with_title',
        'pid': pid,
        'title': title,
        'at': at,
        'text': text,
        'start_line_id': start_line_id,
        'start_offset': start_offset,
        'end_line_id': end_line_id,
        'end_offset': end_offset,
        'link_id': link_id
    })
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

    :param set_str:
    :param log_info:
    :return:
    """
    import re
    import logging
    logger = ljc.set_logging(log_info, 'myPreLogger')
    logger.setLevel(logging.INFO)

    new_string  = re.sub('[{}\' ]', '', set_str)
    new_list = new_string.split(',')
    return new_list


def liststr2list(list_str, log_info):
    """

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
            sample
                Person 2392906	桐谷華	地位職業	声優	38	20	38	22	1192	声優　　　地位職業名
    notice
    　　basically the same as gen_linked_tsv_mod except filtering by mod_list_file
        '\n' in text(mention) has been converted to '\\n'.
        f_title2pid_ext
            format
                (title(from page))\t(pageid(to page))\t(title(to page)\t(maximum number of incoming links(to page))
                \t(eneid_set(to_page))
            sample
                VIAF    2503159 バーチャル国際典拠ファイル      212754  {'1.7.0'}

        linked_json
            sample
            {"page_id": "1008136", "title": "ジェイ・デメリット", "attribute": "国籍", "ENE": "1.1",
            "text_offset": {"start": {"line_id": 45, "offset": 26}, "end": {"line_id": 45, "offset": 32},
            "text": "イングランド"}, "html_offset": {"start": {"line_id": 45, "offset": 478},
            "end": {"line_id": 45, "offset": 484}, "text": "イングランド"}, "link_page_id": "16627",
            "link_type": {"later_name": false, "part_of": false, "derivation_of": false}}


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
        # 'title2pid_org_file': title2pid_org_file,
    })
    get_title = {}
    get_eneid_set = {}

    # check_mod = {}
    # with open(mod_list_file, 'r', encoding='utf-8') as ml:
    #     ml_reader = csv.reader(ml, delimiter='\t')
    #     for ml_line in ml_reader:
    #         cat = ml_line[0]
    #         pid = ml_line[1]
    #         attr = ml_line[2]
    #         mention = ml_line[3]
    #         tmp_key = ':'.join([cat, pid, attr, mention])
    #         if tmp_key not in check_mod:
    #             check_mod[tmp_key] = 1

    with open(title2pid_ext_file, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        # VIAF    2503159 バーチャル国際典拠ファイル      212754  {'1.7.0'}
        for rows in reader:
            # to_pid_str -> to_title
            get_title[rows[1]] = rows[2]
            # to_pid_str -> to_eneid_setstr
            get_eneid_set[rows[1]] = rows[4]
            logger.debug({
                'action': 'gen_linked_tsv_mod',
                'to_pid_str(rows[1])': rows[1],
                'to_title(rows[2])': rows[2],
                'to_eneid_set_str(rows[4])': rows[4],
                'type(rows[4])': type(rows[4]),
            })
            # # 20220916
            # get_pid[to_title] = to_pid_str
    # linked_json_files = linked_json_dir + '*.json'
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
        # linked_tsv = linked_json.replace('.json', '.tsv')
        if '_dist.jsonl' in linked_json:
            linked_tsv = linked_json.replace('_dist.jsonl', '.tsv')
        else:
            linked_tsv = linked_json.replace('.jsonl', '.tsv')
        # 20220825
        # 20220929
        # cat_pre = linked_tsv.replace(linked_json_dir, '')
        # cat = cat_pre.replace('.tsv', '')

        with open(linked_json, mode='r', encoding='utf-8') as g, open(linked_tsv, 'w', encoding='utf-8') as o:
            logger.debug({
                'action': 'gen_linked_tsv',
                'linked_json': linked_json,
                'linked_tsv': linked_tsv,
                'rows[4]': rows[4],
                'type(rows[4])': type(rows[4]),
            })
            for g_line in g:
                g_key_list = []
                d_gline = json.loads(g_line)
                g_key_list = get_key_list_with_ene_title(log_info, **d_gline)
                # [eneid, pid, title, at, text, start_line_id, start_offset, end_line_id, end_offset, link_id]

                logger.debug({
                    'action': 'gen_linked_tsv',
                    'g_key_list(org)': g_key_list
                })
                #  ['1.6.4.16', '725957', '西鉄香椎花園', 'アトラクション', 'ふわふわぞうさん',
                # '94', '0', '94', '8', None]}
                #  ['1.7.13.0', '596942', '雷切', '種類', '日本刀', '47', '26', '47', '29', '36305']}

                ene_label = ''
                cat = ''
                check_dic_key(g_key_list[0], log_info, **d_cnv)
                # if g_key_list[0] in d_cnv:
                cat = d_cnv[g_key_list[0]]
                g_key_list[0] = cat

                logger.debug({
                    'action': 'gen_linked_tsv',
                    'cat': cat,
                    'g_key_list[0]': g_key_list[0],
                    'g_key_list': g_key_list
                })
                # ['Company_Group', '1240793', 'リング・テムコ・ボート', 'もとになった組織', '1947年にジェームズ・リングによって、
                # ic Company ）を創業したことに起源を発する', '49', '0', '49', '81', None]}

                # in case of multiple lines
                # text_pre = g_key_list[4]
                text_pre = g_key_list[4]
                g_key_list[4] = '\\n'.join(text_pre.splitlines())

                # tmp_cat_pid_attr_mention = ':'.join([cat, g_key_list[1], g_key_list[3], g_key_list[4]])
                # if tmp_cat_pid_attr_mention in check_mod:
                #     logger.debug({
                #         'action': 'gen_linked_tsv_mod',
                #         'msg': 'skipped based on mod_list',
                #         'tmp_cat_pid_attr_mention': tmp_cat_pid_attr_mention
                #     })
                #     continue
                # ng
                # 20220826
                g_link_pageid = g_key_list[9]
                logger.debug({
                    'action': 'gen_linked_tsv',
                    'g_link_pageid': g_link_pageid
                })
                g_link_title = ''
                g_link_ene = ''
                if get_title.get(g_link_pageid):
                    g_link_title = get_title[g_link_pageid]
                    logger.debug({
                        'action': 'gen_linked_tsv',
                        'g_link_title': g_link_title,
                        'g_link_pageid': g_link_pageid
                    })
                    # 'g_link_title': 'ミサイル巡洋艦', 'g_link_pageid': '742148'}
                logger.debug({
                    'action': 'gen_linked_tsv',
                    'g_key_list(2)': g_key_list
                })
                g_key_list.insert(10, g_link_title)
                logger.debug({
                    'action': 'gen_linked_tsv',
                    'g_key_list(2-1)': g_key_list
                })
                # 'g_link_title': '指令誘導', 'g_key_list': ['Weapon_Other', '1223107', 'シーウルフ (ミサイル)', 'CLOS',
                # 'CLOS', '110', '8', '110', '12', '2598129', '指令誘導']}
                # 20220921
                # g_link_cat = ''
                # g_link_ecat_set= set()
                g_link_ecat_list = []

                # g_link_eneid_set = set()
                g_link_eneid_list = []
                if g_link_pageid:
                    if get_eneid_set.get(g_link_pageid):
                        g_link_eneid_list = setstr2list(get_eneid_set[g_link_pageid], log_info)

                        logger.debug({
                            'action': 'gen_linked_tsv',
                            'g_link_pageid': g_link_pageid,
                            'g_link_eneid_list': g_link_eneid_list,
                            'type(g_link_eneid_list)': type(g_link_eneid_list)
                        })
                        for g_link_eneid in g_link_eneid_list:
                            logger.debug({
                                'action': 'gen_linked_tsv',
                                'g_link_eneid': g_link_eneid
                            })

                            check_dic_key(g_link_eneid, log_info, **d_cnv)

                            g_link_ecat = d_cnv[g_link_eneid]
                            # g_link_ecat_set.add(g_link_ecat)
                            g_link_ecat_list.append(g_link_ecat)

                # g_key_list.insert(11, g_link_ecat_set)
                g_key_list.insert(11, g_link_ecat_list)
                # g_key_list.insert(11, g_link_eneid_set)
                g_key_list.insert(11, g_link_eneid_list)

                # 20220825
                # g_key_list.insert(0, cat)

                logger.debug({
                    'action': 'gen_linked_tsv',
                    'g_key_list': g_key_list,
                })
                #  'g_key_list': ['Constellation', '47047', 'へびつかい座', '隣接する星座', 'へび座',
                #  '110', '0', '110', '3', '47046', 'へび座', {'1.5.4.5'}, {'Constellation'} ]}
                go_list.append(g_key_list)

            df_go = pd.DataFrame(go_list)
            df_go.to_csv(o, sep='\t', header=False, index=False)

# def linkedjson2tsv_add_linked_title_ene_cnv_year(linked_json_dir, title2pid_ext_file, title2pid_ext_obs_file, log_info,
#                                                  **d_cnv
#                                                  ):
#     """Convert linked json file (with title) to linked tsv file
#        add title of linked page using title2pid_ext_file
#        Wikipedia pid of gold link should be modified from title2pid_ext_obs_file to title2pid_ext_file,
#
#     args:
#         linked_json_dir
#         title2pid_ext_file
#         title2pid_ext_obs_file
#         log_info
#         **d_cnv
#     output:
#         linked_tsv (tsv)
#             format
#                 cat, pageid, title, attribute, text, start_line_id, start_offset, end_line_id, end_offset, link_pageid,
#                 link_page_title, linked cat
#             sample
#                 Person 2392906	桐谷華	地位職業	声優	38	20	38	22	1192	声優
#     notice
#         '\n' in text(mention) has been converted to '\\n'.
#         f_title2pid_ext
#             format
#                 (title(from page))\t(pageid(to page))\t(title(to page)\t(maximum number of incoming links(to page))
#                 \t(eneid(to_page))
#             sample
#                 アメリカ合衆国  1698838 アメリカ合衆国  116818  1.5.1.3
#                 ユナイテッドステイツ    1698838 アメリカ合衆国  116818  1.5.1.3
#     """
#
#     import json
#     import pandas as pd
#     from glob import glob
#
#     import logging
#     logger = ljc.set_logging(log_info, 'myLogger')
#     logger.setLevel(logging.INFO)
#
#     logger.info({
#         'action': 'linkedjson2tsv_add_linked_title_ene_cnv_year',
#         'linked_json_dir': linked_json_dir,
#         # 'title2pid_org_file': title2pid_org_file,
#     })
#     get_title = {}
#     get_eneid = {}
#     get_from_title_to_title = {}
#     wikipedia_cnv = 0
#     obs_ext_file = title2pid_ext_obs_file
#     new_ext_file = title2pid_ext_file
#
#     get_pid_new = {}
#     cnv_obs_pid_new_pid = {}
#
#     with open(new_ext_file, mode='r', encoding='utf-8') as nf:
#         reader = csv.reader(nf, delimiter='\t')
#         # ウィキウィキウェブ      18645   ウィキ  322112  1.7.6
#         for rows in reader:
#             # from_title_new = rows[0]
#             to_pid_new_str = rows[1]
#             to_title_new = rows[2]
#
#             get_title[to_pid_new_str] = to_title_new
#
#             # 20220916
#             get_pid_new[to_title_new] = to_pid_new_str
#             # get_pid_new[from_title_new] = to_pid_new_str
#
#             # 20221001
#             get_eneid[to_title_new] = rows[4]
#
#     with open(obs_ext_file, mode='r', encoding='utf-8') as of:
#
#         reader = csv.reader(of, delimiter='\t')
#         for rows in reader:
#             #    - from_title, to_pid, to_title, to_incoming, to_eneid (*.tsv)
#
#             # from_title = rows[0]
#             to_pid_str = rows[1]
#             to_title = rows[2]
#             # to_ene = rows[4]
#
#             if to_title in get_pid_new:
#                 to_pid_str_rev = get_pid_new[to_title]
#                 cnv_obs_pid_new_pid[to_pid_str] = to_pid_str_rev
#                 # get_ene[to_pid_str_rev] = to_ene
#                 logger.debug({
#                     'to_title': to_title,
#                     'to_pid_str': to_pid_str,
#                     'to_pid_str_rev': to_pid_str_rev,
#                     'cnv_obs_pid_new_pid[to_pid_str]': cnv_obs_pid_new_pid[to_pid_str],
#                 })
#
#     # linked_json_files = linked_json_dir + '*.json'
#     linked_json_files = linked_json_dir + '*.jsonl'
#
#     for linked_json in glob(linked_json_files):
#         if 'for_view' in linked_json:
#             logger.error({
#                 'action': 'cnv_ene_pageid',
#                 'msg': 'illegal file: for_view',
#             })
#             sys.exit()
#         go_list = []
#         # linked_tsv = linked_json.replace('.json', '.tsv')
#         if '_dist.jsonl' in linked_json:
#             linked_tsv = linked_json.replace('_dist.jsonl', '.tsv')
#         else:
#             linked_tsv = linked_json.replace('.jsonl', '.tsv')
#         # 20220825
#         # cat_pre = linked_tsv.replace(linked_json_dir, '')
#         # cat = cat_pre.replace('.tsv', '')
#         cat = ''
#         with open(linked_json, mode='r', encoding='utf-8') as g, open(linked_tsv, 'w', encoding='utf-8') as o:
#             for g_line in g:
#                 g_key_list = []
#                 d_gline = json.loads(g_line)
#                 g_key_list = get_key_list_with_ene_title(log_info, **d_gline)
#                 # g_key_list = [pid, title, at, text, start_line_id, start_offset, end_line_id, end_offset, link_id]
#
#                 # if '鹿島アントラーズ' in g_key_list:
#                 #     logger.info({
#                 #         'action': 'linkedjson2tsv_add_linked_title',
#                 #         'g_key_list': g_key_list,
#                 #     })
#                 # 'g_key_list': ['2332490', 'マルセリーナ', '別名', 'Marcellina', '46', '7', '46', '17', '2332490']}
#                 # 'g_key_list': ['1665409', '大迫勇也', '所属組織', '鹿島アントラーズ', '82', '4', '82', '12', '4670']}
#
#                 # g_link_pageid = g_key_list[8]
#                 ene_label = ''
#                 if g_key_list[0] in d_cnv:
#                     cat = d_cnv[g_key_list[0]]
#                     g_key_list[0] = cat
#                 else:
#                     logger.debug({
#                         'action': 'linkedjson2tsv_add_linked_title_ene_cnv_year',
#                         'msg': 'illegal ene',
#                         'g_key_list': g_key_list
#                     })
#                 # in case of multiple lines
#                 # text_pre = g_key_list[4]
#                 text_pre = g_key_list[4]
#
#                 # 20220826
#                 # g_key_list[4] = '\\n'.join(text_pre.splitlines())
#                 g_key_list[4] = '\\n'.join(text_pre.splitlines())
#                 g_link_pageid = g_key_list[9]
#
#                 # g_key_list[4] = '\n'.join(text_pre.splitlines())
#                 # till here
#                 # if 'つまり' in g_key_list[3] or '要するに' in g_key_list[3] or 'たとえば' in g_key_list[3]:
#                 #     print('key_list_3', g_key_list[3])
#
#                 # 20220826
#                 g_link_obs_pageid = g_key_list[9]
#
#                 if g_link_obs_pageid and g_link_obs_pageid in cnv_obs_pid_new_pid:
#                     g_link_new_pageid = cnv_obs_pid_new_pid[g_link_obs_pageid]
#                     logger.debug({
#                         'action': 'linkedjson2tsv_add_linked_title_ene_cnv_year',
#                         'g_key_list': g_key_list,
#                         'g_link_new_pageid': g_link_new_pageid
#                     })
#                 else:
#                     g_link_new_pageid = g_link_obs_pageid
#                 g_link_title = ''
#                 if get_title.get(g_link_new_pageid):
#                     g_link_title = get_title[g_link_new_pageid]
#                     logger.debug({
#                         'action': 'linkedjson2tsv_add_linked_title_ene_cnv_year',
#                         'g_link_title': g_link_title
#                     })
#                     #  'g_link_title': '機動戦士ガンダム エコール・デュ・シエル'}
#                 g_key_list[9] = g_link_new_pageid
#                 g_key_list.insert(10, g_link_title)
#                 # 20220825
#                 # g_key_list.insert(0, cat)
#                 g_link_cat = ''
#                 g_link_eneid = ''
#                 if get_eneid.get(g_link_new_pageid):
#                     g_link_eneid = get_eneid[g_link_new_pageid]
#                     g_link_cat = d_cnv[g_link_eneid]
#                     g_key_list.insert(11, g_link_cat)
#                     #g_key_list.insert(11, g_link_eneid)
#
#                 logger.debug({
#                     'action': 'linkedjson2tsv_add_linked_title_ene_cnv_year',
#                     'g_key_list': g_key_list,
#                 })
#
#                 go_list.append(g_key_list)
#
#             df_go = pd.DataFrame(go_list)
#             df_go.to_csv(o, sep='\t', header=False, index=False)
#

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

    logger.debug({
        'action': 'get_key_list_with_ene_title',
        'eneid': eneid,
        'pid': pid,
        'title': title,
        'at': at,
        'text': text,
        'start_line_id': start_line_id,
        'start_offset': start_offset,
        'end_line_id': end_line_id,
        'end_offset': end_offset,
        'link_id': link_id
    })
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
        sample: 1.4.4.1 国籍名  Nationality
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
            logging.debug({
                'action': 'reg_all_cat_info',
                'eid': eid,
                'en_label': en_label
            })
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
        #eg. イギリス語      3377    英語    95319   1.7.24.1
        log_info
    Returns:
        d_title2pid
            # format
                key: from_title
                val: to_pid
            # eg: {'イギリス語':'3377'}
        d_pid_title_incoming_eneid
            # format
                key: to_pid
                val: to_title, to_incoming, to_eneid
            # eg: {'3377': ['英語', 95319','1.7.24.1'])
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
