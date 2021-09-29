from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ClearPokidovaDesign import *
import json
import EditWL
import SettingWindow
import random
import os
import configparser


class ProgramMain(QMainWindow, Checking_main):
    vl_autoupdate = "1"
    vl_win_error = "0"
    vl_promting = "1"
    vl_new_wl = "1"
    vl_path_wl = ""
    word = []
    words = {}
    list_1 = []
    list_0 = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.menu_reload.triggered.connect(self.reload_wl)
        self.menu_edit.triggered.connect(self.open_edit_wl)
        self.menu_open.triggered.connect(self.openFileNameDialog)
        self.settint_update.triggered.connect(self.updade_app)
        self.settint_ui.triggered.connect(self.ui_setting_app)
        self.pushButton.clicked.connect(self.button_clicked)
        self.textEdit.textChanged.connect(self.copy_the_text)
        self.WinSetting = SettingWindow.WindowSetting() #инициализирую окно настроек
        self.WinSetting.SignalClose.connect(self.mySignalCloseSetting) #принимаю сигнал с окна настроек
        self.WinEditWl = EditWL.WindowEdit() #инициализирую окно редактора
        self.WinEditWl.SignalClose.connect(self.reload_wl)

        self.openSetting()
        self.test_file()
        self.open_file()
        self.getwords()

    def mySignalCloseSetting(self, data):
        self.openSetting()
        self.reload_wl()

    def ui_setting_app(self):
        self.WinSetting.show()

    def updade_app(self):
        print(self.vl_autoupdate)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Words List (*.json);;All Files (*)", options=options)
        if fileName:
            print(fileName)
            self.vl_path_wl = fileName
            self.saveSetting()
            self.reload_wl()

    def openSetting(self):
        config = configparser.ConfigParser()
        config.read('data\setting.ini')
        self.vl_autoupdate = str(config.get("Settings", "autoupdate"))
        self.vl_promting = str(config.get("Settings", "promting"))
        self.vl_win_error = str(config.get("Settings", "win_error"))
        self.vl_new_wl = str(config.get("Settings", "new_wl"))
        self.vl_path_wl = str(config.get("Settings", "path wl"))

    def saveSetting(self):
        config = configparser.ConfigParser()
        config.add_section("Settings")
        config.set("Settings", "path wl", self.vl_path_wl)
        config.set("Settings", "promting", self.vl_promting)
        config.set("Settings", "autoupdate", self.vl_autoupdate)
        config.set("Settings", "new_wl", self.vl_new_wl)
        config.set("Settings", "win_error", self.vl_win_error)
        with open('data\setting.ini', 'w') as f:
            config.write(f)

    def test_file(self):
        if os.path.exists(self.load_wl()):
            with open(self.load_wl(), 'r') as f:
                try:
                    json.load(f)
                    print('all good')
                except json.decoder.JSONDecodeError:
                    print('fuck, repair')
                    self.repair_json()
        else:
            dir = self.load_wl().split('/')
            if not os.path.exists(dir[0]):
                os.makedirs(dir[0])
            open(self.load_wl(), 'a')
            self.test_file()

    def repair_json(self):
        with open(self.load_wl(), 'w') as fl:
            words = {"Пример": "example"}
            json.dump(words, fl)

    def reload_wl(self):
        with open(self.load_wl(), 'r') as fl:
            if fl.read() == "":
                print('косяк')
                self.repair_json()
        self.open_file()
        self.getwords()
        self.progressBar.setProperty("value", 0)

    def open_edit_wl(self):
        self.WinEditWl.show()

    def load_wl(self):
        self.openSetting()
        print(self.vl_path_wl)
        return self.vl_path_wl

    def open_file(self):
        with open(self.load_wl(), 'r') as f:
            self.words = json.load(f)
            self.list_1 = []
            self.list_0 = list(self.words)

    def getwords(self):
        if set(self.list_1) == set(self.list_0):
            self.label.setText('Поздравляю! Все кончилось')
        else:
            self.word = random.choice(list(self.words.items()))
            if self.word[0] not in self.list_1:
                self.label.setText(self.word[0])
                self.label.setAlignment(Qt.AlignCenter)
            else:
                self.getwords()

    def checking_word(self):
        if str(self.word[1]) == str(self.textEdit.toPlainText()):
            print('молодец!!!')
            self.textEdit.setText('')
            self.list_1.append(self.word[0])
            self.listView.addItem("Перевел " + self.word[0] + ' как ' + self.word[1])
            self.listView.scrollToBottom()
            progress = len(self.list_1) / len(self.list_0) * 100
            self.progressBar.setProperty("value", progress)
            self.getwords()
        else:
            print("Ну ты и старый дурак, иди учи опять")
            if '\n' in str(self.textEdit.toPlainText()):
                text = self.textEdit.toPlainText()
                text = text.replace('\n', '')
                self.textEdit.setText(text)
            self.textEdit.moveCursor(QTextCursor.End)
            matches = 0
            character_error = 0
            for letter1, letter2 in zip(str(self.textEdit.toPlainText()), self.word[1]):
                if letter1 == letter2:
                    matches += 1
                else:
                    character_error = matches
            print(matches)
            print(character_error)
            print_word = self.word[1]
            if character_error == 0:
                character_error = matches
            self.label_2.setText(
                '<html><head/><body><p><span style=\" font-weight:600; font-size:10pt; color: #d1d1d1;\">' + print_word[
                                                                                                             :character_error] + '</span><span style=\" font-weight:600; font-size:10pt; color:#ff0000;\">' + print_word[
                                                                                                                                                                                                              character_error:character_error + 1] + '</span><span style=" font-weight:600; font-size:10pt; color:#11ad09;">' + print_word[
                                                                                                                                                                                                                                                                                                                                character_error + 1:matches + 1] + '</span></p></body></html>')
            print(print_word[:matches + 2])
            print(print_word[:character_error] + "!" + print_word[character_error:character_error + 1])
            # if os.path.exists('data/pic.lol'):
            #     self.window2 = App2()
            #     self.window2.show()

    def button_clicked(self, val=0):
        if val == 0:
            if '\n' in str(self.textEdit.toPlainText()):
                text = self.textEdit.toPlainText()
                text = text.replace('\n', '')
                self.textEdit.setText(text)
                self.textEdit.setText(EditWL.str_check(self.textEdit.toPlainText()))
            if str(self.textEdit.toPlainText()) != '':
                self.checking_word()
        else:
            if '\n' in str(self.textEdit.toPlainText()):
                text = self.textEdit.toPlainText()
                text = text.replace('\n', '')
                self.textEdit.setText(text)
                self.textEdit.setText(EditWL.str_check(self.textEdit.toPlainText()))
            if str(self.textEdit.toPlainText()) != '':
                self.checking_word()

    def copy_the_text(self):
        text = self.textEdit.toPlainText()
        if '\n' in text:
            self.button_clicked(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = ProgramMain()
    MainWindow.show()
    sys.exit(app.exec_())