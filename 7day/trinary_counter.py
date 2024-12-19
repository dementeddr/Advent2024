import numpy

class trinary_counter():
    
    counter = ''
    index = 0

    def __init__(self, num):
        self.counter = numpy.base_repr(num, 3)[::-1]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.counter):
            return 0

        tit = int(self.counter[self.index])
        self.index += 1
        return tit
