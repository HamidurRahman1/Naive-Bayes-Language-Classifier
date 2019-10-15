
from Util import *

import os

TRAIN_POS = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/train/pos/"
TRAIN_NEG = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/train/neg/"
VOCAB = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/imdb.vocab"

action = os.getcwd()+"/small_corpus/train/action/"
comedy = os.getcwd()+"/small_corpus/train/comedy/"

action_map = read_strip_split_map_dir_wo_pun(action)
print(action_map)
comedy_map = read_strip_split_map_dir_wo_pun(comedy)
print(comedy_map)
action_comedy_map = merge_maps(action_map, comedy_map)
print(action_comedy_map)


