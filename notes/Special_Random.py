import random
# Non static methods you need the object
# Static methods you don't need the object


class RandomWiebe:
    @staticmethod
    def special_random():
        return random.randint(1, 100)


print(RandomWiebe.special_random())
