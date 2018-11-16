import random
guesses = 10
word_guessed = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
letter_guessed1 = ""
letter_guessed2 = ""
letter_guessed3 = ""
letter_guessed4 = ""
letter_guessed5 = ""
letter_guessed6 = ""
letter_guessed7 = ""
letter_guessed8 = ""
letter_guessed9 = ""
letter_guessed10 = ""
random_word_list = ["pricy", "roast", "tenor", "tense", "loser", "train", "tears", "jerky", "abhor", "siren", "stair",
                    "arise", "tires", "arson", "jacky", "brick", "chair", "tread", "trail", "pouch", "abdomens",
                    "juxtaposed"]
truly_random_word = random.choice(random_word_list)
letters = list(truly_random_word)
if not truly_random_word == "abdomens  " or "juxtaposed":
    letter_guessed6 = " "
    letter_guessed7 = " "
    letter_guessed8 = " "
    letter_guessed9 = " "
    letter_guessed10 = " "
elif truly_random_word == "abdomens  ":
    letter_guessed9 = " "
    letter_guessed10 = " "
while guesses > 0 and not word_guessed == truly_random_word:
    print("You have %s guesses left" % guesses)
    letter_guessed = input("Guess a lowercase letter ")
    guesses -= 1
    if letter_guessed == letters[0]:
        word_guessed.index[0] = letter_guessed
    elif letter_guessed == letters[1]:
        word_guessed[1] = letter_guessed
    elif letter_guessed == letters[2]:
        word_guessed[2] = letter_guessed
    elif letter_guessed == letters[3]:
        word_guessed[3] = letter_guessed
    elif letter_guessed == letters[4]:
        word_guessed[4] = letter_guessed
    elif letter_guessed == letters[5]:
        word_guessed[5] = letter_guessed
    elif letter_guessed == letters[6]:
        word_guessed[6] = letter_guessed
    elif letter_guessed == letters[7]:
        word_guessed[7] = letter_guessed
    elif letter_guessed == letters[8]:
        word_guessed[8] = letter_guessed
    elif letter_guessed == letters[9]:
        word_guessed[9] = letter_guessed
    print(word_guessed)
if word_guessed == truly_random_word:
    print("You win!")
else:
    print("You lose. Ha!")
word_guessed = (letter_guessed1 + letter_guessed2 + letter_guessed3 + letter_guessed4 + letter_guessed5 +
                    letter_guessed6 + letter_guessed7 + letter_guessed8 + letter_guessed9 + letter_guessed10)
