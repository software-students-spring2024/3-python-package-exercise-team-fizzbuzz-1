from virtual_pet.utilities import create_pet
from virtual_pet.default_species import CAT, DOG, HAMSTER, ROCK
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
print('\t5 - Shoot')
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
print('\t5 - Shoot')
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
print('\t5 - Shoot')
print('\t6 - Nothing')

input('')
print("That's better. Fluffy is less hungry")



