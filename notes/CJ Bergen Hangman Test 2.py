import random
guesses = 10
random_word_list = ["pricy", "roast", "tenor", "tense", "loser", "train", "tears", "jerky", "abhor", "siren", "stair",
                    "arise", "tires", "arson", "jacky", "brick", "chair", "tread", "trail", "pouch", "abdomens",
                    "juxtaposed"]
word_guessed = []
truly_random_word = random.choice(random_word_list)
letters = list(truly_random_word)
print(*letters, sep="")
while guesses > 0 and not "".join(word_guessed) == truly_random_word:
    print("You have %s guesses left" % guesses)
    letter_guessed = input("Guess a lowercase letter ")
    guesses -= 1
    for i in range(len(truly_random_word)):
        if truly_random_word[i] == letter_guessed:
            word_guessed.insert(i, letter_guessed)
            print("".join(word_guessed))
if "".join(word_guessed) == truly_random_word:
    print("You won")
