# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python Programming\Main GUI Elements\Jarvis GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
 


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JARVIS(object):
    def setupUi(self, JARVIS):
        JARVIS.setObjectName("JARVIS")
        JARVIS.resize(1907, 1024)
        self.centralwidget = QtWidgets.QWidget(JARVIS)
        self.centralwidget.setObjectName("centralwidget")
        self.Main_GIF = QtWidgets.QLabel(self.centralwidget)
        self.Main_GIF.setGeometry(QtCore.QRect(620, 60, 671, 641))
        self.Main_GIF.setAutoFillBackground(False)
        self.Main_GIF.setText("")
        self.Main_GIF.setPixmap(QtGui.QPixmap("D:\\Python Programming\\Main GUI Elements\\Artificial Intelligence Loop GIF by xponentialdesign - Find & Share on GIPHY.gif"))
        self.Main_GIF.setScaledContents(False)
        self.Main_GIF.setAlignment(QtCore.Qt.AlignCenter)
        self.Main_GIF.setObjectName("Main_GIF")
        self.BG = QtWidgets.QLabel(self.centralwidget)
        self.BG.setGeometry(QtCore.QRect(-30, -20, 1981, 1001))
        self.BG.setText("")
        self.BG.setPixmap(QtGui.QPixmap("D:\\Python Programming\\Main GUI Elements\\JARVIS.png"))
        self.BG.setScaledContents(True)
        self.BG.setObjectName("BG")
        self.Main_Logo = QtWidgets.QLabel(self.centralwidget)
        self.Main_Logo.setGeometry(QtCore.QRect(780, 580, 311, 291))
        self.Main_Logo.setAutoFillBackground(False)
        self.Main_Logo.setText("")
        self.Main_Logo.setPixmap(QtGui.QPixmap("D:\\Python Programming\\Main GUI Elements\\../GUI/ExtraGui/EDIT.png"))
        self.Main_Logo.setScaledContents(False)
        self.Main_Logo.setObjectName("Main_Logo")
        self.label_start = QtWidgets.QLabel(self.centralwidget)
        self.label_start.setGeometry(QtCore.QRect(1660, 790, 211, 91))
        self.label_start.setText("")
        self.label_start.setPixmap(QtGui.QPixmap("D:\\Python Programming\\Main GUI Elements\\../GUI/Buttons/Start.png"))
        self.label_start.setScaledContents(True)
        self.label_start.setObjectName("label_start")
        self.label_exit = QtWidgets.QLabel(self.centralwidget)
        self.label_exit.setGeometry(QtCore.QRect(1660, 870, 211, 81))
        self.label_exit.setText("")
        self.label_exit.setPixmap(QtGui.QPixmap("D:\\Python Programming\\Main GUI Elements\\../GUI/Buttons/Quit.png"))
        self.label_exit.setScaledContents(True)
        self.label_exit.setObjectName("label_exit")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(1680, 820, 161, 41))
        self.pushButton_start.setStyleSheet("background-color: rgb(69, 190, 172);\n"
"font: 8pt \"Stencil\";\n"
"")
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(1680, 890, 161, 41))
        self.pushButton_exit.setStyleSheet("background-color: rgb(69, 190, 172);\n"
"font: 8pt \"Stencil\";\n"
"")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.TIME = QtWidgets.QTextBrowser(self.centralwidget)
        self.TIME.setGeometry(QtCore.QRect(40, 40, 361, 221))
        self.TIME.setObjectName("TIME")
        self.BG.raise_()
        self.Main_GIF.raise_()
        self.Main_Logo.raise_()
        self.label_start.raise_()
        self.label_exit.raise_()
        self.pushButton_start.raise_()
        self.pushButton_exit.raise_()
        self.TIME.raise_()
        JARVIS.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(JARVIS)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1907, 26))
        self.menubar.setObjectName("menubar")
        JARVIS.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(JARVIS)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        JARVIS.setStatusBar(self.statusbar)

        self.retranslateUi(JARVIS)
        QtCore.QMetaObject.connectSlotsByName(JARVIS)

    def retranslateUi(self, JARVIS):
        _translate = QtCore.QCoreApplication.translate
        JARVIS.setWindowTitle(_translate("JARVIS", "MainWindow"))
        self.pushButton_start.setText(_translate("JARVIS", "START"))
        self.pushButton_exit.setText(_translate("JARVIS", "EXIT"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JARVIS = QtWidgets.QMainWindow()
    ui = Ui_JARVIS()
    ui.setupUi(JARVIS)
    JARVIS.show()
    sys.exit(app.exec_())
