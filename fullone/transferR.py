import random
global R
global previous_value
global current_value

from time import sleep
from slots import slots
from BCC import Poker
from Ruleta import Ruleta
from enemies import enemies

def transfer():
    R = 0
    global money
    money = 1000
    R = random.randint(1,5)
    if R == 1:
        R == 2
    elif R == 2:
        slots()
    elif R == 3:
        Poker(money)
    elif R == 4:
        Ruleta(money)
    elif R == 5:
        enemies()