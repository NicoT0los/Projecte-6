# Autor: Nico Tolos
# Data: 22/10/2025
# Versio: 1
# Descripcio: El programa demana un nombre enter positiu a l'usuari
# i calcula la suma de tots els nombres des de 1 fins a aquest nombre.

# Demana un nombre positiu a l'usuari
try:
    n = int(input("Introdueix un nombre enter positiu: "))

    # Comprova que sigui positiu
    if n < 1:
        print("Error: el nombre ha de ser positiu.")
    else:
        # Calcula la suma amb range()
        total = sum(range(1, n + 1))
        print(f"La suma dels nombres de 1 a {n} és {total}.")

except ValueError:
    print("Error: has d’introduir un nombre enter positiu.")
