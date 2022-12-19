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