"""Default weapons included in the package"""
from virtual_pet.weapons import Weapon

GUN = Weapon(
    name = 'gun',
    sound = 'bang bang',
    kills = ['cat','dog','hamster']
)

CHOCOLATE_CAKE = Weapon(
    name = 'chocolate cake',
    sound = 'crunch',
    kills = ['dog', 'cat']
)

PEANUT_BUTTER = Weapon(
    name = 'peanut butter',
    sound = 'squish',
    kills = ['hamster']
)