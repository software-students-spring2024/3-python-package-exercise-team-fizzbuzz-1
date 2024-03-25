"""Defines the pet class"""

# from enum import Enum
from typing import AnyStr
from termcolor import colored, COLORS
from virtual_pet.species import Species
from virtual_pet.weapons import Weapon

class Pet:
    """Class representing a pet"""

    def __init__(self, name: AnyStr, species: Species) -> None:
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
    
    def die(self) -> bool:
        """Kills the pet"""
        if self.species.immortal:
            print('...')
            return False
        self.status = dict.fromkeys(self.status, 0)
        self.dead = True
        return True

    def feed(self, food: AnyStr = "") -> bool:
        """Feeds the pet if there the hunger bar allows. Returns True if managed to feed
        False otherwise"""

        if self.dead:
            print(self.name + " is dead...")
            print("Please stop trying...")
            self.display()
            return False

        if self.species.immortal:
            print('...')
            return True

        fed = False
        if food in self.species.allergies:
            self.die()
            print("Your pet is severely allergic to " + food + "...")
            print(self.name + " is dead :( Womp womp")
            return False
    
        num_food = 1
        if food in self.species.fav_food:
            num_food *= 2

        for _ in range(num_food):
            if self.status['hunger'] > 0:
                self.status['hunger'] -= 1
                fed = True
            elif not fed:
                print(f"{self.name} is not hungry!!")
            else:
                print(f"{self.name} is satisfied... :)")
        return fed

    def exercise(self, exercise_type: AnyStr) -> bool:
        """Exercises the pet if the hunger bar allows. Returns True if the
        pet exercised and false otherwise"""

        if self.dead:
            print(self.name + " is dead...")
            print("I don't think he has the energy to exercise...")
            self.display()
            return False
        
        if self.species.immortal:
            print('...')
            return True

        multiplier = 1
        if exercise_type in self.species.fav_exercises:
            multiplier *= 2

        duration = 1
        exercised = False
        for _ in range(duration):
            if self.status['hunger'] < 10:
                self.status['hunger'] += 1
                exercised = True
                if self.status['boredom'] > 0:
                    self.status['boredom'] -= 1 * multiplier if self.status['boredom'] - 1 * multiplier > 0 else 0
                if self.status['happiness'] < 10:
                    self.status['happiness'] += 1 * multiplier if self.status['happiness'] + 1 * multiplier < 10 else 10
            else:
                print(f"{self.name} is too hungry to exercise!!")
        return exercised

    def display(self, full: bool = False) -> None:
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
        print(colored(self.species.drawings[state], self.color))

        print(self.species.sound)
        for key in self.status.keys():
            print(key + ": ")
            for _ in range(self.status[key]):
                print(colored("―", "blue"), end= "")
            for _ in range(10 - self.status[key]):
                print("―", end= "")
            print()
        
        if full:
            print('Allergies:')
            print(self.species.allergies)
            print('Favorite foods:')
            print(self.species.fav_food)
            print('Favorite exercises')
            print(self.species.fav_exercises)
            print('Talents:')
            print(self.species.talents)

    def dye(self, color: AnyStr) -> bool:
        """Changes the appearance of the pet (currently just dyes hair)"""
        if color in COLORS:
            self.color = color
            return True
        if color == '':
            print("I don't really know what to do with that...")
            return False
        print(f'{color[0].upper()}{color[1:]} colored dye not available...')
        return False

    def kill(self, weapon: Weapon) -> bool:
        """ Kill the pet with weapon of choice. Return True if killing successful. Return False otherwise"""
        # FIRAS
        pass

    def do_nothing(self) -> bool:
        # FIRAS
        pass