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
