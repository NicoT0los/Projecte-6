class Rellotge:
    def __init__(self, hores=0):
        self.__hores = hores if 0 <= hores <= 23 else 0
    
    def get_hores(self):
        return self.__hores
    
    def set_hores(self, valor):
        if 0 <= valor <= 23:
            self.__hores = valor
            print(f"Hora ajustada a {self.mostrar_hora()}")
        else:
            print("Les hores han d'estar entre 0 i 23")
    
    def mostrar_hora(self):
        return f"{self.__hores:02d}:00"