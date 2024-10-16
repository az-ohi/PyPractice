class Employee:
    lang = "Python" #This is a class attributes
    salary = 50000

ohi = Employee()
ohi.name= "Ohi" #This is a object/instance attributes
print(ohi.name,ohi.lang, ohi.salary )

oli = Employee()
oli.name= "Oli"
print(oli.name,oli.lang, oli.salary )

# Here "name" is object/instance attribute where "lang" and "salary" is class attributes because they belongs to class

