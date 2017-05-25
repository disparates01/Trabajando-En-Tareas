# from T05_GUI import *

from PyQt5 import QtTest
from PyQt5.QtCore import QThread, QThreadPool, QTime
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import QtWidgets # revisar:
from logging import getLogger, DEBUG, WARNING, ERROR, INFO, StreamHandler, Formatter

logger = getLogger(__name__)
logger.setLevel(DEBUG)
formatter = Formatter(
    '%(levelname)s[%(name)s, linea %(lineno)d]:   %(message)s ')
stream_handler = StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


class Juego(QThread, QtWidgets.QDialog):
    def __init__(self, tamanho, objetos):
        self.tamanho = tamanho
        self.objetos = objetos
        # self.ui = T05_GUI()
        self.ui.setupUi(self)

    # Sacado de ejemplo tetris REVISAR Y MODIFICAR
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
            super(Board, self).keyPressEvent(event)

        def checkear_colision(unidad)
            for objeto in self.objetos:
                if


        def checkear_rango():
            pass

        def


if __name__ == '__main__':
    logger.debug('hola')
    logger.debug('chao')

    # app = QtWidgets.QApplication(argv)
    # myapp = Juego()
    # myapp.show()
    # exit(app.exec_())
