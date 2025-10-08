# Autor: Nico Tolos
# Data: 08/10/2025
# Versio: 1

# Descripcio: El programa utilitza un bucle per imprimir
# un patró d'estrelles en forma de triangle.

# Demana a l'usuari el nombre de línies
files = int(input("Introdueix el nombre de línies del patró: "))

# Imprimeix el patró d'estrelles
for i in range(1, files + 1):
    print("*" * i)
