# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/dModifyID.ui'
#
# Created: Wed Jan 14 18:12:23 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dModifyID(object):
    def setupUi(self, dModifyID):
        dModifyID.setObjectName("dModifyID")
        dModifyID.setWindowModality(QtCore.Qt.ApplicationModal)
        dModifyID.resize(309, 329)
        dModifyID.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(dModifyID)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetAskID = QtGui.QWidget(dModifyID)
        self.widgetAskID.setObjectName("widgetAskID")
        self.formLayout_2 = QtGui.QFormLayout(self.widgetAskID)
        self.formLayout_2.setContentsMargins(-1, -1, 28, -1)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lbID = QtGui.QLabel(self.widgetAskID)
        self.lbID.setObjectName("lbID")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.lbID)
        self.cboxID = QtGui.QComboBox(self.widgetAskID)
        self.cboxID.setObjectName("cboxID")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.cboxID)
        self.verticalLayout.addWidget(self.widgetAskID)
        self.widgetMain = QtGui.QWidget(dModifyID)
        self.widgetMain.setObjectName("widgetMain")
        self.formLayout = QtGui.QFormLayout(self.widgetMain)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.cboxResponsible = QtGui.QComboBox(self.widgetMain)
        self.cboxResponsible.setObjectName("cboxResponsible")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cboxResponsible)
        self.cboxPriority = QtGui.QComboBox(self.widgetMain)
        self.cboxPriority.setObjectName("cboxPriority")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.cboxPriority)
        self.cboxState = QtGui.QComboBox(self.widgetMain)
        self.cboxState.setObjectName("cboxState")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.cboxState)
        self.lfCurrentResponsible = QtGui.QLineEdit(self.widgetMain)
        self.lfCurrentResponsible.setReadOnly(True)
        self.lfCurrentResponsible.setObjectName("lfCurrentResponsible")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lfCurrentResponsible)
        self.lfCurrentPriority = QtGui.QLineEdit(self.widgetMain)
        self.lfCurrentPriority.setReadOnly(True)
        self.lfCurrentPriority.setObjectName("lfCurrentPriority")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lfCurrentPriority)
        self.lfCurrentState = QtGui.QLineEdit(self.widgetMain)
        self.lfCurrentState.setReadOnly(True)
        self.lfCurrentState.setObjectName("lfCurrentState")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lfCurrentState)
        self.lbResponsible = QtGui.QLabel(self.widgetMain)
        self.lbResponsible.setObjectName("lbResponsible")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lbResponsible)
        self.lbPriority = QtGui.QLabel(self.widgetMain)
        self.lbPriority.setObjectName("lbPriority")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lbPriority)
        self.lbState = QtGui.QLabel(self.widgetMain)
        self.lbState.setObjectName("lbState")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.lbState)
        self.verticalLayout.addWidget(self.widgetMain)
        self.widgetButtons = QtGui.QWidget(dModifyID)
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

        self.retranslateUi(dModifyID)
        QtCore.QMetaObject.connectSlotsByName(dModifyID)

    def retranslateUi(self, dModifyID):
        dModifyID.setWindowTitle(QtGui.QApplication.translate("dModifyID", "Modificación de ticket", None, QtGui.QApplication.UnicodeUTF8))
        self.lbID.setText(QtGui.QApplication.translate("dModifyID", "Ticket ID", None, QtGui.QApplication.UnicodeUTF8))
        self.lbResponsible.setText(QtGui.QApplication.translate("dModifyID", "Responsable", None, QtGui.QApplication.UnicodeUTF8))
        self.lbPriority.setText(QtGui.QApplication.translate("dModifyID", "Prioridad", None, QtGui.QApplication.UnicodeUTF8))
        self.lbState.setText(QtGui.QApplication.translate("dModifyID", "Estado", None, QtGui.QApplication.UnicodeUTF8))
        self.btCancel.setText(QtGui.QApplication.translate("dModifyID", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.btAccept.setText(QtGui.QApplication.translate("dModifyID", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

