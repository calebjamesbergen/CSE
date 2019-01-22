import random
guesses = 10
did_you_win = False
word = ["Crypt", "roast", "tenor", "tense", "loser", "train", "tears", "jerky", "abhor", "siren", "stair",  "arise",
        "tires", "arson", "jacky", "brick", "chair", "tread", "trail", "pouch", "abdomens",  "juxtaposed"]
word_guessed = "_____"
truly_random_word = random.choice(word)
if truly_random_word == "abdomens":
    word_guessed = "________"
elif truly_random_word == "juxtaposed":
    word_guessed = "__________"
elif truly_random_word == "Crypt?":
    word_guessed = "_____?"
print("".join(word_guessed))
while guesses > 0 and not word_guessed == truly_random_word and not did_you_win:
    print("You have %s guesses left" % guesses)
    letter_guessed = input("Guess a lowercase letter ")
    guesses -= 1
    word_guessed_letters = list(word_guessed)
    if letter_guessed == "c" and truly_random_word == "Crypt?":
        word_guessed_letters[0] = "C"
    if len(letter_guessed) > 1:
        if letter_guessed == truly_random_word:
            word_guessed = letter_guessed
            did_you_win = True
    else:
        for i in range(len(truly_random_word)):
            if truly_random_word[i] == letter_guessed or truly_random_word[i] == str.lower(letter_guessed)\
                    or truly_random_word[i] == str.upper(letter_guessed):
                guesses += 1
                word_guessed_letters[i] = truly_random_word[i]
        word_guessed = "".join(word_guessed_letters)
        print(word_guessed)
if word_guessed == truly_random_word:
    print("You won")
else:
    print("You lose")
    print(truly_random_word)
