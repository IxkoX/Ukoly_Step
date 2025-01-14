import json

# Definice tříd
class Kategorie:
    def __init__(self, nazev):
        self.nazev = nazev

class Znacka:
    def __init__(self, nazev):
        self.nazev = nazev

class Produkt:
    def __init__(self, nazev, skladem, cena, kategorie, znacka):
        self.nazev = nazev
        self.skladem = skladem
        self.cena = cena
        self.kategorie = kategorie  
        self.znacka = znacka 

    def info(self):
        return (f"{self.nazev} ({self.znacka.nazev})\n"
                f"Skladem: {self.skladem} kusů\n"
                f"Cena: {self.cena} Kč\n"
                f"Kategorie: {self.kategorie.nazev}")

# Načtení dat z JSON souboru
with open("Ukoly_Step/Ukol_14/produkty.json", "r", encoding="utf-8") as file:
    data = json.load(file)

kategorie_map = {}
znacka_map = {}

# Vytvoření instancí produktů
produkty = []
for item in data:
    # Zpracování kategorie
    if item["kategorie"] not in kategorie_map:
        kategorie_map[item["kategorie"]] = Kategorie(item["kategorie"])
    kategorie = kategorie_map[item["kategorie"]]

    # Zpracování značky
    if item["znacka"] not in znacka_map:
        znacka_map[item["znacka"]] = Znacka(item["znacka"])
    znacka = znacka_map[item["znacka"]]

    # Vytvoření instance produktu
    produkt = Produkt(item["nazev"], item["skladem"], item["cena"], kategorie, znacka)
    produkty.append(produkt)

# Výpis všech produktů
for produkt in produkty:
    print(produkt.info())
    print("-" * 40)
