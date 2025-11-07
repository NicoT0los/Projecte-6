# Autor: Nico Tolos
# Data: 07/11/2025
# Versio: 1
# Descripcio: Calcula el factorial de diferents nombres de forma recursiva.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(0))
print(factorial(3))
print(factorial(5))
