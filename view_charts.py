import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets 
from static import style

class ViewCharts(QWidget):
    def __init__(self):
        super().__init__()
        size = (400,400)
        self.setWindowTitle("View Charts")
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
        ### Creating Widgets                    
        ###################################################################################
        self.iconWidgetTop =  QPushButton("..Up")
        self.iconWidgetTop.clicked.connect(self.backToMainMenu)

    def layouts(self):
        ###################################################################################
        ### Creating Layouts                    
        ###################################################################################
        self.mainLayout = QGridLayout()
        self.topLayout = QHBoxLayout()
        ###################################################################################
        ### Adding ChildLayouts to MainLayout                                    
        ###################################################################################
        self.mainLayout.addLayout(self.topLayout,0,0)
        ###################################################################################
        ###### Add Widgets to Layouts                    
        ###################################################################################
        self.topLayout.addWidget(self.iconWidgetTop)
        self.topLayout.setContentsMargins(0,2,700,2)
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