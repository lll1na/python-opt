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
