
from Util import return_lowered_lines
from Util import return_all_files
from Util import make_lines_from_dir
from Util import make_words
import os

# 12,500 files
TRAIN_POS = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/train/pos/"
# 12, 500 files
TRAIN_NEG = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/train/neg/"
# 1 file, #89527 lines
VOCAB = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/imdb.vocab"

# vocabularies = return_lowered_lines(VOCAB)
#
# pos_train_files = return_all_files(TRAIN_POS)
#
# neg_train_files = return_all_files(TRAIN_NEG)


pos_train_all_lines = make_lines_from_dir(TRAIN_POS)
print(len(pos_train_all_lines))
words = make_words(pos_train_all_lines)
print(len(words))

neg_train_all_lines = make_lines_from_dir(TRAIN_NEG)
print(len(neg_train_all_lines))
words = make_words(neg_train_all_lines)
print(len(words))





