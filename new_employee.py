import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from static import style

import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

class NewEmployee(QWidget):
    def __init__(self):
        super().__init__()
        # size = (400,400)
        self.setWindowTitle("New Employee")
        self.setWindowIcon(QIcon("icons/icon.ico"))
        self.setGeometry(250, 100, 350,400)
        self.setStyleSheet(style.mainWindowStyle())
        # self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()
        self.get_last_employee_id()

    def widgets(self):
        ###################################################################################
        ###### Adding centralLayout widgets                 
        ###################################################################################
        self.firstNameLabel     = QLabel("First Name")
        self.firstNameEntry     = QLineEdit()
        self.lastNameLabel      = QLabel("Last Name")
        self.lastNameEntry      = QLineEdit()
        self.birthdayLabel      = QLabel("Birthday")
        self.birthdayEntry      = QtWidgets.QCalendarWidget()
        self.departmentLabel    = QLabel("Department")
        self.departmentEntry    = QLineEdit()
        self.salaryLabel        = QLabel("Salary")
        self.salaryEntry        = QLineEdit()
        self.positionLabel      = QLabel("Position")
        self.positionEntry      = QLineEdit()
        self.saveBtnLabel       = QLabel()
        self.saveBtn            = QPushButton("Save")
        self.saveBtn.setStyleSheet(style.saveBtnNewEmployee())
        self.saveBtn.clicked.connect(self.addNewEmployee)

    def layouts(self):
        ###################################################################################
        ### Creating Layouts                    
        ###################################################################################
        self.mainLayout         = QVBoxLayout()
        self.centralLayout      = QFormLayout()
        self.bottomLayout       = QVBoxLayout()
        ###################################################################################
        ### Adding Widgets to MainLayout                    
        ###################################################################################
        self.centralLayout.addRow(self.firstNameLabel, self.firstNameEntry)
        self.centralLayout.addRow(self.lastNameLabel, self.lastNameEntry)
        self.centralLayout.addRow(self.birthdayLabel, self.birthdayEntry)
        self.centralLayout.addRow(self.departmentLabel, self.departmentEntry)
        self.centralLayout.addRow(self.salaryLabel, self.salaryEntry)
        self.centralLayout.addRow(self.positionLabel, self.positionEntry)
        self.bottomLayout.addWidget(self.saveBtn)
        self.bottomLayout.setAlignment(Qt.AlignCenter)
        ###################################################################################
        ### Adding Layout to MainLayout                    
        ###################################################################################
        self.mainLayout.addLayout(self.centralLayout)
        self.mainLayout.addLayout(self.bottomLayout)
        ###################################################################################
        ### Setting MainLayout                                 
        ###################################################################################
        self.setLayout(self.mainLayout)

    def get_last_employee_id(self):
        query = ("SELECT max(id) FROM employee")
        data = cur.execute(query).fetchone()
        if data:
            return data[0]
        return 0

    def addNewEmployee(self):
        firstName = self.firstNameEntry.text()
        lastName = self.lastNameEntry.text()
        department = self.departmentEntry.text()
        salary = self.salaryEntry.text()
        position = self.positionEntry.text()

        if (firstName and lastName and department and salary and position != ""):

            try:
                query1 = ("""
                    INSERT INTO employee(first_name, last_name, birthday, department_name)
                    VALUES(?,?,?,?)
                """)
                cur.execute(query1, (firstName, lastName, datetime.today().strftime('%Y-%m-%d'), department))
                con.commit()

                lastId = self.get_last_employee_id()
                
                query2 = ("""
                    INSERT INTO log_salary(employee_id, salary, date)
                    VALUES(?,?,?)
                """)
                cur.execute(query2, (lastId, salary, datetime.today().strftime('%Y-%m-%d')))
                con.commit()

                query3 = ("""
                    INSERT INTO log_position(employee_id, position, date)
                    VALUES(?,?,?)
                """)
                cur.execute(query3, (lastId, position, datetime.today().strftime('%Y-%m-%d')))
                con.commit()

                QMessageBox.information(self, 'Info', 'New employee was inserted')
            except:
                QMessageBox.information(self, 'Info', 'New employee was not inserted')
        else:
            QMessageBox.information(self, 'Info', 'Fields cannot be empty')


def main():
    App = QApplication(sys.argv)
    window = NewEmployee()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()