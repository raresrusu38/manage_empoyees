import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QEvent, QObject
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
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
        self.table.setColumnCount(7)
        # self.table.setColumnHidden(0, True)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Id"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("First Name"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("Last Name"))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem("Birthday"))
        self.table.setHorizontalHeaderItem(4, QTableWidgetItem("Department"))
        self.table.setHorizontalHeaderItem(5, QTableWidgetItem("Salary"))
        self.table.setHorizontalHeaderItem(6, QTableWidgetItem("Position"))
        self.table.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(4,QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(5,QHeaderView.Stretch)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.verticalHeader().hide()
        self.table.doubleClicked.connect(self.selectedEmployee)
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

        query = (""" SELECT employee.id as ID, employee.first_name as "First Name", employee.last_name as "Last Name",
            employee.birthday as "Birthday", employee.department_name as "Department Name", 
            log_salary.salary as "Salary", log_position.position as "Position"
            FROM employee, log_salary, log_position
            WHERE employee.id = log_salary.employee_id AND employee.id = log_position.employee_id
            AND log_salary.date = (SELECT max(date) FROM log_salary WHERE employee_id = employee.id)
            AND log_position.date = (SELECT max(date) FROM log_position WHERE employee_id = employee.id)
            """)
        result = cur.execute(query)

        for row_data in result:
            row_number = self.table.rowCount()
            self.table.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    
    def selectedEmployee(self):
        global employeeId
        listEmployee = []
        for i in range(0,7):
            listEmployee.append(self.table.item(self.table.currentRow(), i).text())
        
        employeeId = listEmployee[0]
        self.salaryAndPosition = SalaryPosition()
        self.salaryAndPosition.show()
        
### Salary - Position History Window ###
class SalaryPosition(QWidget):
    def __init__(self):
        super().__init__()
        # size = (400,400)
        self.setWindowTitle("Salary - Position History")
        self.setWindowIcon(QIcon("icons/icon.ico"))
        self.setGeometry(250, 100, 800,600)
        self.setStyleSheet(style.mainWindowStyle())
        # self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()
        self.getSalaryHistory()
        self.getPositionHistory()

    def widgets(self):
        ###################################################################################
        ###### Adding LeftLayout widgets                 
        ###################################################################################
        self.salaryLogLabel = QLabel(" [ Salary Log ]")
        self.salaryLogLabel.setAlignment(Qt.AlignCenter)
        self.salaryLogLabel.setStyleSheet(style.salaryLogLabelStyle())
        ###################################################################################
        ###### Adding middleTableLayout widgets                 
        ###################################################################################
        self.tableSalary = QTableWidget()
        self.tableSalary.setStyleSheet(style.tableEmployeesStyle())
        self.tableSalary.setColumnCount(7)
        self.tableSalary.setColumnHidden(0, True)
        self.tableSalary.setHorizontalHeaderItem(0, QTableWidgetItem("Id"))
        self.tableSalary.setHorizontalHeaderItem(1, QTableWidgetItem("First Name"))
        self.tableSalary.setHorizontalHeaderItem(2, QTableWidgetItem("Last Name"))
        self.tableSalary.setHorizontalHeaderItem(3, QTableWidgetItem("Department"))
        self.tableSalary.setHorizontalHeaderItem(4, QTableWidgetItem("Salary"))
        self.tableSalary.setHorizontalHeaderItem(5, QTableWidgetItem("Reason"))
        self.tableSalary.setHorizontalHeaderItem(6, QTableWidgetItem("Date"))
        self.tableSalary.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.tableSalary.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.tableSalary.horizontalHeader().setSectionResizeMode(3,QHeaderView.Stretch)
        self.tableSalary.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableSalary.verticalHeader().hide()
        ###################################################################################
        ###### Adding bottomLeftLayout widgets                 
        ###################################################################################
        self.changeSalaryBtn = QPushButton("Change Salary")
        self.changeSalaryBtn.setStyleSheet(style.changeSalaryBtnStyle())
        self.changeSalaryBtn.clicked.connect(self.changeSalaryFunc)
        ###################################################################################
        ###### Adding RightLayout widgets                 
        ###################################################################################
        self.positionLogLabel = QLabel("[ Position Log ]")
        self.positionLogLabel.setAlignment(Qt.AlignCenter)
        self.positionLogLabel.setStyleSheet(style.positionLogLabelStyle())
        ###################################################################################
        ###### Adding middleTableLayout widgets                 
        ###################################################################################
        self.tablePosition = QTableWidget()
        self.tablePosition.setStyleSheet(style.tableEmployeesStyle())
        self.tablePosition.setColumnCount(6)
        self.tablePosition.setColumnHidden(0, True)
        self.tablePosition.setHorizontalHeaderItem(0, QTableWidgetItem("Id"))
        self.tablePosition.setHorizontalHeaderItem(1, QTableWidgetItem("First Name"))
        self.tablePosition.setHorizontalHeaderItem(2, QTableWidgetItem("Last Name"))
        self.tablePosition.setHorizontalHeaderItem(3, QTableWidgetItem("Department"))
        self.tablePosition.setHorizontalHeaderItem(4, QTableWidgetItem("Position"))
        self.tablePosition.setHorizontalHeaderItem(5, QTableWidgetItem("Date"))
        self.tablePosition.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.tablePosition.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.tablePosition.horizontalHeader().setSectionResizeMode(3,QHeaderView.Stretch)
        self.tablePosition.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tablePosition.verticalHeader().hide()
        ###################################################################################
        ###### Adding bottomRightLayout widgets                 
        ###################################################################################
        self.changePositionBtn = QPushButton("Change Position")
        self.changePositionBtn.setStyleSheet(style.changePositionBtnStyle())
        self.changePositionBtn.clicked.connect(self.changePositionFunc)

    def layouts(self):
        ###################################################################################
        ### Creating mainLayout                    
        ###################################################################################
        self.mainLayout     = QHBoxLayout()
        ###################################################################################
        ### Creating leftLayout                   
        ###################################################################################
        self.leftLayout     = QVBoxLayout()
        self.leftTableLayout = QHBoxLayout()
        self.leftBottomLayout = QVBoxLayout()
        ###################################################################################
        ### Creating rightLayout                    
        ###################################################################################
        self.rightLayout    = QVBoxLayout()
        self.rightTableLayout = QHBoxLayout()
        self.rightBottomLayout = QVBoxLayout()
        ###################################################################################
        ### Adding widgets to LeftLayout                                 
        ###################################################################################
        self.leftLayout.addWidget(self.salaryLogLabel)
        self.leftLayout.addWidget(self.tableSalary)
        self.leftLayout.addWidget(self.changeSalaryBtn)
        ###################################################################################
        ### Adding widgets to RightLayout                                 
        ###################################################################################
        self.rightLayout.addWidget(self.positionLogLabel)
        self.rightLayout.addWidget(self.tablePosition)
        self.rightLayout.addWidget(self.changePositionBtn)
        ###################################################################################
        ### Adding Layouts to leftLayout and rightLayout                                 
        ###################################################################################
        self.leftLayout.addLayout(self.leftTableLayout)
        self.leftLayout.addLayout(self.leftBottomLayout)
        self.rightLayout.addLayout(self.rightTableLayout)
        self.rightLayout.addLayout(self.rightBottomLayout)
        ###################################################################################
        ### Adding Layouts to MainLayout                                 
        ###################################################################################
        self.mainLayout.addLayout(self.leftLayout)
        self.mainLayout.addLayout(self.rightLayout)
        ###################################################################################
        ### Setting MainLayout                                 
        ###################################################################################
        self.setLayout(self.mainLayout)
    
    def getSalaryHistory(self):
        global employeeId
        for i in reversed(range(self.tablePosition.rowCount())):
            self.tableSalary.removeRow(i)

        query = ("""
            SELECT employee.id, employee.first_name, employee.last_name, employee.department_name, log_salary.salary, log_salary.reason, log_salary.date
            FROM employee, log_salary
            WHERE employee.id = log_salary.employee_id AND employee.id = ?

        """)

        result = cur.execute(query, (employeeId,))

        for row_data in result:
            row_number = self.tableSalary.rowCount()
            self.tableSalary.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableSalary.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.tableSalary.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def getPositionHistory(self):
        global employeeId
        for i in reversed(range(self.tablePosition.rowCount())):
            self.tablePosition.removeRow(i)

        query = ("""
            SELECT employee.id, employee.first_name, employee.last_name, employee.department_name, log_position.position, log_position.date
            FROM employee, log_position
            WHERE employee.id = log_position.employee_id AND employee.id = ?

        """)

        result = cur.execute(query, (employeeId,))

        for row_data in result:
            row_number = self.tablePosition.rowCount()
            self.tablePosition.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tablePosition.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.tablePosition.setEditTriggers(QAbstractItemView.NoEditTriggers)


    def changeSalaryFunc(self):
        self.changeSalary           = ChangeSalary()
        # self.close()
    
    def changePositionFunc(self):
        self.changePosition         = ChangePosition()
        # self.close()

class ChangeSalary(QWidget):
    def __init__(self):
        super().__init__()
        size = (400,400)
        self.setWindowTitle("Change Salary")
        self.setWindowIcon(QIcon("icons/icon.ico"))
        self.setGeometry(250, 100, 350,400)
        self.setStyleSheet(style.mainWindowStyle())
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()
        self.populateChangeSalaryWindow()
    
    def widgets(self):
        ###################################################################################
        ###### Adding CentralLayout widgets                 
        ###################################################################################
        self.firstNameLabel = QLabel("First Name")
        self.firstNameEntry = QLabel()
        self.lastNameLabel = QLabel("Last Name")
        self.lastNameEntry = QLabel()
        self.currentSalaryLabel = QLabel("Current salary")
        self.currentSalaryEntry = QLabel()
        self.newSalaryLabel = QLabel("New salary")
        self.newSalaryEntry = QLineEdit()
        self.dateLabel  = QLabel("Date")
        self.dateEntry  = QtWidgets.QCalendarWidget()
        self.reasonLabel = QLabel("Reason")
        self.reasonEntry = QLineEdit()
        ###################################################################################
        ###### Adding BottomLayout widget               
        ###################################################################################
        self.saveBtn = QPushButton("Save")
        self.saveBtn.setStyleSheet(style.saveBtnSalaryChangedStyle())
        self.saveBtn.clicked.connect(self.saveChangeSalary)

    def layouts(self):
        ###################################################################################
        ### Creating Layouts                    
        ###################################################################################
        self.mainLayout         = QVBoxLayout()
        self.centralLayout      = QFormLayout()
        self.bottomLayout       = QHBoxLayout()
        ###################################################################################
        ### Ading Widgets to centralLayout                   
        ###################################################################################
        self.centralLayout.addRow(self.firstNameLabel, self.firstNameEntry)
        self.centralLayout.addRow(self.lastNameLabel, self.lastNameEntry)
        self.centralLayout.addRow(self.currentSalaryLabel, self.currentSalaryEntry)
        self.centralLayout.addRow(self.newSalaryLabel, self.newSalaryEntry)
        self.centralLayout.addRow(self.dateLabel, self.dateEntry)
        self.centralLayout.addRow(self.reasonLabel, self.reasonEntry)
        ###################################################################################
        ### Ading Widgets to bottomLayout                   
        ###################################################################################
        self.bottomLayout.addWidget(self.saveBtn)
        ###################################################################################
        ### Ading Layouts to mainLayout                    
        ###################################################################################
        self.mainLayout.addLayout(self.centralLayout)
        self.mainLayout.addLayout(self.bottomLayout)
        ###################################################################################
        ### Setting MainLayout                                 
        ###################################################################################
        self.setLayout(self.mainLayout)

    def populateChangeSalaryWindow(self):
        global employeeId

        query1 = ("SELECT employee.id, employee.first_name, employee.last_name FROM employee WHERE employee.id = ?")
        employeeData = cur.execute(query1, (employeeId,)).fetchall()
        employeeFirstName = employeeData[0][1]
        employeeLastName = employeeData[0][2]
        self.firstNameEntry.setText(employeeFirstName)
        self.lastNameEntry.setText(employeeLastName)
        
        query2 = ("SELECT log_salary.employee_id, log_salary.salary, log_salary.date, log_salary.reason FROM log_salary WHERE log_salary.employee_id = ?")
        employeeSalaryData = cur.execute(query2, (employeeId,)).fetchall()
        employeeSalary = employeeSalaryData[0][1]
        employeeDate = employeeSalaryData[0][2]
        self.currentSalaryEntry.setText(str(employeeSalary))

    def saveChangeSalary(self):
        global employeeId

        newSalary = self.newSalaryEntry.text()
        reason = self.reasonEntry.text()

        if (newSalary and reason != ""):
            
            try:
        
                query = ("""INSERT INTO 'log_salary' (employee_id, salary, date, reason) VALUES (?,?,?,?)
                """)
                result = cur.execute(query, (employeeId, newSalary, datetime.today().strftime('%Y-%m-%d'), reason))
                con.commit()
                ### Display message to the user ###
                QMessageBox.information(self, 'Info', 'Salary for this employee was changed')
            except:
                QMessageBox.information(self, 'Info', 'Salary for this employee was not changed')
        else:
            QMessageBox.information(self, 'Info', 'Fields cannot be empty')

class ChangePosition(QWidget):
    def __init__(self):
        super().__init__()
        size = (400,400)
        self.setWindowTitle("Change Position")
        self.setWindowIcon(QIcon("icons/icon.ico"))
        self.setGeometry(250, 100, 350,400)
        self.setStyleSheet(style.mainWindowStyle())
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()
        self.populateChangePositionWindow()
    
    def widgets(self):
        ###################################################################################
        ###### Adding CentralLayout widgets                 
        ###################################################################################
        self.firstNameLabel = QLabel("First Name")
        self.firstNameEntry = QLabel()
        self.lastNameLabel = QLabel("Last Name")
        self.lastNameEntry = QLabel()
        self.currentPositionLabel = QLabel("Current Position")
        self.currentPositionEntry = QLabel()
        self.newPositionLabel = QLabel("New Position")
        self.newPositionEntry = QLineEdit()
        self.dateLabel = QLabel("Date")
        self.dateEntry = QtWidgets.QCalendarWidget()
        ###################################################################################
        ###### Adding BottomLayout widget               
        ###################################################################################
        self.saveBtn = QPushButton("Save")
        self.saveBtn.setStyleSheet(style.saveBtnPositionChangedStyle())
        self.saveBtn.clicked.connect(self.saveChangePosition)

    def layouts(self):
        ###################################################################################
        ### Creating Layouts                    
        ###################################################################################
        self.mainLayout         = QVBoxLayout()
        self.centralLayout      = QFormLayout()
        self.bottomLayout       = QHBoxLayout()
        ###################################################################################
        ### Ading Widgets to centralLayout                   
        ###################################################################################
        self.centralLayout.addRow(self.firstNameLabel, self.firstNameEntry)
        self.centralLayout.addRow(self.lastNameLabel, self.lastNameEntry)
        self.centralLayout.addRow(self.currentPositionLabel, self.currentPositionEntry)
        self.centralLayout.addRow(self.newPositionLabel, self.newPositionEntry)
        self.centralLayout.addRow(self.dateLabel, self.dateEntry)
        ###################################################################################
        ### Ading Widgets to bottomLayout                   
        ###################################################################################
        self.bottomLayout.addWidget(self.saveBtn)
        ###################################################################################
        ### Ading Layouts to mainLayout                    
        ###################################################################################
        self.mainLayout.addLayout(self.centralLayout)
        self.mainLayout.addLayout(self.bottomLayout)
        ###################################################################################
        ### Setting MainLayout                                 
        ###################################################################################
        self.setLayout(self.mainLayout)

    def populateChangePositionWindow(self):
        global employeeId

        query1 = ("SELECT employee.id, employee.first_name, employee.last_name FROM employee WHERE employee.id = ?")
        employeeData = cur.execute(query1, (employeeId,)).fetchall()
        employeeFirstName = employeeData[0][1]
        employeeLastName = employeeData[0][2]
        self.firstNameEntry.setText(employeeFirstName)
        self.lastNameEntry.setText(employeeLastName)

        query2 = ("SELECT log_position.employee_id, log_position.position, log_position.date FROM log_position WHERE log_position.employee_id = ?")
        employeePositionData = cur.execute(query2, (employeeId,)).fetchall()
        employeeNewPosition = employeePositionData[0][1]
        self.currentPositionEntry.setText(str(employeeNewPosition))

    def saveChangePosition(self):
        global employeeId

        newPosition = self.newPositionEntry.text()

        if (newPosition != ""):
            
            try:
        
                query = ("""INSERT INTO 'log_position' (employee_id, position, date) VALUES (?,?,?)
                """)
                result = cur.execute(query, (employeeId, newPosition, datetime.today().strftime('%Y-%m-%d')))
                con.commit()
                ### Display message to the user ###
                QMessageBox.information(self, 'Info', 'Position for this employee was changed')
            except:
                QMessageBox.information(self, 'Info', 'Position for this employee was not changed')
        else:
            QMessageBox.information(self, 'Info', 'Fields cannot be empty')

    


def main():
    App = QApplication(sys.argv)
    window = ManageEmployees()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()