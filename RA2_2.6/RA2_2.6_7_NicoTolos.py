# Autor: Nico Tolos
# Data: 19/11/2025
# Versio: 1
# Descripcio: Funcions per convertir temperatures entre Celsius i Fahrenheit.

try:
    with open("resultats.txt", "w") as f:
        f.write("Alguna informació important\n")
except PermissionError:
    print("No es pot escriure al fitxer resultats.txt. Permís denegat.")
