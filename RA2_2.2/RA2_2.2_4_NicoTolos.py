# Autor: Nico Tolos
# Data: 08/10/2025
# Versio: 1

# Descripcio: El programa genera un número aleatori entre 1 i 100 i demana a l’usuari 
# que intenti endevinar-lo. Informa si el número introduït és massa alt, massa baix o correcte.

import random

# Generar un número aleatori entre 1 i 100
secret = random.randint(1, 100)

print("He pensat un número entre 1 i 100. Pots endevinar quin és?")

endevinat = False
while not endevinat:
    intent = int(input("Introdueix un número: "))

    if intent < secret:
        print("Massa baix!")
    elif intent > secret:
        print("Massa alt!")
    else:
        print("Correcte! Has endevinat el número!")
        endevinat = True
