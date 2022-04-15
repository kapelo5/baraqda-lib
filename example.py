from baraqdalib import Generator


if __name__ == '__main__':
    abba = Generator()
    print(abba.generate('PL', 100))  # generate data
    print(abba.stored_draw())  # return generated data from cache
