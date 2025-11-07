# Autor: Nico Tolos
# Data: 07/11/2025
# Versio: 1
# Descripcio: Rep qualsevol quantitat de nombres i retorna la seva multiplicació.

def multiplica_tot(*nombres):
    resultat = 1
    for n in nombres:
        resultat *= n
    return resultat
