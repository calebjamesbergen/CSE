import random
guesses = 8
first_letter = ""
second_letter = ""
third_letter = ""
fourth_letter = ""
fifth_letter = ""
letter_guessed1 = ""
letter_guessed2 = ""
letter_guessed3 = ""
letter_guessed4 = ""
letter_guessed5 = ""
word_guessed = ""
WORDS = ("chair", "brick", "jerky")
random_word = random.choice(WORDS)
word = random_word

if random_word == "jerky":
    first_letter = "j"
    second_letter = "e"
    third_letter = "r"
    fourth_letter = "k"
    fifth_letter = "y"
if random_word == "chair":
    first_letter = "c"
    second_letter = "h"
    third_letter = "a"
    fourth_letter = "i"
    fifth_letter = "r"
if random_word == "brick":
    first_letter = "b"
    second_letter = "r"
    third_letter = "i"
    fourth_letter = "c"
    fifth_letter = "k"

# Random word generation
while guesses > 0 and not word_guessed == random_word:
    print("You have %s guesses left" % guesses)
    letter_guessed = input("Guess a lowercase letter ")
    guesses = guesses - 1
    if letter_guessed == first_letter:
        letter_guessed1 = letter_guessed
    elif letter_guessed == second_letter:
        letter_guessed2 = letter_guessed
    elif letter_guessed == third_letter:
        letter_guessed3 = letter_guessed
    elif letter_guessed == fourth_letter:
        letter_guessed4 = letter_guessed
    elif letter_guessed == fifth_letter:
        letter_guessed5 = letter_guessed
    word_guessed = letter_guessed1 + letter_guessed2 + letter_guessed3 + letter_guessed4 + letter_guessed5
    print(word_guessed)

if guesses > 0:
    print("You win!")
