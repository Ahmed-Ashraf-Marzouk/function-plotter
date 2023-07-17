import sys
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Function Plotter")

        self.setFixedSize(QSize(600, 500))

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout() 

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])

        # Create widgets for the application 
        plotButton = QPushButton("Plot")
        plotButton.clicked.connect(self.inputFunction)
        textFieldFunction = CustomEditText("Enter Function")
        textFieldMin = CustomEditText("Min Value")
        textFieldMax = CustomEditText("Max Value")

        # Horizontal layout elements 
        layout1.addWidget(textFieldMin)
        layout1.addWidget(textFieldMax)
        layout1.addWidget(plotButton)

        # vertical layout elements 
        layout2.addWidget(textFieldFunction)
        layout2.addLayout(layout1)
        layout2.addWidget(sc)
        layout2.setAlignment(Qt.AlignTop)

        self.setIcon()
        widget = QWidget()
        widget.setLayout(layout2)
        self.setCentralWidget(widget)

    def setIcon(self):
        appIcon = QIcon("qt.png")
        self.setWindowIcon(appIcon)
    
    def inputFunction(self):
        pass

# Customized Edit Text 
class CustomEditText(QLineEdit):
    def __init__(self, placeHolder):
        super().__init__()
        self.setPlaceholderText(placeHolder)
        
# Customized Edit Text 
class CustomPushButton(QPushButton):
    def __init__(self, placeHolder):
        super().__init__()
        self.setPlaceholderText(placeHolder)
        

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()




# import ast

# expr = '(x + 5) * 3 ?'
# try:
#     ast.parse(expr)
#     print('valid')
# except SyntaxError:
#     print('invalid')
# https://stackoverflow.com/questions/67264856/how-can-i-validate-a-math-expression-syntax-without-calculate-it