# Autor: Nico Tolos
# Data: 07/11/2025
# Versio: 1
# Descripcio: Simula llençar un dau i calcula la mitjana de tirades.

import random

def llençar_dau():
    return random.randint(1, 6)

def mitjana_daus(n):
    resultats = [llençar_dau() for _ in range(n)]
    return sum(resultats) / n

n = int(input("Quantes vegades vols llençar el dau? "))
print(f"Resultats: {[llençar_dau() for _ in range(n)]}")
print(f"Mitjana de {n} tirades: {mitjana_daus(n):.2f}")
