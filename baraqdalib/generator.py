import random
import os
from typing import List, Any


class Generator:
    def __init__(self) -> None:
        self.weights: List[int] = []
        self._data: List[str] = []
        self._draw: List[List[str]] = []  # cache for results

    def draw(self, count: int = 1) -> Any:
        self._draw.append(random.choices(self._data, weights=self.weights, k=count))

    def generate(self, lang: str = 'PL', counter: int = 1) -> Any:
        path = os.path.join('baraqdalib', 'data', lang)  # create path to subdir
        filelist = []  # list where we store paths to files

        for root, dirs, files in os.walk(path):  # walk and list files
            for file in files:
                # append the file name to the list
                filelist.append(os.path.join(root, file))


        for filepath in filelist:  # read files and store data from them
            file = open(filepath, 'r', encoding='utf-8')
            lines = file.readlines()
            for line in lines:
                line = line.strip('\n\r')
                temp_tab = line.split(" ")
                self._data.append(temp_tab[0])
                self.weights.append(int(temp_tab[1]))
                self.draw(counter)



        return self._draw

    def stored_draw(self) -> list[list[str]]:
        return self._draw
