# Making a list
fruit = [
    'apples',
    'oranges',
    'blackberries',
    'strawberries',
    'blueberries',
    'raspberries',
    'pineapple',
    'mango',
    'coconut'
]    # USE SQUARE BRACKETS!!!!!!!!!!!!!!!!!!!
print(fruit)

# Printing lists without all the stuff
print(fruit[1])  # The number is the index of the list
# The index starts at 0
print(*fruit, sep=' ',)  # How to print a list

# Lengths of a list
print(len(fruit))  # len = length
print("The length of the list is %d" % len(fruit))

# Modifying Lists
fruit[8] = 'banana'
print(*fruit, sep=' ',)

# Looping through Lists
for item in fruit:  # Item just defines it as a variable, it can be named anything
    print(item)


stuff = [
    'stuff',
    'stuff',
    'stuff',
    'stuff',
    'stuff',
]
stuff[2] = 'not stuff'
print(stuff[2])
print(*stuff, sep=' ',)
print("The last thing in the list is %s" % stuff[len(stuff)-1])  # Prints the last item in the list
