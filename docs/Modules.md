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

|option| 説明                                          |
|----|---------------------------------------------|
|wlink/wl| Wikipediaリンクのスコアリング方法(どの環境に現れたタグに加点するか)     |
|f_html_info| htmlタグ情報ファイル                                |
|wf_score/wf| (wlink:f) メンション内の最初のWikipediaリンクに与えるスコア     |
|wr_score/wr| (wlink:r) メンション内の最右のWikipediaリンクに与えるスコア     |
|wp_score/wp| (wlink:p) ページ内で前出のメンションのWikipediaリンクに与えるスコア |
|wl_score_same/wls| (wlink:l)メンション周辺（同一行）にあるWikipediaリンクに与えるスコア |
|wl_score_backward/wlb| (wlink:l)メンション周辺（後の行）にあるWikipediaリンクに与えるスコア |
|wl_score_forward/wlf| (wlink:l)メンション周辺（前の行）にあるWikipediaリンクに与えるスコア |                       
|wl_break/no-wl_break| 候補のリンクが見つかったら探索をやめるかどうかのフラグ                 |
|wl_lines_backward_max| メンションから遡ってWikipediaリンクを探す行数の最大値             |
@click.option('--wl_lines_forward_max', '-wl_fmax', type=click.INT,
              default=cf.OptInfo.wl_lines_forward_max_default, show_default=True,
              help='maximum number of lines to forward-search wikipedia links in the page')
@click.option('--wl_lines_backward_ca', '-wl_bca', type=click.Choice(['f', 'r', 'fr',  'n']),
              default=cf.OptInfo.wl_lines_backward_ca_default, show_default=True,
              help='how to specify the maximum number to backward-search Wikipedia links for each category-attribute. '
                   'f: the number specified in f_wl_lines_backward_max_ca, r: the number estimated using the ratio '
                   'specified by wl_lines_backward_ca_ratio, fr: both f and r (f takes precedence), n: N/A')
@click.option('--wl_lines_forward_ca', '-wl_fca', type=click.Choice(['f', 'r', 'fr',  'n']),
              default=cf.OptInfo.wl_lines_forward_ca_default, show_default=True,
              help='how to specify the maximun number to forward-search Wikipedia links for each category-attribute. '
                   'f: the number specified in f_wl_lines_forward_max_ca, r: the number estimated using the ratio '
                   'specified by wl_lines_forward_ca_ratio, fr: both f and r (f takes precedence), n: N/A')
@click.option('--f_wl_lines_backward_ca', '-f_wl_bca', type=click.STRING,
              default=cf.DataInfo.f_wl_lines_backward_ca_default, show_default=True,
              help='the file to specify maximum number of line to backward-search Wikipedia links in the page for '
                   'each category-attribute pairs. Notice: The default file contains just one example.')
@click.option('--f_wl_lines_forward_ca', '-f_wl_fca', type=click.STRING,
              default=cf.DataInfo.f_wl_lines_forward_ca_default, show_default=True,
              help='the file to specify maximum number of line to forward-search Wikipedia links in the page for each '
                   'category-attribute pairs. Notice: The default file contains just one example.')
@click.option('--wl_lines_backward_ca_ratio', '-wl_bca_ratio', type=click.FLOAT,
              default=cf.OptInfo.wl_lines_backward_ca_ratio_default, show_default=True,
              help='maximum ratio of lines to backward-search wikipedia links in the page; the number of candidate'
                   'lines are estimated for each attribute using the sample data')
@click.option('--wl_lines_forward_ca_ratio', '-wl_fca_ratio', type=click.FLOAT,
              default=cf.OptInfo.wl_lines_forward_ca_ratio_default, show_default=True,
              help='maximum ratio of lines to forward-search wikipedia links in the page; the number of candidate'
                   'lines are estimated for each attribute using the sample data')
@click.option('--f_mention_gold_link_dist_info', default=cf.DataInfo.f_mention_gold_link_dist_info_default,
              show_default=True, type=click.STRING, help='f_mention_gold_link_dist_info')
- **link_prob.py(lp)** 
   - メンションとページのリンク確率をサンプルデータ正解の統計情報から推定。

@click.option('--nil_all_freq_min', '-n_af_min', type=click.FLOAT,
              default=cf.OptInfo.nil_all_freq_min_default, show_default=True,
              help='minimum freq of category-attribute to consider category-attribute-mention link probability '
                   'in the link prob file (f_link_prob). (0.1-1.0)')
@click.option('--lp_min', '-l_min', type=click.FLOAT,
              default=cf.OptInfo.lp_min_default, show_default=True,
              help='minimum category-attribute-mention link probability in the link prob file (f_link_prob). (0.1-1.0)')
@click.option('--f_link_prob', type=click.STRING,
              default=cf.DataInfo.f_link_prob_default, show_default=True,
              help='filename of link probability info file')
#### フィルタリング 
- **attr_range_filtering.py(ar)** (メンション(属性値)のクラスによるフィルタリング)
- **incl_filtering.py(il)** (被リンク数によるフィルタリング)
- **back_link.py(bl)** (被リンクによるフィルタリング)
- **detect_nil.py(dn)** (nil detection(リンクなしの判定) によるフィルタリング)
