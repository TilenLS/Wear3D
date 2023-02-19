import base64
import os
import sys
import sqlite3
from sqlite3 import Error

from PySide2.QtCore import QObject
from PySide2.QtWidgets import QTableWidgetItem, QFileDialog, QMessageBox

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

    def checkSignInDetails(self, dbFolder):

        conn = AppFunctions.create_connection(dbFolder)

        usernameSignIn = self.ui1.username_input.text()
        passwordSignIn = self.ui1.password_input.text()

        toExecute = "SELECT DENTIST_PASSWORD FROM Dentists WHERE DENTIST_USERNAME = :username"
        crsr = conn.cursor()
        crsr.execute(toExecute, {"username": usernameSignIn})

        try:
            passwordTuple = crsr.fetchall()[0]

            toCheckPassword = []
            for i in passwordTuple:
                toCheckPassword.append(i)

            encryptedPassword = encrypt(passwordSignIn)

            if encryptedPassword == toCheckPassword[0]:
                self.startHomePage()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Invalid")
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Invalid password, please try again")
                msg.exec_()

        except:
            msg = QMessageBox()
            msg.setWindowTitle("Invalid")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Username does not exist")
            msg.exec_()

    def addDentist(self, dbFolder):
        conn = AppFunctions.create_connection(dbFolder)

        username = self.ui2.username_input.text()
        password1 = self.ui2.password_input.text()
        password2 = self.ui2.confirm_password_input.text()
        encrypted = encrypt(password1)

        if password1 == password2:

            if not conn.cursor().execute("INSERT INTO Dentists (DENTIST_USERNAME, DENTIST_PASSWORD) VALUES (?,?)", \
                                          (username, encrypted)):
                print("Could not insert dentist data")
            else:
                conn.commit()
                crsr = conn.cursor()
                crsr.execute("SELECT * FROM Dentists")
                print("dentist data: ", crsr.fetchall())  # to show every dentist user in the database
                self.startSignInPage()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Invalid")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Password and confirm password is different. Please try again")
            msg.exec_()

    def create_connection(db_file):
        conn = None

        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn

    def create_table(conn, create_table_sql):
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def main(dbFolder):
        create_patient_table = """ CREATE TABLE IF NOT EXISTS Patients (
                                    PATIENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                    PATIENT_NAME TEXT,
                                    PATIENT_AGE TEXT,
                                    PATIENT_OCCUPATION TEXT,
                                    PATIENT_MEDICAL_HISTORY TEXT,
                                    PATIENT_PAIN_COMPLAINT TEXT,
                                    PATIENT_FINANCIAL_RESOURCES TEXT,
                                    PATIENT_BRUSHING_METHOD TEXT,
                                    PATIENT_BRUSHING_FREQUENCY TEXT,
                                    PATIENT_BRUSHING_TIMING TEXT,
                                    PATIENT_ALCOHOL_INTAKE TEXT,
                                    PATIENT_STRESS_LEVEL TEXT,
                                    PATIENT_SLEEP_APNOEA TEXT,
                                    PATIENT_SNORING_HABIT TEXT,
                                    PATIENT_EXERCISE TEXT,
                                    PATIENT_DRUG_USE TEXT,
                                    PATIENT_UPPER_JAW_SCAN TEXT,
                                    PATIENT_LOWER_JAW_SCAN TEXT
                                );
                            """
        create_dentist_table = """ CREATE TABLE IF NOT EXISTS Dentists (
                                    DENTIST_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                    DENTIST_USERNAME TEXT,
                                    DENTIST_PASSWORD TEXT
                                );
                            """
        conn = AppFunctions.create_connection(dbFolder)

        if conn is not None:
            AppFunctions.create_table(conn, create_patient_table)
            AppFunctions.create_table(conn, create_dentist_table)
        else:
            print("Error! Cannot create a patient database connection")

    def getAllPatients(dbFolder):
        conn = AppFunctions.create_connection(dbFolder)

        get_all_patients = """
                            SELECT * FROM Patients;                         
                           """

        try:
            c = conn.cursor()
            c.execute(get_all_patients)
            return c
        except Error as e:
            print(e)

    def addPatient(self, dbFolder):
        conn = AppFunctions.create_connection(dbFolder)

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

        insert_patient_data_sql = f"""
        INSERT INTO Patients (PATIENT_NAME, PATIENT_AGE, PATIENT_OCCUPATION, PATIENT_MEDICAL_HISTORY, 
        PATIENT_PAIN_COMPLAINT, PATIENT_FINANCIAL_RESOURCES, PATIENT_BRUSHING_METHOD, PATIENT_BRUSHING_FREQUENCY,
        PATIENT_BRUSHING_TIMING, PATIENT_ALCOHOL_INTAKE, PATIENT_STRESS_LEVEL, PATIENT_SLEEP_APNOEA, 
        PATIENT_SNORING_HABIT, PATIENT_EXERCISE, PATIENT_DRUG_USE, PATIENT_UPPER_JAW_SCAN, PATIENT_LOWER_JAW_SCAN) 
        VALUES ('{name}', '{age}', '{occupation}', '{medicalHistory}', '{painComplaint}', '{financialResources}', 
        '{brushingMethod}', '{brushingFrequency}', '{brushingTiming}', '{alocholIntake}', '{stressLevel}', 
        '{sleepApnoea}', '{snoringHabit}', '{exercise}', '{drugUse}', '{upperScan}', '{lowerScan}')
        """

        if not conn.cursor().execute(insert_patient_data_sql):
            print("Could not insert patient data")
        else:
            conn.commit()
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

            AppFunctions.displayPatients(self, AppFunctions.getAllPatients(dbFolder))

    def displayPatients(self, rows):
        for row in rows:
            row_position = self.ui.tableWidget.rowCount()

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