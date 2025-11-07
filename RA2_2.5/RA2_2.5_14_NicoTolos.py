# Autor: Nico Tolos
# Data: 07/11/2025
# Versio: 1
# Descripcio: Comprova si els nombres d'una llista són parells.

def es_parell(numero):
    return numero % 2 == 0

for n in [1, 2, 3, 4, 5, 6]:
    print(f"El número {n} és parell: {es_parell(n)}")
