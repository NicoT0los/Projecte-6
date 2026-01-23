class Estudiant:
    def __init__(self, nom, nota=0):
        self.nom = nom
        self._nota = nota if 0 <= nota <= 10 else 0
    
    def llegir_nota(self):
        return self._nota
    
    def modificar_nota(self, nova_nota):
        if 0 <= nova_nota <= 10:
            self._nota = nova_nota
            print(f"Nota actualitzada a {self._nota}")
        else:
            print("La nota ha d'estar entre 0 i 10")