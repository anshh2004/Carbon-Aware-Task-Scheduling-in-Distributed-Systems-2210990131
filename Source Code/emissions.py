# emissions.py

from config import ENERGY_PER_STEP


def calculate_emission(moer_value):
    """
    Carbon Emission Formula:
    Emissions = Energy × MOER
    """

    return ENERGY_PER_STEP * moer_value