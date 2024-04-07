# DO NOT RECLAIM OWNERSHIP OVER THIS GAME
## Project Originally By Broclly
### Created on 04/07/2024

import time
import random

buildVer = 0.11
playerHealth = 5
enemyHealth = 1
encounterActive = 1
welcomeComplete = 0


def anyKey():
    input("Press any key to continue...")

def forceError():
    int(input("Press any key to quit..."))

def welcome():
    print("~Project by Broclly~")
    print("")
    print("")
    time.sleep(1/4)
    print("Greetings, welcome to Rogue.py!")
    time.sleep(1/4)
    print("This project is to test the limits of using Python as a game engine!")
    time.sleep(1/4)
    print("Current Build Version:", buildVer)
    anyKey()

def enemyTurn():
    enemyHit = random.randint(0,2)
    global playerHealth 
    playerHealth = playerHealth - enemyHit
    print("You were hit for", enemyHit, "damage!")

def playerTurn():
    playerHit = random.randint(0,1)
    global enemyHealth
    enemyHealth = enemyHealth - playerHit
    print("You hit the enemy for", playerHit, "damage!")

def check():
    if playerHealth <= 0:
        print("You died! Try again :(")
        time.sleep(1)
    if enemyHealth <= 0:
        print("You have successfully eliminated the enemy!")
        global encounterActive
        encounterActive = 0
        forceError()


def enemyEncounter():
    if encounterActive == 1:
        enemyTurn()
        playerTurn()
        check()
    

while playerHealth > 0:
    if welcomeComplete == 0:
        welcome()
        welcomeComplete = 1
    enemyEncounter()