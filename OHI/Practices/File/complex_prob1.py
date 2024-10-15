import random
from doctest import script_from_examples


def game():
    print("You are playing a game")
    score = random.randint(1,81)
#     fetch the high score
    with open("high_score.txt") as f:
        highscore = f.read()
        if (highscore != ""):
            highscore= int(highscore) #because f.read reads in string form
        else:
            highscore = 0
    print(f"Your score is {score}")
    if(score> highscore):
        with open("high_score.txt", "w") as f:
            f.write(str(score))
    return score

game()

