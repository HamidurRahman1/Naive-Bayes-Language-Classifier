
import os
from string import punctuation
from collections import Counter
import re
import math


def merge1(map1, map2):
    new_map1 = Counter(map1)
    new_map2 = Counter(map2)
    new_map1.update(new_map2)
    return new_map1


def cal_prob_test_file(processed_class_obj, test_file, total_train_files, total_train_words):
    words = punctuations_regex(make_words(return_lowered_lines(test_file)))
    print(words)
    total_probability = math.log(processed_class_obj.total_files/total_train_files, 2)
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


def lines_from_dir(directory, files=None):
    if files is None:
        files = get_all_files_dir(directory)
    lines = list()
    for file in files:
        lines.extend(return_lowered_lines(directory+file))
    return lines


def clear_file(file):
    open(file, "w").close()


def accuracy(total_mismatch, total_files):
    return 100-(total_mismatch/total_files)*100


def write_to_file_map(map):
    f = open("merged_map.txt", "w+")
    for k, v in map.items():
        f.write(str(k)+"\t"+str(v)+"\n")
    f.close()

