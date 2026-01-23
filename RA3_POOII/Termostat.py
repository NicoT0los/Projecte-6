class Termostat:
    def __init__(self, temperatura=20):
        self.__temperatura = temperatura if 10 <= temperatura <= 30 else 20
    
    def get_temperatura(self):
        return self.__temperatura
    
    def set_temperatura(self, valor):
        if 10 <= valor <= 30:
            self.__temperatura = valor
            print(f"Temperatura ajustada a {self.__temperatura}°C")
        else:
            print("La temperatura ha d'estar entre 10 i 30°C")