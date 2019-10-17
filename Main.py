
import os
from Classes import PreProcess
import datetime

from Util import *

action = os.getcwd()+"/small-corpus/train/action/"
comedy = os.getcwd()+"/small-corpus/train/comedy/"

TRAIN_POS = "/Users/Hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/train/pos/"
TRAIN_NEG = "/Users/Hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/train/neg/"

TEST_POS = "/Users/Hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/test/pos/"
TEST_NEG = "/Users/Hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/test/neg/"

test_file_path = os.getcwd()+"/small-corpus/test/test.txt"

a = datetime.datetime.now()

processed_train_action = PreProcess(action)
processed_train_comedy = PreProcess(comedy)
merged = merge1(processed_train_action.words_map, processed_train_comedy.words_map)
total_files = processed_train_action.total_files + processed_train_comedy.total_files
prob_action = cal_prob_test_file(processed_train_action, test_file_path, total_files, len(merged))
prob_comedy = cal_prob_test_file(processed_train_comedy, test_file_path, total_files, len(merged))
print("action" if prob_action > prob_comedy else "comedy")
print(datetime.datetime.now()-a)

