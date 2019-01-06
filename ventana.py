from ventana_ui import *
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.buttonEncriptar.clicked.connect(self.actualizar)
    def actualizar(self):
        text = self.textDesencriptado.toPlainText(); 
        self.textEncriptado.setPlainText(text)
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()