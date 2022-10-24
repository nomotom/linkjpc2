# DATA INFO

TABLE OF CONTENTS:
- [WHERE TO GET DATA](#where-to-get-data)
- [WHERE TO PUT DATA](#where-to-put-data)
- [DATA DESCRIPTION](#data-description)

# WHERE TO GET DATA

All of the SHINRA 2022 task data are available from [SHINRA2022](http://2022.shinra-project.info/) homepage. 

# WHERE TO PUT DATA  
The files required in entity linking (**_linkjpc2_**) or preprocessing (**_linkjpc_prep_**) (optional) are listed below.  
Please place the files in the following directories (bold fonts) referring the following instructions.  
  - **in_dir** (for test data (+html))　　
  - **out_dir** (for output data)
  - **tmp_data_dir** (for [TP] data specifically used for the test data)
  - **sample_gold_dir** (for sample gold data (+html) )
  - **common_data_dir** (for other data ([CM], [CP], [CD])

The directories are specified as command line arguments or options when you try entity linking or preprocessing.

## Directory structure

### **in_dir**

  Please create the directories and place the test data and html files as follows.  
  - The name of the bottom directory to place test data should be '**ene_annotation**'.
  - Do not place other json files (eg. '*_for_view.jsonl') in the same directory. 
  - Html files should be grouped by categories and be placed in subdirectories under '**html**' respectively.
  
(test data)
   ```angular2html
   + ene_annotation  
      + *.jsonl
``` 

(html_files)
```angular2html
  + html            
     + (ENE category name)         
        + *.html 
```

### **sample_gold_dir**  

  Please create the following directories and place the sample gold data.  
  The name of the bottom directory of sample gold data should be '**link_annotation**'.  
  Html files should be placed in subdirectories corresponding their category directory under '**html**', respectively.  

(preprocessing)

```angular2html
     + link_annotation
         + *.jsonl
  ```
### **sample_input_dir**  

  Please create the following directories and place the sample input data and html files.  
  The name of the bottom directory of sample input data and html files should be '**ene_annotation**' and  **html** respectively.  
  Html files should be placed in subdirectories corresponding their category directory under '**html**'.  

```angular2html
     + ene_annotation
         + *.jsonl
     + html
         * (ENE cagoteyr name)
            + *.html
```

# DATA DESCRIPTION

## (1) Data distributed by project SHINRA 
## (in_dir)
### IT1 (test data)
- filename: '*.jsonl'
- description: Test data.
- available from: [SHINRA2022 HP]

### IT2 (original articles of test data (*.html))
- filename: *.html
- description: *.html files of the original articles of test data. The files are grouped by ENE categories (eg. 'Airport, 'CIty, etc.)
- available from: [SHINRA2022 HP]

## (sample_gold_dir)
### IT3 (sample gold data)
- filename: *.jsonl'
- description: Sample gold data.
- available from: [SHINRA2022 HP]

## (sample_input_dir)

### IT4 (original articles of sample data (*.html))
- filename: ***.html**
- description: *.html files of the original articles of sample data. The files are grouped by ENE categories (eg. Airport, City, etc.)
- available from: [SHINRA2022 HP]  

## (common_data_dir)

### CD1 (f_cirrus_content_default) 
 - filename: '**wikipedia-ja-20210823-json.gz**'
 - based on Wikipedia 20210823
 - description: Wikipedia Cirrus Dump (content)
 - available from: [SHINRA2022 HP]

### CD2 (f_ene_def_for_task_default)
 - filename: '**ene_definition_v9.0.0-with-attributes-and-shinra-tasks-20220714.jsonl**'
 - description: ENE definition for SHINRA task.
 - available from:  [SHINRA2022 HP]

### CD3 (f_enew_org_default)  
 - filename: '**SHINRA2022_Categorization_train_20220616.jsonl**'
 - description: SHINRA2022 training data for Classification task.
 - based on: Wikipedia 2019, ENE9
 - sample:
     - `{"page_id":"1478897","title":"スキマスイッチ ARENA TOUR'07 \"W-ARENA\"THE MOVIE","ENEs":{"HAND.AIP.202204":[{"prob":1,"ENE":"1.7.13.6"}]}}`
 - available from: [SHINRA2022 HP]


## (2) manually created data (common_data_dir)

### CM1 (f_disambiguation_pat_default)
 - filename: '**wikipat_dis.tsv**'
 - description: Disambiguation page judgment rules list.
 - format: target, position, expression (*.tsv)
 - sample:
   - `cat     end     曖昧さ回避 `
 - created by: manually

### CM2 (f_self_link_pat_default)
 - filename: '**self_link_pat.tsv**'
 - format: 
   - pos, pat (*.tsv)
 - sample:
   - `start   別名`
   - `start   合併`
 - created by: manually

### CM3 (f_attr_rng_man_org_default)
 - filename: '**attr_rng_man_org_ene90_20221004.tsv**'
 - description: Manually created attribute range list.
 - format: 
    - ene_label_en, attribute_name, range(ENEID), probability (*.tsv)
 - sample:
   - `Military_Ship   乗船者  1.1 1`
   - `Toy     開発者  1.4     0.8`
 - created by: manually

### CM4 (f_back_link_dump_default) 
 - filename: '**jawiki-20210820-pagelinks_dmp.tsv**'
 - description: Back link dump file converted from jawiki-20210820-pagelinks.sql.
 - format: 
    - back link pid, org_title (*.tsv)
 notice: 
 - created by: 
   - `mysql -u root -D pagelink < jawiki-20210820-pagelinks.sql`
   `...`
   `select pl_from, pl_title from pagelinks into jawiki-20210820-pagelinks_dmp.tsv`
 - based on jawiki-20210820-pagelinks.sql

### CM5 (f_redirect_dump_org_default)
 - filename:'***jawiki-20210820-redirect_dmp.tsv***'
 - description: Wikipedia redirect dump 
 - format: 
    - rd_from, rd_title, rd_namespace
 - sample:
    - `1699304	広瀬香美_THE_BEST_"Love_Winters"	0`<br>
    - `1855418	広瀬香美_THE_BEST_"Love_Winters"	0`<br>
 - based on: jawiki-20210820-redirect.sql

### CM6 (f_redirect_dump_default)
 - filename:'***jawiki-20210820-redirect_dmp_rev.tsv***'
 - description: Wikipedia redirect dump modified version<br>
    - deleted: (a) titles with single punctuation symbols, (b) 'redirects to' titles in namespaces other than zero are omitted<br>
    - escaped: double quotations
 - format: 
    - rd_from, rd_title, rd_namespace
 - sample:<br>
    - `1699304	広瀬香美_THE_BEST_\"Love_Winters\"	0`<br>
    - `1855418	広瀬香美_THE_BEST_\"Love_Winters\"	0`<br>
 - original: 'jawiki-20210820-redirect_dmp.tsv' (based on: jawiki-20210820-redirect.sql.gz)
 - created by:<br>
    - `$ awk 'BEGIN{FS="\t"}$2 !~ /^[[:punct:]]$/{print}' jawiki-20210820-redirect_dmp.tsv | perl -pe 's/\"/\"\"/g;' > jawiki-20210820-redirect_dmp_rev.tsv`
 - notice: 
   - deleted punctuation symbols (`!"#$%&'-=^~\|@`...`)

### CM7 (f_page_dump_org_default)
 - filename:'***jawiki-20210820-page_dmp.tsv***'
 - description: Wikipedia page dump<br>
 - format:  
   - page_id, page_title, page_is_redirect, page_namespace
 - sample:
   - `1696323	広瀬香美_THE_BEST_"Love_Winters"	0	0`<br>
   - `1699304	広瀬香美_THE_BEST"Love_Winters"	1	0`<br>
 - notice:
   - based on: jawiki-20220820-page.sql

### CM8 (f_page_dump_default)
 - filename:'***jawiki-20210820-page_dmp_rev.tsv***'
 - description: Wikipedia page dump<br>
    - deleted: titles with single punctuation symbols<br>
    - escaped: double quotations 
 - format:  
   - page_id, page_title, page_is_redirect, page_namespace
 - sample:
   - `517804	宮下杏菜	0	0`<br>
   - `557692	宮下杏奈	1	0`<br>
 - original: 'jawiki-20210820-page_dmp.tsv' (based on: jawiki-20210820-page.sql)<br>
 - created by:<br>
   -`$ awk 'BEGIN{FS="\t"}$2 !~ /^[[:punct:]]$/{print}' jawiki-20210820-page_dmp.tsv | perl -pe 's/\"/\"\"/g;' > jawiki-20210820-page_dmp_rev.tsv`<br>
 - notice: 
   - pageid: 2021 
   - deleted punctuation symbols(`!"#$%&'-=^~\|@`...`)

### CM9 (f_page_dump_old_org_default)
 - filename:'***jawiki-20190120-page_dmp.tsv***'
 - description: Wikipedia page dump (20190120)<br>
 - format:  
   - page_id, page_title, page_is_redirect, page_namespace
 - sample:
   - `934000	安倍晋三	0	0`<br>
   - `934006	安倍晋三	0	1`<br>
 - based on: jawiki-20190120-page.sql.gz<br>

### CM10 (f_lang_link_dump_org_default)

 - filename:'***jawiki-20210820-langlinks_dmp.tsv***'
 - description: Langlinks dump (20210820)
 - format: 
   - from page(Japanese Wikipedia wgarticleID), lang code, title
 - sample:
   - `102349	el	Chanel`
   - `102349	en	Chanel`
 - based on: jawiki-20210820-langlinks.sql<br>

### CM11 (f_enew_mod_list_default)
 - filename: '**shinra2022_Categorization_train_20220616_stoplist.tsv**'
 - description: ENEW modification list to delete problematic records with specified combination of ENEID, pid, title.
 - format: 
   - ENEID, pid, title (*.tsv)
 - sample: 
   - `1.5.1.3 1419479 フランス陸軍参謀総長`
 - created by: manually

### CM12 (f_wl_lines_backward_ca_default)
 - filename: '**wl_lines_backward_ca.tsv**'
 - description: The file to specify maximum number of line to backward-search Wikipedia links in the page for each category-attribute pair.
 - notice: 
   - The default file contains just one example and should be modified. 
 - format:
    - ene_label_en, attribute_name, distance (*.tsv)
 - sample:
    - `Person  作品    -3`

### CM13 (f_wl_lines_forward_ca_default)
 - filename: '**wl_lines_forward_ca.tsv**'
 - description: The file to specify maximum number of line to forward-search Wikipedia links in the page for each category-attribute pair.
 - notice: 
   - The default file contains just one example and should be modified.  
 - format:
    - ene_label_en, attribute_name, distance (*.tsv)
 - sample:
    - `Person  作品    1`

### CM14 (f_sample_gold_mod_list_default)
 - filename: '**train-link-20221004_stoplist_all.tsv**'
 - description: Linking training data (20221004) modification list to delete problematic records with specified 
combination of category(ENE_label_en), pid, attribute, mention, and linked id.
 - format:
   - ene_label_en, pageid, title, attribute_name,  mention, start_line_id, start_offset, end_line_id, end_offset, linked id`
 - sample:
   - `Airport 4013648 シモン・ボリバル国際空港        別名    シモン・ボリーバル国際空港      82      17      82      30   12345678`
 - notice:
   - Currently, the file is empty. (2022/10/23)
 
### CM15 (f_nil_cand_man_default)
  - filename: '**cat_attr_nil_cand_man.tsv**'
  - description: list of category(ENE en label)-attributes pairs which might be applied nil detection.
  - format:
    - en_label_en, attribute_name (*.tsv)
  - sample:
    - `Fish    保全状況`

### CM16 (f_nil_stop_attr_default)
  - filename: '**nil_stop_attr_man.tsv**'
  - description: list of attributes which should not be applied nil detection.
  - format:
    - en_label_en, attribute_name (*.tsv)
  - sample:
    - 主要都市
    - 中立国
  
## (3) data created by preprocessing tools
## (3-1) (sample_input_dir)

### SI1 (sample input json (ID converted))
 - filename: **xx.jsonl**
 - description: sample input json (year converted)

## (3-2) (sample_gold_dir)

SP1 and SP2 will be created in subdirectory of sample_gold_dir.

### SP1 (sample gold json (ID converted))
 - filename: **xx.jsonl**
 - description: sample gold json (ID converted)

### SP2 (sample gold data info)
 - filename: **XX.tsv** 
 - description: Sample gold data info.
 - format: 
    - category,  org_pageid, org_title, attribute_name, mention, start_line_id, start_offset, end_line_id, 
end_offset, gold_pageid, gold_title, gold_eneid, gold_ene_category (*.tsv)
 - sample:<br>
   - `Person	990044	細井雄二	作品	快傑ズバット	107	1	107	7	130767	快傑ズバット	['1.7.12', '1.7.13.2']	
['Character', 'Broadcast_Program']`

## (3-3) (common_data_dir)

### CP1 (f_common_html_info_default) 
 - filename: '**common_html_tag_info.tsv**'
 - description: Info on embedded links to other Wikipedia pages in original articles of sample data
 - format: 
    - cat, pid, line_id, text_start, text_end, text, title (*.tsv)
 - sample: 
   - `cat	pid	line_id	html_text_start	html_text_end	html_text	title`
   - `City    1617736 90      292     298     リンブルフ州 リンブルフ州 (ベルギー)`
 - notice:
   - with header 

### CP2 (f_wikipedia_page_change_info_default)
 - filename 'jawiki-20190120_20210820_page_change_info.tsv'
 - format: 
   - old_pageid, new_pageid (*.tsv)
 - sample: 
   - `2378461	581`
   - `467914	800`

### CP3 (f_disambiguation_default)
 - filename: '**jawiki-20210823-cirrussearch-content_disambiguation.tsv**'
 - description: Disambiguation page list.
 - format: 
    - pageid, title (*.tsv)
 - sample:
    - `961474	SWEET DREAMS`

### CP4 (f_redirect_info_default) 
 - filename: '**jawiki-20210823_title2pageid_20210820_nodis.tsv**'
 - description: Redirect info file, a modification of original from_title to_pageid information file to exclude disambiguation pages and ill-formatted pages. 
 - format: 
    - title, pageid (*.tsv)
 - sample:
    - `夏の夜の夢	318229`
    - `真夏の夜の夢	318229`
 - notice:
    - based on original redirect file(f_title2pid_org_default, jawiki-20210823_title2pageid_20210820.jsonl).
    - recovered white spaces in Wikipedia titles which are replaced by '_' in the original redirect file.
    - Info on ill formatted pages or disambiguation pages are excluded though not completely.

### CP5 (f_incoming_default) 
 - filename: '**jawiki-20210823-cirrussearch-content_incoming_link.tsv**'
 - description: Incoming link num info list.
 - format:
    - pageid, title, number of incoming links (*.tsv) 
 - sample: 
    - `345792  ピノッキオの冒険        233`
 - created by: (linkjpc_prep --gen_incoming_link) gen_incoming_link_file

### CP6 (f_enew_info_default) 
 - filename: '**shinra2022_Categorization_train_20220616_mod.tsv**'
 - description:
    - ENEW info (based on slightly modified version of ENEW (20200427)).
    - modification list: ENEW_ENEtag_20200427_stoplist.tsv (f_enew_mod_list_default)
 - format:
    - pageid, ENEid, title (*.tsv) 
 - sample: 
    - `345792  1.7.19.6        ピノッキオの冒険`
 - notice: 
    - Not all target pageids are included in the file. (eg. 3682608, 3386984)

### CP7 (f_slink_default) 
 - filename: '**cat_attr_self_link.tsv**'
 - description: Self link info file to estimate the probability of linking to the original article for each category-attribute pair. 
 - format: 
    - ene_label_en, attribute_name, ratio, self_link_freq, cat_attr_freq (*.tsv)
 - sample:
    - `City	合併市区町村	0.47	156	333`
 - note: The ratio is based on sample data. Not all the target categories are included. (eg. Island)

### CP8 (f_self_link_by_attr_name_default)
 - filename: '**self_link_by_attr_name.tsv**'
 - format: 
    - attr
 - sample:
    - `別名・旧称`
    - `合併市区町村`
 - created by: gen_self_link_by_attr_name

### CP9 (f_link_prob_default) 
 - filename: '**sample_cat_attr_mention_linkcand.tsv**'
 - description: Link probability info file. 
 - format: 
    - ene_label_en, attribute_name, mention, link_cand_pageid:prob:freq;...(.tsv)
 - sample: 
    - `City	合併市区町村	上村	37423:0.25:1;151917:0.25:1;1872659:0.25:1;381057:0.25:1`
 - notice:
    - The ratio is based on sample data.

### CP10 (f_linkable_info_default) 
 - filename: '**cat_attr_linkable.tsv**'
 - description: Linkable info file. 
 - format: 
    - ene_label_en, attribute_name, ratio (*.tsv), linked_freq, all_freq
 - sample: 
    - `Painting        所蔵・所有者    0.43    16      37`
 - notice:
   - The ratio is based on sample data.

### CP11 (f_mention_gold_link_dist_default) 
 - filename: '**mention_gold_link_dist.tsv**'
 - description: Mention goldlink dist file, which shows the distance (number of lines) between mentions and (nearest) gold links in sample html files.
 - format: 
    - ene_label_en, attribute_name, distance (.tsv)
 - sample: 
    - `Person 作品 -1`
    - `Person 作品 29`
 - notice: the values are based on sample data

### CP12 (f_attr_rng_man_default)
 - filename: '***attr_rng_man.tsv***'
 - description: attribute range info based on attr_rng_man_org_file (hand-written).
 - format: 
   - cat, attr, rng_eneid, rng_cat, ratio
 - sample: <br>
   - `Music	プロデューサー	1.1	Person	1`
 - based on f_attr_rng_man_org

### CP13 (f_attr_rng_auto_default)
 - filename: '***attr_rng_auto.tsv***'
 - description: attribute range info based on sample data statistics
 - format: 
   - cat, attr, eneid, ratio, freq', sum(cat*attr)
 - sample: <br>
   - `Music	プロデューサー	1.1	Person	0.5	1	2`
   - `Music	プロデューサー	1.4.2	Show_Organization	0.5	1	2`

### CP14 (f_target_attr_info_default)
 - filename: '**ene_definition_v9.0.0-20220714_target_attr.tsv**'
 - format: 
    - eneid, ene_label(ja), ene_label(en), attribute_name, (*.tsv)
 - sample:
    - `1.1	人名	Person	別名・旧称`
    - `1.1	人名	Person	国籍`

### CP15 (f_all_cat_info_default)
 - filename: '**ene_definition_v9.0.0-20220714_all_cat.tsv**'
 - format: 
   - ene_id, ene_label(ja), ene_label(en), (*.tsv)
 - sample: <br>
   - `1.1	人名	Person`
   - `1.2	神名	God`
 - notice:
   - Some categories lack attributes.

### CP16 (f_lang_link_info_default) 
 - filename: '***jawiki-20210820-langlinks_info.tsv***'
 - format: 
   - from page(Japanese Wikipedia wgarticleID), lang code, title
 - sample: <br>
   - `102349	en	Chanel`
   - `102349	hi	चैनल`
   - `102349	zh	香奈儿`
 - based on: jawiki-20210820-langlinks.sql
 - notice: illegal characters (UnicodeDecodeError) are converted to '?'.
 - created by: (linkjpc_prep --gen_lang_link) gen_lang_link_info

### CP17 (f_title2pid_ext_default) 
 - filename: '**jawiki-20210823_title2pageid_20210820_ext.tsv**'
 - description: Summary information on title to pageid conversion, incoming links, and ENE classification of articles. .
 - format: 
    - from_title, to_pid, to_title, to_incoming, to_eneid_set (*.tsv)
 - sample: 
    - `ロメオとジュリエット	28783	ロミオとジュリエット	806	{'1.7.13.4', '1.7.13.5'}  `

### CP18 (f_title2pid_ext_obs_default)
 - filename '**jawiki-20190120-title2pageid_ext.tsv**'
 - format: 
   - from_title, to_pid, to_title, to_incoming, to_eneid
 - sample: <br>
    - `United States of America        1698838 アメリカ合衆国  116818  1.5.1.3`

### CP19 (f_title2pid_org_default)  
 - filename: '**jawiki-20210820-title2pageid.jsonl**'
 - description: Title to pageid conversion info list
 - format: see [title2pageid_for_entitylinking_dataset](https://github.com/k141303/title2pageid_for_entitylinking_dataset)
 - sample:
    - `{"page_id": 311957, "title": "風と共に去りぬ_(宝塚歌劇)", "is_redirect": false}`
 - based on: Wikipedia 20210820

## (3-3) tmp_data_dir

### TP1 (f_input_title_default)
 - filename: '**input_title.txt**'
 - description: Title list of test data.
 - format:
   - title (*.txt)
 
### TP2 (f_back_link_default) 
 - filename: '**back_link_full.tsv**'
 - description: Back link info file, which shows the title pages of test data and the back links to the pages
 - format: org_title, back link (from) pid, back link (from) title (*.tsv)
 - notice: 
   - based on jawiki-20210820-pagelinks.sql

### TP3 (f_mint_partial_default) 
 - filename: '**mint_partial_match.tsv**'
 - description: Mention-title matching ratio list (mention in title, full title)
 - format: 
   - mention, pid, title, ratio, lang(*.tsv)

### TP4 (f_mint_trim_partial_default) 
 - filename: '**mint_trim_partial_match.tsv**'
 - description: Mention-title matching ratio list (mention in title, trimmed title)
 - notice:
   - Disambiguation descriptions enclosed in braces in titles are not used for matching.
 - format: 
   - See f_mint_partial_default

### TP5 (f_tinm_partial_default) 
 - filename: '**tinm_partial_match.tsv**'
 - description: Mention-title matching ratio list (title in mention, full title)
 - format: 
   - mention, pid, title, ratio (*.tsv)

### TP6 (f_tinm_trim_partial_default) 
 - filename: '**tinm_trim_partial_match.tsv**'
 - description: Mention-title matching ratio list (title in mention, tinm title)
 - notice:
   - Disambiguation descriptions enclosed in braces in titles are not used for matching
 - format: 
   - mention, pid, title, ratio lang(.tsv)
 
### TP7 (f_html_info_default)  
 - filename: '**html_tag_info.tsv**'
 - description: Info on embedded links to other Wikipedia pages in original articles of test data
 - format:
   - cat, pid, line_id, html_text_start, html_text_end, text, title (.tsv)
  
## (4) data created by entity linking
### (4-1) (out_dir)

### OL1 (output data)
 - filename: **'*.jsonl' ....**
 - description: Output data.
 - format: See [SHINRA2022] homepage

### (4-2) (common_data_dir)

### CL1 (f_mention_gold_link_dist_info_default) 
 - filename: '**mention_gold_link_dist_info.tsv**'
 - description: Summary of distance from mentions to links to gold pages by category and attribute.
 - format: 
   - cat, attr, backward_limit, forward_limit, diff_backward_num, diff_forward_num, diff_same_num, all_num (tsv)
 - sample:
   - `Person  地位職業        -47     7       18      90      -63     45`
 - notice: the values are based on - sample data


### CL2 (f_attr_rng_merged_default)
 - filename: '***attr_rng_merged.tsv***'
 - format: 
    - cat__attr, eneid, {eneid: ratio, eneid: ratio, ....)
 - description: attribute range info created by each execution 
 - sample: <br>
   - `Competition__優勝者     1.1     {'1.1': 0.8, '1.4': 0.8}`


