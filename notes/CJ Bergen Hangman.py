import random
guesses = 8
letter_guessed1 = ""
letter_guessed2 = ""
letter_guessed3 = ""
letter_guessed4 = ""
letter_guessed5 = ""
word_guessed = ""
WORDS = ("chair", "brick", "jerky")
random_word = random.choice(WORDS)
word = random_word
random_word_list = ["seats ", "roast ", "tenor ", "tense ", "loser ", "train ", "tread ", "trail ", "total "]
random_word_list.append("tears")
random_word_list.append("jerky")
random_word_list.append("treat")
random_word_list.append("siren")
random_word_list.append("stair")
random_word_list.append("arise")
random_word_list.append("tires")
random_word_list.append("arson")
random_word_list.append("jacky")
random_word_list.append("brick")
random_word_list.append("chair")
number = random.randint(0, 19)
truly_random_word = random_word_list[number]
first_letter = truly_random_word[0]
second_letter = truly_random_word[1]
third_letter = truly_random_word[2]
fourth_letter = truly_random_word[3]
fifth_letter = truly_random_word[4]
# Random word generation
while guesses > 0 and not word_guessed == random_word:
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

if guesses > 0:
    print("You win!")
if guesses == 0:
    print("You lose. Ha!")
