from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def registerObserver(self, observer):
        pass

    @abstractmethod
    def removeObserver(self, observer):
        pass

    @abstractmethod
    def notifyObservers(self, observer):
        pass


class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, text):
        pass


class DisplayElement(metaclass=ABCMeta):

    @abstractmethod
    def display(self):
        pass
