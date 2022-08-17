script="./linkjpc/linkjpc_prep.py"
base_dir="/Users/masako/Documents/SHINRA/2021-LinkJP/2021-LinkJP/"
base_data_dir="${base_dir}Download/"
common_data_dir="${base_data_dir}ljc_data/common/"
tmp_data_dir="${base_data_dir}ljc_data/test/"
in_dir="${base_data_dir}linkjp-eval-211027/ene_annotation/"
sample_gold_dir="${base_dir}Download/linkjp-sample-210428/link_annotation/"

python $script $common_data_dir $tmp_data_dir $in_dir $test_gold_dir --gen_test_gold_tsv
        linkedjson2tsv(sample_gold_dir, data_info_prep.title2pid_org_file, log_info)
