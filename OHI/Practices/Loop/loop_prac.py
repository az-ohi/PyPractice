l = ["Ohi", "Oli", "Abbu", "Ammu"]

for i in l:
    if (i.startswith("O")):
        print(f"Hello {i}")

# Prime number check

n = int(input("Enter the number:"))

for i in range(2, n):
    if(n%i == 0):
        print(f"The {n} number is not prime")
        break #once a number found it will break no need for further progress
else:
    print(f"The {n} number is prime")

# sum of till n

n = int(input("Enter the value of n: "))

i = 0
sum = 0

while(i<=n):
    sum += i
    i +=1

print(f"The sum is {sum}")


# factorial

n = int(input("Enter the number: "))

i = 1
fact = 1

while(i<=n):
    fact = fact*i
    i += 1

print(f"The factorial is {fact}")

# with for loop

n = int(input("Enter the number: "))

fact_n = 1

for i in range(1,n+1):
    fact_n = fact_n*i

print(f"The factorial of the {n} is {fact_n} ")



























