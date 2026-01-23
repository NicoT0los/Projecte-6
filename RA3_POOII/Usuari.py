class Usuari:
    def __init__(self, nom, contrasenya):
        self.nom = nom
        self.__contrasenya = contrasenya if len(contrasenya) >= 8 else "12345678"
    
    def canviar_contrasenya(self, nova_contrasenya):
        if len(nova_contrasenya) >= 8:
            self.__contrasenya = nova_contrasenya
            print("Contrasenya canviada correctament")
        else:
            print("La contrasenya ha de tenir mínim 8 caràcters")
    
    def verificar_contrasenya(self, clau):
        return self.__contrasenya == clau