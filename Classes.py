
from Util import get_all_files_dir
from Util import remove_punctuations
from Util import make_words
from Util import lines_from_dir
from Util import make_map_words


class PreProcess:
    def __init__(self, directory):
        self.directory = directory
        self.files = get_all_files_dir(directory)
        self.words = remove_punctuations(make_words(lines_from_dir(self.directory, self.files)))
        self.words_map = make_map_words(self.words)
        self.total_keys = len(self.words_map)
        self.total_words = sum(self.words_map.values())
