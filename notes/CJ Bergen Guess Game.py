import random
wrong_guesses = 0
number = (random.randint(1, 10))
wrong_or_right = False
while wrong_guesses < 5 and not wrong_or_right:
    guess = int(input("Guess a number"))
    wrong_or_right = guess == number
    if guess > number:
        print("Guess lower")
        wrong_guesses += 1
    elif guess < number:
        print("Guess higher")
        wrong_guesses += 1
    elif guess == number:
        print("You win!")
        wrong_or_right = True
