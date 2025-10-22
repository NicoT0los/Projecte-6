# Autor: Nico Tolos
# Data: 22/10/2025
# Versio: 1
# Descripcio: El programa demana un nombre enter positiu a l'usuari
# i mostra tots els nombres parells des de 0 fins a aquest nombre.

# Demana un nombre enter positiu
try:
    n = int(input("Introdueix un nombre enter positiu: "))

    # Comprova que sigui positiu
    if n < 0:
        print("Error: el nombre ha de ser positiu.")
    else:
        # Mostra els nombres parells amb range()
        print(f"Nombres parells des de 0 fins a {n}:")
        for i in range(0, n + 1, 2):
            print(i, end=" ")
        print()

except ValueError:
    print("Error: has d’introduir un nombre enter positiu.")
