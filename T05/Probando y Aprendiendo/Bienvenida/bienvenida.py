# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bienvenida.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 164)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 30, 321, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineNombreUsuario = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineNombreUsuario.setObjectName("lineNombreUsuario")
        self.gridLayout.addWidget(self.lineNombreUsuario, 0, 1, 1, 1)
        self.ButtonPulsar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ButtonPulsar.setObjectName("ButtonPulsar")
        self.gridLayout.addWidget(self.ButtonPulsar, 3, 2, 1, 1)
        self.labelEscribeNombre = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelEscribeNombre.setObjectName("labelEscribeNombre")
        self.gridLayout.addWidget(self.labelEscribeNombre, 0, 0, 1, 1)
        self.labelMensaje = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelMensaje.setText("")
        self.labelMensaje.setObjectName("labelMensaje")
        self.gridLayout.addWidget(self.labelMensaje, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bienvenida"))
        self.ButtonPulsar.setText(_translate("Dialog", "Pulsar"))
        self.labelEscribeNombre.setText(_translate("Dialog", "Escribe nombre:"))

