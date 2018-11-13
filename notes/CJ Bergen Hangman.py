import random
guesses = 8
letter_guessed1 = ""
letter_guessed2 = ""
letter_guessed3 = ""
letter_guessed4 = ""
letter_guessed5 = ""
word_guessed = ""
random_word_list = ["pricy     ", "roast     ", "tenor     ", "tense     ", "loser     ", "train     ",
                    "tears     ", "jerky     ", "treat     ", "siren     ", "stair     ", "arise     ", "tires     ", "arson     ", "jacky     ", "brick     ", "chair     "
                    "tread     ", "trail     ", "pouch", "jumbucks     ", "juxtaposed"]
truly_random_word = random.choice(random_word_list)
first_letter = truly_random_word[0]
second_letter = truly_random_word[1]
third_letter = truly_random_word[2]
fourth_letter = truly_random_word[3]
fifth_letter = truly_random_word[4]
sixth_letter = truly_random_word[5]
seventh_letter = truly_random_word[6]
eighth_letter = truly_random_word[7]
ninth_letter = truly_random_word[8]
tenth_letter = truly_random_word[9]
# Random word generation
while guesses > 0 and not word_guessed == truly_random_word:
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

if word_guessed == truly_random_word:
    print("You win!")
else:
    print("You lose. Ha!")
