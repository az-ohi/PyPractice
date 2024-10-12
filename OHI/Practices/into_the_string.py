name = "ohi"
name_a = 'Ayub'
name_b = '''Zawad'''
print(name_a)
print(name_b)
print(name)
name_c = '''Ayub
Zawad
Ohi'''
print(name_c)
name_slice = name[0:2]
print(name_slice)

print(len(name_b))
print(name_a.endswith("ub"))
print(name_a.startswith("Ay"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print("I am Ohi.\nI am a good boy")

g_name = input("Enter your name")
print("Good evening",g_name)

x = "OHI"
age = 28
print(f"My name is {x} and I am {age} years old")
print("My name is {} and I am {} years old".format(x,age))
print("My name is %s and I am %d years old" %(x,age))


formal = '''Dear name
You are selcted for the project
Date: xxy
'''
print(formal.replace("name","Ohi").replace("xxy","12,Oct,2024"))


















































