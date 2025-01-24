import json

class Basket:
    def __init__(self):
        self.items = []
    
    def add_good(self, good):
        self.items.append(good)
    
    def remove_good_by_id(self, id):
        self.items = [item for item in self.items if item.id != id]
    
    def calculate_total(self):
        return sum(item.price * item.quantity for item in self.items)
        
    def print_invoice(self):
        print("Faktura:")
        for item in self.items:
            print(f"{item.name} - {item.quantity} ks - {item.price * item.quantity:.2f} Kč")
        print(f"Celková částka: {self.calculate_total():.2f} Kč")


class Goods:
    def __init__(self, id, name, price, quantity, category):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    @staticmethod
    def load_goods(filename):
        """Načte seznam zboží ze souboru."""
        with open(filename, "r", encoding="utf-8") as file:
            goods_list = json.load(file)  # Načteme seznam slovníků
        return [Goods(**item) for item in goods_list]  # Převedeme slovníky na objekty

    @staticmethod
    def save_goods(filename, goods_list):
        try:
            # Převedeme objekty na slovníky
            goods_dict_list = [good.to_dict() for good in goods_list]
            
            # Otevření souboru pro zápis
            with open(filename, 'w', encoding='utf-8') as file:
                # Uložíme seznam slovníků
                json.dump(goods_dict_list, file, indent=4, ensure_ascii=False)
            print("Změny byly uloženy.")
        except Exception as e:
            print(f"Chyba při ukládání souboru: {e}")

    def to_dict(self):
        """Převede objekt Goods na slovník."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'category': self.category
        }

    @staticmethod
    def find_good_by_id(goods_list, id):
        """Najde zboží podle ID."""
        return next((item for item in goods_list if item.id == id), None)
    
    @staticmethod
    def add_or_update_good(goods_list, new_good):
        # Projdeme seznam a zjistíme, zda již zboží existuje podle ID
        for item in goods_list:
            if item.id == new_good.id:
                print(f"Zboží {item.name} již existuje.")
                print(f"Aktuální cena: {item.price} Kč/ks, Aktuální množství: {item.quantity} ks skladem.")
                
                # Zjistíme, co chce uživatel upravit
                choice = input("Co chcete upravit? (1: Cena, 2: Množství, 3: Obě): ")
                if choice == "1" or choice == "3":
                    # Uživatel chce upravit cenu
                    try:
                        new_price = float(input("Zadejte novou cenu: "))
                        item.price = new_price
                        print(f"Cena byla aktualizována na {item.price} Kč/ks.")
                    except ValueError:
                        print("Cena musí být číslo. Zkuste to znovu.")
                
                if choice == "2" or choice == "3":
                    # Uživatel chce upravit množství
                    try:
                        new_quantity = int(input("Zadejte nové množství: "))
                        item.quantity = new_quantity
                        print(f"Množství bylo aktualizováno na {item.quantity} ks.")
                    except ValueError:
                        print("Množství musí být celé číslo. Zkuste to znovu.")
                
                return goods_list  # Vracíme aktualizovaný seznam

        # Pokud zboží neexistuje, přidáme nové
        goods_list.append(new_good)
        print(f"Přidáno nové zboží: {new_good.name}")
        return goods_list
    
    

"""
# Načtení zboží
goods_objects = Goods.load_goods("Ukoly_Step/Ukol_16/sklad.json")

# Test
basket = Basket()

# Přidáme první a druhé zboží ze skladu
basket.add_good(goods_objects[0])
basket.add_good(goods_objects[1])

# Vytiskneme fakturu
basket.print_invoice()

# Odebereme první zboží podle ID
basket.remove_good_by_id(goods_objects[0].id)

# Vytiskneme fakturu znovu
basket.print_invoice()
"""