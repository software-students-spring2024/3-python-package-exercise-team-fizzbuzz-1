"""Default species included in the package"""
from virtual_pet.species import Species

CAT = Species(
    name= 'cat',
    drawings= {
        'normal': '/\\__/\\\n(=\'X\'=)\n(")_(")_/',
        'unhappy': '/\\__/\\\n(=>X<=)\n(")_(")_/',
        'tired': '/\\__/\\\n(=~X~=)\n(")_(")_/',
        'dead': '/\\__/\\\n(=xXx=)\n(")_(")_/'
    },
    allergies= [
        'chocolate',
        'grape',
        'onion',
        'garlic'
    ],
    fav_exercises= [
        'laser pointer',
        'toy mouse',
    ],
    talents= [
        'hunting'
    ]
)

DOG = Species(
    name= 'dog',
    drawings= {
        'normal': ' _______\n(| , , |)\n ( (Y) )\n (")_(")',
        'unhappy': ' _______\n(| > < |)\n ( (Y) )\n (")_(")',
        'tired': ' _______\n(| ~ ~ |)\n ( (Y) )\n (")_(")',
        'dead': ' _______\n(| x x |)\n ( (Y) )\n (")_(")'
    },
    allergies= [
        'chocolate',
        'grape',
        'onion',
        'garlic'
    ],
    fav_exercises= [
        'laser pointer',
        'toy mouse',
    ],
    talents= [
        'hunting'
    ]
)

HAMSTER = Species(
    name= 'hamster',
    drawings= {
        'normal': ' o-----o\n( \'(X)\' )\nc(")_(")',
        'unhappy': ' o-----o\n( >(X)< )\nc(")_(")',
        'tired': ' o-----o\n( ~(X)~ )\nc(")_(")',
        'dead': ' o-----o\n( x(X)x )\nc(")_(")',
    },
    allergies= [
        'chocolate',
        'grape',
        'onion',
        'garlic'
    ],
    fav_exercises= [
        'laser pointer',
        'toy mouse',
    ],
    talents= [
        'hunting'
    ]
)

ROCK = Species(
    name= 'rock',
    drawings= {
        'normal': '  ____\n |    \\\n /     \\\n|      /\n \\____/',
        'unhappy': '  ____\n |    \\\n /     \\\n|      /\n \\____/',
        'tired': '  ____\n |    \\\n /     \\\n|      /\n \\____/',
        'dead': '  ____\n |    \\\n /     \\\n|      /\n \\____/',
    },
    allergies= [
        'chocolate',
        'grape',
        'onion',
        'garlic'
    ],
    fav_exercises= [
        'laser pointer',
        'toy mouse',
    ],
    talents= [
        'hunting'
    ]
)