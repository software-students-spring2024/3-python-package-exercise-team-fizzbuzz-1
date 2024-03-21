"""Testing the virtual pet module"""

import pytest
from src.virtual_pet.pet import Pet, Species
from src.virtual_pet.utilities import create_pet

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
        pet = create_pet("test_cat", Species.CAT)
        yield pet

    @pytest.fixture
    def dog(self):
        """Fixture for creating a dog pet"""
        pet = create_pet("test_dog", Species.DOG)
        yield pet

    @pytest.fixture
    def hamster(self):
        """Fixture for creating a hamster pet"""
        pet = create_pet("test_hamster", Species.HAMSTER)
        yield pet

    @pytest.fixture
    def rock(self):
        """Fixture for creating a rock pet"""
        pet = create_pet("test_rock", Species.ROCK)
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
