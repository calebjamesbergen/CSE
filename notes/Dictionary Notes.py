# Dictionary are a file type used for many different things
states = {
    "CA": "California",
    "NJ": "New Jersey",
    "WI": "Wisconsin",
    "NY": "New York"
}

print(states["CA"])
print(states["WI"])

nested_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000
    },
    "NJ": {
        "NAME": "New Jersey",
        "POPULATION": 9000000
    },
    "WI": {
        "NAME": "Wisconsin",
        "POPULATION": 5800000
    },
    "NY": {
        "NAME": "New York",
        "POPULATION": 19500000
    }
}

# How to print a dictionary in a dictionary
print(nested_dictionary["CA"])
# How to print a specific part of a nested dictionary
print(nested_dictionary["CA"]["POPULATION"])
print(nested_dictionary["NY"]["NAME"])

complex_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000,
        "CITIES": [
            "Fresno",
            "San Francisco,"
            "Los Angeles"
        ]
    },
    "NJ": {
        "NAME": "New Jersey",
        "POPULATION": 9000000,
        "CITIES": [
            "Newark",
            "Trenton",
            "Princeton"
        ]
    },
    "WI": {
        "NAME": "Wisconsin",
        "POPULATION": 5800000,
        "CITIES": [
            "Madison",
            "Milwaukee",
            "Green Bay"
        ]
    },
    "NY": {
        "NAME": "New York",
        "POPULATION": 19500000,
        "CITIES": [
            "New York City",
            "Rockester",
            "Buffalo"
        ]
    }
}
