# Autor: Nico Tolos
# Data: 01/10/2025
# Versio: 1

# Descripcio: El programa demana tres números a l’usuari i mostra per pantalla quin és el més gran.

# Demanem tres números a l'usuari i els convertim a enters
num1 = int(input("Introdueix el primer número: "))
num2 = int(input("Introdueix el segon número: "))
num3 = int(input("Introdueix el tercer número: "))

# Inicialment suposem que el primer número és el més gran
mes_gran = num1

# Comparems amb el segon número:
# Si el segon és més gran que l'actual "mes_gran", l'actualitzem
if num2 > mes_gran:
    mes_gran = num2

# Comparems amb el tercer número:
# Si el tercer és més gran que l'actual "mes_gran", l'actualitzem
if num3 > mes_gran:
    mes_gran = num3

# Finalment, mostrem quin és el número més gran
print("El número més gran és:", mes_gran)