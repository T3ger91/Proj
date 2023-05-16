#dodelat fajtení s kostkama
# funkce která definuje nepratele a jejich zivoty
#main func for fighting

import random

def enemies():
    def weapons():
        weapons = ["fists", "baton", "knife", "pistol", "shotgun", "smg", "m4", "rpg"]
        dmg = [5, 15, 20, 25, 30, 35, 40, 50, 80]
        weapon_dmg_dict = {}
        for i in range(len(weapons)):
            weapon_dmg_dict[weapons[i]] = dmg[i]
        return weapon_dmg_dict

    def enemies_hp():
        enemies = ["prisoner", "prison guard", "policeman", "swat", "soldier"]
        hp = [50, 75, 100, 125, 150]
        weapons()
        enemies_hp_dict = {}
        for i in range(len(enemies)):
            enemies_hp_dict[enemies[i]] = hp[i]
        enemy = random.choice(list(enemies_hp_dict.items()))
        weapon = random.choice(list(weapons().items()))
        print(f"You encountered a {enemy[0]} = HP: {enemy[1]} and you have {weapon[0]} = DMG: {weapon[1]}")

    def fight():
        print("Press 'f' to fight or 'e' to escape.")
        while True:
            choice = input("Enter your choice: ")
            if choice == 'f':
                print("You are going to fight.")
                dice_roll = random.randint(1, 6)
                print(f"You rolled a {dice_roll} on the dice.")
                if dice_roll >= 4:
                    print("You killed the enemy. Great!")
                else:
                    print("You got your ass kicked and ran away.")
                break
            elif choice == 'e':
                print("You escaped the fight.")
                break
            else:
                print("Invalid choice. Try again.")

    enemies_hp()
    fight()


