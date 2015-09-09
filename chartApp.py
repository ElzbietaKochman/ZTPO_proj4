from absDrawCreate import makeDraw
from matdraw import kolowy,liniowy,punktowy,slupkowy


class matChart(makeDraw):

    def __init__(self):
        self._chartTypes = {
            "kolowy": kolowy,
            "liniowy": liniowy,
            "punktowy": punktowy,
            "slupkowy": slupkowy
        }

    def drawChart(self, ctype):
        return self._chartTypes[ctype]

