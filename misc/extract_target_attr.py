import json
import csv

# リンキングタスク対象のリスト
# 複数行と1行

# ENE definition json
in_file_dir = '/Users/masako/Documents/SHINRA/ENE/ENE_Definition/ENE_Definition_v9.0/'
in_file = in_file_dir + 'ene_definition_v9.0.0-with-attributes-and-shinra-tasks-20220714.jsonl'
out_file_dir = '/Users/masako/Documents/SHINRA/ENE/ENE_Definition/ENE_Definition_v9.0/'
out_file_multi = out_file_dir + 'ene_definition_v9.0.0-20220714_target_attr.tsv'
out_file_single = out_file_dir + 'ene_definition_v9.0.0-20220714_target_attr_list.tsv'
out_file_single_small = out_file_dir + 'ene_definition_v9.0.0-20220714_target_attr_slist.tsv'

# {"ENE_id": "1.4.4.1", "name": {"en": "Nationality", "ja": "国籍名"}, "definition": {"en": "A name of a nationality.", "ja": "人の国籍の名前。"}, "children_category": [], "parent_category": "1.4.4", "attributes": [{"name": "読み", "description": "ひらがなまたはカタカナ、発音記号(音声記号、ピンイン等）で書かれた読み。\n但し、見出し語と同じ表記の場合は記載しない。\n見出し語の一部の読み、省略されている部分を含む読みは抽出する。", "extraction_task": true, "linking_task": false}, {"name": "別名・旧称", "description": "正式名称、現地語名、旧称、英語名、愛称等を含む。\n", "extraction_task": true, "linking_task": true}, {"name": "国", "description": "見出し語が居住する国。", "extraction_task": true, "linking_task": true}, {"name": "大陸分布地域", "description": "見出し語が居住する大陸地域。\n国より大きな単位。", "extraction_task": true, "linking_task": true}, {"name": "居住地（地域）", "description": "見出し語が居住する地域、自治体。", "extraction_task": true, "linking_task": true}, {"name": "居住地（地形）", "description": "見出し語が居住する地形。\n島、半島、森等。", "extraction_task": true, "linking_task": true}, {"name": "取得
# の条件", "description": "見出し語の国籍の要件。", "extraction_task": true, "linking_task": true}, {"name": "民族（組織）", "description": "見出し語の民族。関連する民族含む。", "extraction_task": true, "linking_task": true}, {"name": "人口（民族）", "description": "最も新しい総人口。\n「約～」、「～人以上」等の曖昧表現がある場合は共に抽出。\n\n過去の複数年の記録がある場合は古い情報は抽出しない。\n見出し語より小さなエリアや性別に依存した記録は抽出しない
# 。\n見込みのデータは抽出しないが、推計人口は抽出する。", "extraction_task": true, "linking_task": false}, {"name": "使用している言語", "description": "見出し語が使用する言語。", "extraction_task": true, "linking_task": true}, {"name": "宗教・信仰", "description": "見出し語が信じる宗教、信仰。", "extraction_task": true, "linking_task": true}, {"name": "民族団体", "description": "見出し語が集う団体。", "extraction_task": true, "linking_task": true}]}
# {"ENE_id": "1.4.5", "name": {"en": "Sports_Organization", "ja": "競技組織名"}, "definition": {"en": "A name of an organization related to sports.", "ja": "スポーツ、競技に関する組織の名前。"}, "children_category": ["1.4.5.0", "1
# .4.5.1", "1.4.5.2", "1.4.5.3"], "parent_category": "1.4"}

print_list = []
attr_dict = {}
with open(in_file, 'r', encoding='utf-8') as i:
    for i_line in i:
        rec = json.loads(i_line)
        eneid = rec['ENE_id']
        ene_name_dic = rec['name']
        ene_name_ja = ene_name_dic['ja']
        ene_name_en = ene_name_dic['en']

        if 'attributes' in rec:
            attr_dict[ene_name_en] = []
            attributes_list = rec['attributes']
            for attr in attributes_list:
                attr_name = attr['name']
                target = attr['linking_task']
                if target == 1:

                    print_list.append([eneid, ene_name_ja, ene_name_en, attr_name])
                    attr_dict[ene_name_en].append(attr_name)

with open(out_file_multi, 'w', encoding='utf-8') as o:
    writer = csv.writer(o, delimiter='\t', lineterminator='\n')
    writer.writerows(print_list)

with open(out_file_single, 'w', encoding='utf-8') as s1, open(out_file_single_small, 'w', encoding='utf-8') as s2:
    writer1 = csv.writer(s1, delimiter='\t', lineterminator='\n')
    for k, v in attr_dict.items():
        writer1.writerow([k, v])
    writer2 = csv.writer(s2, delimiter='\t', lineterminator='\n')
    for k, v in attr_dict.items():
        k_small = k.lower()
        writer2.writerow([k_small, v])