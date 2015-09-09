from factoryDraw import Drawer
from matplotlib import pyplot as mpl


class slupkowy(Drawer):
    def __init__(self):
        super.__init__()
        self._name = "slupkowy"

    def draw(self, theX, theY, **kwargs):
        mpl.bar(theX, theY, **kwargs)


class punktowy(Drawer):
    def __init__(self):
        super.__init__()
        self._name = "punktowy"

    def draw(self, theX, theY, **kwargs):
        mpl.scatter(theX, theY, **kwargs)


class liniowy(Drawer):
    def __init__(self):
        super.__init__()
        self._name = "liniowy"

    def draw(self, theX, theY, **kwargs):
        mpl.plot(theX, theY, **kwargs)


class kolowy(Drawer):
    def __init__(self):
        super.__init__()
        self._name = "kolowy"

    def draw(self, theX, theY, **kwargs):
        mpl.pie(theX, None, theY)

