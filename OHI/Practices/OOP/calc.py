import math #for square root

class calculator:
    def __init__(self, n):
        self.n =n

    def square(self):
        print(f"The square is {(self.n)*(self.n)}")

    def cube(self):
        print(f"The cube is {(self.n)*(self.n)*(self.n)}")

    def root(self):
        print(f"The root is {math.sqrt(self.n)}") #alternative: (self.n)**.5

    @staticmethod
    def greet():
        print("Hello There!!!")

x = int(input("Enter the number you want to square, cube and square root: "))
a= calculator(x)
a.greet()
a.square()
a.cube()
a.root()
