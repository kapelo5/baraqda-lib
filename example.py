from baraqdalib import Generator

if __name__ == '__main__':
    abba = Generator()
    print(abba.generate('PL', 'FemaleFirstName', 10, '\t'))  # generate data
    # print(abba.generate('PL', 'female_names', 100, '\t'))  # generate data
    # print(abba.generate('DE', 'female_names', 100))  # generate data
    # print(abba.draw('PL', 'female_names'))
    # print(abba.access_data('PL', 'male_names'))
    # print(abba.access_data('PL', 'female_names'))
    # print(abba.access_data('DE', 'male_names'))

