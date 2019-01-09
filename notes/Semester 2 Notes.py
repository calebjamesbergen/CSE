print("Hello world!")
# This is a single line comment

cars = 5
driving = True

print("I have %d cars" % cars)
print("I have " + str(cars) + " cars.")
# Concatenate means to combine some stuff in code and it always refers to strings
# Using numbers will not work for this so you must use str()

age = int(input("How old are you?"))
if age < 120:
    print("%s?? Really???" % age)
if age > 120:
    print("If you were %s years old then you would be dead" % age)
    print("Stop lying")
    print("Lying is bad so don't do it")

colors = ["red ", "orange ", "yellow ", "green ", "blue ", "purple "]
print("".join(colors))
colors.append("brown ")
print("".join(colors))
colors.pop(0)
print("".join(colors))
print(colors[1])
print(len(colors))
