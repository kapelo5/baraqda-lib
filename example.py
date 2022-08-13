from baraqdalib import Generator
from baraqdalib import Cars
from baraqdalib import Addresses
from baraqdalib import Person


if __name__ == '__main__':
    # test Generator
    abba = Generator()
    print(abba.generate('PL', 'male_first_name', 100, sep='\t'))

    # test Cars
    car = Cars()
    print(car.generate(count=1))

    # test Person
    person = Person()
    person.set(lang='PL')
    print(person.get())

    person.set(lang='DE')
    print(person.get())



    # test Addresses
    adres = Addresses()
    print(adres.generate(lang='PL'))