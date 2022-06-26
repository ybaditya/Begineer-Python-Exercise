#Generate a random number between 1 and 9 (including 1 and 9).
#  Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.
#  (Hint: remember to use the user input lessons from the very first exercise)
#Extras:

#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, 
# and when the game ends, print this out.

import random

computerGuess = random.randint(1,9)
playerInput = (input('Guess a Number 1 to 9 :'))

if computerGuess == int(playerInput):
    print("Your Guess is Right, YOU'RE SO LUCKY")
    quit()
elif computerGuess > int(playerInput):
    print("Too Low, GuessCounter = 1")
elif computerGuess < int(playerInput):
    print("Too High, GuessCounter = 1")
else:
    print("Wrong format")

countGuess = 1
while computerGuess != playerInput:
    playerInput = (input('Guess a Number 1 to 9 or exit :'))
    if computerGuess == int(playerInput):
        countGuess +=1
        print("Your Guess is Right GuessCounter = " + str(countGuess))
        break
    elif playerInput == "exit":
        print("Thanks for Playing")
        break
    elif computerGuess > int(playerInput):
        countGuess +=1
        print("Too Low, GuessCounter = " + str(countGuess))
    elif computerGuess < int(playerInput):
        countGuess +=1
        print("Too High, GuessCounter = " + str(countGuess))
    else:
        countGuess +=1
        print("Wrong format")