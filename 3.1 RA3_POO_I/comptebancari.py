class CompteBancari:
    def __init__(self, saldo):
        self.saldo = saldo

    def ingressar(self, quantitat):
        self.saldo += quantitat

    def retirar(self, quantitat):
        if quantitat <= self.saldo:
            self.saldo -= quantitat
        else:
            print("Saldo insuficient")

    def veure_saldo(self):
        print(f"Saldo actual: {self.saldo} €")
