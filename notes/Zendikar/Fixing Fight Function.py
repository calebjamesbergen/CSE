class Weapon(object):
    def __init__(self, damage):
        self.damage = damage


class Armor(object):
    def __init__(self, armor):
        self.armor = armor


class Person(object):
    def __init__(self, health, weapon, armor):
        self.health = health
        self.name = "Hi"
        self.weapon = weapon
        self.attack_amt = weapon.damage
        self.armor = armor
        self.defence = armor.armor

    def take_damage(self, damage):
        if damage <= self.armor.armor:
            print("No damage is done because of some FABULOUS armor")
        else:
            self.health -= damage - self.armor.armor
            if self.health <= 0:
                self.health = 0
                print("%s has fallen" % self.name)
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.attack_amt)

    def fight(self, target):
        while target.health > 0 and self.health > 0:
            print("A %s appeared \nWould you like to attack it?" % target.name)
            choice = input("YES or NO")
            if choice.upper() == "YES":
                target.attack(self)
                self.attack(target)
            print("You defeated the %s" % target.name)
            if choice.upper() == "NO":
                pass


class Monster(object):
    def __init__(self, health, weapon, armor):
        self.health = health
        self.name = "Blah"
        self.weapon = weapon
        self.attack_amt = weapon.damage
        self.armor = armor
        self.defence = armor.armor

    def take_damage(self, damage):
        if damage <= self.armor.armor:
            print("No damage is done because of some FABULOUS armor")
        else:
            self.health -= damage - self.armor.armor
            if self.health <= 0:
                self.health = 0
                print("%s has fallen" % self.name)
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.attack_amt)


sword = Weapon(5)
armor1 = Armor(2)

you = Person(100000, Weapon(10), Armor(100))
blah = Monster(100, sword, armor1)

you.fight(blah)
