# Autor: Nico Tolos
# Data: 07/11/2025
# Versio: 1
# Descripcio: Mostra la data actual i calcula dies restants fins a una data.

from datetime import datetime, date

ara = datetime.now()
print("Data i hora actual:", ara.strftime("%d/%m/%Y %H:%M"))

any = int(input("Introdueix un any: "))
mes = int(input("Introdueix un mes: "))
dia = int(input("Introdueix un dia: "))

data_objectiu = date(any, mes, dia)
avui = date.today()
dies_restants = (data_objectiu - avui).days
print(f"Falten {dies_restants} dies per a {data_objectiu.strftime('%d/%m/%Y')}")
