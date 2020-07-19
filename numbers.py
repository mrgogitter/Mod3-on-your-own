#Interactive numbers guessing game

import random

guessesUsed = 0

print('What is your name? ')     #asks for user's name
yourName = input()

secretNumber = random.randint(1, 20)
print('So, ' + yourName + ', Lets see how smart you are. I am thinking of a number between 1 and 20.')     #invites user to play guess the number I am thinking of

for guessesUsed in range(3):     #loop for guessing process
    print('Guess which one...')
    guess = input()
    guess = int(guess)
    
    if guess < secretNumber:
        print('You guessed too low.')
        
    if guess > secretNumber:
        print('You guessed to high.')
        
    if guess == secretNumber:
        break
        
if guess == secretNumber:
    guessesUsed = str(guessesUsed + 1)
    print('Nice going, ' + yourName + ' you guessed the number in ' + guessesUsed + ' guesses!')     #user guessed right
    
if guess != secretNumber:
    secretNumber = str(secretNumber)
    print('Better luck next time...The number I was thinking of was ' + secretNumber + '.')     #user was wrong