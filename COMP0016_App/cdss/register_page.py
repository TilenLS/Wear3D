from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QSize
from PySide2.QtWidgets import QWidget, QVBoxLayout, QFrame, QGridLayout

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_RegisterPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 850)
        MainWindow.setStyleSheet(u"*{\n"
                                 "	border: none;\n"
                                 "	background-color: transparent;\n"
                                 "	background: transparent;\n"
                                 "	padding: 0;\n"
                                 "	margin: 0;\n"
                                 "	color: #fff;\n"
                                 "}\n"
                                 "\n"
                                 "#centralwidget,  #homeButton,  #mainBodyContent,  QLineEdit{\n"
                                 "	background-color: #1b1b27;\n"
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
        self.widget1.setMinimumSize(QSize(900, 800))
        self.widget1.setMaximumSize(16777215, 16777215)
        self.widget1.setStyleSheet("background-color: #515064")
        self.vertical_layout = QGridLayout(self.widget1)
        self.vertical_layout.setContentsMargins(100,50,100,50)
        self.vertical_layout.setSpacing(20)
        self.central_layout.addWidget(self.widget1, 0, Qt.AlignCenter)

        self.register_account_label = QtWidgets.QLabel(self.centralwidget)
        self.register_account_label.setObjectName("register_account_label")
        self.register_account_label.setMinimumWidth(600)
        big_bold_font = QtGui.QFont()
        big_bold_font.setPointSize(30)
        big_bold_font.setBold(True)
        big_bold_font.setWeight(75)
        big_bold_font.setFamily("Bahnschrift Light")
        self.register_account_label.setAlignment(QtCore.Qt.AlignCenter)
        self.register_account_label.setFont(big_bold_font)
        self.vertical_layout.addWidget(self.register_account_label, 0, 0, Qt.AlignHCenter)

        self.already_have_an_account_text = QtWidgets.QLabel(self.centralwidget)
        self.already_have_an_account_text.setObjectName("no_account_yet_text")
        text_font = QtGui.QFont()
        text_font.setPointSize(12)
        text_font.setFamily("Bahnschrift Light")
        self.already_have_an_account_text.setFont(text_font)
        self.vertical_layout.addWidget(self.already_have_an_account_text, 6, 0, Qt.AlignHCenter)

        self.sign_in_button = QtWidgets.QPushButton(self.centralwidget)
        self.sign_in_button.setObjectName("sign_in_button")
        self.sign_in_button.setFixedWidth(300)
        self.sign_in_button.setFixedHeight(60)
        self.sign_in_button.setFont(text_font)
        self.sign_in_button.setStyleSheet("QPushButton {\n"
                                           "    border-radius: 5px;\n"
                                           "    background:#5D3891;\n"
                                           "    color: #FFCEFE;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton::hover {\n"
                                           "    background:#BFACE2;\n"
                                           "    color: #181D31;\n"
                                           "}")

        label_font = QtGui.QFont()
        label_font.setPointSize(14)
        label_font.setFamily("Bahnschrift Light")
        self.vertical_layout.addWidget(self.sign_in_button, 5, 0, Qt.AlignHCenter)

        self.username_input = QtWidgets.QLineEdit(self.centralwidget)
        self.username_input.setPlaceholderText("Please enter your email...")
        self.username_input.setObjectName("username_input")
        self.username_input.setMinimumWidth(500)
        self.username_input.setStyleSheet("QLineEdit {\n"
                                          "\tbackground-color: #282732;\n"
                                          "}"
                                          )
        self.username_input.setFont(label_font)
        self.vertical_layout.addWidget(self.username_input, 1, 0, Qt.AlignHCenter)

        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setPlaceholderText("Please enter your password...")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.password_input.setMinimumWidth(500)
        self.password_input.setStyleSheet("QLineEdit {\n"
                                          "\tbackground-color: #282732;\n"
                                          "}"
                                          )
        self.password_input.setFont(label_font)
        self.vertical_layout.addWidget(self.password_input, 2, 0, Qt.AlignHCenter)

        self.confirm_password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.confirm_password_input.setPlaceholderText("Please confirm your password...")
        self.confirm_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password_input.setObjectName("password_input")
        self.confirm_password_input.setMinimumWidth(500)
        self.confirm_password_input.setStyleSheet("QLineEdit {\n"
                                          "\tbackground-color: #282732;\n"
                                          "}"
                                          )
        self.confirm_password_input.setFont(label_font)
        self.vertical_layout.addWidget(self.confirm_password_input, 3, 0, Qt.AlignHCenter)

        self.register_button = QtWidgets.QPushButton(self.centralwidget)
        self.register_button.setObjectName("register_button")
        label_font.setBold(True)
        self.register_button.setFixedWidth(400)
        self.register_button.setFixedHeight(80)
        self.register_button.setFont(label_font)
        self.register_button.setStyleSheet("QPushButton {\n"
                                          "    border-radius: 5px;\n"
                                          "    background:#C3ACD0;\n"
                                          "    color: #181D31;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton::hover {\n"
                                          "    background:#BFACE2;\n"
                                          "    color: #674188;\n"
                                          "}")
        self.vertical_layout.addWidget(self.register_button, 4, 0, Qt.AlignHCenter)


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
        self.register_account_label.setText(_translate("MainWindow", "Register Account"))
        self.already_have_an_account_text.setText(_translate("MainWindow", "Already have an account?"))
        self.register_button.setText(_translate("MainWindow", "Register"))
        self.sign_in_button.setText(_translate("MainWindow", "Sign In"))