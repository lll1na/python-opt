luvut = []
luku = int(input("Anna luku: "))
while luku != "":
    luvut.append(int(luku))
    luku = input("Anna luku: ")
luvut.sort(reverse = True)
for luku in luvut[:5]:
  print(luku)
    

