"""Example file to demonstrat the functionality of this package"""
from virtual_pet.utilities import create_pet
from virtual_pet.default_species import CAT, DOG, HAMSTER, ROCK
from virtual_pet.default_weapons import GUN, CHOCOLATE_CAKE, PEANUT_BUTTER
from os import system

print()
print()
print("This will serve as a walkthrough of the various functions of this package.")
print("Click any button when you'd like to progress to the next slide of the walkthrough.")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=")

input('')
system('clear')

pets = []
print('Possible Actions:')
print('\t1 - Create pet')
if len(pets):
    print(f'\t2 - Manage pets ({len(pets)} avaiable)')
    print('\t3 - Exit')
else:
    print('\t2 - Exit')

input('')
print()
print("You select 1, creating a pet.")
print()

input('')
system('clear')

print('Choose species: ')
print('\t1 - Cat')
print('\t2 - Dog')
print('\t3 - Hamster')
print('\t4 - Rock')

input('')
print()
print("You select 1, creating a cat.")

input('')
system('clear')

print('Enter pet name: ')

input('')
print()
print("You name the cat, Fluffy")

input('')
system('clear')

pet = create_pet(name="Fluffy", species=CAT)
pets.append(pet)

input('')
print()
print("A display of the pet's information is printed automatically:")
input('')

pet.display(True)

input('')
system('clear')

print("We've successfully created a new pet. Now, let's navigate and manage this pet.")

input('')
system('clear')

print('Possible Actions:')
print('\t1 - Create pet')
if len(pets):
    print(f'\t2 - Manage pets ({len(pets)} avaiable)')
    print('\t3 - Exit')
else:
    print('\t2 - Exit')

input('')
print()
print("You select 2, to be able to manage a pet.")
print()

input('')
system('clear')

print('Choose pet:')
i = 1
for pet in pets:
    print(f'\t{i} - {pet.name} ({pet.get_species_name()})')
    i += 1

input('')
print()
print("You select 1, to be able to manage Fluffy.")
print()

input('')
system('clear')

pet.display()
print('Options:')
print('\t1 - Feed')
print('\t2 - Exercise')
print('\t3 - Sleep (UNIMPLEMENTED)')
print('\t4 - Dye')
print('\t5 - Kill')
print('\t6 - Nothing')

input('')
print()
print("You select 2, choosing to exercise Fluffy.")
pet.exercise("Cimbing")
print()

input('')
system('clear')
print('...')
print('You navigate to the manage my pet menu again')

input('')

pet.display()
print('Options:')
print('\t1 - Feed')
print('\t2 - Exercise')
print('\t3 - Sleep (UNIMPLEMENTED)')
print('\t4 - Dye')
print('\t5 - Kill')
print('\t6 - Nothing')

input('')
print("Notice how Fluffy is a little hungrier now after exercising. Let's give him some food.")

input('')
print()
print("You select 1, choosing to feed Fluffy.")

input('')
system('clear')
print('What would you like to feed the pet?')

input('')
print()
print("You choose to feed Fluffy some 'Salmon'.")
pet.feed("Salmon")
print()

input('')
system('clear')
print('...')
print('You navigate to the manage my pet menu again')

input('')

pet.display()
print('Options:')
print('\t1 - Feed')
print('\t2 - Exercise')
print('\t3 - Sleep (UNIMPLEMENTED)')
print('\t4 - Dye')
print('\t5 - Kill')
print('\t6 - Nothing')

input('')
print("That's better. Fluffy is less hungry.")
print("How about we dye him, you know, give him some style!")

input('')
print()
print("You select 1, choosing to dye Fluffy.")

input('')
print('Enter color')

input('')
print()
print("You select 'red' to dye him red.")
pet.dye('red')

input('')
system('clear')
print('...')
print('You navigate to the manage my pet menu again')

input('')

pet.display()
print('Options:')
print('\t1 - Feed')
print('\t2 - Exercise')
print('\t3 - Sleep (UNIMPLEMENTED)')
print('\t4 - Dye')
print('\t5 - Kill')
print('\t6 - Nothing')

input('')
print("Wooh! Fluffy with that new swag.")
print("Alright, let's leave Fluffy alone for a bit, we've been bothering him for too long")

input('')
print()
print("You select 6, to do nothing with Fluffy.")
pet.do_nothing()

input('')
system('clear')
print('...')
print('You navigate to the manage my pet menu again')

input('')

pet.display()
print('Options:')
print('\t1 - Feed')
print('\t2 - Exercise')
print('\t3 - Sleep (UNIMPLEMENTED)')
print('\t4 - Dye')
print('\t5 - Kill')
print('\t6 - Nothing')

input('')
print("Oh wow! Look at how his status bars have changed.")
print("Alright, let's kill Fluffy.")

input('')
print()
print("You select 5, to kill Fluffy.")

input('')
system('clear')

print("What weapon would you like to use?")
print('\t1 - Gun')
print('\t2 - Chocolate Cake')
print('\t3 - Peanut Butter')

input('')
print()
print("You choose 2, Chocolate Cake. Psst.. Cats hate chocolate cake.")
print()

input('')
pet.kill(CHOCOLATE_CAKE)

input('')
system('clear')
print('...')
print('Alright, this time you navigate to exit the game')

input('')

print('Possible Actions:')
print('\t1 - Create pet')
if len(pets):
    print(f'\t2 - Manage pets ({len(pets)} avaiable)')
    print('\t3 - Exit')
else:
    print('\t2 - Exit')

input('')
print()
print("You choose 3, in order to exit.")

input('')
print('Thanks for playing :)')

input('')
system('clear')

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=")
print("Thank you for going through this walkthrough and learning about the different functions of this game. Happy gaming!")
print()