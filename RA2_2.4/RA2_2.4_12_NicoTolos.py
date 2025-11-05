# Autor: Nico Tolos
# Data: 05/11/2025
# Versio: 1
# Descripcio: Demana a l'usuari 5 paraules i les emmagatzema en una llista.

paraules = []
for i in range(5):
    p = input(f"Escriu la paraula {i+1}: ")
    paraules.append(p)
print("Les paraules són:", paraules)
