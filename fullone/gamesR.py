import random
global R
global previous_value
global current_value


from slots import slots
from BCC import Poker
from Ruleta import Ruleta

from RR import russia_roulette

R = 0
#in progres
#random games without repeating
def gameR():
    R = 0
    global money
    money = 1000
    R = random.randint(1,4)
    if R == 1:
        russia_roulette()
    elif R == 2:
        slots()
    elif R == 3:
        Poker(money)
    elif R == 4:
        Ruleta(money)
def gameRF():
    R = 0
    global money
    money = 1000
    R = random.randint(1,5)
    if R == 1:
        russia_roulette()
    elif R == 2:
        slots()
    elif R == 3:
        Poker(money)
    elif R == 4:
        Ruleta(money)
def gameR3():
    R = 0
    global money
    money = 1000
    R = random.randint(1,4)
    if R == 1:
        russia_roulette()
    elif R == 2:
        slots()
    elif R == 3:
        Poker(money)
    elif R == 4:
        Ruleta(money)



def gameR4():
    R = 0
    global money
    money = 1000
    R = random.randint(1,4)
    if R == 1:
        russia_roulette()
    elif R == 2:
        slots()
    elif R == 3:
        Poker(money)
    elif R == 4:
        Ruleta(money)





