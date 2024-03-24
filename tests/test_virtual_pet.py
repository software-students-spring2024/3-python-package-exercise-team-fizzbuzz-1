"""Testing the virtual pet module"""

import pytest
from virtual_pet.pet import Pet
from virtual_pet.utilities import create_pet
from virtual_pet.default_species import CAT, DOG, ROCK, HAMSTER

class Tests:
    """Class defines tests"""

    def test_create_none(self, capsys):
        """Tests creating a None pet"""
        assert create_pet("test_NONE") is None
        captured = capsys.readouterr()
        assert captured.out == 'Name and species are required to create a pet\n'
        assert create_pet() is None
        captured = capsys.readouterr()
        assert captured.out == 'Name and species are required to create a pet\n'

    @pytest.fixture
    def cat(self):
        """Fixture for creating a cat pet"""
        pet = create_pet("test_cat", CAT)
        assert pet.name == "test_cat"
        assert pet.status['hunger'] == 0
        assert pet.status['happiness'] == 10
        assert pet.status['boredom'] == 0
        assert pet.status['thirst'] == 0
        yield pet

    @pytest.fixture
    def dog(self):
        """Fixture for creating a dog pet"""
        pet = create_pet("test_dog", DOG)
        assert pet.name == "test_dog"
        assert pet.status['hunger'] == 0
        assert pet.status['happiness'] == 10
        assert pet.status['boredom'] == 0
        assert pet.status['thirst'] == 0
        yield pet

    @pytest.fixture
    def hamster(self):
        """Fixture for creating a hamster pet"""
        pet = create_pet("test_hamster", HAMSTER)
        assert pet.name == "test_hamster"
        assert pet.status['hunger'] == 0
        assert pet.status['happiness'] == 10
        assert pet.status['boredom'] == 0
        assert pet.status['thirst'] == 0
        yield pet

    @pytest.fixture
    def rock(self):
        """Fixture for creating a rock pet"""
        pet = create_pet("test_rock", ROCK)
        assert pet.name == "test_rock"
        assert pet.status['hunger'] == 0
        assert pet.status['happiness'] == 10
        assert pet.status['boredom'] == 0
        assert pet.status['thirst'] == 0
        yield pet

    def test_get_species_name(self, cat: Pet, dog: Pet, hamster: Pet, rock: Pet):
        """Tests getting the species names"""
        assert cat.get_species_name() == 'cat'
        assert dog.get_species_name() == 'dog'
        assert hamster.get_species_name() == 'hamster'
        assert rock.get_species_name() == 'rock'

    def test_groom(self, cat: Pet):
        """Tests grooming"""
        assert cat.groom('pink') is False
        assert cat.color != 'pink'
        assert cat.groom('red') is True
        assert cat.color == 'red'


    def test_feed(self, cat: Pet):
        """Tests feeding the pet"""
        cat.status['hunger'] = 5
        cat.feed(1)
        assert cat.status['hunger'] == 4

    def test_feed_not_hungry(self, dog: Pet):
        """Tests feeding the pet if the pet isn't hungry"""
        dog.status['hunger'] = 0
        dog.feed(1)
        assert dog.status['hunger'] == 0

    def test_feed_multiple(self, hamster: Pet):
        """Tests feeding multiple feed points"""
        hamster.status['hunger'] = 5
        hamster.feed(3)
        assert hamster.status['hunger'] == 2

    def test_feed_multiple_times(self, hamster: Pet):
        """Tests feeding mutliple times"""
        hamster.status['hunger'] = 5
        hamster.feed(2)
        hamster.feed(1)
        hamster.feed(1)
        assert hamster.status['hunger'] == 1

    def test_exercise(self, cat: Pet):
        """Tests exercising under normal conditions"""
        cat.status['boredom'] = 5
        cat.status['happiness'] = 5
        cat.status['hunger'] = 5
        cat.exercise(1)
        assert cat.status['boredom'] == 4
        assert cat.status['happiness'] == 6
        assert cat.status['hunger'] == 6

    def test_exercise_max_hunger(self, dog: Pet):
        """Tests exercising when at max hunger"""
        dog.status['boredom'] = 5
        dog.status['happiness'] = 5
        dog.status['hunger'] = 10
        dog.exercise(1)
        assert dog.status['boredom'] == 5
        assert dog.status['happiness'] == 5
        assert dog.status['hunger'] == 10

    def test_exercise_long_duration(self, cat: Pet):
        """Tests exercising for a long duration"""
        cat.status['boredom'] = 5
        cat.status['happiness'] = 5
        cat.status['hunger'] = 0
        cat.exercise(10)
        assert cat.status['boredom'] == 0
        assert cat.status['happiness'] == 10
        assert cat.status['hunger'] == 10
