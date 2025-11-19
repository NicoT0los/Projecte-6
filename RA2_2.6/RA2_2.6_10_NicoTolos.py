# Autor: Nico Tolos
# Data: 19/11/2025
# Versio: 1
# Descripcio: Funcions per convertir temperatures entre Celsius i Fahrenheit.

f = None
try:
    f = open("missatge.txt", "r")
    dades = f.read()
    print(dades)
    # Simulem un error
    raise Exception("Error simulat durant la lectura")
except Exception as e:
    print("S'ha produït un error:", e)
finally:
    if f:
        f.close()
        print("El fitxer s'ha tancat correctament.")
