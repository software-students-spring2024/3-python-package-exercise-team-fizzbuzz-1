"""Default weapons included in the package"""
from virtual_pet.weapons import Weapon

GUN = Weapon(
    name = 'gun',
    sound = 'bang bang',
    kills = ['cat','dog','hamster']
)