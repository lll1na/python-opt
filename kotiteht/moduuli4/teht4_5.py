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
