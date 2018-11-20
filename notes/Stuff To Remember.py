import random
# Terminal = the display bar that pops up when you run a code
random_word_list = ["pricy", "roast", "tenor", "tense", "loser", "train", "tears", "jerky", "abhor", "siren", "stair",
                    "arise", "tires", "arson", "jacky", "brick", "chair", "tread", "trail", "pouch", "abdomens",
                    "juxtaposed"]
truly_random_word = random.choice(random_word_list)
letters = list(truly_random_word)
print(letters)
letters2 = truly_random_word[0] + truly_random_word[1]
print(letters2)
if 0 == 0:
    word = letters + list("     ")
print(word)
