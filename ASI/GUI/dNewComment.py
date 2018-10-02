# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/dNewComment.ui'
#
# Created: Wed Jan 14 18:12:23 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dNewComment(object):
    def setupUi(self, dNewComment):
        dNewComment.setObjectName("dNewComment")
        dNewComment.setWindowModality(QtCore.Qt.ApplicationModal)
        dNewComment.resize(399, 336)
        dNewComment.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(dNewComment)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetMain = QtGui.QWidget(dNewComment)
        self.widgetMain.setObjectName("widgetMain")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widgetMain)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widgetAskID = QtGui.QWidget(self.widgetMain)
        self.widgetAskID.setObjectName("widgetAskID")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widgetAskID)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbTicketID = QtGui.QLabel(self.widgetAskID)
        self.lbTicketID.setObjectName("lbTicketID")
        self.horizontalLayout_2.addWidget(self.lbTicketID)
        self.cboxTicketID = QtGui.QComboBox(self.widgetAskID)
        self.cboxTicketID.setObjectName("cboxTicketID")
        self.horizontalLayout_2.addWidget(self.cboxTicketID)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.widgetAskID)
        self.lbComment = QtGui.QLabel(self.widgetMain)
        self.lbComment.setObjectName("lbComment")
        self.verticalLayout_2.addWidget(self.lbComment)
        self.tfComment = QtGui.QPlainTextEdit(self.widgetMain)
        self.tfComment.setObjectName("tfComment")
        self.verticalLayout_2.addWidget(self.tfComment)
        self.verticalLayout.addWidget(self.widgetMain)
        self.widgetButtons = QtGui.QWidget(dNewComment)
        self.widgetButtons.setObjectName("widgetButtons")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widgetButtons)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btCancel = QtGui.QPushButton(self.widgetButtons)
        self.btCancel.setObjectName("btCancel")
        self.horizontalLayout.addWidget(self.btCancel)
        self.btAccept = QtGui.QPushButton(self.widgetButtons)
        self.btAccept.setDefault(True)
        self.btAccept.setObjectName("btAccept")
        self.horizontalLayout.addWidget(self.btAccept)
        self.verticalLayout.addWidget(self.widgetButtons)

        self.retranslateUi(dNewComment)
        QtCore.QMetaObject.connectSlotsByName(dNewComment)

    def retranslateUi(self, dNewCommentESP):
        dNewCommentESP.setWindowTitle(QtGui.QApplication.translate("dNewCommentESP", "Añadir comentario", None, QtGui.QApplication.UnicodeUTF8))
        self.lbTicketID.setText(QtGui.QApplication.translate("dNewCommentESP", "Ticket ID", None, QtGui.QApplication.UnicodeUTF8))
        self.lbComment.setText(QtGui.QApplication.translate("dNewCommentESP", "Comentario", None, QtGui.QApplication.UnicodeUTF8))
        self.btCancel.setText(QtGui.QApplication.translate("dNewCommentESP", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.btAccept.setText(QtGui.QApplication.translate("dNewCommentESP", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

