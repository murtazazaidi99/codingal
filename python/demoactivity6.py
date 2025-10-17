import random
number = random.randint(0,100 )
guess = int(input("Guess a number between 0and 100: "))
if guess == secret_number:
   print(" Correct! You guessed the number.")
else:
    print(" Wrong! The number was {number}.")