# Autor: Nico Tolos
# Data: 08/10/2025
# Versio: 1

# Descripcio: El programa calcula la suma dels primers 100 nombres enters positius
# (de l'1 al 100) i mostra el resultat per pantalla.

# Inicialitza les variables
num = 1
suma = 0

# Bucle per sumar els números de l'1 al 100
while num <= 100:
    suma += num
    num += 1

# Mostra el resultat
print(f"La suma dels primers 100 nombres enters positius és: {suma}")
