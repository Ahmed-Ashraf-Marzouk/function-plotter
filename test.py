import app
import pytest
from PySide2.QtCore import Qt

@pytest.fixture
def myapp(qtbot):
    testApp = app.MainWindow()
    testApp.show()
    qtbot.addWidget(testApp)
    return testApp

# Success 
def test_noraml_case(myapp, qtbot):
    myapp.textFieldFunction.setText('x^2')
    myapp.textFieldMin.setText('0')
    myapp.textFieldMax.setText('10')
    qtbot.mouseClick(myapp.plotButton, Qt.LeftButton)

# Failure 
def test_input_function_1(myapp, qtbot):
    myapp.textFieldFunction.setText('x2')
    myapp.textFieldMin.setText('-10')
    myapp.textFieldMax.setText('10')
    qtbot.mouseClick(myapp.plotButton, Qt.LeftButton)
    assert False

# Failure 
def test_input_min(myapp, qtbot):
    myapp.textFieldFunction.setText('cos(x)')
    myapp.textFieldMin.setText(' ')
    myapp.textFieldMax.setText('10')
    qtbot.mouseClick(myapp.plotButton, Qt.LeftButton)
    assert myapp.textFieldMin.text() != ' '

# Failure   
def test_input_max(myapp, qtbot):
    myapp.textFieldFunction.setText('cos(x)')
    myapp.textFieldMin.setText('-10')
    myapp.textFieldMax.setText(' ')
    qtbot.mouseClick(myapp.plotButton, Qt.LeftButton)
    assert myapp.textFieldMax.text() != ' '
    