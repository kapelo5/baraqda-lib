from baraqdalib import Generator

if __name__ == '__main__':
    abba = Generator()

    print(abba.generate('PL', 'male_first_name', 100, sep = '\t'))
