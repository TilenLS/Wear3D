import base64
import os
import sys
import requests
from requests.exceptions import ConnectionError
from image_viewer import ImageViewer
from PySide2.QtCore import QObject
from PySide2.QtWidgets import QTableWidgetItem, QFileDialog, QMessageBox, QPushButton, QMainWindow


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
            self.lowerFilePath = QFileDialog.getOpenFileName(self,
                                                self.tr("Open File"), self.tr("~/Desktop/"), self.tr("3D Files (*.ply *.stl)"))[0]
        if upper:
            self.upperFilePath = QFileDialog.getOpenFileName(self,
                                                self.tr("Open File"), self.tr("~/Desktop/"), self.tr("3D Files (*.ply *.stl)"))[0]

    def chooseSextantFile(self):
        self.sextantFilePath = QFileDialog.getOpenFileName(self,
                                                self.tr("Open File"), self.tr("~/Desktop/"), self.tr("3D Files (*.ply *.stl)"))[0]


    def checkSignInDetails(self):
        usernameSignIn = self.ui1.username_input.text()
        passwordSignIn = self.ui1.password_input.text()
        payload = {'username': usernameSignIn, 'password': passwordSignIn}

        url = 'http://20.127.200.67:8080/dentist/signin'
        # url = 'http://127.0.0.1:5000/dentist/signin'
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
                   'encrypted': encrypted}

        url = 'http://20.127.200.67:8080/dentist/signup'
        # url = 'http://127.0.0.1:5000/dentist/signup'
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
        url = 'http://20.127.200.67:8080/patient/all'
        # url = 'http://127.0.0.1:5000/patient/all'
        patients = requests.get(url)
        return patients

    def getPatientNumber():
        url = 'http://20.127.200.67:8080/patient/number'
        # url = 'http://127.0.0.1:5000/patient/number'
        response = requests.get(url)
        patient_number = response.json()['num']
        return patient_number

    def addPatient(self):
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
                    'upperScan': upperScan,
                    'lowerScan': lowerScan,
                    'sextantScan': sextantScan}
        
        url = 'http://20.127.200.67:8080/patient/add'
        # url = 'http://127.0.0.1:5000/patient/add'
        response = requests.post(url, json=payload)
        add_status = response.json()['result']

        if add_status == 'fail':
            print("Could not insert patient data")
        else:
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

            AppFunctions.displayPatientsAfterAdd(self, AppFunctions.getAllPatients(dbFolder))
            patientNumber = AppFunctions.getPatientNumber()
            for i in range(patientNumber):
                self.ui3.viewSpecificButton = QPushButton(self.ui3.tableWidget)
                self.ui3.viewSpecificButton.setObjectName(u"viewSpecificButton")
                self.ui3.tableWidget.setCellWidget(i, 0, self.ui3.viewSpecificButton)
                self.ui3.viewSpecificButton.setText(str(i + 1))
                self.ui3.viewSpecificButton.setStyleSheet("QPushButton {background-color: #ECF2FF}")
                self.ui3.viewSpecificButton.clicked.connect(
                    lambda *args, i=i + 1, f=dbFolder, v=imageViewer: AppFunctions.viewImageAfterAdd(self, i, f, v))

    def deletePatient(self):
        id = self.ui4.id.text()
        payload = {'id': id}

        url = 'http://20.127.200.67:8080/patient/delete'
        # url = 'http://127.0.0.1:5000/patient/delete'
        response = requests.post(url, json=payload)

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

    def viewImage(self, id, dbFolder, viewer):
        self.pages.setCurrentWidget(self.viewPage)

        payload = {'id': id}
        url = 'http://20.127.200.67:8080/patient/view'
        # url = 'http://127.0.0.1:5000/patient/view'
        response = requests.post(url, json=payload)
        upper_path = response.json()['upper']
        lower_path = response.json()['lower']

        viewer.load_mesh(lowerFilePath=lower_path, upperFilePath=upper_path)

        self.homeButton.setStyleSheet(
        "QPushButton {background-color: transparent; border: none}"
        )
        self.viewButton.setStyleSheet(
        "QPushButton {background-color: #FFFFFF; font-weight: bold}"
        )

    def viewImageAfterAdd(self, id, dbFolder, viewer):
        self.ui3.pages.setCurrentWidget(self.ui3.viewPage)
        conn = AppFunctions.create_connection(dbFolder)

        patientID = id

        toExecute = "SELECT PATIENT_UPPER_JAW_SCAN, PATIENT_LOWER_JAW_SCAN FROM Patients WHERE PATIENT_ID = :id"
        crsr = conn.cursor()
        crsr.execute(toExecute, {"id": patientID})

        upper_path, lower_path = crsr.fetchall()[0]

        viewer.load_mesh(lowerFilePath=lower_path, upperFilePath=upper_path)

        self.ui3.homeButton.setStyleSheet(
        "QPushButton {background-color: transparent; border: none}"
        )
        self.ui3.viewButton.setStyleSheet(
        "QPushButton {background-color: #FFFFFF; font-weight: bold}"
        )

    def __get_sextant(self, id, dbFolder):
        conn = AppFunctions.create_connection(dbFolder)

        patientID = id

        toExecute = "SELECT PATIENT_SEXTANT_SCAN FROM Patients WHERE PATIENT_ID = :id"
        crsr = conn.cursor()
        crsr.execute(toExecute, {"id": patientID})

        sextant = crsr.fetchall()[0][0]   # after changing the database (store binary file in the database)
        return sextant

    def predict():
        """ This function is used to send a request to the inference module and get the prediction

        Args:
            id (int): patient id
            dbFolder (str): path to the database folder

        Returns:
            json: a json file with the prediction

        The input should be a patient id and the database folder, then get the result from self.__get_sextant(id, dbFolder), i.e. the sextant scan

        The function should find the .ply file and send it to the sever in a POST request
        """
        # sextant = self.__get_sextant(id, dbFolder)
        # eg.
        sextant = '../back-end/inference_module/JawScan_1.ply'
        url = 'http://20.127.200.67:8080/inference/predict'

        with open(sextant, 'rb') as f:
            files = {'file': (sextant, f)}
            response = requests.post(url, files=files)

        return response.json()
    

if __name__ == "__main__":
    pred = AppFunctions.predict()
    print(pred)






