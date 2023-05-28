def russia_roulette(budget):
    import random
    from slow_print import slow_print
    from time import sleep
    z = 0
    term = 0
    while True:
        if budget == 0:
            slow_print("You lost your entier budget foll !!!\nGAME OVER")
            exit()
        if term == 1:
            break
        else:
            if z == 0:
                slow_print("You find yourself before a small table. On it lies a gun. You have a choice to make.\n")
                slow_print("Do you want to risk and play round of Russian roulette? (yes/no):")
            else:
                slow_print("Do you want to risk and play another round of Russian roulette? (yes/no):")
            que = input().lower()
            if que.lower() == "yes":
                slow_print("Interesting choice. Let's see if luck is on your side.\n")
                sleep(3)
                run = random.randint(1, 6)
                if run == 1:
                    print("BANG")
                    slow_print("You got shot... you lose\nGAME OVER") 
                    exit()
                else:
                    slow_print("Great, you didn't get shot. You earned your prize!\n")
                    budget = budget * 6
                    slow_print(f"From now on your budget is {budget}. ")
                    slow_print("Do you want to play another round? (yes/no):")
                    while True:
                        que = input()
                        if que.lower() == "yes":
                            slow_print("Interesting choice. Let's see if luck is on your side again.\n")
                            z = z + 1
                            break
                        elif que.lower() == "no":
                            slow_print("Alright.\n")
                            term = term + 1
                            break
                        else:
                            slow_print("Please answer with a simple yes or no. ")
                    if term == 1:
                        break
            elif que.lower() == "no":
                slow_print("Well, if you say so...\n")
                break
            else:
                slow_print("Please answer with a simple yes or no. ")
    return budget