import random
guesses = 10
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
word_guessed = ""
random_word_list = ["pricy     ", "roast     ", "tenor     ", "tense     ", "loser     ", "train     ",
                    "tears     ", "jerky     ", "abhor     ", "siren     ", "stair     ", "arise     ",
                    "tires     ", "arson     ", "jacky     ", "brick     ", "chair     ", "tread     ", "trail     ",
                    "pouch     ", "abdomens  ", "juxtaposed"]
truly_random_word = random.choice(random_word_list)
letters = [truly_random_word[0], truly_random_word[1], truly_random_word[2], truly_random_word[3], truly_random_word[4],
           truly_random_word[5], truly_random_word[6], truly_random_word[7], truly_random_word[8], truly_random_word[9]]
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
    guesses = guesses - 1
    if letter_guessed == letters[0]:
        letter_guessed1 = letter_guessed
    elif letter_guessed == letters[1]:
        letter_guessed2 = letter_guessed
    elif letter_guessed == letters[2]:
        letter_guessed3 = letter_guessed
    elif letter_guessed == letters[3]:
        letter_guessed4 = letter_guessed
    elif letter_guessed == letters[4]:
        letter_guessed5 = letter_guessed
    elif letter_guessed == letters[5]:
        letter_guessed6 = letter_guessed
    elif letter_guessed == letters[6]:
        letter_guessed7 = letter_guessed
    elif letter_guessed == letters[7]:
        letter_guessed8 = letter_guessed
    elif letter_guessed == letters[8]:
        letter_guessed9 = letter_guessed
    elif letter_guessed == letters[9]:
        letter_guessed10 = letter_guessed
    word_guessed = (letter_guessed1 + letter_guessed2 + letter_guessed3 + letter_guessed4 + letter_guessed5 +
                    letter_guessed6 + letter_guessed7 + letter_guessed8 + letter_guessed9 + letter_guessed10)
    print(word_guessed)
if word_guessed == truly_random_word:
    print("You win!")
else:
    print("You lose. Ha!")
print(truly_random_word)
