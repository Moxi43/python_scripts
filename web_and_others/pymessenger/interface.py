from PyQt5 import QtCore, QtGui, QtWidgets #40:40
import clientui 

class ExampleApp(QtWidgets.QMainWindow, clientui.Ui_MainWindow):
    def __init__(self):
        super().__init__(self);
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QtApplication([])
    window = ExampleApp()
    window.show()
    app.exec_()        