class Alumne:
    def __init__(self, nom, edat):
        self.nom = nom
        self.__edat = edat if edat >= 0 else 0
    
    def get_edat(self):
        return self.__edat
    
    def set_edat(self, valor):
        if valor >= 0:
            self.__edat = valor
            print(f"Edat de {self.nom} actualitzada a {self.__edat} anys")
        else:
            print("L'edat no pot ser negativa")