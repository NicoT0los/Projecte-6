# Autor: Nico Tolos
# Data: 01/10/2025
# Versio: 1

# Descripcio: El programa demana una nota de l’1 al 10 i mostra per pantalla si l’alumne està aprovat (nota ≥ 5) o suspès (nota < 5).

# Demanem una nota a l'usuari (del 1 al 10) i la convertim a enter
nota = int(input("Introdueix una nota (1-10): "))

# Comprovem si la nota és igual o superior a 5
if nota >= 5:
    # Si la condició és certa, mostrem "Aprovat"
    print("Aprovat")
else:
    # Si la condició no es compleix, mostrem "Suspès"
    print("Suspès")

