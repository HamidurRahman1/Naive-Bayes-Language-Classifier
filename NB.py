
import os
import math

from Pre_Process import punctuations_regex
from Pre_Process import make_words
from Pre_Process import return_lowered_lines
from Pre_Process import get_all_files_dir
from Pre_Process import merge
from Pre_Process import create_out_file

from Pre_Process import TRAIN_POS_OUT_FILE
from Pre_Process import TRAIN_NEG_OUT_FILE

ROOT = os.getcwd()+"/movie-review-HW2/aclImdb/"
TEST_POS = ROOT+"/test/pos/"
TEST_NEG = ROOT+"/test/neg/"
MOVIE_OUTPUT_PREDICTION = "MOVIE-OUTPUT-PREDICTION.txt"
MOVIE_OUTPUT_FET_PARAM = "movie-review-BOW.NB"
TRAIN_POS_FILE = TRAIN_POS_OUT_FILE
TRAIN_NEG_FILE = TRAIN_NEG_OUT_FILE
POS_IND = "+"
NEG_IND = "-"
TEST_POS_FILES = 60
TEST_NEG_FILES = 60
TOTAL_FILES = TEST_POS_FILES+TEST_NEG_FILES


def read_words_make_map(file_path):
    file = open(file_path)
    line = file.readline().rstrip()
    words = line.split()
    word_map = dict()
    for word in words:
        try:
            word_map[word] += 1
        except KeyError:
            word_map[word] = 1
    return word_map


def cal_prob_test_file(class_map, total_words, test_file, total_train_words, IND, FEAT):
    words = punctuations_regex(make_words(return_lowered_lines(test_file)))
    total_probability = math.log((TEST_POS_FILES/TOTAL_FILES), 2)
    for word in words:
        top = class_map.get(word, 0) + 1
        bottom = total_words + total_train_words
        total_probability += math.log((top/bottom), 2)
        FEAT.write("P( "+word+" | "+IND+" ) = " + str(top/bottom) + "\n")
    return total_probability


def class_predictor_file(map1, map1_words, map2, map2_words, directory,
                         test_file, total_train_words, IND1, IND2, OUT, FEAT):
    class1_probability = cal_prob_test_file(map1, map1_words, directory+test_file, total_train_words, IND1, FEAT)
    class2_probability = cal_prob_test_file(map2, map2_words, directory+test_file, total_train_words, IND2, FEAT)
    if class2_probability > class1_probability:
        OUT.write(test_file + ", " + IND2 + ", " + IND1 + "\n")
        return 1
    else:
        OUT.write(test_file + ", " + IND1 + ", " + IND2 + "\n")
        return 0


def class_predictor_dir(map1, map2, directory, total_train_words, ind1, ind2, out, feat):
    files = get_all_files_dir(directory)
    map1_words = sum(map1.values())
    map2_words = sum(map2.values())
    counter = 0
    for file in files:
        counter += class_predictor_file(map1, map1_words, map2, map2_words,
                                        directory, file, total_train_words, ind1, ind2, out, feat)
    return counter


def accuracy(total_mismatch, files):
    return 100-(total_mismatch/files)*100


def run_movie_class_predictor():
    print("PROGRAM STARTED")

    train_pos_map = read_words_make_map(TRAIN_POS_FILE)
    train_neg_map = read_words_make_map(TRAIN_NEG_FILE)
    merged_map = merge(train_pos_map, train_neg_map)
    total_train_keys = len(merged_map)

    create_out_file(MOVIE_OUTPUT_PREDICTION)
    create_out_file(MOVIE_OUTPUT_FET_PARAM)

    print("2 FILES WILL BE CREATED WHERE OUTPUT WILL BE SAVED - \n1. "
          ""+MOVIE_OUTPUT_PREDICTION+" 2."+MOVIE_OUTPUT_FET_PARAM)

    OUT_PRED = open(MOVIE_OUTPUT_PREDICTION, "a")
    OUT_FEAT_PARAM = open(MOVIE_OUTPUT_FET_PARAM, "a")

    OUT_PRED.write("file, my-prediction, label"+"\n")

    pos_neg = class_predictor_dir(train_pos_map, train_neg_map, TEST_POS, total_train_keys, POS_IND, NEG_IND,
                                  OUT_PRED, OUT_FEAT_PARAM)
    neg_pos = class_predictor_dir(train_neg_map, train_pos_map, TEST_NEG, total_train_keys, NEG_IND, POS_IND,
                                  OUT_PRED, OUT_FEAT_PARAM)

    pos_accuracy = accuracy(pos_neg, TEST_POS_FILES)
    neg_accuracy = accuracy(neg_pos, TEST_NEG_FILES)
    OUT_PRED.write("Overall accuracy: "+str((pos_accuracy+neg_accuracy)/2))
    OUT_PRED.close()
    OUT_FEAT_PARAM.close()
    print("PROGRAM FINISHED")


run_movie_class_predictor()

