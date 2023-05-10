def slots():
    import random
    print ("In the room you see an old slot machine.")

    def slots_story():
        que = input("Do you want to play? ")
        while que.lower() != "yes" and que.lower() != "no":
            print("Please answer with a simple yes or no. ")
            que = input("Do you want to play? ")

        if que.lower() == "no":
            print("Too bad I guess... ") 
            exit()

        elif que.lower() == "yes":
            print("Great.")

            bet_per3 = {1: 0.9, 2 : 0.9, 3 : 0.9, 4 : 0.8, 5: 0.7, 6 : 1.7}
            bet_per2 = {1: 0.5, 2 : 0.4, 3 : 0.6, 4 : 0.4, 5: 0.5, 6 : 1.0}
            def slots_r():
                a = random.randint(1,6)
                b = random.randint(1,6)
                c = random.randint(1,6)
            
                def money_win3():
                    return bet + (bet * bet_per3.get(a))
            
                def money_win2a():
                    return bet + (bet * bet_per2.get(a))

                def money_win2b():
                    return bet + (bet * bet_per2.get(b))
            
                print(a, b, c)
                if a == b and a == c:
                    print("Nice")
                    print(f"You won {money_win3()}.")
                    slots_story()


                elif a == b or a == c:
                    print("Two are the same.")
                    print(money_win2a())
                    slots_story()

                elif b == c: 
                    print(f" You won {money_win2b()}. ")
                    slots_story()

                else:
                    print("you lost ")
                    slots_story()

            while True:
                try:
                    bet = int(input("How much do you want to bet? You can bet between 1 and 100 "))
                    if bet >1 and  bet < 100:
                        print("This is by how much more percentagewise you can win with different numbers")
                        print("For three of the same symbol: ")
                        for i,y in bet_per3.items():
                            print(f" {i} + {int(float(y) * 100) } % of your bet")
                        print("For two of the same symbol: ")
                        for i,y in bet_per2.items():
                            print(f" {i} + {int(float(y) * 100) } % of your bet")
                        slots_r()
                    else:
                        print("Enter a bet in between 1 and 100")
                except ValueError:
                    print("Enter a valid NUMBER!")         
    slots_story()

slots()