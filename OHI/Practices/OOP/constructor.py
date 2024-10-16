
class Employee:
    lang = "Python"
    salary = 50000

    def __init__(self, name, salary,lang):
        #dunder method which is automatically called
        self.name = name
        self.salary= salary
        self.lang=lang
        print("I am creating an object")

    def getinfo(self):
        print(f"The language is {self.lang} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


ohi = Employee("Ohi", 10000,"Java_script")
print(ohi.name, ohi.salary, ohi.lang)

