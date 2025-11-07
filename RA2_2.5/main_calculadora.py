# Autor: Nico Tolos
# Data: 07/11/2025
# Versio: 1
# Descripcio: Programa principal que fa servir el mòdul calculadora.py amb dades de l’usuari.

import calculadora

a = float(input("Introdueix el primer número: "))
b = float(input("Introdueix el segon número: "))

print("Suma:", calculadora.suma(a, b))
print("Resta:", calculadora.resta(a, b))
print("Multiplicació:", calculadora.multiplica(a, b))
print("Divisió:", calculadora.divideix(a, b))
