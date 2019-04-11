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
    def __init__(self, name, armor, defence, health, did_you_beat_it, on_fire, gold, exp):
        self.name = name
        self.armor = armor
        self.defence = defence
        self.health = health
        self.did_you_beat_it = did_you_beat_it
        self.on_fire = on_fire
        self.gold = gold
        self.exp = exp

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

    def die(self):
        if self.health <= 0:
            print("%s has died" % self.name)
            self.did_you_beat_it = True


class Knucklotec(Boss):
    def __init__(self, name, armor, defence, health, did_you_beat_it, on_fire, gold, exp):
        super(Knucklotec, self).__init__(name, armor, defence, health, did_you_beat_it, on_fire, gold, exp)

    def attack(self, target):
        print("%s starts to attack" % self.name)
        attack_num = random.randint(1, 4)
        if attack_num == 1:
            print("%s starts to send a fist at you" % self.name)
            print("He hits you but it does not hurt very much")
            target.take_damage(12)
        if attack_num == 2:
            print("%s starts to send a fist high in the air" % self.name)
            print("Suddenly the fist comes crashing down")
            target.take_damage(16)
        if attack_num == 3:
            print("%s sends both fists a you" % self.name)
            print("He then squishes you between both of his fists")
            target.take_damage(18)
        if attack_num == 4:
            print("%s starts to send a fist at you" % self.name)
            print("But he misses")

    def take_damage(self, damage):
        if damage <= self.armor.defence:
            print("No damage is done because of some FABULOUS armor")
        else:
            self.health -= damage - self.armor.defence
            if self.health <= 0:
                self.health = 0
                print("%s has fallen" % self.name)
        print("%s has %d health left" % (self.name, self.health))


class Bowser(Boss):
    def __init__(self, name, armor, defence, health, did_you_beat_it, on_fire, gold, exp):
        super(Bowser, self).__init__(name, armor, defence, health, did_you_beat_it, on_fire, gold, exp)

    def attack(self, target):
        print("%s starts to attack" % self.name)
        attack_num = random.randint(1, 4)
        if attack_num == 1:
            print("%s launches a fireball at you" % self.name)
            target.take_damage(10)
        if attack_num == 2:
            print("%s launches multiple fireballs at you" % self.name)
            target.take_damage(15)
        if attack_num == 3:
            print("%s spins in his shell at you" % self.name)
            target.take_damage(5)
        if attack_num == 4:
            print("%s swipes his claws at you" % self.name)
            print("But he misses")

    def take_damage(self, damage):
        if damage <= self.armor.defence:
            print("No damage is done because of some FABULOUS armor")
        else:
            self.health -= damage - self.armor.defence
            if self.health <= 0:
                self.health = 0
                print("%s has fallen" % self.name)
        print("%s has %d health left" % (self.name, self.health))


class TukTuk(Boss):
    def __init__(self, name, armor, defence, health, did_you_beat_it, on_fire, gold, exp):
        super(TukTuk, self).__init__(name, armor, defence, health, did_you_beat_it, on_fire, gold, exp)

    def attack(self, target):
        if target == target:
            pass
        print("%s swings his torch at you but nothing happens" % self.name)

    def take_damage(self, damage):
        if damage <= self.armor.defence:
            print("No damage is done because of some FABULOUS armor")
        else:
            self.health -= damage - self.armor.defence
            if self.health <= 0:
                self.health = 0
                print("%s has fallen" % self.name)
        print("%s has %d health left" % (self.name, self.health))


class TukTukReturned(Boss):
    def __init__(self, name, armor, defence, health, did_you_beat_it, on_fire, gold, exp):
        super(TukTukReturned, self).__init__(name, armor, defence, health, did_you_beat_it, on_fire, gold, exp)

    def attack(self, target):
        print("%s starts to attack" % self.name)
        attack_num = random.randint(1, 3)
        if attack_num == 1:
            print("%s punches you with 1 fist" % self.name)
            target.take_damage(10)
        if attack_num == 2:
            print("%s punches you with both fists" % self.name)
            target.take_damage(15)
        if attack_num == 3:
            print("%s tries to grab you\nBut he misses" % self.name)

    def take_damage(self, damage):
        if damage <= self.armor.defence:
            print("No damage is done because of some FABULOUS armor")
        else:
            self.health -= damage - self.armor.defence
            if self.health <= 0:
                self.health = 0
                print("%s has fallen" % self.name)
        print("%s has %d health left" % (self.name, self.health))


tuktuk = TukTuk("TukTuk", Armor("Armor", 3, 0), 3, 15, False, False, 5, 5)
tuktukreturned = TukTukReturned("TukTuk Returned", Armor("Armor", 5, 0), 5, 35, False, False, 25, 25)

bowser = Bowser("Bowser", Armor("Armor", 5, 0, False), 5, 35, False, False, 25, 25)

knucklotec = Knucklotec("Knucklotec", Armor("Armor", 10, 0, False), 10, 50, False, False, 50, 50)

stick = Stick("Stick", 1, 0)

wood_sword = Sword("Wood Sword", 10, 5)
stone_sword = Sword("Stone Sword", 15, 10)
ice_sword = Sword("Ice Sword", 25, 20)
cave_sword = Sword("Cave Sword", 25, 20)

diamond_sword = GreatSword("Diamond Sword", 35, 20, 1, 5)
enchanted_sword = GreatSword("Enchanted Sword", 50, 50, 1, 3)

leather_armor = Armor("Leather Armor", 5, 0)
copper_armor = Armor("Copper Armor", 10, 5)
iron_armor = Armor("Iron Armor", 15, 10)
monster_armor = Armor("Monster Armor", 1, None)

diamond_armor = GreatArmor("Diamond Armor", 30, 20)
enchanted_armor = GreatArmor("Enchanted Armor", 50, 40)

goron_tunic = Clothes("Goron Tunic ", None)

bronze_key = Key("Bronze Key", 0)
copper_key = Key("Copper Key", 0)
silver_key = Key("Silver Key", 0)
gold_key = Key("Gold Key", 0)

machete = Tools("Machete", 0)
banana = Tools("Banana", 0)
pickaxe = Tools("Pickaxe", 20, False)

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
        self.gold = gold
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
        self.directions = ["north", "south", "east", "west"]
        self.short_directions = ["n", "s", "e", "w"]
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
        self.health_potions_list = [health_potion.name, good_health_potion.name, great_health_potion.name]
        self.weapons_list = [wood_sword.name, stone_sword.name, ice_sword.name, diamond_sword.name,
                             enchanted_sword.name]
        self.weapons_damage = [10, 15, 25, 25, 35, 50]
        self.armor_list = [copper_armor.name, iron_armor.name, diamond_armor.name, enchanted_armor.name]
        self.armor_defence = [10, 15, 30, 50]
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
        self.first_time1 = True

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
        print("%s damage is dealt" % damage)
        if damage <= self.defence:
            print("No damage is done because of some FABULOUS armor")
        else:
            self.health -= damage - self.defence
            if self.health <= 0:
                self.health = 0
                print("%s has fallen" % self.name)
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.attack_amt-target.armor.defence))
        target.take_damage(self.attack_amt)

    def get_stuff_from_monster(self, target):
        print("You defeated the monster")
        print("You got %s gold" % target.gold)
        self.total_gold += target.gold
        print("Now you have %s gold" % self.total_gold)
        print("You got %s exp" % target.exp)
        self.exp += target.exp
        print("Now you have %s exp" % self.exp)
        self.level_up()

    def fight(self, target):
        while target.health > 0 and self.health > 0 and self.wanting_to_fight:
            if self.first_time1:
                print("A/an %s appeared" % target.name)
                self.first_time1 = False
            print("Would you like to attack it?")
            choice = input("YES or NO")
            if choice.lower() == "i":
                self.check_self()
            if choice.upper() == "YES":
                target.attack(self)
                if self.health > 0:
                    self.attack(target)
            if target.health <= 0 and self.playing:
                self.get_stuff_from_monster(target)
                self.first_time1 = True
            if self.health <= 0:
                you.die()
            if choice.upper() == "NO":
                self.wanting_to_fight = False
                print("As you fled the %s killed you" % target.name)
                self.die()

    def is_it_a_health_potion(self, health_potion1):
        if health_potion1.name == self.health_potions_list[0]:
            self.health_potions += 1
        if health_potion1.name == self.health_potions_list[1]:
            self.good_health_potions += 1
        if health_potion1.name == self.health_potions_list[2]:
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
        if weapon.name == self.weapons_list[0]:
            self.attack_amt = self.weapons_damage[0]
            self.weapon = self.weapons_list[0]
            print("Now you deal %s damage" % self.attack_amt)
        if weapon.name == self.weapons_list[1]:
            self.attack_amt = self.weapons_damage[1]
            self.weapon = self.weapons_list[1]
            print("Now you deal %s damage" % self.attack_amt)
        if weapon.name == self.weapons_list[2]:
            self.attack_amt = self.weapons_damage[2]
            self.weapon = self.weapons_list[2]
            print("Now you deal %s damage" % self.attack_amt)
        if weapon.name == self.weapons_list[3]:
            self.attack_amt = self.weapons_damage[3]
            self.weapon = self.weapons_list[3]
            print("Now you deal %s damage" % self.attack_amt)
        if weapon.name == self.weapons_list[4]:
            self.attack_amt = self.weapons_damage[4]
            self.weapon = self.weapons_list[4]
            print("Now you deal %s damage" % self.attack_amt)

    def is_it_armor(self, armor):
        if armor.name == self.armor_list[0]:
            self.armor = self.armor_list[0]
            self.defence = self.armor_defence[0]
            print("Now you have %s defence" % self.defence)
        if armor.name == self.armor_list[1]:
            self.armor = self.armor_list[1]
            self.defence = self.armor_defence[1]
            print("Now you have %s defence" % self.defence)
        if armor.name == self.armor_list[2]:
            self.armor = self.armor_list[2]
            self.defence = self.armor_defence[2]
            print("Now you have %s defence" % self.defence)
        if armor.name == self.armor_list[3]:
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
        while self.exp >= self.exp_to_level_up:
                self.exp -= self.exp_to_level_up
                print("You leveled up")
                print("You got 5 gold for leveling up")
                self.total_gold += 5
                print("Now you have %s gold" % self.total_gold)
                print("Your health increased by 2")
                self.health += 2
                print("Now you have %s health" % self.health)
                self.level += 1
                print("Now you are level %s" % self.level)

    def check_self(self):
        print("You deal %s damage" % self.attack_amt)
        if self.armor == leather_armor:
            print("You have this armor: Leather armor")
        else:
            print("You have this armor: %s" % self.armor)
        print("You have %s defence" % self.defence)
        print("You have %s health" % self.health)
        print("You have %s gold" % self.total_gold)
        print("You are level %s" % self.level)
        print("You are %s exp away from leveling up" % (self.exp_to_level_up - self.exp))
        if self.weapon == stick:
            print("Your best weapon is a stick")
        else:
            print("Your best weapon is a/an %s" % self.weapon)
        print("This is in your inventory: %s" % ", ".join(self.inventory))
        self.using_health_potion()

    def run_command(self):
        while not self.did_command:
            if self.playing:
                command = input(">")
                if command in self.short_directions:
                    pos = self.short_directions.index(command)
                    command = self.directions[pos]
                if command.lower() in ["q", "quit", "exit"]:
                    self.playing = False
                elif self.burning:
                    self.burn_to_death()
                elif command.lower() == "i":
                    self.check_self()
                elif command in self.directions:
                    try:
                        room_name = getattr(self.current_node, command)
                        self.current_node = globals()[room_name]
                        self.did_command = True
                    except KeyError:
                        print("You can't go that way")
                else:
                    print("Command not recognized")
        self.did_command = False

    def die(self):
        print("You died")
        print("Try again")
        self.playing = False
        self.health = 0
        self.current_node = room


choice1 = input("What would you like your name to be?")

you = Person(choice1, 5, stick, leather_armor)

# Monsters
eldrazi_scout = Monster("Eldrazi Scout", 1, 1, 5, 5, Armor("Monster Armor", 0, 0), Sword("Claw", 1, None))
eldrazi_scion = Monster("Eldrazi Scion", 3, 2, 5, 5, Armor("Monster Armor", 0, 0), Sword("Claw", 1, None))
crab = Monster("Crab", 30, 5, 5, 5, Armor("Monster Armor", 5, None), Sword("Pincer", 1, None))
krayt_dragon = Monster("Krayt Dragon", 20, 15, 10, 10, Armor("Monster Armor", 10, None), Sword("Claw", 1, None))
lylek = Monster("Lylek", 20, 18, 20, 12, Armor("Skin", 12, 0), Weapon("Leg", 13, 0))

sidewinder_naga = Monster("Sidewinder Naga", 5, 4, 10, 5, Armor("Monster Armor", 3, None), Sword("Dagger", 1, None))
hydra = Monster("Hydra", 20, 1 * heads, 15, 20, Armor("Monster Armor", 4, None), Sword("Claw", 1, None))

fire_elemental = Monster("Fire Elemental", 20, 5, 20, 20, Armor("Monster Armor", 5, None), Sword("Flames", 1, None))
volcano_hellion = Monster("Volcano Hellion", 15, 10, 15, 10, Armor("Monster Armor", 5, None), Sword("Flames", 1, None))
volcanic_dragon = Monster("Volcanic Dragon", 15, 15, 15, 15, Armor("Scales", 15, 0), Weapon("Fire breath", 15, 0))
godzilla = Monster("Godzilla", 50, 20, 40, 30, Armor("Skin", 15, 0), Weapon("Fire breath", 20, 0))

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
        if self.choice == self.shop_item1.name and you.total_gold >= self.shop_item1.cost:
            print("You bought a/an %s" % self.shop_item1.name)
            you.total_gold -= self.shop_item1.cost
            print("Now you have %s gold left" % you.total_gold)
            if self.shop_item1.name in you.armor_list:
                you.is_it_armor(self.shop_item1)
            if self.shop_item1.name in you.weapons_list:
                you.is_it_a_weapon(self.shop_item1)
            if self.shop_item1.name in you.health_potions_list:
                you.is_it_a_health_potion(self.shop_item1)
            else:
                you.inventory.append(self.shop_item1.name)

        if self.choice == self.shop_item2.name and you.total_gold >= self.shop_item2.cost:
            print("You bought a/an %s" % self.shop_item2.name)
            you.total_gold -= self.shop_item2.cost
            print("Now you have %s gold left" % you.total_gold)
            if self.shop_item2.name in you.armor_list:
                you.is_it_armor(self.shop_item2)
            if self.shop_item2.name in you.weapons_list:
                you.is_it_a_weapon(self.shop_item2)
            if self.shop_item2.name in you.health_potions_list:
                you.is_it_a_health_potion(self.shop_item2)
            else:
                you.inventory.append(self.shop_item2.name)

        if self.choice == self.shop_item3.name and you.total_gold >= self.shop_item3.cost:
            print("You bought a/an %s" % self.shop_item3.name)
            you.total_gold -= self.shop_item3.cost
            print("Now you have %s gold left" % you.total_gold)
            if self.shop_item3.name in you.armor_list:
                you.is_it_armor(self.shop_item3)
            if self.shop_item3.name in you.weapons_list:
                you.is_it_a_weapon(self.shop_item3)
            if self.shop_item3.name in you.health_potions_list:
                you.is_it_a_health_potion(self.shop_item3)
            else:
                you.inventory.append(self.shop_item3.name)

        if self.choice == self.shop_item4.name and you.total_gold >= self.shop_item4.cost:
            print("You bought a/an %s" % self.shop_item4.name)
            you.total_gold -= self.shop_item4.cost
            print("Now you have %s gold left" % you.total_gold)
            if self.shop_item4.name in you.armor_list:
                you.is_it_armor(self.shop_item4)
            if self.shop_item4.name in you.weapons_list:
                you.is_it_a_weapon(self.shop_item4)
            if self.shop_item4.name in you.health_potions_list:
                you.is_it_a_health_potion(self.shop_item4)
            else:
                you.inventory.append(self.shop_item4.name)

    def run_shop(self):
        print("There is a shop here")
        print("Would you like to enter it")
        self.stay_in_shop = "YES"
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

room = Room(None, None, None, None, None, None, None)

# Raven Gorge
spawn_point_raven_gorge = Room("Spawn Point Raven Gorge", "raven_gorge1", None,
                               None, None, None, None)
raven_gorge1 = Room("Raven Gorge 1", "raven_gorge2", "spawn_point_raven_gorge", None, None, None,
                    "There is an eldrazi scout north of you", True, banana_peel)
raven_gorge2 = Room("Raven Gorge 2", "raven_gorge3", "raven_gorge1", None, "raven_gorge2_left", None,
                    None, False, None, "", False, True, "Eldrazi Scout")
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
                                    "You are now in a valley with grass going out to your east and west")
sheltered_valley1 = Room("Sheltered Valley 1", "sheltered_valley2", "sheltered_valley7",
                         "spawn_point_sheltered_valley", None, None, "There is a dead body north of you")
sheltered_valley2 = Room("Sheltered Valley 2", "sheltered_valley3", "sheltered_valley1", None, None,
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
                         None, None)
sheltered_valley8 = Room("Sheltered Valley 8", "sheltered_valley7", "great_desert", None, None,
                         None, None)
great_desert = Room("Great Desert", "sheltered_valley8", None, None, None, None,
                    "You see a sign and it says \n You are in the great desert \n You are going to die", False, None,
                    "", False, False, "", False, 0, True, stone_sword, health_potion, filler, filler, "YES",
                    "spawn_point_great_desert")
lake = Room("Lake", None, "sheltered_valley5", None, None, None, "The trees open and in front of you is a vast lake",
            False, None,
            "", False, False, "", False, 0, True, stone_sword, health_potion, filler, filler, "YES",
            "spawn_point_lake")
mountain = Room("Mountain", None, "sheltered_valley3", None, None, None, "Ahead of you is a large mountain", False,
                None,
                "", False, False, "", False, 0, True, stone_sword, health_potion, filler, filler, "YES",
                "spawn_point_mountain")

# Mountain
spawn_point_mountain = Room("Spawn Point Mountain", None, None, "mountain6", "mountain1", None,
                            "You are in Spawn Point Mountain")
mountain1 = Room("Mountain 1", "mountain2", "spawn_point_mountain", None, None, None,
                 "You start climbing the right side of the mountain")
mountain2 = Room("Mountain 2", "mountain5", "mountain3", None, None, None,
                 "You start to get short of breath due to the altitude")
mountain3 = Room("Mountain 3", "mountain2", "mountain4", None, None, None, "You see a giant crab south of you")
mountain4 = Room("Mountain 4", "mountain3", None, "mountain_boss", None, None, None)
mountain5 = Room("Mountain 5", None, "mountain2", None, None, None, None)
mountain6 = Room("Mountain 6", None, None, None, None, None, None)
spawn_point_pit = Room("Spawn Point Pit", None, None, "pit2", "pit1", None,
                       "You see torches leading to the east and west")
pit1 = Room("Pit 1", None, None, None, None, None, None)
pit2 = Room("Pit 2", None, None, None, None, None, None)
mountain_boss = Room("Mountain Boss", None, None, "mountain_shop", "mountain4", None,
                     None)
mountain_shop = Room("Mountain Shop", None, None, None, "mountain_boss", None, None, False, None, "", False, False,
                     "", False, 0, True, iron_armor, pickaxe, good_health_potion, filler, "YES")

# Cave
spawn_point_cave = Room("Spawn Point Cave", None, None, "cave5", "cave1", None, "You are now in the cave")
cave1 = Room("Cave 1", "cave2", "cave_special", "spawn_point_cave", None, None, "The torches on the wall start to dim")
cave2 = Room("Cave 2", "cave3", "cave1", "cave_krayt", "cave4", None,
             "To your north you hear someone mumbling about a precious")
cave3 = Room("Cave 3", None, "cave2", None, None, None, None)
cave4 = Room("Cave 4", None, None, None, None, None, None)
cave5 = Room("Cave 5", "cave6", None, None, "spawn_point_cave", None, "The torches on the wall are brightening")
cave6 = Room("Cave 6", "cave_ritual", "cave5", None, "cave_krayt", None, "Some sort of ritual is going on north of you")
cave7 = Room("Cave 7", "cave_in", "cave_ritual", None, "cave_weapon", None, None)
cave_special = Room("Cave Special", None, None, None, None, None, None)
cave_krayt = Room("Cave Krayt", None, None, "cave6", "cave2", None, None)
cave_ritual = Room("Cave Ritual", "cave7", "cave6", None, None, None, "There is some sort of ritual here")
cave_in = Room("Cave In", None, None, None, None, None, "There is a cave in here and you can't pass")
cave_boss = Room("Cave Boss", "cave_shop", "cave_in", None, None, None, None, False, None, "", False, False, "", False,
                 0, False, None, None, None, None, "YES", "spawn_point_boss")
cave_shop = Room("Cave Shop", None, None, None, None, None, None, False, None, "", False, False, "", False,
                 0, True, diamond_sword, diamond_armor, good_health_potion, filler, "YES", "spawn_point_boss")

# Desert
spawn_point_great_desert = Room("Spawn Point Great Desert", None, None, "desert_sandstorm1", "desert1", None,
                                "You are in Spawn Point Mountain")
desert1 = Room("Desert 1", "desert_maze1", "spawn_point_great_desert", None, None, None,
               "Print you see a sign that says\nWelcome to the maze")
desert_maze1 = Room("Desert Maze", "desert_maze6", "desert1", None, "desert_maze2", None, "You are in the maze")
desert_maze2 = Room("Desert Maze", "desert_maze5", None, "desert_maze1", "desert_maze3", None, "You are in the maze")
desert_maze3 = Room("Desert Maze", "desert_maze4", None, "desert_maze2", None, None, "You are in the maze")
desert_maze4 = Room("Desert Maze", "desert_maze9", "desert_maze3", None, "desert_maze2", None, "You are in the maze")
desert_maze5 = Room("Desert Maze", "desert_maze8", "desert_maze5", "desert_maze6", "desert_maze4", None,
                    "You are in the maze")
desert_maze6 = Room("Desert Maze", "desert_maze7", "desert_maze1", None, "desert_maze5", None, "You are in the maze")
desert_maze7 = Room("Desert Maze", "desert_maze10", "desert_maze6", None, "desert_maze8", None, "You are in the maze")
desert_maze8 = Room("Desert Maze", "desert_maze11", "desert_maze5", "desert_maze7", "desert_maze9", None,
                    "You are in the maze")
desert_maze9 = Room("Desert Maze", "desert_maze12", "desert_maze4", "desert_maze8", None, None, "You are in the maze")

desert_maze10 = Room("Desert Maze", "desert_boss", "desert_maze7", None, "desert_maze11", None,
                     "You have left the maze")
desert_maze11 = Room("Desert Maze", "desert_boss", "desert_maze8", "desert_maze10", "desert_maze12", None,
                     "You have left the maze", False, None, "", False, False, "", True, 50)
desert_maze12 = Room("Desert Maze", "desert_boss", "desert_maze9", "desert_maze11", None, None,
                     "You have left the maze")

desert_sandstorm1 = Room("Desert Sandstorm", "desert_sandstorm6", "spawn_point_desert", "desert_sandstorm2", None,
                         None, "There is a raging sandstorm around you")
desert_sandstorm2 = Room("Desert Sandstorm", "desert_sandstorm5", None, "desert_sandstorm3", "desert_sandstorm1",
                         None, "There is a raging sandstorm around you")
desert_sandstorm3 = Room("Desert Sandstorm", "desert_sandstorm4", None, None, "desert_sandstorm2",
                         None, "There is a raging sandstorm around you")
desert_sandstorm4 = Room("Desert Sandstorm", "desert_sandstorm7", "desert_sandstorm3", None, "desert_sandstorm5",
                         None, "There is a raging sandstorm around you")
desert_sandstorm5 = Room("Desert Sandstorm", "desert_sandstorm8", "desert_sandstorm2", "desert_sandstorm4",
                         "desert_sandstorm6", None, "There is a raging sandstorm around you")
desert_sandstorm6 = Room("Desert Sandstorm", "desert_sandstorm9", "desert_sandstorm1", "desert_sandstorm5", None,
                         None, "There is a raging sandstorm around you")
desert_sandstorm7 = Room("Desert Sandstorm", "desert_sandstorm12", "desert_sandstorm4", None, "desert_sandstorm8",
                         None, "There is a raging sandstorm around you")
desert_sandstorm8 = Room("Desert Sandstorm", "desert_sandstorm11", "desert_sandstorm5", "desert_sandstorm7",
                         "desert_sandstorm9", None, "There is a raging sandstorm around you")
desert_sandstorm9 = Room("Desert Sandstorm", "desert_sandstorm10", "desert_sandstorm6", "desert_sandstorm8", None,
                         None, "There is a raging sandstorm around you")
desert_sandstorm10 = Room("Desert Sandstorm", "desert_boss", "desert_sandstorm9", "desert_sandstorm11", None,
                          None, "The sandstorm starts to clear up")
desert_sandstorm11 = Room("Desert Sandstorm", "desert_boss", "desert_sandstorm8", "desert_sandstorm12",
                          "desert_sandstorm10", None, "The sandstorm starts to clear up")
desert_sandstorm12 = Room("Desert Sandstorm", "desert_boss", "desert_sandstorm7", None, "desert_sandstorm11",
                          None, "The sandstorm starts to clear up", False, None, "", False, False, "", True, 50)
desert_boss = Room("Desert Boss", "desert_shop", "spawn_point_desert", None, None, None,
                   "Wow, what is this?\nOh wait it is the boss")
desert_shop = Room("Desert Shop", None, "desert_boss", None, None, None, None, False, None, "", False, False, "",
                   False, 0, True, iron_armor, good_health_potion, goron_tunic, filler, "YES")

# Volcano
spawn_point_volcano = Room("Spawn Point Volcano", "volcano1", "volcano_death", None, "volcano_myth", None,
                           "I wouldn't suggest going any direction other than north")
volcano1 = Room("Volcano 1", "volcano2", "spawn_point_volcano", None, None, None, None)
volcano2 = Room("Volcano 2", "volcano_river", "volcano1", None, "volcano_death2", None,
                "You see a large dragon to your west")
volcano3 = Room("Volcano 3", "volcano4", "volcano_river", "volcano3_right", "volcano_explosion", None, None)
volcano3_right = Room("Volcano 3 Right", None, None, None, "volcano3", None, None)
volcano4 = Room("Volcano 4", None, None, "volcano_boss2", "volcano_boss1", None, None)
volcano_death = Room("Volcano Death", None, None, None, None, None, None)
volcano_death2 = Room("Volcano Death 2", None, None, None, None, None, None)
volcano_myth = Room("Volcano Myth", None, None, None, None, None, None)
volcano_river = Room("Volcano River", "volcano3", "volcano2", None, None, None, None)
volcano_explosion = Room("Volcano Explosion", None, None, "volcano3", None, None, None)
volcano_boss1 = Room("Volcano Boss", "volcano_shop", None, "volcano4", None, None, None)
volcano_boss2 = Room("Volcano Boss", "volcano_shop", None, None, "volcano4", None, None)
volcano_shop = Room("Volcano Shop", None, None, "volcano_boss2", "volcano_boss1", None, None, False, None,
                    "", False, False, "", False, 0, True, diamond_sword, diamond_armor, good_health_potion, filler)


# Lake
spawn_point_lake = Room("Spawn Point Lake", None, None, None, None, None, "You are in Spawn Point Mountain")

# Jungle
spawn_point_jungle = Room(None, None, None, None, None, None, None)

# Boss Area
spawn_point_boss = Room("Spawn Point Boss", None, None, None, None, None, None)

you.current_node = spawn_point_raven_gorge

first_time = True
first_time1 = True
first_time2 = True
first_time3 = True
first_time4 = True

while you.playing:
    if first_time and you.playing:
        print("Welcome to Zendikar")
        print("This game will require skill and a bit of luck")
        print("Try checking your inventory by typing 'i'")
        print("Or type 'north' or 'n' to begin")
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
        desert_shop.stay_in_shop = "YES"
        print("Since this is your first time in a shop I will give you a hint")
        print("Buying an item multiple times, other than a health potion, gives you nothing extra or helpful")
        raven_gorge4.decision_room()
        raven_gorge4.run_shop()
        print("Would you like to go to the next area?")
        print("Once you leave this area you can not come back")
        choice11 = input("YES or NO")
        if choice11.upper() == "YES":
            you.current_node = spawn_point_sheltered_valley
        if choice11.upper() == "NO":
            you.run_command()
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
            break
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
        sheltered_valley7.decision_room()
        print("You hear a strange noise\nWould you like to investigate it?")
        choice12 = input("YES or NO")
        if choice12.upper() == "YES":
            print("You walk out into the tall grass and suddenly multiple swords are sticking out of your gut")
            you.die()
        if choice12.upper() == "NO":
            print("You stay put and nothing peculiar seems to happen")
            you.run_command()
    if you.current_node.name == "Sheltered Valley 8":
        sheltered_valley8.decision_room()
        print("It is getting dark\nWould you like to light a fire?")
        choice13 = input("YES or NO")
        if choice13.upper() == "YES":
            print("You light a fire and discover you are not the only one in this area")
            print("You feel a slight prick in your neck, collapse, and never wake up")
            you.die()
        if choice13.upper() == "NO":
            print("You don't light the fire and shortly after you fall asleep\nWhen you wake up nothing has changed")
            you.run_command()
    if you.current_node.name == "Great Desert":
        desert_shop.stay_in_shop = "YES"
        great_desert.decision_room()
        great_desert.run_shop()
        print("Would you like to go to the next area?")
        print("Once you leave this area you can not come back")
        choice11 = input("YES or NO")
        if choice11.upper() == "YES":
            you.current_node = spawn_point_great_desert
        if choice11.upper() == "NO":
            you.run_command()
    if you.current_node.name == "Lake":
        desert_shop.stay_in_shop = "YES"
        lake.decision_room()
        lake.run_shop()
        print("Would you like to go to the next area?")
        print("Once you leave this area you can not come back")
        choice11 = input("YES or NO")
        if choice11.upper() == "YES":
            you.current_node = spawn_point_lake
        if choice11.upper() == "NO":
            you.run_command()
    if you.current_node.name == "Mountain":
        desert_shop.stay_in_shop = "YES"
        mountain.decision_room()
        mountain.run_shop()
        print("Would you like to go to the next area?")
        print("Once you leave this area you can not come back")
        choice11 = input("YES or NO")
        if choice11.upper() == "YES":
            you.current_node = spawn_point_mountain
        if choice11.upper() == "NO":
            you.run_command()
    if you.current_node.name == "Spawn Point Mountain":
        spawn_point_mountain.run_room()
    if you.current_node.name == "Mountain 1":
        mountain1.run_room()
    if you.current_node.name == "Mountain 2":
        mountain2.run_room()
    if you.current_node.name == "Mountain 3":
        mountain3.run_room()
    if you.current_node.name == "Mountain 4":
        mountain4.decision_room()
        you.fight(crab)
        you.run_command()
    if you.current_node.name == "Mountain 5":
        mountain5.decision_room()
        print("You start to get very dizzy and you fall off the edge of the mountain")
        you.die()
    if you.current_node.name == "Mountain 6":
        mountain6.decision_room()
        fall_off_cliff = random.randint(1, 4)
        if fall_off_cliff == 1:
            print("You tripped over a rock which caused a chunk of rock to move away revealing a fall down to a pit")
            print("You also fell down and miraculously didn't die")
            you.current_node = spawn_point_pit
        else:
            print("You tripped over a rock and fell off the mountain")
            you.die()
    if you.current_node.name == "Spawn Point Pit":
        spawn_point_pit.run_room()
    if you.current_node.name == "Pit 1":
        pit1.decision_room()
        print("You fell down into another pit but this time you didn't survive")
        you.die()
    if you.current_node.name == "Pit 2":
        pit2.decision_room()
        print("Some kor grab you and pull you to your death")
        you.die()
    if you.current_node.name == "Mountain Boss":
        mountain_boss.decision_room()
        if first_time2:
            print("Well, time for a boss fight I guess")
            first_time2 = False
        you.fight(tuktuk)
        if first_time1:
            print("You slay TukTuk but something strange happens")
            print("His bodies starts to shake and out of it comes a stone golem")
            print("The golem says 'I am TukTuk Returned and you are going to die'")
            you.fight(tuktukreturned)
            first_time1 = False
        if you.playing:
            you.run_command()
    if you.current_node.name == "Mountain Shop":
        desert_shop.stay_in_shop = "YES"
        mountain_shop.decision_room()
        mountain_shop.run_shop()
        print("Would you like to go to the next area?")
        print("Once you leave this area you can not come back")
        choice11 = input("YES or NO")
        if choice11.upper() == "YES":
            you.current_node = spawn_point_cave
        if choice11.upper() == "NO":
            you.run_command()

    if you.current_node.name == "Spawn Point Cave":
        spawn_point_cave.run_room()
    if you.current_node.name == "Cave 1":
        cave1.run_room()
    if you.current_node.name == "Cave 2":
        cave2.run_room()
    if you.current_node.name == "Cave 3":
        cave3.decision_room()
        print("Gollum: Would you care to try my riddles?")
        choice2 = input("YES or NO")
        if choice2.upper() == "YES":
            alive = True
            print("Gollum: Here is the first riddle\nWhat has roots as nobody sees \nIs taller than trees, \nUp, up"
                  " it goes, \nAnd yet never grows")
            print("What is it?")
            if alive:
                choice3 = input(">")
                if choice3.upper() == "MOUNTAIN":
                    print("Gollum: You are correct \nTime for the next one")
                else:
                    print("Gollum: You are wrong. Time to die")
                    you.die()
                    alive = False
            if alive:
                print("Gollum: Here is the second one\nVoiceless it cries,\nWingless flutters,\nToothless bites,\n"
                      "Mouthless mutters")
                print("What is it?")
                choice4 = input(">")
                if choice4.upper() == "WIND":
                    print("You are correct")
                else:
                    print("Gollum: You are wrong. Time to die")
                    you.die()
                    alive = False
            if alive:
                print("Gollum: It cannot be seen, cannot be felt,\nCannot be heard, cannot be smelt\nIt lies"
                      "behind the stars and under hills,\nAnd empty holes it fills.\nIt comes first and follows"
                      "after,\nEnds life, kills laughter")
                print("What is it?")
                choice5 = input(">")
                if choice5.upper() == "DARK":
                    print("Gollum: You are correct")
                else:
                    print("Gollum: You are wrong time to die")
                    you.die()
                    alive = False
            if alive:
                print("Gollum: Alive without breath,\nAs cold as death,\nNever thirsty, ever drinking,\n"
                      "All in mail never clinking")
                print("What is it")
                choice6 = input(">")
                if choice6.upper() == "FISH":
                    print("Gollum: You are correct")
                else:
                    print("Gollum: You are wrong time to die")
                    you.die()
                    alive = False
            if alive:
                print("Gollum: This thing all devours:\nBirds, beasts, trees, flowers;\nGnaws iron, bites steel;\n"
                      "Grinds hard stones to meal;\nSlays king, ruins town,\nAnd beats high mountain down")
                print("What is it?")
                choice7 = input(">")
                if choice7.upper() == "TIME":
                    print("Gollum: You are correct")
                else:
                    print("Gollum: You are wrong time to die")
                    you.die()
                    alive = False
            if alive:
                print("Suddenly a short humanoid with very hairy feet walks towards you")
                print("Hi my name is Bilbo")
                print("Here is my riddle for you")
                print("What is in my pocket?")
                choice8 = input(">")
                if choice8.upper() == "NOT A RING":
                    print("Bilbo: Wow. You are correct\nGood job")
                else:
                    print("Bilbo: You are wrong\nHave some fun gollum")
                    you.die()
                    alive = False
            if alive:
                you.run_command()
        if choice2.upper() == "NO":
            print("Gollum: How dare you\nTime to die")
            you.die()

    if you.current_node.name == "Cave 4":
        cave4.decision_room()
        print("Some orcs appear and they make quick work of you")
        you.die()
    if you.current_node.name == "Cave 5":
        cave5.run_room()
    if you.current_node.name == "Cave 6":
        cave6.run_room()
    if you.current_node.name == "Cave 7":
        cave7.decision_room()
        you.fight(lylek)
        you.run_command()
    if you.current_node.name == "Cave Special":
        cave_special.decision_room()
        print("You find Thanos here and using the power of the infinity stones he erases you from history")
        you.die()
    if you.current_node.name == "Cave Krayt":
        cave_krayt.decision_room()
        you.fight(krayt_dragon)
        you.run_command()
    if you.current_node.name == "Cave Ritual":
        cave_ritual.decision_room()
        print("What would you like to do?")
        choice_r = input("Try to SNEAK around the ritual or rush in and ATTACK")
        if choice_r.upper() == "SNEAK":
            print("You snuck around the ritual without anyone seeing you")
            you.run_command()
        else:
            print("You rushed into the ritual but a sudden wave of kor run at you")
            print("They tie you down and you become the sacrifice for the ritual")
            you.die()
    if you.current_node.name == "Cave In":
        cave_in.decision_room()
        if "Pickaxe" in you.inventory:
            print("You have the pickaxe")
            print("Would you like to use it")
            choice9 = input("YES or NO")
            if choice9.upper() == "YES":
                print("With ease you mined away the rocks in your path")
                cave_in.north = 'cave_boss'
            if choice9.upper() == "NO":
                print("You did not use the pickaxe")
        you.run_command()

    if you.current_node.name == "Cave Boss":
        cave_boss.decision_room()
        you.fight(knucklotec)
        you.run_command()
    if you.current_node.name == "Cave Shop":
        desert_shop.stay_in_shop = "YES"
        cave_shop.decision_room()
        cave_shop.run_shop()
        print("Would you like to go to the next area?")
        print("Once you leave this area you can not come back")
        choice11 = input("YES or NO")
        if choice11.upper() == "YES":
            you.current_node = spawn_point_boss
        if choice11.upper() == "NO":
            you.run_command()

    if you.current_node == spawn_point_great_desert:
        spawn_point_great_desert.run_room()
    if you.current_node == desert1:
        desert1.run_room()
    if you.current_node == desert_maze1:
        desert_maze1.run_room()
    if you.current_node == desert_maze2:
        desert_maze2.run_room()
    if you.current_node == desert_maze3:
        desert_maze3.run_room()
    if you.current_node == desert_maze4:
        desert_maze4.run_room()
    if you.current_node == desert_maze5:
        desert_maze5.run_room()
    if you.current_node == desert_maze6:
        desert_maze6.run_room()
    if you.current_node == desert_maze7:
        desert_maze7.run_room()
    if you.current_node == desert_maze8:
        desert_maze8.run_room()
    if you.current_node == desert_maze9:
        desert_maze9.run_room()
    if you.current_node == desert_maze10:
        desert_maze10.run_room()
    if you.current_node == desert_maze11:
        desert_maze11.run_room()
    if you.current_node == desert_maze12:
        desert_maze12.decision_room()
        you.fight(sidewinder_naga)
        you.run_command()

    if you.current_node == desert_sandstorm1:
        desert_sandstorm1.run_room()
    if you.current_node == desert_sandstorm2:
        desert_sandstorm2.run_room()
    if you.current_node == desert_sandstorm3:
        desert_sandstorm3.run_room()
    if you.current_node == desert_sandstorm4:
        desert_sandstorm4.run_room()
    if you.current_node == desert_sandstorm5:
        desert_sandstorm5.run_room()
    if you.current_node == desert_sandstorm6:
        desert_sandstorm6.run_room()
    if you.current_node == desert_sandstorm7:
        desert_sandstorm7.run_room()
    if you.current_node == desert_sandstorm8:
        desert_sandstorm8.run_room()
    if you.current_node == desert_sandstorm9:
        desert_sandstorm9.run_room()
    if you.current_node == desert_sandstorm10:
        desert_sandstorm10.run_room()
    if you.current_node == desert_sandstorm11:
        desert_sandstorm11.run_room()
    if you.current_node == desert_sandstorm12:
        desert_sandstorm12.decision_room()
        you.fight(hydra)
        you.run_command()

    if you.current_node == desert_boss:
        desert_boss.decision_room()
        you.fight(bowser)
        you.run_command()
    if you.current_node == desert_shop:
        desert_shop.stay_in_shop = "YES"
        desert_shop.decision_room()
        desert_shop.run_shop()
        print("Would you like to go to the next area?")
        print("Once you leave this area you can not come back")
        choice11 = input("YES or NO")
        if choice11.upper() == "YES":
            you.current_node = spawn_point_volcano
        if choice11.upper() == "NO":
            you.run_command()

    if you.current_node == spawn_point_volcano:
        spawn_point_volcano.run_room()
        you.burn_to_death()
    if you.current_node == volcano1:
        volcano1.run_room()
        if first_time3:
            you.burning = True
            first_time3 = False
        you.burn_to_death()
    if you.current_node == volcano2:
        volcano2.run_room()
        you.burn_to_death()
    if you.current_node == volcano_death2:
        volcano_death2.decision_room()
        print("A very large dragon is here and his breath roasts you alive")
        you.die()
        break
    if you.current_node == volcano3:
        volcano3.run_room()
        you.burn_to_death()
    if you.current_node == volcano3_right:
        volcano3_right.run_room()
        you.burn_to_death()
    if you.current_node == volcano4:
        volcano4.run_room()
        you.burn_to_death()
    if you.current_node == volcano_death:
        volcano_death.decision_room()
        print("You think you see a mountain but it is not a mountain")
        print("It starts slowly walking towards you and you see that it is ...")
        print()
        print()
        print()
        print("GODZILLA")
        print("He breaths fire and incinerates you instantly")
        you.die()
    if you.current_node == volcano_myth:
        volcano_myth.decision_room()
        print("You think you see a mountain but it is not a mountain")
        print("It turns around and based on it's crown and giant sword you know it is Surtur")
        print("Before you can react he raises his sword and plunges it through the ground where you stand")
        you.die()
    if you.current_node == volcano_river:
        rock_break = random.randint(1, 2)
        volcano_river.decision_room()
        if rock_break == 1:
            print("You walk across a narrow path across a river of lava")
        if rock_break == 2:
            print("As you are walking across a narrow path a rock breaks and you trip and fall into the lava")
            you.die()
        you.burn_to_death()
        you.run_command()
    if you.current_node == volcano_explosion:
        volcano_explosion.decision_room()
        explode = random.randint(1, 2)
        if explode == 1:
            print("You see a volcano to your west but it looks dormant")
        if explode == 2:
            print("You see a volcano to your west and it is definitely not dormant")
            print("It explodes and sends magma everywhere and you aren't able to dodge it in time")
            you.die()
        you.burn_to_death()
    if you.current_node == volcano_boss1:
        volcano_boss1.decision_room()
        you.burn_to_death()
    if you.current_node == volcano_boss2:
        volcano_boss2.decision_room()
        you.burn_to_death()
    if you.current_node == volcano_shop:
        volcano_shop.run_room()
        you.burn_to_death()

    if you.current_node == spawn_point_boss:
        print("Congratulations for making it this far here is 50 gold for your efforts")
        you.total_gold += 50
        print("Now you have %s gold" % you.total_gold)
        print("This is the last area of the game and lucky for you no instant death")
        print("So get ready for the fight of your life")
        spawn_point_boss.run_room()
