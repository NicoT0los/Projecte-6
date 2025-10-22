# Autor: Nico Tolos
# Data: 22/10/2025
# Versio: 1
# Descripcio: El programa demana un nombre enter positiu a l'usuari
# i mostra tots els nombres primers des de 2 fins a aquest nombre.

# Defineix una funció per comprovar si un nombre és primer
def es_primer(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Demana un nombre enter positiu
try:
    n = int(input("Introdueix un nombre enter positiu: "))

    # Comprova que sigui vàlid
    if n < 2:
        print("No hi ha nombres primers menors que 2.")
    else:
        # Mostra els nombres primers
        print(f"Nombres primers des de 2 fins a {n}:")
        for i in range(2, n + 1):
            if es_primer(i):
                print(i, end=" ")
        print()

except ValueError:
    print("Error: has d’introduir un nombre enter positiu.")
