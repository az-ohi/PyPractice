def f_to_c(f):
    return (5*(f-32)/9)

f = int(input("Enter the temp in F: "))
a = f_to_c(f)
print(f"The temp in C is {round(a, 2)}") #round for trimming the float value


