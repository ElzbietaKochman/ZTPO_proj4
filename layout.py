# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wykres.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(650, 570)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 390, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.wybierz = QtGui.QPushButton(self.centralwidget)
        self.wybierz.setGeometry(QtCore.QRect(220, 400, 91, 51))
        self.wybierz.setObjectName(_fromUtf8("wybierz"))
        self.plik = QtGui.QLabel(self.centralwidget)
        self.plik.setGeometry(QtCore.QRect(320, 400, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plik.setFont(font)
        self.plik.setObjectName(_fromUtf8("plik"))
        self.rysuj = QtGui.QPushButton(self.centralwidget)
        self.rysuj.setGeometry(QtCore.QRect(460, 470, 171, 81))
        self.rysuj.setObjectName(_fromUtf8("rysuj"))
        self.pole_wykresu = QtGui.QLabel(self.centralwidget)
        self.pole_wykresu.setGeometry(QtCore.QRect(20, 10, 601, 361))
        self.pole_wykresu.setText(_fromUtf8(""))
        self.pole_wykresu.setObjectName(_fromUtf8("pole_wykresu"))
        self.info = QtGui.QLabel(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(160, 500, 261, 51))
        self.info.setText(_fromUtf8(""))
        self.info.setObjectName(_fromUtf8("info"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(290, 471, 141, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 470, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 420, 120, 141))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.liniowy = QtGui.QRadioButton(self.groupBox)
        self.liniowy.setGeometry(QtCore.QRect(10, 110, 82, 17))
        self.liniowy.setObjectName(_fromUtf8("liniowy"))
        self.slupkowy = QtGui.QRadioButton(self.groupBox)
        self.slupkowy.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.slupkowy.setObjectName(_fromUtf8("slupkowy"))
        self.punktowy = QtGui.QRadioButton(self.groupBox)
        self.punktowy.setGeometry(QtCore.QRect(10, 80, 82, 17))
        self.punktowy.setObjectName(_fromUtf8("punktowy"))
        self.kolowy = QtGui.QRadioButton(self.groupBox)
        self.kolowy.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.kolowy.setObjectName(_fromUtf8("kolowy"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Aplikacja do rysowania wykresów", None))
        self.label.setText(_translate("MainWindow", "Typ wykresu", None))
        self.wybierz.setText(_translate("MainWindow", "Wybierz plik", None))
        self.plik.setText(_translate("MainWindow", "(Wybrany plik)", None))
        self.rysuj.setText(_translate("MainWindow", "RYSUJ WYKRES", None))
        self.label_2.setText(_translate("MainWindow", "Kolor:", None))
        self.liniowy.setText(_translate("MainWindow", "Liniowy", None))
        self.slupkowy.setText(_translate("MainWindow", "Słupkowy", None))
        self.punktowy.setText(_translate("MainWindow", "Punktowy", None))
        self.kolowy.setText(_translate("MainWindow", "Kołowy", None))

