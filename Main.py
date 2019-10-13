
from Util import return_lowered_lines
from Util import return_all_files
from Util import make_lines_from_dir
from Util import make_words
from Util import read_strip_split_map_file
from Util import read_strip_split_map_dir

from os import path

# 12,500 files
TRAIN_POS = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/train/pos/"
# 12, 500 files
TRAIN_NEG = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/train/neg/"
# 1 file, #89527 lines
VOCAB = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/imdb.vocab"

pos_dir_map = read_strip_split_map_dir(TRAIN_NEG)
print(len(pos_dir_map))
print(sum(pos_dir_map.values()))





