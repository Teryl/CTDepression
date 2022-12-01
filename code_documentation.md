# Code Documentation

## Variable Table

### Calculator
| Variable        | Type              | Description   |
| :-------------- | :---------------- | :-----------  |
| `globalTime`    | int               | Total time for level |
| `enemyDict`     | dict - int        | Current stats of enemy |
| `enemyStatlist` | dict - dict - int | Values for stats of all enemies |
| `enemyTypelist` | dict - dict - int | Values for stats of all enemies |
### Clash

| Variable        | Type              | Description   |
| :-------------- | :---------------- | :-----------  |
| `globalTime`    | int               | Total time for level || `globalNRange`  | list[x,y]         | Dictates bounds of calculator number displayed |
| `globalStage`   | int               | Current stage the player is in |
| `enemyDict`     | dict - int        | Current stats of enemy |
| `enemyStatlist` | dict - dict - int | Values for stats of all enemies |
| `enemyTypelist` | dict - dict - int | Values for each type of enemy |
| `enemyDmg`      | int               | Damage done by enemy |
| `enemyFinalDmg` | int               | Damage done to enemy |
| `playerDict`    | dict - int        | Stats of player currrently |
| `playerStatlist`|dict - dict - int  | Int value of each stat |
| `playerDmg`     | int               | Damage done by player |
| `playerFinalDmg`| int               | Damage done to player |
| `playerCrit`          | int               | Critical multiplier |

Player Dictionaries:

- playerDict: {"HP": 0, "Atk": 0, "Def": 0, "Luck": 0, "Luck": 0} 
- playerStatlist: <br>
{<br>
"HP":{0:15,1:25,2:45,3:65,4:90,5:120}, <br>
"Atk":{0:1,1:1.2,2:1.4,3:1.6,4:1.8,5:2}, <br>
"Def":{0:1,1:0.97,2:0.92,3:0.85,4:0.75,5:0.62}, <br>
"Time": {0:0,1:1,2:2,3:3,4:4,5:5}, c
"Luck": {0:100, 1:98, 2:96, 3:94, 4:92, 5:90}
<br>}


Enemy Dictionaries: 
- enemyDict:
{enemyTypelist(Man)} <i> Default Value </i>
- enemyStatlist: <br>
{<br>
{"HP":{0:25,1:45,2:80},
<br>
{"Atk":{0:0.75,1:1,2,2:1.25},
<br>
{"Def":{0:1.25,1:1.2,2:0.75},
<br>
{"Time": {0:10,1:15,2:20},
<br>
{"globalNRange": {0:[0,10], 1:[5,25], 2:[25,100], 3:[100,1000]},
<br>}

- enemyTypelist: <br>
{<br>
    Man: {"Name": "Man","HP": 1,"Atk": 1,"Def": 1,"Time": 1},
<br>
    CancerPatient: {"Name": "Cancer Patient","HP": 1,"Atk": 1,"Def": 0,"Time": 0},
<br>
    FloridaMan: {"Name": "Florida Man","HP": 2,"Atk": 0,"Def": 1,"Time": 1},
<br>
    BepisMan: {"Name": "Bepis Man","HP": 1,"Atk": 2,"Def": 0,"Time": 1},
<br>
    TheRock: {"Name": "The Rock","HP": 1,"Atk": 1,"Def": 2,"Time": 2},
<br>
}