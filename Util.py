
import os
from string import punctuation
from collections import Counter

import datetime


def merge1(map1, map2):
    new_map1 = Counter(map1)
    new_map2 = Counter(map2)
    new_map1.update(new_map2)
    return new_map1


def cal_prob_sent(processed_classifier_obj, test_sent, total_files, final_merged_map):
    total_prob = 1.0
    words = test_sent.rstrip().lstrip().split()
    total_prob *= len(processed_classifier_obj.files)/total_files
    for word in words:
        top = processed_classifier_obj.words_map.get(word, 0) + 1
        bottom = processed_classifier_obj.total_words + len(final_merged_map)
        total_prob *= (top/bottom)
    return total_prob


def cal_prob_test_file(processed_class_obj, test_file, total_train_files, total_train_words):
    total_probability = 1.0
    words = remove_punctuations(make_words(return_lowered_lines(test_file)))
    total_probability *= processed_class_obj.total_files/total_train_files
    for word in words:
        top = processed_class_obj.words_map.get(word, 0) + 1
        bottom = processed_class_obj.total_words + total_train_words
        total_probability *= top/bottom
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


def remove_punctuations(words):
    new_words = list()
    for word in words:
        word = word.strip(punctuation)
        if len(word) != 0:
            new_words.append(word)
    return new_words


def make_lines_from_dir(file_dir):
    files = get_all_files_dir(file_dir)
    all_lines = list()
    for file in files:
        file_path = file_dir+file
        f = open(file_path)
        all_lines.extend(return_lowered_lines(file_path))
        f.close()
    return all_lines


def read_strip_split_map_file(file_path):
    file = open(file_path)
    lines = file.readlines()
    file_map = dict()
    for line in lines:
        splits = line.lower().rstrip().split()
        words = list(filter(None, splits))
        for word in words:
            try:
                file_map[word] += 1
            except KeyError:
                file_map[word] = 1
    return file_map


def read_strip_split_map_file_wo_pun(file_path):
    file = open(file_path)
    lines = file.readlines()
    file_map = dict()
    for line in lines:
        splits = line.lower().rstrip().split()
        words = list(filter(None, splits))
        for word in words:
            word = word.strip(punctuation)
            if len(word) != 0:
                try:
                    file_map[word] += 1
                except KeyError:
                    file_map[word] = 1
    file.close()
    return file_map


def read_strip_split_map_dir(directory):
    directory_map = dict()
    files = get_all_files_dir(directory)
    for file in files:
        file_map = read_strip_split_map_file(directory+file)
        directory_map.update(file_map)
    return directory_map


def read_strip_split_map_dir_wo_pun_dr1(directory):
    directory_map = dict()
    files = get_all_files_dir(directory)
    for file in files:
        file_map = read_strip_split_map_file_wo_pun(directory+file)
        directory_map = merge1(directory_map, file_map)
    return directory_map


def read_strip_split_map_dir_wo_pun(directory):
    files = get_all_files_dir(directory)
    lines = list()
    for file in files:
        lines.extend(return_lowered_lines(directory+file))
    words = make_words(lines)
    words = remove_punctuations(words)
    return make_map_words(words)


def lines_from_dir(directory, files=None):
    if files is None:
        files = get_all_files_dir(directory)
    lines = list()
    for file in files:
        lines.extend(return_lowered_lines(directory+file))
    return lines


def make_vector_file(file_path):
    lines = return_lowered_lines(file_path)
    words_map = read_strip_split_map_file_wo_pun(file_path)
    return lines, words_map


def merge(map1, map2):
    merged = dict(map1)
    for k in map2.keys():
        if k in merged.keys():
            nv = map2.get(k)
            ov = merged.get(k)
            merged[k] = nv + ov
        else:
            merged[k] = map2.get(k)
    return merged


def clear_file(file):
    open(file, "w").close()


def do_original(PreProcess):
    train_pos = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/train/pos/"
    train_neg = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/train/nrg/"

    test_pos = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/test/pos/"
    test_neg = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/test/nrg/"


def do_demo(PreProcess):
    action_train = os.getcwd()+"/small-corpus/train/action/"
    comedy_train = os.getcwd()+"/small-corpus/train/comedy/"

    action_test = os.getcwd()+"/small-corpus/test/action/"
    comedy_test = os.getcwd()+"/small-corpus/test/comedy/"

    action_comedy = os.getcwd()+"/output-demo/action/comedy.txt"
    comedy_action = os.getcwd()+"/output-demo/comedy/action.txt"

    a = datetime.datetime.now()

    clear_file(action_comedy)
    clear_file(comedy_action)

    processed_train_action = PreProcess(action_train)
    processed_train_comedy = PreProcess(comedy_train)
    merged = merge1(processed_train_action.words_map, processed_train_comedy.words_map)
    total_words = len(merged)
    total_files = processed_train_action.total_files+processed_train_comedy.total_files

    class_predictor_dir(processed_train_action, processed_train_comedy, action_test, total_files, total_words,
                        action_comedy)
    class_predictor_dir(processed_train_comedy, processed_train_action, comedy_test, total_files, total_words,
                        comedy_action)

    print("Out of all test-action -> ", processed_train_action.total_files, " : ",
          len(return_lowered_lines(action_comedy)), " are comedy")
    print("Out of all test-comedy -> ", processed_train_comedy.total_files, " : ",
          len(return_lowered_lines(comedy_action)), " are action")

    print(datetime.datetime.now()-a)
