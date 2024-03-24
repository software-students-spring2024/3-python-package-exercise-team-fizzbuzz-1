"""Class allows for the creation of new species of pets"""
from typing import Dict, List, AnyStr

class Species:
    """Species class"""

    def __init__(self, name: AnyStr, drawings: Dict, allergies: List,
                 fav_exercises: List, talents: List) -> None:
        """Creates a Species"""
        self.name = name
        self.drawings = drawings
        self.allergies = allergies
        self.fav_exercises = fav_exercises
        self.talents = talents
