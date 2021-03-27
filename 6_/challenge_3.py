#Modify the program below to use a while loop to
#allow as many guesses as necessary.
#
#The program should let the player know whether to
#guess higher or lower, and should print a message
#when the guess is correct.a correct guess will
#terminate the programme

#As an optional extra, allow the player to quit by entering
#0 (zero) for their guess

import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ",format(highest ))
guess = 0 # initialize to any number outside of the valid range

while guess != answer:
    guess = int(input())
    if guess < answer:
        print("Please guess higher ")
    elif guess > answer: #guess must be greater than number
        print("Please guess lower")

    else:
        print("great, You guessed it")




