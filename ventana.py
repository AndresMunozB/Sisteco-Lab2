from ventana_ui import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.buttonEncriptar.clicked.connect(self.encriptar)
        self.buttonDesencriptar.clicked.connect(self.desencriptar)
    def encriptar(self):
        text = self.textDesencriptado.toPlainText(); 
        self.textEncriptado.setPlainText(self.jad.encrypt(text,"holacomo",8))
    def desencriptar(self):
        text = self.textEncriptado.toPlainText(); 
        self.textDesencriptado.setPlainText(self.jad.decrypt(text,"holacomo",8))
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()