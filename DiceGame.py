Dice game

"""

Rulla dice
spara nummer
om ett, player2s tur
om inte ett, rulla igen, eller hold
om rulla igen, plussa nytt nummer med sparat nummer
hold eller rulla igen, tills ett


def start
loop
graphics greeting
One or Two players?
Input options: Roll or Hold, change name, highscore, rules, restart, cheat, AI difficulty
(Error catches and ignore inputs that are not numbers)
player 1 name and start
add rolled numbers together into a temp_save1
if roll 1, make saved numbers = 0, break
If hold, add temp_save1 into score1, break

player 2 name and start
add rolled numbers together into a temp_save2
if roll 1, make saved numbers = 0, break
If hold, add temp_save2 into score2
loop back

If reaches >=100 points - You win! Play again? (run def start)
Make readMe

Requirements.txt 
License.md
Follow PEP 20 guidelines


"""