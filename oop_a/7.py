class ones_threes_nines(object):
    def __init__(self, num):
        self.nines = num//9
        self.ones = num//1
        self.threes = num//3


n1 = ones_threes_nines(5)
print(n1.ones)
print(n1.threes)
print(n1.nines)