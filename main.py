from tela_cadastro import Tela_Cadastro
from tela_login import Tela_Login
from tela_inicial import Tela_Inicial
from Contaa import Conta
from tela_saldo import Tela_Saldo
from tela_deposita import Tela_Deposita
from tela_extrato import Tela_Extrato
from tela_sacar import Tela_Sacar
from tela_transferencia import Tela_Transferencia
from Historico import Historico
from Cliente import Cliente

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QFileDialog

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()

        self.tela_login = Tela_Login()
        self.tela_login.setupUi(self.stack0)

        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_inicial = Tela_Inicial()
        self.tela_inicial.setupUi(self.stack2)

        self.tela_saldo = Tela_Saldo()
        self.tela_saldo.setupUi(self.stack3)

        self.tela_deposita = Tela_Deposita()
        self.tela_deposita.setupUi(self.stack4)

        self.tela_extrato = Tela_Extrato()
        self.tela_extrato.setupUi(self.stack5)

        self.tela_sacar = Tela_Sacar()
        self.tela_sacar.setupUi(self.stack6)

        self.tela_transferencia = Tela_Transferencia()
        self.tela_transferencia.setupUi(self.stack7)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)

objeto = ''
objeto1 = ''

class Main(QMainWindow,Ui_Main):


    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.cad = Conta()
        self.tela_login.pushButton_2.clicked.connect(self.abrirtelacadastro)
        self.tela_login.pushButton.clicked.connect(self.BotaoLogin)
        self.tela_cadastro.pushButton.clicked.connect(self.botaoCadastra)
        self.tela_cadastro.pushButton_2.clicked.connect(self.voltar)
        self.tela_inicial.pushButton.clicked.connect(self.saldo_main)
        self.tela_inicial.pushButton_2.clicked.connect(self.extrato_main)
        self.tela_inicial.pushButton_3.clicked.connect(self.abrir_transferencia)
        self.tela_inicial.pushButton_4.clicked.connect(self.abrir_sacar)
        self.tela_inicial.pushButton_5.clicked.connect(self.abrir_deposita)
        self.tela_inicial.pushButton_6.clicked.connect(self.voltar1)
        self.tela_saldo.pushButton.clicked.connect(self.voltar2)
        self.tela_deposita.pushButton_2.clicked.connect(self.voltar2)
        self.tela_deposita.pushButton_3.clicked.connect(self.deposita_main)
        self.tela_extrato.pushButton_2.clicked.connect(self.voltar2)
        self.tela_sacar.pushButton_2.clicked.connect(self.voltar2)
        self.tela_sacar.pushButton.clicked.connect(self.sacar_main)
        self.tela_transferencia.pushButton_2.clicked.connect(self.voltar2)
        self.tela_transferencia.pushButton.clicked.connect(self.transferencia_main)

    def botaoCadastra(self):
        nome = self.tela_cadastro.lineEdit.text()
        cpf = self.tela_cadastro.lineEdit_2.text()
        usuario = self.tela_cadastro.lineEdit_3.text()
        senha = self.tela_cadastro.lineEdit_4.text()
        senha1 = self.tela_cadastro.lineEdit_9.text()

        if not(nome == '' or cpf == '' or usuario == '' or senha == '' or senha1 == ''):
            if (senha == senha1):
                retorno = self.cad.usuario(usuario)
                if(retorno == None):
                    cliente = Cliente(nome, cpf, usuario, senha)
                    if(self.cad.cadastrar(cliente)):
                        QMessageBox.information(None, 'POOII', 'Conta criada com sucesso!')
                        self.tela_cadastro.lineEdit.setText('')
                        self.tela_cadastro.lineEdit_2.setText('')
                        self.tela_cadastro.lineEdit_3.setText('')
                        self.tela_cadastro.lineEdit_4.setText('')
                        self.tela_cadastro.lineEdit_9.setText('')
                        self.QtStack.setCurrentIndex(0)
                    else:
                        QMessageBox.information(None, 'POOII', 'O CPF informado já esta cadastrado!')
                else:
                    QMessageBox.information(None, 'POOII', 'O Usuario informado já esta cadastrado!')
            else:
                QMessageBox.information(None, 'POOII', 'As senhas são diferentes, digite novamente!')
        else:
            QMessageBox.information(None, 'POOII', 'Todos os campos devem ser preenchidos!')

    def BotaoLogin(self):
        usuario = self.tela_login.lineEdit.text()
        senha = self.tela_login.lineEdit_2.text()
        if not(usuario == '' or senha == ''):
            retorno = self.cad.login(usuario, senha)
            Main.objeto = retorno
            if (retorno != None):
                self.QtStack.setCurrentIndex(2)
            else:
                QMessageBox.information(None, 'POOII', 'Usuário ou senha incorreto!')
        else:
            QMessageBox.information(None, 'POOII', 'Todos os valores devem ser preenchidos!')

    def extrato_main(self):
        self.QtStack.setCurrentIndex(5)
        extrato = ''
        for i in Main.objeto.history.transacoes:
            extrato += str(i)+"\n"
        self.tela_extrato.textBrowser.setText(extrato)

    def deposita_main(self):
        valor = self.tela_deposita.lineEdit.text()
        if not(valor == ''):
            valorr = float(valor)
            Main.objeto._sal += valorr
            QMessageBox.information(None, 'POOII', 'Valor depositado com sucesso!')
            Main.objeto.history.add_transacoes(f'Deposito realizado no valor de {valorr} R$')
            self.tela_deposita.lineEdit.setText('')
            self.QtStack.setCurrentIndex(2)
        else:
            QMessageBox.information(None, 'POOII', 'Digite o valor a ser depositado!')

    def sacar_main(self):
        valor = self.tela_sacar.lineEdit.text()
        if not(valor == ''):
            valorr = float(valor)
            if(Main.objeto._sal >= valorr):
                Main.objeto._sal -= valorr
                QMessageBox.information(None, 'POOII', 'Valor sacado com sucesso!')
                Main.objeto.history.add_transacoes(f'Saque realizado no valor de {valorr} R$')
                self.tela_sacar.lineEdit.setText('')
                self.QtStack.setCurrentIndex(2)
            else:
                QMessageBox.information(None, 'POOII', 'Saldo insuficiente!')
        else:
            QMessageBox.information(None, 'POOII', 'Digite o valor a ser sacado!')

    def transferencia_main(self):
        valor = self.tela_transferencia.lineEdit.text()
        numero = self.tela_transferencia.lineEdit_2.text()
        if not(valor == '' or numero == ''):
            valorr = float(valor)
            numeroo = int(numero)
            retorno = self.cad.numero_conta(numeroo)
            Main.objeto1 = retorno
            if(retorno != None):
                if (Main.objeto._sal >= valorr):
                    Main.objeto._sal -= valorr
                    Main.objeto1._sal += valorr
                    QMessageBox.information(None, 'POOII', 'Transferência realizada com sucesso!')
                    Main.objeto.history.add_transacoes(f'Transferência realizada no valor de {valorr} R$, para a conta de {Main.objeto1.nome}')
                    Main.objeto1.history.add_transacoes(f'Transferência recebida no valor de {valorr} R$, da conta de {Main.objeto.nome}')
                    self.tela_transferencia.lineEdit.setText('')
                    self.tela_transferencia.lineEdit_2.setText('')
                    self.QtStack.setCurrentIndex(2)
                else:
                    QMessageBox.information(None, 'POOII', 'Saldo insuficiente, impossivel realizar a transferencia!')
            else:
                QMessageBox.information(None, 'POOII', 'Não existe uma conta com o numero informado!')
        else:
            QMessageBox.information(None, 'POOII', 'Todos os campos devem ser preenchidos!')

    def abrir_transferencia(self):
        self.QtStack.setCurrentIndex(7)

    def abrir_sacar(self):
        self.QtStack.setCurrentIndex(6)

    def abrir_deposita(self):
        self.QtStack.setCurrentIndex(4)

    def saldo_main(self):
        numero = str(Main.objeto._num)
        saldoo = str(Main.objeto._sal)
        self.tela_saldo.lineEdit.setText(Main.objeto.nome)
        self.tela_saldo.lineEdit_2.setText(Main.objeto.cpf)
        self.tela_saldo.lineEdit_3.setText(numero)
        self.tela_saldo.lineEdit_4.setText(saldoo)
        self.QtStack.setCurrentIndex(3)

    def abrirtelacadastro(self):
        self.QtStack.setCurrentIndex(1)

    def voltar(self):
        self.tela_cadastro.lineEdit.setText('')
        self.tela_cadastro.lineEdit_2.setText('')
        self.tela_cadastro.lineEdit_3.setText('')
        self.tela_cadastro.lineEdit_4.setText('')
        self.tela_cadastro.lineEdit_9.setText('')
        self.QtStack.setCurrentIndex(0)

    def voltar1(self):
        self.tela_login.lineEdit.setText('')
        self.tela_login.lineEdit_2.setText('')
        self.QtStack.setCurrentIndex(0)

    def voltar2(self):
        self.tela_deposita.lineEdit.setText('')
        #self.tela_extrato.lineEdit.setText('')
        self.tela_sacar.lineEdit.setText('')
        self.tela_transferencia.lineEdit.setText('')
        self.tela_transferencia.lineEdit_2.setText('')
        self.QtStack.setCurrentIndex(2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())