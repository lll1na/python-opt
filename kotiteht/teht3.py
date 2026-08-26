#1
luku = input("Kuhan pituuden senttimetreinä: ")
luku2 = 37 - int(luku)
if int(luku) < 37:
    print("Laske kuhan takaisin järveen!")
    print("Kuhan pituus on " + str(luku2) + " cm liian lyhyt.")
#2
luokka = input("Mikä on sun hyttiluokka: ")
if luokka == "LUX" or luokka == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif luokka == "A" or luokka == "a":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif luokka == "b" or luokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif luokka == "C" or luokka == "c":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")
#3
suk = input("Sinun sukupuoli: ")
hem = float(input("Sinun hemoglobiiniarvo: "))
if suk == "nainen" and  175 >= hem >= 117:
    print("hemoglobiiniarvo on normaali")
elif suk == "nainen" and hem >= 175:
    print("hemoglobiiniarvo on korkea")
elif suk == "nainen" and hem <= 117:
    print("hemoglobiiniarvo on alhainen")
elif suk == "mies" and  195 >= hem >= 134:
    print("hemoglobiiniarvo on normaali")
elif suk == "mies" and hem >= 195:
    print("hemoglobiiniarvo on korkea")
elif suk == "mies" and hem <= 134:
    print("hemoglobiiniarvo on alhainen")
#4
luku =int(input("Vuosiluku: "))
if luku % 400 == 0 :
    print("Se on karkausvuosi")
elif luku % 100 == 0:
    print("Se ei ole karkausvuosi")
elif luku % 4 == 0:
    print("Se on karkausvuosi")

else:
    print("Se ei ole karkausvuosi")
