# homewoek_04.py

imput = input("Zadejte text, který chcete uložit do souboru: ")

with open("Ukoly_Step/Ukol_04/04_file.txt", mode="a", encoding="utf-8") as file:
    file.write(imput + "\n")

print("Text byl úspěšně uložen do souboru.")
