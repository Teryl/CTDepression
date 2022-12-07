# Code Documentation
Welcome! This is the documentation for our game and all related Python code.

*Eternal Number Slumber* is launched by executing *launcher.py*, which is used as a title screen, as well as to configure important settings such as window scale.\
The launcher then executes *main.py*, which contains the bulk of our code.

*main.py* is divided into two main portions - the game engine and the GUI. The game engine is created using common Python modules, while the GUI utilises Tkinter.

### Table of Contents
1. [Programming Conventions and Principles](#programming-conventions-and-principles)
2. [Game Engine Documentation](#game-engine-documentation)
3. [GUI documentation](#gui-documentation)
4. [Index](#index)
5. [Dependencies](#dependancies)

<br>

# Programming Conventions and Principles
We chose to utilise the camelCase naming system to name variables and functions, as it is faster to type, and easier to read in snippets with multiple lines.

For functions, we decided on the following naming convention: `[function type + Function use](arguments)` to increase clarity of our code.

Using functions instead of constants allows us to avoid hard coding. This increases **flexibility** of code - should we need to make changes, they can be implemented a lot easier than if they were hardcoded. Additionally, this increases **clarity** - as all functions are named, the purpose of each value is clearer.

Put succinctly, abstraction makes debugging much easier.

<br>

# Game Engine Documentation

## Running The Game
- The following documentation below describes how the code makes the game run.

## Stage Loop
1. A number, `randN` is generated using `randomizeN(globalStage, enemyStatlist)`.
    - `randN` is the number displayed on the calculator that the player needs to get
2. An enemytype is selected for that stage using `randomizeEnemy()`
    - `randomizeEnemy()`selects an enemy type, and gets the enemy attributes from the `enemyTypeList` dictionary
3. Enemy damage is calculated using `calcEnemyDmg(enemyDict, globalStage)`
    - `enemyDmg = enemyDict["Atk"] * globalStage`
4. Turn Loop starts and repeats until `enemyDict["HP"] = 0`
5. `globalStage` increases by 1
6. Enemies' attributes are updated in the `enemyDict` dictionary in accordance to the value of `globalStage` increasing by 1
    - `enemyDict["HP"] = enemyDict["HP"] * (globalStage**1.07 + 10)`
    - `enemyDict["Atk"] = enemyDict["Atk"] * (globalStage**1.07 / globalStage)`
    - `enemyDict["Def"] = enemyDict["Def"] * (globalStage / globalStage**1.07)`
7. Player gains 1 coin that they can use in the upgrade shop or choose to save for later rounds
    - Player can choose which attribute they want to upgrade using the `upgradeAbility()` function.


## Turn Loop
1. Player damage is calculated using `calcPlayerDmg(timeRemaining, inputPerm, randN)`
    - If inputted equation equals `randN` :
        - `playerDmg = (player.get_statlist("Atk") * timeRemaining)**1.05`
    - If inputted equation does not equal `randN` :
        - `playerDmg = 0`
2. Determine if critical / damage reduction is applied using `calcPlayerCrit(playerDmg, enemyDmg, playerLuck)`
    - If luck test fails, `playerCritRed` multiplier = 1
    - If luck test passes,
        - If `playerDmg > enemyDmg`, critical damage applies, `playerCritRed` multiplier = 1.6
        - If `playerDmg < enemyDmg`, damage reduction applies, `playerCritRed` multiplier = 0.6
3. Final damage is calculated 
    - If `playerDmg > enemyDmg`, player deals damage to enemy
        - Damage to enemy = `(finalDmg * enemyDict["Def"]) * playerCritRed)`
        - Enemy HP updated : `enemyDict["HP"] = int(enemyDict["HP"] - ((finalDmg * enemyDict["Def"]) * playerCritRed))`
    - If `playerDmg < enemyDmg`, player receives damage from enemy 
        - Damage to player = `(abs(finalDmg) * player.get_statlist("Def")) * playerCritRed))`
        - Player HP updated : `player.set_stat("HP", int(player.get_stat("HP") - ((abs(finalDmg) * player.get_statlist("Def")) * playerCritRed)))`


## Game Over
- If `player.get_stat("HP") = 0`, then the function `playerEndgame()` is run and the game ends.

## Visual Representation of Code
<img src="assets/loops flowchart.png" width=""/>
<br>

# GUI Documentation
## Global Variables
- Determines the properties of the window and also establishes commonly used unit values for late referencing.

## Assets Class (Calc UI, Fight UI, Char Sprites)
-  It is a dictionary, serving as the directory for all our assets and stores custom size and scale attribute. It allows us to get the required assets when needed

### Calc UI (Calculator UI) and CalcButtons
- The assets used for our calculator. they consist of the number and operator buttons, as well as the frame and screen.

### Fight UI
- The assets used in creating the background and elements for the fight screen

### Char Sprites 
- The assets which consist of our character and the different enemies

### Asset Get Method
- Loads visual assets and allows us to access them, displaying them in the window

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

- Lastly, using queues, it constantly transfers data between the GUI and main code.\
Inputs into the GUI numberpad are evaluated and sent back to the main code.\
Enemy health, enemy sprite data, enemy name data and other miscellaneous data is transferred from the main code into the GUI

## Actions Class
- Stores all of the basic commands that can be done to modify elements in the GUI. This allows us to call multiple functions per button press to initiate more complex processes simultaniously

## buttonPresses Class
- Lists and carries out the specified processes that should be undergone when each of the buttons are pressed
<br>

# Index
## Variables
### Global
| Variable        | Type              | Description  |
| :-------------- | :---------------- | :----------- |
| `globalNRange`  | list[x,y]         | Range of numbers taken to make a prompt |
| `globalStage`   | int               | Current stage the player is in |
| `globalTime`    | int               | Total time 

### Calculator
| Variable        | Type              | Description  |
| :-------------- | :---------------- | :----------- |
| `inputPerm`     | str               | Equation entered by player to get number |
| `randN`         | int               | Random number generated using bounds of `globalNRange` |
| `timeRemaining` | int               | Time remaining when player gets the answer |

### Game Engine
| Variable        | Type              | Description  | 
| :-------------- | :---------------- | :----------- |
| `enemyDict`     | dict - int        | Current stats of enemy |
| `enemyStatlist` | dict - dict - int | Values for stats of all enemies |
| `enemyTypelist` | dict - dict - int | Values for each type of enemy |
| `enemyDmg`      | int               | Damage done by enemy |
| `enemyNamelist` | list              | All possible names "Man" can take|
| `playerDict`    | dict - int        | Stats of player currrently |
| `playerStatlist`| dict - dict - int | Int value of each stat |
| `playerDmg`     | int               | Damage done by player |
| `playerCritRed` | int               | Critical/Reduction multiplier |
| `finalDmg`      | int               | Contains the results of the clash |


## Dictionaries
### Player
```python
playerDict = {
    "maxHP": 0,
    "HP": 0,
    "Atk": 0,
    "Def": 0,
    "Time": 0,
    "Luck": 0,
    "LVL": globalStage,
    "N": 0,
    "Skill": 0
}
```
```python
playerStatlist = {
    "maxHP":{0:30, 1:45, 2:75, 3:100, 4:140, 5:200},
    "Atk":{0:1, 1:1.2, 2:1.4, 3:1.6, 4:1.8, 5:2}, 
    "Def":{0:1, 1:0.97, 2:0.92, 3:0.85, 4:0.75, 5:0.62}, 
    "Time": {0:0, 1:1, 2:2, 3:3, 4:4, 5:5}, 
    "Luck": {0:100, 1:98, 2:96, 3:94, 4:92, 5:90}
}
```
### Enemy
`enemyDict` is initialised using `enemyDict = enemyTypeList["man"]`.\
It is then assigned an enemy using the `randomizeEnemy()` function: `enemyDict = randomizeEnemy(enemyTypelist)`.\
This allows you to get an attribute of the current enemy easily.\
e.g. `enemyName = enemyDict["Name"]`, `enemyDmg = enemyDict["Atk"] * globalStage`

```python
enemyStatlist = {
    "HP":{0:0.25,1:1,2:1.25},
    "Atk":{0:0.75,1:1,2:1.25},
    "Def":{0:1.25,1:1,2:0.75},
    "Time": {0:10,1:15,2:20},
    "globalNRange": {0:[1,11], 1:[5,26], 2:[25,101], 3:[100,1001]}
}
```
```python
enemyTypeList = {
    "man":{
        "Name": "man",
        "HP": self.enemyStatlist["HP"][1],
        "Atk": self.enemyStatlist["Atk"][1],
        "Def": self.enemyStatlist["Def"][1],
        "Time": self.enemyStatlist["Time"][1]
    }, 

    "Cancer":{
        "Name": "Cancer Patient",
        "HP": self.enemyStatlist["HP"][1],
        "Atk": self.enemyStatlist["Atk"][1],
        "Def": self.enemyStatlist["Def"][0],
        "Time": self.enemyStatlist["Time"][0]
    },

    "Florida":{
        "Name": "Florida Man",
        "HP": self.enemyStatlist["HP"][2],
        "Atk": self.enemyStatlist["Atk"][0],
        "Def": self.enemyStatlist["Def"][1],
        "Time": self.enemyStatlist["Time"][1]
    },

    "Bepis":{
        "Name": "Pepsi Man",
        "HP": self.enemyStatlist["HP"][1],
        "Atk": self.enemyStatlist["Atk"][2],
        "Def": self.enemyStatlist["Def"][0],
        "Time": self.enemyStatlist["Time"][1]
    },

    "Therock":{
        "Name": "The Rock",
        "HP": self.enemyStatlist["HP"][1],
        "Atk": self.enemyStatlist["Atk"][1],
        "Def": self.enemyStatlist["Def"][2],
        "Time": self.enemyStatlist["Time"][2]
    },

    "Kanye":{
        "Name": "Kanye East",
        "HP": self.enemyStatlist["HP"][0],
        "Atk": self.enemyStatlist["Atk"][2],
        "Def": self.enemyStatlist["Def"][1],
        "Time": self.enemyStatlist["Time"][1]
    }
}
```

## Functions
### Calculator
`randomizeEnemy(enemyTypelist)`
- Randomly selects an enemy from the enemy type list.
- Returns the enemy dictionary, `enemyDict`.

<br>

`randomizeN(globalStage, enemyStatlist)`
- Randomly selects a number from the random number range. 
- The range increases as `globalStage` increases
- Returns the number, `randN`

<br>

`calcEnemyDmg(enemyDict, globalStage)`
- Calculates the damage done by the enemy
- Returns the damage done, `enemyDmg`
- `enemyDmg` = `enemyDict["Atk"]` * `globalStage`<sup>1.2</sup>


### Clash
`calcEnemyHP(enemyDict, globalStage)`
- Calculates the HP of the enemy
- Returns the HP of the enemy, `enemyHP`
- `enemyHP` = `enemyDict["HP"]` * `globalStage`<sup>1.15</sup> + 10

<br>

`calcPlayerDmg(timeRemaining, inputPerm, randN, playerDict)`
- Calculates the damage done by the player
- If player input matches `randN`, returns the damage done, `playerDmg`
    - `playerDmg` = `playerDict["Atk"]` * `timeRemaining`
- If player input does not match `randN`, returns 0

<br>

`calcPlayerCrit (playerDmg, enemyDmg, playerLuck)`
- Calculates either critical damage or damage reduction
- Crit chance is based on `playerLuck`, higher the value of `playerLuck`, the lower the chance of crit/damage reduction.
- If damage is being done to the enemy, damage is increased by x1.6
    - If `playerDmg` > `enemyDmg`, = 1.6  
- If damage is being done to the player, damage is reduced by x0.6
    - If `playerDmg` < 0, = 0.6
- returns `playerCritRed`, the critical damage or damage reduction multiplier

<br>

`calcFinalDmg (playerDmg, enemyDmg, playerDict, enemyDict)`
- Calculates the final damage done by both the player and the enemy
- Returns the final damage done, `finalDmg`
    - `finalDmg` = `playerDmg` - `enemyDmg`
- If `playerDmg` > `enemyDmg`, returns damage done to enemy:
    - `finalDmg` = `finalDmg` * `enemyDict["Def"]` * `calcPlayerCrit(playerDmg, enemyDmg, playerDict["Luck"])`
- If `playerDmg` < `enemyDmg`, returns damage done to player:
    - `finalDmg` = `finalDmg` * `playerDict["Def"]` *
- `calcPlayerCrit(playerDmg, enemyDmg, playerLuck)`

<br>

# Dependancies
## Imported Modules
These are the modules we had to import in order for our code to work.
### from time import sleep
- To buffer timings of visuals / delay mechanics

### from math import *
- To allow for usage of maths related functions for calculations

### from tkinter import *
### from tkinter import messagebox
### from tkinter import font
### from tkinter.font import Font
- Importing tkinter, default python inbuilt GUI library. All functional code in this python file will be based about tkinter.

### import os
- Built in python library to handle filepaths. Used to reference assets and other files used in the code.

### import sys
- Allows for passing of command line arguments to assign values to variables in the code from the command line.

### from ctypes import windll, byref, create_unicode_buffer, create_string_buffer
- Python C language interpreter necessary for the importing of custom fonts.

### from threading import Thread, Event
- Allows us to initiate threads, so that we can simultaniously run the game and GUI.

### from queue import Queue
- Allows for communications between threads using queues 
