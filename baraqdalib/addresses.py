from baraqdalib import Generator
import os
import csv
import random


class Addresses:
    def __init__(self):
        self.address_generator = Generator()
        self.streets_file_name: str = 'streets.csv'
        self.cities_file_name: str = 'cities.csv'
        self.cities_pops_data: str = 'cities_pops'
        self.cities_pops_file_name: str = 'cities_pops.txt'
        self.lang = 'PL'
        self.sep: str = '\t'

    def generate(self, counter: int = 1):
        generated_cities = self.address_generator.generate(self.lang, self.cities_pops_data, counter, self.sep)
        return generated_cities

    def getPath(self, file_name):
        return os.path.join('baraqdalib', 'addressData', file_name)

    def getSymCity(self, city: str):
        # print(city)
        with open(os.path.join('baraqdalib', 'addressData', self.cities_file_name), 'r', encoding='utf-8-sig') as citiesFile:
            cities = csv.reader(citiesFile, delimiter=';')
            for sym in cities:
                if sym[1] == city:
                    return sym[0]
        return 'No city in file'

    def getStreets(self, city_sym: int):
        if city_sym != 'No city in file':
            streets = []
            streets_dump = []
            with open(os.path.join('baraqdalib', 'addressData', self.streets_file_name), 'r', encoding='utf-8-sig') as streetsFile:
                streets_csv = csv.reader(streetsFile)
                for row in streets_csv:
                    if row[4] == city_sym:
                        streets.append((row[6] + ' ' + row[8] + ' ' + row[7]).replace('  ', ' '))
                    elif row[4] != 'SYM':
                        if 287400 % int(row[4]):
                            streets_dump.append((row[6] + ' ' + row[8] + ' ' + row[7]).replace('  ', ' '))
                if not streets:
                    return random.choice(streets_dump), (round(random.lognormvariate(1.6, 2)) + 1) % 200
                return random.choice(streets), (round(random.lognormvariate(1.6, 2)) + 1) % 200
        else:
            return city_sym
