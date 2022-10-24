# linkjpc2

目次:
- [はじめに](#はじめに)
  - [タスク](#タスク)
  - [特徴](#特徴)
- [モジュール](#モジュール)
- [エンティティリンキングを試してみる](#エンティティリンキングを試してみる)
- [前処理に関する注意](#前処理に関する注意)
- [今後の課題](#今後の課題)
- [参考情報](#参考情報)
  - [データファイル](#データファイル)
  - [コマンドラインオプション](#コマンドラインオプション)

## はじめに

**_linkjpc2_** は日本語Wikipediaを対象としたエンティティリンキングタスク([SHINRA2022 Linking task](http://2022.shinra-project.info/) )用のpythonスクリプトです。昨年の同タスクのシステム（**_linkjpc_**）を改良したものです。

### タスク

SHINRA2022 Linking taskはWikipedia記事中の、あるエンティティ(事物)を指すテキスト(メンション, 例: イタリア)を対応する記事ページ (例. [イタリア](https://ja.wikipedia.org/wiki/%E3%82%A4%E3%82%BF%E3%83%AA%E3%82%A2)) にリンクするタスクで、Wikification（Wikipediaを対象としたエンティティリンキング）の一種です。

このタスクでは、メンションは単なるテキストではなく、元記事の指す事物の属性情報の一部として与えられます。例えばイタリアの都市の「ヴェネツィア」ページの場合、記事中の「イタリア」というメンションは属性「国」の値として与えられます。

メンションは以下の (a) (c) の例のように別のページを指すことが多いですが、例えば「別名」のような特別の属性の場合には元記事を指す場合もあります。

例 |元記事 (エンティティ) | 属性名|メンション / 属性値 | リンク先のページ
:----------------|:------|:---------------|:---------|:----
(a) |[ヴェネツィア](https://ja.wikipedia.org/wiki/?curid=30053) | 国| イタリア |[イタリア](https://ja.wikipedia.org/wiki/%E3%82%A4%E3%82%BF%E3%83%AA%E3%82%A2) 
(b) |[ヴェネツィア](https://ja.wikipedia.org/wiki/%E3%83%B4%E3%82%A7%E3%83%8D%E3%83%84%E3%82%A3%E3%82%A2) | 別名 | アドリア海の女王 |[ヴェネツィア](https://ja.wikipedia.org/wiki/%E3%83%B4%E3%82%A7%E3%83%8D%E3%83%84%E3%82%A3%E3%82%A2)
(c) |[ヴェネツィア](https://ja.wikipedia.org/wiki/%E3%83%B4%E3%82%A7%E3%83%8D%E3%83%84%E3%82%A3%E3%82%A2) | 特産品 | ヴェネツィアン・グラス |[ヴェネツィアン・グラス](https://ja.wikipedia.org/wiki/%E3%83%B4%E3%82%A7%E3%83%8D%E3%83%84%E3%82%A3%E3%82%A2%E3%83%B3%E3%83%BB%E3%82%B0%E3%83%A9%E3%82%B9)


タスク関連のファイルは[森羅2022のホームページ](http://2022.shinra-project.info/)で配布されています。
ファイルの配置方法等の詳細はdata_info.md をご覧ください。


### 主な特徴 

***linkjpc2***の特徴は以下の通りです。

- 主要モジュールは組み合わせ可能です。文字列一致（メンションとタイトル）、Wikipediaの埋め込みリンクの探索、統計情報に基づく元記事へのリンク(再帰リンク)の推定、テキストからページへのリンク確率の推定を利用することができます。
- 各モジュールは最大4種類のフィルタリングと組み合わせ可能です。フィルタリングには属性の値として適切なクラス(属性のrange)判定、被リンク数、バックリンク、nil判定（リンク先なしの判定）があります。
- 前処理は重いです。

## モジュール
### エンティティリンキング
#### コア
- **linkjpc.py(ljc)**
#### 主要モジュール
- **matching.py(ma)** 
   - メンションと候補ページのタイトルの文字列マッチ。
- **self_link.py(sl)** (再帰リンクの推定)
   - 再帰リンクの推定 (メンションから元記事へのリンクをサンプルデータ正解の統計情報から推定。典型的には別名などの特別な属性の場合。）
- **get_wlink.py(gw)** 
   - メンションのリンク先を元記事の埋め込みリンクから探す。
- **link_prob.py(lp)** 
   - メンションとページのリンク確率をサンプルデータ正解の統計情報から推定。

#### フィルタリング 
- **attr_range_filtering.py(ar)** (メンション(属性値)のクラスによるフィルタリング)
- **incl_filtering.py(il)** (被リンク数によるフィルタリング)
- **back_link.py(bl)** (バックリンクによるフィルタリング)
- **detect_nil.py(dn)** (nil detection(リンクなしの判定) によるフィルタリング)

#### その他
- **config.py(cf)** (クラス定義等)
- **compile_list.py(cl)** (各主要モジュールのリンク先候補から最終候補リストを作成)
- **get_score.py(gs)** (最終候補リストのスコアリング)
- **ljc_common.py(lc)** (モジュール共通情報の辞書作成)

### 前処理
- **linkjpc_prep.py** (前処理)

-----------------

## エンティティリンキングを試してみる

1) スクリプトデータファイルをダウンロード 
   - エンティティリンキング (**_linkjpc_**)と前処理（**_linkjpc_prep_**: オプショナル）に必要なデータファイルのリストはdata_info.mdの[WHERE TO GET DATA]をご覧ください。 
   - 前処理（オプショナル）を試す場合は、以下の[前処理に関する注意](#前処理に関する注意) もご覧ください。

2) ファイルを配置
   - data_info.mdの[WHERE TO PUT DATA]で指定されたディレクトリに配置してください。

3) エンティティリンキングを実行  
   - 以下にエンティティリンキング (**_linkjpc2_**)の簡単な実行例を示します。
   
```

[実行例] メンションを同名のWikipediaページにリンクする (完全一致)

$ python ./linkjpc/linkjpc.py (common_data_dir) (tmp_data_dir) (in_dir) (out_dir) --mod m --mint e -f x

```
|モジュール                     |optionの組み合わせ例  |
|----|----|
|mint                         | --mod m --mint e -f x                                                             |
|tinm                       	|--mod t --tinm p -t_min 0.8 -f x|
|mint, tinm                   |--mod mt --mint p --tinm p -m_min 0.9 -t_min 0.8 -f x|
|wlink	                      |--mod w --wlink rp -f an -ar_tgt w -art ma -al r -n_tgt w -n_cond and_len_or_prob_desc -n_max 0.01 -n_af_min 7 -ld_min 12|
|slink                        |--mod s -s_min 0.5 -s_prb m_est -f x|
|link_prob                    |--mod l -l_min 0.5 -f x|
|slink, mint, wlink, link_prob|--mod s:m:lw -f abn --mint e -s_min 0.5 -s_prb m_est --wlink rp -ar_tgt w -art am -al am -bl_tgt w -l_min 0.6 -n_tgt w -n_cond two_of_prob_len_desc -n_max 0.01 -n_af_min 7 -ld_min 7|


## 注意

### 出力ディレクトリ

以下のいずれかまたはそのサブディレクトリに出力され、既存の同名ファイルを上書きします。
- common_data_dir
- tmp_data_dir
- in_dir 
- sample_gold_dir 
- sample_input_dir

WikipediaのダンプデータによるページID変更等、元データのバージョンによるID変更を解決したファイルはサブディレクトリ(conv)に作成します。

上書きを避けたい場合は、必ず元のファイルを別の場所に保存するか、コマンドラインオプションで別のディレクトリを指定してください。

### 前処理の実行順序

前処理( _**linkjpc_prep**_ )のオプションのうち、A, B, Cのグループに分類したものは、以下に示す順序で実行してください。 **_tests_** ディレクトリのスクリプト例
 ( _linkjpc_prep_all_test.sh_) を参考にしてください。
```

先に以下のダンプファイルを準備してから前処理を実行してください
- redirect dump
- page dump
- langlinks dump　

 (A)A-1) gen_change_wikipedia_info (CP2)
    A-2) conv_sample_json_pageid (SI1)(SP1)
    A-3) gen_target_attr (CP14)(CP15)
    A-4) gen_enew/gen_enew_rev_year (CP6)
 　　 -> A-5) gen_title2pid (CP19)
       -> A-6) gen_incoming_link (CP5)
          A-7) gen_redirect (CP3)(CP4)
          -> A-8) gen_title2pid_ext (CP17)
            -> A-9) gen_lang_link_info (CP16)
              -> A-10) pre_matching (*TP3*)(*TP4*)(*TP5*)(*TP6*)

            -> A-11) gen_back_link (*TP1*)(*TP2*)
               -> A-12) gen_sample_gold_tsv (*SP1*)
                  -> A-13) gen_link_prob (CP9)
                     A-14) gen_slink (CP7)
                     A-15) gen_linkable (CP10)
                     A-16) gen_attr_rng (CP13)(CP14)
                    
 (B) (after A-1 (gen_change_wikipedia_info)(CP2) is over)
     B-1) gen_common_html /gen_common_html_conv_year (CP1)
       -> (after A-12 (gen_sample_gold_tsv) is over)
          B-2) gen_link_dist (CP11)
     B-3) gen_html /gen_html_conv_year (*TP7*)
```

## 今後の課題

- Hyper parameter tuning
- データ更新
- 高速化
  




