### Main Window ###
def mainWindowStyle():
    return """
        background-color:#021728;
        color: #71CFF1;
        font-family: 'Open Sans';
    """
def manageEmployeesBtnStyle():
    return """
        QPushButton {
            background-color: #1779AC;
            color: #fff;
            font-size: 14px;
            font-weight: 600;
            width: 100px;
            height: 40px;
            border-radius: 4px;
        }
        QPushButton:hover {
            background-color: #126692;
            color: #fff;
        }
    """
def viewChartsBtnStyle():
    return """
        QPushButton {
            background-color: #02AD98;
            color: #fff;
            font-size: 14px;
            font-weight: 600;
            width: 100px;
            height: 40px;
            border-radius: 4px;
        }
        QPushButton:hover {
            background-color: #048c7c;
            color: #fff;
        }
    """
### Manage Employees Window ###
def iconWidgetTopStyle():
    return """
        QPushButton {
            background-color: #02AD98;
            color: #E7F4FF;
            font-size: 12px;
            font-weight: 600;
            width: 50px;
            height: 20px;
            border-radius: 4px;
        }
        QPushButton:hover {
            background-color: #018075;
            color: #E7F4FF;
        }
    """
def tableEmployeesStyle():
    return """
        QTableWidget {
            
        }
        QHeaderView::section {
            background-color: #c64d02;
        }
    """
def applyBtnStyle():
    return """
        QPushButton {
            background-color: #02AD98;
            color: #E7F4FF;
            font-size: 12px;
            font-weight: 600;
            max-width: 100px;
            height: 20px;
            border-radius: 4px;
        }
        QPushButton:hover {
            background-color: #018075;
            color: #E7F4FF;
        }
    """
def resetBtnStyle():
    return """
        QPushButton {
            background-color: #02AD98;
            color: #E7F4FF;
            font-size: 12px;
            font-weight: 600;
            max-width: 100px;
            height: 20px;
            border-radius: 4px;
        }
        QPushButton:hover {
            background-color: #018075;
            color: #E7F4FF;
        }
    """
def bottomBackBtnStyle():
    return """
        QPushButton {
            background-color: #02AD98;
            color: #E7F4FF;
            font-size: 12px;
            font-weight: 600;
            min-width: 100px;
            height: 20px;
            border-radius: 4px;
        }
        QPushButton:hover {
            background-color: #018075;
            color: #E7F4FF;
        }
    """
def bottomNewBtnStyle():
    return """
        QPushButton {
            background-color: #02AD98;
            color: #E7F4FF;
            font-size: 12px;
            font-weight: 600;
            min-width: 100px;
            height: 20px;
            border-radius: 4px;
        }
        QPushButton:hover {
            background-color: #018075;
            color: #E7F4FF;
        }
    """
def bottomExportBtnStyle():
    return """
        QPushButton {
            background-color: #02AD98;
            color: #E7F4FF;
            font-size: 12px;
            font-weight: 600;
            min-width: 100px;
            height: 20px;
            border-radius: 4px;
        }
        QPushButton:hover {
            background-color: #018075;
            color: #E7F4FF;
        }
    """
### New Employee Window ###
def saveBtnNewEmployee():
    return """
        QPushButton {
        background-color: #ff9232;
        color: #E7F4FF;
        font-size: 12px;
        font-weight: 600;
        width: 120px;
        height: 25px;
        border-radius: 4px;
        margin: 0 auto;
        text-align: center;
    }
    QPushButton:hover {
        background-color: #de7f2c;
        color: #E7F4FF;
    }
    """
### Salary - Position History Window ###
def salaryLogLabelStyle():
    return """
        QLabel {
            font-weight: 600;
            font-size: 14px;
        }
    """
def changeSalaryBtnStyle():
    return """
        QPushButton {
            background-color: #496a75;
            color: #E7F4FF;
            font-size: 12px;
            font-weight: 600;
            width: 120px;
            height: 25px;
            border-radius: 4px;
            margin: 0 auto;
            text-align: center;
        }
        QPushButton:hover {
            background-color: #3f5f6a;
            color: #E7F4FF;
        }
    """
def positionLogLabelStyle():
    return """
        QLabel {
            font-weight: 600;
            font-size: 14px;
        }
    """
def changePositionBtnStyle():
    return """
        QPushButton {
            background-color: #496a75;
            color: #E7F4FF;
            font-size: 12px;
            font-weight: 600;
            width: 120px;
            height: 25px;
            border-radius: 4px;
            margin: 0 auto;
            text-align: center;
        }
        QPushButton:hover {
            background-color: #3f5f6a;
            color: #E7F4FF;
        }
    """
### Change Salary ###
def saveBtnSalaryChangedStyle():
    return """
        QPushButton {
            background-color: #496a75;
            color: #E7F4FF;
            font-size: 12px;
            font-weight: 600;
            width: 120px;
            height: 25px;
            border-radius: 4px;
            margin: 0 auto;
            text-align: center;
        }
        QPushButton:hover {
            background-color: #3f5f6a;
            color: #E7F4FF;
        }
    """
def saveBtnPositionChangedStyle():
    return """
        QPushButton {
            background-color: #496a75;
            color: #E7F4FF;
            font-size: 12px;
            font-weight: 600;
            width: 120px;
            height: 25px;
            border-radius: 4px;
            margin: 0 auto;
            text-align: center;
        }
        QPushButton:hover {
            background-color: #3f5f6a;
            color: #E7F4FF;
        } 
    """
### Charts Window ###
def iconWidgetBtnStyle():
    return """
        QPushButton {
            background-color: #496a75;
            color: #E7F4FF;
            font-size: 12px;
            font-weight: 600;
            width: 120px;
            height: 25px;
            border-radius: 4px;
            margin: 0 auto;
            text-align: center;
        }
        QPushButton:hover {
            background-color: #3f5f6a;
            color: #E7F4FF;
        } 
    """