

from Util import get_all_files_dir
from Util import read_strip_split_map_dir_wo_pun_dr1
from Util import make_words
from Util import make_map_words
from Util import remove_punctuations
from Util import lines_from_dir
from Util import separate_punctuations


class PreProcess:
    def __init__(self, directory):
        self.directory = directory
        self.files = get_all_files_dir(directory)
        # self.words_map = make_map_words(remove_punctuations(make_words(lines_from_dir(self.directory, self.files))))
        # self.words_map = read_strip_split_map_dir_wo_pun_dr1(self.directory)
        self.words_map = make_map_words(separate_punctuations(make_words(lines_from_dir(self.directory, self.files))))
        self.total_files = len(self.files)
        self.total_keys = len(self.words_map)
        self.total_words = sum(self.words_map.values())


