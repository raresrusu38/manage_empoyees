import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets 
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

    def widgets(self):
        ###################################################################################
        ###### Adding centralLayout widgets                 
        ###################################################################################
        self.firstNameLabel     = QLabel("First Name")
        self.firstNameEntry     = QLineEdit()
        self.lastNameLabel      = QLabel("Last Name")
        self.lastNameEntry      = QLineEdit()
        self.birthdayLabel      = QLabel("Birthday")
        self.birthdayEntry      = QCalendarWidget()
        self.departmentLabel    = QLabel("Department")
        self.departmentEntry    = QLineEdit()
        self.salaryLabel        = QLabel("Salary")
        self.salaryEntry        = QLineEdit()
        self.positionLabel      = QLabel("Position")
        self.positionEntry      = QLineEdit()
        self.saveBtnLabel       = QLabel()
        self.saveBtn            = QPushButton("Save")
        self.saveBtn.setStyleSheet(style.saveBtnNewEmployee())

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


def main():
    App = QApplication(sys.argv)
    window = NewEmployee()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()