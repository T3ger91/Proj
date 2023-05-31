#rew version of RR, clouse to be same can be better
#main func for this game can be used as'russia_roulete as RR'
#only in use by struc
def russia_roulette(budget):
    import random
    from slow_print import slow_print
    from time import sleep
    z = 0
    term = 0
    #game logic
    while True:
        #budget works if 0 end if no go a had
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
                slow_print("Do you want to risk and play another round of Russian roulette? (yes/no):\n")
            while True:    
                que = input().lower()
                z = z +1
                if que.lower() == "yes":
                    slow_print("Interesting choice. Let's see if luck is on your side.\n")
                    sleep(3)
                    run = random.randint(1, 6)
                    #ohh u die logic 
                    if run == 1:
                        print("BANG")
                        slow_print("You got shot... you lose\nGAME OVER") 
                        exit()
                    else:
                        slow_print("Great, you didn't get shot. You earned your prize!\n")
                        budget = budget * 6
                        slow_print(f"From now on your budget is {budget}.\n")
                        break
                elif que.lower() == "no":
                    term = term + 1
                    sentences = ["Well, if you say so...", "Alright..."]
                    slow_print(f"{random.choice(sentences)}\n")
                    break
                 #syntax control moment
                else:
                    slow_print("Please answer with a simple yes or no. ")
    return budget