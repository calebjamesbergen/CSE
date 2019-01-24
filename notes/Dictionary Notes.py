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

nested_dictionary = {
    "KEY": "Value",
    "key1": {
        "key1": 12,
        "key2": True
    },

}

world_map = {
    "room1": {
        "NAME": "Starting room",
        "DESCRIPTION": "Thsdhflaskhdf",
        "PATHS": {
            "NORTH": "room2"
        }
    },
    "room2": {
        "NAME": "next room",
        "DESCRIPTION": "dhaslkdhga",
        "PATHS": {
            "SOUTH": "room1"
        }
    }
}


def moving():
    moving.move = input("Where do you want to go")


hi = 2
bye = 1
print(hi - bye)
moving()
print(moving.move)
if moving.move == "1":
    print("Hi")
