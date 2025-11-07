# Autor: Nico Tolos
# Data: 07/11/2025
# Versio: 1
# Descripcio: Menú interactiu per utilitzar funcions de la calculadora científica.

import cientifica as ci
import calculadora as calc

while True:
    print("\n--- Calculadora Científica ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Arrel quadrada")
    print("4. Potència")
    print("5. Sinus")
    print("0. Sortir")
    
    opcio = input("Escull una opció: ")

    if opcio == "0":
        break
    elif opcio == "1":
        a = float(input("a: "))
        b = float(input("b: "))
        print("Resultat:", calc.suma(a, b))
    elif opcio == "2":
        a = float(input("a: "))
        b = float(input("b: "))
        print("Resultat:", calc.resta(a, b))
    elif opcio == "3":
        x = float(input("x: "))
        print("Resultat:", ci.sqrt(x))
    elif opcio == "4":
        a = float(input("a: "))
        b = float(input("b: "))
        print("Resultat:", ci.pow(a, b))
    elif opcio == "5":
        x = float(input("Angle en graus: "))
        print("Resultat:", ci.sin(x))
    else:
        print("Opció no vàlida.")
