"""
Create farm_animal class as described in README
"""


class FarmAnimal:

    def __init__(self, age):
        self.age = age

    def __str__(self):
        return "".format(type(FarmAnimal), self.age)

    def make_sound(self):
        return ""
