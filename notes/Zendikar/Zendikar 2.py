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
                "NORTH": "Mountain in Distance"
            }
        },
        "Mountain in Distance": {
            "NAME": "Mountain in Distance",
            "DESCRIPTION": "Mountain in Distance",
            "PATHS": {
                "SOUTH": "Sheltered Valley 3"
            }
        },
        "Sheltered Valley 7": {
            "NAME": "Sheltered Valley 7",
            "DESCRIPTION": "Strange Noise",
            "PATHS": {
                "SOUTH": "Sheltered Valley 8",
                "NORTH": "Sheltered Valley 1"
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
        "Great Desert": {
            "NAME": "Great Desert",
            "DESCRIPTION": "Desert",
            "PATHS": {
                "NORTH": "Sheltered Valley 8"
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
                "SOUTH": "Sheltered Valley 5"
            }
        },
        "Sheltered Valley 6": {
            "NAME": "Sheltered Valley 6",
            "DESCRIPTION": "Cabin, instant death",
            "PATHS": {
                "WEST": "Sheltered Valley 4"
            }
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
            "NAME": "Mountain 1",
            "DESCRIPTION": "You start climbing the west side of the mountain",
            "PATHS": {
                "SOUTH": "Spawn Point Mountain",
                "NORTH": "Mountain 2"
            }
        },
        "Mountain 2": {
            "NAME": "Mountain 2",
            "DESCRIPTION": "Out of breath",
            "PATHS": {
                "NORTH": "Mountain 5",
                "SOUTH": "Mountain 3"
            }
        },
        "Mountain 3": {
            "NAME": "Mountain 3",
            "DESCRIPTION": "Thirsty",
            "PATHS": {
                "NORTH": "Mountain 2",
                "SOUTH": "Mountain 4",
                "EAST": "Mountain 5"
            }
        },
        "Mountain 4": {
            "NAME": "Mountain 4",
            "DESCRIPTION": "Crab",
            "PATHS": {
                "NORTH": "Mountain 3"
            }
        },
        "Cave": {
            "NAME": "Cave",
            "DESCRIPTION": "Cave",
            "PATHS": {
                # None
            }
        },
        "Mountain 5": {
            "NAME": "Mountain 5",
            "DESCRIPTION": "Instant death from dehydration",
            "PATHS": {
                # None
            }
        },
        "Mountain 6": {
            "NAME": "Mountain 6",
            "DESCRIPTION": "Button",
            "PATHS": {
                "WEST": "Spawn Point Mountain"
            }
        },
        "Spawn Point Pit": {
            "NAME": "Spawn Point Pit",
            "DESCRIPTION": "Spawn Point Pit",
            "PATHS": {
                "EAST": "Pit 2",
                "WEST": "Pit 1"
            }
        },
        "Pit 1": {
            "NAME": "Pit 1",
            "DESCRIPTION": "Another pit",
            "PATHS": {
                # None
            }
        },
        "Pit 2": {
            "NAME": "Pit 2",
            "DESCRIPTION": "Kor grab you",
            "PATHS": {
                # None
            }
        }
    },
    "Desert Map": {
        "Spawn Point Desert": {
            "NAME": "Spawn Point Desert",
            "DESCRIPTION": "Spawn Point Desert",
            "PATHS": ""
        }
    },
    "Lake Map": {
        "Spawn Point Lake": {
            "NAME": "Spawn Point Lake",
            "DESCRIPTION": "Spawn Point Lake",
            "PATHS": ""
        }
    }
}

heads = 1


class Monster:
    def __init__(self, monster_health, monster_attack, monster_exp, monster_gold, did_you_beat_monster):
        self.monster_health = monster_health
        self.monster_attack = monster_attack
        self.monster_exp = monster_exp
        self.monster_gold = monster_gold
        self.did_you_beat_monster = did_you_beat_monster


eldrazi_scout = Monster(2, 1, 5, 5, False)
eldrazi_scion = Monster(3, 2, 5, 5, False)
crab = Monster(5, 3, 5, 5, False)
krayt_dragon = Monster(10, 5, 10, 10, False)
sidewinder_naga = Monster(5, 4, 10, 5, False)
hydra = Monster(20, 1 * heads, 15, 20, False)
fire_elemental = Monster(20, 5, 20, 20, False)
volcano_hellion = Monster(15, 10, 15, 10, False)


def combine_attack(damage1, damage_from_level1):
    return damage1 + damage_from_level1


def combine_health(health1, health_from_level1):
    return health1 + health_from_level1


directions = ["NORTH", "SOUTH", "EAST", "WEST", "", "Skip"]
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
level = 0
exp = 15
exp_to_level_up = 20
shop = "YES"
in_shop = True
key_items = []


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
        print("Or try moving by typing NORTH")
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
        did_you_beat_raven_gorge = True
        total_gold += 100
    if current_node["NAME"] == "Raven Gorge 1":
        print("You are in %s" % current_node["NAME"])
        print("You start walking forward and you see an eldrazi scout north of you")
    elif current_node["NAME"] == "Raven Gorge 2":
        print("You are in %s" % current_node["NAME"])
        print("You see the eldrazi scout in front of you")
        while eldrazi_scout.monster_health > 0 and health > 0 and not eldrazi_scout.did_you_beat_monster:
            print("The eldrazi scout attacked you")
            print("You took %i damage" % int(eldrazi_scout.monster_attack - defence))
            health = health - (eldrazi_scout.monster_attack - defence)
            print("Now you have %s health left" % health)
            print("What would you like to do")
            eldrazi_fight = input("ATTACK or FLEE")
            if eldrazi_fight == "ATTACK":
                print("You swing your %s at the eldrazi scout" % weapon)
                print("You did %s damage to the eldrazi scout" % damage)
                eldrazi_scout. monster_health -= damage
                print("The eldrazi scion has %s health left" % eldrazi_scout.monster_health)
            if eldrazi_fight == "FLEE":
                alive_raven_gorge = False
                playing = False
                print("You tried to flee but you tripped and the eldrazi killed you")
                print("You died")
                print("Try again")
                break
        if eldrazi_scout.monster_health <= 0:
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
            while eldrazi_scion.monster_health > 0 and combine_health(health, health_from_level) > 0 \
                    and not eldrazi_scion.did_you_beat_monster:
                print("The eldrazi attacked you")
                print("You took % i damage" % int(eldrazi_scion.monster_attack - defence))
                health -= int(eldrazi_scion.monster_attack - defence)
                print("Now you have %s health left" % combine_health(health, health_from_level))
                print("What would you like to attack with?")
                eldrazi_scion_fight1 = input("%s" % weapon)
                print("You swing your %s at the eldrazi" % weapon)
                print("The eldrazi takes %s damage" % damage)
                eldrazi_scion.monster_health -= damage
                print("The eldrazi has %s health left" % eldrazi_scion.monster_health)
            if eldrazi_scion.monster_health <= 0:
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
        print("You have %s gold" % total_gold)
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


if playing:
    print("You beat round 1, congrats")
    print("Here is 25 gold for doing that")
    total_gold += 25
    print("Now you have %s gold" % total_gold)

alive_sheltered_valley = True
did_you_beat_sheltered_valley = False
first_time = False
current_node = world_map["Sheltered Valley Map"]["Spawn Point Sheltered Valley"]
get_gold = False
did_you_get_to_the_desert = False
did_you_get_to_the_mountain = False
did_you_get_to_the_lake = False
shop3 = "YES"


while alive_sheltered_valley and playing and not did_you_beat_sheltered_valley:
    if not first_time:
        print("You are now in Sheltered Valley")
        first_time = True
    print("Poof a shop appears")
    print("Would you like to enter it")
    shop1 = input("YES or NO")
    while shop1 == "YES" and shop3 == "YES":
        print("You entered the shop")
        print("This is what is offered")
        print("Stone Sword: 15 Gold, Health Potion: 5 Gold")
        shop2 = input("STONE SWORD or HEALTH POTION")
        if shop2 == "STONE SWORD" and total_gold >= 15:
            print("You bought a stone sword")
            weapon = "Stone Sword"
            damage = 5
            total_gold -= 15
            print("Now you do %s damage" % combine_attack(damage, damage_from_level))
            print("You have %s gold left" % total_gold)
        if shop2 == "HEALTH POTION" and total_gold >= 5:
            print("You bought a health potion")
            health += 3
            total_gold -= 5
            print("Now you have %s health" % combine_health(health, health_from_level))
            print("You have %s gold left" % total_gold)
        print("Would you like to remain in the shop")
        shop3 = input("YES or NO")
    if shop1 == "NO":
        pass
    command = input(">")
    if command.lower() in ["q", "quit", "exit"]:
        playing = False
    elif command.lower() == "i":
        check_self()
    elif command in directions:
        try:
            room_name = current_node["PATHS"][command]
            current_node = world_map["Sheltered Valley Map"][room_name]
        except KeyError:
            print("You can't go that way")
    else:
        print("Command not recognized")
    if current_node["NAME"] == "Sheltered Valley 1":
        print("You are now in %s" % current_node["NAME"])
        print("You see a dead body in the distance \nWhat do you want to do?")
        dead_body = input("Walk NORTH towards it or walk SOUTH away from it")
        if dead_body == "NORTH":
            current_node = world_map["Sheltered Valley Map"]["Sheltered Valley 2"]
            if not get_gold:
                print("You start walking towards the dead body")
                print("Whoever it was dropped a lot of gold")
                print("You found 50 gold")
                total_gold += 50
                print("Now you have %s gold" % total_gold)
                get_gold = True
        if dead_body == "SOUTH":
            current_node = world_map["Sheltered Valley Map"]["Sheltered Valley 7"]
            print("You walk away from the dead body so whatever killed it hopefully won't kill you")
    if current_node["NAME"] == "Sheltered Valley 2":
        print("You are now in %s" % current_node["NAME"])
    if current_node["NAME"] == "Sheltered Valley 3":
        print("You are now in %s" % current_node["NAME"])
        print("You see a stream running beside you and it makes you thirsty")
        print("Do you want to drink the water")
        water = input("YES or NO")
        if water == "YES":
            print("You drink the water and within a few hours you collapse because of it")
            print("You died")
            print("Try again")
            playing = False
            alive_sheltered_valley = False
        if water == "NO":
            print("You don't take the water and that is probably a good thing")
    if current_node["NAME"] == "Mountain in Distance":
        print("You are now in %s" % current_node["NAME"])
        print("You continue walking and you see a mountain in the distance")
        did_you_get_to_the_mountain = True
        did_you_beat_sheltered_valley = True
        current_node = world_map["Mountain Map"]["Spawn Point Mountain"]
    if current_node["NAME"] == "Sheltered Valley 7":
        print("You are now in %s" % current_node["NAME"])
        print("It starts to darken and suddenly you hear a snap in the grass around you")
        print("Do you want to investigate or stay put")
        noise = input("INVESTIGATE or STAY PUT")
        if noise == "INVESTIGATE":
            print("You go to investigate the noise")
            print("Suddenly you look down and there are multiple swords sticking out of your chest")
            print("You died")
            print("Try again")
            playing = False
            alive_sheltered_valley = False
        if noise == "STAY PUT":
            print("You stayed where you are and nothing appears")
    if current_node["NAME"] == "Sheltered Valley 8":
        print("You are now in %s" % current_node["NAME"])
        print("It is starting to get very dark")
        print("Do you want to make a fire")
        fire = input("YES or NO")
        if fire == "YES":
            print("You make a fire and the heat slowly lulls you to sleep")
            print("When you wake up nothing has changed")
        if fire == "NO":
            print("When darkness strikes so do they")
            print("You feel a small prick in your neck and as the world fades you see a strange humanoid "
                  "standing over you")
    if current_node["NAME"] == "Great Desert":
        print("You are now in %s" % current_node["NAME"])
        print("All in front of you is a vast desert")
        print("You see a sign and it says")
        print("You are in the Great Desert \nYou are going to die")
        did_you_get_to_the_desert = True
        did_you_beat_sheltered_valley = True
        current_node = world_map["Desert Map"]["Spawn Point Desert"]
    if current_node["NAME"] == "Sheltered Valley 4":
        print("You are now in %s" % current_node["NAME"])
        print("There is a wall of trees in front of you with little room to pass into it")
        print("Do you want to go into it or try to go around it")
        tree = input("Go NORTH through it or EAST around it")
        if tree == "NORTH":
            current_node = world_map["Sheltered Valley Map"]["Sheltered Valley 5"]
            print("You enter the mass of trees")
        if tree == "EAST":
            print("You start going along the tree line")
            current_node = world_map["Sheltered Valley Map"]["Sheltered Valley 6"]
    if current_node["NAME"] == "Sheltered Valley 5":
        print("You are now in %s" % current_node["NAME"])
        print("You start to get very tired")
        print("What would you like to do")
        trees = input("Lie down among the trees and SLEEP or keep GOING")
        if trees == "SLEEP":
            print("You lie down on a tree and while you are asleep the tree slowly envelops you")
            print("You died")
            print("Try again")
            playing = False
            alive_sheltered_valley = False
        if trees == "GOING":
            print("You keep on going")
    if current_node["NAME"] == "Lake":
        print("You are now in %s" % current_node["NAME"])
        did_you_get_to_the_lake = True
    if current_node["NAME"] == "Sheltered Valley 6":
        print("You are now in %s" % current_node["NAME"])
        print("You see a cabin and you enter it")
        print("When you enter it there is an eldrazi who kills you")
        print("You died")
        print("Try again")
        playing = False
        alive_sheltered_valley = False

alive_desert = True
alive_lake = True
alive_mountain = True

while playing and alive_desert and did_you_get_to_the_desert:
    print("You are now in the Great Desert")
    break

while playing and alive_mountain and did_you_get_to_the_mountain:
    print("You are at the base of the mountain")
    break

while playing and alive_lake and did_you_get_to_the_lake:
    print("You got to the lake")
    break
