import itertools

out_dir_base = "/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/anal_multi_20211016/"


cmax = 10M

target_prec_key = "top_precision"
target_recall_key = "top_recall"
target_f1_key = "top_f1"
tmp_target_key = target_recall_key

anal_prefix="_module"
# ex. 1_module

sys_mint_org = 'mint_p_01_cmax_10M_amax_10M'
sys_mint = sys_mint_org.replace('_amaxsys_mint_org)
sys_slink = 'slink_01_amax_10K'

sys_tinm = 'tinm_p_01_cmax_100K_amax_100K'

sys_wlink = 'wlink_rpl_amax_100K'

sys_l = 'l_01_max_10M'

lis=[sys_mint, sys_slink, sys_tinm, sys_wlink, sys_l]
result = []
for n in range(1,len(lis)+1):
    for combi in itertools.combinations(lis, n):
        target_dir = out_dir_base + 'eval' + '\n'  + n + anal_prefix + '_' + tmp_target_key
        result.append(list(combi)) #タプルをリスト型に変換
print(result)