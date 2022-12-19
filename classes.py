class NumVariables:
    """Class of numeric variables"""

    def __init__(self, num=0):
        self._num = num

    def adder(self, arg):
        self._num += arg

    def setter(self, arg):
        self._num = arg

    def getter(self):
        return self._num

class BullVariables:
    """Class of Bullian variables"""

    def __init__(self, init_bul=True):
        self._bul = init_bul

    def setter(self, arg):
        self._bul = arg

    def changer(self):
        if self._bul:
            self._bul = False
        else:
            self._bul = True

    def getter(self):
        return self._bul