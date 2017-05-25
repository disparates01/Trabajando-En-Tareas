# from T05_GUI import *

from PyQt5 import QtTest
from PyQt5.QtCore import QThread, QThreadPool, QTime
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import QtWidgets # revisar:
from logging import getLogger, DEBUG, WARNING, ERROR, INFO
from loggers import archivo_logs, stream_handler, file_handler

# ------------------------------------------------------------------------------------------------------------- LOGGERS
archivo_logs()
info = getLogger('INFO [{}'.format(__name__))
info.setLevel(INFO)
info.addHandler(stream_handler)
info.addHandler(file_handler)
debug = getLogger('DEBUG [{}'.format(__name__))
debug.setLevel(DEBUG)
debug.addHandler(file_handler)
warning = getLogger('WARNING [{}'.format(__name__))
warning.setLevel(WARNING)
warning.addHandler(file_handler)
error = getLogger('ERROR [{}'.format(__name__))
error.setLevel(ERROR)
error.addHandler(file_handler)
# ------------------------------------------------------------------------------------------------------------- * * *

class Juego(QThread, QtWidgets.QDialog):
    def __init__(self, tamanho, objetos):
        self.tamanho = tamanho
        self.objetos = objetos
        # self.ui = T05_GUI()
        self.ui.setupUi(self)

    warning.warning('Sacado del tetris. REVISAR Y MODIFICAR')
    def keyPressEvent(self, event):
        # if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape:
        #     super(Board, self).keyPressEvent(event)
        #     return
        key = event.key()
        if key == Qt.Key_P:
            self.pause()
            return
        if self.isPaused:
            return
        elif key == Qt.Key_W:
            pass
            # self.tryMove(self.curPiece, self.curX - 1, self.curY)
        elif key == Qt.Key_A:
            pass
            # self.tryMove(self.curPiece, self.curX + 1, self.curY)
        elif key == Qt.Key_S:
            pass
            # self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)
        elif key == Qt.Key_D:
            pass
            # self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)
        else:
            pass
            # super(Board, self).keyPressEvent(event)

    warning.warning('Completar')
    def checkear_colision(self, unidad):
        for objeto in self.objetos:
            pass

    warning.warning('Completar')
    def checkear_rango(self):
        pass

if __name__ == '__main__':
    pass
    # app = QtWidgets.QApplication(argv)
    # myapp = Juego()
    # myapp.show()
    # exit(app.exec_())
