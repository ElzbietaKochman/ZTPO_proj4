from abc import ABCMeta, abstractmethod


class Drawer(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self._name = ""

    @property
    def name(self):
        return self._name

    def draw(self, x, y):
        pass

    def __str__(self):
        return self.name
