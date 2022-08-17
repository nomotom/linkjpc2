#!/bin/sh -x
script="./linkjpc_all_sample.sh"
out_dir_base="/Users/masako/Documents/SHINRA/2021-LinkJP/test_out/20210929/"

if [  ' -mint' ${script}] ; then
  echo "-mint"
fi
#grep ' -tinm' ${script}
#grep 'incl' ${script} | grep -v '-i_tgt'
#grep 'attr' ${script} | grep -v '-ar_tgt'
#grep '__attr' ${script}
#grep 'imax' ${script}