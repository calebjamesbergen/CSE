guesses = 8
word = "Brick"
first_letter = "B"
second_letter = "r"
third_letter = "i"
fourth_letter = "c"
fifth_letter = "k"
letter_guessed2 = ""

# Random word generation
while guesses > 0 or not letter_guessed2 == word:
    letter_guessed = input("Guess a letter ")
    guesses = guesses - 1
    if letter_guessed == first_letter:
        letter_guessed2 = letter_guessed2 + letter_guessed
        print(letter_guessed2)
    elif letter_guessed == second_letter:
        letter_guessed2 = letter_guessed2 + letter_guessed
        print(letter_guessed2)
    elif letter_guessed == third_letter:
        letter_guessed2 = letter_guessed2 + letter_guessed
        print(letter_guessed2)
    elif letter_guessed == fourth_letter:
        letter_guessed2 = letter_guessed2 + letter_guessed
        print(letter_guessed2)
    elif letter_guessed == fifth_letter:
        letter_guessed2 = letter_guessed2 + letter_guessed
        print(letter_guessed2)
