from baraqdalib import Addresses

addr = Addresses()
for i in range(15):
    data = addr.generate('PL')
    print(data)
