# Autor: Nico Tolos
# Data: 05/11/2025
# Versio: 1
# Descripcio: Demana 10 números i crea dues llistes: una amb els parells i una altra amb els senars.

parells = []
senars = []
for i in range(10):
    n = int(input(f"Introdueix el número {i+1}: "))
    if n % 2 == 0:
        parells.append(n)
    else:
        senars.append(n)

print("Parells:", parells)
print("Senars:", senars)
