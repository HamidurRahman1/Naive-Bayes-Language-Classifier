
import os
from Classes import PreProcess

from Util import merge_maps
from Util import cal_prob_sent

action = os.getcwd()+"/small-corpus/train/action/"
comedy = os.getcwd()+"/small-corpus/train/comedy/"

action_pre = PreProcess(action)
comedy_pre = PreProcess(comedy)
merged_map = merge_maps(action_pre.words_map, comedy_pre.words_map)
print(cal_prob_sent(action_pre, "fast couple shoot fly", len(action_pre.files)+len(comedy_pre.files), merged_map))