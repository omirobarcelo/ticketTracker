# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/dModifyAuto.ui'
#
# Created: Wed Jan 14 18:12:22 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dModifyAuto(object):
    def setupUi(self, dModifyAuto):
        dModifyAuto.setObjectName("dModifyAuto")
        dModifyAuto.setWindowModality(QtCore.Qt.ApplicationModal)
        dModifyAuto.resize(309, 192)
        dModifyAuto.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(dModifyAuto)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetMain = QtGui.QWidget(dModifyAuto)
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
        self.widgetButtons = QtGui.QWidget(dModifyAuto)
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

        self.retranslateUi(dModifyAuto)
        QtCore.QMetaObject.connectSlotsByName(dModifyAuto)

    def retranslateUi(self, dModifyAuto):
        dModifyAuto.setWindowTitle(QtGui.QApplication.translate("dModifyAuto", "Modificación de ticket", None, QtGui.QApplication.UnicodeUTF8))
        self.lbResponsible.setText(QtGui.QApplication.translate("dModifyAuto", "Responsable", None, QtGui.QApplication.UnicodeUTF8))
        self.lbPriority.setText(QtGui.QApplication.translate("dModifyAuto", "Prioridad", None, QtGui.QApplication.UnicodeUTF8))
        self.lbState.setText(QtGui.QApplication.translate("dModifyAuto", "Estado", None, QtGui.QApplication.UnicodeUTF8))
        self.btCancel.setText(QtGui.QApplication.translate("dModifyAuto", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.btAccept.setText(QtGui.QApplication.translate("dModifyAuto", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

