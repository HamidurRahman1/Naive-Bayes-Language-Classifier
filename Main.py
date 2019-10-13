
from Util import return_lowered_lines
from Util import return_all_files

# 12,500 files
TRAIN_POS = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/train/pos/"
# 12, 500 files
TRAIN_NEG = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/train/neg/"
# 1 file, #89527 lines
VOCAB = "/Users/hamidurrahman/Downloads/CSCI381/hw2/movie-review-HW2/aclImdb/imdb.vocab"

vocabularies = return_lowered_lines(VOCAB)
print(len(vocabularies))

pos_train_files = return_all_files(TRAIN_POS)
print(len(pos_train_files))

neg_train_files = return_all_files(TRAIN_NEG)
print(len(neg_train_files))





