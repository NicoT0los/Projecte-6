# Primer demanem els números
num1 = int(input("Introdueix el primer número: "))
num2 = int(input("Introdueix el segon número: "))

# Després fem les operacions
print("La suma és:", num1 + num2)
print("La resta és:", num1 - num2)
print("La multiplicació és:", num1 * num2)

if num2 != 0:
    print("La divisió és:", num1 / num2)
else:
    print("No es pot dividir per zero.")