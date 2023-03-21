import base64
import os
import sys
import requests
from PySide2 import QtCore
from PySide2.QtGui import Qt
from requests.exceptions import ConnectionError
from image_viewer import ImageViewer
from PySide2.QtCore import QObject
from PySide2.QtWidgets import QTableWidgetItem, QFileDialog, QMessageBox, QPushButton, QMainWindow
import open3d as o3d
import numpy as np
import json

domain = "20.127.200.67:8080"
# domain = "127.0.0.1:5000"

def encrypt(originalPassword):
    encrypted = base64.b64encode(originalPassword.encode("utf-8"))

    return encrypted

class AppFunctions():
    def __init__(self, arg):
        super(AppFunctions, self).__init__()
        self.arg = arg

    def tr(self, text):
        return QObject.tr(self, text)

    def choose_file(self, lower: bool = False, upper: bool = False):
        if lower:
            self.ui3.lowerJawScanButton.setStyleSheet("QPushButton {background-color: #D2DAFF}")
            self.lowerFilePath = QFileDialog.getOpenFileName(self,
                                                self.tr("Open File"), self.tr("~/Desktop/"), self.tr("3D Files (*.ply *.stl)"))[0]
        if upper:
            self.ui3.upperJawScanButton.setStyleSheet("QPushButton {background-color: #D2DAFF}")
            self.upperFilePath = QFileDialog.getOpenFileName(self,
                                                self.tr("Open File"), self.tr("~/Desktop/"), self.tr("3D Files (*.ply *.stl)"))[0]

    def chooseSextantFile(self):
        self.ui3.sextantScanButton.setStyleSheet("QPushButton {background-color: #D2DAFF}")
        self.sextantFilePath = QFileDialog.getOpenFileName(self,
                                                self.tr("Open File"), self.tr("~/Desktop/"), self.tr("3D Files (*.ply *.stl)"))[0]


    def checkSignInDetails(self):
        usernameSignIn = self.ui1.username_input.text()
        passwordSignIn = self.ui1.password_input.text()
        payload = {'username': usernameSignIn, 'password': passwordSignIn}

        url = 'http://{}/dentist/signin'.format(domain)
        response = requests.post(url, json=payload)
        signin_status = response.json()['result']

        if signin_status == 'success':
            self.startHomePage()
        elif signin_status == 'fail':
            msg = QMessageBox()
            msg.setWindowTitle("Invalid")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Invalid password, please try again")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Invalid")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Username does not exist")
            msg.exec_()

    def addDentist(self):
        username = self.ui2.username_input.text()
        password1 = self.ui2.password_input.text()
        password2 = self.ui2.confirm_password_input.text()
        encrypted = encrypt(password1)
        payload = {'username': username, 
                   'password': password1,
                   'confirm_password': password2,
                   'encrypted': encrypted.decode("utf-8")}

        url = 'http://{}/dentist/signup'.format(domain)
        response = requests.post(url, json=payload)
        signup_status = response.json()['result']

        if signup_status == 'success':
            self.startSignInPage()
        elif signup_status == 'fail':
            print("Could not insert dentist data")             
        elif signup_status == 'invalid':
            msg = QMessageBox()
            msg.setWindowTitle("Invalid")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Password and confirm password are different. Please try again")
            msg.exec_()

    def getAllPatients():
        url = 'http://{}/patient/all'.format(domain)
        patients = requests.get(url)
        return patients

    def getPatientNumber():
        url = 'http://{}/patient/number'.format(domain)
        response = requests.get(url)
        patient_number = response.json()['num']
        return patient_number

    def addPatient(self, imageViewer):
        name = self.ui3.name.text()
        age = self.ui3.age.text()
        occupation = self.ui3.occupation.text()
        medicalHistory = self.ui3.medicalHistory.currentText()
        painComplaint = self.ui3.painComplaint.currentText()
        financialResources = self.ui3.financialResources.currentText()
        brushingMethod = self.ui3.brushingMethod.currentText()
        brushingFrequency = self.ui3.brushingFrequency.currentText()
        brushingTiming = self.ui3.brushingTiming.currentText()
        alocholIntake = self.ui3.alcoholIntake.currentText()
        stressLevel = self.ui3.stressLevel.currentText()
        sleepApnoea = self.ui3.sleepApnoea.currentText()
        snoringHabit = self.ui3.snoringHabit.currentText()
        exercise = self.ui3.exercise.currentText()
        drugUse = self.ui3.drugUse.currentText()
        upperScan = self.upperFilePath
        lowerScan = self.lowerFilePath
        sextantScan = self.sextantFilePath
        with open(upperScan, 'rb') as f:
            upper = f.read()
        with open(lowerScan, 'rb') as f:
            lower = f.read()
        with open(sextantScan, 'rb') as f:
            sextant = f.read()
        payload = {'name': name,
                    'age': age,
                    'occupation': occupation,
                    'medicalHistory': medicalHistory,
                    'painComplaint': painComplaint,
                    'financialResources': financialResources,
                    'brushingMethod': brushingMethod,
                    'brushingFrequency': brushingFrequency,
                    'brushingTiming': brushingTiming,
                    'alcoholIntake': alocholIntake,
                    'stressLevel': stressLevel,
                    'sleepApnoea': sleepApnoea,
                    'snoringHabit': snoringHabit,
                    'exercise': exercise,
                    'drugUse': drugUse,
                    'upperScan': base64.b64encode(upper).decode('utf-8'),
                    'lowerScan': base64.b64encode(lower).decode('utf-8'),
                    'sextantScan': base64.b64encode(sextant).decode('utf-8')}
        json_data = json.dumps(payload)
        
        url = 'http://{}/patient/add'.format(domain)
        response = requests.post(url, data={'json': json_data})
        add_status = response.json()['result']

        if add_status == 'fail':
            print("Could not insert patient data")
        else:
            self.ui3.lowerJawScanButton.setStyleSheet("QPushButton {background-color: #EAFDFC}")
            self.ui3.upperJawScanButton.setStyleSheet("QPushButton {background-color: #EAFDFC}")
            self.ui3.sextantScanButton.setStyleSheet("QPushButton {background-color: #EAFDFC}")
            self.ui3.name.setText("")
            self.ui3.age.setText("")
            self.ui3.occupation.setText("")
            self.ui3.medicalHistory.setCurrentIndex(0)
            self.ui3.painComplaint.setCurrentIndex(0)
            self.ui3.financialResources.setCurrentIndex(0)
            self.ui3.brushingMethod.setCurrentIndex(0)
            self.ui3.brushingFrequency.setCurrentIndex(0)
            self.ui3.brushingTiming.setCurrentIndex(0)
            self.ui3.alcoholIntake.setCurrentIndex(0)
            self.ui3.stressLevel.setCurrentIndex(0)
            self.ui3.sleepApnoea.setCurrentIndex(0)
            self.ui3.snoringHabit.setCurrentIndex(0)
            self.ui3.exercise.setCurrentIndex(0)
            self.ui3.drugUse.setCurrentIndex(0)

            self.ui3.tableWidget.setSortingEnabled(False)
            patients = AppFunctions.getAllPatients()
            patient_list = patients.json()['data']
            id = []
            for patient in patient_list:
                id.append(patient[0])
            AppFunctions.displayPatientsAfterAdd(self, patients)

            patientNumber = AppFunctions.getPatientNumber()
            for i in range(patientNumber):
                self.ui3.viewSpecificButton = QPushButton(self.ui3.tableWidget)
                self.ui3.viewSpecificButton.setObjectName(u"viewSpecificButton")
                self.ui3.tableWidget.setCellWidget(i, 0, self.ui3.viewSpecificButton)
                self.ui3.viewSpecificButton.setText(str(id[i]))
                self.ui3.viewSpecificButton.setStyleSheet("QPushButton {background-color: #ECF2FF}")
                self.ui3.viewSpecificButton.clicked.connect(
                    lambda *args, i=i, v=imageViewer: AppFunctions.viewImageAfterAdd(self, id[i], v))
                self.ui3.deletePatientButton = QPushButton(self.ui3.tableWidget)
                self.ui3.deletePatientButton.setObjectName(u"deletePatientButton")
                self.ui3.tableWidget.setCellWidget(i, 16, self.ui3.deletePatientButton)
                self.ui3.deletePatientButton.setText("Delete")
                self.ui3.deletePatientButton.setStyleSheet("QPushButton {background-color: #ECF2FF;"
                                                       "text-align: center;}")
                self.ui3.deletePatientButton.clicked.connect(
                    lambda *args, i=i: AppFunctions.deletePatientAfterAdd(self, id[i]))

            self.ui3.tableWidget.setSortingEnabled(True)


    def deletePatient(self, patientID):
        msg = QMessageBox()
        msg.setWindowTitle("Delete Patient")
        messageBoxText = "Are you sure you want to delete details of patient " + str(patientID) + " ?"
        msg.setText(messageBoxText)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Cancel)
        msg.exec_()
        button = msg.clickedButton()
        sb = msg.standardButton(button)

        if sb == QMessageBox.Ok:
            items = self.tableWidget.findItems(str(patientID), QtCore.Qt.MatchExactly)
            if items:
                rowToBeDeleted = items[0].row()

            id = patientID
            payload = {'id': id}

            url = 'http://{}/patient/delete'.format(domain)
            response = requests.post(url, json=payload)

            self.tableWidget.removeRow(rowToBeDeleted)

        if sb == QMessageBox.Cancel:
            pass


    def deletePatientAfterAdd(self, patientID):
        msg = QMessageBox()
        msg.setWindowTitle("Delete Patient")
        messageBoxText = "Are you sure you want to delete details of patient " + str(patientID) + " ?"
        msg.setText(messageBoxText)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Cancel)
        msg.exec_()
        button = msg.clickedButton()
        sb = msg.standardButton(button)

        if sb == QMessageBox.Ok:
            items = self.ui3.tableWidget.findItems(str(patientID), QtCore.Qt.MatchExactly)
            if items:
                rowToBeDeleted = items[0].row()

            id = patientID
            payload = {'id': id}

            url = 'http://{}/patient/delete'.format(domain)
            response = requests.post(url, json=payload)

            self.ui3.tableWidget.removeRow(rowToBeDeleted)

        if sb == QMessageBox.Cancel:
            pass

    def displayPatients(self, rows):
        rows = rows.json()['data']
        for row in rows:
            row_position = self.tableWidget.rowCount()

            if row_position + 1 > row[0]:
                continue

            item_count = 0
            self.tableWidget.setRowCount(row_position + 1)
            qtableWidgetItem = QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(row_position, qtableWidgetItem)

            for item in row:
                self.qtableWidgetItem = QTableWidgetItem()
                self.tableWidget.setItem(row_position, item_count, self.qtableWidgetItem)
                self.qtableWidgetItem = self.tableWidget.item(row_position, item_count)
                self.qtableWidgetItem.setText(str(item))

                item_count += 1
            row_position += 1

    def displayPatientsAfterAdd(self, rows):
        self.ui3.tableWidget.clear()
        self.ui3.tableWidget.setRowCount(0)
        if (self.ui3.tableWidget.columnCount() < 17):
            self.ui3.tableWidget.setColumnCount(17)
        headerLabels = ["ID", "Name", "Age", "Occupation", "Medical history", "Pain complaint", "Financial resources",
                        "Brushing method", "Brushing frequency", "Brushing timing", "Alcohol intake", "Stress level",
                        "Sleep apnoea", "Snoring habit", "Exercise", "Drug use", "Delete patient"]
        self.ui3.tableWidget.setHorizontalHeaderLabels(headerLabels)
        rows = rows.json()['data']
        for row in rows:
            row_position = self.ui3.tableWidget.rowCount()

            if row_position + 1 > row[0]:
                continue

            item_count = 0
            self.ui3.tableWidget.setRowCount(row_position + 1)
            qtableWidgetItem = QTableWidgetItem()
            self.ui3.tableWidget.setVerticalHeaderItem(row_position, qtableWidgetItem)

            for item in row:
                self.qtableWidgetItem = QTableWidgetItem()
                self.ui3.tableWidget.setItem(row_position, item_count, self.qtableWidgetItem)
                self.qtableWidgetItem = self.ui3.tableWidget.item(row_position, item_count)
                self.qtableWidgetItem.setText(str(item))

                item_count += 1
            row_position += 1


    def viewImage(self, id, viewer):
        self.pages.setCurrentWidget(self.viewPage)

        payload = {'id': id}
        url = 'http://{}/patient/view'.format(domain)
        response = requests.post(url, json=payload)
        upper_file = response.json()['upper']
        upper_file = base64.b64decode(upper_file)
        with open('upperScan.ply', 'wb') as f:
            f.write(upper_file)
        lower_file = response.json()['lower']
        lower_file = base64.b64decode(lower_file)
        with open('lowerScan.ply', 'wb') as f:
            f.write(lower_file)
        
        viewer.load_mesh(lowerFilePath='lowerScan.ply', upperFilePath='upperScan.ply')

        self.homeButton.setStyleSheet(
        "QPushButton {background-color: transparent; border: none}"
        )
        self.viewButton.setStyleSheet(
        "QPushButton {background-color: #FFFFFF; font-weight: bold}"
        )

    def viewImageAfterAdd(self, id, viewer):
        self.ui3.pages.setCurrentWidget(self.ui3.viewPage)

        payload = {'id': id}
        url = 'http://{}/patient/view'.format(domain)
        response = requests.post(url, json=payload)
        upper_file = response.json()['upper']
        upper_file = base64.b64decode(upper_file)
        with open('upperScan.ply', 'wb') as f:
            f.write(upper_file)
        lower_file = response.json()['lower']
        lower_file = base64.b64decode(lower_file)
        with open('lowerScan.ply', 'wb') as f:
            f.write(lower_file)

        viewer.load_mesh(lowerFilePath='lowerScan.ply', upperFilePath='upperScan.ply')

        self.ui3.homeButton.setStyleSheet(
        "QPushButton {background-color: transparent; border: none}"
        )
        self.ui3.viewButton.setStyleSheet(
        "QPushButton {background-color: #FFFFFF; font-weight: bold}"
        )

    def predict(id):
        """ This function is used to send a request to the inference module and get the prediction

        Args:
            id (int): patient id
            dbFolder (str): path to the database folder

        Returns:
            json: a json file with the prediction

        The input should be a patient id and the database folder, then get the result from self.__get_sextant(id, dbFolder), i.e. the sextant scan

        The function should find the .ply file and send it to the sever in a POST request
        """
        url = 'http://{}/inference/predict'.format(domain)
        payload = {'id': id}

        response = requests.post(url, json=payload)
        return response.json()['result']
    
    def show_prediction(self):
        id = self.ui3.patientIDInput.text()
        prediction = AppFunctions.predict(id)
        self.ui3.prediction_label.setText(prediction)

    def searchForMatchingItem(self, s):
        self.tableWidget.setCurrentItem(None)

        if not s:
            # Empty string, don't search.
            return

        matching_items = self.tableWidget.findItems(s, Qt.MatchContains)
        if matching_items:
            # we have found something
            item = matching_items[0]  # take the first
            self.tableWidget.setCurrentItem(item)
    

