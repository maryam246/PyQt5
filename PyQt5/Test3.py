# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test3.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 416)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 511, 341))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../Downloads/wp2858563-beautiful-nature-background-hd.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Previous = QtWidgets.QPushButton(self.centralwidget)
        self.Previous.setGeometry(QtCore.QRect(0, 340, 251, 41))
        self.Previous.setObjectName("Previous")
        self.Next = QtWidgets.QPushButton(self.centralwidget)
        self.Next.setGeometry(QtCore.QRect(250, 340, 261, 41))
        self.Next.setObjectName("Next")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Previous.clicked.connect(self.show_1stPic)
        self.Next.clicked.connect(self.show_2ndPic)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Previous.setText(_translate("MainWindow", "<"))
        self.Next.setText(_translate("MainWindow", ">"))

    def show_1stPic(self):
        self.label.setPixmap(QtGui.QPixmap("1stPic.jpg"))
    def show_2ndPic(self):
        self.label.setPixmap(QtGui.QPixmap("2ndPic.jpg"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
