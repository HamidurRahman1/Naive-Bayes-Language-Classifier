

from string import punctuation
from collections import Counter
import os
import re

ROOT = os.getcwd()+"/movie-review-HW2/aclImdb/"
TRAIN_POS = ROOT+"train/pos/"
TRAIN_NEG = ROOT+"train/neg/"
TRAIN_POS_OUT = "TRAIN_POS.txt"
TRAIN_NEG_OUT = "TRAIN_NEG.txt"


class PreProcess:
    def __init__(self, directory):
        self.directory = directory
        self.files = get_all_files_dir(directory)
        self.words = punctuations_regex(make_words(lines_from_dir(self.directory, self.files)))


def merge(map1, map2):
    new_map1 = Counter(map1)
    new_map2 = Counter(map2)
    new_map1.update(new_map2)
    return new_map1


def lines_from_dir(directory, files=None):
    if files is None:
        files = get_all_files_dir(directory)
    lines = list()
    for file in files:
        lines.extend(return_lowered_lines(directory+file))
    return lines


def return_lowered_lines(file_path):
    f = open(file_path)
    lines = f.readlines()
    new_lines = list()
    for line in lines:
        new_lines.append(line.rstrip().lower())
    f.close()
    return new_lines


def get_all_files_dir(directory):
    return os.listdir(directory)


def make_words(lines):
    words = list()
    for line in lines:
        splits = line.split()
        filtered = list(filter(None, splits))
        words.extend(filtered)
    return words


def make_map_words(words):
    words_map = dict()
    for word in words:
        try:
            words_map[word] += 1
        except KeyError:
            words_map[word] = 1
    return words_map


def punctuations_regex(words):
    new_words = list()
    for word in words:
        lst = do_regex(word)
        filtered = list(filter(None, lst))
        new_words.extend(filtered)
    return new_words


def do_regex(word):
    word = word.strip(punctuation)
    r2 = "-{2,}"
    r3 = "'{2,}"
    lw = list()
    if len(word) != 0:
        f1 = re.split(r'[`~!@#$%^&*()_+={}|\\/[:;",<>.\]?]\\*', word)
        for e in f1:
            l1 = list(re.split(r2, e))
            lw.extend(l1)
            l2 = list(re.split(r3, e))
            lw.extend(l2)
            lw.remove(e)
    return lw


def clear_file(file):
    open(file, "w").close()


def write_to_file(file_name, words):
    f = open(file_name, "a")
    for word in words:
        f.write(word+" ")
    f.close()


def create_train_out_file(file):
    open(file, "w+").close()


def run_pre_process():
    print("Pre-Process STARTED")

    preprocessed_train_pos = PreProcess(TRAIN_POS)
    preprocessed_train_neg = PreProcess(TRAIN_NEG)

    create_train_out_file(TRAIN_POS_OUT)
    create_train_out_file(TRAIN_NEG_OUT)

    print("2 FILES WILL BE CREATED WHERE OUTPUT WILL BE SAVED - \n1. "
          ""+TRAIN_POS_OUT + " 2." + TRAIN_NEG_OUT)

    write_to_file(TRAIN_POS_OUT, preprocessed_train_pos.words)
    write_to_file(TRAIN_NEG_OUT, preprocessed_train_neg.words)

    print("Pre-Process FINISHED")


run_pre_process()
