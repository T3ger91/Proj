import random
from BCC import Poker
from Ruleta import Ruleta
from slow_print import slow_print
def transfer():
    R = 0
    global budget
    budget = 1000
    while budget > 0:
        R = random.randint(1, 4)
        if R == 1:
            R == 2
        elif R == 2:
            R == 3
        elif R == 3:
            Poker(budget)
        elif R == 4:
            Ruleta(budget)
    slow_print("You have lost the entire budget.\nGAME OVER")

