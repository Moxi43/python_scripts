# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(440, 439)
        Dialog.setStyleSheet("QPushButton {\n"
"    background-color:white;\n"
"    width:75px;\n"
"    height:50px;\n"
"    font-size:14px;\n"
"    font-weight: bolt;\n"
"    border:1px;\n"
"    border-color:black;\n"
"    text-align:center;\n"
"}\n"
"\n"
"")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 70, 420, 351))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_add = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_add.setStyleSheet("background-color:orange;\n"
"width:100px;\n"
"height:80px;\n"
"font-size:14px;\n"
"font-weight: bolt;\n"
"border:none;\n"
"text-align:center;")
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 3, 3, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_6.setStyleSheet("background-color:white;\n"
"width:100px;\n"
"height:80px;\n"
"font-size:14px;\n"
"font-weight: 900;\n"
"border:none;\n"
"text-align:center;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setStyleSheet("background-color:white;\n"
"width:100px;\n"
"height:80px;\n"
"font-size:14px;\n"
"font-weight: 900;\n"
"border:none;\n"
"text-align:center;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)
        self.pushButton_clear = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_clear.setStyleSheet("background-color:grey;\n"
"width:100px;\n"
"height:80px;\n"
"font-size:14px;\n"
"font-weight: bolt;\n"
"border:none;\n"
"text-align:center;")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout.addWidget(self.pushButton_clear, 4, 0, 1, 1)
        self.pushButton_divison = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_divison.setStyleSheet("background-color:orange;\n"
"width:100px;\n"
"height:80px;\n"
"font-size:14px;\n"
"font-weight: bolt;\n"
"border:none;\n"
"text-align:center;")
        self.pushButton_divison.setObjectName("pushButton_divison")
        self.gridLayout.addWidget(self.pushButton_divison, 4, 2, 1, 1)
        self.pushButton_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_0.setStyleSheet("background-color:white;\n"
"width:100px;\n"
"height:80px;\n"
"font-size:14px;\n"
"font-weight: 900;\n"
"border:none;\n"
"text-align:center;")
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 4, 1, 1, 1)
        self.push_add2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.push_add2.setStyleSheet("background-color:orange;\n"
"width:100px;\n"
"height:80px;\n"
"font-size:14px;\n"
"font-weight: bolt;\n"
"border:none;\n"
"text-align:center;")
        self.push_add2.setObjectName("push_add2")
        self.gridLayout.addWidget(self.push_add2, 0, 3, 1, 1)
        self.pushButton_minus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_minus.setStyleSheet("background-color:orange;\n"
"width:100px;\n"
"height:80px;\n"
"font-size:14px;\n"
"font-weight: bolt;\n"
"border:none;\n"
"text-align:center;")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.gridLayout.addWidget(self.pushButton_minus, 4, 3, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setStyleSheet("background-color:white;\n"
"width:100px;\n"
"height:80px;\n"
"font-size:14px;\n"
"font-weight: 900;\n"
"border:none;\n"
"text-align:center;")
        self.pushButton_11.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_11.setDefault(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 0, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setStyleSheet("background-color:white;\n"
"width:100px;\n"
"height:80\n"
"px;\n"
"font-size:14px;\n"
"font-weight: 900;\n"
"border:none;\n"
"text-align:center;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setStyleSheet("background-color:white;\n"
"width:100px;\n"
"height:80px;\n"
"font-size:14px;\n"
"font-weight: 900;\n"
"border:1px;\n"
"text-align:center;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 0, 0, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_1.setStyleSheet("background-color:white;\n"
"width:100px;\n"
"height:75px;\n"
"font-size:14px;\n"
"font-weight: 900;\n"
"border:none;\n"
"text-align:center;")
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 3, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setStyleSheet("background-color:white;\n"
"width:100px;\n"
"height:75px;\n"
"font-size:14px;\n"
"font-weight: 900;\n"
"border:none;\n"
"text-align:center;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.pushButton_percent = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_percent.setStyleSheet("background-color:orange;\n"
"width:100px;\n"
"height:80px;\n"
"font-size:14px;\n"
"font-weight: bolt;\n"
"border:none;\n"
"text-align:center;")
        self.pushButton_percent.setObjectName("pushButton_percent")
        self.gridLayout.addWidget(self.pushButton_percent, 2, 3, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setStyleSheet("background-color:white;\n"
"width:100px;\n"
"height:80px;\n"
"font-size:14px;\n"
"font-weight: 900;\n"
"border:none;\n"
"text-align:center;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setStyleSheet("background-color:white;\n"
"width:100px;\n"
"height:80px;\n"
"font-size:14px;\n"
"font-weight: 900;\n"
"border:none;\n"
"text-align:center;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lineEdit.setStyleSheet("background-color:white\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_add.setText(_translate("Dialog", "+"))
        self.pushButton_6.setText(_translate("Dialog", "5"))
        self.pushButton_3.setText(_translate("Dialog", "3"))
        self.pushButton_clear.setText(_translate("Dialog", "AC"))
        self.pushButton_divison.setText(_translate("Dialog", "/"))
        self.pushButton_0.setText(_translate("Dialog", "0"))
        self.push_add2.setText(_translate("Dialog", "*"))
        self.pushButton_minus.setText(_translate("Dialog", "-"))
        self.pushButton_11.setText(_translate("Dialog", "9"))
        self.pushButton_5.setText(_translate("Dialog", "6"))
        self.pushButton_9.setText(_translate("Dialog", "7"))
        self.pushButton_1.setText(_translate("Dialog", "1"))
        self.pushButton_2.setText(_translate("Dialog", "2"))
        self.pushButton_percent.setText(_translate("Dialog", "%"))
        self.pushButton_4.setText(_translate("Dialog", "4"))
        self.pushButton_10.setText(_translate("Dialog", "8"))
