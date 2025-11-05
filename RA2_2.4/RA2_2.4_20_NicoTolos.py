# Autor: Nico Tolos
# Data: 05/11/2025
# Versio: 1
# Descripcio: Demana una llista de paraules i crea una nova llista amb només les que comencen per vocal.

paraules = input("Escriu diverses paraules separades per espais: ").split()
vocals = "aeiouAEIOU"
comencen_vocal = [p for p in paraules if p[0] in vocals]
print("Paraules que comencen per vocal:", comencen_vocal)
