# DO NOT RECLAIM OWNERSHIP OVER THIS FILE
## Specific file for use with "Rogue.py"
### Created on 04/15/2024

import random

def charmRoll():
    roll = random.randint(0,5)

    if roll == 1:
        tempCharm  = "Vigorous Necklace" # Has a chance to double hit
    elif roll == 2:
        tempCharm = "Unholy Necklace" # Increases chance to hit, but decreases chance to block
    elif roll == 3:
        tempCharm = "Titanium Necklace" # Increases health
    elif roll == 4:
        tempCharm = "Adrenal Necklace" # Increases  
    elif roll == 5:
        tempCharm = "Blood Necklace"

    print("You have found a " + tempCharm + "!")
    pickUp = input
    













