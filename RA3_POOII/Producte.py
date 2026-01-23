class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.__preu = preu if preu > 0 else 1
    
    def obtenir_preu(self):
        return self.__preu
    
    def modificar_preu(self, nou_preu):
        if nou_preu > 0:
            self.__preu = nou_preu
            print(f"Preu modificat a {nou_preu}€")
        else:
            print("El preu ha de ser superior a 0")