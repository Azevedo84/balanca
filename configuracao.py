import sys
from tela_configura_porta import *
from PyQt5.QtWidgets import QMainWindow,  QApplication, QMessageBox, QFileDialog
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIntValidator, QIcon
import serial.tools.list_ports
import traceback
import inspect
import os
from datetime import datetime


class TelaConfiguracao(QMainWindow, Ui_TelaConfiguraPorta):
    produto_escolhido = pyqtSignal(bool)

    def __init__(self, conectou, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowIcon(QIcon("pacifil.jpg"))

        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        self.conectou = conectou

        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint & ~Qt.WindowMaximizeButtonHint)

        self.caminho_config = 'config.txt'
        caminho = './'
        self.caminho_completo_config = os.path.join(caminho, self.caminho_config)

        int_validator = QIntValidator()
        self.line_bytes.setValidator(int_validator)

        self.btn_Caminho.clicked.connect(self.definir_caminho)
        self.btn_Salvar.clicked.connect(self.verifica_salvamento)

        self.definir_combo_porta()
        self.definir_combo_taxa()

        if os.path.exists(self.caminho_completo_config):
            self.ler_txt_definido()

    def mensagem_alerta(self, mensagem):
        try:
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Warning)
            alert.setText(mensagem)
            alert.setWindowTitle("Atenção")
            alert.setStandardButtons(QMessageBox.Ok)
            alert.exec_()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def grava_erro_banco(self, nome_funcao, e, nome_arquivo):
        try:
            hora_atual = datetime.now()

            hora_formatada = hora_atual.strftime("%d/%m/%Y %H:%M:%S")

            msg_editada = str(e).replace("'", "")
            msg_editada1 = msg_editada.replace('"', ' ')
            msg_editada2 = msg_editada1.replace('\\', '  ')
            dados = f"{hora_formatada}\n" \
                    f"- Nome Arquivo: {nome_arquivo}\n" \
                    f"- Nome Função: {nome_funcao}\n" \
                    f"- Erro: {msg_editada2}"
            with open('log_erro.txt', 'w') as arquivo:
                arquivo.write(dados)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def trata_excecao(self, nome_funcao, mensagem, arquivo):
        try:
            traceback.print_exc()
            print(f'Houve um problema no arquivo: {arquivo} na função: "{nome_funcao}":\n{mensagem}')
            self.mensagem_alerta(f'Houve um problema no arquivo: {arquivo} na função: "{nome_funcao}":\n{mensagem}')

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def definir_combo_porta(self):
        lista = ["", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "COM10"]

        self.combo_Portas.addItems(lista)

    def definir_combo_taxa(self):
        lista = ["", "110", "300", "1200", "2400", "4800", "9600", "14400", "19200", "38400", "57600", "115200"]

        self.combo_Taxa.addItems(lista)

    def ler_txt_definido(self):
        try:
            with open(self.caminho_completo_config, 'r') as arquivo:
                linhas = arquivo.readlines()
                linhas = [linha.strip() for linha in linhas]

                caminho_peso = linhas[0][9:]
                self.line_Caminho.setText(caminho_peso)

                porta = linhas[1][7:]
                porta_count = self.combo_Portas.count()
                for porta_ in range(porta_count):
                    porta_text = self.combo_Portas.itemText(porta_)
                    if porta == porta_text:
                        self.combo_Portas.setCurrentText(porta_text)

                bytes_b = linhas[2][7:]
                self.line_bytes.setText(bytes_b)

                taxa = linhas[3][6:]
                taxa_count = self.combo_Taxa.count()
                for taxa_ in range(taxa_count):
                    taxa_text = self.combo_Taxa.itemText(taxa_)
                    if taxa == taxa_text:
                        self.combo_Taxa.setCurrentText(taxa_text)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def definir_caminho(self):
        try:
            file_name, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo", "peso.txt",
                                                       "Arquivos de Texto (*.txt);;Todos os Arquivos (*)")
            self.line_Caminho.setText(file_name)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def verifica_salvamento(self):
        try:
            porta = self.combo_Portas.currentText()
            caminho = self.line_Caminho.text()
            bytes_b = self.line_bytes.text()
            taxa = self.combo_Taxa.currentText()

            if not caminho:
                self.mensagem_alerta("Defina o caminho do arquivo txt com o peso da bobina!")
            elif not porta:
                self.mensagem_alerta("Defina a porta de comunicação!")
            elif not bytes_b:
                self.mensagem_alerta("Defina o tamanho de bytes!")
            elif not taxa:
                self.mensagem_alerta("Defina a taxa de transmissão!")
            else:
                self.testar_conexao_porta(porta, bytes_b, taxa)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def testar_conexao_porta(self, porta_com, bytes_b, taxa_trans):
        try:
            try:
                taxa_int = int(taxa_trans)
                bytes_m_int = int(bytes_b)

                ser = serial.Serial(porta_com, taxa_int, timeout=2)

                s = ser.read(bytes_m_int)

                if s:
                    self.mensagem_alerta("Conexão com a balança estabelecida com sucesso!")
                    self.salvar_dados()

                    self.conectou = True

                    ser.close()
                else:
                    self.mensagem_alerta(f'Não foi possivel estabelecer uma comunicação com a balança '
                                         f'através da porta "{porta_com}"!')

                    self.conectou = True

                    ser.close()

                self.produto_escolhido.emit(self.conectou)
                self.close()

            except serial.SerialException as e:
                if "FileNotFoundError(2, 'O sistema não pode encontrar o arquivo especificado.'" in str(e):
                    self.mensagem_alerta(f'Não foi possível conectar a porta "{porta_com}". '
                                         f'Verifique se a porta está correta e se o dispositivo está conectado.')
                else:
                    self.mensagem_alerta(f'A porta "{porta_com}" não foi encontrada!\n\n- {e}')

                self.produto_escolhido.emit(self.conectou)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def salvar_dados(self):
        try:
            porta = self.combo_Portas.currentText()
            caminho = self.line_Caminho.text()
            bytes_b = self.line_bytes.text()
            taxa = self.combo_Taxa.currentText()

            with open(self.caminho_config, 'w') as arquivo:
                arquivo.write(f"Caminho: {caminho}\n"
                              f"Porta: {porta}\n"
                              f"Bytes: {bytes_b}\n"
                              f"Taxa: {taxa}")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    opinclui = TelaConfiguracao(False)
    opinclui.show()
    qt.exec_()
