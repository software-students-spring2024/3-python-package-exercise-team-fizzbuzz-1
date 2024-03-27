# Example file showcasing how to interact with virtual_pet methods and functions

from typing import AnyStr, Union, Dict, List
from os import system
from virtual_pet.pet import Pet
from virtual_pet.species import Species
from virtual_pet.weapons import Weapon
from virtual_pet.default_species import CAT, DOG, HAMSTER, ROCK
from virtual_pet.default_weapons import GUN, CHOCOLATE_CAKE, PEANUT_BUTTER
from virtual_pet.utilities import create_pet, create_weapon, play_game, manage_pet

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
""" Use of functions from utilities.py """

# start main game loop
play_game()

# create instantiation of class Pet and return object to variable pet
pet = create_pet(name="Fluffy", species=CAT)

# create instantiation of class Weapon and return object to variable weapon
# weapon of name Bazooka only kills cats and hamsters and makes sound "BOOOM"
weapon = create_weapon(name="Bazooka",kill_list=[CAT.species,HAMSTER.species],sound="BOOOM")

# called by play_game(), provides users with options to interact with selected pet 
manage_pet(pet)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
""" Use of functions from pet.py """
""" These functions are called by manage_pet() """

# returns the name of pet's species
pet_species_name = pet.get_species_name()

# feed pet with chicken if hunger bar allows and if pet is alive, returns true if pet is fed with no issues. Returns false otherwise
pet.feed("Chicken")

# Displays the pet along with their status on terminal
pet.display()

# Changes the appearance of pet by dying its hair red. Returns true if successful (color is defined) and false otherwise
pet.dye("red")

# puts the pet to sleep this turn if possible
pet.sleep()

# Does nothing and pseudorandomly changes pet's status, possibly killing them if thresholds for survival are tested
# returns True if any of the pet's status metrics change, False otherwise
pet.do_nothing()

# Kill pet with weapon determined earlier (this will kill pet as weapon was initialized to kill cats)
# Returns true if kill successful, False otherwise
pet.kill(weapon) # alternatively, choose weapon from default_weapons, like GUN
