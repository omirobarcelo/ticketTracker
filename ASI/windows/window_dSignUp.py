__author__ = 'Otros'

# -*- coding: utf-8 -*-

from PySide import QtGui
from PySide.QtGui import *
from PySide import QtCore

from GUI.dSignUp import Ui_dSignUp
import utils.dSignUp

from windows.window_dSignUpFail import SignUpFail

class SignUp(QtGui.QDialog):
    def __init__(self, parent=None):
        super(SignUp, self).__init__(parent)
        self.ui = Ui_dSignUp()
        self.ui.setupUi(self)

        # Fill Rol combo box
        self.ui.cboxRol.addItems(utils.dSignUp.getWorkList())

        # Define button operations
        self.ui.btAccept.released.connect(self.bt_accept)
        self.ui.btCancel.released.connect(self.reject)

    def bt_accept(self):
        username = self.ui.lfUsername.text()
        password = self.ui.lfPassword.text()
        workname = self.ui.cboxRol.itemText(0) if (self.ui.cboxRol.currentIndex == -1) else self.ui.cboxRol.currentText()
        valid_user = utils.dSignUp.addUser(username, password, workname)
        if valid_user is None:
            self.suf = SignUpFail()
            self.suf.exec_()
        else:
            self.accept()

    @staticmethod
    def userSignUp(parent = None):
        dialog = SignUp(parent)
        result = dialog.exec_()
        username = dialog.ui.lfUsername.text()
        password = dialog.ui.lfPassword.text()
        return (username, password, result == QtGui.QDialog.Accepted)
