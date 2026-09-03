luku = 1
while luku <= 1000:
    if luku % 3 == 0:
        print(luku)
    luku += 1

#2
tuuma = float(2.54)
luku = float(input("Anna tuuma: "))
while luku > 0:
    print(luku * tuuma)
    luku = float(input("Anna tuuma: "))

#3
pienin = None
suurin = None

while True:
    luku = input("Anna luku: ")
    if luku == "":
       break

    luku = float(luku)

    if pienin is None or luku < pienin:
       pienin = luku
    if suurin is None or suurin < luku:
       suurin = luku

print(f"Pienimpi luku on {pienin} ja suurin luku on {suurin}")

#4
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

#5
tunus = "python"
salasana = "rules"
kerta = 0
while kerta <=5:
    tunus2 = input("Anna tunnus: ")
    salasana2 = input("Anna salasana: ")

    kerta += 1
    if tunus2 == tunus and salasana2 == salasana:
        print("Tervetuloa!")
        break

    if kerta > 5:
        print("Pääsy evätty")
        break

