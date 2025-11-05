# Autor: Nico Tolos
# Data: 05/11/2025
# Versio: 1
# Descripcio: Es defineix una funció que retorna la llista al revés sense fer servir reverse().

def llista_reves(llista):
    return llista[::-1]

nums = [1, 2, 3, 4, 5]
print("Llista original:", nums)
print("Llista al revés:", llista_reves(nums))
