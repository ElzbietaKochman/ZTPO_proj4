from absChartColor import Color


class Red(Color):
    def __init__(self):
        super().__init__()
        self._name = "czerwony"
        self._num = 0


class Blue(Color):
    def __init__(self):
        super().__init__()
        self._name = "niebieski"
        self._num = 1


class Black(Color):
    def __init__(self):
        super().__init__()
        self._name = "czarny"
        self._num = 2


class Green(Color):
    def __init__(self):
        super().__init__()
        self._name = "zielony"
        self._num = 3


class Violet(Color):
    def __init__(self):
        super().__init__()
        self._name = "fioletowy"
        self._num = 4
