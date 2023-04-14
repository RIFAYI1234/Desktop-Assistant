import JARVIS
from JARVIS_GUI import Ui_JARVIS
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate

from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *

from PyQt5.uic import loadUiType
import JARVIS_GUI

class MainThread(QThread):

    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        JARVIS.Task_Gui()

startExe = MainThread()

class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()

        self.gui = Ui_JARVIS()
        self.gui.setupUi(self)

        self.gui.pushButton_start.clicked.connect(self.startTask)
        self.gui.pushButton_exit.clicked.connect(self.exit)

    def startTask(self):
        self.gui.label1 = QtGui.QMovie("D:\\Python Programming\\Main GUI Elements\\Artificial Intelligence Loop GIF by xponentialdesign - Find & Share on GIPHY.gif")
        self.gui.Main_GIF.setMovie(self.gui.label1)
        self.gui.label1.start()

        startExe.start()

GuiApp = QApplication(sys.argv)
JARVIS_GUI = Gui_Start()
JARVIS_GUI.show()
exit(GuiApp.exec_())

