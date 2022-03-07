import datetime

class Cliente:

    __slots__ = ['_name', '_sobre', '_cpf']
    def __init__(self, nome, sobrenome, cpf):
        self._name = nome
        self._sobre = sobrenome
        self._cpf = cpf

    @property
    def Nome(self):
        return self._name

    @Nome.setter
    def Nome(self, novo):
        self._name = novo

    @property
    def Sobre(self):
        return self._sobre

    @Sobre.setter
    def Sobre(self, novo):
        self._sobre = novo

    @property
    def CPF(self):
        return self._cpf

    @CPF.setter
    def CPF(self, novo):
        self._cpf = novo

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

class Conta:

    _total_contas = 0

    __slots__ = ['_num', '_sal', '_tit', '_lim', 'history']
    def __init__(self, numero, titular, saldo, limite = 1000):
        self._num = numero
        self._sal = saldo
        self._tit = titular
        self._lim = limite
        Conta._total_contas += 1
        self.history = Historico()

    @property
    def numeros(self):
        return self._num

    @numeros.setter
    def numeros(self, novo):
        self._num = novo

    @property
    def titularr(self):
        return self._tit

    @titularr.setter
    def titularr(self, novo):
        self._tit = novo

    @property
    def Limite(self):
        return self._lim

    @Limite.setter
    def Limite(self, novo):
        self._lim = novo

    @staticmethod
    def get_totalcontas():
        return Conta._total_contas

    def deposita(self, valor):
        self._sal = self._sal + valor
        self.history.add_transacoes('Deposito de %.2f R$ realizado' %(valor))

    def sacar(self, valor):
        if valor <= self._sal:
            self._sal -= valor
            self.history.add_transacoes('Saque realizado no valor de %.2f R$' % (valor))
            return True
        else:
            return False
    def extrato(self):
        print("- Conta: %s" %(self._num))
        print("- Saldo: %.2f" %(self._sal))
        print()

    def transfere(self, destino, valor):
        retorno = self.sacar(valor)
        if retorno:
            destino.deposita(valor)
            self.history.add_transacoes(f'Transferencia realizada para a conta de numero {destino._num} no valor de %.2f - R$' % (valor))
            destino.history.add_transacoes(f'Transferência recebida da conta de numero {self._num} no valor de %.2f - R$' % (valor))
        else:
            return False

cliente1 = Cliente('Gustavo', 'Araujo', '025.333.111-03')
cliente2 = Cliente("Pedro", 'Ferreira', '123.456.789-10')
cliente3 = Cliente('Jose', 'Alvaro', '222.391.111-00')

c1 = Conta('01', cliente1, 1500)
c2 = Conta('02', cliente2, 15000, 2000)
c3 = Conta('03', cliente3, 17000)

c1.extrato()
c2.extrato()

c1.deposita(52)
c2.sacar(11000)

c1.extrato()
c2.extrato()

retorno = c1.transfere(c2, 1100)
if retorno == False:
    print('Saldo insuficiente\n')

c1.extrato()
c2.extrato()

c1.history.imprimir()
c2.history.imprimir()

print()
print(Conta.get_totalcontas())