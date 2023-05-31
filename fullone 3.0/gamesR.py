#in progres
#random games without repeating
def gameR():
    from slots import slots
    from BCC import Poker
    from Ruleta import Ruleta
    from RR import russia_roulette
    import random
    from slow_print import slow_print
    money = 1000
    previous_game = None  # Variable to store the previously played game
        
    while True:
        if money == 0:
            slow_print("You lost your entier money... Game Over")
            break
        if money >= 100000:
            slow_print("You have reached 100,000 you can go... You Won")
            break
        R = random.randint(1, 4)
        
        # Generate a new random number if it's the same as the previous game
        while R == previous_game:
            R = random.randint(1, 4)
        previous_game = R  # Update the previous game
        
        if R == 1:
            money = russia_roulette(money)
        elif R == 2:
            money = slots(money)
        elif R == 3:
            money = Poker(money)
        elif R == 4:
            money = Ruleta(money)