import random
import os
from typing import List, Dict


class Generator:
    def __init__(self) -> None:
        self._data: Dict[str, Dict[str, Dict[str, list]]] = dict(dict(dict()))  # create empty dict

    def draw(self, lang: str, data_type: str, count: int = 1, sep: str = ' ') -> List[str]:  # return table with weighted draw
        try:
            return random.choices(self._data[lang][data_type]['values'],
                                  weights=self._data[lang][data_type]['weights'],
                                  k=count)
        except KeyError:  # run normal generation when error occurred
            self.generate(lang, data_type, count, sep)

    def search_files(self, path, sep, lang) -> None:
        self._data[lang] = {}
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
        temp_list = []
        keys = lines[0].strip('\n\r').split(separator)  # read keys
        weights_index = keys.index('weights')  # return index where weights are stored
        for i in range(len(keys)):  # create lists to store values
            temp_list.append([])
        for line in lines[1::]:  # read line by line and prepare to saving in class variables, start from 1
            line = line.strip('\n\r')
            temp_tab = line.split(separator)
            temp_tab[weights_index] = int(temp_tab[weights_index])
            for t, item in zip(temp_tab, temp_list):
                item.append(t)

        for k, v in zip(keys, temp_list):
            self._data[lang][filename][k] = v

    def generate(self, lang: str, data_type: str, counter: int = 1, sep: str = ' ') -> List[str]:
        # check if key lang exist
        try:
            self._data[lang]
        except KeyError:
            path = os.path.join('baraqdalib', 'data', lang)  # create path to subdirectories
            self.search_files(path, sep, lang)  # search files in directory
            try:  # check if key lang exist after search for directory
                self._data[lang]
            except KeyError:
                print(f'Data not provided for {lang}!')
                return []

        # check if key data_type exist
        try:
            self._data[lang][data_type]
        except KeyError:
            path = os.path.join('baraqdalib', 'data', lang)  # create path to subdirectories
            self.search_files(path, sep, lang)  # search files in directory
            try:  # check if key data_type exist after search and reading files
                self._data[lang][data_type]
            except KeyError:
                print(f'Data not provided for {lang}, {data_type}!')
                return []

        return self.draw(lang, data_type, counter, sep)  # generate weighted dataw

    def access_data(self, lang: str, data_type: str) -> Dict[str, list]:
        try:  # check if keys lang, data_type exists
            self._data[lang][data_type]
        except KeyError:
            print(f'No data for {lang}, {data_type}')
        else:
            return self._data[lang][data_type]
