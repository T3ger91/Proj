def slots(budget):
    firt_deposite = budget
    #from rounding_almost_like_in_matrix import round
    from slow_print import slow_print
    import random
    term = 0
    z = 0
    qark = 0
    while True:
        if budget == 0:
            slow_print("You lost your entier budget foll !!!\nGAME OVER")
            exit()
        if term == 1:
            break    
        else:
            while True:
                if z == 0:
                    if qark == 0:
                        slow_print("In the room you see an old slot machine. ")
                        slow_print("Do you want to play? ")
                    else:
                        slow_print("Do you want to play? ")
                else:
                    slow_print("Do you want to play again?  ")
                que = input().lower()
                if que.lower() == "yes":
                    slow_print("Great. ")
                    while True:        
                        try:
                            slow_print("How much do you want to bet from your budget?")
                            bet = int(input())
                            if bet == 0:
                                slow_print("You can't bet zero! ")
                                continue
                            if bet > budget:
                                slow_print("You can not bet more than you have loser! ")
                            else:
                                budget = budget - bet
                                break
                        except ValueError:
                            print("Enter a valid number!")

                    """
                        slow_print("This is by how much more percentagewise you can win with different numbers \n")
                        slow_print("For three of the same symbol: \n")
                        for i, y in bet_per3.items():
                            print(f"{i} + {int(float(y) * 100)}% of your bet")
                        print("For two of the same symbol:")
                        for i, y in bet_per2.items():
                            print(f"{i} + {int(float(y) * 100)}% of your bet")
                    """
                    bet_per3 = {1: 0.9, 2: 0.9, 3: 0.9, 4: 0.8, 5: 0.7, 6: 1.7}
                    bet_per2 = {1: 0.5, 2: 0.4, 3: 0.6, 4: 0.4, 5: 0.5, 6: 1.0}

                    a = random.randint(1, 6)
                    b = random.randint(1, 6)
                    c = random.randint(1, 6)

                    win3 = bet + (bet * bet_per3.get(a))
                    win2a = bet + (bet * bet_per2.get(a))
                    win2b = bet + (bet * bet_per2.get(b))

                    print(a, b, c)
                    if a == b and a == c:
                        slow_print("Nice")
                        slow_print(f"You won {round(win3)}\n")
                        budget = budget + round(win3)
                        slow_print(f"From now on your budget is {budget}.\n")
                        z = z + 1
                        break
                    elif a == b or a == c:
                        slow_print("Two are the same.")
                        slow_print(f"You won {round(win2a)}\n")
                        budget = budget + round(win2a)
                        slow_print(f"Your budget is {budget}.\n")
                        z = z + 1
                        break
                    elif b == c:
                        slow_print("Two are the same.")
                        slow_print(f"You won {round(win2b)}.\n")
                        budget = budget + round(win2b)
                        slow_print(f"Your budget is {budget}.\n")
                        z = z + 1
                        break
                    else:
                        slow_print("You lose\n")
                        budget = budget + 0
                        slow_print(f"From now on your budget is {budget}.\n")
                        z = z + 1
                        break

                if que.lower() == "no":
                    if budget > firt_deposite:
                        slow_print("Well that's not bed")
                    if budget < firt_deposite:
                        slow_print("Too bad. I guess...\n")
                    term = term + 1
                    break         
                else:
                    print("Please answer with a simple yes or no. ")
                    qark = qark + 1 
    return budget
        