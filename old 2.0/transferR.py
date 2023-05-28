import random
global R
global previous_value
global current_value

from slots import slots
from BCC import Poker
from Ruleta import Ruleta
from slow_print import slow_print

def transfer():
    R = 0
    global money
    money = 1000
    R = random.randint(1,4)
    if R == 1:
        slow_print("U need to run coops are on tha way ")
    elif R == 2:
        slots()
    elif R == 3:
        Poker(money)
    elif R == 4:
        Ruleta(money)
