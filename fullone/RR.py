#main and only one file for Rusian rulet-RR game
#transfering file, with logic with unrepeating games in a row
from transferR import transfer
#func start, no were in use althout by it self 
def russia_roulette():
    import random
    money = []
    money_win = 200
    print("You found yourself before a small table. On it lies a gun. You have a choice to make.")
#main after start logic
    def roulette():
        run = random.randint in (1,6)
        if run == 1:
            print("You got shot...")
        else:
            print("Great, you didn't get shot. You earned your price!")
            print(f"You just won {money_win}.")
            money.append(money_win)
            que = input("Do you want to play another round?")
            while que.lower() != "yes" and que.lower() != "no":
                print("Please answer with a simple yes or no. ")
                que = input("Do you want to risk and play a round of a russian rulette? ")
            if que.lower() == "yes":
                print("Interesting choice. Let's see if luck is on your side again.")
                roulette()
            elif que.lower() == "no":
                print("Alright.")

#story tail 
    def roulette_story():
        que = input("Do you want to risk and play a round of a russian rulette? ")
        while que.lower() != "yes" and que.lower() != "no":
            print("Please answer with a simple yes or no. ")
            que = input("Do you want to risk and play a round of a russian rulette? ")
        if que.lower() == "yes":
            print("Interesting choice. Let's see if luck is on your side.")
            roulette()
        elif que.lower() == "no":
            print("Well, if you say so...")
            transfer()


    roulette_story()



