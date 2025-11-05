# Autor: Nico Tolos
# Data: 05/11/2025
# Versio: 1
# Descripcio: Divideix una frase en paraules i les mostra una per una.

frase = input("Escriu una frase: ")
paraules = frase.split()
for p in paraules:
    print(p)
