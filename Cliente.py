from Historico import Historico
class Cliente:

    __slots__ = ['_name', '_usuario', '_cpf', '_senha', '_sal', '_num', 'history']
    def __init__(self, nome, cpf, usuario, senha):
        self._name = nome
        self._cpf = cpf
        self._usuario = usuario
        self._senha = senha
        self._sal = 0
        self.history = Historico()
        self._num = 0

    @property
    def nome(self):
        return self._name

    @nome.setter
    def nome(self, novo):
        self._name = novo

    @property
    def cpf(self):
        return self._cpf

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, novo):
        self._usuario = novo

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, novo):
        self._senha = novo