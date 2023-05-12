import random
global R
global previous_value
global current_value

from choisesmain import choisemain
from time import sleep
from slots import slots
from BCC import Poker
from Ruleta import Ruleta
from enemies import enemies
from RR import russia_roulette

#in progres
#random games without repeating 
#every room ll have other staff or nothing, just run away 
def gameR():
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
    #elif R == 5:
    #enemies()

gameR()



