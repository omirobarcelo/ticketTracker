__author__ = 'Otros'

# -*- coding: utf-8 -*-

from PySide import QtGui
from PySide.QtGui import *
from PySide import QtCore

from GUI.fMain import Ui_fMain

from windows.window_dLogin import Login
from windows.window_dSearch import Search
from windows.window_dCreate import Create
from windows.window_dModify import Modify
from windows.window_dNewComment import NewComment

import utils.globalVar
import utils.fMain

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        #self.ui = Ui_fMain()
        #self.ui.setupUi(self)

        self.login_and_window_creation()

        # self.show()

    def login_and_window_creation(self):
        self.ui = Ui_fMain()
        self.ui.setupUi(self)
        # Login dialog
        username, level, ok = Login.getLogin()
        if ok:
            utils.globalVar.userLogged = username
            utils.globalVar.levelLogged = level
            # Set buttons
            self.ui.verticalLayout_2.addWidget(self.ui.btSearch)
            self.ui.btSearch.released.connect(self.bt_search)
            self.ui.verticalLayout_2.addWidget(self.ui.btShowAll)
            self.ui.btShowAll.released.connect(self.bt_show_all)
            if not level == 3:
                # Create button definition
                self.btCreate = QtGui.QPushButton(self.ui.widgetButtons)
                self.btCreate.setObjectName("btCreate")
                self.ui.verticalLayout_2.addWidget(self.btCreate)
                self.btCreate.setText(QtGui.QApplication.translate("fMain", "Crear ticket", None, QtGui.QApplication.UnicodeUTF8))
                self.btCreate.released.connect(self.bt_create)
            if not level == 0:
                # Modify button definition
                self.btModify = QtGui.QPushButton(self.ui.widgetButtons)
                self.btModify.setObjectName("btModify")
                self.ui.verticalLayout_2.addWidget(self.btModify)
                self.btModify.setText(QtGui.QApplication.translate("fMain", "Modificar ticket", None, QtGui.QApplication.UnicodeUTF8))
                self.btModify.released.connect(self.bt_modify)
                # New comment button definition
                self.btNewComment = QtGui.QPushButton(self.ui.widgetButtons)
                self.btNewComment.setObjectName("btNewComment")
                self.ui.verticalLayout_2.addWidget(self.btNewComment)
                self.btNewComment.setText(QtGui.QApplication.translate("fMain", "Anadir comentario", None, QtGui.QApplication.UnicodeUTF8))
                self.btNewComment.released.connect(self.bt_new_comment)
            self.ui.verticalLayout_2.addWidget(self.ui.btSignOut)
            self.ui.btSignOut.released.connect(self.bt_sign_out)
            self.ui.verticalLayout_2.addItem(self.ui.spacerItem)

            # Fill table
            self.create_table()

            self.show()

    def create_table(self, ticket_list = None):
        # Get table data including header
        header, table_data = utils.fMain.getTableContent(utils.globalVar.userLogged, utils.globalVar.levelLogged)
        if ticket_list is not None:
            header, table_data = utils.fMain.formatTableGraphic(ticket_list)
        utils.globalVar.table = table_data

        # Set number of rows and columns
        if len(table_data) == 0:
            self.ui.tableTicket.setRowCount(0)
            self.ui.tableTicket.setColumnCount(0)
        else:
            self.ui.tableTicket.setRowCount(len(table_data))
            self.ui.tableTicket.setColumnCount(len(table_data[0]))

        # Set header
        self.ui.tableTicket.setHorizontalHeaderLabels(header)

        # Fill table with data
        if len(table_data) > 0:
            for column in range(len(table_data[0])):
                for row in range(len(table_data)):
                    data = table_data[row][column]
                    item = QtGui.QTableWidgetItem(str(data).decode('utf-8'))
                    self.ui.tableTicket.setItem(row, column, item)

        # Set action on double click
        self.ui.tableTicket.cellDoubleClicked.connect(self.create_ticket_info)

    def create_ticket_info(self, row, column):
        item = self.ui.tableTicket.item(row, 0)
        ticket_id = int(item.text())
        ticket_data = utils.fMain.showTicket(ticket_id)
        self.ui.tfTicketInfo.setPlainText(ticket_data)

    def bt_search(self):
        ticket_list, ok = Search.filterTickets()
        if ok:
            if ticket_list is None:
                ticket_list = []
            self.create_table(ticket_list)

    def bt_show_all(self):
        self.create_table()

    def bt_create(self):
        ok = Create.createTicket()
        if ok:
            self.create_table()

    def bt_modify(self):
        ok = Modify.modifyTickets()
        if ok:
            self.create_table()

    def bt_new_comment(self):
        ok = NewComment.addNewComment()
        if ok:
            self.create_table()

    def bt_sign_out(self):
        self.hide()
        self.login_and_window_creation()
