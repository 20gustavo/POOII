import datetime

class Historico:

    def __init__(self):
        self.transacoes = []
        self.data_abertura = datetime.datetime.today()
        self.transacoes.append(self.data_abertura)

    def add_transacoes(self, string):
        self.transacoes.append(string)

    def imprimir(self):
        for i in self.transacoes:
            print(i)
        print()