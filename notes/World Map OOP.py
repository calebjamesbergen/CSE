"""
class Room(object):
    # This is a constructor
    def __init__(self, name, north=None, south=None, east=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east

# These are instances of the rooms (Instantiation)


# Option 1 - Use the Variables, but fix later
R19A = Room("Mr. Wiebe's Room")
parking_lot = Room("The Parking Lot", None, R19A)

R19A.north = parking_lot

# Option 2 Use Strings, but more difficult controller
R19A = Room("Mr. Wiebe's Room", "parking_lot")
parking_lot = Room("The Parking Lot", None, "R19A")
"""
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
        self.health_potions = ["Health Potion", "Good Health Potion", "Great Health Potion"]
        self.weapons_list = ["Wood Sword", "Stone Sword", "Ice Sword", "Cave Sword", "Diamond Sword", "Enchanted Sword"]
        self.weapons_damage = [3, 5, 15, 15, 15, 25]
        self.armor_list = ["Copper Armor", "Iron Armor", "Diamond Armor", "Enchanted Armor"]
        self.armor_defence = [3, 10, 15, 20]
        self.health_potion_heal = 3
        self.good_health_potion_heal = 5
        self.great_health_potion_heal = 10

    def is_it_a_health_potion(self, health_potion):
        if health_potion == self.health_potions[0]:
            return 3
        if health_potion == self.health_potions[1]:
            return 5
        if health_potion == self.health_potions[2]:
            return 10

    def is_it_a_weapon(self, weapon):
        if weapon == self.weapons_list[0]:
            self.damage = self.weapons_damage[0]
            self.weapon = self.weapons_list[0]
        if weapon == self.weapons_list[1]:
            self.damage = self.weapons_damage[1]
            self.weapon = self.weapons_list[1]
        if weapon == self.weapons_list[2]:
            self.damage = self.weapons_damage[2]
            self.weapon = self.weapons_list[2]
        if weapon == self.weapons_list[3]:
            self.damage = self.weapons_damage[3]
            self.weapon = self.weapons_list[3]
        if weapon == self.weapons_list[4]:
            self.damage = self.weapons_damage[4]
            self.weapon = self.weapons_list[4]
        if weapon == self.weapons_list[5]:
            self.damage = self.weapons_damage[5]
            self.weapon = self.weapons_list[5]
        print("Now you deal %s damage" % self.combine_attack())

    def is_it_armor(self, armor):
        if armor == self.armor_list[0]:
            self.armor = self.armor_list[0]
            self.defence = self.armor_defence[0]
        if armor == self.armor_list[1]:
            self.armor = self.armor_list[1]
            self.defence = self.armor_defence[1]
        if armor == self.armor_list[2]:
            self.armor = self.armor_list[2]
            self.defence = self.armor_defence[2]
        if armor == self.armor_list[3]:
            self.armor = self.armor_list[3]
            self.defence = self.armor_defence[3]
        print("Now you have %s defence" % self.defence)

    def combine_health(self):
        self.total_health = self.health + self.health_from_level
        print("You have %s total health" % self.total_health)

    def combine_attack(self):
        return self.damage + self.damage_from_level

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
            print("You got 5 gold for leveling up")
            self.total_gold += 5
            print("Now you have %s gold" % self.total_gold)
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
            while health > 0 and not did_you_beat_it and self.get_health() > 0:
                print("The %s attacked you and you took %s damage" % (name, you.damage_you_take(attack)))
                self.health -= you.damage_you_take(attack)
                print("Now you have %s health" % self.get_health())
                print("You swung your %s at the %s" % (self.weapon, name))
                print("The %s took %s damage" % (name, self.get_attack()))
                health -= you.get_attack()
                print("Now the %s has %s health left" % (name, health))
            if you.health + you.health_from_level > 0:
                print("You defeated the %s" % name)
                print("You got %s gold" % gold)
                self.total_gold += gold
                print("Now you have %s gold" % gold)
                self.exp += exp
                print("You got %s exp" % exp)
                print("Now you have %s exp" % self.exp)
                self.level_up()
                eldrazi_scout.did_you_beat_monster = True
            elif you.health + you.health_from_level <= 0:
                self.die()
        if fighting in ["FLEE", "flee"]:
            self.die()


class Room(object):
    def __init__(self, name, north, south, east, west, surprise, room_text, surprise_name="", instant_death=False,
                 monster_in_it=False, monster_name="", gold_in_it=False, how_much_gold=0, shop=False, shop_item1=None,
                 shop_item2=None, shop_item3=None, shop_item4=None, shop_item1_cost=None, shop_item2_cost=None,
                 shop_item3_cost=None, shop_item4_cost=None, stay_in_shop="YES", next_place=None):
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
        self.shop = shop
        self.shop_item1 = shop_item1
        self.shop_item2 = shop_item2
        self.shop_item3 = shop_item3
        self.shop_item4 = shop_item4
        self.shop_item1_cost = shop_item1_cost
        self.shop_item2_cost = shop_item2_cost
        self.shop_item3_cost = shop_item3_cost
        self.shop_item4_cost = shop_item4_cost
        self.stay_in_shop = stay_in_shop
        self.next_place = next_place

    def run_shop(self):
        if self.shop:
            print("Would you like to enter the shop?")
            choice = input("YES or NO")
            while you.total_gold > 0 and self.stay_in_shop == "YES" and choice == "YES":
                print("You entered the shop")
                print("Here is what they offer")
                print("%s: %s, %s: %s, %s: %s, %s: %s" % (self.shop_item1, self.shop_item1_cost, self.shop_item2,
                                                          self.shop_item2_cost, self.shop_item3, self.shop_item3_cost,
                                                          self.shop_item4, self.shop_item4_cost))
                what_you_buy = input("%s or %s or %s or %s" % (self.shop_item1, self.shop_item2, self.shop_item3,
                                                               self.shop_item4))
                if what_you_buy == self.shop_item1 and you.total_gold > self.shop_item1_cost:
                    print("You bought a/an %s" % self.shop_item1)
                    you.total_gold -= self.shop_item1_cost
                    print("Now you have %s gold left" % you.total_gold)
                    if self.shop_item1 in you.health_potions:
                        you.health += you.is_it_a_health_potion(self.shop_item1)

                    if self.shop_item1 in you.weapons_list:
                        you.is_it_a_weapon(self.shop_item1)

                    if self.shop_item1 in you.armor_list:
                        you.is_it_armor(self.shop_item1)

                if what_you_buy == self.shop_item2 and you.total_gold > self.shop_item2_cost:
                    print("You bought a/an %s" % self.shop_item2)
                    you.total_gold -= self.shop_item2_cost
                    print("Now you have %s gold left" % you.total_gold)
                    if self.shop_item2 in you.health_potions:
                        you.health += you.is_it_a_health_potion(self.shop_item2)

                    if self.shop_item2 in you.weapons_list:
                        you.is_it_a_weapon(self.shop_item2)

                    if self.shop_item2 in you.armor_list:
                        you.is_it_armor(self.shop_item2)

                if what_you_buy == self.shop_item3 and you.total_gold > self.shop_item3_cost:
                    print("You bought a/an %s" % self.shop_item3)
                    you.total_gold -= self.shop_item3_cost
                    print("Now you have %s gold left" % you.total_gold)
                    if self.shop_item3 in you.health_potions:
                        you.health += you.is_it_a_health_potion(self.shop_item3)

                    if self.shop_item3 in you.weapons_list:
                        you.is_it_a_weapon(self.shop_item3)

                    if self.shop_item3 in you.armor_list:
                        you.is_it_armor(self.shop_item3)

                if what_you_buy == self.shop_item4 and you.total_gold > self.shop_item4_cost:
                    print("You bought a/an %s" % self.shop_item4)
                    you.total_gold -= self.shop_item4_cost
                    print("Now you have %s gold left" % you.total_gold)
                    if self.shop_item4 in you.health_potions:
                        you.health += you.is_it_a_health_potion(self.shop_item4)

                    if self.shop_item4 in you.weapons_list:
                        you.is_it_a_weapon(self.shop_item4)

                    if self.shop_item4 in you.armor_list:
                        you.is_it_armor(self.shop_item4)

                print("Would you like to stay in the shop?")
                self.stay_in_shop = input("YES or NO")
            print("Would you like to leave this area")
            print("You can not return once you leave")
            leave = input("YES or NO")
            if leave == "YES":
                you.room_name = self.next_place
                you.current_node = globals()[you.room_name]
            if leave == "NO":
                pass

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
        if self.shop:
            print("There is a shop here")
            self.run_shop()
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
# Raven Gorge
spawn_point_raven_gorge = Room("Spawn Point Raven Gorge", "raven_gorge1", None,
                               None, None, None, None)
raven_gorge1 = Room("Raven Gorge 1", "raven_gorge2", "spawn_point_raven_gorge", None, None, None,
                    "There is an eldrazi scout north of you")
raven_gorge2 = Room("Raven Gorge 2", "raven_gorge3", "raven_gorge1", None, "raven_gorge2_left", None,
                    "An eldrazi scout is here", "", False, True, "Eldrazi Scout")
raven_gorge2_left = Room("Raven Gorge 2 Left", None, None, "raven_gorge2", None, None, "", "", False, False, "", True,
                         25)
raven_gorge3 = Room("Raven Gorge 3", "raven_gorge4", "raven_gorge2", "raven_gorge3_right", None, None, None, "", False,
                    True, "Eldrazi Scion")
raven_gorge3_right = Room("Raven Gorge 3 Right", None, None, None, "raven_gorge3", True,
                          "An eldrazi devastator appeared and ripped you apart", "Eldrazi Devastator", True)
raven_gorge4 = Room("Raven Gorge 4", None, "raven_gorge3", None, None, None, None, "", False, False, "", False, 0,
                    True, "Wood Sword", "Health Potion", "Copper Armor", None, 5, 5, 5, None, "YES",
                    "spawn_point_sheltered_valley")
# Sheltered Valley
spawn_point_sheltered_valley = Room("Spawn Point Sheltered Valley", None, None, "sheltered_valley4",
                                    "sheltered_valley1", None,
                                    "You are now in a valley with grass going out in every direction")
sheltered_valley1 = Room("Sheltered Valley 1", "sheltered_valley2", "sheltered_valley7",
                         "spawn_point_sheltered_valley", None, None, "There is a dead body north of you")
sheltered_valley2 = Room("Sheltered Valley 2", "sheltered_valley3", None, None, None,
                         None, "Who ever died here dropped a lot of gold", "", False, False, "", True, 50)
sheltered_valley3 = Room("Sheltered Valley 3", "mountain", None, "sheltered_valley4", "sheltered_valley1",
                         None, "There is a stream here and you are very thirsty")
sheltered_valley4 = Room("Sheltered Valley 4", "sheltered_valley5", None, "sheltered_valley6",
                         "spawn_point_sheltered_valley", None,
                         "You start heading east and you see a mass of trees in front of you")
sheltered_valley5 = Room("Sheltered Valley 5", "lake", "sheltered_valley_4", None, None, None,
                         "You are now completely surrounded by trees")
sheltered_valley6 = Room("Sheltered Valley 6", None, None, None, None,
                         True, "You enter the cabin and an eldrazi is in there", "Eldrazi", True)
sheltered_valley7 = Room("Sheltered Valley 7", "sheltered_valley1", "sheltered_valley8", None, None,
                         None, "You hear a strange noise")
sheltered_valley8 = Room("Sheltered Valley 8", "sheltered_valley7", "great_desert", None, None,
                         None, "Night starts to fall and it gets very dark")
great_desert = Room("Great Desert", None, None, None, None, None,
                    "You see a sign and it says \n You are in the great desert \n You are going to die")
lake = Room("Lake", None, None, None, None, None,
            "The trees open and in front of you is a vast lake")
mountain = Room("Mountain", None, None, None, None, None, "Ahead of you is a large mountain")

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
    if you.current_node.name == "Spawn Point Sheltered Valley":
        spawn_point_sheltered_valley.run_room()
    if you.current_node.name == "Sheltered Valley 1":
        sheltered_valley1.run_room()
    if you.current_node.name == "Sheltered Valley 2":
        sheltered_valley2.run_room()
    if you.current_node.name == "Sheltered Valley 3":
        sheltered_valley3.run_room()
    if you.current_node.name == "Sheltered Valley 4":
        sheltered_valley4.run_room()
    if you.current_node.name == "Sheltered Valley 5":
        sheltered_valley5.run_room()
    if you.current_node.name == "Sheltered Valley 6":
        sheltered_valley6.run_room()
    if you.current_node.name == "Sheltered Valley 7":
        sheltered_valley7.run_room()
    if you.current_node.name == "Sheltered Valley 8":
        sheltered_valley8.run_room()
    if you.current_node.name == "Great Desert":
        great_desert.run_room()
    if you.current_node.name == "Lake":
        lake.run_room()
    if you.current_node.name == "Mountain":
        mountain.run_room()
