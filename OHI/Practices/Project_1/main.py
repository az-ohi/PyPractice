'''
1 for snake
-1 for water
0 for gun
'''
import random #for random computer input

computer = random.choice([-1,0,1])
youstr = input("Enter your choice(s/w/g): ")
youDict = {"s":1, "w":-1, "g":0}
you = youDict[youstr]
reverseDict = {1:"Snake", -1:"Water", 0:"Gun"}

print(f"You choose {reverseDict[you]} \nComputer choose {reverseDict[computer]}")

if (computer==you):
    print("It's a draw")

else:
    if(computer==0 and you == -1):
        print("You Won")
    elif(computer==0 and you == 1):
        print("You loose")
    elif(computer==1 and you==-1):
        print("You loose")
    elif(computer==1 and you==0):
        print("You Won")
    elif(computer==-1 and you==1):
        print("You Won")
    elif(computer==-1 and you ==0):
        print("You loose")
    else:
        print("Something went wrong")
