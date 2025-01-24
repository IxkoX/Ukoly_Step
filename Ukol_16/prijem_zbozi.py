import json

def load_goods(filename):
    """Načtení zboží ze souboru JSON."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def save_goods(filename, goods):
    """Uložení změněného seznamu zboží do souboru JSON."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(goods, file, indent=4, ensure_ascii=False)

def add_or_update_good(filename, new_good):
    """Přidání nového zboží nebo aktualizace existujícího v JSON souboru."""
    goods = load_goods(filename)
    for item in goods:
        if item["id"] == new_good["id"]:
            # Aktualizace množství a případně dalších atributů
            item["quantity"] += new_good["quantity"]
            break
    else:
        # Přidání nového zboží, pokud ID neexistuje
        goods.append(new_good)
    
    # Uložení zpět do JSON
    save_goods(filename, goods)
    print(f"Zboží bylo úspěšně přidáno/aktualizováno: {new_good['name']}")
