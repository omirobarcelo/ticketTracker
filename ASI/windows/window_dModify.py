__author__ = 'Otros'

# -*- coding: utf-8 -*-

from PySide import QtGui
from PySide.QtGui import *
from PySide import QtCore

from GUI.dModifyIDAuto import Ui_dModifyIDAuto
import utils.dModify
import utils.globalVar

class Modify(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Modify, self).__init__(parent)
        self.ui = Ui_dModifyIDAuto()
        self.ui.setupUi(self)

        # Fill combo boxes
        self.ui.cboxID.addItems(utils.dModify.getAssignedTicketList(utils.globalVar.userLogged))
        self.ui.cboxID.setCurrentIndex(-1)
        self.ui.cboxResponsible.addItems(utils.dSearch.getUsersList())
        self.ui.cboxResponsible.setCurrentIndex(-1)
        self.ui.cboxPriority.addItems(["Critica", "Grave", "Alta", "Media", "Baja"])
        self.ui.cboxPriority.setCurrentIndex(-1)
        self.ui.cboxState.addItems(["Inicio", "Asignado", "En proceso", "Finalizado"])
        self.ui.cboxState.setCurrentIndex(-1)

        # Define button operations
        self.ui.btAccept.released.connect(self.bt_accept)
        self.ui.btCancel.released.connect(self.reject)

        # Set action on ticket ID selection
        self.ui.cboxID.currentIndexChanged.connect(self.fill_combo_boxes)

    def bt_accept(self):
        ticket_id = int(self.ui.cboxID.currentText())
        responsible = self.ui.cboxResponsible.currentText()
        priority = self.ui.cboxPriority.currentText()
        state = self.ui.cboxState.currentText()
        utils.dModify.updateTicket(ticket_id, responsible, priority, state)
        self.accept()

    def fill_combo_boxes(self, arg__1):
        id = self.ui.cboxID.itemText(int(arg__1))
        ticket_info = utils.dModify.getTicketInfo(int(id))
        index = self.ui.cboxResponsible.findText(ticket_info[0])
        self.ui.cboxResponsible.setCurrentIndex(index)
        index = self.ui.cboxPriority.findText(ticket_info[1])
        self.ui.cboxPriority.setCurrentIndex(index)
        index = self.ui.cboxState.findText(ticket_info[2])
        self.ui.cboxState.setCurrentIndex(index)

    # Ticket creating dialog
    @staticmethod
    def modifyTickets(parent = None):
        dialog = Modify(parent)
        result = dialog.exec_()
        return result == QtGui.QDialog.Accepted
