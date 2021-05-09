'''
Tutorial Used:
https://realpython.com/python-pyqt-gui-calculator/


'''

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QLabel, QStatusBar, QToolBar
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout

class Window(QMainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setWindowTitle('QMainWindow')
		self.setCentralWidget(QLabel('test'))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = Window()
	win.show()
	sys.exit(app.exec())