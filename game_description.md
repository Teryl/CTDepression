# Gameplay
## Lore
There is no lore.
(unless?? n = years left to live?? and grim reaper? and cancer patient????)


## Main Gameplay
The player goes through an infinite number of proceduraly generated levels to achieve a high score.

Each level has an enemy. The player can attack the enemy once per turn. There is no limit to the number of turns per level.

To attack the enemy, the player has to perform an attack using their calculator. This is done by calculating a value `n` using the numbers and operators available in the calculator. This is detailed in [a later section](#math).

Both the player and the enemy have the following variables:
- `HP`: Total hit points
- `Atk`: Attack stat
- `Def`: Defense stat
- `Luck`: Critical hit chance

Each level also has a global variable:
- `Time`: Time limit

### Each Turn:
1. The player performs an attack using their calculator.
2. If the player fails to calculate `n`, base damage = 0
3. If the player succeeds, base damage is calculated using [this algorithm]().
4. The enemy attacks with base damage, which are affected by the following modifiers:
   - random multiplier
   - enemy attack stat
5. The player attacks with base damage, which are affected by the following modifiers:
   - player attack stat
   - time multiplier
6. Additional modifiers are taken into account, such as critical hits or bonus condition
7. Damage from the enemy is offset by damage from the player (or vice versa).
   - If player dealt more damage than the enemy, enemy takes the offset damage.
     - This is decreased based on the enemy's defense stat.
   - If enemy dealt more damage than the player, player takes the offset damage.
     - This is decreased based on the player's defense stat.
7. If the player's HP drops to 0, game ends
8. If the enemy's HP drops to 0, the player proceeds to the next level.


## Math




---
# Art and Assets
## Styleguide
<kbd>Alt</kbd>+<kbd>F4</kbd> your life

btw can you add relative links in the readme.md file so it links to this and maybe the todo list thanks
