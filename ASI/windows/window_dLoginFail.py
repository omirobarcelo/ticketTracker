__author__ = 'Otros'

# -*- coding: utf-8 -*-

from PySide import QtGui
from PySide.QtGui import *
from PySide import QtCore

from GUI.dLoginFail import Ui_dLoginFail

class LoginFail(QtGui.QDialog):
    def __init__(self, parent=None):
        super(LoginFail, self).__init__(parent)
        self.ui = Ui_dLoginFail()
        self.ui.setupUi(self)

        self.ui.btAccept.released.connect(self.accept)
