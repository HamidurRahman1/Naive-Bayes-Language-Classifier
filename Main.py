
import os
from Classes import PreProcess

from Util import *

action = os.getcwd()+"/small-corpus/train/action/"
comedy = os.getcwd()+"/small-corpus/train/comedy/"

TRAIN_POS = "/Users/Hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/train/pos/"
TRAIN_NEG = "/Users/Hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/train/neg/"

TEST_POS = "/Users/Hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/test/pos/"
TEST_NEG = "/Users/Hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/test/neg/"

print(os.path.isdir(TRAIN_POS))

action_pre = PreProcess(action)
comedy_pre = PreProcess(comedy)
merged_map = merge(action_pre.words_map, comedy_pre.words_map)
print(merged_map)
print(merge1(action_pre.words_map, comedy_pre.words_map))
print(cal_prob_sent(comedy_pre, "fast couple shoot fly", len(action_pre.files)+len(comedy_pre.files), merged_map))