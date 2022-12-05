### Calculator Game ver 0.8
### By: Mithunbalaji MG and Dianthe
### Date: 12/06/2022

import math
import random
import time
import os
import threading
import copy
import multiprocessing
from threading import Thread 
def gui():
    import visuals

Thread(target=gui).start()

while True:  
    '''For now, we have not set a time so we call it globalTime, timeRemaining'''
    timeRemaining = 10

    ## initialize playerStatlist and playerDict 
    playerStatlist = {
        "HP":{0:30, 1:45, 2:75, 3:100, 4:140, 5:200},
        "Atk":{0:1, 1:1.2, 2:1.4, 3:1.6, 4:1.8, 5:2}, 
        "Def":{0:1, 1:0.97, 2:0.92, 3:0.85, 4:0.75, 5:0.62}, 
        "Time": {0:0, 1:1, 2:2, 3:3, 4:4, 5:5}, 
        "Luck": {0:100, 1:98, 2:96, 3:94, 4:92, 5:90}
        }
    playerDict = {
        "HP": playerStatlist["HP"][0],
        "Atk": playerStatlist["Atk"][0],
        "Def": playerStatlist["Def"][0],
        "Time": playerStatlist["Time"][0],
        "Luck": playerStatlist["Luck"][0],
        "Skill": 0}
    
    ## initialize enemyNamelist, enemyStatList, enemyTypelist, enemyDict (default enemy is man)
    enemyNamelist = [
        "David",
        "Donggeon",
        "Dianthe",
        "Mithun",
        "Evan",
        "Quan Pham",
        "Jon",
        "Muhammad",
        "Tanjiro",
        "Dashawn",
        "Cindy",
        "Tanya",
        "Joseph",
        "Chaya",
        "Brent",
        "Kim Jeong",
        "Chanel",
        "Jamal",
        os.getlogin()
    ]
    enemyStatlist = {
        "HP":{0:0.25,1:1,2:1.25},
        "Atk":{0:0.75,1:1,2:1.25},
        "Def":{0:1.25,1:1,2:0.75},
        "Time": {0:10,1:15,2:20},
        "globalNRange": {0:[1,11], 1:[5,26], 2:[25,101], 3:[100,1001]}
        }
    enemyTypeList = {
        "man":{
        "Name": enemyNamelist[random.randrange(len(enemyNamelist))],
        "HP": enemyStatlist["HP"][1],
        "Atk": enemyStatlist["Atk"][1],
        "Def": enemyStatlist["Def"][1],
        "Time": enemyStatlist["Time"][1]
        }, 

        "cancerPatient":{
        "Name": "Cancer Patient",
        "HP": enemyStatlist["HP"][1],
        "Atk": enemyStatlist["Atk"][1],
        "Def": enemyStatlist["Def"][0],
        "Time": enemyStatlist["Time"][0]
        },

        "floridaMan":{
        "Name": "Florida Man",
        "HP": enemyStatlist["HP"][2],
        "Atk": enemyStatlist["Atk"][0],
        "Def": enemyStatlist["Def"][1],
        "Time": enemyStatlist["Time"][1]
        },

        "pepsiMan":{
        "Name": "Pepsi Man",
        "HP": enemyStatlist["HP"][1],
        "Atk": enemyStatlist["Atk"][2],
        "Def": enemyStatlist["Def"][0],
        "Time": enemyStatlist["Time"][1]
        },

        "theRock":{
        "Name": "The Rock",
        "HP": enemyStatlist["HP"][1],
        "Atk": enemyStatlist["Atk"][1],
        "Def": enemyStatlist["Def"][2],
        "Time": enemyStatlist["Time"][2]
        },

        "kanyeEast":{
        "Name": "Kanye East",
        "HP": enemyStatlist["HP"][0],
        "Atk": enemyStatlist["Atk"][2],
        "Def": enemyStatlist["Def"][1],
        "Time": enemyStatlist["Time"][1]
        }
    }
    enemyDict = enemyTypeList["man"]

    ## Defining Functions
    # Randomize Number Range:
    def randomizeN(globalStage, enemyStatlist):
        # range of n is selected based on the globalStage
        # the higher the stage, range is increased 
        
        if globalStage <= 3:
            globalNRange = enemyStatlist["globalNRange"][0]
        
        elif globalStage > 3 and globalStage <= 7:
            globalNRange = enemyStatlist["globalNRange"][1]
        
        elif globalStage > 7 and globalStage <= 12:
            globalNRange = enemyStatlist["globalNRange"][2]
        
        elif globalStage > 12:
            globalNRange = enemyStatlist["globalNRange"][3]

        # choose n based on the globalNRange
        n = random.randrange(globalNRange[0], globalNRange[1])
        return n
    
    # Randomize Enemy Type:
    def randomizeEnemy(enemyTypeList):
        enchance = random.randrange(0,101)
        if enchance <= 50:
            return enemyTypeList["man"]

        elif enchance > 50 and enchance <= 60:
            return enemyTypeList["cancerPatient"]

        elif enchance > 60 and enchance <= 70:
            return enemyTypeList["floridaMan"]

        elif enchance > 70 and enchance <= 80:
            return enemyTypeList["pepsiMan"]

        elif enchance > 80 and enchance <= 90:
            return enemyTypeList["theRock"]

        elif enchance > 90:
            return enemyTypeList["kanyeEast"]
        pass
        
    # Calculate Enemy Damage
    def calcEnemyDmg(enemyDict, globalStage):
        enemyDmg = enemyDict["Atk"] * globalStage
        return enemyDmg

    # Calcualate Damage done by Player for each attack
    def calcPlayerDmg(timeRemaining, inputPerm, randN, playerDict):
        # for now, player input taken using keyboard
        # during integration with UI, input taken from click
        if inputPerm == randN:
            playerDmg = (playerDict["Atk"] * timeRemaining)**1.05
        else:
            playerDmg = 0
        return playerDmg

    # Calculate critical damage or damage reduction
    def calcPlayerCrit(playerDmg, enemyDmg, playerLuck):
        if random.randrange(0,101) > playerLuck:
            if playerDmg > enemyDmg:
                playerCritRed = 1.6
            elif playerDmg < enemyDmg:
                playerCritRed = 0.6
            else:
                playerCritRed = 1
        else:
            playerCritRed = 1
        return playerCritRed
    
    # Present option to upgrade abilities
    def upgradeAbility(playerDict, playerStatlist):
        while playerDict["Skill"] > 0:
            playerUpgradeChoice = input("Would you like to upgrade your abilities? (hp/atk/def/time/luck/n): ")
            if playerUpgradeChoice == "atk":
                for i in playerStatlist["Atk"]:
                    if playerStatlist["Atk"][i] == playerDict["Atk"]:
                        playerDict["Atk"] = playerStatlist["Atk"][i+1]
                        playerDict["Skill"] -= 1
                        print("You have upgraded your attack!")
                        print("You have {} upgrade coin(s)!".format(playerDict["Skill"]))
                        break

            elif playerUpgradeChoice == "def":
                for i in playerStatlist["Def"]:
                    if playerStatlist["Def"][i] == playerDict["Def"]:
                        playerDict["Def"] = playerStatlist["Def"][i+1]
                        playerDict["Skill"] -= 1
                        print("You have upgraded your defense!")
                        print("You have {} upgrade coin(s)!".format(playerDict["Skill"]))
                        break

            elif playerUpgradeChoice == "time":
                for i in playerStatlist["Time"]:
                    if playerStatlist["Time"][i] == playerDict["Time"]:
                            playerDict["Time"] = playerStatlist["Time"][i+1]
                            playerDict["Skill"] -= 1
                            print("You have upgraded your time!")
                            print("You have {} upgrade coin(s)!".format(playerDict["Skill"]))
                            break

            elif playerUpgradeChoice == "luck":
                for i in playerStatlist["Luck"]:
                    if playerStatlist["Luck"][i] == playerDict["Luck"]:
                            playerDict["Luck"] = playerStatlist["Luck"][i+1]
                            playerDict["Skill"] -= 1
                            print("You have upgraded your luck!")
                            print("You have {} upgrade coin(s)!".format(playerDict["Skill"]))
                            break

            elif playerUpgradeChoice == "hp":
                for i in playerStatlist["HP"]:
                    if playerStatlist["HP"][i] == playerDict["HP"]:
                            playerDict["HP"] = playerStatlist["HP"][i+1]
                            playerDict["Skill"] -= 1
                            print("You have upgraded your HP!")
                            print("You have {} upgrade coin(s)!".format(playerDict["Skill"]))
                            break

            elif playerUpgradeChoice == "n":
                break

            else:
                print("You have no more upgrade coins!")
                break

    # Initializing globalStage as 1 before round runs
    globalStage = 1

    ## Game runs as long as playerHP > 0, increase globalStage every time
    while playerDict["HP"] > 0:

        # playerDict is default
        playerDict = playerDict
        print(playerDict)

        # Selecting random enemy
        # Deepcopy the dictionary so that when same enemy is selected HP resets
        # Ensure enemyDict is just a copy not an alias
        enemyDict = copy.deepcopy(randomizeEnemy(enemyTypeList))
       
        # Scale intial enemy HP, Atk value, and Defense value 
        enemyDict["HP"] = (enemyDict["HP"] * globalStage**1.07) + 10
        enemyDict["Atk"] = enemyDict["Atk"] * (globalStage**1.07 / globalStage)
        enemyDict["Def"] = enemyDict["Def"] * (globalStage / globalStage**1.07)
        print("global stage: {}, enemy: {}".format(globalStage,enemyDict))

        # Setting global time
        timeRemaining = enemyDict["Time"] + playerDict["Time"]
        
        # Setting values of initial variables
        playerDmg = 0
        enemyDmg = 0

        # Add while loop for enemyHP > 0
        while enemyDict["HP"] >= 0:
            enemyDmg = calcEnemyDmg(enemyDict, globalStage)

            while timeRemaining >= 0:
                # Set a random N
                randN = randomizeN(globalStage, enemyStatlist)
                print("n:",randN)

                # Prompt user input 
                inputPerm = eval(input("Write your equation here: "))

                # Calculate damage done by player, if wrong, playerDmg = 0    
                playerDmg = calcPlayerDmg(timeRemaining, inputPerm, randN, playerDict)

                # Decrease time remaining
                timeRemaining = timeRemaining - 1
                print("Time remaining:",timeRemaining)
                time.sleep(1)
                
                # Calculate Final Damage
                finalDmg = int(playerDmg - enemyDmg)            
                print(playerDmg, enemyDmg)
                
                # Critical hit calculation
                playerCritRed = calcPlayerCrit(playerDmg, enemyDmg, playerDict["Luck"])
                
                '''TEST FUNCTION'''
                if playerDmg >= enemyDmg:
                    enemyDict["HP"] = int(enemyDict["HP"] - ((finalDmg * enemyDict["Def"]) * playerCritRed))
                    print("You did {} damage!".format(finalDmg), "TIMES", playerCritRed)
                
                elif playerDmg < enemyDmg:
                    playerDict["HP"] = int(playerDict["HP"] + ((finalDmg * playerDict["Def"]) * playerCritRed))
                    print("You took {} damage!".format(abs(finalDmg)), "TIMES", playerCritRed)
                
                print("Final HP - You: {}, Enemy: {}".format(playerDict["HP"], enemyDict["HP"]))
                
                # Exit while loop and change enemy
                if enemyDict["HP"] <= 0:
                    break
        

        # Increase globalStage
        globalStage += 1
        
        # Give Skill Points
        playerDict["Skill"] += 1
        print("You have gained an upgrade coin!")
        print("You have {} upgrade coin(s)!".format(playerDict["Skill"]))

        # Upgrade Abilities
        upgradeAbility(playerDict, playerStatlist)

        print("done")
        pass
    pass
