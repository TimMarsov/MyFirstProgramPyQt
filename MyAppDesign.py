from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Checking_main(object):
    def setupUi(self, MainWindow):
        icon = QIcon()
        icon.addPixmap(QPixmap("icon.ico"), QIcon.Selected, QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setObjectName("Учи английский")
        MainWindow.resize(651, 476)
        MainWindow.setStyleSheet("border-radius: 7px;\n"
                                 "background-color: #1B1D23;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setStyleSheet("background-color: #2C313C;")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout_6.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listView = QListWidget(self.centralwidget)
        self.listView.setStyleSheet("color: white;\n"
                                    "border-radius: 7px;\n"
                                    "background-color: #2C313C;")
        self.listView.setObjectName("listWidget")
        self.gridLayout_3.addWidget(self.listView, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QLabel(self.centralwidget)
        self.label.setMinimumSize(QSize(0, 60))
        self.label.setObjectName("label")
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("background-color: #2C313C; color: #d1d1d1;")
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 2, 0, 1, 1)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setMaximumSize(QSize(16777215, 50))
        self.textEdit.setStyleSheet("border-radius: 7px;\n"
                                    "background-color: rgb(255, 255, 255);")
        font = QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 3, 0, 1, 1)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setContentsMargins(-1, 10, -1, 6)
        self.gridLayout_5.setVerticalSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QSize(0, 35))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText('Готово!')
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    color: white;\n"
                                      "    border-radius: 7px;\n"
                                      "    background-color: #595F76;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "    background-color: #50566E;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed{\n"
                                      "    background-color: #434965;\n"
                                      "}")
        self.gridLayout_5.addWidget(self.pushButton, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 4, 0, 1, 1)
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setStyleSheet("QProgressBar{\n"
                                       "  background: rgba(255,255,255,0.1);\n"
                                       "}\n"
                                       "\n"
                                       "QProgressBar::chunk {\n"
                                       "  animation: load 3s normal forwards;\n"
                                       "  box-shadow: 0 10px 40px -10px #fff;\n"
                                       "  border-radius: 7px;\n"
                                       "  background: #c8c8c8;\n"
                                       "\n"
                                       "}")
        self.gridLayout_6.addWidget(self.progressBar, 5, 0, 1, 1)
        self.progressBar.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 651, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.setStyleSheet(
            "background-color: #2C313C; color: white; selection-color: yellow; selection-background-color: #454d5e;")
        self.menu = self.menubar.addMenu("Файл")
        self.setting = self.menubar.addMenu("Настройки")
        self.settint_ui = self.setting.addAction("Основные")
        self.menu_open = self.menu.addAction("Открыть словарь")
        self.menu_reload = self.menu.addAction("Обновить словарь")
        self.menu_edit = self.menu.addAction("Редактировать словарь")

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ну ты это... Слова-то учи"))
        self.listView.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Готово!"))
        self.label.setText(_translate("MainWindow", "Оу, а вы из франции"))
        self.label_2.setText(_translate("MainWindow", ""))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Checking_main()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
