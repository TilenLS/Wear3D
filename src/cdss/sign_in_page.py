from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QObject, QSize
from PySide2.QtWidgets import QFileDialog, QMainWindow, QMessageBox, QFrame, QVBoxLayout, QGridLayout

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SignInPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 850)
        MainWindow.setStyleSheet(u"*{\n"
                                 "	border: none;\n"
                                 "	background-color: transparent;\n"
                                 "	background: transparent;\n"
                                 "	padding: 0;\n"
                                 "	margin: 0;\n"
                                 "	color: #000000;\n"
                                 "}\n"
                                 "\n"
                                 "#centralwidget{\n"
                                 "	background-color: #ECF2FF;\n"
                                 "}\n"
                                 "\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.central_layout = QVBoxLayout(self.centralwidget)
        self.central_layout.setContentsMargins(150,50,150,50)
        MainWindow.setCentralWidget(self.centralwidget)

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)

        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setObjectName("widget1")
        self.widget1.setMinimumSize(QSize(800, 800))
        self.widget1.setStyleSheet("background-color: #BCCEF8")
        self.vertical_layout = QGridLayout(self.widget1)
        self.vertical_layout.setContentsMargins(100,50,100,50)
        self.vertical_layout.setSpacing(20)
        self.central_layout.addWidget(self.widget1, 0, Qt.AlignCenter)


        self.account_login_label = QtWidgets.QLabel(self.centralwidget, wordWrap=True)
        self.account_login_label.setObjectName("account_login_label")
        self.account_login_label.setMinimumWidth(600)
        big_bold_font = QtGui.QFont()
        big_bold_font.setPointSize(30)
        big_bold_font.setBold(True)
        big_bold_font.setWeight(75)
        big_bold_font.setFamily("Bahnschrift Light")
        self.account_login_label.setFont(big_bold_font)
        self.account_login_label.setAlignment(Qt.AlignCenter)
        self.vertical_layout.addWidget(self.account_login_label, 0, 0, Qt.AlignHCenter)

        self.reminder_text = QtWidgets.QLabel(self.centralwidget, wordWrap=True)
        self.reminder_text.setObjectName("reminder_text")
        text_font = QtGui.QFont()
        text_font.setPointSize(14)
        text_font.setFamily("Bahnschrift Light")
        self.reminder_text.setFont(text_font)
        self.reminder_text.setAlignment(Qt.AlignCenter)
        self.vertical_layout.addWidget(self.reminder_text, 1, 0, Qt.AlignHCenter)

        self.no_account_yet_text = QtWidgets.QLabel(self.centralwidget)
        self.no_account_yet_text.setObjectName("no_account_yet_text")
        text_font = QtGui.QFont()
        text_font.setPointSize(12)
        text_font.setFamily("Bahnschrift Light")
        self.no_account_yet_text.setFont(text_font)
        self.vertical_layout.addWidget(self.no_account_yet_text, 5, 0, Qt.AlignHCenter)

        self.register_button = QtWidgets.QPushButton(self.centralwidget)
        self.register_button.setObjectName("register_button")
        self.register_button.setFixedWidth(300)
        self.register_button.setFixedHeight(60)
        self.register_button.setFont(text_font)
        self.register_button.setStyleSheet("QPushButton {\n"
                                       "    border-radius: 5px;\n"
                                       "    background:#8DCBE6;\n"
                                       "    color: #111111;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton::hover {\n"
                                       "    background:#AEE2FF;\n"
                                       "    color: #111111;\n"
                                       "}")

        label_font = QtGui.QFont()
        label_font.setPointSize(14)
        label_font.setFamily("Bahnschrift Light")
        self.vertical_layout.addWidget(self.register_button, 6, 0, Qt.AlignHCenter)

        self.username_input = QtWidgets.QLineEdit(self.centralwidget)
        self.username_input.setPlaceholderText("Please enter your email...")
        self.username_input.setObjectName("username_input")
        self.username_input.setMinimumWidth(500)
        self.username_input.setStyleSheet("QLineEdit {\n"
                                          "\tbackground-color: #ECF2FF;\n"
                                          "}"
                                          )
        self.username_input.setFont(label_font)
        self.vertical_layout.addWidget(self.username_input, 2, 0, Qt.AlignHCenter)

        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setPlaceholderText("Please enter your password...")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.password_input.setMinimumWidth(500)
        self.password_input.setStyleSheet("QLineEdit {\n"
                                          "\tbackground-color: #ECF2FF;\n"
                                          "}"
                                          )
        self.password_input.setFont(label_font)
        self.vertical_layout.addWidget(self.password_input, 3, 0, Qt.AlignHCenter)

        self.sign_in_button = QtWidgets.QPushButton(self.centralwidget)
        self.sign_in_button.setObjectName("sign_in_button")
        self.sign_in_button.setFixedWidth(300)
        self.sign_in_button.setFixedHeight(60)
        label_font.setBold(True)
        self.sign_in_button.setFont(label_font)
        self.sign_in_button.setStyleSheet("QPushButton {\n"
                                       "    border-radius: 5px;\n"
                                       "    background:#B9F3FC;\n"
                                       "    color: #000000;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton::hover {\n"
                                       "    background:#E3F6FF;\n"
                                       "    color: #000000;\n"
                                       "}")
        self.vertical_layout.addWidget(self.sign_in_button, 4, 0, Qt.AlignHCenter)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.account_login_label.setText(_translate("MainWindow", "Account Login"))
        self.reminder_text.setText(_translate("MainWindow", "Please enter your details to get sign in to your account"))
        self.no_account_yet_text.setText(_translate("MainWindow", "No account yet?"))
        self.sign_in_button.setText(_translate("MainWindow", "Sign In"))
        self.register_button.setText(_translate("MainWindow", "Register"))