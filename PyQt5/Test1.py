# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_label1(object):
    def setupUi(self, label1):
        label1.setObjectName("label1")
        label1.resize(320, 240)
        self.centralwidget = QtWidgets.QWidget(label1)
        self.centralwidget.setObjectName("centralwidget")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(90, 110, 131, 41))
        self.button1.setObjectName("button1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 221, 41))
        self.label.setObjectName("label")
        label1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(label1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        label1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(label1)
        self.statusbar.setObjectName("statusbar")
        label1.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(label1)
        QtCore.QMetaObject.connectSlotsByName(label1)

    def retranslateUi(self, label1):
        _translate = QtCore.QCoreApplication.translate
        label1.setWindowTitle(_translate("label1", "MainWindow"))
        self.button1.setText(_translate("label1", "click me!"))
        self.label.setText(_translate("label1", "My name is maryam."))
        self.menufile.setTitle(_translate("label1", "file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    label1 = QtWidgets.QMainWindow()
    ui = Ui_label1()
    ui.setupUi(label1)
    label1.show()
    sys.exit(app.exec_())
