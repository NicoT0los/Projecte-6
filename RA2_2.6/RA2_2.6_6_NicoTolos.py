# Autor: Nico Tolos
# Data: 19/11/2025
# Versio: 1
# Descripcio: Funcions per convertir temperatures entre Celsius i Fahrenheit.

import os

if os.path.exists("dades.txt"):
    with open("dades.txt", "r") as f:
        print(f.read())
else:
    print("Error: el fitxer dades.txt no existeix.")
