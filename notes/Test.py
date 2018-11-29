import random
random_word_list = ["pricy", "roast", "tenor", "tense", "loser", "train", "tears", "jerky", "abhor", "siren", "stair",
                    "arise", "tires", "arson", "jacky", "brick", "chair", "tread", "trail", "pouch", "abdomens",
                    "juxtaposed"]
truly_random_word = random.choice(random_word_list)
if truly_random_word == (random_word_list[:19]):
    print(truly_random_word)
