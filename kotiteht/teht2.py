#1
nimi = input("Anna nimesi: ")
print("Terve " + nimi + "!")

#2
pintaAla = int(input("Mikä on ympyrän säteen: "))
print("Pinta-ala on: " + str(3.14 * int(pintaAla) * int(pintaAla)))

#3
kanta = int(input("Mikä on suorakulmion kanta: "))
korkeus = int(input("Mikä on suorakulmion korkeus: "))
print(f"Suorakulmion piiri on: {2 * kanta + 2 * korkeus}")
print("Suorakulmion pinta-ala on: " + str(int(kanta) * int(korkeus)))

#4
eka = int(input("Anna ensimmäinen luku: "))
toka = int(input("Anna toinen luku: "))
kolmas = int(input("Anna kolmas luku: "))
summa = int(eka + toka + kolmas)
print("Lukujen summa on: " + str(summa))
tulo = int(eka * toka * kolmas)
print("Lukujen tuolos on: " + str(tulo))
kesk = float((eka + toka + kolmas)/3)
print(f"Lukujen keskiarvo on: {kesk}")

#5
lev = int(input("Anna leiviskät: "))
naula = int(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))
luku1 = lev * 20 * 32 * 13.3
luku2 = naula * 32 * 13.3
luku3 = luoti * 13.3
grammat = luku1 + luku2 + luku3
kilot = int(grammat // 1000)
grammat2 = grammat % 1000
print(f"Massa nykymitojen mukaan on: {kilot} kg ja {grammat2:.2f} g")

#6
import random 
print("Kolmenumeroisen koodi: " + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)))
print("Neljännumeroisen koodi: " + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)))