"""
Quotes module voor Stan de GitHub Agent applicatie.

Deze module bevat de functionaliteit voor het genereren en beheren van 
grappige uitspraken over wat een GitHub Agent allemaal kan doen.
"""

import random
from typing import Tuple
from config import ROBOT_QUOTES


def get_random_quote() -> str:
    """
    Selecteert een willekeurige uitspraak uit de lijst met beschikbare quotes.
    
    Returns:
        str: Een willekeurige grappige uitspraak.
    """
    return random.choice(ROBOT_QUOTES)


def get_next_quote(current_index: int) -> Tuple[str, int]:
    """
    Selecteert de volgende uitspraak in de reeks op basis van de huidige index.
    Als het einde van de lijst is bereikt, begint de functie weer bij het begin.
    
    Args:
        current_index (int): De index van de huidige uitspraak.
        
    Returns:
        Tuple[str, int]: Een tuple met de volgende uitspraak en de nieuwe index.
    """
    next_index = (current_index + 1) % len(ROBOT_QUOTES)
    return ROBOT_QUOTES[next_index], next_index
