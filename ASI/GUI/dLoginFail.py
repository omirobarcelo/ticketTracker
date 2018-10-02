# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/dLoginFail.ui'
#
# Created: Wed Jan 14 18:12:22 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dLoginFail(object):
    def setupUi(self, dLoginFail):
        dLoginFail.setObjectName("dLoginFail")
        dLoginFail.setWindowModality(QtCore.Qt.ApplicationModal)
        dLoginFail.resize(381, 150)
        dLoginFail.setModal(True)
        self.btAccept = QtGui.QPushButton(dLoginFail)
        self.btAccept.setGeometry(QtCore.QRect(240, 100, 114, 32))
        self.btAccept.setDefault(True)
        self.btAccept.setObjectName("btAccept")
        self.lbLine1 = QtGui.QLabel(dLoginFail)
        self.lbLine1.setGeometry(QtCore.QRect(40, 30, 291, 20))
        self.lbLine1.setObjectName("lbLine1")
        self.lbLine2 = QtGui.QLabel(dLoginFail)
        self.lbLine2.setGeometry(QtCore.QRect(40, 60, 241, 16))
        self.lbLine2.setObjectName("lbLine2")

        self.retranslateUi(dLoginFail)
        QtCore.QMetaObject.connectSlotsByName(dLoginFail)

    def retranslateUi(self, dLoginFail):
        dLoginFail.setWindowTitle(QtGui.QApplication.translate("dLoginFail", "Error de inicio de sesión", None, QtGui.QApplication.UnicodeUTF8))
        self.btAccept.setText(QtGui.QApplication.translate("dLoginFail", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.lbLine1.setText(QtGui.QApplication.translate("dLoginFail", "El usuario o la contraseña son incorrectos.", None, QtGui.QApplication.UnicodeUTF8))
        self.lbLine2.setText(QtGui.QApplication.translate("dLoginFail", "Por favor, vuelva a intentarlo.", None, QtGui.QApplication.UnicodeUTF8))

