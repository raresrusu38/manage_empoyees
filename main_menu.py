import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from static import style
from manage_employees import ManageEmployees
from view_charts import ViewCharts

import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        size = (400,400)
        self.setWindowTitle("Main Menu")
        self.setWindowIcon(QIcon("icons/icon.ico"))
        self.setGeometry(470, 200, 400,400)
        self.setStyleSheet(style.mainWindowStyle())
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        ###################################################################################
        ### Creating Widgets                    
        ###################################################################################
        self.emptyWidgetTop = QLabel()
        self.manageEmployeesBtn = QPushButton("Manage Employees")
        self.manageEmployeesBtn.clicked.connect(self.manageEmployee)
        self.manageEmployeesBtn.setStyleSheet(style.manageEmployeesBtnStyle())
        self.viewChartsBtn = QPushButton("View Charts")
        self.viewChartsBtn.clicked.connect(self.viewChartsAction)
        self.viewChartsBtn.setStyleSheet(style.viewChartsBtnStyle())
        self.emptyWidgetBottom = QLabel()

    def layouts(self):
        ###################################################################################
        ### Creating Layouts                    
        ###################################################################################
        self.mainLayout         = QVBoxLayout()
        self.topLayout          = QHBoxLayout()
        self.middleUpLayout     = QVBoxLayout()
        self.middleDownLayout   = QVBoxLayout()
        self.bottomLayout       = QHBoxLayout()
        ###################################################################################
        ### Adding ChildLayouts to MainLayout                                    
        ###################################################################################
        self.mainLayout.addLayout(self.topLayout,30)
        self.mainLayout.addLayout(self.middleUpLayout,20)
        self.mainLayout.addLayout(self.middleDownLayout,20)
        self.mainLayout.addLayout(self.bottomLayout,30)
        ###################################################################################
        ###### Add Widgets to Layouts                    
        ###################################################################################
        self.topLayout.addWidget(self.emptyWidgetTop)
        self.middleUpLayout.addWidget(self.manageEmployeesBtn)
        self.middleUpLayout.setContentsMargins(100,5,100,5)
        self.middleDownLayout.addWidget(self.viewChartsBtn)
        self.middleDownLayout.setContentsMargins(100,5,100,5)
        self.bottomLayout.addWidget(self.emptyWidgetBottom)
        ###################################################################################
        ### Setting MainLayout                                 
        ###################################################################################
        self.setLayout(self.mainLayout)

    def manageEmployee(self):
        self.manageEmployees = ManageEmployees()
        

    def viewChartsAction(self):
        self.viewCharts = ViewCharts()


def main():
    App = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()