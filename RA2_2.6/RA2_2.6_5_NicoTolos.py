# Autor: Nico Tolos
# Data: 19/11/2025
# Versio: 1
# Descripcio: Funcions per convertir temperatures entre Celsius i Fahrenheit.

with open("sortida.txt", "r+") as f:
    contingut = f.read()
    print("Contingut actual:")
    print(contingut)
    f.write("Línia afegida amb r+\n")
