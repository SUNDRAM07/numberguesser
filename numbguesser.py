import random
def guess():   
    name=input("What is your name ")       
    random_number = random.randrange(100)
    guesses=int(input("number of guesses you want to guess in:"))
    i=1   #on default it is 0 to 10
    while(i<=guesses):
        ur_guess=int(input("your guess:"))
        if ur_guess < random_number:
            print("your guess is less :( ")
            i+=1
        elif ur_guess > random_number:
            print("your guess is greater :( ")
            i+=1
        else:
            print("your guessed it right :) ")
            print("you guessed it in "+str(i)+" times!!")
            print("Player name: "+name+ " record: "+str(i))
            re=input("would you like to play again y or n ? ")[0].lower()
            if(re=="y"):
                print("YOU'R WISH")
                guess()
            else:
                quit()
game=input("Would you like to play the game of number guesser Y or N? " )[0].lower()
if game=="y" :
    print("Welcome to the number guessing game") 
    guess()   
else:
    l_chance=input("Are you sure you wanna leave? ")[0].lower()
    if l_chance=="y":
        quit()
    else:
        print("Welcome to the number guessing game")
        guess()
                
