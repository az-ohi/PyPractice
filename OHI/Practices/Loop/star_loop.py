n = int(input("Enter n: "))
for ii in range(1, n+1):
    print("*"*ii, end="")
    print()


# star with gap with odd seq


nn= int(input("Enter n: "))


for i in  range(1, nn + 1):
    print(" " * (nn - i), end="") #end= "" doesnt give new line in default
    print("*"*(2*i-1),end="")
    print()























