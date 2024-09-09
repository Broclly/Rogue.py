# DO NOT RECLAIM OWNERSHIP OVER THIS GAME
## Project Originally By Broclly
### Created on 04/07/2024

import time
import random
import assets.playerData
import assets.moreSpace
import assets.weaponIndex
import assets.weapons 
import assets.charms 
import assets.weapons

oneTimer = 0
buildVer = 0.41
playerHealth = 5
enemyHealth = 2
encounterActive = 1
welcomeComplete = 0
criticalMulti = 4
guardActive = 1
guardSpam = 1
perfectParryActive = 0

def anyKey():
    input("Press enter to continue...")

def softClose():
    input("Press enter to quit...")
    exit()

def autoClose():
    time.sleep(3)
    exit()

def welcome():
    print("~Project by Broclly~")
    assets.moreSpace.small()
    time.sleep(1/4)
    print("Greetings, welcome to Rogue.py!")
    time.sleep(1/4)
    print("This project is to test the limits of using Python as a game engine!")
    time.sleep(1/4)
    print("Current Build Version:", buildVer)
    anyKey()

def enemyTurn():
    global enemyHit
    enemyHit = random.randint(0,1)
    global playerHealth
    enemyDamage = (enemyHit * guardActive) - perfectParryActive

    if enemyDamage < 0:
        print("You feel invigorated by your blocking skills!")
        print("You were HEALED for ", (enemyDamage * enemyDamage), "health!")
    else:
        print("You were hit for", enemyDamage, "damage!")

    playerHealth = playerHealth - enemyDamage
    print("You have", playerHealth, "health left!")
    

def playerTurn():
    print("What will you do?")
    time.sleep(1)
    print("1. Guard")
    time.sleep(1/2)
    print("2. Attack")
    time.sleep(1/2)
    try:
        playerTurnChoice = int(input("Make your choice! "))
    except ValueError: 
        print("Invalid Response! Please provide a number instead")
        playerTurn()

    if playerTurnChoice == 1:
        print("You chose guard!")
        time.sleep(1)
        playerGuard()
    if playerTurnChoice == 2:
        print("You chose attack!")
        time.sleep(1)
        playerAttack()

def playerGuard():
    print("You hold up your guard...")
    global guardActive
    global guardSpam
    global perfectParryActive 
    guardActive = 0
    perfectParry = random.randint(0, (5* guardSpam))
    guardSpam = guardSpam + 1
    if perfectParry == 3:
        perfectParryActive = 1
        print("PERFECT BLOCK! PARRY ACTIVE!")
    else:
        perfectParryActive = 0

def playerAttack():
    global playerHit
    global guardSpam
    global perfectParryActive
    global attackDMG
    assets.weapons.swordCheck()
    attackDMG = assets.weapons.weaponDMG
    perfectParryActive = 0
    guardSpam = 1
    guardActive = 1
    playerHit = random.randint(1,assets.weapons.hitChance)
    global enemyHealth
    critCheck()
    if playerHit != 1:
         damage = 0
         print("Attack Failed!")
         print("You hit the enemy for", damage, "damage!")
    else:
        damage = (criticalMulti*critActive) + attackDMG

        enemyHealth = enemyHealth - damage
        print("You hit the enemy for", damage, "damage!")
    
    print("The enemy has", enemyHealth, "health left!")

def critCheck():
    critHit = random.randint(0,assets.weapons.critChance)
    if critHit == 0:
        if playerHit == 1:
            global critActive
            critActive = 1
            print("CRITICAL HIT!")
    else:
        critActive = 0

def check():
    if playerHealth <= 0:
        print("You died! Try again :(")
        time.sleep(3)
        softClose()
    if enemyHealth <= 0:
        print("You have successfully eliminated the enemy!")
        global encounterActive
        encounterActive = 0
        equipmentRoll()
        enemyEncounter()
        encounterActive = 1
        global oneTimer
        oneTimer = 0
    if enemyHealth == 0 and playerHealth == 0:
        print("When the dust settles, neither of you survive...")
        time.sleep(5)
        autoClose()

def equipmentRoll():
    rollActive = random.randint(1,1)

    if rollActive ==  1:
        gearType = random.randint(1,1)
        if gearType == 1:
            assets.weapons.weaponRoll()

def enemyEncounter():
    global oneTimer
    while encounterActive == 1:
        if oneTimer == 0:
            print("An enemy appears! Fight it for victory!")
            global enemyHealth
            enemyHealth = 10
            oneTimer = 1
        playerTurn()
        time.sleep(1)
        enemyTurn()
        time.sleep(3)
        check()
        assets.moreSpace.normal()
        time.sleep(2)   

while playerHealth > 0:
    if welcomeComplete == 0:
        welcome()
        welcomeComplete = 1
        assets.moreSpace.normal()
    enemyEncounter()