class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pinc):
        self.name = name
        self.salary = salary
        self.pinc = pinc

p = programmer("Ohi", 10000, 1380)
print(p.name,p.salary,p.pinc,p.company)

r = programmer("Oli", 12000, 1380)
print(r.name,r.salary,r.pinc,r.company)
