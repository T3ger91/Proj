
def russia_roulette(deposite):
    import random

    def roulette():
        run = random.randint in (1,6)
        if run == 1:
            print("You got shot...")
        else:
            print("Great, you didn't get shot. You earned your price!")
            print(f"You just won {deposite * 6}.")


    def roulette_story():
        print("You found yourself before a small table. On it lies a gun. You have a choice to make.")
        que = input("Do you want to risk and play a round of a russian rulette? ")
        while que.lower() != "yes" and que.lower() != "no":
            print("Please answer with a simple yes or no. ")
            que = input("Do you want to risk and play a round of a russian rulette? ")
        if que.lower() == "yes":
            print("Interesting choice. Let's see if luck is on your side.")
            roulette()
        elif que.lower() == "no":
            print("Why are you so scared?")
            

    roulette_story()
    return deposite

russia_roulette(100)
