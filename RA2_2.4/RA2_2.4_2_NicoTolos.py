# Autor: Nico Tolos
# Data: 05/11/2025
# Versio: 1
# Descripcio: Demana una frase i compta quantes vocals conté.

frase = input("Escriu una frase: ")
vocals = "aeiouAEIOU"
comptador = sum(1 for lletra in frase if lletra in vocals)
print("Nombre de vocals:", comptador)
