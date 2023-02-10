from PySide2 import QtCore, QtGui, QtWidgets

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

        self.register_account_label = QtWidgets.QLabel(self.centralwidget)
        self.register_account_label.setGeometry(QtCore.QRect(0, 20, 1200, 100))
        self.register_account_label.setObjectName("register_account_label")
        big_bold_font = QtGui.QFont()
        big_bold_font.setPointSize(35)
        big_bold_font.setBold(True)
        big_bold_font.setWeight(75)
        big_bold_font.setFamily("Bahnschrift Light")
        self.register_account_label.setAlignment(QtCore.Qt.AlignCenter)
        self.register_account_label.setFont(big_bold_font)

        self.already_have_an_account_text = QtWidgets.QLabel(self.centralwidget)
        self.already_have_an_account_text.setGeometry(QtCore.QRect(0, 693, 1200, 50))
        self.already_have_an_account_text.setObjectName("no_account_yet_text")
        text_font = QtGui.QFont()
        text_font.setPointSize(12)
        text_font.setFamily("Bahnschrift Light")
        self.already_have_an_account_text.setAlignment(QtCore.Qt.AlignCenter)
        self.already_have_an_account_text.setFont(text_font)

        self.sign_in_button = QtWidgets.QPushButton(self.centralwidget)
        self.sign_in_button.setGeometry(QtCore.QRect(550, 750, 100, 45))
        self.sign_in_button.setObjectName("register_button")
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
        label_font.setPointSize(20)
        label_font.setFamily("Bahnschrift Light")

        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(200, 150, 200, 50))
        self.username_label.setObjectName("username_label")
        self.username_label.setFont(label_font)

        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(200, 300, 200, 50))
        self.password_label.setObjectName("password_label")
        self.password_label.setFont(label_font)

        self.confirm_password_label = QtWidgets.QLabel(self.centralwidget)
        self.confirm_password_label.setGeometry(QtCore.QRect(200, 450, 400, 50))
        self.confirm_password_label.setObjectName("confirm_password_label")
        self.confirm_password_label.setFont(label_font)

        self.username_input = QtWidgets.QLineEdit(self.centralwidget)
        self.username_input.setGeometry(QtCore.QRect(200, 220, 800, 50))
        self.username_input.setPlaceholderText("Please enter your email...")
        self.username_input.setObjectName("username_input")
        self.username_input.setFont(label_font)

        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(200, 370, 800, 50))
        self.password_input.setPlaceholderText("Please enter your password...")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.password_input.setFont(label_font)

        self.confirm_password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.confirm_password_input.setGeometry(QtCore.QRect(200, 520, 800, 50))
        self.confirm_password_input.setPlaceholderText("Please enter your confirmed password...")
        self.confirm_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password_input.setObjectName("password_input")
        self.confirm_password_input.setFont(label_font)

        self.register_button = QtWidgets.QPushButton(self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(450, 620, 300, 70))
        self.register_button.setObjectName("sign_in_button")
        label_font.setBold(True)
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

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
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
        self.username_label.setText(_translate("MainWindow", "Username:"))
        self.password_label.setText(_translate("MainWindow", "Password:"))
        self.confirm_password_label.setText(_translate("MainWindow", "Confirm Password:"))
        self.register_button.setText(_translate("MainWindow", "Register"))
        self.sign_in_button.setText(_translate("MainWindow", "Sign In"))