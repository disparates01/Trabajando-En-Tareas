from disenho_gui import *
from sys import exit, argv

class MiFormulario(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(argv)
    myapp = MiFormulario()
    myapp.show()
    exit(app.exec_())