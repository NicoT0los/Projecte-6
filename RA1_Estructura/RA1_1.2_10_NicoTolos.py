# Calculadora senzilla

num1 = float(input("Introdueix el primer número: "))
num2 = float(input("Introdueix el segon número: "))
operacio = input("Introdueix l’operació (+, -, *, /): ")

if operacio == "+":
    print("Resultat:", num1 + num2)
elif operacio == "-":
    print("Resultat:", num1 - num2)
elif operacio == "*":
    print("Resultat:", num1 * num2)
elif operacio == "/":
    if num2 != 0:
        print("Resultat:", num1 / num2)
    else:
        print("Error: no es pot dividir per zero.")
else:
    print("Operació no vàlida.")

print("Gràcies!")
