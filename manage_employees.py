import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets 
from static import style
from new_employee import NewEmployee

import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()


class ManageEmployees(QWidget):
    def __init__(self):
        super().__init__()
        # size = (400,400)
        self.setWindowTitle("Manage Employees")
        self.setWindowIcon(QIcon("icons/icon.ico"))
        self.setGeometry(250, 100, 800,600)
        self.setStyleSheet(style.mainWindowStyle())
        # self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()
        self.getEmployees()

    def widgets(self):
        ###################################################################################
        ###### Adding topLayout widgets                 
        ###################################################################################
        self.iconWidgetTop =  QPushButton("...")
        
        self.iconWidgetTop.setStyleSheet(style.iconWidgetTopStyle())
        ###################################################################################
        ###### Adding parentMiddleUpLayout widgets                 
        ###################################################################################
        self.textForWidget = QLabel("MiddleLeftTopLayout")
        ###################################################################################
        ###### Adding childMiddleUpLeftLayout widgets                 
        ###################################################################################
        self.idLabel            = QLabel("Id")
        self.idEntry            = QLineEdit()
        self.firstNameLabel     = QLabel("First Name")
        self.firstNameEntry     = QLineEdit()
        self.lastNameLabel      = QLabel("Last Name")
        self.lastNameEntry      = QLineEdit()
        self.birthdayLabel      = QLabel("Birthday")
        self.birthdayEntry      = QLineEdit()
        ###################################################################################
        ###### Adding childMiddleUpRightLayout widgets                 
        ###################################################################################
        self.departmentLabel    = QLabel("Department Name")
        self.departmentEntry    = QLineEdit()
        self.salaryLabel        = QLabel("Salary")
        self.salaryEntry        = QLineEdit()
        self.positionLabel      = QLabel("Position")
        self.positionEntry      = QLineEdit()
        ###################################################################################
        ###### Adding childHorizontalUpLayout widgets                 
        ###################################################################################
        self.applyBtn = QPushButton("Apply")
        self.applyBtn.setStyleSheet(style.applyBtnStyle())
        self.resetBtn = QPushButton("Reset")
        self.resetBtn.setStyleSheet(style.resetBtnStyle())
        ###################################################################################
        ###### Adding middleTableLayout widgets                 
        ###################################################################################
        self.table = QTableWidget()
        self.table.setStyleSheet(style.tableEmployeesStyle())
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Id"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("First Name"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("Last Name"))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem("Birthday"))
        self.table.setHorizontalHeaderItem(4, QTableWidgetItem("Department"))
        self.table.setHorizontalHeaderItem(5, QTableWidgetItem("Salary"))
        self.table.setHorizontalHeaderItem(5, QTableWidgetItem("Position"))
        self.table.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(4,QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(5,QHeaderView.Stretch)
        ###################################################################################
        ###### Adding bottomLayout widgets         
        ###################################################################################
        self.bottomBackBtn = QPushButton("Back")
        self.bottomBackBtn.clicked.connect(self.backToMainMenu)
        self.bottomBackBtn.setStyleSheet(style.bottomBackBtnStyle())
        self.bottomNewBtn = QPushButton("New")
        self.bottomNewBtn.setStyleSheet(style.bottomNewBtnStyle())
        self.bottomNewBtn.clicked.connect(self.newEmployee)
        self.bottomExportBtn = QPushButton("Export")
        self.bottomExportBtn.setStyleSheet(style.bottomExportBtnStyle())

    def layouts(self):
        ###################################################################################
        ### Creating Layouts                    
        ###################################################################################
        self.mainLayout = QGridLayout()
        self.topLayout = QHBoxLayout()
        
        self.parentMiddleUpLayout = QHBoxLayout()

        self.childMiddleUpLeftLayout = QFormLayout()
        self.childMiddleUpRightLayout = QFormLayout()

        self.middleDownLayout = QHBoxLayout()
        self.middleDownLayout.setAlignment(Qt.AlignCenter)
        self.middleTableLayout = QHBoxLayout()
        self.bottomLayout = QHBoxLayout()
        ###################################################################################
        ### Adding ChildLayouts to MainLayout                                    
        ###################################################################################
        self.mainLayout.addLayout(self.topLayout,0,0)
        self.mainLayout.addLayout(self.parentMiddleUpLayout,1,0)
        self.mainLayout.addLayout(self.middleDownLayout,2,0)
        self.mainLayout.addLayout(self.middleTableLayout,3,0)
        self.mainLayout.addLayout(self.bottomLayout,4,0)
        ###################################################################################
        ###### Add Widgets to Layouts                    
        ###################################################################################
        self.topLayout.addWidget(self.iconWidgetTop)
        # self.topLayout.setContentsMargins(0,2,730,2)
        self.topLayout.setAlignment(Qt.AlignLeft)
        ###################################################################################
        ### Setting Parent Layout                                 
        ###################################################################################
        self.parentMiddleUpLayout.addLayout(self.childMiddleUpLeftLayout)
        self.parentMiddleUpLayout.addLayout(self.childMiddleUpRightLayout)
        ###################################################################################
        ### Setting Child Left Layout                                 
        ###################################################################################
        self.childMiddleUpLeftLayout.addRow(self.idLabel, self.idEntry)
        self.childMiddleUpLeftLayout.addRow(self.firstNameLabel, self.firstNameEntry)
        self.childMiddleUpLeftLayout.addRow(self.lastNameLabel, self.lastNameEntry)
        self.childMiddleUpLeftLayout.addRow(self.birthdayLabel, self.birthdayEntry)
        ###################################################################################
        ### Setting Child Right Layout                                 
        ###################################################################################
        self.childMiddleUpRightLayout.addRow(self.departmentLabel, self.departmentEntry)
        self.childMiddleUpRightLayout.addRow(self.salaryLabel, self.salaryEntry)
        self.childMiddleUpRightLayout.addRow(self.positionLabel, self.positionEntry)
        ###################################################################################
        ### Setting middleDown Layout                                 
        ###################################################################################
        self.middleDownLayout.addWidget(self.applyBtn)
        self.middleDownLayout.addWidget(self.resetBtn)
        ###################################################################################
        ### Setting middleTable Layout                                 
        ###################################################################################
        self.middleTableLayout.addWidget(self.table)
        ###################################################################################
        ### Setting Bottom Layout                                 
        ###################################################################################
        self.bottomLayout.addWidget(self.bottomBackBtn)
        self.bottomLayout.addWidget(self.bottomNewBtn)
        self.bottomLayout.addWidget(self.bottomExportBtn)
        self.bottomLayout.setAlignment(Qt.AlignRight)
        ###################################################################################
        ### Setting MainLayout                                 
        ###################################################################################
        self.setLayout(self.mainLayout)

    def backToMainMenu(self):
       self.close()
    
    def newEmployee(self):
        self.newEmployee = NewEmployee()

    def getEmployees(self):
        for i in reversed(range(self.table.rowCount())):
            self.table.removeRow(i)

            query = cur.execute(""" SELECT employee.id as ID, employee.first_name as "First Name", employee.last_name as "Last Name",
                employee.birthday as "Birthday", employee.department_name as "Department Name", 
                log_salary.salary as "Salary", log_position.position as "Position"
                FROM employee, log_salary, log_position
                WHERE employee.id = log_salary.employee_id AND employee.id = log_position.employee_id
                AND log_salary.date = (SELECT max(date) FROM log_salary WHERE employee_id = employee.id)
                AND log_position.date = (SELECT max(date) FROM log_position WHERE employee_id = employee.id)""")
    
            for row_data in query:
                row_number = self.table.rowCount()
                self.table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            self.table.setEditTriggers(QAbstractItemWidget.NoEditTriggers)


        

    



def main():
    App = QApplication(sys.argv)
    window = ManageEmployees()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()