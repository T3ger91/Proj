import random

from slots import slots
from BCC import Poker
from Ruleta import Ruleta
from RR import russia_roulette


#in progres
#random games without repeating
def gameR():
    
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

