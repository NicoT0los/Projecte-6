# Autor: Nico Tolos
# Data: 07/11/2025
# Versio: 1
# Descripcio: Calcula el factorial d'un nombre de forma recursiva.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
