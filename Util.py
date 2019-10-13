
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
    pass


def remove_punctuations(words):
    new_words = list()
    for w in words:
        w = w.strip(punctuation)
        if len(w) != 0:
            new_words.append(w)
    return new_words




