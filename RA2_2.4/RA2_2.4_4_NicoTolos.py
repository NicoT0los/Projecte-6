# Autor: Nico Tolos
# Data: 05/11/2025
# Versio: 1
# Descripcio: Demana una paraula i verifica si és un palíndrom.

paraula = input("Introdueix una paraula: ")
if paraula == paraula[::-1]:
    print("És un palíndrom.")
else:
    print("No és un palíndrom.")
