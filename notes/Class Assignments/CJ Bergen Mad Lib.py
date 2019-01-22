day_of_the_week = input("Day of the week: ")
noun1 = input("Noun: ")
number1 = input("Number: ")
noun2 = input("Noun: ")
noun3 = input("Noun: ")
name_of_person = input("Person: ")
adjective1 = input("Adjective: ")
name_of_person2 = input("Person: ")
noun4 = input("Noun: ")
object1 = input("Object: ")

# I love (day of the week). It is the one day of the week where I don’t have to go to (noun).
# I love waking up at (number) in the morning and not having to immediately leave for (noun).
# Also, I love playing (noun) at 3 in the morning and waking up my (name of a person).
# My dad always tells me that I am too (adjective) but I don’t care, I am who (person) is/am
# Then he comes into my (noun) and throws a/an (object) at my head.
# That is when I have to turn it off.

print("I love %s" % day_of_the_week)
print("It is the one day of the week where I don't have to go to %s" % noun1)
print("I love waking up at %s in the morning and not having to immediately leave for %s" % (number1, noun2))
print("Also, I love playing %s at 3 in the morning and waking up my %s" % (noun3, name_of_person))
print("My dad always tells me that I am too %s but I don't care, I am who %s is" % (adjective1, name_of_person2))
print("Then he comes into my %s and throws a/an %s at my head" % (noun4, object1))
print("That is when I have to turn it off")
