# 3 different relationships
# is a relationship # a tesla is a car
# has a relationship # a car has a engine
# can # a car can drive


class Laptop(object):  # first letter of name of object has to be capitalized,
    # Things that a laptop has
    # Everything in this list should be relevant to the program
    def __init__(self, screen_resolution, extra_space=1000, color="Cobalt"):  # def __init__ is a constructor
        self.processor = "Intel i5"
        self.screen_resolution = screen_resolution
        self.battery_left = 100
        self.space_left = extra_space
        self.color = color
        self.os = "Graham cracker"
        self.functioning = True

    def charge(self, time):
        if self.functioning:
            # Computer is already charged
            if self.battery_left >= 100:
                print("The computer is already charged.")
                return

            self.battery_left += time  # This adds to the battery life
            # Computer is mostly charged
            if self.battery_left > 100:
                print("The computer quckly charges.")
                self.battery_left = 100

            # Computer is not charged at all
            else:
                print("The computer is now at %d%%" % self.battery_left)
        else:
            print("It's broken. Good job.")

    def smash(self):
        self.functioning = False
        print("I took the laptop...")
        print()
        print()
        print()
        print("...AND I THREW IT ON THE GROUND!!!")
        print("I was walkin' through the city streets And a man walks up to me and hands me the latest energy drink")
        print("Run faster, jump higher")
        print("Man, I'm not gonna let you poison me")
        print("I threw it on the ground")
        print("You must think I'm a joke")
        print("I ain't gonna be part of your system")
        print("Man! Pump that garbage in another man's veins")
        print("I walk up to my favorite hot dog stand. The guy says you come here all the time.")
        print("Here's one for free. Man. What I look like? A charity case? I took it and THREW IT ON THE GROUND!!!")
        print("At the farmers market with my so called girlfriend")
        print("She hands me her phone. Says it's my dad. Man I'm not stupid")
        print("I THREW IT ON THE GROUND!!! My dad's not a phone... duh")
        print("Some poser walks up to me at a birthday party, hands me a piece of cake"
              "What do you want me to do with it? Eat it? Happy birthday to the ground")
        print("I threw the rest of the the cake too. Welcome to the real world donkey")
        print("So many things to throw on the ground")
        print("Like this, and this, and that the the this")
        print("I'M AN ADULT!!!")
        print("Some Hollywood posers wanted to give me their autograph ... GROUND!!!")
        print("The posers got up, turns out they had a tazer, and they tazed me in the butt hole")
        print("I fell on the ground but the phonies didn't let up")
        print("Tazing on my butt hole over and over")
        print("I was screaming, squirming, my butt hole was on fire")
        print("The moral of the story is, you can't trust the system")
        print("Man")

    def un_smash(self):
        self.functioning = True
        print("You ran so fast you went back in time and un-threw your computer on the ground")
        print("But in the process you killed yourself by going too fast")
        print("Good job")

    def use(self, time):
        self.battery_left -= time
        print("You used the laptop for %s minutes" % time)


my_computer = Laptop("1920x1080", 10000, "Black")
your_computer = Laptop("10, 10", 0, "Orange")
wiebe_computer = Laptop("900000000000000x90000000000000", 99999999999999999999, "Awesome")
default_computer = Laptop("1920x1080")

my_computer.use(60)
my_computer.charge(20)
my_computer.charge(1000)
my_computer.smash()
my_computer.charge(20)
my_computer.un_smash()

your_computer.charge(20)

# Need a constructor
# 5 fields
# 2 methods

print(Special_Random.RandomWiebe.special_random())
