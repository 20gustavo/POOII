from Cliente import Cliente
from Contaa import Conta

if __name__ == '__main__':
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