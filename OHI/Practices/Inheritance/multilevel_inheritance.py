class  employee:
    a = 1

class programmer(employee):
    b = 2

class mananger(programmer):
    c = 3

e= employee()
print(e.a)

p = programmer()
print(p.b, p.a)

m = mananger()
print(m.c, m.b, m.a)