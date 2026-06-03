
#2. The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file Hi-score.txt which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the high-score

import random
def game():
    print("you're playing the game...")
    score = random.randint(1,62)
    print("Your score is: ", score)

    with open('ch9/practice/2high_score.txt') as f:
        hiscore = f.read()
        print("The previous hiscore is: ", hiscore)
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    if(score>hiscore) or hiscore =="":
        #write code
        with open('ch9/practice/2high_score.txt', 'w') as f:
            f.write(str(score))
    return score

game()