import math
import random
import time

while True:  
    '''For now, we have not set a time so we call it globalTime, timeRemaining'''
    timeRemaining = 10

    ## initialize playerStatlist and playerDict 
    playerStatlist = {
        "HP":{0:15,1:25,2:45,3:65,4:90,5:120},
        "Atk":{0:1,1:1.2,2:1.4,3:1.6,4:1.8,5:2}, 
        "Def":{0:1,1:0.97,2:0.92,3:0.85,4:0.75,5:0.62}, 
        "Time": {0:0,1:1,2:2,3:3,4:4,5:5}, 
        "Luck": {0:100, 1:98, 2:96, 3:94, 4:92, 5:90}
        }
    playerDict = {
        "HP": playerStatlist["HP"][0],
        "Atk": playerStatlist["Atk"][0],
        "Def": playerStatlist["Def"][0],
        "Time": playerStatlist["Time"][0],
        "Luck": playerStatlist["Luck"][0]}
        
    ## initialize enemyStatList, enemyTypelist, enemyDict (default enemy is man)
    enemyStatlist = {
        "HP":{0:25,1:45,2:80},
        "Atk":{0:0.75,1:1,2:1.25},
        "Def":{0:1.25,1:1.2,2:0.75},
        "Time": {0:10,1:15,2:20},
        "globalNRange": {0:[1,11], 1:[5,26], 2:[25,101], 3:[100,1001]}
        }
    enemyTypeList = {
        "man":{
        "Name": "Man",
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
        }
    }
    enemyDict = enemyTypeList["man"]

    ## defining the functions
    # randomizEnemy() : select an enemy from enemy list and returns the enemy dictionary
    def randomizeEnemy(enemyTypeList):
        enemy = random.choice(list(enemyTypeList.values()))
        return enemy

    # randomizeN() : select number from random number range
    def randomizeN(globalNRange):
        nRange = random.randrange(globalNRange[0], globalNRange[1])
        return nRange
  
    # calcPlayerDmg () : calculate damage done by player
    def calcPlayerDmg(timeRemaining, inputPerm, randN, playerDict):
        # for now, player input taken using keyboard
        # during integration with UI, input taken from click
        if inputPerm == randN:
            playerDmg = playerDict["Atk"] * timeRemaining
        else:
            playerDmg = 0
        return playerDmg
    
    
    # calcEnemyDmg() : calculate damage done by enemy
    def calcEnemyDmg(enemyDict):
        enemyDmg = enemyDict["Atk"] * globalStage
        return enemyDmg

    
    # initializing globalStage as 1 before round runs
    globalStage = 1

    ## game runs as long as playerHP > 0, increase globalStage every time
    while playerDict["HP"] > 0:
        # playerDict is default
        playerDict = playerDict

        # setting global stage and number range
        if globalStage <= 3:
            globalNRange = randomizeN(enemyStatlist["globalNRange"][0])
        elif globalStage > 3 and globalStage <= 7:
            globalNRange = randomizeN(enemyStatlist["globalNRange"][1])
        elif globalStage > 7 and globalStage <= 8:
            globalNRange = randomizeN(enemyStatlist["globalNRange"][2])
        elif globalStage > 8:
            globalNRange = randomizeN(enemyStatlist["globalNRange"][3])
       
        # selecting random enemy
        enemyDict = randomizeEnemy(enemyTypeList)
        print(enemyDict)
        # defining global time
        globalTime = enemyDict["Time"] + playerDict["Time"]
        
        # add while loop for enemyHP > 0

        ''' # Tested here
        print("n:",globalNRange)
        print("time remaining:",globalTime)
        equation = eval(input("Write your equation here: "))
        test = calcPlayerDmg(globalTime, equation, globalNRange, playerDict)
        print("playerDmg:", test)
        '''
        pass
