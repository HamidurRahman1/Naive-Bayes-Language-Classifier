
from Util import merge_maps
from Util import cal_prob_sent
from Classes import PreProcess
import os

TRAIN_POS = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/train/pos/"
TRAIN_NEG = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/train/neg/"
VOCAB = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/imdb.vocab"

action = os.getcwd()+"/small_corpus/train/action/"
comedy = os.getcwd()+"/small_corpus/train/comedy/"

action_pre = PreProcess(action)
comedy_pre = PreProcess(comedy)
merged_map = merge_maps(action_pre.words_map, comedy_pre.words_map)
print(cal_prob_sent(action_pre, "fast couple shoot fly", len(action_pre.files)+len(comedy_pre.files), merged_map))
