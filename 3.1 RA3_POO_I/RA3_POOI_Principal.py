from cotxe import Cotxe
from rectangle import Rectangle
from estudiant import Estudiant
from comptebancari import CompteBancari
from producte import Producte
from punt import Punt
from gos import Gos
from biblioteca import Biblioteca
from llibre import Llibre
from cercle import Cercle
from persona import Persona

# 1. Cotxes
c1 = Cotxe("Toyota", "Corolla", 2020)
c2 = Cotxe("Seat", "Ibiza", 2018)
c1.mostrar_info()
c2.mostrar_info()

# 2. Rectangles
rectangles = [Rectangle(2, 3), Rectangle(5, 4), Rectangle(6, 7)]
for r in rectangles:
    print("Àrea:", r.area())

# 3. Estudiants aprovats
estudiants = [
    Estudiant("Anna", 8),
    Estudiant("Marc", 4),
    Estudiant("Joan", 6)
]
for e in estudiants:
    if e.ha_aprovat():
        print(e.nom, "ha aprovat")

# 4. Compte bancari
compte = CompteBancari(100)
compte.ingressar(50)
compte.retirar(30)
compte.retirar(200)
compte.veure_saldo()

# 5. Descompte productes
def aplicar_descompte_productes(productes):
    for p in productes:
        p.aplicar_descompte(10)

productes = [Producte("Pa", 1.5), Producte("Llet", 1.2)]
aplicar_descompte_productes(productes)

# 6. Distància entre punts
p1 = Punt(0, 0)
p2 = Punt(3, 4)
print("Distància:", p1.distancia(p2))

# 7. Gos
gos = Gos("Rex", "gos")
gos.fer_soroll()

# 8. Biblioteca
biblio = Biblioteca()
biblio.afegir_llibre(Llibre("1984", "George Orwell", 1949))
biblio.afegir_llibre(Llibre("El Quijote", "Cervantes", 1605))
biblio.mostrar_llibres()

# 9. Cercles amb àrea > 50
cercles = [Cercle(2), Cercle(5), Cercle(10)]
for c in cercles:
    if c.area() > 50:
        print("Cercle amb àrea >", 50)

# 10. Persones majors de 30
def persones_mes_30(persones):
    for p in persones:
        if p.edat > 30:
            print(p.nom)

persones = [Persona("Laura", 28), Persona("Pere", 45)]
persones_mes_30(persones)
