import random
luku = random.randint(1, 10)
arvaus = int(input("Anna arvauksesi (1-10): "))
while arvaus != luku:
    if arvaus > luku:
        print("Arvauksesi on liian suuri.")
    else: 
        print("Arvauksesi on liian pieni.")
    arvaus = int(input("Anna arvauksesi (1-10): "))
print("Oikein!")