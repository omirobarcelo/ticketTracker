# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dLogin.ui'
#
# Created: Sat Jan 17 22:43:50 2015
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dLogin(object):
    def setupUi(self, dLogin):
        dLogin.setObjectName("dLogin")
        dLogin.resize(395, 201)
        self.verticalLayout = QtGui.QVBoxLayout(dLogin)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetMain = QtGui.QWidget(dLogin)
        self.widgetMain.setObjectName("widgetMain")
        self.formLayout = QtGui.QFormLayout(self.widgetMain)
        self.formLayout.setContentsMargins(-1, 20, -1, -1)
        self.formLayout.setObjectName("formLayout")
        self.lbUsername = QtGui.QLabel(self.widgetMain)
        self.lbUsername.setObjectName("lbUsername")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lbUsername)
        self.lfUsername = QtGui.QLineEdit(self.widgetMain)
        self.lfUsername.setObjectName("lfUsername")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lfUsername)
        self.lbPassword = QtGui.QLabel(self.widgetMain)
        self.lbPassword.setObjectName("lbPassword")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lbPassword)
        self.lfPassword = QtGui.QLineEdit(self.widgetMain)
        self.lfPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.lfPassword.setObjectName("lfPassword")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lfPassword)
        self.verticalLayout.addWidget(self.widgetMain)
        self.widgetButtons = QtGui.QWidget(dLogin)
        self.widgetButtons.setObjectName("widgetButtons")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widgetButtons)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 40)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btSignUp = QtGui.QPushButton(self.widgetButtons)
        self.btSignUp.setObjectName("btSignUp")
        self.horizontalLayout.addWidget(self.btSignUp)
        self.btAccept = QtGui.QPushButton(self.widgetButtons)
        self.btAccept.setDefault(True)
        self.btAccept.setObjectName("btAccept")
        self.horizontalLayout.addWidget(self.btAccept)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.widgetButtons)

        self.retranslateUi(dLogin)
        QtCore.QMetaObject.connectSlotsByName(dLogin)

    def retranslateUi(self, dLogin):
        dLogin.setWindowTitle(QtGui.QApplication.translate("dLogin", "Inicio de sesión", None, QtGui.QApplication.UnicodeUTF8))
        self.lbUsername.setText(QtGui.QApplication.translate("dLogin", "Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.lbPassword.setText(QtGui.QApplication.translate("dLogin", "Contraseña", None, QtGui.QApplication.UnicodeUTF8))
        self.btSignUp.setText(QtGui.QApplication.translate("dLogin", "Registrarse", None, QtGui.QApplication.UnicodeUTF8))
        self.btAccept.setText(QtGui.QApplication.translate("dLogin", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

