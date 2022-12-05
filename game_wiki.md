# About
*Eternal Number Slumber* is a fast-paced educational game that combines roguelike gameplay with puzzle mechanics; complete with procedurally generated levels, enemy variety, and player progression for infinite fun.

> *Become the best Grim Reaper the world has ever seen by punching in digits. Upgrade your stats in meaningful ways and come up with unique strategies for each enemy until you become the most feared upon psychopomp in the history of the afterlife.*

Despite having the impressive title of Grim Reaper, you are an overworked office worker who has to deal with uncooperative clients 24/7.\
One day, the IT department sends you a calculator, explaining how it should make your job much more efficient. All you have to do is create equations to match numbers given to you, and your client will be sent to the afterlife! Like taking candy from a baby! ~~Or lives, for that matter.~~


## Motivations
This game is aimed to help primary school kids with their mental calculations. As many kids struggle to find the motivation to study, we have created a game that tests their abilities in Math, and at the same time giving them a purpose to do so through a fun game. For instance, Frinz (Primary 4), a brother of one of our members, struggles with multiplication and mental calculation. Although he does not have the drive to study, he loves playing games on his iPad and enjoys the adrenaline that comes with it. Taking inspiration from Frinz, we ensured that our game is entertaining and competitive, thus making it time-based and included interesting characters.

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
| `Time`   | Time [upgrades](#upgrade-shop)        |
| `Luck`   | [Critical hit](#critical-hits) chance |

These properties can be upgraded via [stat upgrades](#upgrade-shop).\
Enemies also have similar properties; [different enemies](#enemy-types) have different stats.

### Each Turn:
1. A new `n` is generated.
   - The range of `n` is determined by the [type of enemy](#enemy-types).
3. The player attempts to perform an attack using their calculator.
   - If the player fails to calculate `n` within the time limit, base damage = 0.
   - If the player succeeds, base damage is calculated using [this algorithm](#calculator).
4. The enemy attacks with base damage, which are affected by the following modifiers:
   - Enemy attack stat (`enemy.Atk`)
5. The player attacks with base damage, which are affected by the following modifiers:
   - Player attack stat (`player.Atk`)
   - Time multiplier
6. Damage from the enemy is offset by damage from the player (or vice versa).
   - If player dealt more damage than the enemy, enemy takes the offset damage.
     - This is decreased based on the enemy's defense stat. (`enemy.Def`)
   - If enemy dealt more damage than the player, player takes the offset damage.
     - This is decreased based on the player's defense stat. (`player.Def`)
7. Additional modifiers are taken into account, such as [critical hits](#critical-hits) ~~or [bonus conditions](#bonus-conditions)~~.
8. Damage is subtracted from the relevant entity's `HP`.
   - If the player's `HP` drops to 0, game ends.
   - If the enemy's `HP` drops to 0, the player proceeds to the next level.


## Calculator
The calculator is the standard user interface that the player is expected to interact with, and use to control the player character.

It consists of numeric operands, standard operators, parentheses, and navigation buttons. While this sounds quite overwhelming, the GUI itself is quite simplistic, and it has a 8-bit pixel look.

### Each Turn:
1. A new `n` is generated
   - The range of `n` is determined by the [type of enemy](#enemy-types).
2. Within the time limit, the player has to obtain `n` using the available operands, operators, and parentheses.\
   Operands can only be one digit.
   - If the player fails to calculate `n`, or if time limit is reached, base damage = 0.
   - If the player succeeds, base damage = time remaining.


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
Some enemies, called Bosses, have multiple buffs with little or no nerfs. Bosses appear every few levels and drop extra [Upgrade Coins](#upgrade-shop)

Complete list of enemies can be found in this table. Bosses are labelled with an `*`.
| Enemy          | Buffs / Debuffs       |
| :------------- | :-------------------- |
| Man            | -                     |
| Cancer Patient | 🔽 Time <br> 🔽 Def  |
| Florida Man    | 🔼 HP   <br> 🔽 Atk  |
| Bepis Man      | 🔼 Atk  <br> 🔽 Def  |
| The Rock       | 🔼 Def  <br> 🔼 Time |

*Note that* `🔽Time` *is actually a debuff to the player, as they have less time to compute possible permutations.*

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
Every turn, a critical randomiser is rolled.\
If the player is dealing damage that turn, there is a 0-10% chance for the player's damage to be multiplied by 1.6 times.\
If the player is taking damage that turn, there is a 0-10% chance for the damage to be multiplied by 0.6 times.

This chance is rolled and damage is calculated after all preexisting damage modifiers, i.e in [step 7 of each turn](#each-turn).

Initial critical hit rate is 0%. Each upgrade increases it by 2 pp.

### Bonus Conditions (Deprecated)
~~During an encounter with a Boss, the Boss may impose bonus conditions that the player may be required to fulfill.~~

~~A bonus condition limits the player from using the calculator to its full potential. Instead, players have to work under special constraints to fulfill their goal of calculating `n`. For example, players may be barred from using the <kbd>+</kbd> operator, or they may be only limited to using odd numbers as operands.~~

~~Some bonus conditions are optional, while others are mandated. All bonus conditions grant an extra 5 Upgrade Coins upon completion.~~

<br>

# Art and Assets
## Styleguide
<kbd>Alt</kbd>+<kbd>F4</kbd> your life


## Bonus Art
btw can you add relative links in the readme.md file so it links to this and maybe the todo list thanks
