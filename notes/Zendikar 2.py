raven_gorge_map = {
    "Spawn Point Sheltered Valley": {
        "NAME": "Spawn Point Sheltered Valley",
        "DESCRIPTION": "Test room",
        "PATHS": {
            "NORTH": "Raven Gorge 1"
        }
    },
    "Raven Gorge 1": {
        "NAME": "Raven Gorge 1",
        "DESCRIPTION": "Nothing",
        "PATHS": {
            "SOUTH": "Spawn Point",
            "NORTH": "Raven Gorge 2"
        }
    },
    "Raven Gorge 2": {
        "NAME": "Raven Gorge 2",
        "DESCRIPTION": "Eldrazi Scout",
        "PATHS": {
            "SOUTH": "Raven Gorge 1",
            "NORTH": "Raven Gorge 3",
            "WEST": "Raven Gorge 2 Left"
        }
    },
    "Raven Gorge 2 Left": {
      "NAME": "Raven Gorge 2 Left",
      "DESCRIPTION": "25 Gold",
      "PATHS": {
            "EAST": "Raven Gorge 2"
        }
    },
    "Raven Gorge 3": {
        "NAME": "Raven Gorge 3",
        "DESCRIPTION": "Eldrazi Scion",
        "PATHS": {
            "EAST": "Raven Gorge 3 Right",
            "NORTH": "Raven Gorge 4",
            "SOUTH": "Raven Gorge 2"
        }
    },
    "Raven Gorge 3 Right": {
        "NAME": "Raven Gorge 3 Right",
        "DESCRIPTION": "Eldrazi Devastator",
        "PATHS": {
            "WEST": "Raven Gorge 3"
        }
    },
    "Raven Gorge 4": {
        "NAME": "Raven Gorge 4",
        "DESCRIPTION": "Shop",
        "PATHS": {
            "Spawn Point Sheltered Valley"
        }
    }
}

sheltered_valley_map = {
    "Spawn Point Sheltered Valley": {
        "NAME": "Spawn Point Sheltered Valley",
        "DESCRIPTION": "Spawn Point",
        "PATHS": {
            "WEST": "Sheltered Valley 1",
            "EAST": "Sheltered Valley 4"
        }
    },
    "Sheltered Valley 1": {
        "NAME": "Sheltered Valley 1",
        "DESCRIPTION": "Spawn Point",
        "PATHS": {
            "SOUTH": "Sheltered Valley 7",
            "NORTH": "Sheltered Valley 2"
        }
    },
    "Sheltered Valley 2": {
        "NAME": "Sheltered Valley 2",
        "DESCRIPTION": "Dead body with 50 gold",
        "PATHS": {
            "SOUTH": "Sheltered Valley 1",
            "NORTH": "Sheltered Valley 3"
        }
    },
    "Sheltered Valley 3": {
        "NAME": "Sheltered Valley 3",
        "DESCRIPTION": "Stream",
        "PATHS": {
            "SOUTH": "Sheltered Valley 2",
            "NORTH": "Mountain"
        }
    },
    "Mountain": {
        "NAME": "Mountain",
        "DESCRIPTION": "Mountain",
        "PATHS": {
            "": "Spawn Point Mountain"
        }
    },
    "Sheltered Valley 7": {
        "NAME": "Sheltered Valley 7",
        "DESCRIPTION": "Strange Noise",
        "PATHS": {
            "SOUTH": "Sheltered Valley 8"
        }
    },
    "Sheltered Valley 8": {
        "NAME": "Sheltered Valley 8",
        "DESCRIPTION": "Making a fire",
        "PATHS": {
            "SOUTH": "Great Desert",
            "NORTH": "Sheltered Valley 7"
        }
    },
    "Desert": {
        "NAME": "Desert",
        "DESCRIPTION": "Desert",
        "PATHS": {
            "": "Spawn Point Desert"
        }
    },
    "Sheltered Valley 4": {
        "NAME": "Sheltered Valley 4",
        "DESCRIPTION": "Mass of trees",
        "PATHS": {
            "NORTH": "Sheltered Valley 5",
            "EAST": "Sheltered Valley 6"
        }
    },
    "Sheltered Valley 5": {
        "NAME": "Sheltered Valley 5",
        "DESCRIPTION": "Heavy canopy",
        "PATHS": {
            "NORTH": "Lake",
            "SOUTH": "Sheltered Valley 4"
        }
    },
    "Lake": {
        "NAME": "Lake",
        "DESCRIPTION": "Lake",
        "PATHS": {
            "": "Spawn Point Lake"
        }
    },
    "Sheltered Valley 6": {
        "NAME": "Sheltered Valley 6",
        "DESCRIPTION": "Cabin, instant death",
        "PATHS": {}
        # None
    }
}


directions = ["NORTH", "SOUTH", "EAST", "WEST", ""]
alive_raven_gorge = True
current_node = raven_gorge_map["Spawn Point Sheltered Valley"]
playing = True
read_starting_text = False
did_you_beat_raven_gorge = False
weapon = "Stick"
damage = 1
armor = "Leather armor"
defence = 1
total_gold = 0
total_health = 5
eldrazi_scout_attack = 1
eldrazi_scout_health = 2
eldrazi_scion_attack = 2
eldrazi_scion_health = 3

while alive_raven_gorge and playing and not did_you_beat_raven_gorge:
    if not read_starting_text:
        print("Welcome to Zendikar")
        print("This is a game of skill and quite a bit of luck")
        read_starting_text = True
        print("You are in %s" % current_node["NAME"])
    command = input(">")
    if command.lower() in ["q", "quit", "exit"]:
        playing = False
    elif command in directions:
        try:
            room_name = current_node["PATHS"][command]
            current_node = raven_gorge_map[room_name]
        except KeyError:
            print("I can't go that way")
    else:
        print("Command not recognized")
    if current_node["NAME"] == "Raven Gorge 4":
        current_node = sheltered_valley_map["Spawn Point Sheltered Valley"]
        did_you_beat_raven_gorge = True
    if current_node["NAME"] == "Raven Gorge 1":
        print("You are in %s" % current_node["NAME"])
        print("You start walking forward and you see an eldrazi scout north of you")
    elif current_node["NAME"] == "Raven Gorge 2":
        print("You are in %s" % current_node["NAME"])
        print("You see the eldrazi scout in front of you")
        while eldrazi_scout_health > 0:
            print("The eldrazi scout attacked you")
            print("You took %i damage" % int(eldrazi_scout_attack - defence))
            total_health = total_health - (eldrazi_scout_attack - defence)
            print("Now you have %s health left" % total_health)
            print("What would you like to do")
            eldrazi_fight = input("ATTACK or FLEE")
            if eldrazi_fight == "ATTACK":
                print("You swing your %s at the eldrazi scout" % weapon)
                print("You did %s damage to the eldrazi scout" % damage)
                eldrazi_scout_health -= damage
                print("The eldrazi scion has %s health left" % eldrazi_scout_health)
        if eldrazi_scout_health <= 0:
            print("You slayed the eldrazi")
            print("You got 5 gold")
            total_gold += 5
            print("Now you have %s gold" % total_gold)
    elif current_node["NAME"] == "Raven Gorge 2 Left":
        print("You are in %s" % current_node["NAME"])
        print("You found 25 gold")
        total_gold += 25
        print("Now you have %s gold" % total_gold)
    elif current_node["NAME"] == "Raven Gorge 3":
        print("You are in %s" % current_node["NAME"])
        print()
    elif current_node["NAME"] == "Raven Gorge 3 Right":
        print("You are in %s" % current_node["NAME"])
        print("You disturbed an eldrazi devastator")
        print("It turns around and rips you in half with only 2 of its 4 arms")
        print("You died")
        print("Try again")
        alive_raven_gorge = False
        playing = False

alive_sheltered_valley = True
did_you_beat_sheltered_valley = False

while alive_sheltered_valley and playing and not did_you_beat_sheltered_valley:
    print("You are now in Sheltered Valley")
