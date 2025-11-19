# Autor: Nico Tolos
# Data: 19/11/2025
# Versio: 1
# Descripcio: Funcions per convertir temperatures entre Celsius i Fahrenheit.

with open("nombres.txt", "r") as f:
    for i, linia in enumerate(f, start=1):
        try:
            nombre = int(linia.strip())
            print(f"Línia {i}: {nombre}")
        except ValueError:
            print(f"Línia {i} no és un nombre vàlid: {linia.strip()}")
