# Autor: Nico Tolos
# Data: 08/10/2025
# Versio: 1

# Descripcio: El programa demana una frase a l'usuari
# i compta quantes vocals conté.

# Demana una frase a l'usuari
frase = input("Introdueix una frase: ")

# Defineix les vocals
vocals = "aeiouàèéíòóúAEIOUÀÈÉÍÒÓÚ"

# Inicialitza el comptador
comptador = 0

# Recorre cada lletra i comprova si és una vocal
for lletra in frase:
    if lletra in vocals:
        comptador += 1

# Mostra el resultat
print("La frase conté", comptador, "vocals.")
