class Item(object):
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


class Weapon(Item):
    def __init__(self, name, damage, cost):
        super(Weapon, self).__init__(name, cost)
        self.cost = cost
        self.damage = damage


class Armor(Item):
    def __init__(self, name, defence, cost):
        super(Armor, self).__init__(name, cost)
        self.defence = defence
        self.cost = cost


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        if damage < self.armor.defence:
            print("No damage is done because of some FABULOUS armor!")
        else:
            self.health -= damage - self.armor.defence
            if self.health < 0:
                self.health = 0
                print("%s has fallen" % self.name)
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


# Items
sword = Weapon("Sword", 10, None)
canoe = Weapon("Canoe", 84, None)
wiebe_armor = Armor("Armor of the Gods", 100000000000000000, None)

# Characters
orc = Character("Orc", 100, sword, Armor("Generic Armor", 2, None))
wiebe = Character("Wiebe", 100000000000, canoe, wiebe_armor)

orc.attack(wiebe)
wiebe.attack(orc)
wiebe.attack(orc)
