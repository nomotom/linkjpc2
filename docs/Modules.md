# Modules

主要モジュール、フィルタとオプションの説明です。
- (_NEW_): 新規追加

## 主要モジュールとオプション


### **matching.py(ma)** 
  -メンションと候補ページのタイトルの文字列マッチ<br>

| option                         | 説明      |
|--------------------------------|-----------|
| char_match_cand_num_max/-c_max | リンク先候補の最大値                                                          |
| multi_lang                     | 外国語表記のメンションに対応（言語間リンク使用)                                            |
| mint                           | (mint)タイトルにメンション文字列を含むページへのマッチング(mention in title)方法(完全一致/部分一致)     |
| mint_min                       | (mint)文字列一致率の最小値                                                    |
| title_matching_mint/tmm        | (mint)タイトルの丸括弧の扱い(full/trim(括弧を外す))                                 |
| f_mint                         | (mint)文字列一致情報ファイル(full)                                             |
| f_mint_trim                    | (mint)文字列一致情報ファイル(trim)')                                           |
| tinm                           | (tinm)メンション文字列に含まれるタイトルをもつページへのマッチング(title in mention)方法(完全一致/部分一致) |
| tinm_min/t_min                 | (tinm)文字列一致の最小値                                 |                    
| title_matching_tinm/tmt        | (tinm)タイトルの丸括弧の扱い(full/trim(括弧を外す))                                 |
| f_tinm                         | (tinm)文字列一致情報ファイル(full)                                             |
| f_tinm_trim                    | (tinm)文字列一致情報ファイル(trim)                                  |

### **self_link.py(sl)** 
再帰リンクの推定 (メンションから元記事へのリンクをサンプルデータ正解の統計情報から推定。典型的には別名などの特別な属性の場合。）

|option| 説明                           |
|----|------------------------------|
|slink_min/s_min| 再帰リンク率の最小値                   |
|slink_prob| 再帰リンクスコアの計算方法                |
|f_slink| 再帰リンク率情報ファイル                 |
|f_self_link_by_attr_name| 再帰リンク用属性名リスト（属性名から推定する場合に利用） |

### **get_wlink.py(gw)** 
   - メンションのリンク先を元記事の埋め込みリンクから探す。

| option                                | 説明                                                                                                                                                                             | 関連option      |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| wlink/wl                              | Wikipediaリンクのスコアリング方法(どの環境に現れたタグに加点するか)                                                                                                                                        |
| f_html_info                           | htmlタグ情報ファイル                                                                                                                                                                   |               | 
| wf_score/wf                           | メンション内の最初のWikipediaリンクに与えるスコア                                                                                                                                                  | (wlink:f)     |
| wr_score/wr                           | メンション内の最右のWikipediaリンクに与えるスコア                                                                                                                                                  | (wlink:r)     |  
| wp_score/wp                           | ページ内で前出のメンションのWikipediaリンクに与えるスコア                                                                                                                                              | (wlink:p)     |
| wl_score_same/wls                     | メンション周辺（同一行）にあるWikipediaリンクに与えるスコア                                                                                                                                             | (wlink:l)     |
| wl_score_backward/wlb                 | メンション周辺（後の行）にあるWikipediaリンクに与えるスコア                                                                                                                                             | (wlink:l)     |  
| wl_score_forward/wlf                  | メンション周辺（前の行）にあるWikipediaリンクに与えるスコア                                                                                                                                             | (wlink:l)     |
| wl_break/no-wl_break                  | 候補のリンクが見つかったら探索をやめるかどうかのフラグ                                                                                                                                                    |               | 
| wl_lines_backward_max                 | メンションを含むから遡ってWikipediaリンクを探す行数の最大値                                                                                                                                             |               |
| wl_lines_forward_max/wl_fmax          | メンションを含む行以降でWikipediaリンクを探す行数の最大値                                                                                                                                              |               |
| wl_lines_backward_ca                  | 各カテゴリ-属性のペアについてメンションから遡ってWikipediaリンクを探す際の行数？の最大値の決定方法                                                                                                                         |               | 
| wl_lines_forward_ca/wl_fca            | 各カテゴリ-属性のペアについてメンション以降でWikipediaリンクを探す際の行数？の最大値の決定方法                                                                                                                           |               |
| f_wl_lines_backward_ca/f_wl_bca       | 各カテゴリ-属性のペアについてメンションから遡ってWikipediaリンクを探す際の行数？の最大値の指定ファイル                                                                                                                       | (wl_lines_backward_ca:f) |    
| f_wl_lines_forward_ca/f_wl_fca        | 各カテゴリ-属性のペアについてメンション以降でWikipediaリンクを探す際の行数？の最大値の指定ファイル                                                                                                                         | (wl_lines_lines_forward_ca:f) |
| wl_lines_backward_ca_ratio            | 各属性についてメンションから遡ってWikipediaリンクを探す際の行のratioの最大値（サンプルデータの統計から推定）)                                                                                                                 |               |
| wl_lines_forward_ca_ratio/wl_fca_ratio | 各属性についてメンション以降でWikipediaリンクを探す際の行のratioの最大値（サンプルデータの統計から推定）                                                                                                                    |               |
| f_mention_gold_link_dist_info         | 　サンプルデータのメンションと正解Wikipediaリンクの距離に関する統計情報のファイル                                                                                                                                  |              |
| nil_all_freq_min/-n_af_min            | リンク確率情報ファイルに記載するカテゴリ-属性-メンションの組の頻度の最小値 |  |

### **link_prob.py(lp)** 
   - メンションとページのリンク確率をサンプルデータ正解の統計情報から推定。

| option  | 説明   |
|---------|------|
|lp_min/l_min|カテゴリ-属性-メンションの組に対してリンク確率情報ファイルに記載するリンク確率の最小値|
|f_link_prob|リンク確率情報ファイルのファイル名|

## フィルタリング 
### **attr_range_filtering.py(ar)** 
- メンション(属性値)のクラスによるフィルタリング

| option                        | 説明                                                              |
|-------------------------------|-----------------------------------------------------------------|
| attr_rng_auto_freq_min/af_min | トレーニングデータからrangeの情報を取得するメンションの頻度の最小値)        |                                                        | 
| attr_rng_tgt/ar_tgt           | メンション(属性値)のrange(とりうる値のタイプ、現状はENEカテゴリでクラスを指定)によるフィルタリングの対象モジュール |
| f_attr_rng_auto               | メンション(属性値)のrangeによるフィルタリングの定義情報ファイル(サンプルデータの統計を元に自動で作成).e da')  |
| f_attr_rng_man                | メンション(属性値)のrangeによるフィルタリングの定義情報ファイル(人手での定義がベース))                |
| f_attr_rng_merged             | メンション(属性値)のrangeによるフィルタリングの定義情報ファイル(マージ).                       |
| f_enew_info                   | ENEW情報ファイルのファイル名                                                |
| attr_na_co/anc                | ENEWがない候補ページの基本スコア(attr_na_co)                                  |                           
| attr_ng_co/ang                | メンション(属性値)のrangeが一致しない候補ページの基本スコア                               |
| attr_len                      | メンション(属性値)のrangeが一致する候補ページのENEIDのスコアリング                         |
| attr_rng_type/art             | メンション(属性値)のrangeによるフィルタリング方法'                                   |

### **incl_filtering.py(il)** 
 - 被リンク数によるフィルタリング

| option           | 説明                             |
|------------------|--------------------------------|
| incl_max/i_max   | 被リンク数によるフィルタリングで候補とする被リンク数の最大値 |
| incl_tgt/i_tgt   | 被リンク数によるフィルタリングの対象モジュール        |
| incl_type/i_type | 被リンク数によるフィルタリング方法              |

### **back_link.py(bl)** 
- 被リンクによるフィルタリング

| option                     | 説明                                                                                                                 |
|----------------------------|--------------------------------------------------------------------------------------------------------------------|
|back_link_tgt/bl_tgt|被リンクによるフィルタリングの対象モジュール|
|back_link_ng/bl_ng|被リンクなしのスコア|
|back_link_ok/bl_ok|被リンクありのスコア|

### **detect_nil.py(dn)  ** _(NEW)_
- nil detection(リンクなしの判定) によるフィルタリング
- 各モジュールの処理前に判定

| option                    | 説明                                          | 関連option                           |
|---------------------------|---------------------------------------------|------------------------------------|
| nil_all_freq_min/n_af_min | リンク確率情報ファイルでリンク確率を記述する対象となるカテゴリ-属性-メンションの組のサンプルデータでの頻度の最小値 |                                    |
| nil_tgt/n_tgt             | nil detectionの対象モジュール                       ||
| nil_cond/n_cond           | nil判定の条件                                    ||
| nil_desc_exception/n_exc  | nil判定のdescriptiveness条件の適用外の例外カテゴリ-属性リスト    ||
| nil_cat_attr_max/n_max    | サンプルデータのカテゴリ-属性対のうち リンク先なしとするratioの最大値      ||
| len_desc_text_min/ld_min  | nil判定でメンションテキストがdescriptiveと判定するメンションの最小の長さ ||
| f_nil_cand_man            | nil判定対象候補のカテゴリ・属性候補(人手で記述)                  | nil_cond(cman)                     |
| f_nil_stop_attr           | nil判定対象外の属性候補(人手で記述) | nil_cond(nostop) 指定されていないものがnostop ||

