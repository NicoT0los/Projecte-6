# Autor: Nico Tolos
# Data: 22/10/2025
# Versio: 1
# Descripcio: El programa demana un nombre enter a l'usuari
# i mostra la seva taula de multiplicar del 1 al 10.

# Demana un nombre enter
try:
    n = int(input("Introdueix un nombre enter: "))

    # Mostra la taula de multiplicar
    print(f"Taula de multiplicar del {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

except ValueError:
    print("Error: has d’introduir un nombre enter.")
