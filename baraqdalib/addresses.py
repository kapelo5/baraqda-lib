from baraqdalib import Generator
import os
import json
import csv
import random


class Addresses:
    def __init__(self):
        self.address_generator = Generator()
        self.streets_file_name: str = 'streets.csv'
        self.cities_file_name: str = 'cities.json'
        self.cities_pops_data: str = 'cities_pops'
        self.cities_pops_file_name: str = 'cities_pops.txt'
        self.lang = 'PL'
        self.sep: str = '\t'

    def generate(self, counter: int = 1):
        generated_cities = self.address_generator.generate(self.lang, self.cities_pops_data, counter, self.sep)
        return generated_cities

    def getPath(self, file_name):
        return os.path.join('baraqdalib', 'addressData', file_name)

    def getSymCity(self, city):
        with open(self.getPath(self.cities_file_name), 'r', encoding='utf-8-sig') as citiesFile:
            cities = json.load(citiesFile)
            for sym in cities:
                if cities[sym]['NAZWA'] == city:
                    return cities[sym]['SYM']
        return 'No city in file'

    def getStreets(self, city_sym):
        streets = []
        streets_dump = []
        with open(self.getPath(self.streets_file_name), 'r', encoding='utf-8-sig') as streetsFile:
            streets_csv = csv.reader(streetsFile)
            for row in streets_csv:
                if row[4] == city_sym:
                    streets.append((row[6] + ' ' + row[8] + ' ' + row[7]).replace('  ', ' '))
                else:
                    streets_dump.append((row[6] + ' ' + row[8] + ' ' + row[7]).replace('  ', ' '))
            if not streets:
                return random.choice(streets_dump)
            return random.choice(streets)
