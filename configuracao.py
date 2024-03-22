import sys
from tela_configura_porta import *
from PyQt5.QtWidgets import QMainWindow,  QApplication, QMessageBox, QFileDialog
from PyQt5.QtCore import pyqtSignal, Qt
import serial.tools.list_ports
import traceback
import inspect
import os


def mensagem_alerta(mensagem):
    alert = QMessageBox()
    alert.setIcon(QMessageBox.Warning)
    alert.setText(mensagem)
    alert.setWindowTitle("Atenção")
    alert.setStandardButtons(QMessageBox.Ok)
    alert.exec_()


def grava_erro_banco(nome_funcao, e, nome_arquivo):
    msg_editada = str(e).replace("'", "")
    msg_editada1 = msg_editada.replace('"', ' ')
    msg_editada2 = msg_editada1.replace('\\', '  ')
    dados = f"'{nome_arquivo}', '{nome_funcao}', '{msg_editada2}'"
    mensagem_alerta(dados)


def trata_excecao(nome_funcao, mensagem, arquivo):
    try:
        traceback.print_exc()
        print(f'Houve um problema no arquivo: {arquivo} na função: "{nome_funcao}":\n{mensagem}')
        mensagem_alerta(f'Houve um problema no arquivo: {arquivo} na função: "{nome_funcao}":\n{mensagem}')

    except Exception as e:
        print(e)


class TelaConfiguraPorta(QMainWindow, Ui_TelaConfiguraPorta):
    closed = pyqtSignal(object)

    def __init__(self, funcao_tela_principal, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint & ~Qt.WindowMaximizeButtonHint)

        self.funcao_tela_principal = funcao_tela_principal

        self.caminho_config = 'config.txt'
        caminho = './'
        self.caminho_completo_config = os.path.join(caminho, self.caminho_config)

        self.btn_Caminho.clicked.connect(self.definir_caminho)
        self.btn_Salvar.clicked.connect(self.verifica_salvamento)

        self.listar_portas_disponiveis()

        if os.path.exists(self.caminho_completo_config):
            self.ler_txt_definido()

    def listar_portas_disponiveis(self):
        lista = ["", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "COM10"]

        self.combo_Portas.addItems(lista)

    def ler_txt_definido(self):
        with open(self.caminho_completo_config, 'r') as arquivo:
            linhas = arquivo.readlines()

            fim = linhas[0].find("\n")
            porta = linhas[0][7:fim]

            porta_count = self.combo_Portas.count()
            for porta_ in range(porta_count):
                porta_text = self.combo_Portas.itemText(porta_)
                if porta == porta_text:
                    self.combo_Portas.setCurrentText(porta_text)

            caminho_peso = linhas[1][9:]
            self.line_Caminho.setText(caminho_peso)

    def definir_caminho(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo", "peso.txt",
                                                   "Arquivos de Texto (*.txt);;Todos os Arquivos (*)")
        self.line_Caminho.setText(file_name)

    def verifica_salvamento(self):
        porta = self.combo_Portas.currentText()
        caminho = self.line_Caminho.text()

        if not caminho:
            mensagem_alerta("Defina o caminho do arquivo txt com o peso da bobina!")
        elif not porta:
            mensagem_alerta("Defina a porta de comunicação!")
        else:
            self.testar_conexao_porta(porta)

    def testar_conexao_porta(self, porta_com):
        try:
            try:
                ser = serial.Serial(porta_com, 9600, timeout=1)

                s = ser.read(8)

                if s:
                    mensagem_alerta("Conexão com a balança estabelecida com sucesso!")
                    self.salvar_dados()
                    ser.close()
                    self.close()
                else:
                    mensagem_alerta(f'Não foi possivel estabelecer uma comunicação com a balança\n'
                                    f'através da porta "{porta_com}"!')
                    ser.close()

            except serial.SerialException as e:
                print(f'A porta "{porta_com}" não foi encontrada!\n\n- {e}')
                mensagem_alerta(f'A porta "{porta_com}" não foi encontrada!\n\n- {e}')

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, e, nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def salvar_dados(self):
        try:
            porta = self.combo_Portas.currentText()
            caminho = self.line_Caminho.text()

            with open(self.caminho_config, 'w') as arquivo:
                arquivo.write(f"Porta: {porta}\nCaminho: {caminho}")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, e, nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def closeEvent(self, event):
        if event:
            self.closed.emit(self.executar_na_tela_principal)
        super().closeEvent(event)

    def executar_na_tela_principal(self):
        self.funcao_tela_principal()
        self.close()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    opinclui = TelaConfiguraPorta("")
    opinclui.show()
    qt.exec_()
