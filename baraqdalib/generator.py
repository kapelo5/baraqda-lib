import random
import os
from typing import List


class Generator:
    def __init__(self) -> None:
        self.weights: List[List[int]] = []
        self._data: List[List[str]] = []
        self._draw: List[List[str]] = []  # cache for results
        self.filelist: List[str] = []

    def draw(self, count: int = 1) -> None:  # create table with weighted draw and save to cache
        for i in range(len(self._data)):
            self._draw.append(random.choices(self._data[i], weights=self.weights[i], k=count))

    def search_files(self, path) -> None:
        for root, dirs, files in os.walk(path):  # walk and list files
            for file in files:
                # append the file name to the list
                self.filelist.append(os.path.join(root, file))

    def read_files(self) -> None:
        for filepath in self.filelist:  # read files and store data from them
            file = open(filepath, 'r', encoding='utf-8')  # open file
            lines = file.readlines()
            readed_data: List[str] = []
            readed_weights: List[int] = []
            file.close()  # close file
            for line in lines:  # read line by line and prepare to saving in class objects
                line = line.strip('\n\r')
                temp_tab = line.split(" ")
                readed_data.append(temp_tab[0])
                readed_weights.append(int(temp_tab[1]))

            self._data.append(readed_data)
            self.weights.append(readed_weights)


    def generate(self, lang: str = 'PL', counter: int = 1) -> List[List[str]]:
        path = os.path.join('baraqdalib', 'data', lang)  # create path to subdirectories
        self.search_files(path)  # search files in directory
        self.read_files()   # read files
        self.draw(counter)  # generate weighted dataw
        return self._draw

    def stored_draw(self) -> List[List[str]]:  # return stored generated data
        return self._draw
