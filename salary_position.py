import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets 
from static import style

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

    def widgets(self):
        ###################################################################################
        ###### Adding LeftLayout widgets                 
        ###################################################################################
        self.salaryLogLabel = QLabel(" [ Salary Log ]")
        self.salaryLogLabel.setAlignment(Qt.AlignCenter)
        self.salaryLogLabel.setStyleSheet(style.salaryLogLabelStyle())
        self.salaryLog = QListWidget()
        self.changeSalaryBtn = QPushButton("Change Salary")
        self.changeSalaryBtn.setStyleSheet(style.changeSalaryBtnStyle())
        self.changeSalaryBtn.clicked.connect(self.changeSalaryFunc)
        ###################################################################################
        ###### Adding RightLayout widgets                 
        ###################################################################################
        self.positionLogLabel = QLabel("[ Position Log ]")
        self.positionLogLabel.setAlignment(Qt.AlignCenter)
        self.positionLogLabel.setStyleSheet(style.positionLogLabelStyle())
        self.positionLog = QListWidget()
        self.changePositionBtn = QPushButton("Change Position")
        self.changePositionBtn.setStyleSheet(style.changePositionBtnStyle())
        self.changePositionBtn.clicked.connect(self.changePositionFunc)

    def layouts(self):
        ###################################################################################
        ### Creating Layouts                    
        ###################################################################################
        self.mainLayout     = QHBoxLayout()
        self.leftLayout     = QVBoxLayout()
        self.rightLayout    = QVBoxLayout()
        ###################################################################################
        ### Adding widgets to LeftLayout                                 
        ###################################################################################
        self.leftLayout.addWidget(self.salaryLogLabel)
        self.leftLayout.addWidget(self.salaryLog)
        self.leftLayout.addWidget(self.changeSalaryBtn)
        ###################################################################################
        ### Adding widgets to LeftLayout                                 
        ###################################################################################
        self.rightLayout.addWidget(self.positionLogLabel)
        self.rightLayout.addWidget(self.positionLog)
        self.rightLayout.addWidget(self.changePositionBtn)
        ###################################################################################
        ### Adding Layouts to MainLayout                                 
        ###################################################################################
        self.mainLayout.addLayout(self.leftLayout)
        self.mainLayout.addLayout(self.rightLayout)
        ###################################################################################
        ### Setting MainLayout                                 
        ###################################################################################
        self.setLayout(self.mainLayout)

    def changeSalaryFunc(self):
        self.changeSalary           = ChangeSalary()
        # self.close()
    
    def changePositionFunc(self):
        self.changePosition         = ChangePosition()
        # self.close()

class ChangeSalary(QWidget):
    def __init__(self):
        super().__init__()
        # size = (400,400)
        self.setWindowTitle("Change Salary")
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
        self.reasonLabel = QLabel("Reason")
        self.reasonEntry = QLineEdit()
        ###################################################################################
        ###### Adding BottomLayout widget               
        ###################################################################################
        self.saveBtn = QPushButton("Save")
        self.saveBtn.setStyleSheet(style.saveBtnSalaryChangedStyle())

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


class ChangePosition(QWidget):
    def __init__(self):
        super().__init__()
        # size = (400,400)
        self.setWindowTitle("Change Position")
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
        ###### Adding CentralLayout widgets                 
        ###################################################################################
        self.firstNameLabel = QLabel("First Name")
        self.firstNameEntry = QLabel()
        self.lastNameLabel = QLabel("Last Name")
        self.lastNameEntry = QLabel()
        self.currentSalaryLabel = QLabel("Current salary")
        self.currentSalaryEntry = QLabel()
        self.currentPositionLabel = QLabel("Current Position")
        self.currentPositionEntry = QLineEdit()
        self.newPositionLabel = QLabel("New Position")
        self.newPositionEntry = QLineEdit()
        ###################################################################################
        ###### Adding BottomLayout widget               
        ###################################################################################
        self.saveBtn = QPushButton("Save")
        self.saveBtn.setStyleSheet(style.saveBtnPositionChangedStyle())

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
        self.centralLayout.addRow(self.currentPositionLabel, self.currentPositionEntry)
        self.centralLayout.addRow(self.newPositionLabel, self.newPositionEntry)
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
    


def main():
    App = QApplication(sys.argv)
    window = SalaryPosition()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()