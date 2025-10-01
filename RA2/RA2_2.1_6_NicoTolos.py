# Autor: Nico Tolos
# Data: 01/10/2025
# Versio: 1

# Descripcio: El programa demana una lletra a l’usuari i indica si és una vocal o una consonant.

lletra = input("Introdueix una lletra: ")  
# Demana a l’usuari que introdueixi una lletra

# Comprovem si la lletra és una vocal
if lletra in ["a", "e", "i", "o", "u"]:  
    # Si la lletra és dins de la llista de vocals
    print("És una vocal.")  
    # Mostra que és una vocal
else:  
    # En qualsevol altre cas
    print("És una consonant.")  
    # Mostra que és una consonant

