class Biblioteca:
    def __init__(self):
        self.llibres = []

    def afegir_llibre(self, llibre):
        self.llibres.append(llibre)

    def mostrar_llibres(self):
        for llibre in self.llibres:
            llibre.mostrar_info()
