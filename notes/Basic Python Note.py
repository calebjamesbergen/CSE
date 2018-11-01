import random    # This should be on line 1 always
"""
# Link to where all of the notes are github.com/EdisonHS/

print("Hello World!")

# Apparently I'm going too slow, so I will speed up
# This is a comment
# This has no effect on the code
# This is used for a variety of things, such as
# 1. Making personal notes about my code
# 2. Commenting out code that does not work

print("Notice what is happening here.")
print()  # This creates a new line
print()  # Do you notice the underline here?
# Hover over top it to see what is wrong
# Pep 8 = This is a style guide to help fix my code
# -5 points for each Pep 8 error and max of 20 points

# Math
print(5 + 3)
print(5 - 3)
print(4 * 5)
print(6 / 5)

# Semi-Advanced Math
print("Figure this out...")
print(6 // 4)
print(12 // 3)
print(9 // 4)
print()
# This always gives an integer with no decimal place (it does not round)

print("Figure this out too...")
print(6 % 4)
print(5 % 3)
print(9 % 4)
# Subtracts the second number from the first unlimited times until just before it goes negative
# Like a clock (military time) 15-12 = 3 o clock

# 150 // 60 = 2 hours
# 150 % 60 = 30 minutes
# 150 minutes equals 2 hours and 30 minutes

# Defining Variables
car_name = "Wiebe Mobile"  # String
car_type = "Tesla"  # String
car_cylinders = 16  # Integer
car_miles_per_gallon = 0.01  # Float

print("I have a car called %s. It's pretty nice." % car_name)  # The s represents string
print("It has %d cylinders, but gets %f mpg" % (car_cylinders, car_miles_per_gallon))
# The d represents digit
# The f represents float
# Most likely b for Boolean
# The variables get put in in the order that you put them (look above)

# Taking Input
print()
name = input("What is your name? ")
print("Hello %s" % name)

age = input("How old are you?")
print("%s? You belong in a museum!" % age)

# Recasting
real_age = int(input("How old are you again? "))
hidden_age = real_age + 5
print(hidden_age)
# This will be used for the project after Mad Libs

# Random Number
#  import random
#  for x in range(1):
# x = random.randint(1, 5)
"""

# Multi-line Comments
# Hit quotation 3 times and press enter

"""
This is a multi-line comment
anything in between them is automatically commented out.
"""

# You have to have 2 blanks lines before and after the def function
# Defining Functions


def say_it():
    print("Hello World!")


say_it()
say_it()
say_it()


# f(x) = 2x + 3
# f = the name
# in the parentheses is the parameter
def f(x):
    print(2*x + 3)


f(1)
f(5)


# ** = raised to the power of
def distance(x1, y1, x2, y2):
    dist = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    print(dist)


distance(0, 0, 3, 4)
distance(0, 0, 5, 12)

# For loops
# In this case "i" is a variable
for i in (1, 2, 3):
    say_it()

for i in range(5):    # Range(5) gives the numbers 0-4
    f(i)

for i in range(5):
    print(i ** 2)
# Don't do too many for loops in a for loop

# While Loop
a = 0
while a < 10:
    print(a)
    a += 1  # This is the same as a = a + 1


"""
Hints for loops:
For loops - Use when you know EXACTLY how many iterations
While loops - Use when you DON'T know how many iterations
"""

# Control Statement (If statements)
sunny = False
if sunny:
    print("Go outside")


def grade_calc(percentage):
    if percentage >= 90:  # >= Equivalent of greater then or equal to
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


your_grade = grade_calc(82)
print(your_grade)

# Random numbers
print(random.randint(0, 100))

# Equality Statements
print(5 > 3)
print(5 >= 3)
print(3 == 3)
print(3 != 4)  # Is not equal to
"""
a = 3 # A is set to 3
a == 3 # Is a equal to 3?
"""
