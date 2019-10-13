
import os
from string import punctuation


def return_lowered_lines(file_path):
    f = open(file_path)
    lines = f.readlines()
    new_lines = list()
    for line in lines:
        new_lines.append(line.rstrip().lower())
    return new_lines


def return_all_files(file_dir):
    return os.listdir(file_dir)


def make_words(lines):
    words = list()
    for line in lines:
        splits = line.split()
        filtered = list(filter(None, splits))
        words.extend(filtered)
    return words


def remove_punctuations(words):
    new_words = list()
    for w in words:
        w = w.strip(punctuation)
        if len(w) != 0:
            new_words.append(w)
    return new_words


def make_lines_from_dir(file_dir):
    files = return_all_files(file_dir)
    all_lines = list()
    for file in files:
        file_path = file_dir+file
        f = open(file_path)
        all_lines.extend(return_lowered_lines(file_path))
        f.close()
    return all_lines


