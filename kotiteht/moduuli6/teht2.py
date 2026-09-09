import random

tahko = int(input("Anna nopan tahkojen yhteismäärän: "))

def arva(tahko):
    return random.randint(1,tahko)

luku = 0

while luku != tahko:
    luku = arva(tahko)
    print(luku)

