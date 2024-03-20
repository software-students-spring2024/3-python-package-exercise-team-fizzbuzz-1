from virtual_pet import Pet as pet, create_pet
def main():
    pet = pet("Fido", "dog")
    print(f"{pet.name} is a {pet.species}")
    print(f"{pet.name} has {pet.hunger} hunger and {pet.happiness} happiness")
    pet.feed()
    print(f"{pet.name} has {pet.hunger} hunger and {pet.happiness} happiness")

if __name__ == '__main__':
    main()