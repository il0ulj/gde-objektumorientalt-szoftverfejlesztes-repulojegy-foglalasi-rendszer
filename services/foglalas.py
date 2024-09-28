# services/foglalas.py
class FoglalasKezelo:
    def __init__(self):
        self.foglalasok = []

    def foglal(self, jarat, utas_nev):
        self.foglalasok.append({"utas_nev": utas_nev, "jarat": jarat})

        print(f"Sikeres foglalás: {utas_nev} részére, a(z) {jarat.get_jaratszam()} járatszámú járatra, "
              f"aminek a célállomása a(z) {jarat.get_celallomas()}. "
              f"A jegy ára: {jarat.get_jegyar()} HUF")

    def lemond(self, utas_nev):
        foglalas = next((f for f in self.foglalasok if f["utas_nev"] == utas_nev), None)
        if foglalas:
            self.foglalasok.remove(foglalas)
            print(f"Sikeres lemondás: {utas_nev} foglalása törölve.")
        else:
            print(f"Nincs foglalás {utas_nev} névvel.")

    def listaz_foglalasok(self):
        if not self.foglalasok:
            print("Nincsenek foglalások.")
        else:
            for foglalas in self.foglalasok:
                jarat = foglalas["jarat"]
                utas_nev = foglalas["utas_nev"]
                print(f"Utas: {utas_nev}, Járat: {jarat.get_jaratszam()}, Célállomás: {jarat.get_celallomas()}, "
                      f"Jegyár: {jarat.get_jegyar()} HUF")

