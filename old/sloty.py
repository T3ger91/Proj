def slots():
    import random
    print ("In the room you an old slot machine.")

    def slots_story():
        que = input("Do you want to play? ")
        while que.lower() != "yes" and que.lower() != "no":
            print("Please answer with a simple yes or no. ")
            que = input("Do you want to play? ")

        if que.lower() == "no":
            print("Too bad I guess... ")
        
        elif que.lower() == "yes":
            print("Great.")

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
                

            slots_story()


        bet_per3 = {1: 0.7, 2 : 0.6, 3 : 0.4, 4 : 0.5, 5: 0.4, 6 : 1.0}
        bet_per2 = {1: 0.2, 2 : 0.2, 3 : 0.3, 4 : 0.2, 5: 0.3, 6 : 0.5}
        bet = int(input("How much do you want to bet? You can bet between 1 and 100 "))
        print("This is by how much more you can win with different numbers")
        print("For three of the same symbol: ")
        for i,y in bet_per3.items():
            print(f" {i} * {int(float(y) * 100) } %")
        print("For two of the same symbol: ")
        for i,y in bet_per2.items():
            print(f" {i} * {int(float(y) * 100) } %")

        

        slots_r()
    slots_story()
slots()