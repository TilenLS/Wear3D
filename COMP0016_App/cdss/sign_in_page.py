from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QObject, QSize
from PySide2.QtWidgets import QFileDialog, QMainWindow, QMessageBox, QFrame, QVBoxLayout


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

        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setObjectName("widget1")
        self.widget1.setMinimumSize(QSize(800, 800))
        self.widget1.move(200, 50)
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setStyleSheet("background-color: #515064")

        layout = QVBoxLayout()
        layout.addWidget(self.frame)
        self.widget1.setLayout(layout)


        self.account_login_label = QtWidgets.QLabel(self.centralwidget)
        self.account_login_label.setGeometry(QtCore.QRect(0, 80, 1200, 100))
        self.account_login_label.setObjectName("account_login_label")
        big_bold_font = QtGui.QFont()
        big_bold_font.setPointSize(35)
        big_bold_font.setBold(True)
        big_bold_font.setWeight(75)
        big_bold_font.setFamily("Bahnschrift Light")
        self.account_login_label.setAlignment(QtCore.Qt.AlignCenter)
        self.account_login_label.setFont(big_bold_font)

        self.reminder_text = QtWidgets.QLabel(self.centralwidget)
        self.reminder_text.setGeometry(QtCore.QRect(0, 200, 1200, 50))
        self.reminder_text.setObjectName("reminder_text")
        text_font = QtGui.QFont()
        text_font.setPointSize(14)
        text_font.setFamily("Bahnschrift Light")
        self.reminder_text.setAlignment(QtCore.Qt.AlignCenter)
        self.reminder_text.setFont(text_font)

        self.no_account_yet_text = QtWidgets.QLabel(self.centralwidget)
        self.no_account_yet_text.setGeometry(QtCore.QRect(0, 680, 1200, 50))
        self.no_account_yet_text.setObjectName("no_account_yet_text")
        text_font = QtGui.QFont()
        text_font.setPointSize(12)
        text_font.setFamily("Bahnschrift Light")
        self.no_account_yet_text.setAlignment(QtCore.Qt.AlignCenter)
        self.no_account_yet_text.setFont(text_font)

        self.register_button = QtWidgets.QPushButton(self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(550, 750, 100, 45))
        self.register_button.setObjectName("register_button")
        self.register_button.setFont(text_font)
        self.register_button.setStyleSheet("QPushButton {\n"
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

        self.username_input = QtWidgets.QLineEdit(self.centralwidget)
        self.username_input.setGeometry(QtCore.QRect(350, 320, 500, 70))
        self.username_input.setPlaceholderText("Please enter your email...")
        self.username_input.setObjectName("username_input")
        self.username_input.setFont(label_font)

        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(350, 470, 500, 70))
        self.password_input.setPlaceholderText("Please enter your password...")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.password_input.setFont(label_font)

        self.sign_in_button = QtWidgets.QPushButton(self.centralwidget)
        self.sign_in_button.setGeometry(QtCore.QRect(450, 600, 300, 70))
        self.sign_in_button.setObjectName("sign_in_button")
        label_font.setBold(True)
        self.sign_in_button.setFont(label_font)
        self.sign_in_button.setStyleSheet("QPushButton {\n"
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
        self.account_login_label.setText(_translate("MainWindow", "Account Login"))
        self.reminder_text.setText(_translate("MainWindow", "Please enter your details to get sign in to your account"))
        self.no_account_yet_text.setText(_translate("MainWindow", "No account yet?"))
        self.sign_in_button.setText(_translate("MainWindow", "Sign In"))
        self.register_button.setText(_translate("MainWindow", "Register"))