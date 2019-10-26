
import math
from pre_process import PreProcess
from pre_process import merge1
from pre_process import punctuations_regex
from pre_process import make_words
from pre_process import return_lowered_lines
from pre_process import get_all_files_dir
from pre_process import clear_file


def cal_prob_test_file(processed_class_obj, test_file, total_train_files, total_train_words):
    words = punctuations_regex(make_words(return_lowered_lines(test_file)))
    total_probability = math.log((processed_class_obj.total_files/total_train_files), 2)
    for word in words:
        top = processed_class_obj.words_map.get(word, 0) + 1
        bottom = processed_class_obj.total_words + total_train_words
        total_probability += math.log((top/bottom), 2)
    return total_probability


def class_predictor_dir(class1_obj, class2_obj, directory, total_train_files, total_train_words, file_to_write):
    files = get_all_files_dir(directory)
    for file in files:
        class_predictor_file(class1_obj, class2_obj, directory+file,
                             total_train_files, total_train_words, file_to_write)


def class_predictor_file(class1_obj, class2_obj, test_file, total_train_files, total_train_words, file_to_write):
    class1_probability = cal_prob_test_file(class1_obj, test_file, total_train_files, total_train_words)
    class2_probability = cal_prob_test_file(class2_obj, test_file, total_train_files, total_train_words)
    if class2_probability > class1_probability:
        file_obj = open(file_to_write, "a")
        file_obj.write(str(1) + "\n")
        file_obj.close()


def accuracy(total_mismatch, files):
    return 100-(total_mismatch/files)*100


POS = "/pos/"
NEG = "/neg/"

TRAIN = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/train"
TEST = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/test"

TRAIN_POS = TRAIN+POS
TRAIN_NEG = TRAIN+NEG

TEST_POS = TEST+POS
TEST_NEG = TEST+NEG

processed_train_pos = PreProcess(TRAIN_POS)
processed_train_neg = PreProcess(TRAIN_NEG)
merged = merge1(processed_train_pos.words_map, processed_train_neg.words_map)
total_train_len = len(merged)
print(total_train_len)
print(sum(merged.values()))

pos_neg_file = "pos_neg_file.txt"
neg_pos_file = "neg_pos_file.txt"

clear_file(pos_neg_file)
clear_file(neg_pos_file)

total_files = processed_train_pos.total_files + processed_train_neg.total_files
class_predictor_dir(processed_train_pos, processed_train_neg, TEST_POS, total_files, total_train_len, pos_neg_file)
class_predictor_dir(processed_train_neg, processed_train_pos, TEST_NEG, total_files, total_train_len, neg_pos_file)

pos_in_neg = len(return_lowered_lines(neg_pos_file))
neg_in_pos = len(return_lowered_lines(pos_neg_file))
print("Out of all test-pos -> ", processed_train_pos.total_files, " :", neg_in_pos, "are neg")
print("Out of all test-neg -> ", processed_train_neg.total_files, " :", pos_in_neg, "are pos")

print("given all test-pos files, my model predicted that it is :",
      accuracy(neg_in_pos, processed_train_pos.total_files), "% accurate")

print("given all test-neg files, my model predicted that it is :",
      accuracy(pos_in_neg, processed_train_neg.total_files), "% accurate")
