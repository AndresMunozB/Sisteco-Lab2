# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 512)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textClave = QtWidgets.QLineEdit(self.centralwidget)
        self.textClave.setGeometry(QtCore.QRect(250, 20, 113, 23))
        self.textClave.setObjectName("textClave")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 20, 41, 16))
        self.label.setObjectName("label")
        self.spinTamanio = QtWidgets.QSpinBox(self.centralwidget)
        self.spinTamanio.setGeometry(QtCore.QRect(540, 20, 47, 24))
        self.spinTamanio.setObjectName("spinTamanio")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 20, 121, 16))
        self.label_2.setObjectName("label_2")
        self.buttonEncriptar = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEncriptar.setGeometry(QtCore.QRect(160, 420, 80, 23))
        self.buttonEncriptar.setObjectName("buttonEncriptar")
        self.buttonDesencriptar = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDesencriptar.setGeometry(QtCore.QRect(560, 420, 80, 23))
        self.buttonDesencriptar.setObjectName("buttonDesencriptar")
        self.textDesencriptado = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textDesencriptado.setGeometry(QtCore.QRect(63, 99, 271, 301))
        self.textDesencriptado.setObjectName("textDesencriptado")
        self.textEncriptado = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEncriptado.setGeometry(QtCore.QRect(450, 100, 271, 301))
        self.textEncriptado.setPlainText("")
        self.textEncriptado.setObjectName("textEncriptado")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Clave"))
        self.label_2.setText(_translate("MainWindow", "Tamaño del bloque"))
        self.buttonEncriptar.setText(_translate("MainWindow", "Encriptar"))
        self.buttonDesencriptar.setText(_translate("MainWindow", "Desencriptar"))
        self.textDesencriptado.setPlainText(_translate("MainWindow", "asdfasdf"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

