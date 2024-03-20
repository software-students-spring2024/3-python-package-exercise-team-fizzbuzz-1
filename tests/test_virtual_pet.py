import pytest
from src.virtual_pet.Pet import *
from typing import AnyStr, List, Dict


class Tests:

    def test_create_NONE(self, capsys):
        assert create_pet("test_NONE") == None
        captured = capsys.readouterr()
        assert captured.out == 'Name and species are required to create a pet\n'
        assert create_pet() == None
        captured = capsys.readouterr()
        assert captured.out == 'Name and species are required to create a pet\n'

    @pytest.fixture
    def cat(self):
        pet = create_pet("test_cat", Species.CAT)
        yield pet
    
    @pytest.fixture
    def dog(self):
        pet = create_pet("test_dog", Species.DOG)
        yield pet

    @pytest.fixture
    def hamster(self):
        pet = create_pet("test_hamster", Species.HAMSTER)
        yield pet

    @pytest.fixture
    def rock(self):
        pet = create_pet("test_rock", Species.ROCK)
        yield pet

    def test_get_species_name(self, cat: Pet, dog: Pet, hamster: Pet, rock: Pet):
        assert cat.get_species_name() == 'cat'
        assert dog.get_species_name() == 'dog'
        assert hamster.get_species_name() == 'hamster'
        assert rock.get_species_name() == 'rock'

    def test_groom(self, cat: Pet, capsys):
        assert cat.groom('pink') == False
        assert cat.color != 'pink'
        assert cat.groom('red') == True
        assert cat.color == 'red'
