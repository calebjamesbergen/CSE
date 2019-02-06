world_map = {
    "Raven Gorge Map": {
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
                "SOUTH": "Spawn Point Sheltered Valley",
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
                "SOUTH": "Raven Gorge 3"
            }
        }
    },

    "Sheltered Valley Map": {
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
    },
    "Mountain Map": {
        "Spawn Point Mountain": {
            "NAME": "Spawn Point Mountain",
            "DESCRIPTION": "Spawn Point Mountain",
            "PATHS": {
                "WEST": "Mountain 1",
                "EAST": "Mountain 6"
            }
        },
        "Mountain 1": {
            "NAME": "",
            "DESCRIPTION": "",
            "PATHS": {
                "SOUTH": "Spawn Point Mountain",
                "NORTH": "Mountain 2"
            }
        },
        "Mountain 2": {
            "NAME": "",
            "DESCRIPTION": "",
            "PATHS": {
                "NORTH": "Mountain 5",
                "SOUTH": "Mountain 3"
            }
        },
        "Mountain 3": {
            "NAME": "",
            "DESCRIPTION": "",
            "PATHS": {
                "NORTH": "Mountain 2",
                "SOUTH": "Mountain 4",
                "EAST": "Mountain 5"
            }
        },
        "Mountain 4": {
            "NAME": "",
            "DESCRIPTION": "",
            "PATHS": {
                "NORTH": "Mountain 3"
            }
        },
        "Cave": {
            "NAME": "",
            "DESCRIPTION": "",
            "PATHS": {
                # None
            }
        },
        "Mountain 5": {
            "NAME": "",
            "DESCRIPTION": "",
            "PATHS": {
                # None
            }
        },
        "Mountain 6": {
            "NAME": "",
            "DESCRIPTION": "",
            "PATHS": {

            }
        },
        "Spawn Point Pit": {
            "NAME": "",
            "DESCRIPTION": "",
            "PATHS": {

            }
        },
        "Pit 1": {
            "NAME": "",
            "DESCRIPTION": "",
            "PATHS": {

            }
        },
        "Pit 2": {
            "NAME": "",
            "DESCRIPTION": "",
            "PATHS": {

            }
        }
    },
}


def combine_attack(damage1, damage_from_level1):
    return damage1 + damage_from_level1


def combine_health(health1, health_from_level1):
    return health1 + health_from_level1


directions = ["NORTH", "SOUTH", "EAST", "WEST", "", "N", "S", "E", "W", "Skip"]
alive_raven_gorge = True
current_node = world_map["Raven Gorge Map"]["Spawn Point Sheltered Valley"]
playing = True
read_starting_text = False
did_you_beat_raven_gorge = False
weapon = "Stick"
damage = 1
damage_from_level = 0
armor = "Leather armor"
defence = 1
total_gold = 0
health = 5
health_from_level = 0
health_potions_owned = 0
level = 0
exp = 15
exp_to_level_up = 20
eldrazi_scout_attack = 1
eldrazi_scout_health = 2
eldrazi_scion_attack = 2
eldrazi_scion_health = 3
shop = "YES"
did_you_beat_the_eldrazi_scout = False
did_you_beat_the_eldrazi_scion = False
in_shop = True


def check_self():
    print("You have this weapon: %s" % weapon)
    print("You deal %s damage" % damage)
    print("You have this armor: %s" % armor)
    print("You have %s defence" % defence)
    print("You have %s health" % health)
    print("You have %s gold" % total_gold)
    print("You are level %s" % level)
    print("You are %s exp away from leveling up" % (exp_to_level_up - exp))
    print("Your best weapon is a/an %s" % weapon)


while alive_raven_gorge and playing and not did_you_beat_raven_gorge:
    if not read_starting_text:
        print("Welcome to Zendikar")
        print("This is a game of skill and quite a bit of luck")
        print("Try checking your stats and inventory by typing i")
        read_starting_text = True
        print("You are in %s" % current_node["NAME"])
    command = input(">")
    if command.lower() in ["q", "quit", "exit"]:
        playing = False
    elif command.lower() == "i":
        check_self()
    elif command in directions:
        try:
            room_name = current_node["PATHS"][command]
            current_node = world_map["Raven Gorge Map"][room_name]
        except KeyError:
            print("You can't go that way")
    else:
        print("Command not recognized")
    if command == "Skip":
        current_node = world_map["Raven Gorge Map"]["Raven Gorge 4"]
        total_gold += 100
    if current_node["NAME"] == "Raven Gorge 1":
        print("You are in %s" % current_node["NAME"])
        print("You start walking forward and you see an eldrazi scout north of you")
    elif current_node["NAME"] == "Raven Gorge 2":
        print("You are in %s" % current_node["NAME"])
        print("You see the eldrazi scout in front of you")
        while eldrazi_scout_health > 0 and health > 0 and not did_you_beat_the_eldrazi_scout:
            print("The eldrazi scout attacked you")
            print("You took %i damage" % int(eldrazi_scout_attack - defence))
            health = health - (eldrazi_scout_attack - defence)
            print("Now you have %s health left" % health)
            print("What would you like to do")
            eldrazi_fight = input("ATTACK or FLEE")
            if eldrazi_fight == "ATTACK":
                print("You swing your %s at the eldrazi scout" % weapon)
                print("You did %s damage to the eldrazi scout" % damage)
                eldrazi_scout_health -= damage
                print("The eldrazi scion has %s health left" % eldrazi_scout_health)
            if eldrazi_fight == "FLEE":
                alive_raven_gorge = False
                playing = False
                print("You tried to flee but you tripped and the eldrazi killed you")
                print("You died")
                print("Try again")
                break
        if eldrazi_scout_health <= 0:
            print("You slayed the eldrazi")
            print("You got 5 gold")
            total_gold += 5
            print("Now you have %s gold" % total_gold)
            exp += 5
            print("You got 5 exp")
            if exp >= exp_to_level_up:
                exp -= 20
                level += 1
                damage_from_level += 1
                health_from_level += 1
                print("You leveled up")
                print("Your damage and health increased by 1")
        did_you_beat_the_eldrazi_scout = True
    elif current_node["NAME"] == "Raven Gorge 2 Left":
        print("You are in %s" % current_node["NAME"])
        print("You found 25 gold")
        total_gold += 25
        print("Now you have %s gold" % total_gold)
    elif current_node["NAME"] == "Raven Gorge 3":
        print("You are in %s" % current_node["NAME"])
        print("An eldrazi scion appears")
        print("What would you like to do")
        eldrazi_scion_fight = input("ATTACK or FLEE")
        if eldrazi_scion_fight == "ATTACK":
            while eldrazi_scion_health > 0 and combine_health(health, health_from_level) > 0 \
                    and not did_you_beat_the_eldrazi_scion:
                print("The eldrazi attacked you")
                print("You took % i damage" % int(eldrazi_scion_attack - defence))
                health -= int(eldrazi_scion_attack - defence)
                print("Now you have %s health left" % combine_health(health, health_from_level))
                print("What would you like to attack with?")
                eldrazi_scion_fight1 = input("%s" % weapon)
                print("You swing your %s at the eldrazi" % weapon)
                print("The eldrazi takes %s damage" % damage)
                eldrazi_scion_health -= damage
                print("The eldrazi has %s health left" % eldrazi_scion_health)
            if eldrazi_scion_health <= 0:
                print("You defeated the eldrazi")
                total_gold += 5
                print("Now you have %s gold" % total_gold)
                exp += 5
                if exp >= exp_to_level_up:
                    exp -= 20
                    level += 1
                    damage_from_level += 1
                    health_from_level += 1
                    print("You leveled up")
                    print("Your damage and health increased by 1")
                    did_you_beat_the_eldrazi_scion = True
        if eldrazi_scion_fight == "FLEE":
            print("You tripped and the eldrazi killed you")
            print("You died")
            print("Try again")
            alive_raven_gorge = False
            playing = False
    elif current_node["NAME"] == "Raven Gorge 3 Right":
        print("You are in %s" % current_node["NAME"])
        print("You disturbed an eldrazi devastator")
        print("It turns around and rips you in half with only 2 of its 4 arms")
        print("You died")
        print("Try again")
        alive_raven_gorge = False
        playing = False
    elif current_node["NAME"] == "Raven Gorge 4":
        print("You have reached the end of this area")
        print("Poof a shop appears")
        print("Would you like to enter the shop")
        choice = input("YES or NO")
        if choice == "YES":
            print("This is what is offered")
            print("Wood Sword: 5 Gold, Copper Armor: 5 Gold, Health Potion: 5 Gold")
            print("What would you like to buy")
            while total_gold > 0 and shop == "YES" and in_shop:
                raven_gorge_shop = input("WOOD SWORD or COPPER ARMOR or HEALTH POTION")
                if raven_gorge_shop == "WOOD SWORD" and total_gold >= 5:
                    total_gold -= 5
                    weapon = "WOOD SWORD"
                    damage = 3
                    print("You bought the Wood Sword")
                    print("Now you deal %s damage" % combine_attack(damage, damage_from_level))
                    print("Now you have %s gold" % total_gold)
                if raven_gorge_shop == "COPPER ARMOR" and total_gold >= 5:
                    total_gold -= 5
                    armor = "COPPER ARMOR"
                    defence = 3
                    print("You bought the Copper Armor")
                    print("Now you have %s defence" % defence)
                    print("Now you have %s gold" % total_gold)
                if raven_gorge_shop == "HEALTH POTION" and total_gold >= 5:
                    total_gold -= 5
                    health += 3
                    print("You bought the Health Potion")
                    print("Now you have %s health" % combine_health(health, health_from_level))
                    print("Now you have %s gold" % total_gold)
                print("Would you like to remain in the shop")
                shop = input("YES or NO")
                if shop == "NO":
                    current_node = world_map["Sheltered Valley Map"]["Spawn Point Sheltered Valley"]
                    did_you_beat_raven_gorge = True
        if choice == "NO":
            pass

alive_sheltered_valley = True
did_you_beat_sheltered_valley = False

while alive_sheltered_valley and playing and not did_you_beat_sheltered_valley:
    print("You are now in Sheltered Valley")
    break
