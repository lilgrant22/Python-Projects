"""
Create winged_animal class as described in README
"""

from src.farm_animal import FarmAnimal


class WingedAnimal(FarmAnimal):

    def make_sound(self):
        return "flap, flap"

    def __init__(self, age):
        FarmAnimal.__init__(self, age)

    def __str__(self):
        return "{} {} {}".format(FarmAnimal.__str__(self), self.age, WingedAnimal.make_sound(self))

