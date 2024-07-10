import sys
from tela_balanca import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import os
import serial.tools.list_ports
import inspect
import traceback
from datetime import datetime
import re


def transforma_string_virgula(string):
    try:
        if "R$ " in string:
            limpa_string = string.replace("R$ ", '')
        elif "%" in string:
            limpa_string = string.replace("%", '')
        else:
            limpa_string = string

        if limpa_string:
            if "." in limpa_string:
                string_com_virgula = limpa_string.replace('.', ',')
            else:
                string_com_virgula = limpa_string
        else:
            string_com_virgula = "0,00"

        return string_com_virgula

    except Exception as e:
        print(e)


def transforma_em_float(string):
    try:
        string_certo = str(string)

        if "R$ " in string_certo:
            limpa_string = string_certo.replace("R$ ", '')
        elif "%" in string_certo:
            limpa_string = string_certo.replace("%", '')
        else:
            limpa_string = string_certo

        if limpa_string:
            if "," in limpa_string:
                string_com_ponto = limpa_string.replace(',', '.')
                valor_float = float(string_com_ponto)
            else:
                valor_float = float(limpa_string)
        else:
            valor_float = 0.00

        return valor_float

    except Exception as e:
        print(e)


class TelaInicio(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowIcon(QtGui.QIcon(r'imagens\pacifil.jpg'))

        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        self.nome_arquivo = os.path.basename(nome_arquivo_com_caminho)

        self.btn_Salvar_Txt1.clicked.connect(self.salvar_txt1)
        self.btn_Salvar_Txt2.clicked.connect(self.salvar_txt2)
        self.btn_Peso_Canudo1.clicked.connect(self.ler_canudo1)
        self.btn_Peso_Canudo2.clicked.connect(self.ler_canudo2)
        self.btn_Peso_Bobina1.clicked.connect(self.ler_bobina1)
        self.btn_Peso_Bobina2.clicked.connect(self.ler_bobina2)

        self.btn_Limpar1.clicked.connect(self.limpar_tudo1)
        self.btn_Limpar2.clicked.connect(self.limpar_tudo2)

        self.btn_Configura.clicked.connect(self.abrir_tela_config)

        self.tela_config = []
        self.conectou = False

        config_txt = 'config.txt'
        caminho = './'
        self.caminho_config_txt = os.path.join(caminho, config_txt)

        self.producao_bob1 = False
        self.producao_bob2 = False

        self.ver_se_txt_existe()

    def abrir_tela_config(self):
        try:
            self.chama_tela_configuracao(self.conectou)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def chama_tela_configuracao(self, conectou):
        try:
            from configuracao import TelaConfiguracao

            self.tela_config = TelaConfiguracao(conectou)
            self.tela_config.produto_escolhido.connect(self.recebe_conexao)
            self.tela_config.show()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def recebe_conexao(self, conectou):
        try:
            if conectou:
                self.label_msg.setStyleSheet("color: green;")
                self.label_msg.setText("Balança conectada!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

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
            self.mensagem_alerta(f'Houve um problema no arquivo: {arquivo} na função: "{nome_funcao}":\n{mensagem}')

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def ler_txt_config(self):
        try:
            with open(self.caminho_config_txt, 'r') as arquivo:
                linhas = arquivo.readlines()
                linhas = [linha.strip() for linha in linhas]

                caminho_peso = linhas[0][9:]
                porta_com = linhas[1][7:]
                bytes_b = linhas[2][7:]
                taxa = linhas[3][6:]

                return caminho_peso, porta_com, bytes_b, taxa

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def ver_se_txt_existe(self):
        try:
            if not os.path.exists(self.caminho_config_txt):
                msg1 = 'O programa de pesagem não está configurado.\n'
                msg1 += 'Pressione o botão "Configurações" para concluir esta etapa!'
                msg2 = 'O programa de pesagem não está configurado!'
                self.label_msg.setStyleSheet("color: red;")
                self.label_msg.setText(msg2)
                self.mensagem_alerta(msg1)

                self.btn_Configura.setFocus()
            else:
                self.testar_conexao_porta()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def testar_conexao_porta(self):
        try:
            caminho_peso, porta_com, bytes_b, taxa = self.ler_txt_config()

            try:
                if caminho_peso and porta_com and bytes_b and taxa:
                    num_bytes = int(bytes_b)
                    taxa_trans = int(taxa)

                    ser = serial.Serial(porta_com, taxa_trans, timeout=2)

                    s = ser.read(num_bytes)

                    if s:
                        self.label_msg.setStyleSheet("color: green;")
                        self.label_msg.setText("Balança conectada!")

                        ser.close()

                    else:
                        msg = f'Não foi possivel estabelecer uma comunicação com a balança ' \
                              f'através da porta "{porta_com}"!'

                        self.mensagem_alerta(msg)
                        self.label_msg.setStyleSheet("color: red;")
                        self.label_msg.setText(msg)
                        self.btn_Configura.setFocus()

                        ser.close()

                else:
                    msg1 = 'O programa de pesagem não está configurado.\n'
                    msg1 += 'Pressione o botão "Configurações" para concluir esta etapa!'
                    msg2 = 'O programa de pesagem não está configurado!'
                    self.label_msg.setStyleSheet("color: red;")
                    self.label_msg.setText(msg2)
                    self.mensagem_alerta(msg1)

                    self.btn_Configura.setFocus()

            except serial.SerialException as e:
                if "FileNotFoundError(2, 'O sistema não pode encontrar o arquivo especificado.'" in str(e):
                    self.mensagem_alerta(f'Não foi possível conectar a porta "{porta_com}". '
                                         f'Verifique se a porta está correta e se o dispositivo está conectado.')
                else:
                    self.mensagem_alerta(f'A porta "{porta_com}" não foi encontrada!\n\n- {e}')

                self.label_msg.setStyleSheet("color: red;")
                self.label_msg.setText(f'A porta "{porta_com}" não foi encontrada!')
                self.btn_Configura.setFocus()

                nome_funcao = inspect.currentframe().f_code.co_name
                self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def salvar_txt1(self):
        try:
            if not os.path.exists(self.caminho_config_txt):
                msg1 = 'O programa de pesagem não está configurado.\n'
                msg1 += 'Pressione o botão "Configurações" para concluir esta etapa!'
                msg2 = 'O programa de pesagem não está configurado!'
                self.label_msg.setStyleSheet("color: red;")
                self.label_msg.setText(msg2)
                self.mensagem_alerta(msg1)

                self.btn_Configura.setFocus()
            else:
                peso = self.line_Liquido1.text()

                if peso:
                    peso_float = transforma_em_float(peso)

                    if peso_float > 0:
                        caminho_peso, porta_com, bytes_b, taxa = self.ler_txt_config()

                        if caminho_peso:
                            with open(caminho_peso, 'w') as arquivo1:
                                peso_virgula = transforma_string_virgula(peso)
                                arquivo1.write(peso_virgula)

                                self.mensagem_alerta("Peso da Bobina 1 salvo com sucesso!")

                        self.limpar_tudo1()

                        peso_canudo2 = self.line_Canudo2.text()
                        if not peso_canudo2:
                            self.widget_Verde1.setStyleSheet("background-color: rgb(182, 182, 182);")
                            self.widget_Verde2.setStyleSheet("background-color: rgb(182, 182, 182);")

                            self.label_Titulo1.setText("Aguardando Peso")

                            self.producao_bob1 = False
                            self.producao_bob2 = False
                        else:
                            self.widget_Verde1.setStyleSheet("background-color: rgb(182, 182, 182);")
                            self.widget_Verde2.setStyleSheet("background-color: green;")

                            self.label_Titulo1.setText("Aguardando Peso")

                            self.producao_bob1 = False
                            self.producao_bob2 = True

                    else:
                        self.mensagem_alerta("O peso deve ser maior que zero!!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def salvar_txt2(self):
        try:
            if not os.path.exists(self.caminho_config_txt):
                msg1 = 'O programa de pesagem não está configurado.\n'
                msg1 += 'Pressione o botão "Configurações" para concluir esta etapa!'
                msg2 = 'O programa de pesagem não está configurado!'
                self.label_msg.setStyleSheet("color: red;")
                self.label_msg.setText(msg2)
                self.mensagem_alerta(msg1)

                self.btn_Configura.setFocus()
            else:
                peso = self.line_Liquido2.text()

                if peso:
                    peso_float = transforma_em_float(peso)

                    if peso_float > 0:
                        caminho_peso, porta_com, bytes_b, taxa = self.ler_txt_config()

                        if caminho_peso:
                            with open(caminho_peso, 'w') as arquivo1:
                                peso_virgula = transforma_string_virgula(peso)
                                arquivo1.write(peso_virgula)

                                self.mensagem_alerta("Peso da Bobina 2 salvo com sucesso!")

                        self.limpar_tudo2()

                        peso_canudo1 = self.line_Canudo1.text()
                        if not peso_canudo1:
                            self.widget_Verde1.setStyleSheet("background-color: rgb(182, 182, 182);")
                            self.widget_Verde2.setStyleSheet("background-color: rgb(182, 182, 182);")

                            self.label_Titulo2.setText("Aguardando Peso")

                            self.producao_bob1 = False
                            self.producao_bob2 = False
                        else:
                            self.widget_Verde1.setStyleSheet("background-color: green;")
                            self.widget_Verde2.setStyleSheet("background-color: rgb(182, 182, 182);")

                            self.label_Titulo2.setText("Aguardando Peso")

                            self.producao_bob1 = True
                            self.producao_bob2 = False

                    else:
                        self.mensagem_alerta("O peso deve ser maior que zero!!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def ler_peso_balanca(self):
        caminho_peso, porta_com, bytes_b, taxa = self.ler_txt_config()
        try:
            if not os.path.exists(self.caminho_config_txt):
                msg1 = 'O programa de pesagem não está configurado.\n'
                msg1 += 'Pressione o botão "Configurações" para concluir esta etapa!'
                msg2 = 'O programa de pesagem não está configurado!'
                self.label_msg.setStyleSheet("color: red;")
                self.label_msg.setText(msg2)
                self.mensagem_alerta(msg1)

                self.btn_Configura.setFocus()
            else:
                try:
                    if caminho_peso and porta_com and bytes_b and taxa:
                        num_bytes = int(bytes_b)
                        taxa_trans = int(taxa)

                        ser = serial.Serial(porta_com, taxa_trans, timeout=2)

                        leitura_serial = ser.read(num_bytes)
                        if leitura_serial:
                            peso_inicial = leitura_serial.decode().strip()

                            padrao = re.compile(r'\d+\.\d+')

                            peso_final1 = padrao.findall(str(peso_inicial))
                            if peso_final1:
                                peso_final_float = float(peso_final1[0])
                                peso_final = str(peso_final_float)

                                ser.close()

                                return peso_final
                            else:
                                self.mensagem_alerta(f"Formato de peso inválido recebido da balança: {peso_inicial}")
                                ser.close()

                                peso_final = ""

                            return peso_final

                        else:
                            self.mensagem_alerta("Nenhum dado recebido. Fechando a porta serial.")
                            ser.close()

                except serial.SerialException as e:
                    if "FileNotFoundError(2, 'O sistema não pode encontrar o arquivo especificado.'" in str(e):
                        self.mensagem_alerta(f'Não foi possível conectar a porta "{porta_com}". '
                                             f'Verifique se a porta está correta e se o dispositivo está conectado.')
                    else:
                        self.mensagem_alerta(f'A porta "{porta_com}" não foi encontrada!\n\n- {e}')

                    self.label_msg.setStyleSheet("color: red;")
                    self.label_msg.setText(f'A porta "{porta_com}" não foi encontrada!')
                    self.btn_Configura.setFocus()

                    nome_funcao = inspect.currentframe().f_code.co_name
                    self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def ler_canudo1(self):
        try:
            peso_final = self.ler_peso_balanca()
            if peso_final:
                peso_virgula = transforma_string_virgula(peso_final)
                self.line_Canudo1.setText(peso_virgula)

                peso_canudo2 = self.line_Canudo2.text()
                if not peso_canudo2:
                    self.widget_Verde1.setStyleSheet("background-color: green;")
                    self.widget_Verde2.setStyleSheet("background-color: rgb(182, 182, 182);")

                    self.producao_bob1 = True
                    self.producao_bob2 = False

                self.label_Titulo1.setText("Aguardando Peso Bobina")

                self.calcular_peso_liquido1()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def ler_canudo2(self):
        try:
            peso_final = self.ler_peso_balanca()
            if peso_final:
                peso_virgula = transforma_string_virgula(peso_final)
                self.line_Canudo2.setText(peso_virgula)

                peso_canudo1 = self.line_Canudo1.text()
                if not peso_canudo1:
                    self.widget_Verde1.setStyleSheet("background-color: rgb(182, 182, 182);")
                    self.widget_Verde2.setStyleSheet("background-color: green;")

                    self.producao_bob1 = False
                    self.producao_bob2 = True

                self.label_Titulo2.setText("Aguardando Peso Bobina")

                self.calcular_peso_liquido2()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def ler_bobina1(self):
        try:
            if self.producao_bob1:
                peso_canudo1 = self.line_Canudo1.text()
                if peso_canudo1:
                    peso_final = self.ler_peso_balanca()
                    if peso_final:
                        peso_virgula = transforma_string_virgula(peso_final)
                        self.line_Bobina1.setText(peso_virgula)

                    self.label_Titulo1.setText("Aguardando Salvar Peso")

                    self.calcular_peso_liquido1()
                else:
                    self.mensagem_alerta("Primeiro deve ser lançado o peso do canudo!")
            else:
                self.mensagem_alerta("Primeiro deve ser lançado o peso da bobina que está em produção!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def ler_bobina2(self):
        try:
            if self.producao_bob2:
                peso_canudo2 = self.line_Canudo2.text()
                if peso_canudo2:
                    peso_final = self.ler_peso_balanca()
                    if peso_final:
                        peso_virgula = transforma_string_virgula(peso_final)
                        self.line_Bobina2.setText(peso_virgula)

                    self.label_Titulo2.setText("Aguardando Salvar Peso")

                    self.calcular_peso_liquido2()
                else:
                    self.mensagem_alerta("Primeiro deve ser lançado o peso do canudo!")

            else:
                self.mensagem_alerta("Primeiro deve ser lançado o peso da bobina que está em produção!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def calcular_peso_liquido1(self):
        try:
            canudo = self.line_Canudo1.text()
            bobina = self.line_Bobina1.text()

            if canudo and bobina:
                canudo_float = transforma_em_float(canudo)
                bobina_float = transforma_em_float(bobina)

                peso_liquido = "%.2f" % (bobina_float - canudo_float)
                peso_liq_str = str(peso_liquido)
                peso_virgula = transforma_string_virgula(peso_liq_str)
                self.line_Liquido1.setText(peso_virgula)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def calcular_peso_liquido2(self):
        try:
            canudo = self.line_Canudo2.text()
            bobina = self.line_Bobina2.text()

            if canudo and bobina:
                canudo_float = transforma_em_float(canudo)
                bobina_float = transforma_em_float(bobina)

                peso_liquido = "%.2f" % (bobina_float - canudo_float)
                peso_liq_str = str(peso_liquido)
                peso_virgula = transforma_string_virgula(peso_liq_str)
                self.line_Liquido2.setText(peso_virgula)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def limpar_tudo1(self):
        try:
            self.line_Canudo1.clear()
            self.line_Bobina1.clear()
            self.line_Liquido1.clear()

            self.producao_bob1 = False

            self.label_Titulo1.setText("Aguardando Peso")

            self.widget_Verde1.setStyleSheet("background-color: rgb(182, 182, 182);")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)

    def limpar_tudo2(self):
        try:
            self.line_Canudo2.clear()
            self.line_Bobina2.clear()
            self.line_Liquido2.clear()

            self.producao_bob2 = False

            self.label_Titulo2.setText("Aguardando Peso")

            self.widget_Verde2.setStyleSheet("background-color: rgb(182, 182, 182);")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            self.trata_excecao(nome_funcao, e, self.nome_arquivo)
            self.grava_erro_banco(nome_funcao, e, self.nome_arquivo)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    opinclui = TelaInicio()
    opinclui.show()
    qt.exec_()
