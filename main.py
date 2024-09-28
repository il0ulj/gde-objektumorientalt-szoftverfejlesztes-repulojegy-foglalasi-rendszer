# main.py
from models.legitarsasag import LegiTarsasag
from models.belfoldiJarat import BelfoldiJarat
from models.nemzetkoziJarat import NemzetkoziJarat
from services.foglalas import FoglalasKezelo

def rendszer_inditas():
    legitarsasag = LegiTarsasag("PetAir")
    jarat1 = BelfoldiJarat("BJ11", "Budapest, Budapest Liszt Ferenc nemzetközi repülőtér", 15000)
    jarat2 = NemzetkoziJarat("NJ11", "London, Lutoni repülőtér", 50000)
    jarat3 = NemzetkoziJarat("NJ12", "New York, John Fitzgerald Kennedy nemzetközi repülőtér", 80000)
    
    legitarsasag.hozzaad_jarat(jarat1)
    legitarsasag.hozzaad_jarat(jarat2)
    legitarsasag.hozzaad_jarat(jarat3)

    foglalas_kezelo = FoglalasKezelo()
    foglalas_kezelo.foglal(jarat1, "Kiss János")
    foglalas_kezelo.foglal(jarat2, "Nagy Anna")
    foglalas_kezelo.foglal(jarat3, "Szabó Péter")
    foglalas_kezelo.foglal(jarat2, "Tóth Sándor")
    foglalas_kezelo.foglal(jarat1, "Kovács Izabella")
    foglalas_kezelo.foglal(jarat3, "Varga Sára")



    return legitarsasag, foglalas_kezelo


def felhasznaloi_interfesz():
    legitarsasag, foglalas_kezelo = rendszer_inditas()

    while True:
        print("\n--- Repülőjegy Foglalási Rendszer ---")
        print("1. Járatok listázása")
        print("2. Jegy foglalása")
        print("3. Foglalás lemondása")
        print("4. Foglalások listázása")
        print("5. Kilépés")

        valasztas = input("Válassz egy opciót: ")

        if valasztas == '1':
            legitarsasag.listaz_jaratok()
        elif valasztas == '2':
            utas_nev = input("Add meg az utas nevét: ")
            jaratszam = input("Add meg a foglalni kívánt járatszámot: ")
            jarat = next((j for j in legitarsasag.jaratok if j.get_jaratszam() == jaratszam), None)
            if jarat:
                foglalas_kezelo.foglal(jarat, utas_nev)
            else:
                print("Nincs ilyen járat.")
        elif valasztas == '3':
            utas_nev = input("Add meg a lemondani kívánt utas nevét: ")
            foglalas_kezelo.lemond(utas_nev)
        elif valasztas == '4':
            foglalas_kezelo.listaz_foglalasok()
        elif valasztas == '5':
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás. Próbáld újra.")


if __name__ == "__main__":
    felhasznaloi_interfesz()

