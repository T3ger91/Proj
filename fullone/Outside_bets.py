#outsidebets function, cant be separated from: inside bets,bets,ruleta
from slow_print import slow_print
from slow_printRL import slow_printRL
#func name can be used by this name
#in use by Ruleta.py
def Outside_bet(deposite):
    import random
    from time import sleep
    #all types of bets in game
    start_sentence =["What do you want to choose", "What do you want to bet on?"]
    bets = ["Value of numbers, Odd or Even numbers, Color of number, Column of numbers, Dozen of numbers", 
            "Red/Black bet, Odd/Even bet, High/Low bet, Dozen bet, Column bet"]
    slow_printRL("    _\n   / |------------------------------------------------------------|-----------------|\n  /  [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36] |third column  |                 |\n < 0 [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35] |second column |    Win: 2:1     |\n  \  [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34] |first column  |                 |\n   \_|---------------------------------------------|--------------|                 |\n     |  1. Dozen  |   2. Dozen     |   3. Dozen    | Probability of winning: 32,43% |\n     |------------|----------------|---------------|--------------------------------|\n     | 1 to 18 | even | red | black | odd |19 to 36| Probability of winning: 48,65% |\n     |---------------------------------------------| Win: 1:1                       |\n                 |---------------------|           |--------------------------------|\n                 |       0 = green     |\n                 | Even number = Black |\n                 |   Odd number = Red  |\n                 |---------------------|\n ")
    choice = input(f"{random.choice(start_sentence)}: {random.choice(bets)}? \n").lower()
    
    number = random.randint(0,36)
    if number == 0:
        color = "Green"
    else:
        if number % 2 == 0:
            color = "Balck"
        else:
            color = "Red"
    #rulet structure in console
    column1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
    column2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    column3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
    #giveme the number and lets go to play 
    if choice == "value of numbers" or choice == "value of number" or choice == "value" or choice == "high/low bet" or choice == "high" or choice == "low":#
        while True:
            slow_print("What do you want to bet on?\nHigh numbers or Low numbers: ")
            choice_type = input().lower()
            if choice_type == "high numbers" or choice_type == "high number" or choice_type == "high" or choice_type == "higher" :#
                if number in range(19,36):
                    sleep(1)
                    slow_print(f"{color} {number} came up you win! Your deposit has been doubled! " )
                    deposite = deposite * 2
                    #print(deposite)
                    break
                else:
                    sleep(1)
                    print(f"{color} {number} came up you lose! You lost your deposit")
                    deposite = 0
                    #print(deposite)
                    break
            #low numbers bet logic 
            if choice_type == "low number" or choice_type == "low numbers" or choice_type == "low" or choice_type == "lower":#
                if number in range(1,18):
                    sleep(1)
                    slow_print(f"{color} {number} came up you win! Your deposit has been doubled." )
                    deposite = deposite * 2
                    #print(deposite)
                    break
                else:
                    #lose sentense 
                    sleep(1)
                    slow_print(f"{color} {number} came up you lose! You lost your deposit")
                    deposite = 0
                    #print(deposite)
                    break
            else: 
                print("=" * 40)
                print("Enter the correct syntax:")
            #odd or even number rolls 
    if choice == "odd or even number" or choice == "odd or even numbers" or choice == "odd" or choice == "even" or choice == "odd/even bet"  :#
        while True:
            slow_print("Do you want to bet on odd or even number?  ")
            choice_type = input().lower()
            if choice_type == "odd numbers" or  choice_type == "odd number" or choice_type == "odd" :#
                if number %2 != 0:
                    sleep(1)
                    slow_print(f"{color} {number} came up. Great choice! Your deposite has been doubled! ")
                    deposite = deposite * 2
                    #print(deposite)
                    break
                else:
                    sleep(1)
                    slow_print(f"{color} {number} came up you lose! You lost your deposit")
                    deposite = 0
                    #print(deposite)
                    break
            if choice_type == "even nuumber" or choice_type== "even numbers" or choice_type== "even" :#
                #win sentense
                if number %2 == 0:
                    sleep(1)
                    slow_print(f"{color} {number} came up you win! Your deposit has been doubled." )
                    deposite = deposite * 2
                    #print(deposite)
                    break
                else:
                    sleep(1)
                    slow_print(f"{color} {number} came up. Wrong choice! You lost your deposit")
                    deposite = 0
                    #print(deposite)
                    break
            else:
                print("=" * 40)
                print("Enter the correct syntax:")
            #color of numbers, bets on black / red
    if choice == "color of number" or choice == "color of numbers" or choice == "color" or choice == "red/black bet" or choice == "red" or choice == "black" :
        while True:
            slow_print("What is your lucky color red or black? ")
            choice_type = input().lower()
            if choice_type == "red":
                if color == "Red":
                    sleep(1)
                    slow_print(f"{color} {number} came up. Great choice! Your deposite has been doubled! ")
                    deposite = deposite * 2
                    #print(deposite)
                    break
                else:
                    sleep(1)
                    slow_print(f"{color} {number} came up. Wrong choice! You lost your deposit")
                    deposite = 0
                    #print(deposite)
                    break
            if choice_type == "black":
                if color == "Black":
                    sleep(1)
                    slow_print(f"{color} {number} came up. Great choice! Your deposite has been doubled! ")
                    deposite = deposite * 2
                    #print(deposite)
                    break
                else:
                    sleep(1)
                    slow_print(f"{color} {number} came up. Wrong choice! You lost your deposit")
                    deposite = 0
                    #print(deposite)
                    break    
            else:
                print("=" * 40)
                print("Enter the correct syntax:")
    if choice == "column of numbers" or choice == "column of number" or choice == "column":
        while True:
            slow_print("What is your lucky Column ? First, Second or Third ?  ")
            choice_type = input().lower()
            if choice_type == "first column" or choice_type == "1. column" or choice_type == "column1" or choice_type == "column 1" or choice_type == "first":
                if number in column1:
                    sleep(1)
                    slow_print(f"{color} {number} came up. Great choice! Your deposite has been tripled! ")
                    deposite = deposite * 3
                    #print(deposite)
                    break
                else:
                    sleep(1)
                    slow_print(f"{color} {number} came up. Wrong choice! You lost your deposit")
                    deposite = 0
                    #print(deposite)
                    break
            if choice_type == "second column" or choice_type == "2. column" or choice_type == "column2" or choice_type == "column 2" or choice_type == "second":
                if number in column2:
                    sleep(1)
                    slow_print(f"{color} {number} came up. Great choice! Your deposite has been tripled! ")
                    deposite = deposite * 3
                    #print(deposite)
                    break
                else:
                    sleep(1)
                    slow_print(f"{color} {number} came up. Wrong choice! You lost your deposit")
                    deposite = 0
                    #print(deposite)
                    break
            if choice_type == "third column" or choice_type == "3. column" or choice_type == "column3" or choice_type == "column 3" or choice_type == "third":
                if number in column3:
                    sleep(1)
                    slow_print(f"{color} {number} came up. Great choice! Your deposite has been tripled! ")
                    deposite = deposite * 3
                    #print(deposite)
                    break
                else:
                    sleep(1)
                    slow_print(f"{color} {number} came up. Wrong choice! You lost your deposit")
                    deposite = 0
                    #print(deposite)
                    break
            else:
                print("=" * 40)
                print("Enter the correct syntax:")
    #3 parts of rulet, bets on dozen, logic for them as well 
    if choice == "dozen of numbers" or choice == "dozen of number" or choice == "dozen":
        while True:
            slow_print("What is your lucky Dozen of numbers ? First, Second or Third ?  ")
            choice_type = input().lower()
            if choice_type == "first dozen of numbers" or choice_type == "first dozen of number" or choice_type == "dozen1" or choice_type == "dozen 1" or choice_type == "first" or choice_type == "first dozen" or choice_type == "1. dozen" :
                if number >= 1 and number <= 12:
                    sleep(1)
                    slow_print(f"{color} {number} came up. Great choice! Your deposite has been tripled! ")
                    deposite = deposite * 3
                    #print(deposite)
                    break
                else:
                    sleep(1)
                    slow_print(f"{color} {number} came up. Wrong choice! You lost your deposit")
                    deposite = 0
                    #print(deposite)
                    break
            if choice_type == "second dozen of numbers" or choice_type == "second dozen of number" or choice_type == "dozen2" or choice_type == "dozen 2" or choice_type == "second" or choice_type == "second dozen" or choice_type == "2. dozen" :
                if number >= 13 and number <= 24 :
                    sleep(1)
                    slow_print(f"{color} {number} came up. Great choice! Your deposite has been tripled! ")
                    deposite = deposite * 3
                    #print(deposite)
                    break
                else:
                    sleep(1)
                    slow_print(f"{color} {number} came up. Wrong choice! You lost your deposit")
                    deposite = 0
                    #print(deposite)
                    break
            if choice_type == "third dozen of numbers" or choice_type == "third dozen of number" or choice_type == "dozen3" or choice_type == "dozen 3" or choice_type == "third" or choice_type == "third dozen" or choice_type == "3. dozen" :
                if number >= 25 and number <= 36:
                    sleep(1)
                    slow_print(f"{color} {number} came up. Great choice! Your deposite has been tripled! ")
                    deposite = deposite * 3
                    #print(deposite)
                    break
                else:
                    sleep(1)
                    slow_print(f"{color} {number} came up. Wrong choice! You lost your deposit")
                    deposite = 0
                    #print(deposite)
                    break
            else:
                print("=" * 40)
                print("Enter the correct syntax:")
    return deposite
if __name__ == "__main__":
    print("Tento kod se spusti pouze tehdy když jse spuštěn jako hlavní program")
