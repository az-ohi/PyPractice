class complex:
    def __init__(self, r, i):
        self.r = r  # Real part
        self.i = i  # Imaginary part

    def __add__(self, cn):
        return complex(self.r + cn.r, self.i + cn.i)

    def __mul__(self, cn):
        # (a+bi) * (c+di) = (ac - bd) + (ad + bc)i
        real_part = self.r * cn.r - self.i * cn.i
        imaginary_part = self.r * cn.i + self.i * cn.r
        return complex(real_part, imaginary_part)

    def __str__(self):
        return f"{self.r} + {self.i}i"

# Testing the class
c1 = complex(1, 2)
c2 = complex(3, 4)

# Addition
print(c1 + c2)  # Output: 4 + 6i

# Multiplication
print(c1 * c2)  # Output: -5 + 10i
