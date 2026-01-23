class CompteBancari:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial
    
    def ingressar(self, quantitat):
        if quantitat > 0:
            self.__saldo += quantitat
            print(f"S'han ingressat {quantitat}€. Saldo actual: {self.__saldo}€")
        else:
            print("La quantitat a ingressar ha de ser positiva")
    
    def retirar(self, quantitat):
        if quantitat > 0:
            if quantitat <= self.__saldo:
                self.__saldo -= quantitat
                print(f"S'han retirat {quantitat}€. Saldo actual: {self.__saldo}€")
            else:
                print("Saldo insuficient")
        else:
            print("La quantitat a retirar ha de ser positiva")
    
    def consultar_saldo(self):
        return self.__saldo