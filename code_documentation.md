# Code Documentation

## Variable Table

### Calculation

#### Clash Calculation:

| Variable      | Type            : |   Description   |
| :------      | :---------------: |  :------:  |
|`globalTime`   |int|total time for level          |
|`enemyDict`    |dict - int| current stats of enemy|
|`enemyStatlist`|dict - dict - int|values for stats of all enemies|
|`enemyTypelist`|dict - dict - int|values for each type of enemy|
|`enemyDmg`     |int|dmg done by enemy|
|`enemyFinalDmg`|int|dmg done to enemy|
|`globalNRange` |list[x,y]|dictates bounds of calculator number displayed|
|`globalStage`  |int|current stage the player is in|
|`playerDict`   |dict - int|stats of player currrently|
|`playerStatlist`|dict - dict - int|int value of each stat|
|`playerDmg`    |int|dmg done by player|
|`playerFinalDmg`|int|dmg done to player|
|`Chance`       |str|intermediate variable|
|`Crit`         |int|crit multiplier|

Player Dictionaries:

- playerDict: `{"HP": 0, "Atk": 0, "Def": 0, "Luck": 0, "Time": 0}`
- playerStatlist: `{"HP":{0:15,1:25,2:45,3:65,4:90,5:120},"Atk":{0:1,1:1.2,2:1.4,3:1.6,4:1.8,5:2}, "Def":{0:1,1:0.97,2:0.92,3:0.85,4:0.75,5:0.62}, "Time": {0:0,1:1,2:2,3:3,4:4,5:5}, "Luck": {0:100, 1:98, 2:96, 3:94, 4:92, 5:90}}`


Enemy Dictionaries: 
- enemyDict:
`{"HP": 0, "Atk": 0, "Def": 0, "Time": 0, "globalNRange": 0}`
- enemyStatlist: `{"HP":{0:25,1:45,2:80},"Atk":{0:0.75,1:1,2,2:1.25}, "Def":{0:1.25,1:1.2,2:0.75}, "Time": {0:10,1:15,2:20}, "globalNRange": {0:[0,10], 1:[5,25], 2:[25,100], 3:[100,1000]}}`