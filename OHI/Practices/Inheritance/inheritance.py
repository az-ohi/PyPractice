class Employee:
    company = "RUMC"
    def show(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"The name of the employee is {self.name} and the salary is {self.salary}.")

class programmer(Employee):
    company = "MBSTU"
    def show_lang(self, lang):
        self.lang = lang
        print(f"He is good at {self.lang}")

a = Employee()
b = programmer()
print(a.company, b.company)
a.show("Ohi", 10000)
b.show_lang("Python")