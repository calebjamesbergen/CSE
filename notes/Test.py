import random
random_number = random.randint(1, 4)
print("*" * random_number)
word = ["*" * random_number]
word2 = list(word)
print(word2)
word2[1] = "?"
