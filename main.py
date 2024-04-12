# DO NOT RECLAIM OWNERSHIP OVER THIS GAME
## Project Originally By Broclly
### Created on 04/07/2024

import time
import random
import moreSpace

buildVer = 0.21
playerHealth = 5
enemyHealth = 10
encounterActive = 1
welcomeComplete = 0
criticalMulti = 2
guardActive = 1

def anyKey():
    input("Press enter to continue...")

def softClose():
    input("Press enter to quit...")
    exit()

def welcome():
    print("~Project by Broclly~")
    moreSpace.small()
    time.sleep(1/4)
    print("Greetings, welcome to Rogue.py!")
    time.sleep(1/4)
    print("This project is to test the limits of using Python as a game engine!")
    time.sleep(1/4)
    print("Current Build Version:", buildVer)
    anyKey()

def enemyTurn():
    global enemyHit
    enemyHit = random.randint(0,2)
    global playerHealth
    enemyDamage = enemyHit * guardActive
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
    playerTurnChoice = int(input("Make your choice! "))

    if playerTurnChoice == 1:
        print("You chose guard!")
        time.sleep(1)
        playerGuard()
    if playerTurnChoice == 2:
        print("You chose attack!")
        time.sleep(1)
        playerAttack()

def playerGuard():
    global guardActive
    guardActive = 1
    guardHit = random.randint(0,2)
    if guardHit == 2:
        print("Guard Sucessful!")
        guardActive = 0
    else:
        print("Guard Failed!")
        guardActive = 1


def playerAttack():
    playerHit = random.randint(0,1)
    global enemyHealth
    critCheck()
    if playerHit == 0:
         damage = (playerHit + critActive)* criticalMulti
         print("Attack Failed!")
         print("You hit the enemy for", damage, "damage!")
    else:
        damage = (playerHit)* criticalMulti
        enemyHealth = enemyHealth - damage
        print("You hit the enemy for", damage, "damage!")
    
    print("The enemy has", enemyHealth, "health left!")

def critCheck():
    critHit = random.randint(0,10)
    if critHit == 0:
        global critActive
        critActive = 1
        print("CRITICAL HIT!")
    else:
        critActive = 0

def check():
    if playerHealth <= 0:
        print("You died! Try again :(")
        time.sleep(3)
    if enemyHealth <= 0:
        print("You have successfully eliminated the enemy!")
        global encounterActive
        encounterActive = 0
        softClose()
    if enemyHealth == 0 and playerHealth == 0:
        print("When the dust settles, neither of you survive...")
        time.sleep(5)

def enemyEncounter():
    if encounterActive == 1:
        playerTurn()
        time.sleep(1)
        enemyTurn()
        time.sleep(3)
        check()
        moreSpace.normal()
        time.sleep(2)   

while playerHealth > 0:
    if welcomeComplete == 0:
        welcome()
        welcomeComplete = 1
        moreSpace.normal()
    enemyEncounter()