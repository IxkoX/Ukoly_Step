# homework_06
import json

countries = {
    "CZ": "Česko",
    "SK": "Slovensko",
    "DE": "Německo",
    "AT": "Rakousko",
    "PL": "Polsko",
}

# 1) Převrácení klíčů a hodnot
#countries_name = {value: key for key, value in countries.items()}
countries_name = {countries[key]: key for key in countries}

# 2) Zjištění počtu znaků pro každý stát
countries_len = {key: len(value) for key, value in countries.items()}

# Výpis výsledků
print("countries_name:", countries_name)
print(json.dumps(countries_name, ensure_ascii=False, indent=4))
print("countries_len:", countries_len)
print(json.dumps(countries_len, ensure_ascii=False, indent=4))
