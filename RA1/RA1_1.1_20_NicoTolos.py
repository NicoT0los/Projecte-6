# 20. Minuts a hores i minuts
minuts = int(input("Introdueix el nombre de minuts: "))
hores = minuts // 60
resta_minuts = minuts % 60
print(f"{minuts} minuts són {hores} hores i {resta_minuts} minuts.")