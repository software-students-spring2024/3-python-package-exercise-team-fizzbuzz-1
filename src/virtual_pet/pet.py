"""Defines the pet class"""

# from enum import Enum
from typing import AnyStr
from termcolor import colored, COLORS
from virtual_pet.species import Species
from virtual_pet.weapons import Weapon
import random

class Pet:
    """Class representing a pet, containing all the necessary methods to interact with the pet"""

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
        """Feeds the pet if the hunger bar allows. Returns True if managed to feed
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

        if self.dead:
            print(self.name + " is dead...")
            print("Why are you trying to kill " + self.name + " again, you cruel-hearted scoundrel? Your malice stains even the darkest shadows.")
            self.display()
            return False

        elif (weapon.kills(self.species) == True):
            self.die()

            random_insults = ['vile miscreant, your depravity stains the very air we breathe.',
            'sinister fiend, your malevolent deeds darken the souls of those around you.', 
            'wicked villain, your cruelty leaves scars on the hearts of the innocent.',
            'despicable tyrant, your callousness knows no mercy.',
            'malevolent demon, your actions betray a soul blacker than the abyss.',
            'detestable savage, your ruthlessness taints every corner you touch.',
            'spiteful knave, your malicious intent poisons the well of goodwill.'
            ]
            random_insult = random.choice(random_insults)

            print(weapon.sound)
            print("You have killed " + self.name + ".." + " with " + weapon.name + " You " + random_insult)

            return True
            
        else:
            random_attacks = ['May you be blasted for your evil',
            'May you face divine retribution for your wicked deeds.',
            'May you be condemned for the darkness you bring into the world.',
            'May the consequences of your evil actions haunt you relentlessly.',
            "May you be held accountable for the suffering you've attempted to cause",
            "May the light of truth expose your malevolence, and may justice prevail."
            ]
            random_attack = random.choice(random_attacks)

            print("You have failed at killing " + self.name + ".." + random_attack)

            return False

    def do_nothing(self) -> bool:
        """ Does nothing and pseudorandomly changes pet's status, possibly killing them if thresholds for survival are tested """

        if self.dead:
            print(self.name + " is dead...")
            print("All they can do is absolutely nothing.")
            self.display()
            return False

        if self.species.immortal:
            print('...')
            return True
        
        changed = False

        if(self.status['hunger'] >= 0):
            hunger_addition=random.randint(0, 2)
            self.status['hunger']+=hunger_addition
            if(self.status['hunger'] > 10):
                print(self.name + " starved to death! Well done taking care of them..")
                self.die()
            changed=True
        
        if(self.status['happiness'] >= 0):
            happiness_subtraction=random.randint(0, 2)
            self.status['happiness']-=happiness_subtraction
            if(self.status['happiness'] < 0):
                print(self.name + " got depressed and killed itself. You're such a great parent..")
                self.die()
            changed=True
        
        if(self.status['boredom'] >= 0):
            boredom_addition = random.randint(0, 2)
            self.status['boredom']+=boredom_addition
            if(self.status['boredom'] > 10):
                print(self.name + " got bored to death! If only you had showed them a little more attention..")
                self.die()
            changed=True
        
        if(self.status['thirst'] >= 0):
            thirst_addition = random.randint(0, 2)
            self.status['thirst']+=thirst_addition
            if(self.status['thirst'] > 10):
                print(self.name + " died out of dehydration! If only you hadn't hogged up all the water..")
                self.die()
            changed=True
        
        if(self.status['sleepiness'] >= 0):
            sleepiness_addition = random.randint(0, 2)
            self.status['sleepiness']+=sleepiness_addition
            if(self.status['sleepiness'] > 10):
                print(self.name + " died of insomnia. If only you had tucked them into bed..")
                self.die()
            changed=True
        
        return changed



