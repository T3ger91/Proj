import random
from BCC import Poker
from Ruleta import Ruleta
from enemies import enemies

def transfer():
    R = 0
    global money
    money = 1000
    R = random.randint(1, 4)
    if R == 1:
        R == 2
    elif R == 2:
        R == 3
    elif R == 3:
        Poker(money)
    elif R == 4:
        Ruleta(money)
    elif R == 5:
        enemies()