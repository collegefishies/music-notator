'''
Tutorial Used:
https://realpython.com/python-pyqt-gui-calculator/


'''

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100,100,280,80)
window.move(60,15)

hello_message = QLabel('<h1>Hello World</h1>', parent=window)
hello_message.move(60,15)

window.show()

sys.exit(app.exec_())