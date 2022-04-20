import random
import os
from typing import List, Dict


class Generator:
    def __init__(self) -> None:
        self._data: Dict[str, Dict[str, Dict[str, list]]] = dict(dict(dict()))

    def draw(self, lang: str, data_type: str, count: int = 1) -> List[str]:  # create table with weighted draw
        return random.choices(self._data[lang][data_type]['values'],
                              weights=self._data[lang][data_type]['weights'],
                              k=count)

    def search_files(self, path, sep, lang) -> None:
        for root, dirs, files in os.walk(path):  # walk and list files
            for file in files:
                # make keys in _data for files
                filename = file.split('.')[0]
                self._data[lang][filename] = {}  # create dict with key filename
                self.read_files(os.path.join(root, file), sep, lang, filename)

    def read_files(self, filepath, separator, lang, filename) -> None:
        # read files and store data from them
        file = open(filepath, 'r', encoding='utf-8')  # open file
        lines = file.readlines()  # read all lines
        file.close()  # close file
        # make temp list to store data from file
        values: List[str] = []
        weights: List[int] = []
        for line in lines[1::]:  # read line by line and prepare to saving in class variables start from 1
            line = line.strip('\n\r')
            temp_tab = line.split(separator)
            values.append(temp_tab[0])
            weights.append(int(temp_tab[1]))

        keys = lines[0].strip('\n\r').split(separator)  # read keys
        self._data[lang][filename][keys[0]] = values
        self._data[lang][filename][keys[1]] = weights

    def generate(self, lang: str, data_type: str, counter: int = 1, sep: str = ' ') -> List[str]:
        # check if key lang exist
        try:
            self._data[lang]
        except KeyError:
            path = os.path.join('baraqdalib', 'data', lang)  # create path to subdirectories
            self._data[lang] = {}
            self.search_files(path, sep, lang)  # search files in directory
        else:  # check if key data_type exist
            try:
                self._data[lang][data_type]
            except KeyError:
                path = os.path.join('baraqdalib', 'data', lang)  # create path to subdirectories
                self.search_files(path, sep, lang)  # search files in directory

        return self.draw(lang, 'male_names', counter)  # generate weighted dataw
