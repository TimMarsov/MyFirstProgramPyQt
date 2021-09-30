import SettingWindowDesign
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import configparser
import sys
import ClearPokidovaCode

class WindowSetting(QMainWindow, SettingWindowDesign.Setting_ui):
    vl_autoupdate = "1"
    vl_win_error = "0"
    vl_promting = "1"
    vl_new_wl = "1"
    vl_path_wl = ""
    vl_version = "0.3"
    SignalClose = pyqtSignal(str) #создаю сигнал
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.radio_promting.clicked.connect(self.promting)
        self.radio_autoupdate.clicked.connect(self.autoupdate)
        self.radio_window_error.clicked.connect(self.error_win)
        self.radio_newWL.clicked.connect(self.new_wl)
        self.Save_st_button.clicked.connect(self.saveSetting)
        self.pushButton_3.clicked.connect(self.openFileNameDialog)
        self.close_button.clicked.connect(self.openSetting)
        self.openSetting()


    def closeEvent(self, event):
        self.SignalClose.emit("fuck") #отправляю сигнал

    def enable_button(self):
        self.Save_st_button.setEnabled(True)
        self.close_button.setEnabled(True)

    def promting(self):
        self.enable_button()
        if self.radio_promting.isChecked() == True:
            self.vl_promting = "1"
        else:
            self.vl_promting = "0"

    def autoupdate(self):
        self.enable_button()
        if self.radio_autoupdate.isChecked() == True:
            self.vl_autoupdate = "1"
        else:
            self.vl_autoupdate = "0"

    def new_wl(self):
        self.enable_button()
        if self.radio_newWL.isChecked() == True:
            self.vl_new_wl = "1"
        else:
            self.vl_new_wl = "0"

    def error_win(self):
        self.enable_button()
        if self.radio_window_error.isChecked() == True:
            self.vl_win_error = "1"
        else:
            self.vl_win_error = "0"

    def saveSetting(self):
        config = configparser.ConfigParser()
        config.add_section("Settings")
        config.set("Settings", "promting", self.vl_promting)
        config.set("Settings", "autoupdate", self.vl_autoupdate)
        config.set("Settings", "new_wl", self.vl_new_wl)
        config.set("Settings", "win_error", self.vl_win_error)
        config.set("Settings", "path wl", self.vl_path_wl)
        config.set("Settings", "version", self.vl_version)
        with open('data\setting.ini', 'w') as f:
            config.write(f)

    def openSetting(self):
        config = configparser.ConfigParser()
        config.read('data\setting.ini')
        self.vl_autoupdate = str(config.get("Settings", "autoupdate"))
        self.vl_promting = str(config.get("Settings", "promting"))
        self.vl_win_error = str(config.get("Settings", "win_error"))
        self.vl_new_wl = str(config.get("Settings", "new_wl"))
        self.vl_path_wl = str(config.get("Settings", "path wl"))
        self.vl_version = str(config.get("Settings", "version"))
        self.checkingSet()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Words List (*.json);;All Files (*)", options=options)
        if fileName:
            print(fileName)
            self.vl_path_wl = str(fileName)
            self.enable_button()

    def checkingSet(self):
        if self.vl_autoupdate == "1":
            self.radio_autoupdate.setChecked(True)
        else:
            self.radio_autoupdate.setChecked(False)
        if self.vl_promting == "1":
            self.radio_promting.setChecked(True)
        else:
            self.radio_promting.setChecked(False)
        if self.vl_new_wl == "1":
            self.radio_newWL.setChecked(True)
        else:
            self.radio_newWL.setChecked(False)
        if self.vl_win_error == "1":
            self.radio_window_error.setChecked(True)
        else:
            self.radio_window_error.setChecked(False)

