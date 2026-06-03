'''
1 for snake
-1 for water
0 for gun
'''
import random



computer = random.choice([1,0,-1])
you = input("Enter your choice: ")
yourDict = {"s": 1, "w": -1, 'g':0}
revdict = {1:"Snake", -1:"Water", 0:'Gun'}
younum = yourDict[you]
print(f"Computer chose:{revdict[computer]} vs you chose: {revdict[yourDict[you]]} ")

if(computer == younum):
    print("This is draw!!")
else:


    if(computer == -1 and younum ==1):
        print("You win!!")
    elif(computer == -1 and younum ==0):
        print("You lose!!")
    elif(computer == 1 and younum ==0):
        print("You Win!!")
    elif(computer == 0 and younum ==1):
        print("You win!!")
    elif(computer == 1 and younum ==-1):
        print("You lose!!")
    elif(computer == 0 and younum ==-1):
        print("You lose!!")
    else:
        print("something wrong")