# Constant
IVA = 0.21   # Constant que representa el 21% d'IVA

# Funció que calcula el preu amb IVA
def preu_amb_iva(preu):
    return preu + (preu * IVA)

# Entrada de l’usuari
preu_sense_iva = float(input("Introdueix el preu sense IVA: "))

# Crida a la funció i sortida per pantalla
preu_final = preu_amb_iva(preu_sense_iva)
print("El preu final amb IVA és:", preu_final)
