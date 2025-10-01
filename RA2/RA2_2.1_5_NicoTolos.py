# Autor: Nico Tolos
# Data: 01/10/2025
# Versio: 1

# Descripcio: És un programa senzill que determina si una persona és major o menor d’edat segons l’any de naixement.

any = int(input("Introdueix el teu any de naixement: "))  
# Demana a l’usuari l’any de naixement i el guarda com a número enter

if any < 2007:  
    # Comprova si l’any és anterior a 2007
    print("Ets major d'edat")  
    # Si és anterior, la persona és major d’edat

else:  
    # En qualsevol altre cas (2007 o posterior)
    print("Ets menor d'edat")  
    # La persona encara és menor d’edat

