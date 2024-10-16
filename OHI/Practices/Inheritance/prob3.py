class Employee:
    pass
e = Employee()
e.salary = 500
e.increment = 20

print(e.salary, e.increment)

#or as a class

class Employee:
    salary = 500
    increment = 20

    @property
    def salary_after_increment(self):
        return (self.salary + self.salary*(self.increment/100))

    @salary_after_increment.setter
    def salary_after_increment(self,new_salary):
        self.increment= ((new_salary/self.salary)-1)*100


e = Employee()
print(e.salary_after_increment)
e.salary_after_increment= 600
print(round(e.increment ,1))

