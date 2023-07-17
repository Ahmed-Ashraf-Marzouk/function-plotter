import sys
import matplotlib
import numpy as np
from sympy import SympifyError, var
from sympy import sympify
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QMessageBox
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import (
    QApplication,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

LS = 1000
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Function Plotter")

        self.setFixedSize(QSize(600, 500))
        self.syExpr = '' # for parsing user input function

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout() 

        self.sc = MplCanvas(self, width=5, height=4, dpi=100)

        self.msgF = QMessageBox()
        self.msgF.setIcon(QMessageBox.Critical)
        self.msgF.setText("Error in function")
        self.msgF.setInformativeText('Invalid input function')
        self.msgF.setWindowTitle("Error")
       
        self.msgV = QMessageBox()
        self.msgV.setIcon(QMessageBox.Critical)
        self.msgV.setText("Error in value")
        self.msgV.setInformativeText('Wrong min or max value')
        self.msgV.setWindowTitle("Error")

        # Create widgets for the application 
        self.plotButton = QPushButton("Plot!")
        self.plotButton.clicked.connect(self.inputFunction)
        self.plotButton.setStyleSheet("background-color: #70e000")
        self.textFieldFunction = CustomEditText("Enter Function")
        self.textFieldMin = CustomEditText("Min Value")
        self.textFieldMax = CustomEditText("Max Value")

        # Horizontal layout elements 
        layout1.addWidget(self.textFieldMin)
        layout1.addWidget(self.textFieldMax)
        layout1.addWidget(self.plotButton)

        # vertical layout elements 
        layout2.addWidget(self.textFieldFunction)
        layout2.addLayout(layout1)
        layout2.addWidget(self.sc)
        layout2.setAlignment(Qt.AlignTop)

        self.setIcon()
        widget = QWidget()
        widget.setLayout(layout2)
        self.setCentralWidget(widget)

    def setIcon(self):
        appIcon = QIcon("qt.png")
        self.setWindowIcon(appIcon)
    
    def inputFunction(self):
        funcText = self.textFieldFunction.text()
        self.validate(funcText)
    
    def validate(self, expr):
        
        try:
           self.plot(expr)
        except SympifyError:
            self.msgF.exec_()
        except ValueError:
            self.msgV.exec_()

    def plot(self, expr):
        min = int(self.textFieldMin.text())
        max = int(self.textFieldMax.text())
        x = var('x')
        f = np.linspace(min, max, LS)
        y = []
        self.syExpr = sympify(expr)
        for i in f:
            y.append(self.syExpr.subs(x, i))
        self.sc.axes.cla()
        self.sc.axes.plot(f, y, color="#70e000")
        self.sc.draw()



# Customized Edit Text 
class CustomEditText(QLineEdit):
    def __init__(self, placeHolder):
        super().__init__()
        self.setPlaceholderText(placeHolder)
        self.setStyleSheet("QLineEdit:focus {border: 1px solid #70e000;}")

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()