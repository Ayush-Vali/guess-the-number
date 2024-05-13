# import cleanversion

import random

def guess():
    
    lvl=input("Select the dificulty level: 'easy' or 'hard'=")
    gnum=int(input("Guess the number between 1 to 100="))
    rightguess=random.randint(1,100)
    #when first number itself gets right
    if gnum==rightguess:
        print("You guessed the right number on first guess")
    else:
        if gnum>rightguess:
            print("Too high")
        else:
            print("Too low")#first guess hints
            
        if lvl=="easy":
            for c in range(10):
                i=10-c
                print(f"You have only {i} chances to guess the number")
                gnum=int(input("Guess the number again, between 1 to 100="))
                if gnum>rightguess:
                    print("Too high")
                elif gnum==rightguess:
                    print("You guessed the right number")
                    break
                else:
                    print("Too low")
            if i==1:
                print(f"You have run out of chances, the right number was {rightguess}")
        else:
            for c in range(5):
                i=5-c
                print(f"You have only {i} chances to guess the number")
                gnum=int(input("Guess the number again, between 1 to 100="))
                if gnum>rightguess:
                    print("Too high")
                elif gnum==rightguess:
                    print("You guessed the right number")
                    break
                else:
                    print("Too low")
            if i==1:
                print(f"You have run out of chances, the right number was {rightguess}")
    

gamin=True
while gamin:
    start=input("Do you want to start the game?: yes or no ").lower()
    if start == "yes":
      print("Welcome to the game")
      guess()
    else:
      print("Goodbye")
      
      gamein=False