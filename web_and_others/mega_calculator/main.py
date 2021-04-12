from PySide import QtCore, QtGui
import sys
from calc import Ui_Dialog

#####
app = QtGui.QApplication(sys.argv)
#####
Dialog = QtGui.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
##########
def bp0():
	ui.lineEdit.setText("0")
def bp1():
	ui.lineEdit.setText("1")
def bp2():
	ui.lineEdit.setText("2")
def bp3():
	ui.lineEdit.setText("3")
def bp4():
	ui.lineEdit.setText("4")
def bp5():
	ui.lineEdit.setText("5")
def bp6():
	ui.lineEdit.setText("6")
def bp7():
	ui.lineEdit.setText("7")
def bp8():
	ui.lineEdit.setText("8")	
def bp9():
	ui.lineEdit.setText("9")
			
ui.pushButton_10.clicked.connect(bp0)
ui.pushButton_7.clicked.connect(bp1)
ui.pushButton_8.clicked.connect(bp2)	
ui.pushButton_9.clicked.connect(bp3)
ui.pushButton_4.clicked.connect(bp4)
ui.pushButton_5.clicked.connect(bp5)
ui.pushButton_6.clicked.connect(bp6)
ui.pushButton_2.clicked.connect(bp7)
ui.pushButton.clicked.connect(bp8)
ui.pushButton_3.clicked.connect(bp9)

############
sys.exit(app.exec_())

