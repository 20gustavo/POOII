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