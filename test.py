
# coding: utf-8

# In[10]:

import os, time
import sys

from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QStandardItemModel
from PyQt4.QtGui import QStandardItem
import package.book_ui
from package.book_ui import Ui_MainWindow
#from firebase import firebase

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
     
    def closeEvent(self, event):
        # do stuff
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    size = window.maximumSize()
    window.show()
    window.setFixedSize(880, 620)
    app.exec_()

