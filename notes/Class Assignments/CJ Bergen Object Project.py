class MagicCard(object):
    def __init__(self, max_toughness, attacked_toughness, damage, tapped, dead):
        self.max_toughness = max_toughness
        self.attacked_toughness = attacked_toughness
        self.damage = damage
        self.tapped = tapped
        self.dead = dead

    def attack(self, attacker_toughness, attacker_attack, attacker_dead):
        if not self.tapped and not self.dead:
            self.tapped = True
            print("You attacked")
            print("You did %s damage" % self.damage)
            print("You took %s damage" % attacker_attack)
            self.attacked_toughness -= attacker_attack
            print("Now you have %s toughness" % int(self.attacked_toughness))
            print("Your opponent has %s toughness" % int(attacker_toughness - self.damage))
            if self.attacked_toughness <= 0:
                self.dead = True
            if attacker_dead:
                print("You killed the other card")
                print("Good job")
            if self.dead:
                print("You died")
                print("HA!")

    def new_turn(self):
        print("Your turn started again")
        print("Your card untapped and regained all of its health")
        self.attacked_toughness = self.max_toughness
        self.tapped = False
        print("Your card has %s health and deals %s damage" % (self.max_toughness, self.damage))


eldrazi = MagicCard(3, 3, 2, False, False)
dragon = MagicCard(5, 5, 5, False, False)

eldrazi.attack(dragon.max_toughness, dragon.damage, dragon.dead)
eldrazi.new_turn()
print()
dragon.attack(eldrazi.max_toughness, eldrazi.damage, eldrazi.dead)
dragon.new_turn()
