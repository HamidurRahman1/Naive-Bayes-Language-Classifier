

#
# def get_all_files_dir(directory):
#     return os.listdir(directory)
#
#
# def make_words(lines):
#     pass
#     words = list()
#     for line in lines:
#         splits = line.split()
#         filtered = list(filter(None, splits))
#         words.extend(filtered)
#     return words
#
#
# def make_lines_from_dir(file_dir):
#     files = get_all_files_dir(file_dir)
#     all_lines = list()
#     for file in files:
#         file_path = file_dir+file
#         f = open(file_path)
#         all_lines.extend(return_lowered_lines(file_path))
#         f.close()
#     return all_lines
#
#
# def read_strip_split_map_dir_wo_pun_dr1(directory):
#     directory_map = dict()
#     files = get_all_files_dir(directory)
#     for file in files:
#         file_map = read_strip_split_map_file_wo_pun(directory+file)
#         directory_map = directory_map.update(file_map)
#         # print(merge_maps(directory_map, file_map))
#     return directory_map
#
#
# def read_strip_split_map_dir_wo_pun(directory):
#     files = get_all_files_dir(directory)
#     lines = list()
#     for file in files:
#         lines.extend(return_lowered_lines(directory+file))
#     words = make_words(lines)
#     words = remove_punctuations(words)
#     return make_map_words(words)
#
#
# def read_strip_split_map_file(file_path):
#     file = open(file_path)
#     lines = file.readlines()
#     file_map = dict()
#     for line in lines:
#         splits = line.lower().rstrip().split()
#         words = list(filter(None, splits))
#         for word in words:
#             try:
#                 file_map[word] += 1
#             except KeyError:
#                 file_map[word] = 1
#     return file_map
#
#
# def read_strip_split_map_dir(directory):
#     directory_map = dict()
#     files = return_all_files(directory)
#     for file in files:
#         file_map = read_strip_split_map_file(directory+file)
#         directory_map.update(file_map)
#     return directory_map
#
#
# def read_strip_split_map_file_wo_pun(file_path):
#     file = open(file_path)
#     lines = file.readlines()
#     file_map = dict()
#     for line in lines:
#         splits = line.lower().rstrip().split()
#         words = list(filter(None, splits))
#         for word in words:
#             word = word.strip(punctuation)
#             if len(word) != 0:
#                 try:
#                     file_map[word] += 1
#                 except KeyError:
#                     file_map[word] = 1
#     file.close()
#     return file_map
#
#
#
# def lines_from_dir(directory, files=None):
#     if files is None:
#         files = get_all_files_dir(directory)
#     lines = list()
#     for file in files:
#         lines.extend(return_lowered_lines(directory+file))
#     return lines
#
#
# def make_vector_file(file_path):
#     lines = return_lowered_lines(file_path)
#     words_map = read_strip_split_map_file_wo_pun(file_path)
#     return lines, words_map
#
#
# def read_strip_split_map_dir_wo_pun_dr1(directory):
#     directory_map = dict()
#     files = get_all_files_dir(directory)
#     for file in files:
#         file_map = read_strip_split_map_file_wo_pun(directory+file)
#         directory_map = directory_map.update(file_map)
#         # print(merge_maps(directory_map, file_map))
#     return directory_map
#
#
# def read_strip_split_map_dir_wo_pun(directory):
#     files = get_all_files_dir(directory)
#     lines = list()
#     for file in files:
#         lines.extend(return_lowered_lines(directory+file))
#     words = make_words(lines)
#     words = remove_punctuations(words)
#     return make_map_words(words)
#
#
# def lines_from_dir(directory, files=None):
#     if files is None:
#         files = get_all_files_dir(directory)
#     lines = list()
#     for file in files:
#         lines.extend(return_lowered_lines(directory+file))
#     return lines
#
#
# def make_vector_file(file_path):
#     lines = return_lowered_lines(file_path)
#     words_map = read_strip_split_map_file_wo_pun(file_path)
#     return lines, words_map
#
#
# def merge_maps(map1, map2):
#     return {**map1, **map2}
#

import os
from string import punctuation


def cal_prob_sent(processed_classifier_obj, test_sent, total_files, final_merged_map):
    total_prob = 1.0
    words = test_sent.rstrip().lstrip().split()
    total_prob *= len(processed_classifier_obj.files)/total_files
    for word in words:
        top = processed_classifier_obj.words_map.get(word, 0) + 1
        bottom = processed_classifier_obj.total_words + len(final_merged_map)
        total_prob *= (top/bottom)
    return total_prob


def return_lowered_lines(file_path):
    f = open(file_path)
    lines = f.readlines()
    new_lines = list()
    for line in lines:
        new_lines.append(line.rstrip().lower())
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
    for w in words:
        w = w.strip(punctuation)
        if len(w) != 0:
            new_words.append(w)
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
        directory_map = merge(directory_map, file_map)
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


def merge_maps(map1, map2):
    return {**map1, **map2}


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

