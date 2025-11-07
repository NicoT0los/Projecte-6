# Autor: Nico Tolos
# Data: 07/11/2025
# Versio: 1
# Descripcio: Programa que converteix temperatures demanades a l'usuari.

import conversions

c = float(input("Introdueix temperatura en Celsius: "))
f = float(input("Introdueix temperatura en Fahrenheit: "))

print(f"{c} °C són {conversions.celsius_a_fahrenheit(c):.2f} °F")
print(f"{f} °F són {conversions.fahrenheit_a_celsius(f):.2f} °C")
