class employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"the class value of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0] #set first name as frame so 0 is given, because 0 is the first pos in set
        self.lname=value.split(" ")[1] #split device the string according space and makes a set

e = employee()
e.name = "Ayub Zawad"
e.a = 45
print(e.fname)
print(e.lname)
e.show()