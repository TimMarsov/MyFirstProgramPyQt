# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WorkWindow(object):
    def setupUi(self, WorkWindow):
        WorkWindow.setObjectName("WorkWindow")
        WorkWindow.resize(507, 391)
        self.centralwidget = QtWidgets.QWidget(WorkWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listwidget_words = QtWidgets.QListWidget(self.centralwidget)
        self.listwidget_words.setGeometry(QtCore.QRect(20, 40, 461, 201))
        self.listwidget_words.setObjectName("list_phones")
        self.phone_editbox = QtWidgets.QTextEdit(self.centralwidget)
        self.phone_editbox.setGeometry(QtCore.QRect(20, 250, 461, 51))
        self.phone_editbox.setObjectName("phone_editbox")
        self.save_edited_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_edited_button.setGeometry(QtCore.QRect(20, 310, 461, 31))
        self.save_edited_button.setObjectName("save_edited_button")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(20, 10, 61, 19))
        self.toolButton.setObjectName("toolButton")
        WorkWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WorkWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 507, 21))
        self.menubar.setObjectName("menubar")
        WorkWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WorkWindow)
        self.statusbar.setObjectName("statusbar")
        WorkWindow.setStatusBar(self.statusbar)

        self.retranslateUi(WorkWindow)
        QtCore.QMetaObject.connectSlotsByName(WorkWindow)

    def retranslateUi(self, WorkWindow):
        _translate = QtCore.QCoreApplication.translate
        WorkWindow.setWindowTitle(_translate("WorkWindow", "MainWindow"))
        self.save_edited_button.setText(_translate("WorkWindow", "Принять"))
        self.toolButton.setText(_translate("WorkWindow", "Save"))