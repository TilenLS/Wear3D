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
                                 "	background-color: #BCCEF8;\n"
                                 "	padding: 0;\n"
                                 "	margin: 0;\n"
                                 "	color: #000000;\n"
                                 "}\n"
                                 "\n"
                                 "#centralwidget{\n"
                                 "	background-color: #BCCEF8;\n"
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
        self.widget1.setMinimumSize(QSize(600, 700))
        self.widget1.setMaximumSize(QSize(600, 700))
        radius = 30
        self.widget1.setStyleSheet("background-color: #ECF2FF;\n"
                                   "border-top-left-radius:{0}px\n;"
                                   "border-bottom-left-radius:{0}px\n;"
                                   "border-top-right-radius:{0}px\n;"
                                   "border-bottom-right-radius:{0}px;\n".format(radius))
        self.vertical_layout = QGridLayout(self.widget1)
        self.vertical_layout.setContentsMargins(100,50,100,50)
        self.vertical_layout.setSpacing(20)
        self.central_layout.addWidget(self.widget1, 0, Qt.AlignCenter)

        self.register_account_label = QtWidgets.QLabel(self.centralwidget)
        self.register_account_label.setObjectName("register_account_label")
        self.register_account_label.setMinimumWidth(400)
        big_bold_font = QtGui.QFont()
        big_bold_font.setPointSize(30)
        big_bold_font.setBold(True)
        big_bold_font.setWeight(75)
        big_bold_font.setFamily("Bahnschrift Light")
        self.register_account_label.setAlignment(QtCore.Qt.AlignCenter)
        self.register_account_label.setFont(big_bold_font)
        self.vertical_layout.addWidget(self.register_account_label, 1, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.iconLabel = QtWidgets.QLabel(self.centralwidget, wordWrap=True)
        self.iconLabel.setObjectName("iconLabel")
        self.iconLabel.setMinimumWidth(130)
        self.iconLabel.setMinimumHeight(130)
        self.iconLabel.setPixmap(QPixmap(u":/icons/Icons/user-plus_focus.png"))
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setAlignment(Qt.AlignCenter)
        self.vertical_layout.addWidget(self.iconLabel, 0, 0, Qt.AlignHCenter)

        self.already_have_an_account_text = QtWidgets.QLabel(self.centralwidget)
        self.already_have_an_account_text.setObjectName("no_account_yet_text")
        text_font = QtGui.QFont()
        text_font.setPointSize(12)
        text_font.setFamily("Bahnschrift Light")
        self.already_have_an_account_text.setFont(text_font)
        self.vertical_layout.addWidget(self.already_have_an_account_text, 6, 0, Qt.AlignCenter | Qt.AlignBottom)

        self.sign_in_button = QtWidgets.QPushButton(self.centralwidget)
        self.sign_in_button.setObjectName("sign_in_button")
        self.sign_in_button.setFixedWidth(300)
        self.sign_in_button.setFixedHeight(60)
        self.sign_in_button.setFont(text_font)
        self.sign_in_button.setStyleSheet("QPushButton {\n"
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
        self.vertical_layout.addWidget(self.sign_in_button, 7, 0, Qt.AlignHCenter)

        self.username_input = QtWidgets.QLineEdit(self.centralwidget)
        self.username_input.setPlaceholderText("Please enter your email...")
        self.username_input.setObjectName("username_input")
        self.username_input.setMinimumWidth(410)
        self.username_input.setStyleSheet("QLineEdit {\n"
                                          "\tborder: 1px solid grey;\n"
                                          "\tbackground-color: #ECF2FF;\n"
                                          "}"
                                          )
        self.username_input.setFont(label_font)
        self.vertical_layout.addWidget(self.username_input, 2, 0, Qt.AlignLeft)

        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setPlaceholderText("Please enter your password...")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.password_input.setMinimumWidth(410)
        self.password_input.setStyleSheet("QLineEdit {\n"
                                          "\tborder: 1px solid grey;\n"
                                          "\tbackground-color: #ECF2FF;\n"
                                          "}"
                                          )
        self.password_input.setFont(label_font)
        self.vertical_layout.addWidget(self.password_input, 3, 0, Qt.AlignLeft)

        self.confirm_password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.confirm_password_input.setPlaceholderText("Please confirm your password...")
        self.confirm_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password_input.setObjectName("password_input")
        self.confirm_password_input.setMinimumWidth(410)
        self.confirm_password_input.setStyleSheet("QLineEdit {\n"
                                          "\tborder: 1px solid grey;\n"
                                          "\tbackground-color: #ECF2FF;\n"
                                          "}"
                                          )
        self.confirm_password_input.setFont(label_font)
        self.vertical_layout.addWidget(self.confirm_password_input, 4, 0, Qt.AlignLeft)

        self.register_button = QtWidgets.QPushButton(self.centralwidget)
        self.register_button.setObjectName("register_button")
        label_font.setBold(True)
        self.register_button.setFixedWidth(300)
        self.register_button.setFixedHeight(60)
        self.register_button.setFont(label_font)
        self.register_button.setStyleSheet("QPushButton {\n"
                                          "    border-radius: 5px;\n"
                                          "    background:#97DEFF;\n"
                                          "    color: #000000;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton::hover {\n"
                                          "    background:#62CDFF;\n"
                                          "    color: #000000;\n"
                                          "}")
        self.vertical_layout.addWidget(self.register_button, 5, 0, Qt.AlignHCenter)


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
        self.register_account_label.setText(_translate("MainWindow", "Register"))
        self.already_have_an_account_text.setText(_translate("MainWindow", "Already have an account?"))
        self.register_button.setText(_translate("MainWindow", "Register"))
        self.sign_in_button.setText(_translate("MainWindow", "Sign In"))