import config as cf
import os
import copy
import json
from glob import glob


in_dir = '/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/20210905/mint_p_02_incl_1/'
out_dir = '/Users/masako/Documents/SHINRA/2021-LinkJP/test_out_task2/20210905/mint_p_02_incl_1/'


in_files = in_dir + '*.json'
print('in_files', in_files)
for in_file in glob(in_files):
    rec_t2_out = []

    with open(in_file, mode='r', encoding='utf-8') as i:

        fname = in_file.replace(in_dir, '')
        ene_cat = fname.replace('.json', '')
        print('ene_cat:', ene_cat)
        outfile = out_dir + fname
        print('outfile:', outfile)

        for i_line in i:
            # tmp mention
            rec_t2 = json.loads(i_line)

            rec_t2['link_type'] = {}
            rec_t2['link_type']['part_of']= {}
            rec_t2['link_type']['later_name'] = {}
            rec_t2['link_type']['derivation_of'] = {}


            mention_info_task2 = cf.MentionInfoTask2(
                rec_t2['page_id'],
                ene_cat,
                rec_t2['attribute'],
                rec_t2['text_offset']['start']['line_id'],
                rec_t2['text_offset']['start']['offset'],
                rec_t2['text_offset']['end']['line_id'],
                rec_t2['text_offset']['end']['offset'],
                rec_t2['text_offset']['text'],
                rec_t2['html_offset']['start']['line_id'],
                rec_t2['html_offset']['start']['offset'],
                rec_t2['html_offset']['end']['line_id'],
                rec_t2['html_offset']['end']['offset'],
                rec_t2['html_offset']['text'],
                rec_t2['link_page_id'],
                '',
                '',
                ''
            )

            if '合併市区町村' in mention_info_task2.attr_label:
                mention_info_task2.link_type_part_of = True
                rec_t2['link_type']['part_of'] = True
            else:
                mention_info_task2.link_type_part_of = False
                rec_t2['link_type']['part_of'] = False

            if '旧称' in mention_info_task2.attr_label:
                mention_info_task2.link_type_later_name = True
                rec_t2['link_type']['later_name'] = True

            else:
                mention_info_task2.link_type_later_name = False
                rec_t2['link_type']['later_name'] = False


            mention_info_task2.link_type_derivation_of = False
            rec_t2['link_type']['derivation_of'] = False

            rec_t2_out.append(copy.deepcopy(rec_t2))


        try:
            os.makedirs(out_dir)
        except FileExistsError:
            pass
        with open(outfile, mode='w', encoding='utf-8') as o:
            for tline in rec_t2_out:
                json.dump(tline, o, ensure_ascii=False)
                o.write('\n')