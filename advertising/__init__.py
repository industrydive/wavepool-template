import random

ADS = [
    {
        'company_name': 'Fast Banana',
        'copy': 'get your bananas fast!',
        'logo': 'fastbanana.png',
    },
    {
        'company_name': 'SpaceCube',
        'copy': 'space for your cubes!',
        'logo': 'spacecube.png',
    },
    {
        'company_name': 'Cyberdyne Systems',
        'copy': "it's not self aware, yet!",
        'logo': 'cyberdyne.jpeg',
    },
    {
        'company_name': 'Weyland-Yutani Corp',
        'copy': 'Out of this world job opportunities!',
        'logo': 'weyland.png',
    },
]


def get_ad():
    return random.choice(ADS)
