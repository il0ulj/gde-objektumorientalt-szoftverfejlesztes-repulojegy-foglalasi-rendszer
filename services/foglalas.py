class JegyFoglalas:
    def __init__(self, jarat, utas_nev):
        self.jarat = jarat
        self.utas_nev = utas_nev

    def __str__(self):
        return f"Foglalás: {self.utas_nev}, {self.jarat.get_celallomas()}, {self.jarat.get_jegyar()} HUF"

class FoglalasKezelo:
    def __init__(self):
        self.foglalasok = []

    def foglal(self, jarat, utas_nev):
        foglalas = JegyFoglalas(jarat, utas_nev)
        self.foglalasok.append(foglalas)
        print(f"Sikeres foglalás: {utas_nev} részére a(z) {jarat.get_celallomas()} járatra. Ár: {jarat.get_jegyar()} HUF")
        return jarat.get_jegyar()

    def lemond(self, utas_nev):
        for foglalas in self.foglalasok:
            if foglalas.utas_nev == utas_nev:
                self.foglalasok.remove(foglalas)
                print(f"{utas_nev} foglalása törölve.")
                return True
        print(f"Foglalás nem található: {utas_nev}")
        return False

    def listaz_foglalasok(self):
        if not self.foglalasok:
            print("Nincs aktív foglalás.")
        else:
            print("\nAktív foglalások:")
            for foglalas in self.foglalasok:
                print(foglalas)

