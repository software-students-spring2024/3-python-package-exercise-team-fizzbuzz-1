"""Defines the pet class"""

from enum import Enum
from typing import AnyStr
from termcolor import colored, COLORS

class Species(Enum):
    """Enum representing possible species"""

    NONE = 0
    CAT = 1
    DOG = 2
    HAMSTER = 3
    ROCK = 4

messages = {
    'create': [
        'Created cat',
        'Created dog',
        'Created hamster',
        'Created rock',
    ],
    'feed': [
        'Meowlicious',
        'Wooftastic',
        'Squeak...',
        '...'
    ],
    'exercise': [

    ]
}

class Pet:
    """Class representing a pet"""

    drawings = {
        'cat': {
            'normal': '/\\__/\\\n(=\'X\'=)\n(")_(")_/',
            'unhappy': '/\\__/\\\n(=>X<=)\n(")_(")_/',
            'tired': '/\\__/\\\n(=~X~=)\n(")_(")_/',
            'dead': '/\\__/\\\n(=xXx=)\n(")_(")_/'
        },
        'dog': {
            'normal': ' _______\n(| , , |)\n ( (Y) )\n (")_(")',
            'unhappy': ' _______\n(| > < |)\n ( (Y) )\n (")_(")',
            'tired': ' _______\n(| ~ ~ |)\n ( (Y) )\n (")_(")',
            'dead': ' _______\n(| x x |)\n ( (Y) )\n (")_(")'
        },
        'hamster': {
            'normal': ' o-----o\n( \'(X)\' )\nc(")_(")',
            'unhappy': ' o-----o\n( >(X)< )\nc(")_(")',
            'tired': ' o-----o\n( ~(X)~ )\nc(")_(")',
            'dead': ' o-----o\n( x(X)x )\nc(")_(")',
        },
        'rock': {
            'normal': '  ____\n |    \\\n /     \\\n|      /\n \\____/',
            'unhappy': '  ____\n |    \\\n /     \\\n|      /\n \\____/',
            'tired': '  ____\n |    \\\n /     \\\n|      /\n \\____/',
            'dead': '  ____\n |    \\\n /     \\\n|      /\n \\____/',
        }
    }


    def __init__(self, name: AnyStr, species: AnyStr) -> None:
        self.name = name
        self.species = species
        self.talents = {}
        self.color = 'white'
        self.status = {
            'hunger': 0,
            'happiness' : 10,
            'boredom': 0,
            'thirst': 0,
            'sleepiness' : 0
        }
        self.dead = False

    def get_species_name(self) -> AnyStr:
        """Returns lower case species name of the pet"""
        return self.species.name.lower()

    def feed(self, num_food: int) -> bool:
        """Feeds the pet if there the hunger bar allows. Returns True if managed to feed
        False otherwise"""
        fed = False
        for _ in range(num_food):
            if self.status['hunger'] > 0:
                self.status['hunger'] -= 1
                fed = True
            else:
                print(f"{self.name} is not hungry!!")
        return fed

    def exercise(self, duration: int) -> bool:
        """Exercises the pet if the hunger bar allows. Returns True if the
        pet exercised and false otherwise"""
        exercised = False
        for _ in range(duration):
            if self.status['hunger'] < 10:
                self.status['hunger'] += 1
                exercised = True
                if self.status['boredom'] > 0:
                    self.status['boredom'] -= 1
                if self.status['happiness'] < 10:
                    self.status['happiness'] += 1
            else:
                print(f"{self.name} is too hungry to exercise!!")
        return exercised

    def display(self):
        """Displays the pet along with their status on the terminal"""
        state = None
        if self.dead:
            state = 'dead'
        elif self.status['happiness'] < 5:
            state = 'unhappy'
        elif self.status['sleepiness'] > 5:
            state = 'sleepy'
        else:
            state = 'normal'
        print(colored(Pet.drawings[self.get_species_name()][state], self.color))

    def groom(self, color: AnyStr) -> bool:
        """Changes the appearance of the pet (currently just dyes hair)"""
        if color in COLORS:
            self.color = color
            return True
        print('Invalid color')
        return False
