# DO NOT RECLAIM OWNERSHIP OVER THIS FILE
## Specific file for use with "Rogue.py"
### Created on 04/14/2024

import random
from assets.weaponIndex import *
from assets.playerData import playerEquipped

weaponsList = ["starter-sword", "beautiful-blade", "heavy-hitter"]
tempWeapon = "null"


def weaponRoll():
    global tempWeaponRoll
    tempWeaponRoll = random.randint(0,len(weaponsList) - 1)
    tempWeapon = weaponsList[tempWeaponRoll]
    currentWeapDMG = weaponDMG
    currentCritChance = critChance
    tempWeaponDMG = tempSwordCheck()

    print("You found a new weapon: " + tempWeapon + "!")
    print("(Current Stats: Weapon Damage = ", currentWeapDMG," Critical Chance = ", currentCritChance,")")
    assign = int(input("Would you like to replace your current one with this one? (1 for yes, 0 for no) "))
    if assign == 1:
        playerEquipped["weapon"] = tempWeapon
        print("You pick up the weapon, and replace your current one!")
    else:
        print("You drop the weapon, and continue your treck onwards...")

def swordCheck():
    global weaponDMG
    global critChance
    global hitChance

    if playerEquipped["weapon"] == "starter-sword":
        weaponDMG = starterSword["weaponDMG"]
        critChance = starterSword["critChance"]
        hitChance = starterSword["hitChance"]

    elif playerEquipped["weapon"] == "beautiful-blade":
        weaponDMG = beautifulBlade["weaponDMG"]
        critChance = beautifulBlade["critChance"]
        hitChance = beautifulBlade["hitChance"]


    elif playerEquipped["weapon"] == "heavy-hitter":
        weaponDMG = heavyHitter["weaponDMG"]
        critChance = heavyHitter["critChance"]
        hitChance = heavyHitter["hitChance"]


    elif playerEquipped["weapon"] == "admin-blade":
        weaponDMG = adminBlade["weaponDMG"]
        critChance = adminBlade["critChance"]
        hitChance = adminBlade["hitChance"]

def tempSwordCheck():
    from assets.playerData import tempPlayerData
    global tempWeaponDMG
    global tempCritChance

    if tempPlayerData["tempWeapon"] == "starter-sword":
        tempWeaponDMG = starterSword["weaponDMG"]
        tempCritChance = starterSword["critChance"]

    elif tempPlayerData["tempWeapon"] == "beautiful-blade":
        tempWeaponDMG = beautifulBlade["weaponDMG"]
        tempCritChance = beautifulBlade["critChance"]

    elif tempPlayerData["tempWeapon"] == "heavy-hitter":
        tempWeaponDMG = heavyHitter["weaponDMG"]
        tempCritChance = heavyHitter["critChance"]

    elif tempPlayerData["tempWeapon"] == "admin-blade":
        tempWeaponDMG = adminBlade["weaponDMG"]
        tempCritChance = adminBlade["critChance"]