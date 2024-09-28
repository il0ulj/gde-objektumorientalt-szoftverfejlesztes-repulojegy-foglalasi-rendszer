# models/legitarsasag.py
class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def hozzaad_jarat(self, jarat):
        self.jaratok.append(jarat)

    def listaz_jaratok(self):
        print(f"\n{self.nev} járatai:")
        for jarat in self.jaratok:
            print(jarat)

