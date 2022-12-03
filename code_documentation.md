# Code Documentation

## Variable Tables

### Global
| Variable        | Type              | Description   |
| :-------------- | :---------------- | :-----------  |
| `globalTime`    | int               | Total time for level in seconds|
| `globalNRange`  | list[x,y]         | Range of numbers taken to make a prompt |
| `globalStage`   | int               | Current stage the player is in |
### Calculator
| Variable        | Type              | Description   |
| :-------------- | :---------------- | :-----------  |
| `inputPerm`    | str               | Equation entered by player to get number |
| `randN`    | int               | Random number generated using bounds of `globalNRange` |
| `timeRemaining`    | int               | Time remaining when player gets the answer |

### Clash

| Variable        | Type              | Description   | 
| :-------------- | :---------------- | :-----------  |
| `enemyDict`     | dict - int        | Current stats of enemy |
| `enemyStatlist` | dict - dict - int | Values for stats of all enemies |
| `enemyTypelist` | dict - dict - int | Values for each type of enemy |
| `enemyDmg`      | int               | Damage done by enemy |
| `playerDict`    | dict - int        | Stats of player currrently |
| `playerStatlist`|dict - dict - int  | Int value of each stat |
| `playerDmg`     | int               | Damage done by player |
| `playerCrit`          | int               | Critical multiplier |
| `playerRed`          | int               | Damage Reduction multiplier |
| `finalDmg` | int               | Contains the results of the clash |

## Dictionaries

### Player

- playerDict: 
{<br>
"HP": playerStatlist[0], <br>
"Atk": playerStatlist[0], <br>
"Def": playerStatlist[0], <br>
"Luck": playerStatlist[0], <br>
"Luck": playerStatlist[0]<br>}

- playerStatlist:
{<br>
"HP":{0:15,1:25,2:45,3:65,4:90,5:120}, <br>
"Atk":{0:1,1:1.2,2:1.4,3:1.6,4:1.8,5:2}, <br>
"Def":{0:1,1:0.97,2:0.92,3:0.85,4:0.75,5:0.62}, <br>
"Time": {0:0,1:1,2:2,3:3,4:4,5:5}, c
"Luck": {0:100, 1:98, 2:96, 3:94, 4:92, 5:90}
<br>}

### Enemy
- enemyDict:
{enemyTypelist["Man"]} <i> Default Value </i>

- enemyStatlist:
{<br>
{"HP":{0:25,1:45,2:80},
<br>
{"Atk":{0:0.75,1:1,2,2:1.25},
<br>
{"Def":{0:1.25,1:1.2,2:0.75},
<br>
{"Time": {0:10,1:15,2:20},
<br>
{"NRange": {0:[0,10], 1:[5,25], 2:[25,100], 3:[100,1000]},
<br>}

- enemyTypelist:
{<br>
     - "Man": {<br>
        "Name": "Man",<br>
        "HP": enemyStatlist["HP"][1],<br>
        "Atk": enemyStatlist["Atk"][1],<br>
        "Def": enemyStatlist["Def"][1],<br>
        "Time": enemyStatlist["Time"][1]},<br>
<br>
     - "CancerPatient": {<br>
     "Name": "Cancer Patient",<br>
     "HP": enemyStatlist["HP"][1],<br>
     "Atk": enemyStatlist["Atk"][1],<br>
     "Def": enemyStatlist["Def"][0],<br>
     "Time": enemyStatlist["Time"][0]},<br>
<br>
     - "FloridaMan": {<br>
     "Name": "Florida Man",<br>
     "HP": enemyStatlist["HP"][2],<br>
     "Atk": enemyStatlist["Atk"][0],<br>
     "Def": enemyStatlist["Def"][1],<br>
     "Time": enemyStatlist["Time"][1]},<br>
<br>
     - "PepsiMan": {<br>
     "Name": "Pepsi Man",<br>
     "HP": enemyStatlist["HP"][1],<br>
     "Atk": enemyStatlist["Atk"][2],<br>
     "Def": enemyStatlist["Def"][0],<br>
     "Time": enemyStatlist["Time"][1]},<br>
<br>
     - "TheRock": {<br>
     "Name": "The Rock",<br>
     "HP": enemyStatlist["HP"][1],<br>
     "Atk": enemyStatlist["Atk"][1],<br>
     "Def": enemyStatlist["Def"][2],<br>
     "Time": enemyStatlist["Time"][2]},
<br>
}

## Functions

### Calculator

- randomizeEnemy(enemyTypelist, enemyStatlist):
    - Randomly selects an enemy from the enemy list
    - Returns the enemy dictionary