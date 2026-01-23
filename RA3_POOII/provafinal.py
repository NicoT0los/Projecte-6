# Importació de totes les classes
from CompteBancari import CompteBancari
from Estudiant import Estudiant
from Termostat import Termostat
from Usuari import Usuari
from Sensor import Sensor
from Producte import Producte
from Rellotge import Rellotge
from Alumne import Alumne
from Joc import Joc
from CompteUsuari import CompteUsuari

print("=" * 60)
print("PROVES DE LES CLASSES - PROGRAMACIÓ ORIENTADA A OBJECTES II")
print("=" * 60)

# 1. CompteBancari
print("\n1. COMPTE BANCARI")
print("-" * 40)
compte = CompteBancari(1000)
print(f"Saldo inicial: {compte.consultar_saldo()}€")
compte.ingressar(500)
compte.retirar(200)
compte.retirar(2000)  # Prova amb saldo insuficient
print(f"Saldo final: {compte.consultar_saldo()}€")

# 2. Estudiant
print("\n2. ESTUDIANT")
print("-" * 40)
estudiant = Estudiant("Maria", 7.5)
print(f"Nota inicial: {estudiant.llegir_nota()}")
estudiant.modificar_nota(8.5)
estudiant.modificar_nota(11)  # Prova amb nota invàlida
print(f"Nota final: {estudiant.llegir_nota()}")

# 3. Termostat
print("\n3. TERMÒSTAT")
print("-" * 40)
termostat = Termostat(22)
print(f"Temperatura inicial: {termostat.get_temperatura()}°C")
termostat.set_temperatura(25)
termostat.set_temperatura(35)  # Prova amb valor invàlid
print(f"Temperatura final: {termostat.get_temperatura()}°C")

# 4. Usuari
print("\n4. USUARI (Contrasenya)")
print("-" * 40)
usuari = Usuari("Joan", "password123")
usuari.verificar_contrasenya("password123")
usuari.verificar_contrasenya("incorrecta")
usuari.canviar_contrasenya("novapass2024")
usuari.canviar_contrasenya("123")  # Prova amb contrasenya curta

# 5. Sensor
print("\n5. SENSOR")
print("-" * 40)
sensor = Sensor(50)
print(f"Valor inicial del sensor: {sensor.get_valor()}")
sensor.set_valor(75)
sensor.set_valor(150)  # Prova amb valor invàlid
print(f"Valor final del sensor: {sensor.get_valor()}")

# 6. Producte
print("\n6. PRODUCTE")
print("-" * 40)
producte = Producte("Portàtil", 899.99)
print(f"Producte: {producte.nom}, Preu: {producte.obtenir_preu()}€")
producte.modificar_preu(799.99)
producte.modificar_preu(-50)  # Prova amb preu invàlid
print(f"Preu final: {producte.obtenir_preu()}€")

# 7. Rellotge
print("\n7. RELLOTGE")
print("-" * 40)
rellotge = Rellotge(14)
print(f"Hora inicial: {rellotge.mostrar_hora()}")
rellotge.set_hores(21)
rellotge.set_hores(25)  # Prova amb hora invàlida
print(f"Hora final: {rellotge.mostrar_hora()}")

# 8. Alumne
print("\n8. ALUMNE")
print("-" * 40)
alumne = Alumne("Pere", 16)
print(f"Alumne: {alumne.nom}, Edat: {alumne.get_edat()} anys")
alumne.set_edat(17)
alumne.set_edat(-5)  # Prova amb edat negativa
print(f"Edat final: {alumne.get_edat()} anys")

# 9. Joc
print("\n9. JOC (Puntuació)")
print("-" * 40)
joc = Joc()
print(f"Puntuació inicial: {joc.obtenir_puntuacio()}")
joc.sumar_punts(100)
joc.sumar_punts(250)
joc.sumar_punts(50)
print(f"Puntuació acumulada: {joc.obtenir_puntuacio()}")
joc.reiniciar_puntuacio()
print(f"Puntuació després de reiniciar: {joc.obtenir_puntuacio()}")

# 10. CompteUsuari
print("\n10. COMPTE USUARI (Email)")
print("-" * 40)
compte_usuari = CompteUsuari("Anna", "anna@exemple.com")
print(f"Usuari: {compte_usuari.nom}, Email: {compte_usuari.get_email()}")
compte_usuari.set_email("anna.nova@gmail.com")
compte_usuari.set_email("emailinvalid")  # Prova amb email invàlid
print(f"Email final: {compte_usuari.get_email()}")

print("\n" + "=" * 60)
print("FI DE LES PROVES")
print("=" * 60)