# Autor: Nico Tolos
# Data: 08/10/2025
# Versio: 1

# Descripcio: El programa demana a l'usuari un número enter positiu i determina
# si és un nombre primer o no.

# Demana un número enter positiu
num = int(input("Introdueix un número enter positiu: "))

# Comprova si és vàlid
if num <= 0:
    print("Has d’introduir un número enter positiu.")
else:
    # Comprova si és primer
    primer = True

    if num == 1:
        primer = False  # El 1 no es considera primer
    else:
        divisor = 2
        while divisor <= num // 2:
            if num % divisor == 0:
                primer = False
                break
            divisor += 1

    # Mostra el resultat
    if primer:
        print(f"El número {num} és primer.")
    else:
        print(f"El número {num} no és primer.")
