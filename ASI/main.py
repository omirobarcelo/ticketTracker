__author__ = 'Otros'

# -*- coding: utf-8 -*-
from PySide import QtGui

import sys

from windows.window_fMain import MainWindow


if __name__ == '__main__':
    app = QtGui.QApplication([])

    win = MainWindow()

    sys.exit(app.exec_())
