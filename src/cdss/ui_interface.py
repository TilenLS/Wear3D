# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceTIzdfT.ui'
## Form generated from reading UI file 'interfaceYDckni.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os

from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from typing import Any

from model import AppFunctions
from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget
from iconify.qt import QtCore

import QSS_Resources_rc

class Ui_HomePage(object):
    def setupUi(self, MainWindow, patientNumber, imageViewer):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 850)
        MainWindow.setMinimumSize(QSize(1200, 850))


        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #000000;\n"
"}\n"
"\n"
"#centralwidget,  #homeButton,  #mainBodyContent,  QLineEdit{\n"
"	background-color: #FFFFFF;\n"
"}\n"
"\n"
"#mainBody,  #viewingTools{\n"
"	background-color: #ECF2FF;\n"
"}\n"
"\n"
"#header{\n"
"	background-color: #BCCEF8;\n"
"}\n"
"\n"                                
"#pushButton{\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 5px;\n"
"}\n"
"\n"
"#homeButton{\n"
"	border-left: 3px solid #cc5bce;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#widget_5,  #widget_6 {\n"
"	background-color: #ECF2FF;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menuButton = QPushButton(self.frame_2)
        self.menuButton.setObjectName(u"menuButton")
        self.menuButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/Icons/align-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.menuButton, 0, Qt.AlignLeft)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignLeft)

        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy)
        self.mainBody.setMinimumSize(QSize(784, 500))
        self.horizontalLayout_2 = QHBoxLayout(self.mainBody)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 9, 0, 0)
        self.leftMenu = QCustomSlideMenu(self.mainBody)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(200, 0))
        self.verticalLayout_3 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 20)
        self.widget = QWidget(self.leftMenu)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(200, 500))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 0, 0, 0)
        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.homeButton = QPushButton(self.frame_3)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeButton.setStyleSheet(u"background-color: #FFFFFF;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/home_focus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon3)
        self.homeButton.setIconSize(QSize(16, 16))

        self.verticalLayout_5.addWidget(self.homeButton)

        self.viewButton = QPushButton(self.frame_3)
        self.viewButton.setObjectName(u"viewButton")
        self.viewButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/archive_focus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.viewButton.setIcon(icon4)
        self.viewButton.setIconSize(QSize(16, 16))


        self.verticalLayout_5.addWidget(self.viewButton)


        self.analysisButton = QPushButton(self.frame_3)
        self.analysisButton.setObjectName(u"analysisButton")
        self.analysisButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/activity_focus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.analysisButton.setIcon(icon5)
        self.analysisButton.setIconSize(QSize(16, 16))

        self.verticalLayout_5.addWidget(self.analysisButton)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout_2.addWidget(self.leftMenu)

        self.mainBodyContent = QWidget(self.mainBody)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        self.verticalLayout_2 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pages = QCustomStackedWidget(self.mainBodyContent)
        self.pages.setObjectName(u"pages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.vboxLayout = QVBoxLayout(self.homePage)
        self.vboxLayout.setSpacing(0)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.homePage)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_14 = QVBoxLayout(self.widget_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_6 = QFrame(self.widget_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)

        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)


        self.showPatientFormButton = QPushButton(self.frame_6)
        self.showPatientFormButton.setObjectName(u"showPatientFormButton")
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.showPatientFormButton.setFont(font2)
        self.showPatientFormButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/Icons/plus-square_focus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.showPatientFormButton.setIcon(icon9)
        self.showPatientFormButton.setIconSize(QSize(24, 26))

        self.horizontalLayout_5.addWidget(self.showPatientFormButton, 0, Qt.AlignRight)


        self.verticalLayout_14.addWidget(self.frame_6)

        self.tableWidget = QTableWidget(self.widget_4)
        if (self.tableWidget.columnCount() < 17):
            self.tableWidget.setColumnCount(17)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        self.tableWidget.setObjectName(u"tableWidget")

        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setStyleSheet(
                "QHeaderView::section{"
                "border-top:1px solid #000000;"
                "border-left:0px solid #000000;"
                "border-right:1px solid #000000;"
                "border-bottom: 1px solid #000000;"
                "background-color:#D2DAFF;"
                "padding:4px;"
                "}"
                "QTableCornerButton::section{"
                "border-top:0px solid #D8D8D8;"
                "border-left:0px solid #D8D8D8;"
                "border-right:1px solid #D8D8D8;"
                "border-bottom: 1px solid #D8D8D8;"
                "background-color:#D2DAFF;"
                "}"
        )

        self.verticalLayout_14.addWidget(self.tableWidget)

        # dbFolder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Database/ToothWear.db'))
        # AppFunctions.main(dbFolder)
        patients = AppFunctions.getAllPatients()
        patient_list = patients.json()['data']
        id = []
        for patient in patient_list:
            id.append(patient[0])
        AppFunctions.displayPatients(self, patients)

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        for i in range(patientNumber):
            self.viewSpecificButton = QPushButton(self.tableWidget)
            self.viewSpecificButton.setObjectName(u"viewSpecificButton")
            self.tableWidget.setCellWidget(i, 0, self.viewSpecificButton)
            self.viewSpecificButton.setText(str(id[i]))
            self.viewSpecificButton.setStyleSheet("QPushButton {background-color: #ECF2FF}")
            self.viewSpecificButton.clicked.connect(
                        lambda *args, i=i, v=imageViewer: AppFunctions.viewImage(self, id[i], v))
            self.deletePatientButton = QPushButton(self.tableWidget)
            self.deletePatientButton.setObjectName(u"deletePatientButton")
            self.tableWidget.setCellWidget(i, 16, self.deletePatientButton)
            self.deletePatientButton.setText("Delete")
            self.deletePatientButton.setStyleSheet("QPushButton {background-color: #ECF2FF;"
                                                   "text-align: center;}")
            self.deletePatientButton.clicked.connect(
                       lambda *args, i=i: AppFunctions.deletePatient(self, id[i]))



        self.vboxLayout.addWidget(self.widget_4)

        self.pages.addWidget(self.homePage)
        self.viewPage = QWidget()
        self.viewPage.setObjectName(u"viewPage")
        self.horizontalLayout_6 = QHBoxLayout(self.viewPage)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_3 = QWidget(self.viewPage)
        self.widget_3.setObjectName(u"widget_3")

        self.horizontalLayout_6.addWidget(self.widget_3)

        self.viewingTools = QWidget(self.viewPage)
        self.viewingTools.setObjectName(u"viewingTools")
        self.viewingTools.setMinimumSize(QSize(200, 450))
        self.viewingTools.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.viewingTools)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.viewingTools)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_10.addWidget(self.pushButton_3, 0, Qt.AlignHCenter)

        self.pushButton_4 = QPushButton(self.viewingTools)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_10.addWidget(self.pushButton_4, 0, Qt.AlignHCenter)

        self.horizontalLayout_6.addWidget(self.viewingTools, 0, Qt.AlignRight)

        self.viewPage = QSplitter()
        self.viewPage.setMidLineWidth(800)
        self.viewPage.setOrientation(Qt.Horizontal)
        self.viewPage.setHandleWidth(20)
        self.viewPage.setChildrenCollapsible(False)
        self.viewPage.setObjectName(u"viewPage")

        self.widget_3 = QWidget(self.viewPage)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 0))
        self.widget_3.setMaximumSize(QSize(16777215,16777215))
        self.widget_3_layout = QVBoxLayout(self.widget_3)
        self.widget_3_layout.setSpacing(0)
        self.widget_3_layout.setObjectName(u"widget_3_layout")
        self.widget_3_layout.setContentsMargins(0,0,0,0)

        self.viewingTools = QWidget(self.viewPage)
        self.viewingTools.setObjectName(u"viewingTools")
        self.viewingTools.setMinimumSize(QSize(270, 500))
        self.viewingTools.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_10 = QGridLayout(self.viewingTools)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(40, 50, 40, 50)
        self.verticalLayout_10.setSpacing(10)

        self.pushButton_3 = QCheckBox(self.viewingTools)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(
        "QCheckBox {\n"
        "background-color: #BCCEF8; \n"
        "border-radius: 10px; \n"
        "padding: 10px 20px; \n"
        "}"
        "QCheckBox::indicator {\n"
        "color: #FFF \n"
        "background-color: #453C67; \n"
        "border-radius: 10px; \n"
        "padding: 10px 20px; \n"
        "}"
        )

        self.verticalLayout_10.addWidget(self.pushButton_3, 0, 0, Qt.AlignVCenter)

        self.pushButton_4 = QCheckBox(self.viewingTools)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(
        "QCheckBox {\n"
        "background-color: #BCCEF8; \n"
        "border-radius: 10px; \n"
        "padding: 10px 20px; \n"
        "}"
        "QCheckBox::indicator {\n"
        "color: #FFF \n"
        "background-color: #453C67; \n"
        "border-radius: 10px; \n"
        "padding: 10px 20px; \n"
        "}"
        )

        self.verticalLayout_10.addWidget(self.pushButton_4, 1, 0, Qt.AlignVCenter)

        self.loadUpperMesh = QPushButton(self.viewingTools)
        self.loadUpperMesh = QPushButton(u"loadUpperMesh")
        self.loadUpperMesh.setCursor(QCursor(Qt.PointingHandCursor))
        self.loadUpperMesh.setStyleSheet(
        "QPushButton {\n"
        "background-color: #BCCEF8; \n"
        "border-radius: 5px; \n"
        "padding: 10px 20px; \n"
        "text-align: centre; \n"
        "}"
        "QPushButton::hover {\n"
        "background-color: #8D9EFF; \n"
        "}"
        )

        self.verticalLayout_10.addWidget(self.loadUpperMesh, 2, 0, Qt.AlignVCenter)

        self.loadLowerMesh = QPushButton(self.viewingTools)
        self.loadLowerMesh = QPushButton(u"loadLowerMesh")
        self.loadLowerMesh.setCursor(QCursor(Qt.PointingHandCursor))
        self.loadLowerMesh.setStyleSheet(
        "QPushButton {\n"
        "background-color: #BCCEF8; \n"
        "border-radius: 5px; \n"
        "padding: 10px 20px; \n"
        "text-align: centre; \n"
        "}"
        "QPushButton::hover {\n"
        "background-color: #8D9EFF; \n"
        "}"
        )

        self.verticalLayout_10.addWidget(self.loadLowerMesh, 3, 0, Qt.AlignVCenter)

        self.resetViewPoint = QPushButton(self.viewingTools)
        self.resetViewPoint = QPushButton(u"resetViewPoint")
        self.resetViewPoint.setCursor(QCursor(Qt.PointingHandCursor))
        self.resetViewPoint.setStyleSheet(
        "QPushButton {\n"
        "background-color: #BCCEF8; \n"
        "border-radius: 5px; \n"
        "padding: 10px 20px; \n"
        "text-align: centre; \n"
        "}"
        "QPushButton::hover {\n"
        "background-color: #8D9EFF; \n"
        "}"
        )

        self.verticalLayout_10.addWidget(self.resetViewPoint, 4, 0, Qt.AlignVCenter)

        self.horizontalLayout_6 = QGridLayout(self.viewPage)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.horizontalLayout_6.addWidget(self.viewingTools, 0, Qt.AlignRight)

        self.pages.addWidget(self.viewPage)
        self.analysisPage = QWidget()
        self.analysisPage.setObjectName(u"analysisPage")
        self.verticalLayout_11 = QVBoxLayout(self.analysisPage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_7 = QWidget(self.analysisPage)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_12 = QVBoxLayout(self.widget_7)
        self.verticalLayout_12.setSpacing(12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_7)
        self.widget_5.setObjectName(u"widget_5")
        self.label_7 = QLabel(self.widget_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 50, 50))
        self.label_7.setPixmap(QPixmap(u":/icons/Icons/bar-chart_focus.png"))
        self.label_9 = QLabel(self.widget_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(60, 20, 550, 32))
        self.label_9.setFont(font)

        self.run_analysis_button = QPushButton(self.widget_5)
        self.run_analysis_button.setObjectName(u"run_analysis")
        self.run_analysis_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.run_analysis_button.setStyleSheet("QPushButton {background-color: #BCCEF8}")
        icon20 = QIcon()
        icon20.addFile(u":/icons/Icons/loader_focus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.run_analysis_button.setIcon(icon20)
        self.run_analysis_button.setIconSize(QSize(24, 26))
        self.run_analysis_button.setGeometry(QRect(400, 270, 140, 40))

        self.patientIDInput = QLineEdit(self.widget_5)
        self.patientIDInput.setObjectName(u"occupation")
        self.patientIDInput.setGeometry(QRect(50, 270, 300, 40))

        self.prediction_label = QLabel(self.widget_5)
        self.prediction_label.setObjectName(u"prediction_label")
        self.prediction_label.setGeometry(QRect(120, 90, 200, 50))
        self.label_7.setScaledContents(True)

        self.treatment_plan_label = QLabel(self.widget_5)
        self.treatment_plan_label.setObjectName(u"treatment_plan_label")
        self.treatment_plan_label.setGeometry(QRect(120, 90, 200, 350))

        self.verticalLayout_12.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_7)
        self.widget_6.setObjectName(u"widget_6")
        self.label_10 = QLabel(self.widget_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 10, 40, 40))
        self.label_10.setPixmap(QPixmap(u":/icons/Icons/check-square_focus.png"))
        self.label_10.setScaledContents(True)
        self.label_11 = QLabel(self.widget_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(67, 15, 300, 32))
        self.label_11.setFont(font)

        self.verticalLayout_12.addWidget(self.widget_6)


        self.verticalLayout_11.addWidget(self.widget_7)

        self.pages.addWidget(self.analysisPage)

        self.verticalLayout_2.addWidget(self.pages)


        self.horizontalLayout_2.addWidget(self.mainBodyContent)

        self.rightMenu = QCustomSlideMenu(self.mainBody)
        self.rightMenu.setObjectName(u"rightMenu")
        self.rightMenu.setMinimumSize(QSize(0, 0))
        self.rightMenu.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_2 = QWidget(self.rightMenu)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 50))
        self.label_2.setMaximumSize(QSize(50, 50))
        self.label_2.setPixmap(QPixmap(u":/icons/Icons/edit_focus.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.frame_5 = QFrame(self.widget_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.name = QLineEdit(self.frame_5)
        self.name.setObjectName(u"name")

        self.verticalLayout_9.addWidget(self.name)

        self.age = QLineEdit(self.frame_5)
        self.age.setObjectName(u"age")

        self.verticalLayout_9.addWidget(self.age)

        self.occupation = QLineEdit(self.frame_5)
        self.occupation.setObjectName(u"occupation")

        self.verticalLayout_9.addWidget(self.occupation)

        self.medicalHistory = QComboBox(self.frame_5)
        view = QListView(self.medicalHistory)
        self.medicalHistory.setView(view)
        view.setTextElideMode(QtCore.Qt.ElideNone)
        view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        model1 = QStandardItemModel()

        model1.appendRow(QStandardItem("gastric disorders"))
        model1.appendRow(QStandardItem("eating disorders"))
        model1.appendRow(QStandardItem("erosive medications/supplements"))
        model1.appendRow(QStandardItem("reduced salivary flow"))
        model1.appendRow(QStandardItem("psychological conditions"))
        model1.appendRow(QStandardItem("chronic alcoholism"))
        model1.appendRow(QStandardItem("radiotherapy to head and neck region"))
        model1.appendRow(QStandardItem("none of the above"))

        self.medicalHistory.setModel(ProxyModel(model1, 'Medical History'))
        self.medicalHistory.setCurrentIndex(0)
        self.medicalHistory.setStyleSheet("QComboBox{background: #FFFFFF}")

        self.medicalHistory.setObjectName(u"medicalHistory")

        self.verticalLayout_9.addWidget(self.medicalHistory)

        self.painComplaint = QComboBox(self.frame_5)
        view = QListView(self.painComplaint)
        self.painComplaint.setView(view)
        view.setTextElideMode(QtCore.Qt.ElideNone)
        view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        model2 = QStandardItemModel()

        model2.appendRow(QStandardItem("sensitivity and/or pain"))
        model2.appendRow(QStandardItem("functional problems (difficulty chewing and eating)"))
        model2.appendRow(QStandardItem("deterioration of aesthetic appearance (compromised dental attractiveness)"))
        model2.appendRow(QStandardItem("fast progress of the tooth wear process after a period of monitoring"))
        model2.appendRow(QStandardItem("wear atypical for the age of the patient"))
        model2.appendRow(QStandardItem("crumbling of dental hard tissue and restorations, threatening the "
                                          "integrity of teeth"))
        model2.appendRow(QStandardItem("etiological factors not influenceable"))
        model2.appendRow(QStandardItem("surfaces that are included in occlusion and articulation, leading to the "
                                          "loss of VDO"))
        model2.appendRow(QStandardItem("the condition of the saliva"))
        model2.appendRow(QStandardItem("phonetic impairment"))
        model2.appendRow(QStandardItem("none of the above"))

        self.painComplaint.setModel(ProxyModel(model2, 'Pain Complaint'))
        self.painComplaint.setCurrentIndex(0)
        self.painComplaint.setStyleSheet("QComboBox{background: #FFFFFF}")

        self.verticalLayout_9.addWidget(self.painComplaint)

        self.financialResources = QComboBox(self.frame_5)
        self.financialResources.setObjectName(u"financialResources")

        model3 = QStandardItemModel()

        model3.appendRow(QStandardItem("low"))
        model3.appendRow(QStandardItem("medium"))
        model3.appendRow(QStandardItem("high"))

        self.financialResources.setModel(ProxyModel(model3, 'Financial Resources'))
        self.financialResources.setCurrentIndex(0)
        self.financialResources.setStyleSheet("QComboBox{background: #FFFFFF}")

        self.verticalLayout_9.addWidget(self.financialResources)

        self.brushingMethod = QComboBox(self.frame_5)
        self.brushingMethod.setObjectName(u"brushingMethod")

        model4 = QStandardItemModel()

        model4.appendRow(QStandardItem("electric"))
        model4.appendRow(QStandardItem("manual"))
        model4.appendRow(QStandardItem("both"))

        self.brushingMethod.setModel(ProxyModel(model4, 'Brushing Method'))
        self.brushingMethod.setCurrentIndex(0)
        self.brushingMethod.setStyleSheet("QComboBox{background: #FFFFFF}")

        self.verticalLayout_9.addWidget(self.brushingMethod)

        self.brushingFrequency = QComboBox(self.frame_5)
        self.brushingFrequency.setObjectName(u"brushingFrequency")

        model5 = QStandardItemModel()

        model5.appendRow(QStandardItem("1x/ day"))
        model5.appendRow(QStandardItem("2x/ day"))
        model5.appendRow(QStandardItem("3x/ day"))

        self.brushingFrequency.setModel(ProxyModel(model5, 'Brushing Frequency'))
        self.brushingFrequency.setCurrentIndex(0)
        self.brushingFrequency.setStyleSheet("QComboBox{background: #FFFFFF}")

        self.verticalLayout_9.addWidget(self.brushingFrequency)

        self.brushingTiming = QComboBox(self.frame_5)
        self.brushingTiming.setObjectName(u"brushingTiming")

        model6 = QStandardItemModel()

        model6.appendRow(QStandardItem("before breakfast"))
        model6.appendRow(QStandardItem("after breakfast"))

        self.brushingTiming.setModel(ProxyModel(model6, 'Brushing Timing'))
        self.brushingTiming.setCurrentIndex(0)
        self.brushingTiming.setStyleSheet("QComboBox{background: #FFFFFF}")

        self.verticalLayout_9.addWidget(self.brushingTiming)

        self.alcoholIntake = QComboBox(self.frame_5)
        self.alcoholIntake.setObjectName(u"alcoholIntake")

        model7 = QStandardItemModel()

        model7.appendRow(QStandardItem("Nil"))
        model7.appendRow(QStandardItem("< 14 units/week"))
        model7.appendRow(QStandardItem("> 14 units/week"))

        self.alcoholIntake.setModel(ProxyModel(model7, 'Alcohol Intake'))
        self.alcoholIntake.setCurrentIndex(0)
        self.alcoholIntake.setStyleSheet("QComboBox{background: #FFFFFF}")

        self.verticalLayout_9.addWidget(self.alcoholIntake)

        self.stressLevel = QComboBox(self.frame_5)
        self.stressLevel.setObjectName(u"stressLevel")

        model8 = QStandardItemModel()

        model8.appendRow(QStandardItem("Low"))
        model8.appendRow(QStandardItem("Medium"))
        model8.appendRow(QStandardItem("High"))

        self.stressLevel.setModel(ProxyModel(model8, 'Stress Level'))
        self.stressLevel.setCurrentIndex(0)
        self.stressLevel.setStyleSheet("QComboBox{background: #FFFFFF}")

        self.verticalLayout_9.addWidget(self.stressLevel)

        self.sleepApnoea = QComboBox(self.frame_5)
        self.sleepApnoea.setObjectName(u"sleepApnoea")

        model9 = QStandardItemModel()

        model9.appendRow(QStandardItem("Yes"))
        model9.appendRow(QStandardItem("No"))

        self.sleepApnoea.setModel(ProxyModel(model9, 'Sleep Apnoea'))
        self.sleepApnoea.setCurrentIndex(0)
        self.sleepApnoea.setStyleSheet("QComboBox{background: #FFFFFF}")

        self.verticalLayout_9.addWidget(self.sleepApnoea)

        self.snoringHabit = QComboBox(self.frame_5)
        self.snoringHabit.setObjectName(u"snoringHabit")

        model10 = QStandardItemModel()

        model10.appendRow(QStandardItem("Yes"))
        model10.appendRow(QStandardItem("No"))

        self.snoringHabit.setModel(ProxyModel(model10, 'Snoring Habit'))
        self.snoringHabit.setCurrentIndex(0)
        self.snoringHabit.setStyleSheet("QComboBox{background: #FFFFFF}")

        self.verticalLayout_9.addWidget(self.snoringHabit)

        self.exercise = QComboBox(self.frame_5)
        self.exercise.setObjectName(u"exercise")

        model11 = QStandardItemModel()

        model11.appendRow(QStandardItem("Yes"))
        model11.appendRow(QStandardItem("No"))

        self.exercise.setModel(ProxyModel(model11, 'Exercise'))
        self.exercise.setCurrentIndex(0)
        self.exercise.setStyleSheet("QComboBox{background: #FFFFFF}")

        self.verticalLayout_9.addWidget(self.exercise)

        self.drugUse = QComboBox(self.frame_5)
        self.drugUse.setObjectName(u"drugUse")

        model12 = QStandardItemModel()

        model12.appendRow(QStandardItem("Yes"))
        model12.appendRow(QStandardItem("No"))

        self.drugUse.setModel(ProxyModel(model12, 'Drug Use'))
        self.drugUse.setCurrentIndex(0)
        self.drugUse.setStyleSheet("QComboBox{background: #FFFFFF}")

        self.verticalLayout_9.addWidget(self.drugUse)

        self.upperJawScanButton = QPushButton(self.widget_2)
        self.upperJawScanButton.setObjectName(u"upperJawScanButton")
        icon10 = QIcon()
        icon10.addFile(u":/icons/Icons/file-plus_focus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.upperJawScanButton.setIcon(icon10)
        self.upperJawScanButton.setIconSize(QSize(24, 24))
        self.upperJawScanButton.setStyleSheet("QPushButton {background-color: #EAFDFC}"
                                              "QPushButton::pressed {background-color: #D2DAFF}"
                                              "QPushButton::hover {background-color: #D2DAFF}")
        self.upperJawScanButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.upperJawScanButton)

        self.lowerJawScanButton = QPushButton(self.widget_2)
        self.lowerJawScanButton.setObjectName(u"lowerJawScanButton")
        icon10 = QIcon()
        icon10.addFile(u":/icons/Icons/file-plus_focus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lowerJawScanButton.setIcon(icon10)
        self.lowerJawScanButton.setIconSize(QSize(24, 24))
        self.lowerJawScanButton.setStyleSheet("QPushButton {background-color: #EAFDFC}"
                                              "QPushButton::pressed {background-color: #D2DAFF}"
                                              "QPushButton::hover {background-color: #D2DAFF}")
        self.lowerJawScanButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.lowerJawScanButton)

        self.sextantScanButton = QPushButton(self.widget_2)
        self.sextantScanButton.setObjectName(u"sextantScanButton")
        icon10 = QIcon()
        icon10.addFile(u":/icons/Icons/file-plus_focus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sextantScanButton.setIcon(icon10)
        self.sextantScanButton.setIconSize(QSize(24, 24))
        self.sextantScanButton.setStyleSheet("QPushButton {background-color: #EAFDFC}"
                                             "QPushButton::pressed {background-color: #D2DAFF}"
                                             "QPushButton::hover {background-color: #D2DAFF}")
        self.sextantScanButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.sextantScanButton)

        self.verticalLayout_8.addWidget(self.frame_5, 0, Qt.AlignTop)

        self.addPatientButton = QPushButton(self.widget_2)
        self.addPatientButton.setObjectName(u"addPatientButton")
        icon10 = QIcon()
        icon10.addFile(u":/icons/Icons/file-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addPatientButton.setIcon(icon10)
        self.addPatientButton.setIconSize(QSize(24, 24))
        self.addPatientButton.setStyleSheet("QPushButton{background-color: #BCCEF8; border-radius: 10px; border : 1px solid grey}"
                                            "QPushButton::pressed{background-color: #7286D3}"
                                            "QPushButton::hover{background-color: #7286D3}")
        self.addPatientButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.addPatientButton, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.widget_2, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.rightMenu)


        self.verticalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tooth Wear Clinical Decision Support System", None))
        self.pushButton_2.setText("")
        self.pushButton.setText("")
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.viewButton.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.analysisButton.setText(QCoreApplication.translate("MainWindow", u"Run Analysis", None))
        self.showPatientFormButton.setText(QCoreApplication.translate("MainWindow", u"Add patient details", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Occupation", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Medical history", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Pain complaint", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Financial resources", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Brushing method", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Brushing frequency", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Brushing timing", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Alcohol intake", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Stress level", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Sleep apnoea", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Snoring habit", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Exercise", None));
        ___qtablewidgetitem15 = self.tableWidget.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Drug use", None));
        ___qtablewidgetitem16 = self.tableWidget.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Delete Patient", None));


        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Hide upper", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Hide lower", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Patient Tooth Wear Grade", None))
        self.run_analysis_button.setText(QCoreApplication.translate("MainWindow", u"Run Analysis", None))
        self.label_10.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Treatment Plans", None))

        self.loadUpperMesh.setText(QCoreApplication.translate("MainWindow", u"Load upper", None))
        self.loadLowerMesh.setText(QCoreApplication.translate("MainWindow", u"Load lower", None))
        self.resetViewPoint.setText(QCoreApplication.translate("MainWindow", u"Reset camera", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Hide upper", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Hide lower", None))
        self.label_2.setText("")
        self.name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.age.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.occupation.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Occupation", None))
        self.upperJawScanButton.setText(QCoreApplication.translate("MainWindow", u"Choose upper jaw scan", None))
        self.lowerJawScanButton.setText(QCoreApplication.translate("MainWindow", u"Choose lower jaw scan", None))
        self.sextantScanButton.setText(QCoreApplication.translate("MainWindow", u"Choose sextant file", None))
        self.addPatientButton.setText(QCoreApplication.translate("MainWindow", u"Add Patient", None))
        self.patientIDInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter patient id", None))

    # retranslateUi

class ProxyModel(QAbstractProxyModel):
    def __init__(self, model, placeholderText='---', parent=None):
        super().__init__(parent)
        self._placeholderText = placeholderText
        self.setSourceModel(model)

    def index(self, row: int, column: int, parent: QModelIndex = ...) -> QModelIndex:
        return self.createIndex(row, column)

    def parent(self, index: QModelIndex = ...) -> QModelIndex:
        return QModelIndex()

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return self.sourceModel().rowCount() + 1 if self.sourceModel() else 0

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return self.sourceModel().columnCount() if self.sourceModel() else 0

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole) -> Any:
        if index.row() == 0 and role == Qt.DisplayRole:
            return self._placeholderText
        elif index.row() == 0 and role == Qt.EditRole:
            return None
        else:
            return super().data(index, role)

    def mapFromSource(self, sourceIndex: QModelIndex):
        return self.index(sourceIndex.row() + 1, sourceIndex.column())

    def mapToSource(self, proxyIndex: QModelIndex):
        return self.sourceModel().index(proxyIndex.row() - 1, proxyIndex.column())

    def mapSelectionFromSource(self, sourceSelection: QItemSelection):
        return super().mapSelection(sourceSelection)

    def mapSelectionToSource(self, proxySelection: QItemSelection):
        return super().mapSelectionToSource(proxySelection)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.DisplayRole):
        if not self.sourceModel():
            return None
        if orientation == Qt.Vertical:
            return self.sourceModel().headerData(section - 1, orientation, role)
        else:
            return self.sourceModel().headerData(section, orientation, role)

    def removeRows(self, row: int, count: int, parent: QModelIndex = ...) -> bool:
        return self.sourceModel().removeRows(row, count - 1)



