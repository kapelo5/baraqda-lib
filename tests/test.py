import unittest
from collections import Counter
from numpy import cumsum
# from baraqdalib import Generator
# from baraqda-lib.baraqdalib import Generator

class MyTestCase(unittest.TestCase):
    # def __init__(self):
    #     self.p = Generator()

    # def read_test_file(self):
    #     file = open('test_file.txt', 'r')
    #     lines =

        # wziąc  i wczytać tuataj testowy pliczek i potem na tych danych sprawdzać resztę funkjci
        # powołanie instancji klasy jezt bez sensu, precież ja chcę ttylko sprawdzić jak i czy funkcje w klasie są sprawne
        # czyli omijamy powołanie klasy i sprawdzamy tylko czy pojedynczaa funkcja działa
        # jeśli kazda funkcja podrzędna działą to główna też będzie działała
        # to nie działa tak jak bym myslał, potrzebuje obiektu jako self do przekaznia do funkcji, inaczej
        # przesuwa mi lang do self i wtedy nie działa mi stworzenie ścieżki


    def test_first_name(self):

        name = Generator.generate(Generator(),'PL', 1)
        print(name)
        assert name
        # self.assertIsInstance(name, str)
        # assert name in p._data

    def test_weighed_random(self):
        p = Generator()
        names = p.generate('PL', 1000)
        print(names)
        names_counts = Counter(names)
        names_count_az = {}
        for i in sorted(names_counts):
            names_count_az[i] = names_counts[i]
        names_counts_az_weighs = list(names_count_az.values())
        for i in range(len(names_counts_az_weighs)):
            names_counts_az_weighs[i] = float(int(names_counts_az_weighs[i])/1000)

        names_counts_az_weighs = cumsum(names_counts_az_weighs)

        for i in range(len(names_counts_az_weighs)):
            self.assertAlmostEqual(names_counts_az_weighs[i], p.weights[i], delta=0.05)


if __name__ == '__main__':
    unittest.main()
