from PyQt5 import QTWidgets
from ui_calculator import Ui_Calculator

class CalculatorWindow(QTWidgets, QMainWindow, Ui_calculator):
	def __init__(self):
		super().__init__()
		self.show()
