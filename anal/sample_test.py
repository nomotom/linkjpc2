import logging


class LogInfo(object):
    log_file_name_default = 'anal.log'
    logging_ini_default = './logging_anal.ini'

    def __init__(self,
                 logging_ini=logging_ini_default):
        self.logging_ini = logging_ini


def set_logging(log_info, slogger_name):
    from os import path
    from logging import getLogger, config

    logging_ini = log_info.logging_ini
    log_file_path = path.join(path.dirname(path.abspath(__file__)), logging_ini)
    logging.config.fileConfig(log_file_path)

    slogger = logging.getLogger(slogger_name)
    return slogger


def get_key_full(log_info, **tr):
    # 準一致の情報も取得

    # print('(get_key_full)tr', tr )
    # print('(get_key_full)tr', tr )
    # import evaluation_linkjp as el
    import sys
    import logging

    logger = set_logging(log_info, 'myAnalLogger')
    # logger = el.set_logging(log_info, 'myAnalLogger')
    logger.setLevel(logging.INFO)

    try:
        pid = tr['page_id']
    except (KeyError, ValueError) as ex:
        print("{}".format(ex), 'page_id', tr)
        sys.exit()

    try:
        at = tr['attribute']
    except (KeyError, ValueError) as ex:
        print("{}".format(ex), 'attribute', tr)
        sys.exit()

    if 'text_offset' not in tr:
        raise KeyError('(get_key_full)format_error: text_offset', tr)
        # sys.exit()
    else:
        if 'start' not in tr['text_offset']:
            raise KeyError('(get_key_full)format_error: start', tr)
        else:
            if 'line_id' not in tr['text_offset']['start']:
                raise KeyError('(get_key_full)format_error: line_id', tr)
            else:
                start_line_id = str(tr['text_offset']['start']['line_id'])

            if 'offset' not in tr['text_offset']['start']:
                raise KeyError('(get_key_full)format_error: offset', tr)
            else:
                start_offset = str(tr['text_offset']['start']['offset'])

        if 'end' not in tr['text_offset']:
            raise KeyError('(get_key_full)format_error: end', tr)
        else:
            if 'line_id' not in tr['text_offset']['end']:
                raise KeyError('(get_key_full)format_error: line_id', tr)
            else:
                end_line_id = str(tr['text_offset']['end']['line_id'])

            if 'offset' not in tr['text_offset']['end']:
                raise KeyError('(get_key_full)format_error: offset', tr)
            else:
                end_offset = str(tr['text_offset']['end']['offset'])

            if 'text' not in tr['text_offset']:
                raise KeyError('(get_key_full)format_error: text', tr)
            else:
                text = tr['text_offset']['text']
                logger.debug({
                    'action': 'get_key_full',
                    'pid': pid,
                    'text': text,
                    'tr': tr
                })
    link_id = ''
    later_name = ''
    part_of = ''
    derivation_of = ''
    if 'link_page_id' in tr:
        link_id = tr['link_page_id']

        if 'link_type' not in tr:
            logger.error({
                'action': 'get_key_full',
                'error': '(get_key_full)format_error: link_type',
                'tr': tr
            })
            sys.exit()
        else:
            if 'later_name' not in tr['link_type']:
                logger.error({
                    'action': 'get_key_full',
                    'error': '(get_key_full)format_error: later_name',
                    'tr': tr
                })
                sys.exit()
            else:
                if not tr['link_type'].get('later_name'):
                    later_name = ''
                else:
                    later_name = tr['link_type']['later_name']
            if 'part_of' not in tr['link_type']:
                logger.error({
                    'action': 'get_key_full',
                    'error': '(get_key_full)format_error: part_of',
                    'tr': tr
                })
                sys.exit()
            else:
                if not tr['link_type'].get('part_of'):
                    part_of = ''
                else:
                    part_of = tr['link_type']['part_of']
            if 'derivation_of' not in tr:
                logger.error({
                    'action': 'get_key_full',
                    'error': '(get_key_full)format_error: derivation_of',
                    'tr': tr
                })
                sys.exit()
            else:
                if not tr['link_type'].get('derivation_of'):
                    derivation_of = ''
                else:
                    derivation_of = tr['link_type']['derivation_of']
    tmp_list = [pid, at, text, start_line_id, start_offset, end_line_id, end_offset, link_id, later_name, part_of, derivation_of]

    tmp_str = '\t'.join(tmp_list)
    return tmp_str


def get_key_plus(log_info, **tr):


    # print('(get_key_plus)tr', tr )
    # print('(get_key_plus)tr', tr )
    #import evaluation_linkjp as el
    import sys
    import logging

    #logger = el.set_logging(log_info, 'myAnalLogger')
    logger = set_logging(log_info, 'myAnalLogger')
    logger.setLevel(logging.INFO)

    try:
        pid = tr['page_id']
    except (KeyError, ValueError) as ex:
        print("{}".format(ex), 'page_id', tr)
        sys.exit()

    try:
        at = tr['attribute']
    except (KeyError, ValueError) as ex:
        print("{}".format(ex), 'attribute', tr)
        sys.exit()

    if 'text_offset' not in tr:
        raise KeyError('(get_key_plus)format_error: text_offset', tr)
        # sys.exit()
    else:
        if 'start' not in tr['text_offset']:
            raise KeyError('(get_key_plus)format_error: start', tr)
        else:
            if 'line_id' not in tr['text_offset']['start']:
                raise KeyError('(get_key_plus)format_error: line_id', tr)
            else:
                start_line_id = str(tr['text_offset']['start']['line_id'])

            if 'offset' not in tr['text_offset']['start']:
                raise KeyError('(get_key_plus)format_error: offset', tr)
            else:
                start_offset = str(tr['text_offset']['start']['offset'])

        if 'end' not in tr['text_offset']:
            raise KeyError('(get_key_plus)format_error: end', tr)
        else:
            if 'line_id' not in tr['text_offset']['end']:
                raise KeyError('(get_key_plus)format_error: line_id', tr)
            else:
                end_line_id = str(tr['text_offset']['end']['line_id'])

            if 'offset' not in tr['text_offset']['end']:
                raise KeyError('(get_key_plus)format_error: offset', tr)
            else:
                end_offset = str(tr['text_offset']['end']['offset'])

            if 'text' not in tr['text_offset']:
                raise KeyError('(get_key_plus)format_error: text', tr)
            else:
                text = tr['text_offset']['text']
                logger.debug({
                    'action': 'get_key_plus',
                    'pid': pid,
                    'text': text,
                    'tr': tr
                })

    if 'link_page_id' not in tr:
        link_id = ''
    else:
        link_id = tr['link_page_id']

    tmp_list = [pid, at, text, start_line_id, start_offset, end_line_id, end_offset, link_id]

    tmp_str = '\t'.join(tmp_list)
    return tmp_str


def get_key(log_info, **tr):

    # print('(get_key)tr', tr )
    # print('(get_key)tr', tr )
    # import evaluation_linkjp as el
    import sys
    import logging
    logger = set_logging(log_info, 'myAnalLogger')
    logger.setLevel(logging.INFO)

    try:
        pid = tr['page_id']
    except (KeyError, ValueError) as ex:
        logger.error({
            'action': 'get_key',
            'error': ex,
            'tr': tr
        })
        sys.exit()

    try:
        at = tr['attribute']
    except (KeyError, ValueError) as ex:
        logger.error({
            'action': 'get_key',
            'error': ex,
            'tr': tr
        })
        sys.exit()

    if 'text_offset' not in tr:
        logger.error({
            'action': 'get_key',
            'error': 'format_error: text_offset',
            'tr': tr
        })
        sys.exit()
    else:
        if 'start' not in tr['text_offset']:
            logger.error({
                'action': 'get_key',
                'error': 'format_error: start(text_offset)',
                'tr': tr
            })
            sys.exit()
        else:
            if 'line_id' not in tr['text_offset']['start']:
                logger.error({
                    'action': 'get_key',
                    'error': 'format_error: line_id(start)',
                    'tr': tr
                })
                sys.exit()
            else:
                start_line_id = str(tr['text_offset']['start']['line_id'])

            if 'offset' not in tr['text_offset']['start']:
                logger.error({
                    'action': 'get_key',
                    'error': 'format_error: offset(start)',
                    'tr': tr
                })
                sys.exit()
            else:
                start_offset = str(tr['text_offset']['start']['offset'])

        if 'end' not in tr['text_offset']:
            logger.error({
                'action': 'get_key',
                'error': 'format_error: end(text_offset)',
                'tr': tr
            })
            sys.exit()
        else:
            if 'line_id' not in tr['text_offset']['end']:
                logger.error({
                    'action': 'get_key',
                    'error': 'format_error: line_id(end)',
                    'tr': tr
                })
                sys.exit()
            else:
                end_line_id = str(tr['text_offset']['end']['line_id'])

            if 'offset' not in tr['text_offset']['end']:
                logger.error({
                    'action': 'get_key',
                    'error': 'format_error: offset(end)',
                    'tr': tr
                })
                sys.exit()
            else:
                end_offset = str(tr['text_offset']['end']['offset'])

            if 'text' not in tr['text_offset']:
                logger.error({
                    'action': 'get_key',
                    'error': 'format_error: text(text_offset)',
                    'tr': tr
                })
                sys.exit()
            else:
                text = tr['text_offset']['text']

    tmp_list = [pid, at, text, start_line_id, start_offset, end_line_id, end_offset]

    tmp_str = '\t'.join(tmp_list)
    return tmp_str