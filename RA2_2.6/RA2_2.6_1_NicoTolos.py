# Llegir i mostrar el contingut d'un fitxer
try:
    with open("missatge.txt", "r") as f:
        contingut = f.read()
        print("Contingut del fitxer:")
        print(contingut)
except FileNotFoundError:
    print("El fitxer missatge.txt no existeix.")
