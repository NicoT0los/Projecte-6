# Autor: Nico Tolos
# Data: 07/11/2025
# Versio: 1
# Descripcio: Determina l'estat d'una persona segons la seva edat.

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

for edat in [12, 25, 70]:
    estat, descripcio = estat_persona(edat)
    print(f"Edat {edat}: {estat} - {descripcio}")
