# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/dCreate.ui'
#
# Created: Wed Jan 14 18:12:22 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dCreate(object):
    def setupUi(self, dCreate):
        dCreate.setObjectName("dCreate")
        dCreate.setWindowModality(QtCore.Qt.ApplicationModal)
        dCreate.resize(400, 300)
        dCreate.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(dCreate)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetDescription = QtGui.QWidget(dCreate)
        self.widgetDescription.setObjectName("widgetDescription")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widgetDescription)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbDescription = QtGui.QLabel(self.widgetDescription)
        self.lbDescription.setObjectName("lbDescription")
        self.verticalLayout_2.addWidget(self.lbDescription)
        self.tfDescription = QtGui.QPlainTextEdit(self.widgetDescription)
        self.tfDescription.setObjectName("tfDescription")
        self.verticalLayout_2.addWidget(self.tfDescription)
        self.verticalLayout.addWidget(self.widgetDescription)
        self.widgetButtons = QtGui.QWidget(dCreate)
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
        self.verticalLayout.addWidget(self.widgetButtons)

        self.retranslateUi(dCreate)
        QtCore.QMetaObject.connectSlotsByName(dCreate)

    def retranslateUi(self, dCreate):
        dCreate.setWindowTitle(QtGui.QApplication.translate("dCreate", "Crear ticket", None, QtGui.QApplication.UnicodeUTF8))
        self.lbDescription.setText(QtGui.QApplication.translate("dCreate", "Descripción", None, QtGui.QApplication.UnicodeUTF8))
        self.btCancel.setText(QtGui.QApplication.translate("dCreate", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.btAccept.setText(QtGui.QApplication.translate("dCreate", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

