from enum import Enum
from typing import List, Dict, AnyStr, Union
from termcolor import colored, COLORS

class Species(Enum):
    NONE = -1
    CAT = 0
    DOG = 1
    HAMSTER = 2
    ROCK = 3

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
        self.hunger = 0
        self.happiness = 10
        self.boredom = 0
        self.thirst = 0
        self.species = species
        self.talent_level = 0
        self.talents = []
        self.color = 'white'
        self.dead = False
        self.sleepiness = 0

    def get_species_name(self) -> AnyStr:
        return self.species.name.lower()

    def feed(self, numFood: int) -> bool:
    
        for i in range(numFood):
            if self.hunger > 0:
                self.hunger -= 1
                return True
            else:
                print(f"{self.name} is not hungry!!")
                return False

    def exercise(self, duration: int) -> bool:
        exercised = False
        for i in range(duration):
            if self.hunger < 10: 
                self.hunger += 1
                exercised = True
            else:
                print(f"{self.name} is too hungry to exercise!!")
            if self.boredom > 0:
                self.boredom -= 1
            if self.happiness < 10:
                self.happiness += 1
        return exercised
    
    def display(self):
        state = None
        if self.dead:
            state = 'dead'
        elif self.happiness < 5:
            state = 'unhappy'
        elif self.sleepiness > 5:
            state = 'sleepy'
        else:
            state = 'normal'
        print(colored(Pet.drawings[self.get_species_name()][state], self.color))

    def groom(self, color: AnyStr) -> bool:
        if color in COLORS:
            self.color = color
            return True
        else:
            print('Invalid color')
            return False
            

def create_pet(name: AnyStr = "", species: Species = Species.NONE) -> Union[Pet,None]:
        if name == "" or species == Species.NONE:
            print('Name and species are required to create a pet')
            return None
        return Pet(name, species)