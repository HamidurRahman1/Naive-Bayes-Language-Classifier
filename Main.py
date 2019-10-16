
import os
from Classes import PreProcess

from Util import merge
from Util import cal_prob_sent
from Util import read_strip_split_map_dir_wo_pun_dr1

action = os.getcwd()+"/small-corpus/train/action/"
comedy = os.getcwd()+"/small-corpus/train/comedy/"

action_pre = PreProcess(action)
comedy_pre = PreProcess(comedy)
merged_map = merge(action_pre.words_map, comedy_pre.words_map)
print(action_pre.words_map)
print(comedy_pre.words_map)
print(merged_map)
print(cal_prob_sent(comedy_pre, "fast couple shoot fly", len(action_pre.files)+len(comedy_pre.files), merged_map))

ap = read_strip_split_map_dir_wo_pun_dr1(action)
cp = read_strip_split_map_dir_wo_pun_dr1(comedy)
m = merge(ap, cp)
print(ap)
print(cp)
print(m)
