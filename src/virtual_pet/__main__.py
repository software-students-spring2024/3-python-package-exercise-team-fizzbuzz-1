from virtual_pet.utilities import *
from virtual_pet.default_species import CAT, DOG, HAMSTER, ROCK

def main():
    cat = create_pet('Cashew', CAT)
    cat.groom('blue')
    cat.display()
    cat.groom('green')
    cat.display()
    print(cat.groom('pink'))
    cat.display()

if __name__ == '__main__':
    main()
