# Autor: Nico Tolos
# Data: 22/10/2025
# Versio: 1
# Descripcio: El programa demana un nombre enter a l'usuari
# i mostra una seqüència de nombres des de 0 fins a aquest nombre.

# Demana un nombre enter a l'usuari
try:
    n = int(input("Introdueix un nombre enter: "))

    # Mostra la seqüència
    for i in range(n + 1):
        print(i, end=" ")
    print()

except ValueError:
    print("Error: has d’introduir un nombre enter.")
