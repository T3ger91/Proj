#slots game, main and only one func for the game
from transfer import transfer
from slow_print import slow_print
#main func, no were in use, only slowprint.py needed to go
def slots():
    import random
    slow_print("In the room you see an old slot machine.")
#story tail 
    def slots_story():
        slow_print("Do you want to play? ")
        que = input()
        while que.lower() != "yes" and que.lower() != "no":
            print("Please answer with a simple yes or no. ")
            slow_print("Do you want to play? ")
            que = input()
            #next game logic if u choose no as an answer
        if que.lower() == "no":
            slow_print(f"Too bad I guess... \n")
            transfer()
        elif que.lower() == "yes":
            slow_print("Great.")
            #chances to win with spetial numbers 
            bet_per3 = {1: 0.9, 2: 0.9, 3: 0.9, 4: 0.8, 5: 0.7, 6: 1.7}
            bet_per2 = {1: 0.5, 2: 0.4, 3: 0.6, 4: 0.4, 5: 0.5, 6: 1.0}
            #logic in random 
            def slots_r():
                a = random.randint(1, 6)
                b = random.randint(1, 6)
                c = random.randint(1, 6)
                #wins logic
                def money_win3():
                    return bet + (bet * bet_per3.get(a))

                def money_win2a():
                    return bet + (bet * bet_per2.get(a))

                def money_win2b():
                    return bet + (bet * bet_per2.get(b))

                print(a, b, c)
                if a == b and a == c:
                    slow_print("Nice")
                    slow_print(f"You won {money_win3()}.")
                    slots_story()
                elif a == b or a == c:
                    slow_print("Two are the same.")
                    slow_print(money_win2a())
                    slots_story()
                elif b == c:
                    slow_print(f" You won {money_win2b()}. \n")
                    slots_story()
                else:
                    slow_print("you lost \n")
                    slots_story()

            while True:
                #try with checking for misses in input
                try:
                    slow_print("How much do you want to bet? You can bet between 1 and 100 ")
                    bet = int(input())
                    if bet >= 1 and bet < 100:
                        slow_print("This is by how much more percentagewise you can win with different numbers \n")
                        slow_print(" For three of the same symbol: \n")
                        for i, y in bet_per3.items():
                            print(f" {i} + {int(float(y) * 100)} % of your bet")
                        print(" For two of the same symbol: ")
                        for i, y in bet_per2.items():
                            print(f" {i} + {int(float(y) * 100)} % of your bet")
                        slots_r()
                    else:
                        print("Enter a bet in between 1 and 100")
                except ValueError:
                    print("Enter a valid NUMBER!")

    slots_story()


