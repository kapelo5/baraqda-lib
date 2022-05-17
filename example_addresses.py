from baraqdalib import Addresses

addr = Addresses()
for i in range(100):
    cities = addr.generate()
    print(cities)
cities = addr.generate(10)
print(cities)
sym = addr.get_sym_city('Mińsk Mazowiecki')
print(sym)
streets1 = addr.get_streets(sym)
print(streets1)
