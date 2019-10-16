
import os
from Classes import PreProcess

from Util import merge_maps
from Util import merge
from Util import cal_prob_sent

action = os.getcwd()+"/small-corpus/train/action/"
comedy = os.getcwd()+"/small-corpus/train/comedy/"

action_pre = PreProcess(action)
comedy_pre = PreProcess(comedy)
merged_map = merge(action_pre.words_map, comedy_pre.words_map)
print(action_pre.words_map)
print(comedy_pre.words_map)
print(merged_map)
print(cal_prob_sent(action_pre, "fast couple shoot fly", len(action_pre.files)+len(comedy_pre.files), merged_map))

