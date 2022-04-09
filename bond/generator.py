import random
from typing import List, Any
from bond.data import PL


class Generator:
    def __init__(self) -> None:
        self.weights: List[int] = []
        self._data: List[str] = []

    def set_item(self, k: List[int], v: List[str]) -> None:
        self.weights = k
        self._data = v

    def draw(self, count: int = 1) -> Any:
        return random.choices(self._data, weights=self.weights, k=count)


def generate(counter: int = 1, lang: str = 'PL') -> List[str]:
    gen = Generator()
    if lang == 'PL':  # Task: create request without checking if
        gen.set_item(list(PL.StoreData.first_name_male_weighs), sorted(list(PL.StoreData.first_name_male)))
    return gen.draw(counter)
