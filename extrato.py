class Extrato:   
    def __init__(self):
        self.transacoes = []

    def extrato(self, numeroconta):
        print("Extrato : ",numeroconta," \n")
        for p in self.transacoes:
            print(p[0],'  ', p[1], '  ', p[2], '  ', p[3])
          