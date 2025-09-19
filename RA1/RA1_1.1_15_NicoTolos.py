# 15. Velocitat mitjana
distancia = float(input("Introdueix la distància (km): "))
temps = float(input("Introdueix el temps (hores): "))
if temps > 0:
    velocitat = distancia / temps
    print("La velocitat mitjana és:", velocitat, "km/h")
else:
    print("El temps ha de ser més gran que zero.")