import unittest
from collections import Counter
from numpy import cumsum
from baraqdalib import Generator

class MyTestCase(unittest.TestCase):
    def test_first_name(self):
        self.p = Generator()
        self.name = self.p.generate('PL', 1)
        assert name
        self.assertIsInstance(name, str)
        assert name in p._data

    def test_weighed_random(self):
        p = Generator()
        names = p.generate('PL', 1000)
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
