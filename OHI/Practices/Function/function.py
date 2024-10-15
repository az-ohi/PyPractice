# # a = int (input("Enter your number: "))
# # b = int (input("Enter your number: "))
# # c = int (input("Enter your number: "))
# # print((a+b+c)/3)

# # Function defination

def avg():
    a = int(input("Enter your number: "))
    b = int (input("Enter your number: "))
    c = int (input("Enter your number: "))
    average = (a+b+c)/3
    print(average)

# # Function call

avg()
print("Thank you")
avg()
print("Thank you")

# return value

def avg():
    a = int(input("Enter your number: "))
    b = int (input("Enter your number: "))
    c = int (input("Enter your number: "))
    average = (a+b+c)/3
    return average

print(f"The average is {avg()}")


