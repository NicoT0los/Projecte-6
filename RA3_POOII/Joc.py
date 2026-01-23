class Joc:
    def __init__(self):
        self.__puntuacio = 0
    
    def sumar_punts(self, punts):
        if punts > 0:
            self.__puntuacio += punts
            print(f"S'han sumat {punts} punts. Puntuació actual: {self.__puntuacio}")
        else:
            print("Els punts a sumar han de ser positius")
    
    def reiniciar_puntuacio(self):
        self.__puntuacio = 0
        print("Puntuació reiniciada a 0")
    
    def obtenir_puntuacio(self):
        return self.__puntuacio