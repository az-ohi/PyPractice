class Demo:
    a = 4

o = Demo()
print(o.a) #it will print class attribute because instance attribute is not present
o.a = 0 #instance attribute is declared
print(o.a) #so it prints instance attribute
print(Demo.a) #but class attribute is not changed