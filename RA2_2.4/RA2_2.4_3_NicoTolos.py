# Autor: Nico Tolos
# Data: 05/11/2025
# Versio: 1
# Descripcio: Es defineix una funció que reverteix una cadena.

def reversa(cadena):
    return cadena[::-1]

text = input("Introdueix una cadena: ")
print("Revertida:", reversa(text))
