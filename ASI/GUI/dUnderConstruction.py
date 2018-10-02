# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/dUnderConstruction.ui'
#
# Created: Wed Jan 14 18:12:23 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dUnderConstruction(object):
    def setupUi(self, dUnderConstruction):
        dUnderConstruction.setObjectName("dUnderConstruction")
        dUnderConstruction.setWindowModality(QtCore.Qt.ApplicationModal)
        dUnderConstruction.resize(399, 128)
        dUnderConstruction.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(dUnderConstruction)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetInfo = QtGui.QWidget(dUnderConstruction)
        self.widgetInfo.setObjectName("widgetInfo")
        self.gridLayout_2 = QtGui.QGridLayout(self.widgetInfo)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtGui.QLabel(self.widgetInfo)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.widgetInfo)
        self.widgetButtons = QtGui.QWidget(dUnderConstruction)
        self.widgetButtons.setObjectName("widgetButtons")
        self.gridLayout = QtGui.QGridLayout(self.widgetButtons)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btAccept = QtGui.QPushButton(self.widgetButtons)
        self.btAccept.setDefault(True)
        self.btAccept.setObjectName("btAccept")
        self.gridLayout.addWidget(self.btAccept, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.widgetButtons)

        self.retranslateUi(dUnderConstruction)
        QtCore.QMetaObject.connectSlotsByName(dUnderConstruction)

    def retranslateUi(self, dUnderConstruction):
        dUnderConstruction.setWindowTitle(QtGui.QApplication.translate("dUnderConstruction", "Under construction", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dUnderConstruction", "Site under construction. Function not yet implemented.", None, QtGui.QApplication.UnicodeUTF8))
        self.btAccept.setText(QtGui.QApplication.translate("dUnderConstruction", "Accept", None, QtGui.QApplication.UnicodeUTF8))

