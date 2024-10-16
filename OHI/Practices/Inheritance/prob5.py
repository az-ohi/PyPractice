class complex:
    def __init__(self, l):
        self.l =l

    def __len__(self):
        return len(self.l)


c1 = complex([1,2,3,4,5,6,6,6])


print(len(c1))