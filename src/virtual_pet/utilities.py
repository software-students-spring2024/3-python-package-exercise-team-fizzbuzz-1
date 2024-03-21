"""Utilities"""
from typing import AnyStr, Union
from src.virtual_pet.pet import Pet, Species

def create_pet(name: AnyStr = "", species: Species = Species.NONE) -> Union[Pet,None]:
    """Creates a pet"""
    if not name or not species or species == Species.NONE:
        print('Name and species are required to create a pet')
        return None
    return Pet(name, species)
