from bienvenida import *
from sys import exit, argv

class MiFormulario(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ButtonPulsar.clicked.connect(self.mostrar_mensaje)
        #QtCore.QObject.connect(self.ui.ButtonPulsar, QtCore.SIGNAL('clicked()'), self.mostrar_mensaje)

    def mostrar_mensaje(self):
        self.ui.labelMensaje.setText('Hola '+ self.ui.lineNombreUsuario.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication(argv)
    myapp = MiFormulario()
    myapp.show()
    exit(app.exec_())