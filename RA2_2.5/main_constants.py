# Autor: Nico Tolos
# Data: 07/11/2025
# Versio: 1
# Descripcio: Calcula la força gravitatòria amb dades d'usuari.

import constants

massa = float(input("Introdueix la massa (kg): "))
forca = massa * constants.GRAVETAT
print(f"Força gravitatòria: {forca:.2f} N")
