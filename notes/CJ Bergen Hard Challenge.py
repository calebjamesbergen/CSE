import datetime  # Will show time
import math


# 9th Challenge
def letter_test(letter):
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        return "The letter is a vowel"
    else:
        return "The letter is a consonant"


print(letter_test("c"))


# 10th Challenge
def is_it_a_number(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


print(is_it_a_number(2))
print(is_it_a_number("a"))


# 11th Challenge
def the_time():
    return datetime.datetime.now()


print(the_time())


# 12th Challenge
def compare_numbers(number1, number2):
        return math.gcd(number1, number2)  # Greatest common denominator


print(compare_numbers(4, 8))
print(compare_numbers(3, 9))
