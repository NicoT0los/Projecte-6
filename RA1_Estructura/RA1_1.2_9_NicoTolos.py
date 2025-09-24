# Programa que demana un número i diu si és positiu, negatiu o zero

# Demanem el número a l'usuari
numero = float(input("Introdueix un número: "))

# Comprovem si és positiu, negatiu o zero
if numero > 0:
    print("El número és positiu.")
elif numero < 0:
    print("El número és negatiu.")
else:
    print("El número és zero.")

# Missatge final
print("Gràcies!")
