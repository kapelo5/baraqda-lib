from baraqdalib.addresses import Addresses

addr = Addresses()
cities = addr.generate(10)
for i in cities:
    print(i)
    sym = addr.getSymCity(i)
    streets1 = addr.getStreets(sym)
    print(streets1)
