# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/fLogin.ui'
#
# Created: Wed Jan 14 18:12:23 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_fLogin(object):
    def setupUi(self, fLogin):
        fLogin.setObjectName("fLogin")
        fLogin.resize(800, 602)
        self.centralwidget = QtGui.QWidget(fLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetFields = QtGui.QWidget(self.centralwidget)
        self.widgetFields.setObjectName("widgetFields")
        self.formLayout = QtGui.QFormLayout(self.widgetFields)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setContentsMargins(-1, 150, -1, -1)
        self.formLayout.setObjectName("formLayout")
        self.lbUsername = QtGui.QLabel(self.widgetFields)
        self.lbUsername.setObjectName("lbUsername")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lbUsername)
        self.lfUsername = QtGui.QLineEdit(self.widgetFields)
        self.lfUsername.setObjectName("lfUsername")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lfUsername)
        self.lbPassword = QtGui.QLabel(self.widgetFields)
        self.lbPassword.setObjectName("lbPassword")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lbPassword)
        self.lfPassword = QtGui.QLineEdit(self.widgetFields)
        self.lfPassword.setObjectName("lfPassword")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lfPassword)
        self.verticalLayout.addWidget(self.widgetFields)
        self.widgetButtons = QtGui.QWidget(self.centralwidget)
        self.widgetButtons.setObjectName("widgetButtons")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widgetButtons)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 300)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btSignUp = QtGui.QPushButton(self.widgetButtons)
        self.btSignUp.setObjectName("btSignUp")
        self.horizontalLayout.addWidget(self.btSignUp)
        self.btLogIn = QtGui.QPushButton(self.widgetButtons)
        self.btLogIn.setObjectName("btLogIn")
        self.horizontalLayout.addWidget(self.btLogIn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.widgetButtons)
        fLogin.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fLogin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuLanguage = QtGui.QMenu(self.menubar)
        self.menuLanguage.setObjectName("menuLanguage")
        fLogin.setMenuBar(self.menubar)
        self.actionESP = QtGui.QAction(fLogin)
        self.actionESP.setCheckable(True)
        self.actionESP.setChecked(True)
        self.actionESP.setObjectName("actionESP")
        self.actionCAT = QtGui.QAction(fLogin)
        self.actionCAT.setObjectName("actionCAT")
        self.actionENG = QtGui.QAction(fLogin)
        self.actionENG.setObjectName("actionENG")
        self.actionCHI = QtGui.QAction(fLogin)
        self.actionCHI.setObjectName("actionCHI")
        self.menuLanguage.addAction(self.actionESP)
        self.menuLanguage.addAction(self.actionCAT)
        self.menuLanguage.addAction(self.actionENG)
        self.menuLanguage.addAction(self.actionCHI)
        self.menubar.addAction(self.menuLanguage.menuAction())

        self.retranslateUi(fLogin)
        QtCore.QMetaObject.connectSlotsByName(fLogin)

    def retranslateUi(self, fLogin):
        fLogin.setWindowTitle(QtGui.QApplication.translate("fLogin", "Inicio de sesión", None, QtGui.QApplication.UnicodeUTF8))
        self.lbUsername.setText(QtGui.QApplication.translate("fLogin", "Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.lbPassword.setText(QtGui.QApplication.translate("fLogin", "Contraseña", None, QtGui.QApplication.UnicodeUTF8))
        self.btSignUp.setText(QtGui.QApplication.translate("fLogin", "Registrarse", None, QtGui.QApplication.UnicodeUTF8))
        self.btLogIn.setText(QtGui.QApplication.translate("fLogin", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLanguage.setTitle(QtGui.QApplication.translate("fLogin", "Idioma", None, QtGui.QApplication.UnicodeUTF8))
        self.actionESP.setText(QtGui.QApplication.translate("fLogin", "Castellano", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCAT.setText(QtGui.QApplication.translate("fLogin", "Catalán", None, QtGui.QApplication.UnicodeUTF8))
        self.actionENG.setText(QtGui.QApplication.translate("fLogin", "Inglés", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCHI.setText(QtGui.QApplication.translate("fLogin", "Chicken", None, QtGui.QApplication.UnicodeUTF8))

