"""
Create rooster class as described in README
"""

from src.chicken import Chicken


class Rooster(Chicken):

    def can_lay_eggs(self):
        return False

    def make_sound(self):
        return "flap, flap - cock-a-doodle doo!"

    def __init__(self, age):
        Chicken.__init__(self, age)

    def __str__(self):
        return "{} {} {}".format(Chicken.__str__(self), self.age, Rooster.make_sound(self))

    def __eq__(self, other):
        if type(other) == Chicken:
            return True
        if self.age == other.age:
            return True
        else:
            return False
