"""
Create goat class as described in README
"""

from src.ruminant import Ruminant


class Goat(Ruminant):

    def can_lay_eggs(self):
        return False

    def make_sound(self):
        return "burp - baah"

    def __init__(self, age):
        Ruminant.__init__(self, age)

    def __str__(self):
        return "{} {} {}".format(Ruminant.__str__(self), self.age, Goat.make_sound(self))

    def __eq__(self, other):
        if type(other) == Ruminant:
            return True
        if self.age == other.age:
            return True
        else:
            return False
