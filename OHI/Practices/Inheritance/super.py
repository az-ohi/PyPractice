class  employee:
    def __init__(self):
        print("Constructor of employee")
    a = 1

class programmer(employee):
    def __init__(self):
        print("Constructor of employee")
    b = 2

class mananger(programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of programmer")
    c = 3

# e= employee()
# print(e.a)
#
# p = programmer()
# print(p.b, p.a)

m = mananger()
print(m.c, m.b, m.a)