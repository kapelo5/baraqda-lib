from baraqdalib import Person
from baraqdalib import Generator
if __name__ == '__main__':
    test = Person()
    test.set('DE')
    # test = Generator()
    # test.generate('DE', 'eyes')
    # print(test.access_data('DE', 'eyes'))
    # print(test.get())
    i = 0
    while i <= 100:

        test.set('DE')
        print(test.get())
        i = i + 1