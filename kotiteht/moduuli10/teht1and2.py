class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros  

    def kerros_ylös(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
        print(f"Hissi on nyt kerroksessa {self.kerros}.")

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
        print(f"Hissi on nyt kerroksessa {self.kerros}.")

    def siirry_kerrokseen(self, kohde):
        if kohde < self.alin_kerros or kohde > self.ylin_kerros:
            print(f"Kerrosta {kohde} ei ole olemassa.")
            return
        while self.kerros < kohde:
            self.kerros_ylös()
        while self.kerros > kohde:
            self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumäärä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros)
                       for _ in range(hissien_lukumäärä)]

    def aja_hissiä(self, hissin_numero, kohdekerros):
        # hissit numeroidaan 1:stä alkaen
        if hissin_numero < 1 or hissin_numero > len(self.hissit):
            print(f"Hissiä numero {hissin_numero} ei ole olemassa.")
            return
        print(f"Ajetaan hissiä {hissin_numero} kerrokseen {kohdekerros}.")
        self.hissit[hissin_numero - 1].siirry_kerrokseen(kohdekerros)


if __name__ == "__main__":
    # Tehtävä 1
    print("--- Tehtävä 1 ---")
    h = Hissi(1, 10)
    h.siirry_kerrokseen(5)
    h.siirry_kerrokseen(h.alin_kerros)

    # Tehtävä 2
    print("\n--- Tehtävä 2 ---")
    talo = Talo(1, 10, 3)
    talo.aja_hissiä(1, 4)
    talo.aja_hissiä(2, 7)
    talo.aja_hissiä(3, 2)
    talo.aja_hissiä(1, 1)
    talo.aja_hissiä(2, 1)
    talo.aja_hissiä(3, 1)