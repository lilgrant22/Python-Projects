"""
Create ruminant class as described in README
"""

from src.farm_animal import FarmAnimal


class Ruminant(FarmAnimal):

    def make_sound(self):
        return "burp"

    def __init__(self, age):
        FarmAnimal.__init__(self, age)

    def __str__(self):
        return "{} {} {}".format(FarmAnimal.__str__(self), self.age, Ruminant.make_sound(self))
