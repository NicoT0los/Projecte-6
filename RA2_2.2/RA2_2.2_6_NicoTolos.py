# Autor: Nico Tolos
# Data: 08/10/2025
# Versio: 1

# Descripcio: El programa mostra els primers 10 termes de la seqüència de Fibonacci
# (comença amb 0 i 1) i mostra el resultat per pantalla.

a, b = 0, 1

print("Primers 10 termes de la seqüència de Fibonacci:")

for i in range(10):
    print(a, end=" " if i < 9 else "\n")
    a, b = b, a + b
