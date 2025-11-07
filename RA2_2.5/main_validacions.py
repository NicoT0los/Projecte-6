# Autor: Nico Tolos
# Data: 07/11/2025
# Versio: 1
# Descripcio: Programa que comprova si un email i un telèfon són vàlids.

import validacions as v

email = input("Introdueix un correu electrònic: ")
telefon = input("Introdueix un número de telèfon: ")

print("Email vàlid:", v.es_email_valid(email))
print("Telèfon vàlid:", v.es_telefon_valid(telefon))
