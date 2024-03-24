"""Utilities"""
from typing import AnyStr, Union, Dict, List
from virtual_pet.pet import Pet
from virtual_pet.species import Species
# from virtual_pet.default_species import CAT, DOG, HAMSTER, ROCK

def create_species(name: AnyStr, drawings: Dict, allergies: List, fav_exercises: List, talents: List) -> Union[Species, None]:
    """Creates a species after data validation"""
    if drawings.keys() < {'normal', 'unhappy', 'mad', 'dead'}:
        print("Missing drawings:\n Please ensure {'normal', 'unhappy', 'mad', 'dead'} are in the list of drawings")
        return None
    return Species(name, drawings, allergies, fav_exercises, talents)

def create_pet(name: AnyStr = "", species: Species = None) -> Union[Pet,None]:
    """Creates a pet after data validation"""
    if not name or not isinstance(species, Species):
        print('Name and species are required to create a pet')
        return None
    return Pet(name, species)
