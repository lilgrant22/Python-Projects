from src.farm_animal import FarmAnimal
from src.hen import Hen
from src.rooster import Rooster
from src.duck import Duck
from src.goat import Goat
from src.cow import Cow
import random

def get_barnyard():
    """
    Return a list of animals as described in README
    :return : list of animal instances
    """

    animals = [Hen(0.25), Hen(0.6), Hen(1.0), Hen(8.0), Rooster(0.25), Rooster(0.6), Rooster(1.0), Duck(3.0), Cow(2.2), Goat(1.3)]

    return animals

def get_layers(animals):
    """
    Given list of animals, return ones that can lay eggs
    :param animals: list of animal instances
    :return : list of "layers"
    """
    for i in animals:
        if type(i) == Hen and type(i) == Duck:
            animals = [i]

    return animals

def get_roosters(animals):
    """
    Given list of animals, return ones that are roosters
    :param animals: list of animal instances
    :return : list of rooster instances
    """
    for i in animals:
        if type(i) == Rooster:
            animals = [i]

    return animals

def listen(animals):
    """
    Given list of animals, return list of sounds they make
    :param animals: list of animal instances
    :return : list of sounds
    """
    for i in animals:
        return i.make_sound()
    
if __name__ == '__main__':

    animals = get_barnyard()
    print("All animals:",[str(ani) for ani in animals])
    print(" listen: ",listen(animals))
    print(" Laying hens:", [str(ani) for ani in get_layers(animals)])
    print(" Roosters: ",[str(ani) for ani in get_roosters(animals)])
