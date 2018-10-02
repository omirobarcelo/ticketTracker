__author__ = 'Otros'

# -*- coding: utf-8 -*-

from PySide import QtGui
from PySide.QtGui import *
from PySide import QtCore

from GUI.dCreate import Ui_dCreate
import utils.dCreate
import utils.globalVar

class Create(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Create, self).__init__(parent)
        self.ui = Ui_dCreate()
        self.ui.setupUi(self)

        # Define button operations
        self.ui.btAccept.released.connect(self.bt_accept)
        self.ui.btCancel.released.connect(self.reject)

    def bt_accept(self):
        description = self.ui.tfDescription.toPlainText()
        utils.dCreate.addTicket(description, utils.globalVar.userLogged)
        self.accept()

    # Ticket creating dialog
    @staticmethod
    def createTicket(parent = None):
        dialog = Create(parent)
        result = dialog.exec_()
        return result == QtGui.QDialog.Accepted
