def Inside_bet(deposite):
    import random
    from time import sleep
    start_sentence =["What do you want to choose", "What do you want to bet on?"]
    bets = ["Straight up bet, Split bet, Street bet, Corner bet, Line bet or Zero bet", "Zero, one, two, three, four, or six numbers next to each other ?" ]
    print("    _\n   / |---------------------------------------------|\n  /  | 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36 |\n < 0 | 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35 |\n  \  | 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34 |\n   \_|---------------------------------------------|\n     | Straight Up bet | Chance: 2,70%  | Win: 35:1|\n     | Zero bet        | Chance: 2,70%  | Win: 35:1|\n     | Split bet       | Chance: 5,41%  | Win: 17:1|\n     | Street bet      | Chance: 8,11%  | Win: 11:1|\n     | Corner bet      | Chance: 10,81% | Win: 8:1 |\n     | Line bet        | Chance: 16,22% | Win: 5:1 |\n     |---------------------------------------------|")
    def more_than_one_numbers_bet(x,y):
        import random
        from time import sleep
        while True:
            number = random.randint(0,36)
            if number == 0:
                color = "Green"
            else:
                if number % 2 == 0:
                    color = "Balck"
                else:
                    color = "Red"
            try:
                pole = []
                choice_type = input("Enter you lucky numbers in row separated by a comma: ")
                stringpole = choice_type.split(",")
                for i in stringpole:
                    pole.append(int(i))
                if int(i) > 36:
                    print("*" * 40)
                    print("Enter the number on the roulette wheel!")
                elif len(pole) > x:
                    print("*" * 40)
                    print("Enter onely two numbers in row on the roulette wheel!")               
                else:       
                    if number in pole:
                        sleep(1)
                        print(f"{color} {number} came up you win! Your deposit was increased 36 times!")
                        deposite =  deposite * y
                        #print(deposite)
                        break
                    else:
                        sleep(1)
                        print(f"{color} {number} came up you lose! You lost your deposit")
                        deposite = deposite * 0
                        #print(deposite)
                        break
            except ValueError:
                print("*" * 40)
                print("Enter correct syntax")
    while True:
        choice = input(f"{random.choice(start_sentence)}: {random.choice(bets)}? \n").lower()
        if choice == "one" or choice == "1" or choice == "one number" or choice == "straight up bet" or choice == "straight up" or choice == "straight":#
            while True:
                number = random.randint(0,36)
                if number == 0:
                    color = "Green"
                else:
                    if number % 2 == 0:
                        color = "Balck"
                    else:
                        color = "Red"
                try:
                    choice_type = int(input("Enter you lucky number: ")) 
                    if choice_type > 36:
                        print("*" * 40)
                        print("Enter the number on the roulette wheel!")
                    else:       
                        if choice_type == number:
                            sleep(1)
                            print(f"{color} {number} came up you win! Your deposit was increased 36 times!")
                            deposite = deposite * 36
                            #print(deposite)
                            break
                        else:
                            sleep(1)
                            print(f"{color} {number} came up you lose! You lost your deposit")
                            deposite = deposite * 0
                            #print(deposite)
                            break
                except ValueError:
                    print("*" * 40)
                    print("Enter correct syntax")
            break
        if choice == "zero" or choice == "zero bet" or choice == "0" or choice == "0 bet" or choice == "zero number" or choice == "0 number":
            while True:
                number = random.randint(0,36)
                if number == 0:
                    color = "Green"
                else:
                    if number % 2 == 0:
                        color = "Balck"
                    else:
                        color = "Red"

                if number == 0:
                    sleep(1)
                    print(f"{color} {number} came up you win! Your deposit was increased 36 times!")
                    deposite = deposite * 36
                    #print(deposite)
                    break
                else:
                    sleep(1)
                    print(f"{color} {number} came up you lose! You lost your deposit")
                    deposite = deposite * 0
                    #print(deposite)
                    break
            break
        if choice == "2" or choice == "two" or choice == "two number" or choice == "split bet" or choice == "split":
            x = 2
            y = 16
            more_than_one_numbers_bet(x,y)
            break
        if choice == "3" or choice == "three" or choice == "three number" or choice == "street bet"  or choice == "street":
            x = 3
            y = 12
            more_than_one_numbers_bet(x,y)
            break
        if choice == "4" or choice == "four" or choice == "four number" or choice == "corner bet" or choice == "corner":
            x = 4
            y = 9
            more_than_one_numbers_bet(x,y)
            break
        if choice == "6" or choice == "six" or choice == "six number" or choice == "line bet" or choice == "line":
            x = 6
            y = 6
            more_than_one_numbers_bet(x,y)
            break
        else:
            print("Chose the option from menu: ")
    return deposite
            
if __name__ == "__main__":
    print("Tento kod se spusti pouze tehdy když jse spuštěn jako hlavní program")