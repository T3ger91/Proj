#main file for rululete game, inculudes inside, outside and random bets
#cant work without mantioned files
def Ruleta(budget):
    from Inside_bets import Inside_bet
    from Outside_bets import Outside_bet
    from Random_bet import Random_bet
    z = 0
    #story tail with logic 
    while True:
        z = z + 1
        sentences = ["Welcome to a rulet game!!! What tipe of bets system you want to play: Inside bets, Outside bets or Random bets?"]
        while True:
                try:
                    deposite = int(input("Enter the amount you want to bet:\n"))
                    budget = budget - deposite
                    if deposite == 0:
                        print("you can't bet zero")
                    else:
                        break
                except ValueError:
                    print("*" * 40)
                    print("Enter correct syntax int")          
        if z == 1:
            output = sentences[0]
        else:
            output = sentences[1]
        try:
            x = input(f"{output}\n").lower()
            if x == "inside bets" or x == "inside bet" or x == "inside":
                budget = budget + Inside_bet(deposite)
                print(f"Your budget is now {budget}.")
                while True:
                    y = input("Do you want play again? Yes or No\n").lower()
                    if y == "yes":
                        break
                    elif y == "no":
                        exit()
                    else:
                        print("Please enter a valid response.")
            elif x == "outside bet" or x == "outside bets" or x == "outside":
                budget = budget + Outside_bet(deposite)
                print(f"Your budget is now {budget}.")
                while True:
                    y = input("Do you want play again? Yes or No\n").lower()
                    if y == "yes":
                        break
                    elif y == "no":
                        exit()
                    else:
                        print("Please enter a valid response.")
            elif x == "random bets" or x == "random bets" or x == "random":
                budget  = budget + Random_bet(deposite)
                print(f"Your budget is now {budget}.")
                while True:
                    y = input("Do you want play again? Yes or No\n").lower()
                    if y == "yes":
                        break
                    elif y == "no":
                        exit()
                    else:
                        print("Please enter a valid response.")
            else:
                print("Enter opotion from menu!!!")
        except ValueError:
            print("Enter correct syntax!!!")

Ruleta(1000)
