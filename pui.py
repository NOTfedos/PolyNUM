# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1016, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 581, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line_polynom = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_polynom.setObjectName("line_polynom")
        self.verticalLayout.addWidget(self.line_polynom)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 110, 160, 89))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_sum = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_sum.setCheckable(False)
        self.btn_sum.setObjectName("btn_sum")
        self.horizontalLayout.addWidget(self.btn_sum)
        self.btn_sub = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_sub.setCheckable(False)
        self.btn_sub.setObjectName("btn_sub")
        self.horizontalLayout.addWidget(self.btn_sub)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_mult = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_mult.setCheckable(False)
        self.btn_mult.setObjectName("btn_mult")
        self.horizontalLayout_2.addWidget(self.btn_mult)
        self.btn_div = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_div.setEnabled(False)
        self.btn_div.setCheckable(False)
        self.btn_div.setObjectName("btn_div")
        self.horizontalLayout_2.addWidget(self.btn_div)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_dxdy = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_dxdy.setEnabled(False)
        self.btn_dxdy.setCheckable(True)
        self.btn_dxdy.setObjectName("btn_dxdy")
        self.horizontalLayout_3.addWidget(self.btn_dxdy)
        self.btn_solve = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_solve.setEnabled(False)
        self.btn_solve.setObjectName("btn_solve")
        self.horizontalLayout_3.addWidget(self.btn_solve)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.btn_eq = QtWidgets.QPushButton(self.centralwidget)
        self.btn_eq.setGeometry(QtCore.QRect(210, 130, 75, 23))
        self.btn_eq.setCheckable(False)
        self.btn_eq.setObjectName("btn_eq")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(620, 30, 361, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.last_polynom = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.last_polynom.setText("")
        self.last_polynom.setObjectName("last_polynom")
        self.verticalLayout_3.addWidget(self.last_polynom)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 220, 191, 16))
        self.label_3.setObjectName("label_3")
        self.edtXValue = QtWidgets.QLineEdit(self.centralwidget)
        self.edtXValue.setGeometry(QtCore.QRect(210, 220, 113, 20))
        self.edtXValue.setObjectName("edtXValue")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 250, 61, 16))
        self.label_4.setObjectName("label_4")
        self.edtXResult = QtWidgets.QLineEdit(self.centralwidget)
        self.edtXResult.setGeometry(QtCore.QRect(210, 250, 113, 20))
        self.edtXResult.setReadOnly(True)
        self.edtXResult.setObjectName("edtXResult")
        self.btn_calculate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_calculate.setGeometry(QtCore.QRect(350, 220, 75, 23))
        self.btn_calculate.setObjectName("btn_calculate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1016, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Многочлен"))
        self.btn_sum.setText(_translate("MainWindow", "+"))
        self.btn_sub.setText(_translate("MainWindow", "-"))
        self.btn_mult.setText(_translate("MainWindow", "*"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_dxdy.setText(_translate("MainWindow", "dy/dx"))
        self.btn_solve.setText(_translate("MainWindow", "f(x) = 0"))
        self.btn_eq.setText(_translate("MainWindow", "="))
        self.label_2.setText(_translate("MainWindow", "Последние многочлены"))
        self.label_3.setText(_translate("MainWindow", "Вычислить значение при x равном"))
        self.label_4.setText(_translate("MainWindow", "Результат:"))
        self.btn_calculate.setText(_translate("MainWindow", "Вычислить"))

