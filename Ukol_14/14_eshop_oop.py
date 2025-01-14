# 14_eshop_oop.py

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

# Vytvoření kategorií
kategorie_plysaci = Kategorie("Plyšáci")
kategorie_lego = Kategorie("Lego")
kategorie_auticka = Kategorie("Autíčka")

# Vytvoření značek
znacka_disney = Znacka("Disney")
znacka_lego = Znacka("LEGO")
znacka_hotwheels = Znacka("Hot Wheels")

# Vytvoření produktů
produkty = [
    Produkt("Medvídek Pú", 10, 350, kategorie_plysaci, znacka_disney),
    Produkt("Myšák Mickey", 5, 400, kategorie_plysaci, znacka_disney),
    Produkt("Pejsek Fluffy", 8, 250, kategorie_plysaci, znacka_disney),
    Produkt("Kočička Kitty", 12, 300, kategorie_plysaci, znacka_disney),
    Produkt("Sovička Ouki", 7, 320, kategorie_plysaci, znacka_disney),
    Produkt("Zajíček Hopík", 15, 280, kategorie_plysaci, znacka_disney),
    Produkt("Tučňák Pingo", 4, 340, kategorie_plysaci, znacka_disney),
    Produkt("Panda Mimi", 9, 370, kategorie_plysaci, znacka_disney),
    Produkt("Žirafka Lili", 6, 330, kategorie_plysaci, znacka_disney),
    Produkt("Sloník Eli", 3, 390, kategorie_plysaci, znacka_disney),

    Produkt("Lego City", 20, 800, kategorie_lego, znacka_lego),
    Produkt("Lego Friends", 15, 750, kategorie_lego, znacka_lego),
    Produkt("Lego Technic", 10, 1200, kategorie_lego, znacka_lego),
    Produkt("Lego Star Wars", 8, 1500, kategorie_lego, znacka_lego),
    Produkt("Lego Harry Potter", 12, 1400, kategorie_lego, znacka_lego),
    Produkt("Lego Duplo", 25, 500, kategorie_lego, znacka_lego),
    Produkt("Lego Creator", 14, 950, kategorie_lego, znacka_lego),
    Produkt("Lego Ninjago", 18, 1100, kategorie_lego, znacka_lego),
    Produkt("Lego Architecture", 6, 1600, kategorie_lego, znacka_lego),
    Produkt("Lego Marvel", 9, 1300, kategorie_lego, znacka_lego),

    Produkt("Hot Wheels Sport", 30, 120, kategorie_auticka, znacka_hotwheels),
    Produkt("Hot Wheels SUV", 20, 150, kategorie_auticka, znacka_hotwheels),
    Produkt("Hot Wheels Monster Truck", 10, 250, kategorie_auticka, znacka_hotwheels),
    Produkt("Hot Wheels Retro", 12, 200, kategorie_auticka, znacka_hotwheels),
    Produkt("Hot Wheels Off-Road", 8, 180, kategorie_auticka, znacka_hotwheels),
    Produkt("Hot Wheels Drift", 15, 170, kategorie_auticka, znacka_hotwheels),
    Produkt("Hot Wheels Police", 22, 190, kategorie_auticka, znacka_hotwheels),
    Produkt("Hot Wheels Fire Truck", 14, 220, kategorie_auticka, znacka_hotwheels),
    Produkt("Hot Wheels Ambulance", 18, 210, kategorie_auticka, znacka_hotwheels),
    Produkt("Hot Wheels Classic", 25, 160, kategorie_auticka, znacka_hotwheels)
]

# Výpis všech produktů
for produkt in produkty:
    print(produkt.info())
    print("-" * 50)
