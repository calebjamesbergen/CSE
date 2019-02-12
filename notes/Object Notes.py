# 3 different relationships
# is a relationship # a tesla is a car
# has a relationship # a car has a engine
# can # a car can drive


class Laptop(object):  # first letter of name of object has to be capitalized,
    # Things that a laptop has
    # Everything in this list should be relevant to the program
    def __init__(self, screen_resolution, extra_space, color,):
        self.processor = "Intel i5"
        self.screen_resolution = screen_resolution
        self.battery_left = 100
        self.space_left = extra_space
        self.color = color
        self.os = "Graham cracker"

    def charge(self, time):
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


my_computer = Laptop("1920x1080", 10000, "Black")
your_computer = Laptop("10, 10", 0, "Orange")
wiebe_computer = Laptop("900000000000000x90000000000000", 99999999999999999999, "Awesome")
