
from kosik import Basket, Goods

def display_goods(goods):
    """Zobrazí seznam dostupného zboží."""
    print("Dostupné zboží:")
    for item in goods:
        print(f"{item.id}. {item.name} - {item.price} Kč/ks - {item.quantity} ks skladem")

def main():
    # Načtení zboží ze skladu
    goods_objects = Goods.load_goods("Ukoly_Step/Ukol_16/sklad.json")
    
    # Inicializace košíku
    basket = Basket()
    
    print("Vítejte v e-shopu!")
    while True:
        display_goods(goods_objects)
        
        # Výběr zboží
        choice = input("Zadejte ID zboží (nebo 'q' pro ukončení): ").strip()
        if choice.lower() == 'q':
            break
        
        # Kontrola správnosti vstupu
        try:
            choice_id = int(choice)
            selected_good = next((g for g in goods_objects if g.id == choice_id), None)
            if not selected_good:
                print("Zboží s tímto ID nebylo nalezeno.")
                continue
        except ValueError:
            print("Neplatný vstup, zkuste to znovu.")
            continue

        # Zadání množství
        
        while True:
            quantity = input(f"Zadejte počet kusů pro {selected_good.name} (max {selected_good.quantity}): ").strip()    
            try:
                quantity = int(quantity)
                if quantity <= 0 or quantity > selected_good.quantity:
                    print("Neplatné množství. Zadejte hodnotu v povoleném rozsahu.")
                    continue
                else:
                    break
            except ValueError:
                print("Neplatný vstup, zkuste to znovu.")

        # Přidání do košíku
        basket.add_good(Goods(selected_good.id, selected_good.name, selected_good.price, quantity, selected_good.category))
        selected_good.quantity -= quantity  # Aktualizace skladu
        print(f"Přidáno {quantity} ks zboží {selected_good.name} do košíku.")

    # Ukončení nákupu a tisk faktury
    print("\nVáš nákup byl dokončen.")
    basket.print_invoice()

    # Aktualizace skladu
    Goods.save_goods("Ukoly_Step/Ukol_16/sklad.json", goods_objects)

if __name__ == "__main__":
    main()
