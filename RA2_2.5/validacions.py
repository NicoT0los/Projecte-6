# Autor: Nico Tolos
# Data: 07/11/2025
# Versio: 1
# Descripcio: Validació bàsica de correus i telèfons.

import re

def es_email_valid(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) is not None

def es_telefon_valid(telefon):
    return re.match(r'^\+?\d{9,15}$', telefon) is not None
