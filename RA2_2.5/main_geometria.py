# Autor: Nico Tolos
# Data: 07/11/2025
# Versio: 1
# Descripcio: Programa que calcula àrees demanant dades a l'usuari.

import geometria

costat = float(input("Costat del quadrat: "))
radi = float(input("Radi del cercle: "))
base = float(input("Base del rectangle: "))
altura = float(input("Altura del rectangle: "))

print("Àrea del quadrat:", geometria.area_quadrat(costat))
print("Àrea del cercle:", geometria.area_cercle(radi))
print("Àrea del rectangle:", geometria.area_rectangle(base, altura))
