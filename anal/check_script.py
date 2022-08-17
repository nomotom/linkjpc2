
script_file = './tests_private/linkjpc_test_private.sh'
#script_file = './linkjpc_all_test.sh'
#script_file = './linkjpc_all_test.sh'
#script_file = './linkjpc_final_test.sh'

with open(script_file, mode='r', encoding='utf-8') as f:
    for line in f:

        if 'python' in line:

            if '_01' in line and not '0.1' in line:
                print('check number and digit:0.1', line)
            if '0.1' in line and (not '_01' in line):
                print('check number and digit:0.1', line)
            if '_02' in line and not '0.2' in line:
                print('check number and digit:0.2', line)
            if '0.2' in line and not '_02' in line:
                print('check number and digit:0.2', line)
            if '_03' in line and not '0.3' in line:
                print('check number and digit:0.3', line)
            if '0.3' in line and not '_03' in line:
                print('check number and digit:0.3', line)
            if '_04' in line and not '0.4' in line:
                print('check number and digit:0.4', line)
            if '0.4' in line and not '_04' in line:
                print('check number and digit:0.4', line)
            if '_05' in line and not '0.5' in line:
                print('check number and digit:0.5', line)
            if '0.5' in line and not '_05' in line:
                print('check number and digit:0.5', line)
            if '_06' in line and not '0.6' in line:
                print('check number and digit:0.6', line)
            if '0.6' in line and not '_06' in line:
                print('check number and digit:0.6', line)
            if '_07' in line and not '0.7' in line:
                print('check number and digit:0.7', line)
            if '0.7' in line and not '_07' in line:
                print('check number and digit:0.7', line)
            if '_08' in line and not '0.8' in line:
                print('check number and digit:0.8', line)
            if '0.8' in line and not '_08' in line:
                print('check number and digit:0.8', line)
            if '_09' in line and not '0.9' in line:
                print('check number and digit:0.9', line)
            if '0.9' in line and not '_09' in line:
                print('check number and digit:0.9', line)
            if ('_1_' in line  or '_1/' in line )and not '1.0' in line:
                print('warning:check number and digit:1.0', line)
            if '1.0' in line and (not '_1_' in line and not '_1/' in line and not '_10_' in line and not '_10/' in line):
                print('warning:check number and digit:1.0', line)
            if ('_10_' in line  or '_10/' in line ) and (not ' 10' in line and not '1.0' in line):
                print('warning:check number and digit:10 a', line)
            if ' 10 ' in line and (not '_10_' in line and not '_10/' in line and not '_10_' in line and not '_10/' in line):
                print('warning:check number and digit:10 b', line)
            if ('_100_' in line or '_100/' in line ) and not ' 100' in line:
                print('warning:check number and digit:100 a', line)
            if ' 100 ' in line and ((not '_100_' in line) and (not '_100/' in line) and (not '_100_' in line) and
                                    (not '_100/' in line)):
                print('warning:check number and digit:100 b', line)
            if ('_1000_' in line or '_1000/' in line or '_1K/' in line) and not ' 1000' in line:
                print('warning:check number and digit:1000 a', line)
            if ' 1000 ' in line and ((not '_1000_' in line) and (not '_1000/' in line) and (not '_1000_' in line)
                                     and (not '_1000/' in line) and (not '_1K/' in line)):
                print('warning:check number and digit:1000 b', line)
            if (('_10000_' in line) or ('_10000/' in line) or ('_10K_' in line) or ('_10K/' in line))\
                    and (not ' 10000' in line)  :
                print('warning:check number and digit:10000 a', line)
            if ' 10000 ' in line and ((not '_10000_' in line) and (not '_10000/' in line) and (not '_10000_' in line)
                                      and (not '_10000/' in line) and (not '_10K_' in line ) and (not '_10K/' in line)):
                print('warning:check number and digit:10000 b', line)
            if ' 100000 ' in line and ((not '_100000_' in line) and (not '_100000/' in line) and (not '_100000_' in line)
                                      and (not '_100000/' in line) and (not '_100K_' in line ) and (not '_100K/' in line)):
                print('warning:check number and digit:100000 a', line)
            if ' 1000000 ' in line and ((not '_1000000_' in line) and (not '_1000000/' in line) and (not '_1000000_' in line)
                                      and (not '_1000000/' in line) and (not '_1M_' in line ) and (not '_1M/' in line)):
                print('warning:check number and digit:1000000 a', line)
            if ' 10000000 ' in line and ((not '_10000000_' in line) and (not '_10000000/' in line) and (not '_10000000_' in line)
                                      and (not '_10000000/' in line) and (not '_10M_' in line ) and (not '_10M/' in line)):
                print('warning:check number and digit:10000000 a', line)
            if ' 100000000 ' in line and ((not '_100000000_' in line) and (not '_100000000/' in line) and (not '_100000000_' in line)
                                      and (not '_100000000/' in line) and (not '_100M_' in line ) and (not '_100M/' in line)):
                print('warning:check number and digit:100000000 a', line)
            if '_amax' in line and (not ' -a_max' in line ):
                print('amax should be specified using a_max', line)
            if '-a_max' in line and (not '_amax' in line ):
                print('warning: a_max should be specified in path', line)
            if ' -ans_max ' in line:
                print('ans_max should be preceded by -- not -', line)
            if ' --a_max ' in line:
                print('a_max should be preceded by - not --', line)
            if '_attr ' in line and not 'ar_tgt' in line:
                print('attr should be specified using ar_tgt', line)
            if ' -attr_range_tgt ' in line:
                print('attr_range_tgt should be preceded by -- not -', line)
            if ' --ar_tgt ' in line:
                print('ar_tgt should be preceded by - not --', line)
            if ' -attr_na_co ' in line:
                print('attr_na_co should be preceded by -- not -', line)
            if ' --anc ' in line:
                print('anc should be preceded by - not --', line)
            if ' -attr_ng_co ' in line:
                print('attr_ng_co should be preceded by -- not -', line)
            if ' --ang ' in line:
                print('ang should be preceded by - not --', line)
            if ' -attr_len ' in line:
                print('attr_len should be preceded by -- not -', line)
            if ' --al ' in line:
                print('al should be preceded by - not --', line)
            if ' -back_link_tgt ' in line:
                print('back_link_tgt should be preceded by -- not -', line)
            if ' --bl_tgt ' in line:
                print('bl_tgt should be preceded by - not --', line)
            if ' -back_link_type ' in line:
                print('back_link_type should be preceded by -- not -', line)
            if ' --bl_type ' in line:
                print('bl_type should be preceded by - not --', line)
            if ' -back_link_ng ' in line:
                print('back_link_ng should be preceded by -- not -', line)
            if ' --bl_ng ' in line:
                print('bl_ng should be preceded by - not --', line)
            if '_bl ' in line and not 'bl_tgt':
                print('attr should be specified using ar_tgt', line)
            if ' -char_match_cand_num_max ' in line:
                print('char_match_cand_num_max should be preceded by -- not -', line)
            if ' --c_max ' in line:
                print('c_max should be preceded by - not --', line)

            if ' -filtering ' in line:
                print('filtering should be preceded by -- not -', line)
            if '--f ' in line:
                print('f should be preceded by - not --', line)
            if '_fixed ' in line and not 's_prb':
                print('fixed should be specified using s_prb', line)

            if ' -incl_max ' in line:
                print('incl_max should be preceded by -- not -', line)
            if ' --i_max ' in line:
                print('i_max should be preceded by - not --', line)
            if ' -incl_tgt ' in line:
                print('incl_tgt should be preceded by -- not -', line)
            if ' --i_tgt ' in line:
                print('i_tgt should be preceded by - not --', line)
            if ' -incl_type ' in line:
                print('incl_type should be preceded by -- not -', line)
            if ' --i_type ' in line:
                print('i_type should be preceded by - not --', line)

            if ' -log_level ' in line:
                print('log_level should be preceded by -- not -', line)

            if ' --l_min ' in line:
                print('lp_min should be preceded by - not --', line)
            if '  l_min ' in line:
                print('l_min should be preceded by -', line)

            if ' -lp_min ' in line:
                print('lp_min should be preceded by -- not -', line)
            if ' --lp_min ' in line:
                print('lp_min should be preceded by - not --', line)

            if '_mid ' in line and not 's_prb':
                print('mid should be specified using s_prb', line)
            if ' -mint ' in line:
                print('mint should be preceded by -- not -', line)
            if ' -mint_min ' in line:
                print('mint_min should be preceded by -- not -', line)

            if 'mint' in line and (not '--mod m' in line) and (not ':m' in line):
                print('warning: mod m may not be specified', line)

            if ' -mod_w ' in line:
                print('mod_w should be preceded by -- not -', line)
            if '-mw ' in line:
                print('no such option: use mod_w instead', line)

            if ' --m_min ' in line:
                print('m_min should be preceded by - not --', line)
            if ' -mod ' in line:
                print('mod should be preceded by -- not -', line)
            if '_raw ' in line and not 's_prb':
                print('raw should be specified using s_prb', line)
            if ' -slink_min ' in line:
                print('slink_min should be preceded by -- not -', line)
            if ' --s_min ' in line:
                print('s_min should be preceded by - not --', line)
            if ' -slink_prob ' in line:
                print('slink_prob should be preceded by -- not -', line)
            if ' --s_prb ' in line:
                print('s_prb should be preceded by - not --', line)

            if ' -score_type ' in line:
                print('score_type should be preceded by -- not -', line)

            if ' -title_matching_mint ' in line:
                print('title_matching_mint should be preceded by -- not -', line)
            if ' --tmm ' in line:
                print('tmm should be preceded by - not --', line)
            if ' -tinm ' in line:
                print('tinm should be preceded by -- not -', line)
            if ' -tinm_min ' in line:
                print('tinm_min should be preceded by -- not -', line)
            if ' --t_min ' in line:
                print('t_min should be preceded by - not --', line)
            if ' -title_matching_tinm ' in line:
                print('title_matching_tinm should be preceded by -- not -', line)

            if 'trim' in line and (not ' -tmt' in line and not ' -tmm' in line):
                print('trim should be specified using either tmt or tmm', line)
            if 'tinm' in line and (not '--mod t' in line) and (not ':t' in line) and (not ' mt' in line) and (not ':mt' in line):
                print('warning: mod t may not be specified', line)

            if ' -wlink ' in line:
                print('wlink should be preceded by -- not -', line)
            if ' --wl ' in line:
                print('wl should be preceded by - not --', line)
            if ' -wf_score ' in line:
                print('wf_score should be preceded by -- not -', line)
            if ' --wf ' in line:
                print('wf should be preceded by - not --', line)
            if ' -wr_score ' in line:
                print('wr_score should be preceded by -- not -', line)
            if ' --wr ' in line:
                print('wr should be preceded by - not --', line)
            if ' -wp_score ' in line:
                print('wp_score should be preceded by -- not -', line)
            if ' --wp ' in line:
                print('wp should be preceded by - not --', line)
            if ' -wl_score_same ' in line:
                print('wl_score_same should be preceded by -- not -', line)
            if ' --wls ' in line:
                print('wls should be preceded by - not --', line)
            if ' -wl_score_pre ' in line:
                print('wl_score_pre should be preceded by -- not -', line)
            if ' --wlp ' in line:
                print('wlp should be preceded by - not --', line)
            if ' -wl_score_next ' in line:
                print('wl_score_next should be preceded by -- not -', line)
            if ' --wln ' in line:
                print('wln should be preceded by - not --', line)

            if 'wlink_frp' in line and not 'wlink frp' in line:
                print('frp should be specified', line)
            if 'wlink_rp' in line and not 'wlink rp' in line:
                print('rp should be specified', line)
            if ('_if/' in line or '_if_' in line ) and not 'i_type' in line:
                print('warning: i_type may not be speficied', line)







