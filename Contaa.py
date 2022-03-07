from Historico import Historico
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