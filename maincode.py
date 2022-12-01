import math
import random
import time

while True:  
    ## set global stage and time
    globalStage = 1
    globalTime = 0
    '''For now, we have not set a time so we call it globalTime, timeRemaining'''
    timeRemaining = 10

    ## initialize enemy dict and statlist
    # for now initialize HP and attack as 100 and 50, later change depending on enemy and player3 type
    enemyDict = {"HP": 100, "Atk": 50, "Def": 0, "Time": 0, "globalNRange": 0}
    enemyStatlist = {
        "HP":{0:25,1:45,2:80},
        "Atk":{0:0.75,1:1,2:1.25},
        "Def":{0:1.25,1:1.2,2:0.75},
        "Time": {0:10,1:15,2:20},
        "globalNRange": {0:[0,10], 1:[5,25], 2:[25,100], 3:[100,1000]}
        }
    
    ## initialize player dict and statlist 
    playerDict = {"HP": 100, "Atk": 50, "Def": 0, "Luck": 0, "Time": 0}
    playerStatlist = {
        "HP":{0:15,1:25,2:45,3:65,4:90,5:120},
        "Atk":{0:1,1:1.2,2:1.4,3:1.6,4:1.8,5:2}, 
        "Def":{0:1,1:0.97,2:0.92,3:0.85,4:0.75,5:0.62}, 
        "Time": {0:0,1:1,2:2,3:3,4:4,5:5}, 
        "Luck": {0:100, 1:98, 2:96, 3:94, 4:92, 5:90}
        }
    
    ## hardcode HP for now
    enemyHP = enemyDict["HP"]
    playerHP = playerDict["HP"]
    
    ## create while loop for clash-attack
    # while player and enemy HP is greater than 0, round continues
    # when HP reaches 0 for any entity, exit while loop and increase stage
    while playerHP > 0 and enemyHP > 0:
        # generate new number n based on enemy
        # for now value will equate to 1st index in the list, 25
        n = enemyStatlist['globalNRange'][globalStage][1]
        
        print("Calculator value:",n)
        print("Player HP: {}\nEnemy HP: {}".format(playerHP,enemyHP))

        ## initialize first damage as 0
        playerDmg = 0
        enemyDmg = 0
        print("Player Dmg: {}\nEnemy Dmg: {}".format(playerDmg,enemyDmg))

        equation = eval(input("Write your equation here: "))
        print(equation)
        ## crit, multiplier hard coded for now
        crit = 1
        multiplier = 1.2

        # if player types wrong eqn, damage dealt to player
        if equation != n:
            enemyDmg = enemyDict["Atk"] * globalStage**(multiplier)
            print("Damage dealt by enemy: ",enemyDmg)
            playerHP = playerHP - enemyDmg
        
        # if player types right eqn, damage dealt to enemy
        else:

            playerDmg = playerDict["Atk"] * globalStage**(multiplier)
            print("Damage dealt by player: ",playerDmg)
            enemyHP = enemyHP - playerDmg
        
            

            
        
        finalDmg = playerDmg - enemyDmg
        print("New Player HP: {}\nNew Enemy HP: {}".format(playerHP,enemyHP))
        if finalDmg > 0:
            dmgToEnemy = crit * finalDmg * enemyDict["Def"]
            dmgToPlayer = 0

        if finalDmg < 0:
            dmgToPlayer = finalDmg *  playerDict["Def"]
            dmgToEnemy = 0
    
    # calculate damage done by player, and damage done by enemy
    # if damage done by player > 






        
        globalStage += 1
        pass
    
    pass
