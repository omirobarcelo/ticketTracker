__author__ = 'Otros'

# -*- coding: utf-8 -*-

from PySide import QtGui
from PySide.QtGui import *
from PySide import QtCore

from GUI.dNewComment import Ui_dNewComment
import utils.dNewComment
import utils.globalVar

class NewComment(QtGui.QDialog):
    def __init__(self, parent=None):
        super(NewComment, self).__init__(parent)
        self.ui = Ui_dNewComment()
        self.ui.setupUi(self)

        # Fill ticket ID combo box
        self.ui.cboxTicketID.addItems(utils.dNewComment.getAssignedTicketList(utils.globalVar.userLogged))

        # Define button operations
        self.ui.btAccept.released.connect(self.bt_accept)
        self.ui.btCancel.released.connect(self.reject)

    def bt_accept(self):
        ticket_id = self.ui.cboxTicketID.itemText(0) if (self.ui.cboxTicketID.currentIndex == -1) else self.ui.cboxTicketID.currentText()
        text = self.ui.tfComment.toPlainText()
        utils.dNewComment.addComment(text, utils.globalVar.userLogged, int(ticket_id))
        self.accept()

    # Ticket creating dialog
    @staticmethod
    def addNewComment(parent = None):
        dialog = NewComment(parent)
        result = dialog.exec_()
        return result == QtGui.QDialog.Accepted
