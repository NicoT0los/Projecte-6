# Autor: Nico Tolos
# Data: 07/11/2025
# Versio: 1
# Descripcio: Funcions bàsiques de càlcul: suma, resta, multiplicació i divisió.

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divideix(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: divisió per zero!"
