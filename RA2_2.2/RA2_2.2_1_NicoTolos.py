# Autor: Nico Tolos
# Data: 08/10/2025
# Versio: 1

# Descripcio: El programa mostra una compte enrere des de 10 fins a 1
# i després imprimeix "Feliç Any Nou!".

import time  # Llibreria per fer pauses entre números

# Compta enrere de 10 a 1
num = 10
while num >= 1:
    print(num)
    time.sleep(1)  # Espera 1 segon entre números
    num -= 1

# Missatge final
print("Feliç Any Nou!")
