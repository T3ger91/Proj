#dodelat fajtení s kostkama
# funkce která definuje nepratele a jejich zivoty
#main func for fighting 
def enemies():
    def weapons():
        weapons=["fists","baton","knife","pistol","shotgun","smg","m4","rpg"]
        dmg = [5,15,20,25,30,35,40,50,80]
        weapon_dmg_dict = {}
        for i in range(len(weapons)):
           weapon_dmg_dict[weapons[i]] = dmg[i]
        return weapon_dmg_dict
    #Hp init
    def enemies_hp():
        import random
        enemies=["prisoner", "prison guard", "policeman", "swat", "solider"]
        hp = [50, 75, 100, 125, 150]
        weapons()
        enemies_hp_dict = {}
        for i in range(len(enemies)):
            enemies_hp_dict[enemies[i]] = hp[i]
        print(f"you encountered a {random.choice(list(enemies_hp_dict.items()))} = HP and you have {random.choice(list(weapons().items()))} =DMG")
        #keyboard keys init for easy fight 
        def fight_keys():
            print("Press 'f' to fight or 'e' to escape.")
            while True:
                if keyboard.is_pressed('f'):
                    print("You are going to fight him.")
                    kostka1 = (random.randint(1,6))
                    print(f"you got a {kostka1} on your the dice")
                    if kostka1 == {6,5,4}:
                        print("you killed him, great!")
                    if kostka1 =={3,2,1}:
                        print("you got your ass kicked and ran away")
                    return False
                elif keyboard.is_pressed('e'):
                    print("You escaped the fight.")
                    return True
                else:
                    pass
        fight_keys()
        return enemies
    enemies_hp()
    #dmg generation for enemies 
    def enemies_dmg():
        enemies = enemies_hp()
        dmg = [50, 75, 100, 125, 150]
        enemies_dmg_dict = {}
        for i in range(len(enemies)):
            enemies_dmg_dict[enemies[i]] = dmg[i]
    #enemies_dmg()
    #def budget():
        budget = 0
        print(f"you have {budget} $")
    def hp_player():
        hp_player = 100
        return hp_player
