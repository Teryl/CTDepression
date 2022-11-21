# Description
\[Title] is a fast-paced educational game that combines roguelike gameplay with puzzle mechanics; complete with procedurally generated levels, enemy variety, and player progression for infinite fun.

There is no lore. (unless?? n = years left to live?? and cancer patient????)

<!--line breaks are such a mess. delete this later-->
\
Become the best Grim Reaper the world has ever seen by not doing math homework. Upgrade your stats in meaningful ways and come up with unique strategies for each enemy until you become the most feared upon psychopomp in the history of the afterlife.

> *There is no lore. STAR WARS™: The Old Republic™ is a free-to-play MMORPG that puts you at the center of your own story-driven saga. Play as a Jedi, Sith, Bounty Hunter, or one of many other iconic STAR WARS roles in the galaxy far, far away over three thousand years before the classic films.*

<br>

# Gameplay
## Gameplay Overview
The player goes through an infinite number of procedurally generated levels to achieve a high score.

Each level has an enemy. The player can attack the enemy once per turn. There is no limit to the number of turns per level.\
To attack the enemy, the player has to perform an attack using their calculator. This is done by calculating a value `n` using the operands and operators available in the calculator, within the time limit. This is detailed in [a later section](#calculator).

Each level has two global variables which are determined by [enemy type](#enemy-types):
|          |                     |
| :------: | :------------------ |
| `Time`   | Time limit          |
| `nRange` | Possible `n` values |

The player has the following properties (variables):
|          |                  |
| :------: | :--------------- |
| `HP`     | Total hit points |
| `Atk`    | Attack stat      |
| `Def`    | Defense stat     |
| `Luck`   | [Critical hit](#critical-hits) chance |

These properties can be upgraded via [stat upgrades](#upgrade-shop).\
Enemies also have similar properties; [different enemies](#enemy-types) have different stats.

### Each Turn:
1. A new `n` is generated.
2. The player attempts to perform an attack using their calculator.
   - If the player fails to calculate `n` within the time limit, base damage = 0.
   - If the player succeeds, base damage is calculated using [this algorithm](#calculator).
3. The enemy attacks with base damage, which are affected by the following modifiers:
   - Random multiplier
   - Enemy attack stat (`enemy.Atk`)
4. The player attacks with base damage, which are affected by the following modifiers:
   - Player attack stat (`player.Atk`)
   - Time multiplier
5. Additional modifiers are taken into account, such as [critical hits](#critical-hits) or [bonus conditions](#bonus-conditions).
6. Damage from the enemy is offset by damage from the player (or vice versa).
   - If player dealt more damage than the enemy, enemy takes the offset damage.
     - This is decreased based on the enemy's defense stat. (`enemy.Def`)
   - If enemy dealt more damage than the player, player takes the offset damage.
     - This is decreased based on the player's defense stat. (`player.Def`)
7. Damage is subtracted from the relevant entity's `HP`.
   - If the player's `HP` drops to 0, game ends
   - If the enemy's `HP` drops to 0, the player proceeds to the next level.


## Calculator
### Each Turn:
1. A new `n` is generated
   - The range of `n` is determined by the [type of enemy](#enemy-types).
2. Within the time limit, the player has to obtain `n` using the available operands, operators, and parentheses.
   - If the player fails to calculate `n`, or if time limit is reached, base damage = 0
   - If the player succeeds, base damage is calculated as per following:
```
permutation points = value of each
total sum points = unique permutation regardless of order
base damage = constant\*total sum points
idk what is going on here @teryl pls take over
```


## Other Features
### Enemy Types
Each enemy has the following properties:
|          |                     |
| :------: | :------------------ |
| `Time`   | Time limit          |
| `nRange` | Possible `n` values |
| `HP`     | Total hit points    |
| `Atk`    | Attack stat         |
| `Def`    | Defense stat        |

Different enemies have different values for each property, requiring unique strategies and promoting dynamic combat.

Most enemies have a single stat buffed, while another stat is debuffed. ([Read more about buffs and nerfs](https://en.wikipedia.org/wiki/Game_balance#Buffs_and_nerfs))\
Some enemies, called Bosses, have multiple buffs with little or no nerfs. Bosses appear every few levels.

Complete list of enemies can be found in this table. Bosses are labelled with an `*`.
| Enemy          | Buffs / Debuffs       |
| :------------- | :-------------------- |
| Man            | -                     |
| Cancer Patient | 🔽 Time <br> 🔽 Def  |
| Florida Man    | 🔼 HP   <br> 🔽 Atk  |
| Bepis Man      | 🔼 Atk  <br> 🔽 Def  |
| The Rock       | 🔼 Def  <br> 🔼 Time |

*Note that `🔽 Time` is actually a buff, and the inverse a nerf/debuff.*

Every enemy is buffed or debuffed a different amount. The buff/debuff multipliers are finely tuned to scale with the [player's progression](#upgrade-shop) so that as they reach new levels, they are constantly challenged by stronger enemies.\
Power scaling with the player character, the enemies should scale at a slightly higher rate than the player, so that the player's skill ceiling is reached at a certain point. Failure to achieve this balance means the player would find the late game tedious rather than challenging and fun.

### Upgrade Shop
The player can also become stronger as they progress through the game. This is done via stat upgrades, aka player progression.

Completing a level grants the player an Upgrade Coin. Upgrade Coins can be used to purchase upgrades for the player.\
As the player purchases more upgrades, each upgrade will cost more Upgrade Coins than the previous.\
However, the player will have more opportunities to earn Upgrade Coins as they reach higher levels. (e.g. Bosses, [bonus conditions](#bonus-conditions))

The player is able to invest their Upgrade Coins into the following stats:
| Stat     | Effect           |
| :------: | :--------------- |
| `HP`     | 🔼 Max hit points + Healing |
| `Atk`    | 🔼 Attack stat      |
| `Def`    | 🔼 Defense stat     |
| `Luck`   | 🔼 [Critical hit](#critical-hits) chance |

Alternatively, the player can choose to purchase the *Golden Stopwatch* upgrade. This upgrade increases the time limit permanently by 1 second.

### Critical Hits
Every turn, there is a chance for the player's damage to be multiplied by 2 times. This chance is rolled and damage is calculated after all preexisting damage modifiers except `Def`, i.e in [step 5 of each turn](#each-turn).

Initial critical hit rate is 0%. Each upgrade increases it by 2 pp.

### Bonus Conditions
`decide if bonus condition is for bosses or just random`

<br>

# Art and Assets
## Styleguide
<kbd>Alt</kbd>+<kbd>F4</kbd> your life

btw can you add relative links in the readme.md file so it links to this and maybe the todo list thanks
