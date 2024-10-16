def is_prime(n):
    # Prime numbers are greater than 1
    if n <= 1:
        return False
    # Check divisibility from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Input from user
number = int(input("Enter a number: "))

# Check if the number is prime
if (is_prime(number)==True):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
