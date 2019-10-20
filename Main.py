
from Util import *
import datetime
from Classes import PreProcess

print("PROGRAM STARTED")
train_pos = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/train/pos/"
train_neg = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/train/neg/"

test_pos = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/test/pos/"
test_neg = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/test/neg/"

pos_neg = os.getcwd()+"/output/pos/neg.txt"
neg_pos = os.getcwd()+"/output/neg/pos.txt"

a = datetime.datetime.now()

clear_file(pos_neg)
clear_file(neg_pos)

processed_train_pos = PreProcess(train_pos)
processed_train_neg = PreProcess(train_neg)
merged = merge1(processed_train_pos.words_map, processed_train_neg.words_map)
total_words = len(merged)
print(total_words)
print(sum(merged.values()))

write_to_file_map(merged)

print("time taken to train the model", datetime.datetime.now()-a)

total_files = processed_train_pos.total_files + processed_train_neg.total_files

class_predictor_dir(processed_train_pos, processed_train_neg, test_pos, total_files, total_words, pos_neg)
class_predictor_dir(processed_train_neg, processed_train_pos, test_neg, total_files, total_words, neg_pos)

pos_in_neg = len(return_lowered_lines(neg_pos))
neg_in_pos = len(return_lowered_lines(pos_neg))
print("Out of all test-pos -> ", processed_train_pos.total_files, " : ", neg_in_pos, " are neg")
print("Out of all test-neg -> ", processed_train_neg.total_files, " : ", pos_in_neg, " are pos")

print("given all test-pos files, my model predicted that it is : ",
      accuracy(neg_in_pos, processed_train_pos.total_files), "% accurate")

print("given all test-neg files, my model predicted that it is : ",
      accuracy(pos_in_neg, processed_train_neg.total_files), "% accurate")

print(datetime.datetime.now()-a)
print("PROGRAM FINISHED")
