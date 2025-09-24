import math

PI = 3.1416  # Constant

def calcular_area(radi):   # Aquesta part és una funció
    return PI * radi ** 2

radi = float(input("Introdueix el radi: "))  
# Aquesta línia llegeix dades de l'usuari
# 'radi' és una variable

area = calcular_area(radi)  
# 'area' és una variable

print("L'àrea del cercle és:", area)  
# Aquesta línia mostra el resultat
