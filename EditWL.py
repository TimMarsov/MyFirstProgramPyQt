import sys

from EditWLDesign import *
from PyQt5 import QtWidgets, QtGui
import json
import os
import configparser

def str_check(txt):
    while True:
        try:
            if txt[-1] == ' ':
                txt = txt[0:-1]
            elif txt[0] == ' ':
                txt = txt[1:]
            else:
                text = txt.lower()
                return text
        except IndexError:
            return txt


class WindowEdit(QtWidgets.QMainWindow, Ui_WorkWindow):
    SignalClose = QtCore.pyqtSignal(str) #создаю сигнал
    def __init__(self):
        super().__init__()
        self.setupUi(self) # Это нужно для инициализации нашего дизайна
        self.toolButton.setText('Save and exit')
        self.toolButton.adjustSize()

        self.toolButton.clicked.connect(self.save_tool)
        self.save_edited_button.clicked.connect(self.edit_select_item)

        self.listwidget_words.itemClicked.connect(self.select_item)
        self.listwidget_words.itemDoubleClicked.connect(self.double_click)
        self.load_file()
        self.phone_editbox.textChanged.connect(self.checking_return)
        QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+S'), self).activated.connect(self.conect)

    def closeEvent(self, event): #при закрытии приложения выполняю
        self.SignalClose.emit("fuck") #отправляю сигнал
    def showEvent(self, a0: QtGui.QShowEvent):
        self.load_file()

    def conect(self):
        text = self.phone_editbox.toPlainText()
        test_ls = text.split(' - ')
        if text == '':
            txt = str_check(QtGui.QGuiApplication.clipboard().text())
            self.phone_editbox.setText(txt + " - ")

        elif test_ls[1] != '':
            self.save_edited_button.click()
        else:
            txt = str_check(QtGui.QGuiApplication.clipboard().text())
            self.phone_editbox.setText(text + txt)

    def double_click(self):
        self.listwidget_words.clearSelection()
        self.phone_editbox.setText('')
        if [] == self.listwidget_words.selectedItems():
            if self.sel_it > -1:
                self.listwidget_words.item(self.sel_it).setIcon(QtGui.QIcon(None))

    def checking_return(self):
        if '\n' in self.phone_editbox.toPlainText():
            self.phone_editbox.setText(self.phone_editbox.toPlainText().replace('\n', ''))
            # self.phone_editbox.moveCursor(QtGui.QTextCursor.End)
            self.save_edited_button.click()

    def edit_select_item(self):
        if [] == self.listwidget_words.selectedItems():
            if self.phone_editbox.toPlainText() != "":
                self.listwidget_words.addItem((self.phone_editbox.toPlainText()))
                self.phone_editbox.setText('')
                self.double_click()
        else:
            index = self.listwidget_words.currentRow()
            self.listwidget_words.item(index).setText(self.phone_editbox.toPlainText())
            self.phone_editbox.setText('')
            self.double_click()
            if self.listwidget_words.item(index).text() == '':
                self.listwidget_words.takeItem(index)

    sel_it = -1
    check_clicl = 0

    def select_item(self):
        index = self.listwidget_words.currentRow()
        if index != self.sel_it:
            if self.sel_it < self.listwidget_words.count():
                if self.sel_it >= 0:
                    self.listwidget_words.item(self.sel_it).setIcon(QtGui.QIcon(None))
        self.listwidget_words.item(index).setIcon(QtGui.QIcon('icon.png'))
        self.phone_editbox.setText(self.listwidget_words.item(index).text())
        if index == self.sel_it and self.check_clicl == 0:
            # if self.check_clicl > 0:
            #     self.check_clicl = 0
            #     return None
            # self.check_clicl =1
            self.check_clicl = 1
            self.double_click()
        else:
            self.check_clicl = 0

        self.sel_it = index


    def save_tool(self):
        index = 0
        key = []
        value = []
        while index < self.listwidget_words.count():
            if ' - ' in self.listwidget_words.item(index).text():
                line = self.listwidget_words.item(index).text().split(" - ")
                key.append(line[0])
                value.append(line[1])
                index += 1
            else:
                self.phone_editbox.setText('Ошибка! Упущен разделитель " - "; проверьте наличие пропусков возле дефиса')
                self.phone_editbox.moveCursor(QtGui.QTextCursor.End)
                return None
        with open(self.load_wl(), 'w') as f:
            word_dict = dict(zip(key, value))
            json.dump(word_dict, f)
            print(word_dict)
        self.close()


    def load_wl(self):
        config = configparser.ConfigParser()
        config.read('data\setting.ini')
        return str(config.get("Settings", "path wl"))
    words = {}
    keys = []
    values = []

    def load_file(self):
        self.listwidget_words.clear()
        if os.path.exists(self.load_wl()):
            with open(self.load_wl(), 'r') as f:
                try:
                    self.words = json.load(f)
                    self.keys, self.values = zip(*self.words.items())
                    for index, key in enumerate(self.keys):
                        self.listwidget_words.addItem(str(key) + ' - ' + str(self.values[index]))
                except json.decoder.JSONDecodeError:
                    self.listwidget_words.addItem("пример - example")
        else:
            dir = self.load_wl().split('/')
            if not os.path.exists(dir[0]):
                os.makedirs(dir[0])
            open(self.load_wl(), 'a')
            self.listwidget_words.addItem("пример - example")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = WindowEdit()
    MainWindow.show()
    sys.exit(app.exec_())