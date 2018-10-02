# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/dSearch.ui'
#
# Created: Wed Jan 14 18:12:23 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dSearch(object):
    def setupUi(self, dSearch):
        dSearch.setObjectName("dSearch")
        dSearch.setWindowModality(QtCore.Qt.ApplicationModal)
        dSearch.resize(298, 266)
        dSearch.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(dSearch)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetMain = QtGui.QWidget(dSearch)
        self.widgetMain.setObjectName("widgetMain")
        self.formLayout = QtGui.QFormLayout(self.widgetMain)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lbID = QtGui.QLabel(self.widgetMain)
        self.lbID.setObjectName("lbID")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lbID)
        self.cboxID = QtGui.QComboBox(self.widgetMain)
        self.cboxID.setObjectName("cboxID")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cboxID)
        self.lbCreator = QtGui.QLabel(self.widgetMain)
        self.lbCreator.setObjectName("lbCreator")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lbCreator)
        self.cboxCreator = QtGui.QComboBox(self.widgetMain)
        self.cboxCreator.setObjectName("cboxCreator")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cboxCreator)
        self.lbResponsible = QtGui.QLabel(self.widgetMain)
        self.lbResponsible.setObjectName("lbResponsible")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lbResponsible)
        self.cboxResponsible = QtGui.QComboBox(self.widgetMain)
        self.cboxResponsible.setObjectName("cboxResponsible")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.cboxResponsible)
        self.lbPriority = QtGui.QLabel(self.widgetMain)
        self.lbPriority.setObjectName("lbPriority")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.lbPriority)
        self.cboxPriority = QtGui.QComboBox(self.widgetMain)
        self.cboxPriority.setObjectName("cboxPriority")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.cboxPriority)
        self.lbState = QtGui.QLabel(self.widgetMain)
        self.lbState.setObjectName("lbState")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.lbState)
        self.cboxState = QtGui.QComboBox(self.widgetMain)
        self.cboxState.setObjectName("cboxState")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.cboxState)
        self.verticalLayout.addWidget(self.widgetMain)
        self.widgetButtons = QtGui.QWidget(dSearch)
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

        self.retranslateUi(dSearch)
        QtCore.QMetaObject.connectSlotsByName(dSearch)

    def retranslateUi(self, dSearch):
        dSearch.setWindowTitle(QtGui.QApplication.translate("dSearch", "Filtrar tickets", None, QtGui.QApplication.UnicodeUTF8))
        self.lbID.setText(QtGui.QApplication.translate("dSearch", "Ticket ID", None, QtGui.QApplication.UnicodeUTF8))
        self.lbCreator.setText(QtGui.QApplication.translate("dSearch", "Creador", None, QtGui.QApplication.UnicodeUTF8))
        self.lbResponsible.setText(QtGui.QApplication.translate("dSearch", "Responsable", None, QtGui.QApplication.UnicodeUTF8))
        self.lbPriority.setText(QtGui.QApplication.translate("dSearch", "Prioridad", None, QtGui.QApplication.UnicodeUTF8))
        self.lbState.setText(QtGui.QApplication.translate("dSearch", "Estado", None, QtGui.QApplication.UnicodeUTF8))
        self.btCancel.setText(QtGui.QApplication.translate("dSearch", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.btAccept.setText(QtGui.QApplication.translate("dSearch", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

