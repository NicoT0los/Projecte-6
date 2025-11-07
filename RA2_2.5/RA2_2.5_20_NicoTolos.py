# Autor: Nico Tolos
# Data: 07/11/2025
# Versio: 1
# Descripcio: Filtra els nombres parells de diverses llistes i els mostra.

def filtra_parells(llista):
    return [n for n in llista if n % 2 == 0]

print(filtra_parells([1, 2, 3, 4, 5, 6]))
print(filtra_parells([10, 15, 20, 25, 30]))
