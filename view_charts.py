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
        self.create_bar()
        self.widgets()
        self.layouts()
        
    def create_bar(self):
        set0 = QBarSet("Rares")
        set1 = QBarSet("Daniela")
        set2 = QBarSet("Andrei")

        set0 << 1 << 2 << 3 << 4 << 5 << 6
        set1 << 5 << 0 << 0 << 4 << 0 << 7
        set2 << 3 << 5 << 8 << 13 << 8 << 5

        series = QPercentBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)

        self.chart = QChart()
        self.chart.addSeries(series)
        self.chart.setTitle("Percent BarChart")
        self.chart.setAnimationOptions(QChart.SeriesAnimations)

        categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
        axis = QBarCategoryAxis()
        axis.append(categories)
        self.chart.createDefaultAxes()
        self.chart.setAxisX(axis, series)

        self.chartView = QChartView(self.chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)

    def widgets(self):
        ###################################################################################
        ### Creating Widgets for centralLayout and bottomLayout               
        ###################################################################################
        # self.left = QListWidget()
        self.right = QListWidget()
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
        self.leftLayout.addWidget(self.chartView)
        self.rightLayout.addWidget(self.right)
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



def main():
    App = QApplication(sys.argv)
    window = ViewCharts()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
