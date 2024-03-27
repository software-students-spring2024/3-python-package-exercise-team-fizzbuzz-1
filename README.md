![Python build & test](https://github.com/software-students-spring2024/3-python-package-exercise-team-fizzbuzz-1/actions/workflows/build.yaml/badge.svg)

# Virtual Pet

## Team members

- [Dhiyaa Al Jorf](https://github.com/DoodyShark)

- [Firas Darwish](https://github.com/FirasBDarwish)

- [Shubhi Upadhyay](https://github.com/shubhiupa19)

## Description

virtual_pet is a python package that allows you to create, maintain, etc. a bunch of virtual pets. The behaviour and reactions of these pets are dependant on their species and other factors, which makes it a more enjoyable experience. The package allows for both handling pets directly from code, or a terminal game that accepts text input.

## How to install and use this package

1. Create a pipenv-managed virtual environment and install the latest version of virtual-[et]: pipenv install -i https://test.pypi.org/simple/ virtual-pet. (Note that you can add the version number by replacing virtual-pet with virtual-pet==X.X.X. Also note that if you've previously created a pipenv virtual environment in the same directory, you may have to delete the old one first. Find out where it is located with the pipenv --venv command.)
1. Activate the virtual environment: pipenv shell.
1. Create a Python program file that imports virtual-pet and uses it, e.g. from virtual-pet import utilities and then run utilities.play_game()
1. Run the program: python3 my_program_filename.py.
1. Exit the virtual environment: exit.

Alternatively, you can run the module directly from the terminal:

1. Create and activate up the pipenv virtual environment as before.
1. Run the package directly from the command line: python3 -m virtual_pet. This should run the code in the __main__.py file. This should begin the game loop
1. Exit the virtual environment.

Example python file:

There is an example python file provided in the repository: virtual_pet_example.py. It includes all functionalities in the package. Additonally, the code is extensively commented if you want to pry deeper into the functionality

## How to contribute to this project

1. Clone the [repository](https://github.com/software-students-spring2024/3-python-package-exercise-team-fizzbuzz-1/)
1. Activate the virtual environment: pipenv shell.
1. While updating, ensure that you are running in editable mode: pipenv install -e .
1. When done updating, 
    1. Deactivate editing mode by uninstalling the local version of virtual-pet: pipenv uninstall virtual-pet.
    1. Install the remote version of virtual-pet from testpypi: pipenv install -i https://test.pypi.org/simple/ virtual-pet
    1. update the version number on pyproject.toml file
    1. Build the project run: python -m build
    1. Verify that the built .tar archive has the files you expect your package to have (including any important non-code files) by running the command: tar --list -f dist/virtual_pet-X.X.X.tar.gz, where X.X.X is replaced with the current version number.
    1. Upload your changes to the TestPyPI repository using twine, e.g. twine upload -r testpypi dist/*. This step assumes you have access to the API key

To test your code, there is a set of tests provided in the tests/test_virtual_pet.py file. Run the tests by running: pytest. If an error occurs, run python -m pytest. If the error persists, ensure that pytest is installed (it is included in the dev dependencies of the pipenv so if the pipenv is activated correctly, this shouldn't be an issue).

## Documentation of Functions

Link to example file: [example.py](https://github.com/software-students-spring2024/3-python-package-exercise-team-fizzbuzz-1/blob/main/examples/example.py.py)

1. Functions in [src/virtual_pet/utilities.py](https://github.com/software-students-spring2024/3-python-package-exercise-team-fizzbuzz-1/blob/main/src/virtual_pet/utilities.py)

```python

def play_game(numTurns: int = float('inf')):
    """ Manges the main game loop, keeps track of the number of pets instantiated, guides
    user through main menu (selecting between creating a pet, managing a pet, or exiting).
    Repeats until user exits.
    """

def manage_pet(pet: Pet):
    """ Interact with a selected pet, used by play_game() when user choose to manage pet"""

def create_species(name: AnyStr, drawings: Dict, allergies: List, fav_exercises: List, talents: List) -> Union[Species, None]:
    """Creates a species after data validation """

def create_weapon(name: AnyStr, kill_list: List, sound: AnyStr) -> Union[Weapon, None]:
    """ Create a weapon after data validation """
    return Weapon(name, kill_list, sound)

def create_pet(name: AnyStr = "", species: Species = None) -> Union[Pet,None]:
    """Creates a pet after data validation, used by play_game() when user decides to create a pet"""

```

1. Functions in [src/virtual_pet/pet.py](https://github.com/software-students-spring2024/3-python-package-exercise-team-fizzbuzz-1/blob/main/src/virtual_pet/pet.py) under Pet class

```python

# These functions are called by manage_pet(), or when the user wishes to interact with the pet

def feed(self, food: AnyStr = "") -> bool:
    """Feeds the pet if the hunger bar allows. Returns True if managed to feed """

def exercise(self, exercise_type: AnyStr) -> bool:
    """Exercises the pet if the hunger bar allows. Returns True if the pet exercised and false otherwise"""

def display(self, full: bool = False) -> None:
    """Displays the pet along with their status on the terminal"""

def dye(self, color: AnyStr) -> bool:
    """Changes the appearance of the pet (currently just dyes hair)"""

def kill(self, weapon: Weapon) -> bool:
    """ Kill the pet with weapon of choice. Return True if killing successful. Return False otherwise"""

def do_nothing(self) -> bool:
        """ Does nothing and pseudorandomly changes pet's status, possibly killing them if thresholds for survival are tested """

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Helper functions

def get_species_name(self) -> AnyStr:
    """Returns lower case species name of the pet"""

def die(self) -> bool:
    """Kills the pet"""

```