class Sensor:
    def __init__(self, valor=0):
        self.__valor = valor if 0 <= valor <= 100 else 0
    
    def get_valor(self):
        return self.__valor
    
    def set_valor(self, nou_valor):
        if 0 <= nou_valor <= 100:
            self.__valor = nou_valor
            print(f"Valor del sensor actualitzat a {self.__valor}")
        else:
            print("El valor ha d'estar entre 0 i 100")