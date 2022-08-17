import csv

# sys_dir_common = '/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/exp_systems/'

sys_dir_common = '/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/bert_aiprb_modules/'
# sys_dir_common = '/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/aiprb/'
# sys_dir_common = '/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/bert_rulebase_no_slink_attr/'
# sys_a = 'a_AIPRB_SMWL'
# sys_b = 'b_NAIST_only_bert'
# sys_c = '1_slink_05_mid'
# sys_d = '2_mint_e'
# sys_e = '3_wlink_rp_al_am_bl'
# sys_f = '4_l_06'
# sys_g = 'ATID_ATAG_SEARCH'
# sys_h = 'AIPCB_CBI'
# sys_i = 'amano_genre'

# sys_a = 'a_AIPRB_SMWL'
# sys_b = 'b_NAIST_BERT'
# sys_c = '1_slink'
# sys_d = '2_mint'
# sys_e = '3_wlink'
# sys_f = '4_linkp'

sys_a = 'a_AIPRB_SMWL'
sys_b = 'b_NAIST_BERT'

# sys_a = '1_slink'
# sys_b = '2_mint'
# sys_c = '3_wlink'
# sys_d = '4_linkp'
# sys_a = 'mint_e'
# sys_b = 'wlink_rp'
# sys_c = 'slink_05_mid'
# sys_d = 'l_06'

# sys_a = 'NAIST_only_bert'
# sys_b = 'AIPRB_SMWL'
# sys_list = [sys_a, sys_b, sys_c, sys_d, sys_e, sys_f, sys_g, sys_h, sys_i]
# sys_list = [sys_a, sys_b, sys_c, sys_d, sys_e, sys_f]
sys_list = [sys_a, sys_b]

# sys_list = [sys_a, sys_b, sys_c, sys_d, sys_e]

# sys_list = [sys_a, sys_b, sys_c, sys_d]

sys_a_reg = {}
sys_b_reg = {}
# sys_c_reg = {}
# sys_d_reg = {}
# sys_e_reg = {}
# sys_f_reg = {}
# sys_g_reg = {}
# sys_h_reg = {}
# sys_i_reg = ()
sys_all_reg = {}
# dict_list = [sys_a_reg, sys_b_reg, sys_c_reg, sys_d_reg, sys_e_reg]
dict_list = [sys_a_reg, sys_b_reg]
# dict_list = [sys_a_reg, sys_b_reg, sys_c_reg, sys_d_reg, sys_e_reg, sys_f_reg]

# dict_list = [sys_a_reg, sys_b_reg, sys_c_reg, sys_d_reg, sys_e_reg, sys_f_reg, sys_g_reg, sys_h_reg, sys_i_reg]

# dict_list = [sys_a_reg, sys_b_reg, sys_c_reg, sys_d_reg]

ext_judge = '_judge.tsv'
ext_tsv = '.tsv'
# out_sys_a_head = sys_dir_common + 'diff_only_' + sys_a + '_'
# out_sys_b_head = sys_dir_common + 'diff_only_' + sys_b + '_'
# out_file = sys_dir_common + 'diff_' + sys_a + '_' + sys_b + '_' + sys_c + '_' + sys_d +
# '_' + sys_e + '_' + sys_f + '_' + sys_g + '_' + sys_h +  '_' + sys_i + ext_tsv
# out_file = sys_dir_common + 'diff_' + sys_a + '_' + sys_b + '_' + sys_c + '_' + sys_d \
#            + '_' + sys_e + '_' + sys_f + ext_tsv
out_file = sys_dir_common + 'diff_' + sys_a + '_' + sys_b + ext_tsv\

# out_file = sys_dir_common + 'diff_' + sys_a + '_' + sys_b + '_' + sys_c + '_' + sys_d  + ext_tsv\
#            + '_' + sys_e + ext_tsv

cat_list = ['Airport', 'City', 'Company', 'Compound', 'Conference', 'Lake', 'Person']

# out_list = [out_sys_a_head, out_sys_b_head]


sys_cnt = 0
for sys_dir in sys_list:
    sys_cnt += 1
    index = sys_cnt - 1
    for cat in cat_list:
        j_fname = sys_dir_common + sys_dir + '/' + cat + ext_judge
        # o_fname = sys_dir_common + sys_dir + '/' + cat + ext_out
        with open(j_fname, 'r', encoding='utf-8') as j:
            reader = csv.reader(j, delimiter='\t')
            for row in reader:
                sys = row[0]
                # print('sys', sys)
                new_row = row
                del new_row[0]

                row_str = '\t'.join(row)
                row_str = row_str.rstrip('\n')
                new_row_str = '\t'.join(new_row)
                new_row_str = new_row_str.rstrip('\n')
                # print('new_row_str', new_row_str)
                if not sys_all_reg.get(new_row_str):
                    sys_all_reg[new_row_str] = []
                # common_keyでsystem を登録
                if sys not in sys_all_reg[new_row_str]:
                    sys_all_reg[new_row_str].append(sys)
# for i_dict in d_list:
#    for k, v in i_dict:

dupli_list = []
s_cnt = 0

for common_key in sys_all_reg:
    # print('sys_all_reg[k]', sys_all_reg[k])
    mark = ''
    # common_keyを登録したのが1システムのみ
    if len(sys_all_reg[common_key]) == 1:
        # systemリストのidx番目のシステムがこのcommon_keyで登録されているか
        for tmp_sys in sys_list:
            if tmp_sys in sys_all_reg[common_key]:
                # if sys_list[idx] in sys_all_reg[common_key]:

                # print('sys_all_reg[common_key]', sys_all_reg[common_key])
                # 個別の辞書にcommon_keyを登録
                # dict_list[idx][common_key] = 1
                # mark = '\t' + 'only_' + sys_list[idx]
                mark = 'UNIQ\t' + tmp_sys
                sys_all_reg[common_key] = mark
    elif len(sys_all_reg[common_key]) > 1:

        mark = 'DUPLI\t'
        for tmp_sys in sys_list:
            if tmp_sys in sys_all_reg[common_key]:
                # if sys_list[idx] in sys_all_reg[common_key]:

                # print('sys_all_reg[common_key]', sys_all_reg[common_key])
                # 個別の辞書にcommon_keyを登録
                # dict_list[idx][common_key] = 1
                # mark = '\t' + 'only_' + sys_list[idx]
                mark = mark + tmp_sys + ';'

        mark.rstrip(';')
        sys_all_reg[common_key] = mark

        # mark = 'DUPLI\t' + sys_a + '_AND_' + sys_b
        # sys_all_reg[common_key] = mark

with open(out_file, 'w', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='\t', lineterminator='\n')
    for k, v in sys_all_reg.items():
        # print(k, v)
        writer.writerow([k, v])


# # 個別の辞書を出力
# t_cnt = 0
# for out_head in out_list:
#     t_cnt += 1
#     t_idx = t_cnt -1
#
#     for cat in cat_list:
#         out_file = out_head + cat + ext_tsv
#         # print(out_file)
#         with open(out_file, 'w', encoding='utf-8') as f:
#             writer = csv.writer(f)
#             for k, v in dict_list[t_idx].items():
#                 print(k, v)
#                 writer.writerow([k, v])

# for k, sys_name in sys_all_reg:
#     if len(sys_all_reg[k]) > 1:
#         dupli_list.append()
#         if not dupli_dict.get(k):
#             dupli_dict[k] = []
#         dupli_dict[k].append(v)
