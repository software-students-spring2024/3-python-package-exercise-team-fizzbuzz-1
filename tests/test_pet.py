from virtual_pet.pet import Pet, create_pet

def test_create_pet():
    pet = create_pet("Fido", "dog")
    assert pet.name == "Fido"
    assert pet.species == "dog"
    assert pet.hunger == 0
    assert pet.happiness == 10
    assert pet.boredom == 0
    assert pet.thirst == 0

def test_create_empty_name():
    pet = create_pet("", "dog")
    assert pet is None

def test_create_empty_species():
    pet = create_pet("Fido", "")
    assert pet is None

def test_feed():
    pet = Pet("Hallie", "cat")
    pet.hunger = 5
    pet.feed(1)
    assert pet.hunger == 4

def test_feed_not_hungry():
    pet = Pet("Hallie", "cat")
    pet.hunger = 0
    pet.feed(1)
    assert pet.hunger == 0

def test_feed_multiple():
    pet = Pet("Hallie", "cat")
    pet.hunger = 5
    pet.feed(3)
    assert pet.hunger == 2

def test_feed_multiple_times():
    pet = Pet("Hallie", "cat")
    pet.hunger = 5
    pet.feed(2)
    pet.feed(1)
    pet.feed(1)
    assert pet.hunger == 1

def test_exercise():
    pet = Pet("Hallie", "cat")
    pet.boredom = 5
    pet.happiness = 5
    pet.hunger = 5
    pet.exercise(1)
    assert pet.boredom == 4
    assert pet.happiness == 6
    assert pet.hunger == 6
def test_exercise_max_hunger():
    pet = Pet("Hallie", "cat")
    pet.boredom = 5
    pet.happiness = 5
    pet.hunger = 10
    pet.exercise(1)
    assert pet.boredom == 5
    assert pet.happiness == 5
    assert pet.hunger == 10
def test_exercise_long_duration():
    pet = Pet("Hallie", "cat")
    pet.boredom = 5
    pet.happiness = 5
    pet.hunger = 0
    pet.exercise(10)
    assert pet.boredom == 0
    assert pet.happiness == 10
    assert pet.hunger == 10

