# Autor: Nico Tolos
# Data: 07/11/2025
# Versio: 1
# Descripcio: Retorna l'estat d'una persona segons l'edat i una descripció addicional.

def estat_persona(edat):
    if edat < 18:
        estat = "Menor d'edat"
        descripcio = "Encara no ets adult."
    elif edat < 65:
        estat = "Adult"
        descripcio = "Estàs en edat laboral."
    else:
        estat = "Jubilat"
        descripcio = "Gaudeix de la jubilació!"
    return estat, descripcio
