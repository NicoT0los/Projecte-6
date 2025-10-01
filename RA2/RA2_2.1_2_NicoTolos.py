# Autor: Nico Tolos
# Data: 01/10/2025
# Versio: 1

# Descripcio: El programa demana un numero a l'usuari i mostra si es parell o imparell segons el residu de dividir-lo entre 2.

# Demanem a l'usuari que introdueixi un número.
num = int(input("Introdueix un número: "))

# Ara comprovem si el número és parell o imparell.
# Per fer-ho utilitzem l'operador %, que ens dona el residu de la divisió.
# Si el residu de dividir entre 2 és 0, el número és parell.
if num % 2 == 0:
    # Si la condició anterior és certa (residu = 0), escrivim que és parell.
    print("El número és parell.")
else:
    # Si no es compleix la condició (residu diferent de 0), vol dir que és imparell.
    print("El número és imparell.")
