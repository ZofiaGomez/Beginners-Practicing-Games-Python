# First we import the module 'random' so we can get a random number in
# our functions, and we give it the alias 'r'

import random as r


# Then we create a variable that will hold a function that gives us a 
# random number inside the range we want

def start():
    print("Guess the number from range 1 to 10")

def game():
    global rand_num
    rand_num = r.randint(1, 10)

def inputuser():
    global i
    i = 0   
    while True:
        input_user = int(input("Input a number: "))
        # r.seed(r.random())
        if abs(input_user) <= 10 and abs(input_user) >= 1:
            
            i += 1

            if rand_num < input_user:
                print("The number is smaller...")
            elif rand_num > input_user:
                print("The number is bigger...")
            elif rand_num == input_user:
                print("Congrats! The number is correct.", "You have \
                    guessed the number after ", i, " tries")
                restart = str(input("Do you want to play again? (yes/no) "))
                if restart.lower() == "no":
                    print("Thanks for playing! Check more of Zophia Gomez in URL")
                    break
                elif restart.lower() == "yes":
                    start()
                    game()
                    inputuser()
        else:
            print("Invalid number")

start()
game()
inputuser()