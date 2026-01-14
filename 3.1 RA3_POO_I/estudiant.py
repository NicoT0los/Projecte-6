class Estudiant:
    def __init__(self, nom, nota):
        self.nom = nom
        self.nota = nota

    def ha_aprovat(self):
        return self.nota >= 5
