from abc import ABCMeta, abstractmethod


class makeDraw(metaclass=ABCMeta):
    @abstractmethod
    def drawChart(self, ctype):
        return NotImplemented

    def drawing(self, ctype, theX, theY, **kwargs):
        cha = self.drawChart(ctype)

        cha.draw(self, theX, theY, **kwargs)

        return cha
