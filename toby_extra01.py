import random
#i feel like i could have had the random number generation be seperate from the main game in a lot more graceful of a way but whatever
def numgamewnewnum():
    global secretnum
    secretnum = random.randint(2, 999) #you said between 1 and 1000 so i assumed that meant not inclusive
    global guesses
    guesses = 0
    global invalids
    invalids = 0
    numgame()
def numgame():
    global userguess
    userguess= input("guess a number between 1 and 1000? ")
    if userguess.isdigit() == False:
        userguess = 1
    global userguessi
    userguessi = int(userguess)
    if guesses == 10:
        pagainl = input("uh oh, no more guesses left. do you want to play again? y/n ?")
        if pagainl == "n" or "N":
            exit()
        elif pagainl == "y" or "Y":
            numgamewnewnum()
            #i know its not that graceful to just close everything if one declines to play  again but what else coulkd i do? also i was to lazy to really acount for not yes no answers.         
    if userguessi < 1000 and userguessi > 1:
        Answer()
    else:
        print("that's not a possible answer!") 
        global invalids
        invalids += 1
        if invalids == 10:
            print("you literally wasted all your guesses on answers that couldn't possibly be correct, i give up")
            exit()
        else:
             print("whatever, guess again...")
             numgame()
def Answer():
    global guesses
    guesses += 1
    if userguessi < secretnum:
        print("think higher, guess again")
        numgame()
    if userguessi > secretnum:
        print("think lower, guess again")
        numgame()
    if userguessi == secretnum:
        print("DING DING DING weeeee Haaaaavvvvee a wiiiinnnnerrr!!!!!!!!")
        pagainw = input("anyways do you want to play again y/n ?")
    if pagainw == "n" or "N":
        exit()
    elif pagainw == "y" or "Y":
        numgamewnewnum()
numgamewnewnum()




   
        
