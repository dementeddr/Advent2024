class binary_counter():
    
    counter = 0
    index = 0

    def __init__(self, num):
        self.counter = num

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        bit = bool((self.counter >> self.index) & 1)
        self.index += 1
        return bit
