# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_configura_porta.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaConfiguraPorta(object):
    def setupUi(self, TelaConfiguraPorta):
        TelaConfiguraPorta.setObjectName("TelaConfiguraPorta")
        TelaConfiguraPorta.setWindowModality(QtCore.Qt.ApplicationModal)
        TelaConfiguraPorta.resize(555, 309)
        self.centralwidget = QtWidgets.QWidget(TelaConfiguraPorta)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setMinimumSize(QtCore.QSize(0, 40))
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(1, 121, 86);\n"
"color: rgb(255, 255, 255);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_14 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_Caminho = QtWidgets.QPushButton(self.widget_3)
        self.btn_Caminho.setMinimumSize(QtCore.QSize(70, 25))
        self.btn_Caminho.setMaximumSize(QtCore.QSize(70, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Caminho.setFont(font)
        self.btn_Caminho.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Caminho.setStyleSheet("background-color: rgb(141, 141, 141);")
        self.btn_Caminho.setObjectName("btn_Caminho")
        self.horizontalLayout.addWidget(self.btn_Caminho)
        self.line_Caminho = QtWidgets.QLineEdit(self.widget_3)
        self.line_Caminho.setMinimumSize(QtCore.QSize(0, 25))
        self.line_Caminho.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_Caminho.setFont(font)
        self.line_Caminho.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Caminho.setObjectName("line_Caminho")
        self.horizontalLayout.addWidget(self.line_Caminho)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.widget)
        self.widget_8 = QtWidgets.QWidget(self.centralwidget)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.widget_8)
        self.label_5.setMinimumSize(QtCore.QSize(60, 0))
        self.label_5.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.widget_2 = QtWidgets.QWidget(self.widget_8)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_3.addWidget(self.label_15)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_11 = QtWidgets.QLabel(self.widget_4)
        self.label_11.setMinimumSize(QtCore.QSize(160, 0))
        self.label_11.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.combo_Portas = QtWidgets.QComboBox(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_Portas.sizePolicy().hasHeightForWidth())
        self.combo_Portas.setSizePolicy(sizePolicy)
        self.combo_Portas.setMinimumSize(QtCore.QSize(100, 25))
        self.combo_Portas.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.combo_Portas.setFont(font)
        self.combo_Portas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.combo_Portas.setObjectName("combo_Portas")
        self.horizontalLayout_2.addWidget(self.combo_Portas)
        self.label = QtWidgets.QLabel(self.widget_4)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.widget_7 = QtWidgets.QWidget(self.widget_2)
        self.widget_7.setStyleSheet("")
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_16 = QtWidgets.QLabel(self.widget_7)
        self.label_16.setMinimumSize(QtCore.QSize(160, 0))
        self.label_16.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_5.addWidget(self.label_16)
        self.combo_Taxa = QtWidgets.QComboBox(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_Taxa.sizePolicy().hasHeightForWidth())
        self.combo_Taxa.setSizePolicy(sizePolicy)
        self.combo_Taxa.setMinimumSize(QtCore.QSize(100, 25))
        self.combo_Taxa.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.combo_Taxa.setFont(font)
        self.combo_Taxa.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.combo_Taxa.setObjectName("combo_Taxa")
        self.horizontalLayout_5.addWidget(self.combo_Taxa)
        self.label_4 = QtWidgets.QLabel(self.widget_7)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.verticalLayout_3.addWidget(self.widget_7)
        self.widget_6 = QtWidgets.QWidget(self.widget_2)
        self.widget_6.setStyleSheet("")
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.widget_6)
        self.label_12.setMinimumSize(QtCore.QSize(160, 0))
        self.label_12.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.line_bytes = QtWidgets.QLineEdit(self.widget_6)
        self.line_bytes.setMinimumSize(QtCore.QSize(100, 25))
        self.line_bytes.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_bytes.setFont(font)
        self.line_bytes.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.line_bytes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_bytes.setAlignment(QtCore.Qt.AlignCenter)
        self.line_bytes.setObjectName("line_bytes")
        self.horizontalLayout_4.addWidget(self.line_bytes)
        self.label_3 = QtWidgets.QLabel(self.widget_6)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.verticalLayout_3.addWidget(self.widget_6)
        self.horizontalLayout_6.addWidget(self.widget_2)
        self.widget_9 = QtWidgets.QWidget(self.widget_8)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget_9)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.btn_Salvar = QtWidgets.QPushButton(self.widget_9)
        self.btn_Salvar.setMinimumSize(QtCore.QSize(80, 35))
        self.btn_Salvar.setMaximumSize(QtCore.QSize(80, 35))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Salvar.setFont(font)
        self.btn_Salvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Salvar.setStyleSheet("background-color: rgb(141, 141, 141);")
        self.btn_Salvar.setObjectName("btn_Salvar")
        self.verticalLayout_4.addWidget(self.btn_Salvar)
        self.horizontalLayout_6.addWidget(self.widget_9)
        self.verticalLayout.addWidget(self.widget_8)
        TelaConfiguraPorta.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaConfiguraPorta)
        QtCore.QMetaObject.connectSlotsByName(TelaConfiguraPorta)

    def retranslateUi(self, TelaConfiguraPorta):
        _translate = QtCore.QCoreApplication.translate
        TelaConfiguraPorta.setWindowTitle(_translate("TelaConfiguraPorta", "Configurações"))
        self.label_13.setText(_translate("TelaConfiguraPorta", "Configurações"))
        self.label_14.setText(_translate("TelaConfiguraPorta", "Definir caminho do arquivo \"txt\" com o peso da bobina:"))
        self.btn_Caminho.setText(_translate("TelaConfiguraPorta", "Caminho"))
        self.label_15.setText(_translate("TelaConfiguraPorta", "Definir parâmetros de comunicação:"))
        self.label_11.setText(_translate("TelaConfiguraPorta", "Porta Serial (COM):"))
        self.label_16.setText(_translate("TelaConfiguraPorta", "Taxa Transmissão (bps):"))
        self.label_12.setText(_translate("TelaConfiguraPorta", "Número de Bytes:"))
        self.btn_Salvar.setText(_translate("TelaConfiguraPorta", "Testar\n"
"e Salvar"))
