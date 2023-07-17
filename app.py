import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PySide2.QtCore import Qt, QSize
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

        self.setWindowTitle("Function Drawer")

        self.setFixedSize(QSize(600, 500))

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout() 

        self.editText_function = QLineEdit()
        self.editText_function.setPlaceholderText("Enter Function")
        self.editText_function.setAlignment(Qt.AlignTop)

        # Horizontal layout elements 
        layout1.addWidget(QLineEdit("Min Valeu"))
        layout1.addWidget(QLineEdit("Max Value"))
        layout1.addWidget(QPushButton("Draw"))

        # vertical layout elements 
        layout2.addWidget(self.editText_function)
        layout2.addLayout(layout1)

        widget = QWidget()
        widget.setLayout(layout2)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()