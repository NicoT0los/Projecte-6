# Autor: Nico Tolos
# Data: 05/11/2025
# Versio: 1
# Descripcio: Es defineix una funció que elimina tots els espais d'una cadena.

def sense_espais(cadena):
    return cadena.replace(" ", "")

text = input("Introdueix una cadena: ")
print("Sense espais:", sense_espais(text))
