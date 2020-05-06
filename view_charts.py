import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets 
from static import style

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
        self.widgets()
        self.layouts()

    def widgets(self):
        ###################################################################################
        ### Creating Widgets for centralLayout and bottomLayout               
        ###################################################################################
        self.left = QListWidget()
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
        self.leftLayout = QVBoxLayout()
        self.rightLayout = QVBoxLayout()
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
        self.leftLayout.addWidget(self.left)
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