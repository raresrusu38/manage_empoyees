import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import *
from static import style

import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

class ViewCharts(QWidget):
    def __init__(self):
        super().__init__()
        # size = (400,400)
        self.setWindowTitle("View Charts")
        self.setWindowIcon(QIcon("icons/icon.ico"))
        self.setGeometry(250, 100, 800,600)
        self.setStyleSheet(style.mainWindowStyle())
        # self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.get_salary_statistics()
        self.get_total_department_salaries()
        self.widgets()
        self.layouts()
        
    def get_salary_statistics(self):
        result_list = [0,0,0]

        query = ("SELECT max(salary) FROM log_salary")
        result = cur.execute(query,).fetchone()
        if query:
            result_list[2] = result[0]

        query = ("SELECT avg(salary) FROM log_salary")
        result = cur.execute(query,).fetchone()
        if query:
            result_list[1] = result[0]

        query = ("SELECT min(salary) FROM log_salary")
        result = cur.execute(query,).fetchone()
        if query:
            result_list[0] = result[0]

        minBarSet = QBarSet("Min. Salary")
        avgBarSet = QBarSet("Avg. Salary")
        maxBarSet = QBarSet("Max. Salary")

        minBarSet << result_list[0]
        avgBarSet << result_list[1]
        maxBarSet << result_list[2]

        leftseries = QBarSeries()
        leftseries.append(minBarSet)
        leftseries.append(avgBarSet)
        leftseries.append(maxBarSet)

        self.leftchart = QChart()
        self.leftchart.addSeries(leftseries)
        self.leftchart.setTitle("Salary Statistics Chart")
        self.leftchart.setAnimationOptions(QChart.SeriesAnimations)

        # categories = ["1000", "2000", "3000", "4000", "5000", "6000"]
        axis = QBarCategoryAxis()
        axis.append('min:' + str(result_list[0]) + ' | ' + 'avg:' + str(result_list[1]) + ' | ' + 'max:' + str(result_list[2]))
        self.leftchart.createDefaultAxes()
        self.leftchart.setAxisX(axis, leftseries)

        self.leftchartView = QChartView(self.leftchart)
        self.leftchartView.setRenderHint(QPainter.Antialiasing)

    def get_total_department_salaries(self):
        query = ("""
            SELECT employee.department_name, SUM(log_salary.salary) 
            FROM employee, log_salary 
            WHERE log_salary.employee_id = employee.id
            GROUP BY employee.department_name
        """)
        result = cur.execute(query,).fetchall()

        rightseries = QPieSeries()
       
        for entry in result:
            print(entry)
        rightseries.append(entry[0], entry[1])

        self.rightchart = QChart()
        self.rightchart.addSeries(rightseries)
        self.rightchart.setTitle("Total Salaries per department")
        self.rightchart.setAnimationOptions(QChart.SeriesAnimations)

        self.rightchartView = QChartView(self.rightchart)
        self.rightchartView.setRenderHint(QPainter.Antialiasing)

    def widgets(self):
        ###################################################################################
        ### Creating Widgets for centralLayout and bottomLayout               
        ###################################################################################
        self.iconWidgetBtn =  QPushButton("Back")
        self.iconWidgetBtn.setStyleSheet(style.iconWidgetBtnStyle())
        self.iconWidgetBtn.clicked.connect(self.backToMainMenu)

    def layouts(self):
        ###################################################################################
        ### Creating Layouts                    
        ###################################################################################
        self.mainLayout = QGridLayout()
        self.centralLayout = QHBoxLayout()
        self.leftLayout = QGridLayout()
        self.rightLayout = QGridLayout()
        self.bottomLayout = QHBoxLayout()
        ###################################################################################
        ### Adding ChildLayouts to centralLayout                                    
        ###################################################################################
        self.centralLayout.addLayout(self.leftLayout)
        self.centralLayout.addLayout(self.rightLayout)   
        ###################################################################################
        ### Adding ChildLayouts to MainLayout                                    
        ###################################################################################
        self.mainLayout.addLayout(self.centralLayout,0,0)
        self.mainLayout.addLayout(self.bottomLayout, 1,0)                         
        ###################################################################################
        ###### Add Widgets to leftLayout and rightLayout                    
        ###################################################################################
        self.leftLayout.addWidget(self.leftchartView)
        self.rightLayout.addWidget(self.rightchartView)
        ###################################################################################
        ###### Add Widgets to bottomLayout                    
        ###################################################################################
        self.bottomLayout.addWidget(self.iconWidgetBtn, alignment=Qt.AlignRight)
        ###################################################################################
        ### Setting MainLayout                                 
        ###################################################################################
        self.setLayout(self.mainLayout)

    def backToMainMenu(self):
       self.close()

