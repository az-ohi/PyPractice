
import random

n =random.randint(1,100)

a = -1 #condition for entering into while loop
guesses = 0
while (a!=n):
    a = int(input("Guess the number: "))

    if (a>n):
        print("\nLower Number please")
        guesses += 1

    elif(a==n):
        print(f"\nYou have guessed the number {n} in {guesses} attempts")

    else:
        print("\nHigher number please")
