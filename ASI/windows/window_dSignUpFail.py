__author__ = 'Otros'

# -*- coding: utf-8 -*-

from PySide import QtGui
from PySide.QtGui import *
from PySide import QtCore

from GUI.dSignUpFail import Ui_dSignUpFail

class SignUpFail(QtGui.QDialog):
    def __init__(self, parent=None):
        super(SignUpFail, self).__init__(parent)
        self.ui = Ui_dSignUpFail()
        self.ui.setupUi(self)

        self.ui.btAccept.released.connect(self.accept)
