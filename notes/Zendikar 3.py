heads = 1


class Monster:
    def __init__(self, name, monster_health, monster_attack, monster_exp, monster_gold, did_you_beat_monster):
        self.name = name
        self.monster_health = monster_health
        self.monster_attack = monster_attack
        self.monster_exp = monster_exp
        self.monster_gold = monster_gold
        self.did_you_beat_monster = did_you_beat_monster


class Person(object):
    def __init__(self, assigned_room="Spawn Point Raven Gorge"):
        self.alive_raven_gorge = True
        self.directions = ["north", "south", "east", "west", "", "Skip"]
        self.current_node = assigned_room
        self.playing = True
        self.read_starting_text = False
        self.did_you_beat_raven_gorge = False
        self.weapon = "Stick"
        self.damage = 1
        self.damage_from_level = 1
        self.armor = "Leather armor"
        self.defence = 1
        self.total_gold = 0
        self.health = 5
        self.health_from_level = 1
        self.level = 1
        self.exp = 15
        self.exp_to_level_up = 20
        self.shop = "YES"
        self.in_shop = True
        self.key_items = []
        self.room_name = ""
        self.alive_sheltered_valley = True
        self.did_you_beat_sheltered_valley = False
        self.first_time = False
        self.get_gold = False
        self.did_you_get_to_the_desert = False
        self.did_you_get_to_the_mountain = False
        self.did_you_get_to_the_lake = False
        self.shop3 = "YES"
        self.total_health = self.health + self.health_from_level
        self.total_damage = self.damage + self.damage_from_level
        self.defence = 1

    def combine_health(self):
        self.total_health = self.health + self.health_from_level
        print("You have %s total health" % self.total_health)

    def combine_attack(self):
        self.total_damage = self.damage + self.damage_from_level
        print("You deal %s damage" % self.total_damage)

    def get_attack(self):
        return self.damage + self.damage_from_level

    def get_health(self):
        return self.health + self.health_from_level

    def damage_you_take(self, monster_attack):
        return monster_attack - self.defence

    def level_up(self):
        if self.exp >= self.exp_to_level_up:
            self.exp -= 20
            print("You leveled up")
            print("Your health and attack increased by one")
            self.damage_from_level += 1
            self.health_from_level += 1
            self.level += 1
            print("Now you are level %s" % self.level)

    def check_self(self):
        print("You have this weapon: %s" % self.weapon)
        print("You deal %s damage" % self.damage)
        print("You have this armor: %s" % self.armor)
        print("You have %s defence" % self.defence)
        print("You have %s health" % self.health)
        print("You have %s gold" % self.total_gold)
        print("You are level %s" % self.level)
        print("You are %s exp away from leveling up" % (self.exp_to_level_up - self.exp))
        print("Your best weapon is a/an %s" % self.weapon)

    def command(self):
        command = input(">")
        if command.lower() in ["q", "quit", "exit"]:
            self.playing = False
        elif command.lower() == "i":
            self.check_self()
        elif command in self.directions:
            try:
                room_name = getattr(self.current_node, command)
                self.current_node = globals()[room_name]
            except KeyError:
                print("You can't go that way")
        else:
            print("Command not recognized")
        if command == "Skip":
            self.did_you_beat_raven_gorge = True
            self.total_gold += 100

    def die(self):
        print("You died")
        print("Try again")
        self.playing = False

    def fight(self, name, health, attack, exp, gold, did_you_beat_it):
        print("What would you like to do")
        fighting = input("ATTACK or FLEE")
        if fighting == "ATTACK" or "attack":
            while health > 0 and not did_you_beat_it:
                print("You swung your %s at the %s" % (self.weapon, name))
                print("The %s took %s damage" % (name, self.get_attack()))
                health -= you.get_attack()
                print("Now the %s has %s health left" % (name, health))
                print("The %s attacked you and you took %s damage" % (name, you.damage_you_take(attack)))
                self.health -= you.damage_you_take(attack)
                print("Now you have %s health" % self.get_health())
            if you.get_health() > 0:
                print("You defeated the %s" % name)
                print("You got %s gold" % gold)
                self.total_gold += gold
                print("Now you have %s gold" % gold)
                self.exp += exp
                print("You got %s exp" % exp)
                print("Now you have %s exp" % self.exp)
                self.level_up()
                eldrazi_scout.did_you_beat_monster = True
            elif you.get_health() <= 0:
                print("You died")
                print("Try again")
                self.playing = False
                afgaafdsf
        if fighting == "FLEE" or "flee":
            print("You died")
            print("Try again")
            self.playing = False


class Room(object):
    def __init__(self, name, north, south, east, west, surprise, room_text, surprise_name="", instant_death=False,
                 monster_in_it=False, monster_name="", gold_in_it=False, how_much_gold=0):
        self.monsters = monster_in_it
        self.north = north
        self.name = name
        self.south = south
        self.east = east
        self.west = west
        self.surprise = surprise
        self.room_text = room_text
        self.surprise_name = surprise_name
        self.instant_death = instant_death
        self.gold_in_it = gold_in_it
        self.how_much_gold = how_much_gold
        self.monster_name = monster_name

    def run_room(self, name=None, health=None, attack=None, gold=None, exp=None, did_you_beat_it=None):
        print(self.name)
        if self.room_text:
            print(self.room_text)
        if self.gold_in_it:
            print("You found %s gold" % self.how_much_gold)
            you.total_gold += self.how_much_gold
            print("Now you have %s gold" % you.total_gold)
        if self.monsters:
            print("A/an %s appeared" % name)
            you.fight(name, health, attack, gold, exp, did_you_beat_it)
        if self.instant_death:
            you.playing = False
            print("You died")
            print("Try again")
        if you.playing:
            you.command()


you = Person()

# Monsters
eldrazi_scout = Monster("Eldrazi Scout", 2, 1, 5, 5, False)
eldrazi_scion = Monster("Eldrazi Scion", 3, 2, 5, 5, False)
crab = Monster("Crab", 5, 3, 5, 5, False)
krayt_dragon = Monster("Krayt Dragon", 10, 5, 10, 10, False)
sidewinder_naga = Monster("Sidewinder Naga", 5, 4, 10, 5, False)
hydra = Monster("Hydra", 20, 1 * heads, 15, 20, False)
fire_elemental = Monster("Fire Elemental", 20, 5, 20, 20, False)
volcano_hellion = Monster("Volcano Hellion", 15, 10, 15, 10, False)

# Rooms
spawn_point_raven_gorge = Room("Spawn Point Raven Gorge", "raven_gorge1", None,
                               None, None, None, None)
raven_gorge1 = Room("Raven Gorge 1", "raven_gorge2", None, None, "raven_gorge2_left", None,
                    "There is an eldrazi scout north of you")
raven_gorge2 = Room("Raven Gorge 2", "raven_gorge3", "raven_gorge1", None, "raven_gorge2_left", None,
                    "An eldrazi scout is here", "", False, True, "Eldrazi Scout")
raven_gorge2_left = Room("Raven Gorge 2 Left", None, None, "raven_gorge2", None, None, "", "", False, False, "", True,
                         25)
raven_gorge3 = Room("Raven Gorge 3", "raven_gorge4", "raven_gorge2", "raven_gorge3_right", None, None, None, "", False,
                    True, "Eldrazi Scion")
raven_gorge3_right = Room("Raven Gorge 3 Right", None, None, None, "raven_gorge3", True,
                          "An eldrazi devastator appeared and ripped you apart", "Eldrazi Devastator", True)
raven_gorge4 = Room("Raven Gorge 4", None, "raven_gorge3", None, None, None, None)

you.current_node = spawn_point_raven_gorge

while you.playing:
    if you.current_node.name == "Spawn Point Raven Gorge":
        spawn_point_raven_gorge.run_room()
    if you.current_node.name == "Raven Gorge 1":
        raven_gorge1.run_room()
    if you.current_node.name == "Raven Gorge 2":
        raven_gorge2.run_room("Eldrazi Scout", eldrazi_scout.monster_health, eldrazi_scout.monster_attack,
                              eldrazi_scout.monster_gold, eldrazi_scout.monster_exp, eldrazi_scout.did_you_beat_monster)
    if you.current_node.name == "Raven Gorge 2 Left":
        raven_gorge2_left.run_room()
    if you.current_node.name == "Raven Gorge 3":
        raven_gorge3.run_room("Eldrazi Scion", eldrazi_scion.monster_health, eldrazi_scion.monster_attack,
                              eldrazi_scion.monster_gold, eldrazi_scion.monster_exp, eldrazi_scion.did_you_beat_monster)
    if you.current_node.name == "Raven Gorge 3 Right":
        raven_gorge3_right.run_room()
    if you.current_node.name == "Raven Gorge 4":
        raven_gorge4.run_room()


while you.alive_raven_gorge and you.playing and not you.did_you_beat_raven_gorge:
    if not you.read_starting_text:
        print("Welcome to Zendikar")
        print("This is a game of skill and quite a bit of luck")
        print("Try checking your stats and inventory by typing i")
        print("Or try moving by typing NORTH")
        you.read_starting_text = True
        print("You are in %s" % you.current_node.name)
    you.command()
    if you.current_node.name == "Raven Gorge 1":
        print("You are in %s" % you.current_node.name)
        if not eldrazi_scout.did_you_beat_monster:
            print("You start walking forward and you see an eldrazi scout north of you")
    elif you.current_node.name == "Raven Gorge 2":
        print("You are in %s" % you.current_node.name)
        if not eldrazi_scout.did_you_beat_monster:
            print("You see the eldrazi scout in front of you")
            you.fight(eldrazi_scout.name, eldrazi_scout.monster_health, eldrazi_scout.monster_attack,
                      eldrazi_scout.monster_gold, eldrazi_scout.monster_exp, eldrazi_scout.did_you_beat_monster)
    elif you.current_node.name == "Raven Gorge 2 Left":
        print("You are in %s" % you.current_node.name)
        print("You found 25 gold")
        you.total_gold += 25
        print("Now you have %s gold" % you.total_gold)
    elif you.current_node.name == "Raven Gorge 3":
        print("You are in %s" % you.current_node.name)
        print("An eldrazi scion appears")
        print("What would you like to do")
        eldrazi_scion_fight = input("ATTACK or FLEE")
        if eldrazi_scion_fight == "ATTACK":
            while eldrazi_scion.monster_health > 0 and you.total_health > 0 \
                    and not eldrazi_scion.did_you_beat_monster:
                print("The eldrazi attacked you")
                print("You took % i damage" % int(eldrazi_scion.monster_attack - you.defence))
                you.health -= int(eldrazi_scion.monster_attack - you.defence)
                print("Now you have %s health left" % you.combine_health())
                print("What would you like to attack with?")
                eldrazi_scion_fight1 = input("%s" % you.weapon)
                print("You swing your %s at the eldrazi" % you.weapon)
                print("The eldrazi takes %s damage" % you.damage)
                eldrazi_scion.monster_health -= you.damage
                print("The eldrazi has %s health left" % eldrazi_scion.monster_health)
                you.combine_health()
            if eldrazi_scion.monster_health <= 0:
                print("You defeated the eldrazi")
                you.total_gold += 5
                print("Now you have %s gold" % you.total_gold)
                you.exp += 5
                if you.exp >= you.exp_to_level_up:
                    you.exp -= 20
                    you.level += 1
                    you.damage_from_level += 1
                    you.health_from_level += 1
                    print("You leveled up")
                    print("Your damage and health increased by 1")
                    did_you_beat_the_eldrazi_scion = True
        if eldrazi_scion_fight == "FLEE":
            print("You tripped and the eldrazi killed you")
            print("You died")
            print("Try again")
            you.alive_raven_gorge = False
            playing = False
    elif you.current_node.name == "Raven Gorge 3 Right":
        print("You are in %s" % you.current_node.name)
        print("You disturbed an eldrazi devastator")
        print("It turns around and rips you in half with only 2 of its 4 arms")
        print("You died")
        print("Try again")
        you.alive_raven_gorge = False
        playing = False
    elif you.current_node.name == "Raven Gorge 4":
        print("You have reached the end of this area")
        print("Poof a shop appears")
        print("Would you like to enter the shop")
        print("You have %s gold" % you.total_gold)
        choice = input("YES or NO")
        if choice == "YES":
            print("This is what is offered")
            print("Wood Sword: 5 Gold, Copper Armor: 5 Gold, Health Potion: 5 Gold")
            print("What would you like to buy")
            while you.total_gold > 0 and you.shop == "YES" and you.in_shop:
                raven_gorge_shop = input("WOOD SWORD or COPPER ARMOR or HEALTH POTION")
                if raven_gorge_shop == "WOOD SWORD" and you.total_gold >= 5:
                    you.total_gold -= 5
                    weapon = "WOOD SWORD"
                    damage = 3
                    print("You bought the Wood Sword")
                    print("Now you deal %s damage" % you.combine_attack())
                    print("Now you have %s gold" % you.total_gold)
                if raven_gorge_shop == "COPPER ARMOR" and you.total_gold >= 5:
                    you.total_gold -= 5
                    armor = "COPPER ARMOR"
                    you.defence = 3
                    print("You bought the Copper Armor")
                    print("Now you have %s defence" % defence)
                    print("Now you have %s gold" % you.total_gold)
                if raven_gorge_shop == "HEALTH POTION" and you.total_gold >= 5:
                    you.total_gold -= 5
                    you.health += 3
                    print("You bought the Health Potion")
                    print("Now you have %s health" % you.combine_health())
                    print("Now you have %s gold" % you.total_gold)
                print("Would you like to remain in the shop")
                shop = input("YES or NO")
                if shop == "NO":
                    current_node = world_map["Sheltered Valley Map"]["Spawn Point Sheltered Valley"]
                    did_you_beat_raven_gorge = True
        if choice == "NO":
            pass


if you.playing:
    print("You beat round 1, congrats")
    print("Here is 25 gold for doing that")
    you.total_gold += 25
    print("Now you have %s gold" % you.total_gold)

"""
while you.alive_sheltered_valley and you.playing and not you.did_you_beat_sheltered_valley:
    if not you.first_time:
        print("You are now in Sheltered Valley")
        you.first_time = True
    print("Poof a shop appears")
    print("Would you like to enter it")
    shop1 = input("YES or NO")
    while shop1 == "YES" and you.shop3 == "YES":
        print("You entered the shop")
        print("This is what is offered")
        print("Stone Sword: 15 Gold, Health Potion: 5 Gold")
        shop2 = input("STONE SWORD or HEALTH POTION")
        if shop2 == "STONE SWORD" and you.total_gold >= 15:
            print("You bought a stone sword")
            weapon = "Stone Sword"
            damage = 5
            you.total_gold -= 15
            print("Now you do %s damage" % you.combine_attack())
            print("You have %s gold left" % you.total_gold)
        if shop2 == "HEALTH POTION" and you.total_gold >= 5:
            print("You bought a health potion")
            you.health += 3
            you.total_gold -= 5
            print("Now you have %s health" % you.combine_health())
            print("You have %s gold left" % you.total_gold)
        print("Would you like to remain in the shop")
        shop3 = input("YES or NO")
    if shop1 == "NO":
        pass
    you.command()
    if you.current_node.name == "Sheltered Valley 1":
        print("You are now in %s" % you.current_node.name)
        print("You see a dead body in the distance \nWhat do you want to do?")
        dead_body = input("Walk NORTH towards it or walk SOUTH away from it")
        if dead_body == "NORTH":
            you.current_node = world_map["Sheltered Valley Map"]["Sheltered Valley 2"]
            if not you.get_gold:
                print("You start walking towards the dead body")
                print("Whoever it was dropped a lot of gold")
                print("You found 50 gold")
                you.total_gold += 50
                print("Now you have %s gold" % you.total_gold)
                get_gold = True
        if dead_body == "SOUTH":
            you.current_node = world_map["Sheltered Valley Map"]["Sheltered Valley 7"]
            print("You walk away from the dead body so whatever killed it hopefully won't kill you")
    if you.current_node.name == "Sheltered Valley 2":
        print("You are now in %s" % you.current_node.name)
    if you.current_node.name == "Sheltered Valley 3":
        print("You are now in %s" % you.current_node.name)
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
    if you.current_node.name == "Mountain in Distance":
        print("You are now in %s" % you.current_node.name)
        print("You continue walking and you see a mountain in the distance")
        did_you_get_to_the_mountain = True
        did_you_beat_sheltered_valley = True
        you.current_node = world_map["Mountain Map"]["Spawn Point Mountain"]
    if you.current_node.name == "Sheltered Valley 7":
        print("You are now in %s" % you.current_node.name)
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
    if you.current_node.name == "Sheltered Valley 8":
        print("You are now in %s" % you.current_node.name)
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
    if you.current_node.name == "Great Desert":
        print("You are now in %s" % you.current_node.name)
        print("All in front of you is a vast desert")
        print("You see a sign and it says")
        print("You are in the Great Desert \nYou are going to die")
        did_you_get_to_the_desert = True
        did_you_beat_sheltered_valley = True
        you.current_node = world_map["Desert Map"]["Spawn Point Desert"]
    if you.current_node.name == "Sheltered Valley 4":
        print("You are now in %s" % you.current_node.name)
        print("There is a wall of trees in front of you with little room to pass into it")
        print("Do you want to go into it or try to go around it")
        tree = input("Go NORTH through it or EAST around it")
        if tree == "NORTH":
            you.current_node = world_map["Sheltered Valley Map"]["Sheltered Valley 5"]
            print("You enter the mass of trees")
        if tree == "EAST":
            print("You start going along the tree line")
            you.current_node = world_map["Sheltered Valley Map"]["Sheltered Valley 6"]
    if you.current_node.name == "Sheltered Valley 5":
        print("You are now in %s" % you.current_node.name)
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
    if you.current_node.name == "Lake":
        print("You are now in %s" % you.current_node.name)
        did_you_get_to_the_lake = True
    if you.current_node.name == "Sheltered Valley 6":
        print("You are now in %s" % you.current_node.name)
        print("You see a cabin and you enter it")
        print("When you enter it there is an eldrazi who kills you")
        print("You died")
        print("Try again")
        playing = False
        alive_sheltered_valley = False

alive_desert = True
alive_lake = True
alive_mountain = True

while you.playing and alive_desert and you.did_you_get_to_the_desert:
    print("You are now in the Great Desert")
    break

while you.playing and alive_mountain and you.did_you_get_to_the_mountain:
    print("You are at the base of the mountain")
    break

while you.playing and alive_lake and you.did_you_get_to_the_lake:
    print("You got to the lake")
    break
"""
