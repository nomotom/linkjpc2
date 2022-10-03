# DATA INFO

TABLE OF CONTENTS:
- [WHERE TO GET DATA](#where-to-get-data)
- [WHERE TO PUT DATA](#where-to-put-data)
- [DATA DESCRIPTION](#data-description)

# WHERE TO GET DATA

Where to get data depends on the data creation method as shown below.

Data creation method | data necessay for entity linking (_linkjpc_)          | additional data necessary for preprocessing (optional) |Where to get data 
:-------------------------------------|:---------|:-------|:-----------------------------------------
(1) [project SHINRA data distribution](#1-project-shinra-data-distribution) | [IT1](#it1-test-data)| [IT2](#it2-original-articles-of-test-data-html), [IT3](#it3-sample-gold-data), [IT4](#it4-original-articles-of-sample-data-html), <br> [CD1](#cd1-f_cirrus_content_default), [CD2](#cd2-f_title2pid_org_default), [CD3](#CD3-f_enew_org_default)|project SHINRA site <br>- [SHINRA2021LinkJP](http://shinra-project.info/shinra2021linkjp/) <br> - [SHINRA Data Dowload](http://shinra-project.info/download/) <br><br>(Please access to each page linked in **_[DATA DESCRIPTION](#data-description)_** below.)
(2) [manually created data](#2-manually-created-data)|[CM4-6](#cm4-f_wl_lines_backward_ca_default)|[CM1-3](#cm1-f_disambiguation_pat_default)| [public data (rule-based systems)](https://drive.google.com/drive/folders/1rNlUanyl1ULEUUKMifIMZgwhzs-84iQT?usp=sharing) 
(3) [Data created by preprocessing tools](#3-data-created-by-preprocessing-tools) |[CP7-9](#cp7-f_slink_default),<BR> [TP2-TP7](#tp2-f_back_link_default) |  |   the same as (2) above 

See **_[DATA DESCRIPTION](#data-description)_** for details about files and download pages.  

Please place the downloaded files to the directories specified in **[WHERE TO PUT DATA](#where-to-put-data)**.  
As for (2) and (3) above, the data files are grouped and stored in three folders on the download site, namely, **tmp_data_dir**, **sample_gold_dir**, and 
**common_data_dir**.

# WHERE TO PUT DATA  
The files required in entity linking (**_linkjpc_**) or preprocessing (**_linkjpc_prep_**) (optional) are listed below.  
Please place the files in the following directories (bold fonts) referring the following instructions.  
  - **in_dir** (for test data (+html))　　
  - **out_dir** (for output data (entity linking))
  - **tmp_data_dir** (for data specifically used for the test data)
  - **sample_gold_dir** (for sample gold data (+html) (used for preprocessing))
  - **common_data_dir** (for other data)  
The directories are specified as command line arguments or options when you try entity linking or preprocessing.

    
## **in_dir** (linkjpc, linkjpc_prep)

  Please create the directories and place the test data ([IT1](#it1-test-data)) (*.json) and html files ([IT2](#it2-original-articles-of-test-data-html)) as follows.  
  - The name of the bottom directory to place test data should be '**ene_annotation**'.
  - Do not place other json files (eg. '*_for_view.json') in the same directory. 
  - Html files should be grouped by categories and be placed in subdirectories under '**html**' respectively.
  
(entity linking, preprocessing)
   ```angular2html
   + ene_annotation  
      + Airport.json　(IT1)
      + City.json (IT1)
      + Company.json (IT1)
      + Compound.json (IT1)
      + Conference.json (IT1)
      + Lake.json (IT1)
      + Person.json (IT1)
``` 

(preprocessing)
```angular2html
  + html            
     + Airport         
        + *.html (IT2)
     + City
        + *.html (IT2)
     + Company
        + *.html (IT2)
     + Compound
        + *.html (IT2)
     + Conference
        + *.html (IT2)
     + Lake
        + *.html (IT2)
     + Person
        + *.html (IT2)
```
### **common_data_dir** (linkjpc, linkjpc_prep)

(entity linking)
>- wl_lines_backward_ca.tsv ([CM4](#cm4-f_wl_lines_backward_ca_default))
>- wl_lines_forward_ca.tsv ([CM5](#cm5-f_wl_lines_forward_ca_default)) 
>- attr_def.tsv ([CM6](#CM6-f_attr_rng_default))
>- cat_attr_self_link.tsv ([CP7](#cp7-f_slink_default))
>- jawiki-20190120-title2pageid_ext.tsv ([CP8](#cp8-f_title2pid_ext_default))
>- sample_cat_attr_mention_linkcand.tsv ([CP9](#cp9-f_link_prob_default))


(preprocessing)
> - jawiki-20190121-cirrussearch-content.json.gz ([CD1](#cd1-f_cirrus_content_default)) 
> - jawiki-20190120-title2pageid.json ([CD2](#cd2-f_title2pid_org_default)) 
> - shinra2022_Categorization_train_20220616.jsonl ([CD3](#cd3-f_enew_org_default))
> - jawiki-20190121-cirrussearch-content_wikipat_dis.tsv ([CM1](#cm1-f_disambiguation_pat_default)) 
> - ENEW_ENEtag_20200427_stoplist.tsv ([CM2](#cm2-f_enew_mod_list_default)) 
> - jawiki-20190120-pagelinks_dmp.tsv ([CM3](#CM3-f_back_link_dump_default)) 

### **tmp_data_dir**  (linkjpc, linkjpc_prep)
(entity linking)
- input_title.txt ([TP1](#tp1-f_input_title_default))
- back_link_full.tsv ([TP2](#tp2-f_back_link_default))
- mint_partial_match.tsv ([TP3](#tp3-f_mint_partial_default))
- mint_trim_partial_match.tsv ([TP4](#tp4-f_mint_trim_partial_default))
- tinm_partial_match.tsv ([TP5](#tp5-f_tinm_partial_default))
- tinm_trim_partial_match.tsv ([TP6](#tp6-f_tinm_trim_partial_default))
- html_tag_info.tsv ([TP7](#tp7-f_html_info_default))

### **sample_gold_dir**  (linkjpc_prep)

  In case of preprocessing, create the following directories (bold fonts) and place the sample gold data (*.json, [IT3](#it3-sample-gold-data)) and html files ([IT4](#it4-original-articles-of-sample-data-html)).  
  The name of the bottom directory of sample gold data should be '**link_annotation**'.  
  Html files should be placed in subdirectories corresponding their category directory under '**html**', respectively.  

(preprocessing)

```angular2html
  + link_annotation (*1)       
     + Airport.json (IT3)
     + City.json (IT3)
     + Company.json (IT3)
     + Compound.json (IT3)
     + Conference.json (IT3)
     + Lake.json (IT3)
     + Person.json (IT3)
   + html               
     + Airport         
       + *.html (IT4)
     + City
       + *.html (IT4)
     + Company
       + *.html (IT4)
     + Compound
       + *.html (IT4)
     + Conference
       + *.html (IT4)
     + Lake
       + *.html (IT4)
     + Person
       + *.html (IT4)
  ```
  *1: [SP1](#sp1-sample-gold-data-info) files (*.tsv) will be also created in the same directory in preprocessing.

# DATA DESCRIPTION

## (1) project SHINRA data distribution
## (1-1) test data and html files (in_dir)
### IT1 (test data)
- filename: '[ENE category].json'
- description: Test data.
- available from: [SHINRA2022](http://2022.shinra-project.info/data-download/) サブタスク固有データ/リンキング ([ベースラインデータ/リーダーボード入力データ]()) 
- used in: (linkjpc) linkjpc, (linkjpc_prep) linkjpc_prep

### IT2 (original articles of test data (*.html))
- filename: *.html
- description: *.html files of the original articles of test data. The files are grouped by ENE categories (eg. 'Airport, 'CIty, etc.)
- available from: [SHINRA2022](http://2022.shinra-project.info/data-download/) サブタスク固有データ/リンキング ([評価データ: 入力ファイル、対象のWikipediaページ]())
- used in: (linkjpc_prep)gen_html_info_file

## (1-2) (sample data(=training data) and html files (sample_gold_dir)
### IT3 (sample gold data)
- filename: '[ENE category].json'
- description: Sample gold data.
- available from: [SHINRA2022](http://2022.shinra-project.info/data-download/) サブタスク固有データ/リンキング ([教師データ](https://drive.google.com/file/d/12aR95_a0oSTeEBG6fgBvxjDq-trEruWc/view?usp=sharing)) 
- used in: (linkjpc_prep)gen_link_prob_file

### IT4 (original articles of sample data (*.html))
- filename: ***.html**
- description: *.html files of the original articles of sample data. The files are grouped by ENE categories (eg. Airport, City, etc.)
- available from: [SHINRA2022](http://2022.shinra-project.info/data-download/) サブタスク固有データ/リンキング ([教師データ](https://drive.google.com/file/d/1b9Xm-Qd1sVfmDr8o4y3t-dVnGai15P-q/view?usp=sharing)) 
- used in: (linkjpc_prep)gen_html_info_file

## (1-3) other task data (common_data_dir)

### CD1 (f_cirrus_content_default) 
 - filename: '**wikipedia-ja-20210823-json.gz**'
 - based on Wikipedia 20210823
 - description: Wikipedia Cirrus Dump (content)
 - available from: SHINRA homepage
 - used in: (linkjpc_prep) gen_disambiuation_file, gen_incoming_link_file

### CD2 (f_title2pid_org_default)
 - filename: '**jawiki-20210820-title2pageid.jsonl**'
 - based on: Wikipedia 20210820
 - description: Title to pageid conversion info list
 - available from: SHINRA homepage???
 - sample: 
   - `{"page_id": 302067, "title": "イギリス語", "is_redirect": true,
 "redirect_to": {"page_id": 3377, "title": "英語", "is_redirect": false}}`
   - `{"page_id": 311957, "title": "風と共に去りぬ_(宝塚歌劇)", "is_redirect": false}`
 - used in: (linkjpc_prep) linkedjson2tsv, gen_redirect_info_file


### CD3 (f_enew_org_default)  
 - filename: '**shinra2022_Categorization_train_20220616.jsonl**'
 - description: SHINRA2022 training data for Classification task.
 - available from: SHINRA homepage
 - based on: Wikipedia 2019, ENE9
 - sample:
   - `{"page_id":"1478897","title":"スキマスイッチ ARENA TOUR'07 \"W-ARENA\"THE MOVIE","ENEs":{"HAND.AIP.202204":[{"prob":1,"ENE":"1.7.13.6"}]}}`
 　- `{"page_id":"1715611","title":"虹 〜もうひとつの夏〜","ENEs":{"HAND.AIP.202204":[{"prob":1,"ENE":"1.7.13.5"}]}}` 
   - `{"page_id":"72942","title":"バックス (ローマ神話)","ENEs":{"HAND.AIP.202204":[{"prob":1,"ENE":"1.2"}]}}` 
 - used in: (linkjpc_prep) gen_enew_info_file

### CD4 (f_ene_def_for_task_default)
 - filename: '**ene_definition_v9.0.0-with-attributes-and-shinra-tasks-20220714.jsonl**'
 - description: ENE definition for SHINRA task.
 - available from: SHINRA homepage
## (2) manually created data (common_data_dir)

Download the data listed below from _URL(to be prepared)_ .  
(Or you might create them by yourself :)

### CM1 (f_disambiguation_pat_default)
 - (SHINRA2021: Wikipedia2019)
 - filename: '**wikipat_dis.tsv**'
 - description: Disambiguation page judgment rules list.
 - format: target, position, expression (*.tsv)
 - sample:
   - cat     end     曖昧さ回避 
 - created by: manually
 - used in: (linkjpc_prep) gen_disambiguation_file

### CM2 (f_enew_mod_list_default)
 - filename: '**ENEW_ENEtag_20200427_stoplist.tsv**'
 - description: ENEW modification list 
 - format: ENEID, pid, title (*.tsv)
 - sample: 
   - `1.5.1.3 1419479 フランス陸軍参謀総長`
 - created by: manually
 - used in: (linkjpc_prep) gen_enew_info_file

### CM3 (f_back_link_dump_default) 
 - (SHINRA2021: Wikipedia2019)
 - filename: '**jawiki-20190120-pagelinks_dmp.tsv**'
 - description: Back link dump file converted from jawiki-20190120-pagelinks.sql.
 - format: back link pid, org_title (*.tsv)
 notice: 
 - The original sql file is available from: project SHINRA data distribution, [SHINRA2021-LinkJP](http://shinra-project.info/shinra2021linkjp/) (公開データ/コード,  [リンク先のWikipediaデータ(WikiDump)](https://drive.google.com/drive/folders/1emH81ac0e1kYKAF4mvpCslRAgBKCN_Ah?usp=sharing)))
 - created by: 
 ```mysql -u root -D pagelink < jawiki-20190120-pagelinks.sql```
 - used in: (linkjpc_prep) gen_back_link_info_file
 - (SHINRA2022: Wikipedia2019)


### CM4 (f_wl_lines_backward_ca_default)
 - filename: '**wl_lines_backward_ca.tsv**'
 - description: The file to specify maximum number of line to backward-search Wikipedia links in the page for each category-attribute pair.
 - notice: 
   - The default file contains just one example and should be modified. 
 - format:
   - ene_label_en, attribute_name, distance (*.tsv)
 - sample:
   - `Person  作品    -3`
 - used in: (linkjpc) gw.reg_mention_gold_distance_ca

### CM5 (f_wl_lines_forward_ca_default)
 - filename: '**wl_lines_forward_ca.tsv**'
 - description: The file to specify maximum number of line to forward-search Wikipedia links in the page for each category-attribute pair.
 - notice: 
   - The default file contains just one example and should be modified.  
 - format:
   - ene_label_en, attribute_name, distance (*.tsv)
 - sample:
   - `Person  作品    1`
 - used in: (linkjpc) gw.reg_mention_gold_distance_ca

### CM6 (f_attr_rng_man_org_default)
 - filename: '**attr_rng_man_org_ene90_20221002.tsv**'
 - format: ene_label_en, attribute_name, range, probability (*.tsv)
   - (range):    'ene':eneid
 - sample:
   - `Military_Ship   乗船者  1.1 1`
 - created by: manually
 - used in: (linkjpc)gen_attr_rng


### CM9 (f_self_link_pat_default)
 - filename: '**self_link_pat.tsv**'
 - format: pos, pat (*.tsv)
 - sample:
   - start   別名
   - start   合併
 - created by: manually
 - used in: (linkjpc_prep)gen_self_link_by_attr_name

### CM11 (f_redirect_dump_org_default)
 - filename:'***jawiki-20210820-redirect_dmp.tsv***'
 - description: Wikipedia redirect dump 
 - format: rd_from, rd_title, rd_namespace
 - sample:
   -- `557692	宮下杏菜	0`<br>
   -- `557693	宮下杏菜	0`<br>
   -- `1699304	広瀬香美_THE_BEST_"Love_Winters"	0`<br>
   -- `1855418	広瀬香美_THE_BEST_"Love_Winters"	0`<br>
　
 - based on: jawiki-20210820-redirect.sql.gz)

### CM12 (f_redirect_dump_default)
 - filename:'***jawiki-20210820-redirect_dmp_rev.tsv***'
 - description: Wikipedia redirect dump modified version<br>
   -- deleted: (a) titles with single punctuation symbols, (b) 'redirects to' titles in namespaces other than zero are omitted<br>
   -- escaped: double quotations
 - format: rd_from, rd_title, rd_namespace
 - sample:<br>
   -- `557692	宮下杏菜	0`<br>
   -- `557693	宮下杏菜	0`<br>
   -- `1699304	広瀬香美_THE_BEST_\"Love_Winters\"	0`<br>
   -- `1855418	広瀬香美_THE_BEST_\"Love_Winters\"	0`<br>
 - original: 'jawiki-20210820-redirect_dmp.tsv' (based on: jawiki-20210820-redirect.sql.gz)
 - created by:<br>
    - `$ awk 'BEGIN{FS="\t"}$2 !~ /^[[:punct:]]$/{print}' jawiki-20210820-redirect_dmp.tsv | perl -pe 's/\"/\"\"/g;' > jawiki-20210820-redirect_dmp_rev.tsv`
 - notice: 
  -- punctuation symbols in awk(!"#$%&'-=^~\|@`...)

### CM13 (f_page_dump_org_default)
 - filename:'***jawiki-20210820-page_dmp.tsv***'
 - description: Wikipedia page dump<br>
 - format:  page_id, page_title, page_is_redirect, page_namespace
 - sample:<br>
 -- `517804	宮下杏菜	0	0`<br>
 -- `557692	宮下杏奈	1	0`<br>
 -- `557693	広末由依	1	0`<br>
 -- `1698838	アメリカ合衆国	0	0`<br>
 -- `9575	アメリカ合衆国	0	1`<br>
 -- `127671	アメリカ合衆国	0	14`<br>
 -- `582422	アメリカ合衆国	0	102`<br>
 -- `1033542	アメリカ合衆国	0	103`<br>
 -- `1696323	広瀬香美_THE_BEST_"Love_Winters"	0	0`<br>
 -- `1699304	広瀬香美_THE_BEST"Love_Winters"	1	0`<br>
 - notice:
 -- based on: jawiki-20220820-page.sql.gz


### CM14 (f_page_dump_default)
 - filename:'***jawiki-20210820-page_dmp_rev.tsv***'
 - description: Wikipedia page dump<br>
   -- deleted: titles with single punctuation symbols<br>
   -- escaped: double quotations 
 - format:  page_id, page_title, page_is_redirect, page_namespace
 - sample:<br>
 -- `934006	安倍晋三	0	1`<br>
 -- `2694582	安倍晋三	0	3`<br>
 -- `2697850	安倍晋三	0	2`<br>
 -- `2747973	安倍晋三	0	14`<br>
 -- `4136738	安倍晋三	0	0`<br>
 -- `517804	宮下杏菜	0	0`<br>
 -- `557692	宮下杏奈	1	0`<br>
 -- `557693	広末由依	1	0`<br>
 -- `1698838	アメリカ合衆国	0	0`<br>
 -- `9575	アメリカ合衆国	0	1`<br>
 -- `127671	アメリカ合衆国	0	14`<br>
 -- `582422	アメリカ合衆国	0	102`<br>
 -- `1033542	アメリカ合衆国	0	103`<br>
 -- `1696323	広瀬香美_THE_BEST_\"Love_Winters\"	0	0`<br>
 -- `1699304	広瀬香美_THE_BEST\"Love_Winters\"	1	0`
 - original: 'jawiki-20210820-page_dmp.tsv' (based on: jawiki-20210820-page.sql.gz)<br>
 - created by:<br>
  -- `$ awk 'BEGIN{FS="\t"}$2 !~ /^[[:punct:]]$/{print}' jawiki-20210820-page_dmp.tsv | perl -pe 's/\"/\"\"/g;' > jawiki-20210820-page_dmp_rev.tsv`<br>
 - notice: 
  -- pageid: 2021 
  -- punctuation symbols in awk(!"#$%&'-=^~\|@`...)

## CM15 (f_page_dump_old_org_default)
 - filename:'***jawiki-20190120-page_dmp.tsv***'
 - description: Wikipedia page dump (20190120)<br>
   -- deleted: titles with single punctuation symbols<br>
   -- escaped: double quotations 
 - format:  page_id, page_title, page_is_redirect, page_namespace
 - sample:<br>
 -- `934000	安倍晋三	0	0`<br>
 -- `934006	安倍晋三	0	1`<br>
 -- `2694582	安倍晋三	0	3`<br>
 -- `2697850	安倍晋三	0	2`<br>
 -- `2747973	安倍晋三	0	14`<br>
 - based on: jawiki-20190120-page.sql.gz<br>
 - created by:<br>
  -- `$ awk 'BEGIN{FS="\t"}$2 !~ /^[[:punct:]]$/{print}' jawiki-20190120-page_dmp.tsv | perl -pe 's/\"/\"\"/g;' > jawiki-20210820-page_dmp_rev.tsv`<br>
 - notice: 
  -- pageid: 2021 
  -- punctuation symbols in awk(!"#$%&'-=^~\|@`...)

## CM16 (f_lang_link_dump_org_default)

 - filename:'***jawiki-20210820-langlinks_dmp.tsv***'
 - description: Langlinks dump (20210820)
 - format: from page(Japanese Wikipedia wgarticleID), lang code, title
 - sample: <br>
 -- `102349	ast	Chanel`
 -- `102349	az	Chanel`
 -- `102349	ca	Chanel`
 -- `102349	da	Chanel`
 -- `102349	de	Chanel`
 -- `102349	el	Chanel`
 -- `102349	en	Chanel`
 - based on: jawiki-20210820-langlinks.sql.gz<br>


## (3) data created by preprocessing tools
## (3-1) (sample_gold_dir)

### SP1 (sample gold data info)
 - filename: **Airport.tsv, City.tsv, 'Company.tsv, 'Compound.tsv, 'Conference.tsv, 'Lake.tsv, 'Person.tsv** 
 - description: Sample gold data info.
 - format: category,  org_pageid, org_title, attribute_name, mention, start_line_id, start_offset, end_line_id, 
 - end_offset, gold_pageid, gold_title, gold_eneid, gold_ene_category (*.tsv)
 - sample:<br>
 - `Person	1058520	竹内えり	作品	白い巨塔	79	0	79	4	29582	
白い巨塔 (2003年のテレビドラマ)	['1.7.13.2']　['Broadcast_Program']`
 - `Person	990044	細井雄二	作品	快傑ズバット	107	1	107	7	130767	快傑ズバット	['1.7.12', '1.7.13.2']	
['Character', 'Broadcast_Program']`
 - created by: (linkjpc_prep --gen_sample_gold_tsv) gen_sample_gold_tsv
 - used in: (linkjpc_prep) gen_link_prob_file, gen_mention_gold_link_dist

## (3-2) (common_data_dir)

### CP1 (f_common_html_info_default) 
 - filename: '**common_html_tag_info.tsv**'
 - description: Info on embedded links to other Wikipedia pages in original articles of sample data
 - format: 
   - cat, pid, line_id, text_start, text_end, text, title (*.tsv)
 - sample: 
   - `City    1617736 90      292     298     リンブルフ州 リンブルフ州 (ベルギー)`
 - created by: gen_html_info_file
 - used in: (linkjpc_prep) gen_mention_gold_link_dist

### CP2 (f_disambiguation_default)
 - filename: '**jawiki-20210823-cirrussearch-content_disambiguation.tsv**'
 - description: Disambiguation page list.
 - format: pageid, title (*.tsv)
 - sample: 
   - `1128763 テトラ (曖昧さ回避)`
   - `3077413	ハムレット (曖昧さ回避)`
 - notice: 
   - pageid: 2021 
 - created by: (linkjpc_prep --redirect) gen_disambiguation_file
 - used in: (linkjpc_prep) gen_redirect_info_file

### CP3 (f_redirect_info_default) 
 - filename: '**jawiki-20210823_title2pageid_20210820_nodis.tsv**'
 - description: Redirect info file, a modification of original from_title to_pageid information file to exclude disambiguation pages and ill-formatted pages. 
 - format: title, pageid (*.tsv)
 - sample: 
   - `1904年アメリカ合衆国大統領選挙  1477879`
   - `風と共に去りぬ (宝塚歌劇)311957`
 - notice:
   - based on original redirect file(f_title2pid_org_default, jawiki-20210823_title2pageid_20210820.jsonl).
   - recovered white spaces in Wikipedia titles which are replaced by '_' in the original redirect file.
   - Info on ill formatted pages or disambiguation pages are excluded though not completely.
 - created by: (linkjpc_prep --redirect) gen_redirect_info_file
 - used in: (linkjpc_prep) gen_title2pid_ext_file

### CP4 (f_incoming_default) 
 - filename: '**jawiki-20210823-cirrussearch-content_incoming_link.tsv**'
 - description: Incoming link num info list.
 - format:
   - pageid, title, number of incoming links (*.tsv) 
 - sample: 
   - `311957	風と共に去りぬ (宝塚歌劇)	1091`
   - `345792  ピノッキオの冒険        233`
 - created by: (linkjpc_prep --gen_incoming_link) gen_incoming_link_file
 - used in: (linkjpc_prep) gen_title2pid_ext_file

### CP5 (f_enew_info_default) 
 - filename: '**ENEW_ENEtag_20200427_mod.tsv**'
 - description:
   - ENEW info (based on slightly modified version of ENEW (20200427)).
   - modification list: ENEW_ENEtag_20200427_stoplist.tsv (f_enew_mod_list_default)
 - format:
   - pageid, ENEid, title (*.tsv) 
 - sample: 
   - `311957	1.7.19.4	風と共に去りぬ (宝塚歌劇)`
   - `345792  1.7.19.6        ピノッキオの冒険`
 - notice: 
    - Not all target pageids are included in the file. (eg. 3682608, 3386984)
 - created by: (linkjpc_prep --gen_title2pid) gen_enew_info_file
 - used in: (linkjpc_prep) gen_title2pid_ext_file
 
### CP6 (f_mention_gold_link_dist_default) 
 - filename: '**mention_gold_link_dist.tsv**'
 - description: Mention goldlink dist file, which shows the distance (number of lines) between mentions and (nearest) gold links in sample html files.
 - format: ene_label_en, attribute_name, distance (.tsv)
 - sample: 
   - `Person 作品 -1`
   - `Person 作品 29`
 - notice: the values are based on sample data
 - created by: (linkjpc_prep --gen_link_dist) gen_mention_gold_link_dist
 - used in: (linkjpc_prep --gen_link_dist) gen_mention_gold_link_dist_info

### CP7 (f_slink_default) 
 - filename: '**cat_attr_self_link.tsv**'
 - description: Self link info file to estimate the probability of linking to the original article for each category-attribute pair. 
 - format: ene_label_en, attribute_name, ratio (*.tsv)
 - sample:
   - `City	合併市区町村	0.47	156	333`
 - note: The ratio is based on SHINRA2021-LinkJP sample data (ver.20210428).
 - created by: (linkjpc_prep --gen_slink) gen_self_link_info
 - used in: (linkjpc) sl.check_slink_info

### CP8 (f_title2pid_ext_default) 
 - filename: '**jawiki-20210823_title2pageid_20210820_ext.tsv**'
 - description: Summary information on title to pageid conversion, incoming links, and ENE classification of articles. .
 - format: 
   - from_title, to_pid, to_title, to_incoming, to_eneid_set (*.tsv)
 - sample: 
   - `ロメオとジュリエット	28783	ロミオとジュリエット	806	{'1.7.13.4', '1.7.13.5'}  `
   - `安倍晋三	4136738	安倍晋三	3337	{'1.1'}  
 - created by: gen_title2pid_ext_file
 - used in: (linkjpc_prep --gen_title2pid) gen_back_link_info_file (get_to_pid_to_title_incoming_eneid), 
    prematching_mention_title (reg_pid2title), 
    gen_self_link_info (get_category)
   (linkjpc) ljc_main, lc.reg_title2pid_ext
 
### CP9 (f_link_prob_default) 
 - filename: '**sample_cat_attr_mention_linkcand.tsv**'
 - description: Link probability info file. 
 - format: 
   - ene_label_en, attribute_name, mention, link_cand_pageid:prob:freq;...(.tsv)
 - sample: 
   - `City	合併市区町村	上村	151917:0.25:1;37423:0.25:1;381057:0.25:1;1872659:0.25:1`
 - notice:
   - The ratio is based on LinkJP2021 sample data ver.20210428.
 - created by: (linkjpc_prep --gen_link_prob) gen_link_prob_file 
 - used in: (linkjpc) lp.get_link_prob_info

### CP10 (f_linkable_info_default) 
 - filename: '**cat_attr_linkable.tsv**'
 - description: Linkable info file. 
 - format: 
   - ene_label_en, attribute_name, ratio (*.tsv)
 - sample: 
   - `Train   駆動方式        0.67`
   - `Train   制御装置        0.33`
 - notice:
   - The ratio is based on LinkJP2022 training data ver.202207.
 - created by: (linkjpc_prep --gen_linkable) gen_linkable_info_file 
 - used in: (linkjpc) dn.check_linkable_info

### CP11 (f_nil_default) 
 - filename: '**cat_attr_nil.tsv**'
 - description: Nil info file to estimate the probability of nil link for each category-attribute pair. 
 - format: ene_label_en, attribute_name, ratio (*.tsv)
 - sample:
   - `Person  家族    0.0`
   - `Person  別名    1.0`
 - note: The ratio is based on SHINRA2022-LinkJP training data (ver.202207).
 - created by: (linkjpc_prep --gen_nil) gen_nil_info
 - used in: (linkjpc) 

~~### CP14 (f_self_link_attr_info_default)   
    -- filename:'***self_link_attr_info_file***'
    - format: attribute name, self_link ratio, self_link num, freq
    - sample:
    -- 別名  1.0   100  100
    -- 標語　0.0     0   10
    -- 種類　0.0     0   20~~

### CP15 (f_attr_rng_man_default)
 - filename: '***cat_attr_rng_man.tsv***'
 - format: cat, attr, rng_eneid, rng_cat, ratio
 - sample: <br>
 - `School  理事長  1.1 Person      1.0`

### CP15 (f_attr_rng_auto_default)
 - filename: '***cat_attr_rng_auto.tsv***'
 - format: cat, attr, eneid, ratio, freq', sum(cat*attr)
 - sample: <br>
 - `Music   プロデューサー  1.1   Person  1.0  10   10`

### CP16 (f_lang_link_info_default) 
 - filename: '***jawiki-20210820-langlinks_info.tsv***'
 - format: from page(Japanese Wikipedia wgarticleID), lang code, title
 - sample: <br>
 -- `102349	ast	Chanel`
 -- `102349	az	Chanel`
 -- `102349	ca	Chanel`
 -- `102349	da	Chanel`
 -- `102349	de	Chanel`
 -- `102349	el	Chanel`
 -- `102349	en	Chanel`
 - based on: jawiki-20210820-langlinks.sql.gz
 - notice: illegal characters (UnicodeDecodeError) are converted to '?'.
 - created by: (linkjpc_prep --gen_lang_link) gen_lang_link_info
 
### CP17 (f_target_attr_info_default)
 - filename: '**ene_definition_v9.0.0-20220714_target_attr.tsv**'
 - format: ene_label_en, attribute_name, (*.tsv)
 - sample:
   - `1.1	人名	Person	別名・旧称`
   - `1.1	人名	Person	国籍`
 - created by: (linkjpc_prep)gen_target_attr_info
 - used in: (linkjpc)gen_self_link_info, lc.reg_target_attr_info

### CP18 (f_all_cat_info_default)
 - filename: '**ene_definition_v9.0.0-20220714_all_cat.tsv**'
 - format: ene_id, ene_label_ja, ene_label_en, (*.tsv)
 - sample: <br>
 - `0	ＣＯＮＣＥＰＴ	CONCEPT`
 - `1	名前	Name`
 - `1.0	名前＿その他	Name_Other`
 - `1.1	人名	Person`
 - `1.2	神名	God`

 - notice:
   - Some categories lack attributes.
 - created by: (linkjpc_prep)gen_target_attr_info 
 - used in: 
 - 
### CP19 (f_self_link_by_attr_name_default)
 - filename: '**self_link_by_attr_name.tsv**'
 - format: attr
 - sample:
   - 別名・旧称
   - 合併市区町村
 - created by: gen_self_link_by_attr_name
 - used in: (linkjpc_prep)gen_self_link_by_attr_name

## (3-3) (tmp_data_dir)

### TP1 (f_input_title_default)
 - filename: '**input_title.txt**'
 - description: Title list of test data.
 - format:
   - title (*.txt) 
 - created by: (linkjpc_prep --gen_back_link) extract_input_title
 - used in: (linkjpc_prep) gen_back_link_info_file
 
### TP2 (f_back_link_default) 
 - filename: '**back_link_full.tsv**'
 - description: Back link info file, which shows the title pages of test data and the back links to the pages
 - format: org_title, back link (from) pid, back link (from) title (*.tsv)
 - sample: 
   - `1975年度新人選手選択会議 (日本プロ野球)	143952	中畑清`
 - notice: 
   - based on jawiki-20210820-pagelinks.sql
 - created by: (linkjpc_prep --gen_back_link) gen_back_link_info_file
 - used in: (linkjpc) bl.check_back_link_info

### TP3 (f_mint_partial_default) 
 - filename: '**mint_partial_match.tsv**'
 - description: Mention-title matching ratio list (mention in title, full title)
 - format: mention, pid, title, ratio (*.tsv)
 - sample:
   - `風と共に去りぬ	457696	風と共に去りぬ	1.0`
   - `風と共に去りぬ	671718	風と共に去りぬ (映画)	0.58`
   - `風と共に去りぬ	311957	風と共に去りぬ (宝塚歌劇)	0.5`
 - created by: (linkjpc_pre --pre_matching) prematch_mention_title
 - used in: (linkjpc) ljc_main, mc.reg_matching_info

### TP4 (f_mint_trim_partial_default) 
 - filename: '**mint_trim_partial_match.tsv**'
 - description: Mention-title matching ratio list (mention in title, trimmed title)
 - notice:
   - Disambiguation descriptions enclosed in braces in titles are not used for matching.
 - format: See f_mint_partial_default
 - sample:
   - `風と共に去りぬ	311957	風と共に去りぬ (宝塚歌劇)	1.0`
   - `風と共に去りぬ	671718	風と共に去りぬ (映画)	1.0`
   - `風と共に去りぬ	457696	風と共に去りぬ	1.0`
 - created by: (linkjpc_pre --pre_matching) prematch_mention_title
 - used in: (linkjpc) ljc_main, mc.reg_matching_info
 
### TP5 (f_tinm_partial_default) 
 - filename: '**tinm_partial_match.tsv**'
 - description: Mention-title matching ratio list (title in mention, full title)
 - format: mention, pid, title, ratio (*.tsv)
 - sample:
   - `風と共に去りぬ	457696	風と共に去りぬ	1.0`
   - `風と共に去りぬ	895511	風と共に	0.57`
 - created by: (linkjpc_pre --pre_matching) prematch_mention_title
 - used in: (linkjpc) ljc_main, mc.reg_matching_info
 
### TP6 (f_tinm_trim_partial_default) 
 - filename: '**tinm_trim_partial_match.tsv**'
 - description: Mention-title matching ratio list (title in mention, tinm title)
 - notice:
   - Disambiguation descriptions enclosed in braces in titles are not used for matching
 - format: 
   - mention, pid, title, ratio (.tsv)
 - sample:
   - `風と共に去りぬ	311957	風と共に去りぬ (宝塚歌劇)	1.0`
   - `風と共に去りぬ	671718	風と共に去りぬ (映画)	1.0`
   - `風と共に去りぬ	457696	風と共に去りぬ	1.0`
   - `風と共に去りぬ	895511	風と共に	0.57`
   - `風と共に去りぬ	3624861	風と共に (曲)	0.57`
 - created by: (linkjpc_pre --pre_matching) prematch_mention_title
 - used in: (linkjpc) ljc_main, mc.reg_matching_info

### TP7 (f_html_info_default)  
 - filename: '**html_tag_info.tsv**'
 - description: Info on embedded links to other Wikipedia pages in original articles of test data
 - format: 
   - cat, pid, line_id, text_start, text_end, text, title (.tsv)
 - sample: 
   - `City    1617736 90      292     298     リンブルフ州    リンブルフ州 (ベルギー)`
 - created by: (linkjpc_prep --gen_html) gen_html_info_file
 - used by: (linkjpc) gw.reg_tag_info
 
## (4) data created by entity linking
### (4-1) (out_dir)

### OL1 (output data)
 - filename: **'Airport.json', 'City.json', ....**
 - description: Output data.
 - format: [SHINRA2022](http://shinra-project.info/shinra2021linkjp/#data-format)

### (4-2) (common_data_dir)

### CL1 (f_mention_gold_link_dist_info_default) 
 - filename: '**mention_gold_link_dist_info.tsv**'
 - description: Summary of distance from mentions to links to gold pages by category and attribute.
 - format: 
   - cat, attr, backward_limit, forward_limit, diff_backward_num, diff_forward_num, diff_same_num, all_num (tsv)
 - sample:
   - Person  地位職業        -47     7       18      90      -63     45
   - Person  生誕地  -57     6       9       21      15      45
 notice: the values are based on - sample data
 - created by: (linkjpc) gw.reg_mention_gold_distance
 - used in: (linkjpc) gw.reg_mention_gold_distance



