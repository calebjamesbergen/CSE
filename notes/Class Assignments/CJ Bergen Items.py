class Item(object):
    def __init__(self, name, cost):
        self.cost = cost
        self.name = name

    def pick_up(self):
        print("You found a %s" % self.name)
        print("Would you like to pick it up")
        choice = input("YES or NO")
        if choice.upper() == "YES":
            you.inventory.append(self.name)
        if choice.upper() == "NO":
            pass


class Weapon(Item):
    def __init__(self, name, damage, cost):
        super(Weapon, self).__init__(name, cost)
        self.damage = damage


class Armor(Item):
    def __init__(self, name, defence, cost):
        super(Armor, self).__init__(name, cost)
        self.defence = defence


class Key(Item):
    def __init__(self, name, cost):
        super(Key, self).__init__(name, cost)


class Potion(Item):
    def __init__(self, name, cost):
        super(Potion, self).__init__(name, cost)

    def get_health_potion(self, name):
        if self.cost == self.cost:
            pass
        if name == "Health Potion":
            you.health_potions += 1
        if name == "Good Health Potion":
            you.good_health_potions += 1
        if name == "Health Potion":
            you.health_potions += 1


class Clothes(Item):
    def __init__(self, name, cost):
        super(Clothes, self).__init__(name, cost)

    def stop_burning(self):
        if self.cost == self.cost:
            pass
        if you.burning_to_death:
            you.burning_to_death = False


class Tools(Item):
    def __init__(self, name, cost, new_location, changed_location):
        super(Tools, self).__init__(name, cost)
        changed_location.paths.North = new_location


class Teleporter(Item):
    def __init__(self, name, cost):
        super(Teleporter, self).__init__(name, cost)


stick = Weapon("Stick", 1, 0)
key = Key("Bronze Key", None)

heads = 1


class Monster(object):
    def __init__(self, name, monster_health, monster_attack, monster_exp, monster_gold, did_you_beat_monster):
        self.name = name
        self.monster_health = monster_health
        self.monster_attack = monster_attack
        self.monster_exp = monster_exp
        self.monster_gold = monster_gold
        self.did_you_beat_monster = did_you_beat_monster


eldrazi_scout = Monster("Eldrazi Scout", 2, 1, 5, 5, False)
eldrazi_scion = Monster("Eldrazi Scion", 3, 2, 5, 5, False)
crab = Monster("Crab", 5, 3, 5, 5, False)
krayt_dragon = Monster("Krayt Dragon", 10, 5, 10, 10, False)
sidewinder_naga = Monster("Sidewinder Naga", 5, 4, 10, 5, False)
hydra = Monster("Hydra", 20, 1 * heads, 15, 20, False)
fire_elemental = Monster("Fire Elemental", 20, 5, 20, 20, False)
volcano_hellion = Monster("Volcano Hellion", 15, 10, 15, 10, False)


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
        self.total_health = self.health + self.health_from_level
        self.total_damage = self.damage + self.damage_from_level
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
        self.good_health_potions = 1
        self.great_health_potions = 1
        self.did_command = False
        self.did_attack = False
        self.turns_to_burn_to_death = 3
        self.burning_to_death = False

    def is_it_a_health_potion(self, health_potion):
        if health_potion == self.health_potions_list[0]:
            self.health_potions += 1
        if health_potion == self.health_potions_list[1]:
            self.good_health_potions += 1
        if health_potion == self.health_potions_list[2]:
            self.great_health_potions += 1

    def burn_to_death(self):
        if self.burning_to_death:
            self.turns_to_burn_to_death -= 1
            print("You are %s turns away from burning to death" % self.turns_to_burn_to_death)

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
        print("Your inventory includes: %s" % "".join(self.inventory))
        self.using_health_potion()
        self.using_health_potion()
        self.using_health_potion()

    def command(self):
        while not self.did_command:
            if self.playing:
                command = input(">")
                if command.lower() in ["q", "quit", "exit"]:
                    self.playing = False
                elif command.lower() == "i":
                    self.check_self()
                elif command in self.directions:
                    try:
                        room_name = getattr(self.current_node, command)
                        self.current_node = globals()[room_name]
                        self.did_command = True
                        you.burn_to_death()
                    except KeyError:
                        print("You can't go that way")
                else:
                    print("Command not recognized")
                if command == "s":
                    room_name = "spawn_point_sheltered_valley"
                    self.current_node = globals()[room_name]
                    self.total_gold += 100
                    self.weapon = "Wood Sword"
                    self.damage = 3
                    self.armor = "Copper Armor"
                    self.defence = 3
                    self.health = 10
        self.did_command = False

    def die(self):
        print("You died")
        print("Try again")
        self.playing = False

    def fight(self, name, health, attack, exp, gold, did_you_beat_it):
        print("What would you like to do")
        fighting = ""
        while not self.did_attack:
            fighting = input("ATTACK or FLEE")
            if fighting in ["ATTACK", "attack", "Attack", "FLEE", "flee", "Flee"]:
                self.did_attack = True
        if fighting in ["ATTACK", "attack", "Attack"]:
            while health > 0 and not did_you_beat_it and self.get_health() > 0:
                self.did_attack = True
                print("The %s attacked you and you took %s damage" % (name, you.damage_you_take(attack)))
                self.health -= you.damage_you_take(attack)
                print("Now you have %s health" % self.get_health())
                print("You swung your %s at the %s" % (self.weapon, name))
                print("The %s took %s damage" % (name, self.get_attack()))
                health -= you.get_attack()
                if health >= 0:
                    print("Now the %s has %s health left" % (name, health))
                if health < 0:
                    print("Now the %s has 0 health left" % name)
            if you.health + you.health_from_level > 0:
                print("You defeated the %s" % name)
                print("You got %s gold" % gold)
                self.total_gold += gold
                print("Now you have %s gold" % self.total_gold)
                self.exp += exp
                print("You got %s exp" % exp)
                print("Now you have %s exp" % self.exp)
                self.level_up()
                eldrazi_scout.did_you_beat_monster = True
            elif you.health + you.health_from_level <= 0:
                self.die()
        if fighting in ["FLEE", "flee"]:
            self.die()
        self.did_attack = False


you = Person()
