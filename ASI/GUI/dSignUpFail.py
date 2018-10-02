# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dSignUpFail.ui'
#
# Created: Sat Jan 17 22:44:16 2015
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dSignUpFail(object):
    def setupUi(self, dSignUpFail):
        dSignUpFail.setObjectName("dSignUpFail")
        dSignUpFail.setWindowModality(QtCore.Qt.ApplicationModal)
        dSignUpFail.resize(381, 150)
        dSignUpFail.setModal(True)
        self.btAccept = QtGui.QPushButton(dSignUpFail)
        self.btAccept.setGeometry(QtCore.QRect(240, 100, 114, 32))
        self.btAccept.setDefault(True)
        self.btAccept.setObjectName("btAccept")
        self.lbLine1 = QtGui.QLabel(dSignUpFail)
        self.lbLine1.setGeometry(QtCore.QRect(40, 30, 291, 20))
        self.lbLine1.setObjectName("lbLine1")
        self.lbLine2 = QtGui.QLabel(dSignUpFail)
        self.lbLine2.setGeometry(QtCore.QRect(40, 60, 241, 16))
        self.lbLine2.setObjectName("lbLine2")

        self.retranslateUi(dSignUpFail)
        QtCore.QMetaObject.connectSlotsByName(dSignUpFail)

    def retranslateUi(self, dSignUpFail):
        dSignUpFail.setWindowTitle(QtGui.QApplication.translate("dSignUpFail", "Error de registro", None, QtGui.QApplication.UnicodeUTF8))
        self.btAccept.setText(QtGui.QApplication.translate("dSignUpFail", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.lbLine1.setText(QtGui.QApplication.translate("dSignUpFail", "El nombre de usuario ya existe.", None, QtGui.QApplication.UnicodeUTF8))
        self.lbLine2.setText(QtGui.QApplication.translate("dSignUpFail", "Por favor, vuelva a intentarlo.", None, QtGui.QApplication.UnicodeUTF8))

