__author__ = 'Otros'

# -*- coding: utf-8 -*-

from PySide import QtGui
from PySide.QtGui import *
from PySide import QtCore

from GUI.dSearch import Ui_dSearch
import utils.dSearch
import utils.globalVar

class Search(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Search, self).__init__(parent)
        self.ui = Ui_dSearch()
        self.ui.setupUi(self)

        # Fill combo boxes
        self.ui.cboxID.addItems(utils.dSearch.getTicketIDsList(utils.globalVar.userLogged))
        self.ui.cboxID.setCurrentIndex(-1)
        self.ui.cboxCreator.addItems(utils.dSearch.getUsersList())
        self.ui.cboxCreator.setCurrentIndex(-1)
        self.ui.cboxResponsible.addItems(utils.dSearch.getUsersList())
        self.ui.cboxResponsible.setCurrentIndex(-1)
        self.ui.cboxPriority.addItems(["Critica", "Grave", "Alta", "Media", "Baja"])
        self.ui.cboxPriority.setCurrentIndex(-1)
        self.ui.cboxState.addItems(["Inicio", "Asignado", "En proceso", "Finalizado"])
        self.ui.cboxState.setCurrentIndex(-1)

        # Define button operations
        self.ui.btAccept.released.connect(self.accept)
        self.ui.btCancel.released.connect(self.reject)

    # Ticket creating dialog
    @staticmethod
    def filterTickets(parent = None):
        dialog = Search(parent)
        result = dialog.exec_()
        search_results = None
        if result == QtGui.QDialog.Accepted:
            ticket_id = None if (dialog.ui.cboxID.currentText() == '') else int(dialog.ui.cboxID.currentText())
            creator = None if (dialog.ui.cboxCreator.currentText() == '') else dialog.ui.cboxCreator.currentText()
            responsible = None if (dialog.ui.cboxResponsible.currentText() == '') else dialog.ui.cboxResponsible.currentText()
            priority = None if (dialog.ui.cboxPriority.currentText() == '') else dialog.ui.cboxPriority.currentText()
            state = None if (dialog.ui.cboxState.currentText() == '') else dialog.ui.cboxState.currentText()
            search_results = utils.dSearch.searchTicket(ticket_id, creator, responsible, priority, state)
        return (search_results, result == QtGui.QDialog.Accepted)
