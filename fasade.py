from layout import Ui_MainWindow, _translate
from PyQt4 import QtGui
from chartType import chart, changeText
from chartApp import matChart
from chartColor import Black, Blue, Green, Red, Violet
import csv
import matplotlib.pyplot as mpl


class WykresApp(QtGui.QMainWindow):
    _singleton = None

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.theX = []
        self.ui.theY = []

        self.colors = [Red(), Blue(), Black(), Green(), Violet()]
        for item in self.colors:
            self.addComboBoxItem(item.num, item.name)

        self.ui.wybierz.clicked.connect(self.selectFile)
        self.fileSelect = QtGui.QFileDialog(self)
        self.ui.rysuj.clicked.connect(self.printChart)
        self.scene = QtGui.QGraphicsScene()
        self.ui.slupkowy.clicked.connect(self.getSelectedRadio)
        self.ui.kolowy.clicked.connect(self.getSelectedRadio)
        self.ui.liniowy.clicked.connect(self.getSelectedRadio)
        self.ui.punktowy.clicked.connect(self.getSelectedRadio)
        self.ui.slupkowy.click()

    # singleton
    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(WykresApp, cls).__new__(cls, *args, **kwargs)
        return cls._singleton

    def changeText(self, text):
        self.ui.info.setText(text)

    def selectFile(self):
        self.fileSelect.name = self.fileSelect.getOpenFileName()
        self.ui.plik.setText(self.fileSelect.name)
        self.openFile()

    def openFile(self):
        with open(self.fileSelect.name, "r") as csvfile:
            file = csv.reader(csvfile, delimiter=',')
            for row in file:
                self.ui.theX.append(int(row[0]))
                if len(row) == 2:
                    self.ui.theY.append(int(row[1]))

    def printImage(self):
        pixmap = QtGui.QPixmap("wykres.png")
        self.ui.pole_wykresu.setScaledContents(True)
        self.ui.pole_wykresu.setPixmap(pixmap)

    def getSelectedRadio(self):
        chartType = chart()
        changeText(chartType, self)  # rejestrowanie obserwatora
        for radio in self.ui.groupBox.children():
            if radio.isChecked():
                if "kolowy" != radio.objectName():
                    chartType.setTextAndObject("Plik tekstowy, gdzie wierszem jest dwójka \n(x,y)", radio)
                else:
                    chartType.setTextAndObject("Plik tekstowy, gdzie wierszem jest dwójka \n(x, nazwa zmiennej)\n"
                                               "kolor - nie dotyczy", radio)

    def printChart(self):
        mpl.cla()
        charter = matChart()
        drawCorrectChart(charter, self.ui.selectedRadio.objectName(), self.ui.theX, self.ui.theY,
                         color=self.colors[self.ui.comboBox.currentIndex()].paramName)
        mpl.ylabel("Y")
        mpl.xlabel("X")
        mpl.savefig("wykres.png")
        self.printImage()

    def addComboBoxItem(self, num, name):
        self.ui.comboBox.addItem("")
        self.ui.comboBox.setItemText(num, _translate("MainWindow", name, None))


def drawCorrectChart(drawApp, ctype, theX, theY, **kwargs):
    drawApp.drawing(ctype, theX, theY, **kwargs)
