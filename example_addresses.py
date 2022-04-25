from baraqdalib.addresses import Addresses

addr = Addresses()
cities = addr.generate(100)
print(cities)
cities = addr.generate(10)
print(cities)
sym = addr.get_sym_city('Mińsk Mazowiecki')
print(sym)
streets1 = addr.get_streets(sym)
print(streets1)
