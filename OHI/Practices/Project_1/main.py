'''
1 for snake
-1 for water
0 for gun
'''
import random #for random computer input

computer = random.choice([-1,0,1])
youstr = input("Enter your choice(r/p/s): ")
youDict = {"r":1, "p":-1, "s":0}
you = youDict[youstr]
reverseDict = {1:"Rock", -1:"Paper", 0:"Scissors"}

print(f"You choose {reverseDict[you]} \nComputer choose {reverseDict[computer]}")

if (computer==you):
    print("It's a draw")

else:
    if(computer==0 and you == -1):
        print("You loose")
    elif(computer==0 and you == 1):
        print("You won!!!")
    elif(computer==1 and you==-1):
        print("You won!!!")
    elif(computer==1 and you==0):
        print("You loose")
    elif(computer==-1 and you==1):
        print("You loose")
    elif(computer==-1 and you ==0):
        print("You won!!!")
    else:
        print("Something went wrong")
