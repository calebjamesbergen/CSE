import random
guesses = 10
word = ["Crypt", "roast", "tenor", "tense", "loser", "train", "tears", "jerky", "abhor", "siren", "stair",  "arise",
        "tires", "arson", "jacky", "brick", "chair", "tread", "trail", "pouch", "abdomens",  "juxtaposed"]
word_guessed = ["_____"]
truly_random_word = "Crypt"
random.choice(word)
if truly_random_word == "abdomens":
    word_guessed = ["________"]
elif truly_random_word == "juxtaposed":
    word_guessed = ["_________"]
elif truly_random_word == "Crypt":
    word_guessed = ["_____?"]
print("".join(word_guessed))
while guesses > 0 and not "".join(word_guessed) == truly_random_word:
    print("You have %s guesses left" % guesses)
    letter_guessed = input("Guess a lowercase letter ")
    guesses -= 1
    for i in range(len(truly_random_word)):
        if truly_random_word[i] == letter_guessed:
            word_guessed_letters = list(word_guessed)
            word_guessed_letters[i] = letter_guessed
            word_guessed = "".join(word_guessed_letters)
            print("".join(word_guessed))
            guesses += 1
if "".join(word_guessed) == truly_random_word:
    print("You won")
else:
    print("You lose")
    print(truly_random_word)
