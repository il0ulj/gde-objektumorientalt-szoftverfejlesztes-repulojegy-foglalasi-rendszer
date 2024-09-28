# models/belfoldiJarat.py
from models.jarat import Jarat

class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def get_tipus(self):
        return "Belföldi Járat"
