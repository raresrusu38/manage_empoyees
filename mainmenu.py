import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from static import style

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manage Employees")
        self.setWindowIcon(QIcon("icons/icon.ico"))
        self.setGeometry(470, 200, 350,400)
        self.setStyleSheet(style.mainWindowStyle())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        pass

    def layouts(self):
        self.mainLayout         = QVBoxLayout()
        self.topLayout          = QVBoxLayout()
        self.middleUpLayout     = QVBoxLayout()
        self.middleDownLayout   = QVBoxLayout()
        self.bottomLayout     = QVBoxLayout()
        self.topGroupBox        = QGroupBox()
        self.bottomGroupBox   = QGroupBox()

def main():
    App = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()