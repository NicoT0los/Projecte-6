class ImpressoraPDF:
    def imprimir(self, contingut):
        raise NotImplementedError("Cal implementar el mètode imprimir")


class ImpressoraPDF(ImpressoraPDF):
    def imprimir(self, contingut):
        print(f"Imprimint PDF: {contingut}")


class Factura:
    def __init__(self, client, import_total, impressora):
        self.client = client
        self.import_total = import_total
        self.impressora = impressora
    
    def imprimir_factura(self):
        contingut = f"Factura per a {self.client}, total: {self.import_total} €"
        self.impressora.imprimir(contingut)


impressora_pdf = ImpressoraPDF()
factura = Factura("Client ABC", 1500, impressora_pdf)
factura.imprimir_factura()