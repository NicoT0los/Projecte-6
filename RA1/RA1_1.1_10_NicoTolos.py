# 10. Demana dues edats i mostra qui és més gran
edat1 = int(input("Introdueix la primera edat: "))
edat2 = int(input("Introdueix la segona edat: "))
if edat1 > edat2:
    print("La primera persona és més gran.")
elif edat2 > edat1:
    print("La segona persona és més gran.")
else:
    print("Tenen la mateixa edat.")