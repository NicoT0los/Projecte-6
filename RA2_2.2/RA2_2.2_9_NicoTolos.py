# Autor: Nico Tolos
# Data: 08/10/2025
# Versio: 1

# Descripcio: El programa demana una llista de nombres a l'usuari
# i mostra quin és el número màxim.

# Demana a l'usuari una llista de nombres separats per espais
entrada = input("Introdueix una llista de nombres separats per espais: ")

# Converteix la cadena en una llista de nombres
llista = [float(num) for num in entrada.split()]

# Troba el número màxim
maxim = max(llista)

# Mostra el resultat
print("El número màxim de la llista és:", maxim)
