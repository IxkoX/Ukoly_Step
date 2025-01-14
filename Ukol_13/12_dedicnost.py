#12_dedicnost.py

"""
Příkl 3x dědičnost
Zvíře (parent) - Pes (child).
Dopravní prostředek (parent) - Kolo (child).
Elektronické zařízení (parent) - Mobilní telefon (child).
"""

class Zvire:
    def __init__(self, jmeno, druh):
        self.jmeno = jmeno
        self.druh = druh

    def zvuk(self):
        return "Neznámý zvuk"

    def info(self):
        return f"{self.druh} jménem {self.jmeno}"

class Pes(Zvire):
    def __init__(self, jmeno, rasa):
        super().__init__(jmeno, "Pes")
        self.rasa = rasa

    def zvuk(self):
        return "Štěkot"

    def info(self):
        return f"{self.druh} jménem {self.jmeno}, rasa: {self.rasa}"

class Kocka(Zvire):
    def __init__(self, jmeno, barva):
        super().__init__(jmeno, "Kočka")
        self.barva = barva

    def zvuk(self):
        return "Mňoukání"

    def info(self):
        return f"{self.druh} jménem {self.jmeno}, barva: {self.barva}"


# Příklad
rex = Pes("Rex", "Německý ovčák")
micka = Kocka("Micka", "bílá")

print(rex.info()) 
print(rex.zvuk()) 

print(micka.info())
print(micka.zvuk())

