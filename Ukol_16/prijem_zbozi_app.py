from kosik import Goods

def main():
    filename = "Ukoly_Step/Ukol_16/sklad.json"
    
    # Načteme zboží
    goods_list = Goods.load_goods(filename)
    
    while True:
        print("\n1. Přidat nebo aktualizovat zboží")
        print("2. Zobrazit zboží")
        print("3. Uložit změny a ukončit")
        
        choice = input("Vyberte možnost: ")
        
        if choice == "1":
            print("\nAktuální seznam zboží:")
            # Zobrazíme aktuální seznam zboží
            for item in goods_list:
                print(f"ID: {item.id}, {item.name} - {item.price} Kč/ks - {item.quantity} ks skladem")
            
            try:
                id = int(input("\nZadejte ID zboží (pro úpravu nebo přidání nového): "))
                
                # Zkontrolujeme, zda zboží s tímto ID existuje
                existing_good = None
                for item in goods_list:
                    if item.id == id:
                        existing_good = item
                        break
                
                if existing_good:
                    # Zboží existuje, nabídneme úpravy
                    print(f"Zboží {existing_good.name} již existuje.")
                    print(f"Aktuální cena: {existing_good.price} Kč/ks, Aktuální množství: {existing_good.quantity} ks skladem.")
                    
                    # Nabídneme uživateli úpravy
                    while True:
                        choice = input("Co chcete upravit? (1: Cena, 2: Množství, 3: Obě): ")

                        if choice == "1" or choice == "3":
                            # Uživatel chce upravit cenu
                            while True:
                                try:
                                    new_price = float(input("Zadejte novou cenu: "))
                                    existing_good.price = new_price
                                    print(f"Cena byla aktualizována na {existing_good.price} Kč/ks.")
                                    break
                                except ValueError:
                                    print("Cena musí být číslo. Zkuste to znovu.")
                        
                        if choice == "2" or choice == "3":
                            # Uživatel chce upravit množství
                            while True:
                                try:
                                    new_quantity = int(input("Zadejte nové množství: "))
                                    existing_good.quantity = new_quantity
                                    print(f"Množství bylo aktualizováno na {existing_good.quantity} ks.")
                                    break
                                except ValueError:
                                    print("Množství musí být celé číslo. Zkuste to znovu.")
                                    
                        if choice in ["1", "2", "3"]:
                            break
                        else:
                            print("Neplatná volba, zkuste to znovu.")
                
                else:
                    # Zboží neexistuje, přidáme nové
                    name = input("Zadejte název zboží: ")
                    while True:
                        try:
                            price = float(input("Zadejte cenu za ks: "))
                            break
                        except ValueError:
                            print("Cena musí být číslo. Zkuste to znovu.")
                    while True:
                        try:
                            quantity = int(input("Zadejte množství: "))
                            break
                        except ValueError:
                            print("Množství musí být celé číslo. Zkuste to znovu.")
                    category = input("Zadejte kategorii: ")

                    new_good = Goods(id, name, price, quantity, category)
                    goods_list.append(new_good)
                    print(f"Přidáno nové zboží: {new_good.name}")
            
            except ValueError:
                print("Neplatný vstup, zkuste to znovu.")
        
        elif choice == "2":
            # Zobrazíme zboží
            for item in goods_list:
                print(f"ID: {item.id}, {item.name} - {item.price} Kč/ks - {item.quantity} ks skladem")
        
        elif choice == "3":
            # Uložíme změny zpět do souboru
            Goods.save_goods(filename, goods_list)
            break
        
        else:
            print("Neplatná volba, zkuste to znovu.")

if __name__ == "__main__":
    main()
 