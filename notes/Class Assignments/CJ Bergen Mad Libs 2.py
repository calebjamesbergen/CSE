words_list = [
    input("Day of the week:"),
    input("Noun:"),
    input("Number:"),
    input("Noun:"),
    input("Noun:"),
    input("Person:"),
    input("Adjective:"),
    input("Person:"),
    input("Noun:"),
    input("Object:"),
]
# I love (day of the week). It is the one day of the week where I don’t have to go to (noun).
# I love waking up at (number) in the morning and not having to immediately leave for (noun).
# Also, I love playing (noun) at 3 in the morning and waking up my (name of a person).
# My dad always tells me that I am too (adjective) but I don’t care, I am who (person) is/am
# Then he comes into my (noun) and throws a/an (object) at my head.
# That is when I have to turn it off.

print("I love %s" % words_list[0])
print("It is the one day of the week where I don't have to go to %s" % words_list[1])
print("I love waking up at %s in the morning and not having to immediately leave for %s" %
      (words_list[2], words_list[3]))
print("Also, I love playing %s at 3 in the morning and waking up my %s" % (words_list[4], words_list[5]))
print("My dad always tells me that I am too %s but I don't care, I am who %s is" % (words_list[6], words_list[7]))
print("Then he comes into my %s and throws a/an %s at my head" % (words_list[8], words_list[9]))
print("That is when I have to turn it off")
