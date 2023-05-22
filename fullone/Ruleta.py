#main file for rululete game, inculudes inside, outside and random bets
#cant work without mantioned files
#also nowere in use so used as single game without conection to others
def Ruleta(budget):
    global deposite
    from slow_print import slow_print
    from Inside_bets import Inside_bet
    from Outside_bets import Outside_bet
    from Random_bet import Random_bet
    from transferC import transfer
    z = 0
    k = 0
    while True:
        z = z + 1
        sentences = [
            "Welcome to a rulet game!!! What tipe of bets system you want to play: Inside bets, Outside bets or Random bets?\n",
            "What tipe of bets system you want to play: Inside bets, Outside bets or Random bets?\n"]
        if z == 1:
            output = sentences[0]
        else:
            output = sentences[1]
        slow_print(output)
        x = input().lower()

        try:
            #imp[ort usage 
            if x == "inside bets" or x == "inside bet" or x == "inside":
                while True:
                    try:
                        slow_print("Enter the amount you want to bet:\n")
                        deposite = int(input())
                        if deposite > budget:
                            print("U cant bet more than u have")
                            continue
                        budget = budget - deposite
                        if deposite == 0:
                            slow_print("You can't bet zero ")
                        else:
                            break
                    except ValueError:
                        print("*" * 40)
                        print("Enter correct syntax int")
                budget = budget + Inside_bet(deposite)
                slow_print(f" Your budget is now {budget}. ")
                while True:
                    slow_print("Do you want play again? Yes or No\n")
                    y = input().lower()
                    if y == "yes":
                        break
                    elif y == "no":
                        transfer()
                    else:
                        print("Please enter a valid response.")
            elif x == "outside bet" or x == "outside bets" or x == "outside":
                while True:
                    try:
                        slow_print("Enter the amount you want to bet:\n")
                        deposite = int(input())
                        if deposite > budget:
                            #no more money then u have bitch 
                            print("U cant bet more than u have")
                            continue
                        budget = budget - deposite
                        if deposite == 0:
                            slow_print("you can't bet zero")
                        else:
                            break
                    except ValueError:
                        print("*" * 40)
                        print("Enter correct syntax int")
                budget = budget + Outside_bet(deposite)
                slow_print(f"Your budget is now {budget}. ")
                while True:
                    slow_print("Do you want play again? Yes or No\n")
                    y = input().lower()
                    #logic for next random game inm transfers
                    if y == "yes":
                        break
                    elif y == "no":
                        transfer()
                    else:
                        print("Please enter a valid response.")
            elif x == "random bets" or x == "random bets" or x == "random":
                while True:
                    try:
                        slow_print("Enter the amount you want to bet:\n")
                        deposite = int(input())
                        if deposite > budget:
                            print("U cant bet more than u have")
                            continue
                        budget = budget - deposite
                        if deposite == 0:
                            slow_print("you can't bet zero")
                        else:
                            break
                    except ValueError:
                        print("*" * 40)
                        print("Enter correct syntax int")
                budget = budget + Random_bet(deposite)
                slow_print(f"Your budget is now {budget}. ")
                while True:
                    slow_print("Do you want play again? Yes or No\n")
                    y = input().lower()
                    if y == "yes":
                        break
                    elif y == "no":
                        transfer()
                    else:
                        print("Please enter a valid response.")
            else:
                slow_print("Enter opotion from menu!!!")
                #error staff 
        except ValueError:
            print("Enter correct syntax!!!")




