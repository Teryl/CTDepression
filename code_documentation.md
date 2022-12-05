# Code Documentation

## Variable Tables

### Global
| Variable        | Type              | Description   |
| :-------------- | :---------------- | :-----------  |
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
| `enemyNamelist`      | list               | All possible names "Man" can take:|
| `playerDict`    | dict - int        | Stats of player currrently |
| `playerStatlist`|dict - dict - int  | Int value of each stat |
| `playerDmg`     | int               | Damage done by player |
| `playerCritRed`          | int               | Critical/Reduction multiplier |
| `finalDmg` | int               | Contains the results of the clash |

## Dictionaries

### Player

- playerDict: 
{<br>
"HP": playerStatlist["HP"][0], <br>
"Atk": playerStatlist[Atk"][0], <br>
"Def": playerStatlist["Def"][0], <br>
"Time": playerStatlist["Time"][0], <br>
"Luck": playerStatlist["Luck"][0]<br>
} <br><i> Default Value </i> <br>

- playerStatlist:
{<br>
"HP":{0:15,1:25,2:45,3:65,4:90,5:120}, <br>
"Atk":{0:1,1:1.2,2:1.4,3:1.6,4:1.8,5:2}, <br>
"Def":{0:1,1:0.97,2:0.92,3:0.85,4:0.75,5:0.62}, <br>
"Time": {0:0,1:1,2:2,3:3,4:4,5:5}, <br>
"Luck": {0:100, 1:98, 2:96, 3:94, 4:92, 5:90}
<br>}

### Enemy
- enemyDict = randomizeEnemy(enemyTypelist) <br>
     - also apply scalers to Atk, Def and HP stats
     - enemyDict["Atk"] *= `globalStage`<sup>1.15</sup> /  `globalStage`
     - enemyDict["Def"] *= `globalStage` / `globalStage`<sup>1.15</sup>
     - enemyDict["HP"] = ( `enemyDict["HP]` * `globalStage`<sup>1.15</sup> ) + 10
     

- enemyStatlist:
     {<br>
     {"HP":{0:0.75,1:1,2:1.25},
     <br>
     {"Atk":{0:0.75,1:1,2,2:1.25},
     <br>
     {"Def":{0:1.25,1:1.2,2:0.75},
     <br>
     {"Time": {0:10,1:15,2:20},
     <br>
     {"NRange": {0:[0,10], 1:[5,25], 2:[25,100], 3:[100,1000]},
     <br>
     }

- enemyTypelist:
{<br>
     - "man": {<br>
        "Name": randomizeName(),<br>
        "HP": enemyStatlist["HP"][1],<br>
        "Atk": enemyStatlist["Atk"][1],<br>
        "Def": enemyStatlist["Def"][1],<br>
        "Time": enemyStatlist["Time"][1]},<br>
<br>
     - "cancerpatient": {<br>
     "Name": "Cancer Patient",<br>
     "HP": enemyStatlist["HP"][1],<br>
     "Atk": enemyStatlist["Atk"][1],<br>
     "Def": enemyStatlist["Def"][0],<br>
     "Time": enemyStatlist["Time"][0]},<br>
<br>
     - "floridaman": {<br>
     "Name": "Florida Man",<br>
     "HP": enemyStatlist["HP"][2],<br>
     "Atk": enemyStatlist["Atk"][0],<br>
     "Def": enemyStatlist["Def"][1],<br>
     "Time": enemyStatlist["Time"][1]},<br>
<br>
     - "pepsiman": {<br>
     "Name": "Pepsi Man",<br>
     "HP": enemyStatlist["HP"][1],<br>
     "Atk": enemyStatlist["Atk"][2],<br>
     "Def": enemyStatlist["Def"][0],<br>
     "Time": enemyStatlist["Time"][1]},<br>
<br>
     - "therock": {<br>
     "Name": "The Rock",<br>
     "HP": enemyStatlist["HP"][1],<br>
     "Atk": enemyStatlist["Atk"][1],<br>
     "Def": enemyStatlist["Def"][2],<br>
     "Time": enemyStatlist["Time"][2]},
<br>
}

## Functions

### Calculator

- randomizeEnemy(`enemyTypelist`):
    - Randomly selects an enemy from the enemy type list
    - Returns the enemy dictionary, `enemyDict`

- randomizeN(`globalNRange`):
     - Randomly selects a number from the random number range
     - Returns the number, `randN`


- calcEnemyDmg(`enemyDict, globalStage`):
     - Calculates the damage done by the enemy
     - Returns the damage done, `enemyDmg`
          - `enemyDmg` = `enemyDict["Atk"]` * `globalStage`<sup>1.2</sup>
     
### Clash

- calcEnemyHP(`enemyDict`, `globalStage`):
     - Calculates the HP of the enemy
     - Returns the HP of the enemy, `enemyHP`
          - `enemyHP` = `enemyDict["HP"]` * `globalStage`<sup>1.15</sup> + 10

- calcPlayerDmg(`timeRemaining`, `inputPerm`, `randN`, `playerDict`):
     - Calculates the damage done by the player
     - If player input matches `randN`, returns the damage done, `playerDmg`
          - `playerDmg` = `playerDict["Atk"]` * `timeRemaining`
     - If player input does not match `randN`, returns 0

- calcPlayerCrit (`playerDmg`, `enemyDmg`, `playerLuck`):
     - Calculates either critical damage or damage reduction
     - Crit chance is based on `playerLuck`, higher the value of `playerLuck`, the lower the chance of crit/damage reduction.
     - If damage is being done to the enemy, damage is increased by x1.6
         -  If `playerDmg` > `enemyDmg`, = 1.6  
     - If damage is being done to the player, damage is reduced by x0.6
          - If `playerDmg` < 0, = 0.6
     - returns `playerCritRed`, the critical damage or damage reduction multiplier

- calcFinalDmg (`playerDmg`, `enemyDmg`, `playerDict`, `enemyDict`):
     - Calculates the final damage done by both the player and the enemy
     - Returns the final damage done, `finalDmg`
          - `finalDmg` = `playerDmg` - `enemyDmg`
     - If `playerDmg` > `enemyDmg`, returns damage done to enemy:
          - `finalDmg` = `finalDmg` * `enemyDict["Def"]` * `calcPlayerCrit(playerDmg, enemyDmg, playerDict["Luck"])`
     - If `playerDmg` < `enemyDmg`, returns damage done to player:
          - `finalDmg` = `finalDmg` * `playerDict["Def"]` *
          `calcPlayerCrit(playerDmg, enemyDmg, playerLuck)`



# Visual Code Explanation

## Imported Modules
from time import sleep
- To buffer timings of visuals / delay mechanics

from math import *
- To allow for usage of maths related functions for calculations

from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter.font import Font
- Importing tkinter, default python inbuilt GUI library. All functional code in this python file will be based about tkinter.

import os
- Built in python library to handle filepaths. Used to reference assets and other files used in the code.

import sys
- Allows for passing of command line arguments to assign values to variables in the code from the command line.

from ctypes import windll, byref, create_unicode_buffer, create_string_buffer
- Python C language interpreter necessary for the importing of custom fonts.

## Global Variables
- Determines the properties of the window and also establishes commonly used unit values for late referencing.

## Player Class
- Sets values for initial player HP, Attack, Defence, Luck, Level and Time

## Assets Class(Calc UI and Fight UI)
-  It is a dictionary, serving as the directory for all our assets and stores custom size and scale attribute. It allows us to get the assets when needed

### Calc UI (Calculator UI) and CalcButtons
- The assets used for our calculator. they consist of the number and operator buttons, as well as the frame and screen.

### Fight UI (Fight UI)
- The assets used in creating the background and elements for the fight screen

### Asset Get Method
- Loads visual assets and allows us to access them,

## Fonts
- Initialises and loads fonts for the calculator. The font used was MonogramRevised, which is a modified TrueType Font.

## Game Class
- The class which consists of functions which allow the game to run

### Initialise
- Initialises the class, setting attributes of the calculator

### Button Function Allocation
- Several dictionaries that serve to link player inputs to the calculator keys

 ### Create Combat Display Update Loop
- Displays updates on the calculator in accordance to inputs by the players.\
Example: Pressing numerical keys on the calculator will cause the respective numbers to appear on the calculator screen

- It also evaluates equations keyed into the calculator, and returns the result on the calculator screen.\
Example: Inputting "(" , "1", "+" , "4", ")" , "x" , "2" computes (1 + 4) * 2 = 10, and then displays 10 on the calculator screen

## Actions Class
 -   Starts the tkinter loop