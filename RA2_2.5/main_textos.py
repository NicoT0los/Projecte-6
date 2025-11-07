# Autor: Nico Tolos
# Data: 07/11/2025
# Versio: 1
# Descripcio: Programa que prova funcions del mòdul textos amb dades d'usuari.

import textos as tx

frase = input("Escriu una frase: ")

print("Majúscules:", tx.en_majuscules(frase))
print("Minúscules:", tx.en_minuscules(frase))
print("Capitalitzada:", tx.capitalitza(frase))
