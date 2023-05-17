import random


dice1=[1, 2, 3, 4, 5, 6]
dice2=[1, 2, 3, 4, 5, 6]
dice=[dice1, dice2]
def result():
    myinput = input("print 'roll':")
    if myinput == "roll":
        roll1 = random.choice(dice1)
        roll2 = random.choice(dice2)
        return int(roll1) + int(roll2)

def roll():
    rollresult = result()
    print(rollresult)
    if rollresult in (7, 11):
        print("You won")
        return
    elif rollresult in (2, 3, 12):
        print("Casino won")
        return
    else:
        goal=rollresult
    while True:
        rollresult = result()
        if rollresult == 7:
            print("Casino won")
            return
        elif rollresult == goal:
            print("You won")
            return
        else:
            print(rollresult)
roll()