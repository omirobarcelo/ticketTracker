# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/dSignUp.ui'
#
# Created: Wed Jan 14 18:12:23 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dSignUp(object):
    def setupUi(self, dSignUp):
        dSignUp.setObjectName("dSignUp")
        dSignUp.setWindowModality(QtCore.Qt.ApplicationModal)
        dSignUp.resize(288, 265)
        dSignUp.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(dSignUp)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetMain = QtGui.QWidget(dSignUp)
        self.widgetMain.setObjectName("widgetMain")
        self.formLayout = QtGui.QFormLayout(self.widgetMain)
        self.formLayout.setContentsMargins(-1, 35, -1, -1)
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
        self.lfPassword.setPlaceholderText("")
        self.lfPassword.setObjectName("lfPassword")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lfPassword)
        self.lbRol = QtGui.QLabel(self.widgetMain)
        self.lbRol.setObjectName("lbRol")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lbRol)
        self.cboxRol = QtGui.QComboBox(self.widgetMain)
        self.cboxRol.setEditable(False)
        self.cboxRol.setMinimumContentsLength(0)
        self.cboxRol.setObjectName("cboxRol")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.cboxRol)
        self.verticalLayout.addWidget(self.widgetMain)
        self.widgetButtons = QtGui.QWidget(dSignUp)
        self.widgetButtons.setObjectName("widgetButtons")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widgetButtons)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btCancel = QtGui.QPushButton(self.widgetButtons)
        self.btCancel.setObjectName("btCancel")
        self.horizontalLayout.addWidget(self.btCancel)
        self.btAccept = QtGui.QPushButton(self.widgetButtons)
        self.btAccept.setDefault(True)
        self.btAccept.setObjectName("btAccept")
        self.horizontalLayout.addWidget(self.btAccept)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.widgetButtons)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(dSignUp)
        QtCore.QMetaObject.connectSlotsByName(dSignUp)

    def retranslateUi(self, dSignUp):
        dSignUp.setWindowTitle(QtGui.QApplication.translate("dSignUp", "Registro de usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.lbUsername.setText(QtGui.QApplication.translate("dSignUp", "Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.lbPassword.setText(QtGui.QApplication.translate("dSignUp", "Contraseña", None, QtGui.QApplication.UnicodeUTF8))
        self.lbRol.setText(QtGui.QApplication.translate("dSignUp", "Rol", None, QtGui.QApplication.UnicodeUTF8))
        self.btCancel.setText(QtGui.QApplication.translate("dSignUp", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.btAccept.setText(QtGui.QApplication.translate("dSignUp", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

