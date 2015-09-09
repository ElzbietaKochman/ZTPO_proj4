from abc import ABCMeta, abstractmethod
from chartColorList import color_list


class Color(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self._name = "Nieznany kolor"
        self._num = -1
        self._paramName = color_list[self.__class__.__name__]

    @property
    def paramName(self):
        return self._paramName

    @property
    def name(self):
        return self._name

    @property
    def num(self):
        return self._num
