import unittest
from collections import Counter
from bond.generator import generate
from bond.data import PL
from numpy import cumsum


class MyTestCase(unittest.TestCase):
    def test_first_name(self):
        name = generate(1, 'PL')[0]
        assert name
        self.assertIsInstance(name, str)
        assert name in PL.StoreData.first_name_male

    def test_weighed_random(self):
        names = generate(1000, 'PL')
        # print(names)
        names_counts = Counter(names)
        names_count_az = {}
        for i in sorted(names_counts):
            names_count_az[i] = names_counts[i]
        names_counts_az_weighs = list(names_count_az.values())
        for i in range(len(names_counts_az_weighs)):
            names_counts_az_weighs[i] = float(int(names_counts_az_weighs[i])/1000)

        names_counts_az_weighs = cumsum(names_counts_az_weighs)

        for i in range(len(names_counts_az_weighs)):
            self.assertAlmostEqual(names_counts_az_weighs[i], PL.StoreData.first_name_male_weighs[i], delta=0.05)


if __name__ == '__main__':
    unittest.main()
