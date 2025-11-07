# Autor: Nico Tolos
# Data: 07/11/2025
# Versio: 1
# Descripcio: Programa principal que fa servir el paquet utilitats per fer conversions.

from utilitats import temps, moneda

# Demanem dades a l'usuari
segons = int(input("Introdueix el nombre de segons: "))
euros = float(input("Introdueix una quantitat en euros: "))

# Fem conversions
print(f"{segons} segons = {temps.segons_a_minuts(segons):.2f} minuts")
print(f"{segons} segons = {temps.segons_a_hores(segons):.2f} hores")
print(f"{euros} euros = {moneda.euros_a_dolars(euros):.2f} dòlars")
