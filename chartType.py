from abc import ABCMeta, abstractmethod
from observer import Subject, Observer, DisplayElement


class chart(Subject):
    def __init__(self):
        self._text = ""
        self._type = None
        self._observers = []

    def registerObserver(self, observer):
        self._observers.append(observer)

    def removeObserver(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notifyObservers(self):
        for o in self._observers:
            o.update(self._text, self._type)

    def text(self):
        return self._text

    def type(self):
        return self._type

    def radioChanged(self):
        self.notifyObservers()

    def setTextAndObject(self, text, ctype):
        self._text = text
        self._type = ctype
        self.radioChanged()


class abstractTextChanger(metaclass=ABCMeta):
    def __init__(self):
        self._text = None
        self._type = None


class changeText(abstractTextChanger, DisplayElement, Observer):
    def __init__(self, chartType, gui):
        self.chartType = chartType
        chartType.registerObserver(self)
        self.gui = gui

    def update(self, text, ctype):
        self._text = text
        self._type = ctype
        self.display()

    def display(self):
        self.gui.changeText(self._text)
        self.gui.ui.selectedRadio = self._type
