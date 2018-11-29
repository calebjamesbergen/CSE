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


food = [
    'pizza', 'chicken', 'ham', 'turkey', 'cheese', 'poutine', 'chips', 'salmon',
    'hamburger', 'french fries', 'tacos', 'pie', 'cake', 'candy', 'cookie',
    'chile', 'soup', 'zwiebach', 'lasagna', 'burrito',
]
print(*food, sep=' ')  # Must have an astrix in the beginning!!!!!!!! DO NOT IGNORE!!!

# Slicing
print(*food[2:5], sep=' ')  # Starts at beginning and through the rest of the numbers except the one listed
print(food[3:4])  # Only 1 thing
print(food[10:])  # Start at index 10 and go to the end
print(food[:5])  # Starts at 0 and goes up to but not to 5

# Adding stuff to a list (part 1)
food.append("orange")
food.append("bacon")
print(food)
# Everything is in the form Object.method(parameters)

# Adding to a list (not at the end)
food.insert(2, "ramen")  # Puts it in there but replaces nothing
print(food)

# Removing from a list
food.remove("ham")
food.remove("turkey")
print(food)
# This removes the specific item from the list

# Removing from a list (pt 2)
# Sometimes, you don't know what is in the list, but you know
# You want to get rid of something at a specific index
food.pop(0)
print(food)
# Notice that "pizza" is no longer in the list because it is at index 0

# Practice time...
stuff2 = ["Hi", "there", "human"]
print(*stuff2, sep=" ",)
stuff2.append("soul")
print(*stuff2, sep=" ",)
stuff2.pop(0)
print(*stuff2, sep=" ",)

# Finding things in a list
print(food.index("zwiebach"))  # This will print the index of that item

# Things I notice people do:
# Some people have made lists with parentheses instead of brackets
brands = ("apple", "samsung", "HTC")
# This is a TUPLE, not a list. Tuples are immutable (cannot be changed)

# Changing things into a list
string1 = "turquoise"
list1 = list(string1)
print(*list1, sep=" ")

# Hangman hints
for i in range(len(list1)):  # i goes through all indices
    if list1[i] == "u":  # If we find a "u
        list1.pop(i)  # Remove the i-th index
        list1.insert(i, "*")  # Put a * there instead

# Changing back into a string (list→string)
print("".join(list1))
