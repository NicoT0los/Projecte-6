# Autor: Nico Tolos
# Data: 01/10/2025
# Versio: 1

# Descripcio: El programa demana un número, el converteix a decimal i decideix, mitjançant condicions, si és positiu, igual a zero o negatiu.

# Demanem el número a l'usuari
num = float(input("Introdueix un número: "))

# Comprovem si és més gran que zero
if num > 0:
    print("El número és més gran que zero.")
elif num == 0:
    print("El número és igual a zero.")
else:
    print("El número és més petit que zero.")
