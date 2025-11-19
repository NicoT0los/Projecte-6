# Autor: Nico Tolos
# Data: 19/11/2025
# Versio: 1
# Descripcio: Funcions per convertir temperatures entre Celsius i Fahrenheit.

try:
    with open("nou_fitxer.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    with open("nou_fitxer.txt", "w") as f:
        f.write("Fitxer creat automàticament\n")
    print("Fitxer creat amb contingut per defecte.")
