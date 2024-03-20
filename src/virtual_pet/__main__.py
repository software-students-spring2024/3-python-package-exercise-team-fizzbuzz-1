from Pet import *

def main():
    # pet = pet("Fido", "dog")
    # print(f"{pet.name} is a {pet.species}")
    # print(f"{pet.name} has {pet.hunger} hunger and {pet.happiness} happiness")
    # pet.feed()
    # print(f"{pet.name} has {pet.hunger} hunger and {pet.happiness} happiness")
    cat = create_pet('Cashew', Species.ROCK)
    cat.groom('blue')
    cat.display()
    cat.groom('green')
    cat.display()
    print(cat.groom('pink'))
    cat.display()

if __name__ == '__main__':
    main()