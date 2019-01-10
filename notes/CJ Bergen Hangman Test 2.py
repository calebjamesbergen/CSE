import random
guesses = 10
did_you_add_the_quotation_mark = False
word = ["Crypt?", "roast", "tenor", "tense", "loser", "train", "tears", "jerky", "abhor", "siren", "stair",  "arise",
        "tires", "arson", "jacky", "brick", "chair", "tread", "trail", "pouch", "abdomens",  "juxtaposed"]
word_guessed = []
truly_random_word = "Crypt?"
random.choice(word)
letters = list(truly_random_word)
while guesses > 0 and not "".join(word_guessed) == truly_random_word:
    print("You have %s guesses left" % guesses)
    letter_guessed = input("Guess a lowercase letter ")
    guesses -= 1
    for i in range(len(truly_random_word)):
        if truly_random_word[i] == letter_guessed:
            word_guessed.insert(i, letter_guessed)
            print("".join(word_guessed))
        if truly_random_word == "Crypt?" and not did_you_add_the_quotation_mark:
            word_guessed.append("?")
            did_you_add_the_quotation_mark = True
if "".join(word_guessed) == truly_random_word:
    print("You won")
else:
    print("You lose")
    print(truly_random_word)
