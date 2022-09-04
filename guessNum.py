# != - не е равно
# int - число (не забравяй)
# \n - на нов ред
import random
num = random.randrange(1, 10)
guess = int(input("Guess a number between 1 and 10."))

while guess < 1 or guess > 10:
    print("This number can not be selected.\nPlease select a number within the given range.")
    guess = int(input("Guess a number between 1 and 10."))

while guess != num:
    if guess < num:
        print("The number you selected is lower than the generated one.")
        guess = int(input("Try again."))
    else:
        print("The number you selected is greater than the generated one.")
        guess = int(input("Try again."))

if guess == num:
    print("Congratulations! You guessed the number.")
