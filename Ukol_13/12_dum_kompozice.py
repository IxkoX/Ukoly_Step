#12_dum_kompozice.py

"""
Příklad 3 kompozicí
Dům - Okno (1 dům má více oken).
Knihovna - Kniha (1 knihovna obsahuje více knih).
Zahrada - Strom (1 zahrada obsahuje více stromů).
"""
class Okno:
    def __init__(self, velikost):
        self.velikost = velikost  # Velikost okna v metrech čtverečních

class Dum:
    def __init__(self):
        self.okna = []  # Seznam oken v domě

    def pridat_okno(self, velikost):
        nove_okno = Okno(velikost)
        self.okna.append(nove_okno)

    def vypis_okna(self):
        for i, okno in enumerate(self.okna, 1):
            print(f"Okno {i}: velikost {okno.velikost} m²")


dum = Dum()
dum.pridat_okno(2.5)
dum.pridat_okno(1.8)

dum.vypis_okna()
