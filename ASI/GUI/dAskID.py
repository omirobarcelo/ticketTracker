# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/dAskID.ui'
#
# Created: Wed Jan 14 18:12:22 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dAskID(object):
    def setupUi(self, dAskID):
        dAskID.setObjectName("dAskID")
        dAskID.setWindowModality(QtCore.Qt.ApplicationModal)
        dAskID.resize(229, 172)
        dAskID.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(dAskID)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetText = QtGui.QWidget(dAskID)
        self.widgetText.setObjectName("widgetText")
        self.gridLayout = QtGui.QGridLayout(self.widgetText)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lbInfo = QtGui.QLabel(self.widgetText)
        self.lbInfo.setObjectName("lbInfo")
        self.gridLayout.addWidget(self.lbInfo, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.widgetText)
        self.widgetSelect = QtGui.QWidget(dAskID)
        self.widgetSelect.setObjectName("widgetSelect")
        self.formLayout = QtGui.QFormLayout(self.widgetSelect)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lbID = QtGui.QLabel(self.widgetSelect)
        self.lbID.setObjectName("lbID")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lbID)
        self.cboxID = QtGui.QComboBox(self.widgetSelect)
        self.cboxID.setObjectName("cboxID")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cboxID)
        self.verticalLayout.addWidget(self.widgetSelect)
        self.widgetButtons = QtGui.QWidget(dAskID)
        self.widgetButtons.setObjectName("widgetButtons")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widgetButtons)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btCancel = QtGui.QPushButton(self.widgetButtons)
        self.btCancel.setObjectName("btCancel")
        self.horizontalLayout.addWidget(self.btCancel)
        self.btAccept = QtGui.QPushButton(self.widgetButtons)
        self.btAccept.setDefault(True)
        self.btAccept.setObjectName("btAccept")
        self.horizontalLayout.addWidget(self.btAccept)
        self.verticalLayout.addWidget(self.widgetButtons)

        self.retranslateUi(dAskID)
        QtCore.QMetaObject.connectSlotsByName(dAskID)

    def retranslateUi(self, dAskID):
        dAskID.setWindowTitle(QtGui.QApplication.translate("dAskID", "Seleccione ticket", None, QtGui.QApplication.UnicodeUTF8))
        self.lbInfo.setText(QtGui.QApplication.translate("dAskID", "Seleccione ticket a modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.lbID.setText(QtGui.QApplication.translate("dAskID", "Ticket ID", None, QtGui.QApplication.UnicodeUTF8))
        self.btCancel.setText(QtGui.QApplication.translate("dAskID", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.btAccept.setText(QtGui.QApplication.translate("dAskID", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

