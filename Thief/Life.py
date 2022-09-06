import Character


answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
player = Character.thief

def Life():
    choice = input("Type SKIP to skip the cutscene or press enter to continue ")
    if choice.lower() == "skip":
        Choice()
    else:
        print ("You open your eyes to see yourself in space")
        input(".")
        print ("A giant blue rift in the sky opens and closes")
        input(".")
        print ("???: You have awoke")
        input(".")
        file = open("CharacterClass.txt","r")
        char = file.read()
        file.close()
        file = open("CharacterName.txt","r")
        Name = file.read()
        file.close()
        print ("???:",Name, "the", char)
        input(".")
        print ("???: I am ALL")
        input(".")
        print ("ALL: Father to ALL-KNOWING")
        input(".")
        print ("ALL: You may have heard i was dead")
        input(".")
        print ("ALL: But as long as there is gods there is me")
        input(".")
        print ("ALL: I created all this. Universes, Life, Death, Power, Order.. EVERYTHING")
        input(".")
        print ("ALL: I am no longer in control as i am now... just a spirit")
        input(".")
        print ("ALL: Through this rift is where i lie")
        input(".")
        print ("ALL: If you was to reach me")
        input(".")
        print ("ALL: You would have to gain a fragment of every universe.")
        input(".")
        print ("A special key that can be forged in the GODS FOUNDRY to unlock this rift")
        input(".")
        print ("THE HEART, my heart to be specific")
        input(".")
        print ("ALL: As it is what was used to create all this")
        input(".")
        print ("ALL: Where i would make my final stand to protect the HEART")
        input(".")
        print ("ALL: If you would win, you would have ORDER")
        input(".")
        print ("ALL: Wait...")
        input(".")
        print ("Shadow Man: So you are alive")
        print ("Shadow Man speaks through your lifeless body. He listened from inside your body")
        input(".")
        print ("ALL: Shadow...")
        input(".")
        print ("ALL: I know your plan")
        input(".")
        print ("ALL: I know how eager you are")
        input(".")
        print ("ALL: To seek ORDER")
        input(".")
        print ("Shadow Man: I seek the ORDER OF DESTRUCTION")
        input(".")
        print ("ALL: Well you know how to get here now as you have been in control of this body")
        input(".")
        print ("Shadow Man: I did what i must. To seek the knowledge")
        input(".")
        print ("ALL: You will not get close to killing all gods ")
        input(".")
        print ("Shadow Man: I hope to speak to you soon, ALL.")
        input(".")
        print ("Shadow Man: After you watch over me, slaughter your daughter.")
        print ("Shadow Man fades away")
        Choice()

def Choice():
    print ("You feel LIFE run through you again")
    input(".")
    print ("You awake in water")
    input(".")
    file = open("CharacterClass.txt","r")
    char = file.read()
    file.close()
    file = open("CharacterName.txt","r")
    Name = file.read()
    file.close() 
    print ("ALL:",Name)  
    input(".")
    print ("ALL: You are the last to be reborn") 
    input(".")
    print ("ALL: Shadow Man will no longer be in control of you")
    input(".")
    print ("ALL: You get your REDEMPTION, THE SECOND CHANCE")
    input(".")
    FLAG = True
    while FLAG == True:
        print ("ALL: Now where do you want to AWAKE")
        print ("A: Monsterverse (Hollow Earth)")
        print ("B: Star Wars (Death Star)")
        choice = input(">>")
        if choice in answer_A:
            if player.char_type == "mage":
                from Mage import Monsterverse
            if player.char_type  == "thief":
                from Thief import Monsterverse
            if player.char_type == "prisoner":
                from Prisoner import Monsterverse
            if player.char_type== "gamer":
                from Gamer import Monsterverse
            if player.char_type == "vagabound":
                from Vagabound import Monsterverse
            if player.char_type== "warrior":
                from Warrior  import Monsterverse
        if choice in answer_B:
            if player.char_type == "mage":
                from Mage import StarWars
            if player.char_type  == "thief":
                from Thief import StarWars
            if player.char_type == "prisoner":
                from Prisoner import StarWars
            if player.char_type== "gamer":
                from Gamer import StarWars
            if player.char_type == "vagabound":
                from Vagabound import StarWars
            if player.char_type== "warrior":
                from Warrior  import StarWars



        



Life()