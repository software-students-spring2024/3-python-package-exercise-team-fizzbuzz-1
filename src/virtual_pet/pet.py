class Pet:
    def __init__(self, name, species):
        self.name = name
        self.hunger = 0
        self.happiness = 10
        self.boredom = 0
        self.thirst = 0
        self.species = species
        self.talent_level = 0
        self.talents = []

    def feed(self, numFood):
    
        for i in range(numFood):
            if self.hunger > 0:
                self.hunger -= 1
            else:
                print(f"{self.name} is not hungry!!")

    def exercise(self, duration):
        for i in range(duration):
            if self.hunger < 10: 
                self.hunger += 1
            else:
                print(f"{self.name} is too hungry to exercise!!")
                break
            if self.boredom > 0:
                self.boredom -= 1
            if self.happiness < 10:
                self.happiness += 1
            

def create_pet(name, species):
        if name == "" or species == "":
            print("Name and species are required to create a pet")
            return None
        return Pet(name, species)