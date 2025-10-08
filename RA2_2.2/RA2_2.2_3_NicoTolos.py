# Autor: Nico Tolos
# Data: 08/10/2025
# Versio: 1

# Descripcio: El programa demana un número enter i mostra la seva taula de multiplicar
# del 1 al 10 sense utilitzar la funció range().

# Demana un número enter a l'usuari
num = int(input("Introdueix un número enter: "))

# Inicialitza el comptador
i = 1

# Mostra la taula de multiplicar del 1 al 10 sense usar range()
print(f"Taula de multiplicar del {num}:")
while i <= 10:
    resultat = num * i
    print(f"{num} x {i} = {resultat}")
    i += 1
