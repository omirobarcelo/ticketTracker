# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/dModifyIDAuto.ui'
#
# Created: Wed Jan 14 18:12:23 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dModifyIDAuto(object):
    def setupUi(self, dModifyIDAuto):
        dModifyIDAuto.setObjectName("dModifyIDAuto")
        dModifyIDAuto.setWindowModality(QtCore.Qt.ApplicationModal)
        dModifyIDAuto.resize(308, 257)
        dModifyIDAuto.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(dModifyIDAuto)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetAskID = QtGui.QWidget(dModifyIDAuto)
        self.widgetAskID.setObjectName("widgetAskID")
        self.formLayout_2 = QtGui.QFormLayout(self.widgetAskID)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lbID = QtGui.QLabel(self.widgetAskID)
        self.lbID.setObjectName("lbID")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.lbID)
        self.cboxID = QtGui.QComboBox(self.widgetAskID)
        self.cboxID.setObjectName("cboxID")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.cboxID)
        self.verticalLayout.addWidget(self.widgetAskID)
        self.widgetMain = QtGui.QWidget(dModifyIDAuto)
        self.widgetMain.setObjectName("widgetMain")
        self.formLayout = QtGui.QFormLayout(self.widgetMain)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lbResponsible = QtGui.QLabel(self.widgetMain)
        self.lbResponsible.setObjectName("lbResponsible")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lbResponsible)
        self.cboxResponsible = QtGui.QComboBox(self.widgetMain)
        self.cboxResponsible.setObjectName("cboxResponsible")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cboxResponsible)
        self.lbPriority = QtGui.QLabel(self.widgetMain)
        self.lbPriority.setObjectName("lbPriority")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lbPriority)
        self.cboxPriority = QtGui.QComboBox(self.widgetMain)
        self.cboxPriority.setObjectName("cboxPriority")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cboxPriority)
        self.lbState = QtGui.QLabel(self.widgetMain)
        self.lbState.setObjectName("lbState")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lbState)
        self.cboxState = QtGui.QComboBox(self.widgetMain)
        self.cboxState.setObjectName("cboxState")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.cboxState)
        self.verticalLayout.addWidget(self.widgetMain)
        self.widgetButtons = QtGui.QWidget(dModifyIDAuto)
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

        self.retranslateUi(dModifyIDAuto)
        QtCore.QMetaObject.connectSlotsByName(dModifyIDAuto)

    def retranslateUi(self, dModifyIDAuto):
        dModifyIDAuto.setWindowTitle(QtGui.QApplication.translate("dModifyIDAuto", "Modificación de ticket", None, QtGui.QApplication.UnicodeUTF8))
        self.lbID.setText(QtGui.QApplication.translate("dModifyIDAuto", "    Ticket ID", None, QtGui.QApplication.UnicodeUTF8))
        self.lbResponsible.setText(QtGui.QApplication.translate("dModifyIDAuto", "Responsable", None, QtGui.QApplication.UnicodeUTF8))
        self.lbPriority.setText(QtGui.QApplication.translate("dModifyIDAuto", "Prioridad", None, QtGui.QApplication.UnicodeUTF8))
        self.lbState.setText(QtGui.QApplication.translate("dModifyIDAuto", "Estado", None, QtGui.QApplication.UnicodeUTF8))
        self.btCancel.setText(QtGui.QApplication.translate("dModifyIDAuto", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.btAccept.setText(QtGui.QApplication.translate("dModifyIDAuto", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

