#cant be separated from: inside bets,bets,ruleta
#random bet for ruleta game, main file RR.py
def Random_bet(deposite):
    from slow_print import slow_print
    import random
    from time import sleep
    #random choises
    slow_print(f"On what numbers do you want to bet on ?\nLimit for the input is 18 numbers in a row and separated by comma, like : *1,2*,and same numbers cant be entered more than once.\n")
    choice = input()
    #logic for it with chances
    while True:
        #random num and color 
        number = random.randint(0,36)
        if number == 0:
            color = "Green"
        else:
            if number % 2 == 0:
                color = "Balck"
            else:
                color = "Red"
                #wrighting func 
        try:
            pole = []
            stringpole = choice.split(",")
            for i in stringpole:
                 pole.append(int(i))
            win = 36 / len(pole)
            if int(i) > 36:
                print("*" * 40)
                print("Enter the number on the roulette wheel!")
                #win/lose logic, simple as hell: a is your num, b is random num, if a=b u win, if a/=/b u lose 
            else:       
                if number in pole:
                    sleep(1)
                    slow_print(f"{color} {number} came up you win! Your deposit was increased {win} times!")
                    deposite = deposite * win
                    #print(deposite)
                    break
                else:
                    sleep(1)
                    slow_print(f"{color} {number} came up you lose! You lost your deposit")
                    deposite = 0
                    #print(deposite)
                    break
                    #excepting error form syn 
        except ValueError:
            print("*" * 40)
            print("Enter correct syntax")
    return deposite               
    
if __name__ == "__main__":
    print("Tento kod se spusti pouze tehdy když jse spuštěn jako hlavní program")
