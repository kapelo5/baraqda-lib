from baraqdalib.addresses import Addresses

addr = Addresses()
cities = addr.generate(100)
for i in cities:
    print(i)
    sym = addr.getSymCity(i)
    streets1 = addr.getStreets(sym)
    print(streets1)

sym = addr.getSymCity('Mińsk Mazowiecki')
print(sym)
streets1 = addr.getStreets(sym)
print(streets1)
