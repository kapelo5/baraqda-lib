from baraqdalib import Generator
import os
import csv
import random
from typing import List, Dict


class Addresses:
    def __init__(self):
        self.address_generator = Generator()

        self.streets_file_name: str = 'streets.csv'
        self.cities_file_name: str = 'cities.csv'
        self.cities_pops_data: str = 'cities_pops'
        self.cities_pops_file_name: str = 'cities_pops.txt'

        self._postal_code: List[List[str, str]] = list(list())
        self._streets: List[List[str, str]] = list(list())
        self._cities: List[List[str, str]] = list(list())

        self.sep: str = '\t'

        self._set_streets()
        self._set_cities()
        self._set_codes()

    def _set_codes(self):   # Setting self._postal_code variable with list from 'postal_codes.csv'
        with open(os.path.join('baraqdalib', 'addressData', 'postal_codes.csv'), 'r', encoding='utf-8-sig') as codesFile:
            codes = csv.reader(codesFile, delimiter=';')
            for code in codes:
                self._postal_code.append([code[2], code[0]])

    def _set_cities(self):   # Setting self.cities variable with list from self.cities_file_name
        with open(os.path.join('baraqdalib', 'addressData', self.cities_file_name), 'r', encoding='utf-8-sig') as citiesFile:
            cities = csv.reader(citiesFile, delimiter=';')
            for sym in cities:
                self._cities.append(sym)

    def _set_streets(self):  # Setting self.streets variable with list from self.cities_file_name
        with open(os.path.join('baraqdalib', 'addressData', self.streets_file_name), 'r',
                  encoding='utf-8-sig') as streetsFile:
            streets_csv = csv.reader(streetsFile)
            for row in streets_csv:
                self._streets.append([row[4], (row[6] + ' ' + row[8] + ' ' + row[7]).replace('  ', ' ')])

    def generate(self, counter: int = 1, lang: str = 'PL'):   # Generating from Generator class
        generated_cities = self.address_generator.generate(lang, self.cities_pops_data, counter, self.sep)
        address: Dict[Dict[str, str]] = dict(dict())
        for city, address_id in zip(generated_cities, range(len(generated_cities))):
            sym = self.get_sym_city(city)
            street = self.get_streets(int(sym))
            postal_code = self.get_code(str(city))
            address.update({str(address_id): {'street': street, 'city': city, 'postal_code': postal_code}})
        return address

    def get_code(self, city: str):  # Searching for city in postal_codes returning it's value
        codes = list()
        for code in self._postal_code:
            if code[0] == city:
                codes.append(code[1])
        if codes:
            return random.choice(codes)
        return 'No city in file'

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
            return city_sym       # If city_sym is set as a 'No city in file' returning this string
