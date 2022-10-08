# Modules

#### 主要モジュールとオプション
　　**: 新規追加

- **matching.py(ma)** 
  -メンションと候補ページのタイトルの文字列マッチ<br>
2x15
- 
|option| 説明                                                                    |
|----|-----------------------------------------------------------------------|
|char_match_cand_num_max/-c_max| リンク先候補の最大値                                                            |
|multi_lang| 外国語表記のメンションに対応（言語間リンク使用)                                              |
|mint| (mint)タイトルにメンション文字列を含むページへのマッチング(mention in title)方法(完全一致/部分一致) |
|mint_min| (mint)文字列一致率の最小値                                                      |
|title_matching_mint/tmm| (mint)タイトルの丸括弧の扱い(full/trim(括弧を外す))                                   |
|f_mint| (mint)文字列一致情報ファイル(full)                                               |
|f_mint_trim| (mint)文字列一致情報ファイル(trim)')                                             |
|tinm| (tinm)メンション文字列に含まれるタイトルをもつページへのマッチング(title in mention)方法(完全一致/部分一致)   |
|tinm_min/t_min| (tinm)文字列一致の最小値
|title_matching_tinm/tmt| (tinm)タイトルの丸括弧の扱い(full/trim(括弧を外す)) |
|f_tinm| (tinm)文字列一致情報ファイル(full)|
|f_tinm_trim| (tinm)文字列一致情報ファイル(trim)|

- **self_link.py(sl)** (再帰リンクの推定)
再帰リンクの推定 (メンションから元記事へのリンクをサンプルデータ正解の統計情報から推定。典型的には別名などの特別な属性の場合。）

|option| 説明                           |
|----|------------------------------|
|slink_min/s_min| 再帰リンク率の最小値                   |
|slink_prob| 再帰リンクスコアの計算方法                |
|f_slink| 再帰リンク率情報ファイル                 |
|f_self_link_by_attr_name| 再帰リンク用属性名リスト（属性名から推定する場合に利用） |

- **get_wlink.py(gw)** 
   - メンションのリンク先を元記事の埋め込みリンクから探す。

| option                                | 説明                                                                                                                                         | 関連option      |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| wlink/wl                              | Wikipediaリンクのスコアリング方法(どの環境に現れたタグに加点するか)                                                                                                    |
| f_html_info                           | htmlタグ情報ファイル                                                                                                                               |               | 
| wf_score/wf                           | メンション内の最初のWikipediaリンクに与えるスコア                                                                                                              | (wlink:f)     |
| wr_score/wr                           | メンション内の最右のWikipediaリンクに与えるスコア                                                                                                              | (wlink:r)     |  
| wp_score/wp                           | ページ内で前出のメンションのWikipediaリンクに与えるスコア                                                                                                          | (wlink:p)     |
| wl_score_same/wls                     | メンション周辺（同一行）にあるWikipediaリンクに与えるスコア                                                                                                         | (wlink:l)     |
| wl_score_backward/wlb                 | メンション周辺（後の行）にあるWikipediaリンクに与えるスコア                                                                                                         | (wlink:l)     |  
| wl_score_forward/wlf                  | メンション周辺（前の行）にあるWikipediaリンクに与えるスコア                                                                                                         | (wlink:l)     |
| wl_break/no-wl_break                  | 候補のリンクが見つかったら探索をやめるかどうかのフラグ                                                                                                                |               | 
| wl_lines_backward_max                 | メンションを含むから遡ってWikipediaリンクを探す行数の最大値                                                                                                         |               |
| wl_lines_forward_max/wl_fmax          | メンションを含む行以降でWikipediaリンクを探す行数の最大値                                                                                                          |               |
| wl_lines_backward_ca                  | 各カテゴリ-属性のペアについてメンションから遡ってWikipediaリンクを探す際の行数？の最大値の決定方法                                                                                     |               | 
| wl_lines_forward_ca/wl_fca            | 各カテゴリ-属性のペアについてメンション以降でWikipediaリンクを探す際の行数？の最大値の決定方法                                                                                       |               |
| f_wl_lines_backward_ca/f_wl_bca       | 各カテゴリ-属性のペアについてメンションから遡ってWikipediaリンクを探す際の行数？の最大値の指定ファイル                                                                                   | (wl_lines_backward_ca:f) |    
| f_wl_lines_forward_ca/f_wl_fca        | 各カテゴリ-属性のペアについてメンション以降でWikipediaリンクを探す際の行数？の最大値の指定ファイル      | (wl_lines_lines_forward_ca:f) |
| wl_lines_backward_ca_ratio            | 各属性についてメンションから遡ってWikipediaリンクを探す際の行のratioの最大値（サンプルデータの統計から推定）)      |               |
| wl_lines_forward_ca_ratio/wl_fca_ratio | 各属性についてメンション以降でWikipediaリンクを探す際の行のratioの最大値（サンプルデータの統計から推定）                |               |
| f_mention_gold_link_dist_info         | 　サンプルデータのメンションと正解Wikipediaリンクの距離に関する統計情報のファイル          |              |
| nil_all_freq_min/-n_af_min            | minimum freq of category-attribute to consider category-attribute-mention link probability in the link prob file (f_link_prob). (0.1-1.0)' |  |

- **link_prob.py(lp)** 
   - メンションとページのリンク確率をサンプルデータ正解の統計情報から推定。

| option  | 説明   |
|---------|------|
|lp_min/l_min|カテゴリ-属性-メンションの組に対してリンク確率情報ファイルに記載するリンク確率の最小値|
|f_link_prob|リンク確率情報ファイルのファイル名|

#### フィルタリング 
- **attr_range_filtering.py(ar)** (メンション(属性値)のクラスによるフィルタリング)
- | option  | 説明   |
|---------|------|
|attr_rng_auto_freq_min', '-af_min', type=click.INT,
              attr_rng_auto_freq_min_default
              |maximum number of range frequencies in the training data')
|attr_rng_tgt', '-ar_tgt', 
              attr_rng_tgt_default
              |target module of attribute range filtering, specified as the combination of '
                   'the following characters'
                   'm: mint, t: tinm, w: wlink, s: slink, l: link_prob, n: N/A')
|f_attr_rng_auto', 
              f_attr_rng_auto_default
              |filename of attribute range definition file (auto). The ranges are generated based on statistics of'
                   'sample data.')
|f_attr_rng_man', 
              f_attr_rng_man_default
              |filename of attribute range definition file (man). The ranges are manually specified using ENEIDs.')
|f_attr_rng_merged', 
              f_attr_rng_merged_default
              |filename of attribute range definition file (merged). ')
|f_enew_info', 
              f_enew_info_default
              |filename of enew_info_file.')
|attr_na_co', '-anc''attr_na_co (base score (0.1-1.0) for candidate pages which are not given ENEW')
|attr_ng_co', '-ang' attr_ng_co (base score (0.1-1.0) for candidate pages which do not match attribute range')
|attr_len', '-al',['a', 'r', 'ar', 'am', 'n']),
              attr_len_default
              |scoring of the ENEID of candidate page on attribute range (eg. matching ratio between ENEIDs of '
                   'candidate pages and that of gold pages),'
                   'n: raw matching ratio,'
                   'a: adjusted matching ratio (adjusted matching ratio to ignore 1st layer of the ENE hierarchy if '
                   'the ENEID begins with 1 (Name)), '
                   'r: raw matching ratio + raw depth (# of layers in the ENE hierarchy) of ENEID of the gold page'
                   '(specified in the attribute range definition file), '
                   'ar: adjusted matching ratio + adjusted depth (adjusted to ignore 1st layer of the ENE hierarchy'
                   'if the ENEID begins with 1 (Name)),'
                   'am: adjusted matching ratio + modified depth (modify the adjusted depth to diminish its influence)')
|attr_rng_type', '-art',['a', 'm', 'ma', 'am']),
              attr_rng_type_default
              |attribute range estimation type. m: use attribute range definition manually specified'
                   'a: use attribute range definition automatically generated based on sample data'
                   'ma: m + a (m > a) (m is preferred when conflict arises on the ratio),'
                   'am: a + m (a > m) (a is preferred when conflict arises on the ratio)')
- **incl_filtering.py(il)** (被リンク数によるフィルタリング)
| option  | 説明   |
|---------|------|
|incl_max', '-i_max', type=click.INT,
              incl_max_default
              |maximum number of filtering candidate pages using incoming links')
|incl_tgt', '-i_tgt', 
              incl_tgt_default
              |target module of incoming link filtering,'
                   'specified as the combination of the following characters'
                   'm: mint, t: tinm, w: wlink, s: slink, l: link_prob, n: N/A')
|incl_type', '-i_type',['o', 'f', 'a', 'n']),
              incl_type_default
              |type of incoming link filtering,'
                   'o: ordering by number of incoming links (reciprocal ranking), '
                   'f: filtering (keep the original values unchanged), '
                   'a: adjust value based on ordering by number of incoming links, '
                   'n: N/A')
- **back_link.py(bl)** (被リンクによるフィルタリング)
|back_link_tgt', '-bl_tgt', 
              back_link_tgt_default
              |target module of back link filtering,'
                   'specified as the combination of the following characters'
                   'm: mint, t: tinm, w: wlink, s: slink, l: link_prob, n: N/A')
|back_link_ng', '-bl_ng', type=click.FLOAT,
              back_link_ng_default
              |score for not back link')
- **detect_nil.py(dn)** (nil detection(リンクなしの判定) によるフィルタリング)
--nil_all_freq_min', '-n_af_min', type=click.FLOAT,
              nil_all_freq_min_default
              |minimum freq of category-attribute to consider category-attribute-mention link probability '
                   'in the link prob file (f_link_prob). (0.1-1.0)')
