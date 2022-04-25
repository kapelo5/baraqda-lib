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
        self.address = {}
        self.sep: str = '\t'
        self._streets = []
        self._cities = []
        self._set_streets()
        self._set_cities()

    def _set_cities(self):   # Setting self.cities variable with list from set.cities_file_name
        with open(os.path.join('baraqdalib', 'addressData', self.cities_file_name), 'r', encoding='utf-8-sig') as citiesFile:
            cities = csv.reader(citiesFile, delimiter=';')
            for sym in cities:
                self._cities.append(sym)

    def _set_streets(self):  # Setting self.streets variable with list from sel.cities_file_name
        with open(os.path.join('baraqdalib', 'addressData', self.streets_file_name), 'r',
                  encoding='utf-8-sig') as streetsFile:
            streets_csv = csv.reader(streetsFile)
            for row in streets_csv:
                self._streets.append([row[4], (row[6] + ' ' + row[8] + ' ' + row[7]).replace('  ', ' ')])

    def generate(self, counter: int = 1):   # Generating from Generator class
        generated_cities = self.address_generator.generate(self.lang, self.cities_pops_data, counter, self.sep)
        for city, city_id in zip(generated_cities, range(len(generated_cities))):
            sym = self.get_sym_city(city)
            street = self.get_streets(sym)
            self.address.update({str(city_id): {'Street': street, 'City': city}})
        return self.address

    def get_path(self, file_name):   # Returning path /baraqdalib/addressData/
        return os.path.join('baraqdalib', 'addressData', file_name)

    def get_sym_city(self, city: str):    # Searching for city in cities and returning sym
        for sym in self._cities:
            if sym[1] == city:
                return sym[0]
        return 'No city in file'

    def get_streets(self, city_sym: int):    # Returning streets for city sym
        if city_sym != 'No city in file':   # If city_sym isn't set as a 'No city in file' generating address
            streets = []
            streets_dump = []
            for row in self._streets:   # Reading streets
                if row[0] == city_sym:      # Checking if city is in list
                    streets.append(row[1])
                elif row[0] != 'SYM' and row[0] != city_sym:    # Checking if city isn't in list and isn't header 'SYM'
                    if 287400 % int(row[0]):        # Decimation of list of streets from which we generate
                        streets_dump.append(row[1])
            if not streets:
                return random.choice(streets_dump) + ' ' + str((round(random.lognormvariate(1.6, 2)) + 1) % 200)    # Generating address if city isn't in file
            return random.choice(streets) + ' ' + str((round(random.lognormvariate(1.6, 2)) + 1) % 200)     # Generating address if city is in file
        else:
            return city_sym       # # If city_sym is set as a 'No city in file' returning this string
