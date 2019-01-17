# Creating a dictionary
released = {
    "Are you alive": True,
    "Did you die": False,
    "iphone 3GS": False,
    "iphone 4": False,
    "iphone 4S": False,
    "iphone 5": False
}
# Adding new values
released["iphone 5S"] = 2013

# Deleting stuff
del released["Are you alive"]

# Length of a dictionary
print(len(released))

# Checking if stuff is in your list
for item in released:
    if "iphone 5" in released:
        print("Key found")
        break
    else:
        print("No keys found")

# Getting a value of a specific thing
print(released.get("iphone 3G", "none"))

print("-" * 10)
print("iphone releases so far: ")
print("-" * 10)
for release in released:
    print(release)

# Get only the keys from a dictionary
print("This dictionary contains these keys: ", " ".join(released))
