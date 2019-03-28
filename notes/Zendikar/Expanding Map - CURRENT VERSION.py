import random


class Item(object):
    def __init__(self, name, cost, is_it_collected=False):
        self.name = name
        self.cost = cost
        self.is_it_collected = is_it_collected


class Weapon(Item):
    def __init__(self, name, damage, cost, is_it_collected=False):
        super(Weapon, self).__init__(name, cost, is_it_collected)
        self.cost = cost
        self.damage = damage


class Stick(Weapon):
    def __init__(self, name, damage, cost, is_it_collected=False):
        super(Stick, self).__init__(name, damage, cost, is_it_collected)


class Sword(Weapon):
    def __init__(self, name, damage, cost, is_it_collected=False):
        super(Sword, self).__init__(name, damage, cost, is_it_collected)


class GreatSword(Weapon):
    def __init__(self, name, damage, cost, crit_rate1, crit_rate2, is_it_collected=False):
        super(GreatSword, self).__init__(name, damage, cost, is_it_collected)
        self.crit_rate1 = crit_rate1
        self.crit_rate2 = crit_rate2

    def crit_chance(self):
        critical_chance = random.randint(self.crit_rate1, self.crit_rate2)
        if critical_chance == self.crit_rate2:
            print("Critical hit")
            return "you.damage" * 2
        else:
            return "you.damage"


class Armor(Item):
    def __init__(self, name, defence, cost, is_it_collected=False):
        super(Armor, self).__init__(name, cost, is_it_collected)
        self.defence = defence
        self.cost = cost


class GreatArmor(Item):
    def __init__(self, name, defence, cost, is_it_collected=False):
        super(GreatArmor, self).__init__(name, cost, is_it_collected)
        self.defence = defence
        self.cost = cost

    def get_health_potion(self, name):
        if self.cost == self.cost:
            pass
        if name == "Health Potion":
            you.health_potions += 1
        if name == "Good Health Potion":
            you.good_health_potions += 1
        if name == "Health Potion":
            you.health_potions += 1


class AdditionalItem(Item):
    def __init__(self, name, cost, is_it_collected=False):
        super(AdditionalItem, self).__init__(name, cost, is_it_collected)
        self.name = name
        self.cost = cost


class Clothes(AdditionalItem):
    def __init__(self, name, cost, is_it_collected=False):
        super(Clothes, self).__init__(name, cost, is_it_collected)
        self.cost = cost


class Key(AdditionalItem):
    def __init__(self, name, cost, is_it_collected=False):
        super(Key, self).__init__(name, cost, is_it_collected)
        self.cost = cost


class Tools(AdditionalItem):
    def __init__(self, name, cost, is_it_collected=False):
        super(Tools, self).__init__(name, cost, is_it_collected)
        self.cost = cost


class Vehicle(AdditionalItem):
    def __init__(self, name, cost, is_it_collected=False):
        super(Vehicle, self).__init__(name, cost, is_it_collected)
        self.cost = cost


class Potion(AdditionalItem):
    def __init__(self, name, cost, is_it_collected=False):
        super(Potion, self).__init__(name, cost, is_it_collected)
        self.cost = cost


class Trash(AdditionalItem):
    def __init__(self, name, cost, is_it_collected=False):
        super(Trash, self).__init__(name, cost, is_it_collected)


class BananaPeel(Trash):
    def __init__(self, name, cost, is_it_collected=False):
        super(BananaPeel, self).__init__(name, cost, is_it_collected)


class BrokenBone(Trash):
    def __init__(self, name, cost, is_it_collected=False):
        super(BrokenBone, self).__init__(name, cost, is_it_collected)


class Fang(Trash):
    def __init__(self, name, cost, is_it_collected=False):
        super(Fang, self).__init__(name, cost, is_it_collected)


class Intestines(Trash):
    def __init__(self, name, cost, is_it_collected=False):
        super(Intestines, self).__init__(name, cost, is_it_collected)


class RottingFlesh(Trash):
    def __init__(self, name, cost, is_it_collected=False):
        super(RottingFlesh, self).__init__(name, cost, is_it_collected)


class Filler(Item):
    def __init__(self, name, cost, is_it_collected=False):
        super(Filler, self).__init__(name, cost, is_it_collected)
        self.name = name
        self.cost = cost


class Boss(object):
    def __init__(self, name, weapon, armor, health, crit_rate1, crit_rate2, crit_chance, crit_hit, did_you_beat_it,
                 on_fire=False):
        self.name = name
        self.weapon = weapon
        self.damage = weapon.damage
        self.armor = armor
        self.defence = armor.defence
        self.health = health
        self.crit_rate1 = crit_rate1
        self.crit_rate2 = crit_rate2
        self.crit_hit = crit_hit
        self.crit_chance = crit_chance
        self.damage_dealing = 0
        self.did_you_beat_it = did_you_beat_it
        self.on_fire = on_fire

    def burning(self):
        if self.on_fire and self.health > 0:
            print("%s has been burned" % self.name)
            self.health -= 5
            if self.health > 0:
                print("%s has taken 5 damage \nNow %s has %s health" % (self.name, self.name, self.health))
            else:
                self.health = 0
                print("%s has taken 5 damage \nNow %s has %s health" % (self.name, self.name, self.health))
            self.die()

    def attack_damage(self):
        self.damage_dealing = self.damage
        self.crit_chance = random.randint(self.crit_rate1, self.crit_rate2)
        if self.crit_chance == self.crit_hit:
            self.damage_dealing *= 2
        return self.damage_dealing

    def die(self):
        if self.health <= 0:
            print("%s has died" % self.name)
            self.did_you_beat_it = True


boss = Boss("Boss", Sword("Sword", 50, 0, False), Armor("Armor", 50, 0, False), 200, 1, 4, 4, False, False, True)

stick = Stick("Stick", 1, 0)

wood_sword = Sword("Wood Sword", 3, 5)
stone_sword = Sword("Stone Sword", 5, 10)
ice_sword = Sword("Ice Sword", 15, 20)
cave_sword = Sword("Cave Sword", 15, 20)

diamond_sword = GreatSword("Diamond Sword", 15, 20, 1, 5)
enchanted_sword = GreatSword("Enchanted Sword", 25, 50, 1, 3)

leather_armor = Armor("Leather Armor", 1, 0)
copper_armor = Armor("Copper Armor", 3, 5)
iron_armor = Armor("Iron Armor", 10, 10)
monster_armor = Armor("Monster Armor", 1, None)

diamond_armor = GreatArmor("Diamond Armor", 15, 20)
enchanted_armor = GreatArmor("Enchanted Armor", 20, 40)

goron_tunic = Clothes("Goron Tunic ", None)

bronze_key = Key("Bronze Key", 0)
copper_key = Key("Copper Key", 0)
silver_key = Key("Silver Key", 0)
gold_key = Key("Gold Key", 0)

machete = Tools("Machete", 0)
banana = Tools("Banana", 0)

boat = Vehicle("Boat", 25)

health_potion = Potion("Health Potion", 5)
good_health_potion = Potion("Good Health Potion", 10)
great_health_potion = Potion("Great Health Potion", 15)

banana_peel = BananaPeel("Banana peel", 0)

broken_bone = BrokenBone("Broken bone", 0)

fang = Fang("Fang", 0)

intestines = Intestines("Intestines", 0)

rotting_flesh = RottingFlesh("Rotting flesh", 0)

filler = Filler("Sold out", 0)

heads = 1


class Monster(object):
    def __init__(self, name, health, attack, exp, gold, armor, weapon, on_fire=False):
        self.name = name
        self.armor = armor
        self.health = health
        self.damage = attack
        self.exp = exp
        self.monster_gold = gold
        self.weapon = weapon
        self.on_fire = on_fire

    def burning(self):
        if self.on_fire and self.health > 0:
            print("%s has been burned" % self.name)
            self.health -= 5
            if self.health > 0:
                print("%s has taken 5 damage \nNow %s has %s health" % (self.name, self.name, self.health))
            else:
                self.health = 0
                print("%s has taken 5 damage \nNow %s has %s health" % (self.name, self.name, self.health))

    def take_damage(self, damage):
        if damage < self.armor.defence:
            print("No damage is done because of some FABULOUS armor!")
        else:
            self.health -= damage - self.armor.defence
        self.burning()
        if self.health < 0:
            self.health = 0
            print("%s has fallen" % self.name)
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


class Person(object):
    def __init__(self, name, health, weapon, armor, assigned_room="Spawn Point Raven Gorge"):
        self.name = name
        self.alive_raven_gorge = True
        self.directions = ["north", "south", "east", "west", "", "Skip"]
        self.current_node = assigned_room
        self.playing = True
        self.read_starting_text = False
        self.did_you_beat_raven_gorge = False
        self.weapon = weapon
        self.attack_amt = weapon.damage
        self.armor = armor
        self.defence = 1
        self.total_gold = 0
        self.health = health
        self.level = 1
        self.exp = 25
        self.exp_to_level_up = 30
        self.shop = "YES"
        self.in_shop = True
        self.inventory = []
        self.room_name = ""
        self.alive_sheltered_valley = True
        self.did_you_beat_sheltered_valley = False
        self.first_time = False
        self.get_gold = False
        self.did_you_get_to_the_desert = False
        self.did_you_get_to_the_mountain = False
        self.did_you_get_to_the_lake = False
        self.shop3 = "YES"
        self.defence = 1
        self.health_potions_list = ["Health Potion", "Good Health Potion", "Great Health Potion"]
        self.weapons_list = ["Wood Sword", "Stone Sword", "Ice Sword", "Cave Sword", "Diamond Sword", "Enchanted Sword"]
        self.weapons_damage = [3, 5, 15, 15, 15, 25]
        self.armor_list = ["Copper Armor", "Iron Armor", "Diamond Armor", "Enchanted Armor"]
        self.armor_defence = [3, 10, 15, 20]
        self.health_potion_heal = 3
        self.good_health_potion_heal = 5
        self.great_health_potion_heal = 10
        self.health_potions = 1
        self.good_health_potions = 0
        self.great_health_potions = 0
        self.did_command = False
        self.did_attack = False
        self.burning = False
        self.turns_to_burn_to_death = 3
        self.wanting_to_fight = True

    def burn_to_death(self):
        if goron_tunic.name in self.inventory:
            self.burning = False
            print("Because you have the goron tunic you do not get hurt by the heat")
        if self.turns_to_burn_to_death == 3 and self.burning:
            print("You are starting to get hot")
        if self.turns_to_burn_to_death == 2 and self.burning:
            print("You are starting to get very hot")
        if self.turns_to_burn_to_death == 1 and self.burning:
            print("You are so hot steam can be seen coming off your body")
        if self.turns_to_burn_to_death == 0 and self.burning:
            print("You died due to extreme heat")
            self.die()
        self.turns_to_burn_to_death -= 1

    def take_damage(self, damage):
        if damage <= self.armor.defence:
            print("No damage is done because of some FABULOUS armor")
        else:
            self.health -= damage - self.armor.defence
            if self.health <= 0:
                self.health = 0
                print("%s has fallen" % self.name)
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.attack_amt-target.armor.defence))
        target.take_damage(self.attack_amt)

    def fight(self, target):
        while target.health > 0 and self.health > 0 and self.wanting_to_fight:
            print("A %s appeared \nWould you like to attack it?" % target.name)
            choice = input("YES or NO")
            if choice.lower() == "i":
                self.check_self()
            if choice.upper() == "YES":
                target.attack(self)
                self.attack(target)
                if self.health > 0 and self.playing:
                    if target.health <= 0:
                        print("You defeated the %s" % target.name)
                        print("You got %s gold" % target.monster_gold)
                        self.total_gold += target.monster_gold
                        print("Now you have %s gold" % target.monster_gold)
                        print("You got %s exp" % target.exp)
                        self.exp += target.exp
                        self.level_up()
            if choice.upper() == "NO":
                self.wanting_to_fight = False

            if self.health == self.health:
                pass

    def is_it_a_health_potion(self, health_potion1):
        if health_potion1 == self.health_potions_list[0]:
            self.health_potions += 1
        if health_potion1 == self.health_potions_list[1]:
            self.good_health_potions += 1
        if health_potion1 == self.health_potions_list[2]:
            self.great_health_potions += 1

    def using_health_potion(self):
        if self.health_potions > 0:
            print("You have a health potion. Would you like to use it?")
            choice = input("YES or NO")
            if choice.upper() == "YES":
                self.health_potions -= 1
                print("You used a health potion")
                print("You restored %s health" % self.health_potion_heal)
                self.health += self.health_potion_heal
                print("Now you have %s health" % self.health)
            if choice.upper == "NO":
                pass
        if self.good_health_potions > 0:
            print("You have a good health potion. Would you like to use it?")
            choice = input("YES or NO")
            if choice.upper() == "YES":
                self.good_health_potions -= 1
                print("You used a good health potion")
                print("You restored %s health" % self.good_health_potion_heal)
                self.health += self.good_health_potion_heal
                print("Now you have %s health" % self.health)
            if choice.upper == "NO":
                pass
        if self.great_health_potions > 0:
            print("You have a great health potion. Would you like to use it?")
            choice = input("YES or NO")
            if choice.upper() == "YES":
                self.great_health_potions -= 1
                print("You used a health potion")
                print("You restored %s health" % self.great_health_potion_heal)
                self.health += self.great_health_potion_heal
                print("Now you have %s health" % self.health)
            if choice.upper == "NO":
                pass

    def is_it_a_weapon(self, weapon):
        if weapon == self.weapons_list[0]:
            self.attack_amt = self.weapons_damage[0]
            self.weapon = self.weapons_list[0]
            print("Now you deal %s damage" % self.attack_amt)
        if weapon == self.weapons_list[1]:
            self.attack_amt = self.weapons_damage[1]
            self.weapon = self.weapons_list[1]
            print("Now you deal %s damage" % self.attack_amt)
        if weapon == self.weapons_list[2]:
            self.attack_amt = self.weapons_damage[2]
            self.weapon = self.weapons_list[2]
            print("Now you deal %s damage" % self.attack_amt)
        if weapon == self.weapons_list[3]:
            self.attack_amt = self.weapons_damage[3]
            self.weapon = self.weapons_list[3]
            print("Now you deal %s damage" % self.attack_amt)
        if weapon == self.weapons_list[4]:
            self.attack_amt = self.weapons_damage[4]
            self.weapon = self.weapons_list[4]
            print("Now you deal %s damage" % self.attack_amt)
        if weapon == self.weapons_list[5]:
            self.attack_amt = self.weapons_damage[5]
            self.weapon = self.weapons_list[5]
            print("Now you deal %s damage" % self.attack_amt)

    def is_it_armor(self, armor):
        if armor == self.armor_list[0]:
            self.armor = self.armor_list[0]
            self.defence = self.armor_defence[0]
            print("Now you have %s defence" % self.defence)
        if armor == self.armor_list[1]:
            self.armor = self.armor_list[1]
            self.defence = self.armor_defence[1]
            print("Now you have %s defence" % self.defence)
        if armor == self.armor_list[2]:
            self.armor = self.armor_list[2]
            self.defence = self.armor_defence[2]
            print("Now you have %s defence" % self.defence)
        if armor == self.armor_list[3]:
            self.armor = self.armor_list[3]
            self.defence = self.armor_defence[3]
            print("Now you have %s defence" % self.defence)

    def pick_up_item(self, item):
        print("There is a %s" % item.name)
        print("Would you like to pick it up?")
        choice = input("YES or NO")

        if choice.upper() == "YES":
            added_item = False
            if item in self.health_potions_list:
                self.is_it_a_health_potion(item.name)
                added_item = True
            if not added_item:
                self.inventory.append(item.name)
                print("You picked up the %s" % item.name)
            item.is_it_collected = True

        if choice.upper() == "NO":
            print("You didn't pick up the %s" % item.name)

    def level_up(self):
        if self.exp >= self.exp_to_level_up:
            self.exp -= 20
            print("You leveled up")
            print("You got 5 gold for leveling up")
            self.total_gold += 5
            print("Now you have %s gold" % self.total_gold)
            print("Your health and attack increased by one")
            self.attack_amt += 1
            self.health += 1
            self.level += 1
            print("Now you are level %s" % self.level)

    def check_self(self):
        print("You deal %s damage" % self.attack_amt)
        print("You have this armor: %s" % self.armor.name)
        print("You have %s defence" % self.defence)
        print("You have %s health" % self.health)
        print("You have %s gold" % self.total_gold)
        print("You are level %s" % self.level)
        print("You are %s exp away from leveling up" % (self.exp_to_level_up - self.exp))
        print("Your best weapon is a/an %s" % self.weapon.name)
        print("This is in your inventory: %s" % ", ".join(self.inventory))
        self.using_health_potion()

    def run_command(self):
        while not self.did_command:
            if self.playing:
                command = input(">")
                if command.lower() in ["q", "quit", "exit"]:
                    self.playing = False
                elif self.burning:
                    self.burn_to_death()
                elif command.lower() == "i":
                    self.check_self()
                elif command == "":
                    pass
                elif command in self.directions:
                    try:
                        room_name = getattr(self.current_node, command)
                        self.current_node = globals()[room_name]
                        self.did_command = True
                    except KeyError:
                        print("You can't go that way")
                else:
                    print("Command not recognized")
                if command == "s":
                    room_name = "spawn_point_sheltered_valley"
                    self.current_node = globals()[room_name]
                    self.total_gold += 100
                    self.weapon = "Wood Sword"
                    self.attack_amt = 3
                    self.armor = "Copper Armor"
                    self.defence = 3
                    self.health = 10
        self.did_command = False

    def die(self):
        print("You died")
        print("Try again")
        self.playing = False
        self.health = 0


choice1 = input("What would you like your name to be?")

you = Person(choice1, 5, stick, leather_armor)

# Monsters
eldrazi_scout = Monster("Eldrazi Scout", 1, 1, 5, 5, Armor("Monster Armor", 0, 0), Sword("Claw", 1, None))
eldrazi_scion = Monster("Eldrazi Scion", 3, 2, 5, 5, Armor("Monster Armor", 0, 0), Sword("Claw", 1, None))
crab = Monster("Crab", 5, 3, 5, 5, Armor("Monster Armor", 2, None), Sword("Pincer", 1, None))
krayt_dragon = Monster("Krayt Dragon", 10, 5, 10, 10, Armor("Monster Armor", 3, None), Sword("Claw", 1, None))
sidewinder_naga = Monster("Sidewinder Naga", 5, 4, 10, 5, Armor("Monster Armor", 3, None), Sword("Dagger", 1, None))
hydra = Monster("Hydra", 20, 1 * heads, 15, 20, Armor("Monster Armor", 4, None), Sword("Claw", 1, None))
fire_elemental = Monster("Fire Elemental", 20, 5, 20, 20, Armor("Monster Armor", 5, None), Sword("Flames", 1, None))
volcano_hellion = Monster("Volcano Hellion", 15, 10, 15, 10, Armor("Monster Armor", 5, None), Sword("Flames", 1, None))

lylek = Monster("Lylek", 15, 20, 20, 15, Armor("Skin", 15, 0), Weapon("Leg", 20, 0))
godzilla = Monster("Godzilla", 50, 20, 40, 30, Armor("Skin", 15, 0), Weapon("Fire breath", 20, 0))
volcanic_dragon = Monster("Volcanic Dragon", 15, 15, 15, 15, Armor("Scales", 15, 0), Weapon("Fire breath", 15, 0))
bellowing_tanglewurm = Monster("Bellowing Tanglewurm", 30, 15, 20, 20, Armor("Skin", 20, 0), Weapon("Mouth", 15, 0))
grunn = Monster("Grunn", 60, 10, 40, 40, Armor("Grass Armor", 15, 0), Weapon("Fist", 10, 0))
baloth = Monster("Baloth", 20, 20, 20, 20, Armor("Skin", 20, 0), Weapon("Mouth", 20, 0))


class Room(object):
    def __init__(self, name, north, south, east, west, surprise, room_text, item_in_it=False, item=None,
                 surprise_name="", instant_death=False, monster_in_it=False, monster_name="", gold_in_it=False,
                 how_much_gold=0, shop=False, shop_item1=None, shop_item2=None, shop_item3=None, shop_item4=None,
                 stay_in_shop="YES", next_place=None, ):
        self.monsters = monster_in_it
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.surprise = surprise
        self.room_text = room_text
        self.surprise_name = surprise_name
        self.instant_death = instant_death
        self.monster_in_it = monster_in_it
        self.gold_in_it = gold_in_it
        self.how_much_gold = how_much_gold
        self.monster_name = monster_name
        self.shop = shop
        self.shop_item1 = shop_item1
        self.shop_item2 = shop_item2
        self.shop_item3 = shop_item3
        self.shop_item4 = shop_item4
        if self.shop_item1 is not None:
            self.shop_item1_cost = shop_item1.cost
        else:
            self.shop_item1_cost = 0
        if self.shop_item2 is not None:
            self.shop_item2_cost = shop_item2.cost
        else:
            self.shop_item2_cost = 0
        if self.shop_item3 is not None:
            self.shop_item3_cost = shop_item3.cost
        else:
            self.shop_item4_cost = 0
        if self.shop_item4 is not None:
            self.shop_item4_cost = shop_item4.cost
        else:
            self.shop_item1_cost = 0
        self.stay_in_shop = stay_in_shop
        self.next_place = next_place
        self.item_in_it = item_in_it
        self.item = item
        self.did_it = False
        self.choice = ""
        self.enter_shop = ""

    def printing_stuff_for_shop(self):
        did_it = False
        if self.shop_item4.name is not None and not did_it:
            print("%s: %s, %s: %s, %s: %s, %s: %s" % (self.shop_item1.name, self.shop_item1.cost,
                                                      self.shop_item2.name, self.shop_item2.cost,
                                                      self.shop_item3.name, self.shop_item3.cost,
                                                      self.shop_item4.name, self.shop_item4.cost))
            did_it = True
        if self.shop_item3.name is not None and not did_it:
            print("%s: %s, %s: %s, %s: %s" % (self.shop_item1.name, self.shop_item1.cost,
                                              self.shop_item2.name, self.shop_item2.cost,
                                              self.shop_item3.name, self.shop_item3.cost,))
            did_it = True
        if self.shop_item2.name is not None and not did_it:
            print("%s: %s, %s: %s" % (self.shop_item1.name, self.shop_item1.cost,
                                      self.shop_item2.name, self.shop_item2.cost))
            did_it = True
        if self.shop_item1.name is not None and not did_it:
            print("%s: %s" % (self.shop_item1.name, self.shop_item1.cost))
            did_it = True
            if did_it == did_it:
                pass

    def choosing_what_to_buy(self):
        print("What would you like to buy")
        did_it = False
        if self.shop_item4.name is not None and not did_it:
            self.choice = input("%s or %s or %s or %s" % (self.shop_item1.name, self.shop_item2.name,
                                                          self.shop_item3.name, self.shop_item4.name))
            did_it = True
        if self.shop_item3.name is not None and not did_it:
            self.choice = input("%s or %s or %s" % (self.shop_item1.name, self.shop_item2.name,
                                                    self.shop_item3.name))
            did_it = True
        if self.shop_item2.name is not None and not did_it:
            self.choice = input("%s or %s" % (self.shop_item1.name, self.shop_item2.name))
            did_it = True
        if self.shop_item1.name is not None and not did_it:
            self.choice = input("%s" % self.shop_item1.name)
            did_it = True
            if did_it == did_it:
                pass

    def buying_stuff(self):
        self.choosing_what_to_buy()
        if self.choice == self.shop_item1.name and you.total_gold > self.shop_item1.cost:
            print("You bought a/an %s" % self.shop_item1.name)
            you.total_gold -= self.shop_item1.cost
            if self.shop_item1 in you.weapons_list:
                you.is_it_a_weapon(self.shop_item1)
            elif self.shop_item1 in you.armor_list:
                you.is_it_armor(self.shop_item1)
            elif self.shop_item1 in you.health_potions_list:
                you.is_it_a_health_potion(self.shop_item1)
            else:
                you.inventory.append(self.shop_item1)
            print("Now you have %s gold left" % you.total_gold)

        if self.choice == self.shop_item2.name and you.total_gold > self.shop_item2.cost:
            print("You bought a/an %s" % self.shop_item2.name)
            you.total_gold -= self.shop_item2.cost
            if self.shop_item2 in you.weapons_list:
                you.is_it_a_weapon(self.shop_item2)
            elif self.shop_item2 in you.armor_list:
                you.is_it_armor(self.shop_item2)
            elif self.shop_item2 in you.health_potions_list:
                you.is_it_a_health_potion(self.shop_item2)
            else:
                you.inventory.append(self.shop_item2)
            print("Now you have %s gold left" % you.total_gold)

        if self.choice == self.shop_item3.name and you.total_gold > self.shop_item3.cost:
            print("You bought a/an %s" % self.shop_item3.name)
            you.total_gold -= self.shop_item3.cost
            if self.shop_item3 in you.weapons_list:
                you.is_it_a_weapon(self.shop_item3)
            elif self.shop_item3 in you.armor_list:
                you.is_it_armor(self.shop_item3)
            elif self.shop_item3 in you.health_potions_list:
                you.is_it_a_health_potion(self.shop_item3)
            else:
                you.inventory.append(self.shop_item3)
            print("Now you have %s gold left" % you.total_gold)

        if self.choice == self.shop_item4.name and you.total_gold > self.shop_item4.cost:
            print("You bought a/an %s" % self.shop_item4.name)
            you.total_gold -= self.shop_item4.cost
            if self.shop_item4 in you.weapons_list:
                you.is_it_a_weapon(self.shop_item4)
            elif self.shop_item4 in you.armor_list:
                you.is_it_armor(self.shop_item4)
            elif self.shop_item4 in you.health_potions_list:
                you.is_it_a_health_potion(self.shop_item4)
            else:
                you.inventory.append(self.shop_item4)
            print("Now you have %s gold left" % you.total_gold)

    def run_shop(self):
        print("Would you like to enter it")
        self.enter_shop = input("YES or NO")
        while self.enter_shop.upper() == "YES" and self.stay_in_shop.upper() == "YES":
            if self.stay_in_shop.upper() == "YES":
                print("You entered the shop")
                print("Here is what they offer")
                self.printing_stuff_for_shop()
                self.buying_stuff()
                print("Would you like to stay in the shop?")
                self.stay_in_shop = input("YES or NO")

        if self.stay_in_shop.upper() == "NO":
            print("You did not enter the shop")

    def decision_room(self):
        print(self.name)
        if self.room_text:
            print(self.room_text)

    def run_room(self, target=None):
        print(self.name)
        if self.room_text:
            print(self.room_text)
        if self.item_in_it:
            if not self.item.is_it_collected:
                you.pick_up_item(self.item)
        if self.gold_in_it:
            print("You found %s gold" % self.how_much_gold)
            you.total_gold += self.how_much_gold
            print("Now you have %s gold" % you.total_gold)
        if self.instant_death:
            you.die()
        if self.monster_in_it:
            you.fight(target)
        if self.shop:
            print("There is a shop here")
            self.run_shop()
        if you.playing:
            you.run_command()


# Rooms
# Raven Gorge
spawn_point_raven_gorge = Room("Spawn Point Raven Gorge", "raven_gorge1", None,
                               None, None, None, None)
raven_gorge1 = Room("Raven Gorge 1", "raven_gorge2", "spawn_point_raven_gorge", None, None, None,
                    "There is an eldrazi scout north of you", True, banana_peel)
raven_gorge2 = Room("Raven Gorge 2", "raven_gorge3", "raven_gorge1", None, "raven_gorge2_left", None,
                    "An eldrazi scout is here", False, None, "", False, True, "Eldrazi Scout")
raven_gorge2_left = Room("Raven Gorge 2 Left", None, None, "raven_gorge2", None, None, "", False, None,
                         "", False, False, "", True, 25)
raven_gorge3 = Room("Raven Gorge 3", "raven_gorge4", "raven_gorge2", "raven_gorge3_right", None, None, None, False,
                    None, "", False, True, "Eldrazi Scion")
raven_gorge3_right = Room("Raven Gorge 3 Right", None, None, None, "raven_gorge3", True,
                          "An eldrazi devastator appeared and ripped you apart", False, None, "Eldrazi Devastator",
                          True)
raven_gorge4 = Room("Raven Gorge 4", None, "raven_gorge3", None, None, None, None, False, None, "", False, False,
                    "", False, 0, True, wood_sword, health_potion, copper_armor, filler, "YES",
                    "spawn_point_sheltered_valley")
# Sheltered Valley
spawn_point_sheltered_valley = Room("Spawn Point Sheltered Valley", None, None, "sheltered_valley4",
                                    "sheltered_valley1", None,
                                    "You are now in a valley with grass going out in every direction")
sheltered_valley1 = Room("Sheltered Valley 1", "sheltered_valley2", "sheltered_valley7",
                         "spawn_point_sheltered_valley", None, None, "There is a dead body north of you")
sheltered_valley2 = Room("Sheltered Valley 2", "sheltered_valley3", None, None, None,
                         None, "Who ever died here dropped a lot of gold", False, None, "", False, False, "", True, 50)
sheltered_valley3 = Room("Sheltered Valley 3", "mountain", None, "sheltered_valley4", "sheltered_valley1",
                         None, "There is a stream here and you are very thirsty")
sheltered_valley4 = Room("Sheltered Valley 4", "sheltered_valley5", None, "sheltered_valley6",
                         "spawn_point_sheltered_valley", None,
                         "You start heading east and you see a mass of trees in front of you \nAlso to your east you"
                         " see a cabin")
sheltered_valley5 = Room("Sheltered Valley 5", "lake", "sheltered_valley_4", None, None, None,
                         "You are now completely surrounded by trees")
sheltered_valley6 = Room("Sheltered Valley 6", None, None, None, None,
                         True, "You enter the cabin and an eldrazi is in there", False, None, "Eldrazi", True)
sheltered_valley7 = Room("Sheltered Valley 7", "sheltered_valley1", "sheltered_valley8", None, None,
                         None, "You hear a strange noise")
sheltered_valley8 = Room("Sheltered Valley 8", "sheltered_valley7", "great_desert", None, None,
                         None, "Night starts to fall and it gets very dark")
great_desert = Room("Great Desert", None, None, None, None, None,
                    "You see a sign and it says \n You are in the great desert \n You are going to die", False, None,
                    "", False, False, "", False, 0, True, stone_sword, health_potion, filler, filler, "YES",
                    "spawn_point_great_desert")
lake = Room("Lake", None, None, None, None, None, "The trees open and in front of you is a vast lake", False, None,
            "", False, False, "", False, 0, True, stone_sword, health_potion, filler, filler, "YES",
            "spawn_point_lake")
mountain = Room("Mountain", None, None, None, None, None, "Ahead of you is a large mountain", False, None,
                "", False, False, "", False, 0, True, stone_sword, health_potion, filler, filler, "YES",
                "spawn_point_mountain")

# Mountain
spawn_point_mountain = Room("Spawn Point Mountain", None, None, None, None, None, "You are in Spawn Point Mountain")
# Lake
spawn_point_lake = Room("Spawn Point Lake", None, None, None, None, None, "You are in Spawn Point Mountain")
# Desert
spawn_point_great_desert = Room("Spawn Point Great Desert", None, None, None, None, None,
                                "You are in Spawn Point Mountain")
you.current_node = spawn_point_raven_gorge

first_time = True

while you.playing:
    if first_time:
        print("Welcome to Zendikar")
        print("This game will require skill and a bit of luck")
        print("Try checking your inventory by typing 'i'")
        print("Or type 'north' 'south' 'east' or 'west' to begin")
        print("Have fun")
        first_time = False
    if you.current_node.name == "Spawn Point Raven Gorge":
        spawn_point_raven_gorge.run_room()
    if you.current_node.name == "Raven Gorge 1":
        raven_gorge1.run_room()
    if you.current_node.name == "Raven Gorge 2":
        raven_gorge2.run_room(eldrazi_scout)
    if you.current_node.name == "Raven Gorge 2 Left":
        raven_gorge2_left.run_room()
    if you.current_node.name == "Raven Gorge 3":
        raven_gorge3.run_room(eldrazi_scion)
    if you.current_node.name == "Raven Gorge 3 Right":
        raven_gorge3_right.run_room()
    if you.current_node.name == "Raven Gorge 4":
        print("Since this is your first time in a shop I will give you a hint")
        print("Buying an item multiple times, other than a health potion, gives you nothing extra or helpful")
        raven_gorge4.run_room()
    if you.current_node.name == "Spawn Point Sheltered Valley":
        spawn_point_sheltered_valley.run_room()
    if you.current_node.name == "Sheltered Valley 1":
        sheltered_valley1.run_room()
    if you.current_node.name == "Sheltered Valley 2":
        sheltered_valley2.run_room()
    if you.current_node.name == "Sheltered Valley 3":
        sheltered_valley3.decision_room()
        print("You start to get very thirsty and there is a stream beside you")
        print("Do you want to drink from it")
        stream = input("YES or NO")
        if stream.upper() == "YES":
            print("You drank from the stream and you are no longer thirsty")
            print("Sadly within a couple of minutes you fall over and do not get back up")
            you.die()
        if stream.upper() == "NO":
            print("You do not drink from the stream and that is probably a good thing")
        you.run_command()
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
