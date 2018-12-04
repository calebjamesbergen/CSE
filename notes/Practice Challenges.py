import random
import math


# Finding what is divisible by 7 and not divisible by 5 from 2000 to 3200
for i in range(2000, 3200):
    if i % 7 == 0 and not i % 5 == 0:
        print(i)


# Finding the factorial of a number
def find_the_factorial(number):
    return math.factorial(number)


print(find_the_factorial(8))

print(random.sample(range(100), 5))
