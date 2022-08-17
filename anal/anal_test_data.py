gold_base = '/Users/masako/Documents/SHINRA/2021-LinkJP/Download/linkjp-eval-211027/'
anal_base = '/Users/masako/Documents/SHINRA/2021-LinkJP/anal/'

ene_files = gold_base + 'ene_annotation/*.tsv'
link_files = gold_base + 'link_annotation/*.tsv'
out_file = anal_base + 'gold_linked_ratio.txt'

ext = '.tsv'
def get_category(fname, dname, exte):
    cat_pre = fname.replace(dname, '')
    cat_new = cat_pre.replace(exte, '')
    return cat_new

from glob import glob
import re
import pandas as pd

check_ene = {}
check_link = {}

# tsvファイルが失敗
# line 208762     名前の謂れ      "湖名の「アサバスカ（aðapaskāw）」というのはクリー語で「次々と植物が生えている場所」といった意味であり

echeck_cat_attr = {}
for e_fname in glob(ene_files):
    ecat = get_category(e_fname, gold_base, ext)
    with open(e_fname, mode = 'r', encoding = 'utf8') as e:
        for line in e:
            print('line', line)
            new_line = line.rstrip()
            (pid, eattr, org_title, line_start, pos_start, line_end, pos_end) = re.split('\t', new_line)
            ecat_attr = ecat + ':' + eattr
            if not echeck_cat_attr.get(new_line):
                if not check_ene.get(ecat_attr):
                    check_ene[ecat_attr] = 1
                else:
                    check_ene[ecat_attr] += 1
                echeck_cat_attr[ecat_attr] = 1
lcheck_cat_attr = {}
for l_fname in glob(link_files):
    lcat = get_category(l_fname, category, ext)
    with open(l_fname, mode = 'r', encoding = 'utf8') as l:
        for line in l:
            print('line', line)
            new_line = line.rstrip()
            (pid, lattr, org_title, line_start, pos_start, line_end, pos_end, link) = re.split('\t', line)
            lcat_attr = lcat + ':' + lattr

            if not lcheck_cat_attr.get(new_line):
                if not check_ene.get(lcat_attr):
                    check_link[lcat_attr] = 1
                else:
                    check_link[lcat_attr] += 1
                lcheck_cat_attr[lcat_attr] = 1

elist = []
for cat_attr in check_ene:
    (cat, attr) = re.split(':', cat_attr)
    elist.append([cat, attr, check_ene[cat_attr], check_link[cat_attr], check_link[cat_attr]/check_ene[cat_attr]])
    df = pd.DataFrame(elist)
    df.to_csv(outfile, sep='\t', header=False, index=False)











