class Employee:
    company = "RUMC"
    def show(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"The name of the employee is {self.name} and the salary is {self.salary}.")

class coder:
    language = "Java_script"
    def print_lang(self):
        print(f"Out of all languages here is your language: {self.language}")


class programmer(Employee, coder):
    company = "MBSTU"
    def show_lang(self, lang):
        self.lang = lang
        print(f"He is good at {self.lang}")

# a = Employee()
# b = coder()
c = programmer()

# print(a.company, c.company)

#here by c. we can find all function because we include all function in programmer class

c.show("Ohi", 10000)
c.print_lang()
c.show_lang("Python")
