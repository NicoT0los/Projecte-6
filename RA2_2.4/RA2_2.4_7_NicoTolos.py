# Autor: Nico Tolos
# Data: 05/11/2025
# Versio: 1
# Descripcio: Demana una cadena i compta quantes vegades apareix una lletra concreta.

cadena = input("Introdueix una cadena: ")
lletra = input("Quina lletra vols comptar? ")
comptador = cadena.count(lletra)
print(f"La lletra '{lletra}' apareix {comptador} vegades.")
