# homework_05

import datetime

# Aktuálního roku
current_year = datetime.datetime.now().year

# Otevření souboru jen jednou proto na začátku
with open("Ukoly_Step/Ukol_05/05_datumy.txt", mode="a", encoding="utf-8") as file:
    # Iterace přes všechny měsíce
    for month in range(1, 13):
        first_day = datetime.date(current_year, month, 1)
        print(first_day.strftime("%d/%m/%Y"))
        file.write(first_day.strftime("%d/%m/%Y") + "\n")
