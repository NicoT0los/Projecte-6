class Descompte20:
    def aplicar(self, total):
        return total * 0.2


class CarretCompra:
    def __init__(self, total, estrategia_descompte):
        self.total = total
        self.estrategia_descompte = estrategia_descompte
    
    def calcular_total_amb_descompte(self):
        descompte = self.estrategia_descompte.aplicar(self.total)
        return self.total - descompte


descompte = Descompte20()
carret = CarretCompra(100, descompte)
print(f"Total amb descompte: {carret.calcular_total_amb_descompte()}€")