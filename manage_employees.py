import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets 
from static import style
import sqlite3

con = sqlite3.connect("employees.db")
cur = con.cursor()

class ManageEmployees(QWidget):
    def __init__(self):
        super().__init__()
        size = (400,400)
        self.setWindowTitle("Manage Employees")
        self.setWindowIcon(QIcon("icons/icon.ico"))
        self.setGeometry(250, 100, 800,600)
        self.setStyleSheet(style.mainWindowStyle())
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        ###################################################################################
        ###### Adding topLayout widgets                 
        ###################################################################################
        self.iconWidgetTop =  QPushButton("...")
        self.iconWidgetTop.clicked.connect(self.backToMainMenu)
        self.iconWidgetTop.setStyleSheet(style.iconWidgetTopStyle())
        ###################################################################################
        ###### Adding parentMiddleUpLayout widgets                 
        ###################################################################################
        self.textForWidget = QLabel("MiddleLeftTopLayout")
        ###################################################################################
        ###### Adding childMiddleUpLeftLayout widgets                 
        ###################################################################################
        self.idLabel1        = QLabel("Id")
        self.idEntry1        = QLineEdit()
        self.firstNameLabel1 = QLabel("First Name")
        self.firstNameEntry1 = QLineEdit()
        ###################################################################################
        ###### Adding childMiddleUpLeftLayout widgets                 
        ###################################################################################
        self.idLabel2        = QLabel("Id")
        self.idEntry2        = QLineEdit()
        self.firstNameLabel2 = QLabel("First Name")
        self.firstNameEntry2 = QLineEdit()
        ###################################################################################
        ###### Adding childHorizontalUpLayout widgets                 
        ###################################################################################
        self.applyBtn = QPushButton("Apply")
        self.applyBtn.setStyleSheet(style.applyBtnStyle())
        self.resetBtn = QPushButton("Reset")
        self.resetBtn.setStyleSheet(style.resetBtnStyle())
        ###################################################################################
        ###### Adding middleDownLayout widgets                 
        ###################################################################################
        self.idLabel3        = QLabel("Id")
        self.idEntry3        = QLineEdit()
        self.firstNameLabel3 = QLabel("First Name")
        self.firstNameEntry3 = QLineEdit()
        ###################################################################################
        ###### Adding middleTableLayout widgets                 
        ###################################################################################
        self.table = QTableWidget()
        self.table.setStyleSheet(style.tableEmployeesStyle())
        self.table.setColumnCount(6)
        # self.table.setColumnHidden(0, True)
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
        ###################################################################################
        ###### Adding bottomLayout widgets         
        ###################################################################################
        self.bottomBackBtn = QPushButton("Back")
        self.bottomBackBtn.setStyleSheet(style.bottomBackBtnStyle())
        self.bottomNewBtn = QPushButton("New")
        self.bottomNewBtn.setStyleSheet(style.bottomNewBtnStyle())
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
        self.childMiddleUpCenterLayout = QFormLayout()
        self.childMiddleUpRightLayout = QFormLayout()

        self.middleDownLayout = QHBoxLayout()
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
        self.topLayout.setContentsMargins(0,2,730,2)
        ###################################################################################
        ### Setting Parent Layout                                 
        ###################################################################################
        self.parentMiddleUpLayout.addLayout(self.childMiddleUpLeftLayout)
        self.parentMiddleUpLayout.addLayout(self.childMiddleUpCenterLayout)
        self.parentMiddleUpLayout.addLayout(self.childMiddleUpRightLayout)
        ###################################################################################
        ### Setting Child Left Layout                                 
        ###################################################################################
        self.childMiddleUpLeftLayout.addRow(self.idLabel1, self.idEntry1)
        self.childMiddleUpLeftLayout.addRow(self.firstNameLabel1, self.firstNameEntry1)
        ###################################################################################
        ### Setting Child Center Layout                                 
        ###################################################################################
        self.childMiddleUpCenterLayout.addRow(self.idLabel2, self.idEntry2)
        self.childMiddleUpCenterLayout.addRow(self.firstNameLabel2, self.firstNameEntry2)
        ###################################################################################
        ### Setting Child Right Layout                                 
        ###################################################################################
        self.childMiddleUpRightLayout.addRow(self.idLabel3, self.idEntry3)
        self.childMiddleUpRightLayout.addRow(self.firstNameLabel3, self.firstNameEntry3)
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
        ###################################################################################
        ### Setting MainLayout                                 
        ###################################################################################
        self.setLayout(self.mainLayout)

    def backToMainMenu(self):
       self.close()



def main():
    App = QApplication(sys.argv)
    window = ManageEmployees()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()