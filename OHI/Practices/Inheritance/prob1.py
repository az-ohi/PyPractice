class twoDVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show (self):
        print(f"The 2d vector is {self.i}i+{self.j}j..")

class threeDVector(twoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show (self):
        print(f"The 3d vector is {self.i}i+{self.j}j+{self.k}k..")

a = twoDVector(1,2)
a.show()
b= threeDVector(1,2,5)
b.show()

