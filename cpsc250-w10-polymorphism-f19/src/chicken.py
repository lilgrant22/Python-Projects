"""
Create chicken class as described in README
"""

from src.winged_animal import WingedAnimal


class Chicken(WingedAnimal):

    def make_sound(self):
        return "flap, flap - cluck, cluck"

    def __init__(self, age):
        WingedAnimal.__init__(self, age)

    def __str__(self):
        return "{} {} {}".format(WingedAnimal.__str__(self), self.age, Chicken.make_sound(self))

    def __eq__(self, other):
        if type(other) == WingedAnimal:
            return True
        if self.age == other.age:
            return True
        else:
            return False
