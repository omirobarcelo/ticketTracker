__author__ = 'Otros'

# -*- coding: utf-8 -*-

from PySide import QtGui
from PySide.QtGui import *
from PySide import QtCore

from GUI.dLogin import Ui_dLogin
import utils.dLogin

from windows.window_dSignUp import SignUp
from windows.window_dLoginFail import LoginFail

class Login(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.ui = Ui_dLogin()
        self.ui.setupUi(self)

        # Define button operations
        self.ui.btAccept.released.connect(self.bt_accept)
        self.ui.btSignUp.released.connect(self.bt_sign_up)
        
    def bt_accept(self):
        username = self.ui.lfUsername.text()
        password = self.ui.lfPassword.text()
        level = utils.dLogin.checkLogin(username, password)
        if level is None:
            self.lf = LoginFail()
            self.lf.exec_()
        else:
            self.accept()

    def bt_sign_up(self):
        username, password, ok = SignUp.userSignUp()
        if ok:
            self.ui.lfUsername.setText(username)
            self.ui.lfPassword.setText(password)

    # Login dialog, gets username and password
    @staticmethod
    def getLogin(parent = None):
        dialog = Login(parent)
        result = dialog.exec_()
        username = dialog.ui.lfUsername.text()
        password = dialog.ui.lfPassword.text()
        level = utils.dLogin.checkLogin(username, password)
        return (username, level, result == QtGui.QDialog.Accepted)
