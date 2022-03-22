class Conta:

    _total_contas = 0

    __slots__ = ['_num', '_sal', '_tit', 'history', '_lista_pessoas']
    def __init__(self):
        self._lista_pessoas = []

    def cadastrar(self, titular):
        existe = self.busca(titular.cpf)
        if (existe == None):
            Conta._total_contas += 1
            titular._num = Conta._total_contas
            self._lista_pessoas.append(titular)
            return True
        else:
            return False

    def busca(self, cpf):
        for lp in self._lista_pessoas:
            if lp.cpf == cpf:
                return lp
        return None

    def login(self, usuario, senha):
        for lg in self._lista_pessoas:
            if(lg.usuario == usuario and lg.senha == senha):
                return lg
        return None

    def usuario(self, usuario):
        for lu in self._lista_pessoas:
            if(lu.usuario == usuario):
                return lu
        return None

    def numero_conta(self, numero):
        for lu in self._lista_pessoas:
            if(lu._num == numero):
                return lu
        return None


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