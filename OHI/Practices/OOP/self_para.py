class Employee:
    lang = "Python" #This is a class attributes
    salary = 50000
    def getinfo(self):
        print(f"The language is {self.lang} and the salary is {self.salary}")


ohi = Employee()
ohi.lang= "Java_Script" #This is a object/instance attributes
ohi.getinfo()
Employee.getinfo(ohi) #did the same this as upper line code

class Employee:
    lang = "Python" #This is a class attributes
    salary = 50000
    def getinfo(self):
        print(f"The language is {self.lang} and the salary is {self.salary}")

    def greet(self):
        print("Good Morning")


ohi = Employee()
ohi.lang= "Java_Script" #This is a object/instance attributes
ohi.getinfo()
# Employee.getinfo(ohi) #did the same this as upper line code
ohi.greet()

# static method doesnt require self

class Employee:
    lang = "Python" #This is a class attributes
    salary = 50000
    def getinfo(self):
        print(f"The language is {self.lang} and the salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good Morning")


ohi = Employee()
ohi.lang= "Java_Script" #This is a object/instance attributes
ohi.getinfo()
# Employee.getinfo(ohi) #did the same this as upper line code
ohi.greet()





