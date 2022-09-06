import os,sys
import os.path
import Character as Character# Import character to access character types
import time
import Weapons as Weapons
from Weapons import Lightsaber, Sword
import random
player = Character.warrior

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
DUEL = ["D", "d"]
yes = ["Y", "y", "yes"] 
no = ["N", "n", "no"]
def save(s):
    file=open("loadfile.txt","w")
    file.write(s)
    file.close()

s = "Fallen"
save(s)

def intro():
    print ("MR TIME appears through a portal")
    time.sleep(3)
    print ("MR TIME: I recognise you")
    time.sleep(3)
    print ("Doctor Strange uses his sling ring to hold down MR TIME")
    time.sleep(3)
    print ("MR TIME uses time manipulation to break free and charges down the oblivious doctor strange")
    time.sleep(5)
    print ("Doctor Strange uses the time stone to slow down MR TIME")
    time.sleep(2)
    print ("But being the god of time it does not affect him")
    time.sleep(3)
    print ("He grabs the time stone and smashes it into the ground making it explode")
    time.sleep(4)
    print ("The explosion hits you")
    print ("Everytime there is a '.' you are able to press enter to skip the dialogue")
    input(".")
    print ("MR TIME uses his time ability to prevent any further damage ")
    input(".")
    print ("MR TIME: Shadow Man has reached his final form")
    input(".")
    print ("MR TIME: He plans destruction of ALL life")
    input(".")
    print ("MR TIME: He is going to go from universe to universe to kill and destroy")
    time.sleep(4)
    print ("MR TIME: I have the task of trying to protect EARTH")
    time.sleep(3)
    print ("MR TIME: I have an idea that if it works it could help our cause")
    time.sleep(5)
    print ("MR TIME: I am going to resurrect all of the dead gods. I just need to get to the tombs")
    input(".")
    print ("MR TIME: Can you help me?")
    input(".")
    print ("DOCTOR STRANGE: We will need more of a higher power... Yes i will")
    input(".")
    file = open("CharacterName.txt","r")
    Name = file.read()
    print ("Doctor Strange: ",Name, ",You go explore, see what you can find.")
    time.sleep(5)
    file.close()
    Pub()

def Pub():
    print ("You enter a pub full of EDL members")
    file = open("CharacterSkin.txt","r")
    Skin = file.read()
    if Skin == "White":
        print ("You are invited over to their table")
        input(".")
        print ("One is in a karate costume and called Paul. He leads this group")
        input(".")
        print ("Paul: I have a quest for you to embark on")
        input(".")
        print ("Paul: 'I need you to kill the ni.. ',within seconds the rock smashes his face into a table and takes his face off")
        input(".")
        print ("The EDL Members run away") 
        Rock()
    else:
        print ("They notice you")
        input(".")
        print ("A guy in a karate costume comes over this is PAUL the leader")
        input(".")
        print ("PAUL: Listen up you", Skin , "Cunt")
        input(".")
        print ("PAUL: Your not welcome here")
        input(".")
        print ("You emit your lightsaber and OMG ITS THE ROCK HE ROCK BOTTOMS PAUL THROUGH THE TABLE AND RIPS HIS FACE OFF")
        input(".")
        Rock()

def Rock():
    file = open("CharacterName.txt","r")
    Name = file.read()
    print ("The Rock: Hello again", Name)
    input(".")
    print ("The Rock: Sauron has started to attack Earth considering he already has middle earth")
    input(".")
    print ("The Rock: That Kavu would destroy him")
    print (Name, ": I had a rough first encounter with him. I watched Shadow Man free him it was like he knew he was there")
    input(".")
    print ("The Rock: He probably did, locked in the underworld since the beginning of time he was born to rule")
    input(".")
    print ("The Rock: Now he is going to be able to eat more and get stronger")
    input(".")
    print ("The Rock: He could easily just destroy us all")
    input(".")
    print ("You both walk around a corner and see people getting hung")
    input(".")
    print ("You turn around to see vecna approach you both")
    input(".")
    print ("Vecna: Where is he?")
    input(".")
    print ("The Rock: Who?")
    input(".")
    print ("Vecna: Shadow Man")
    print ("Vecna: He ran away last time. now there will be no more running")
    input(".")
    print ("Vecna picks up a car")
    time.sleep(3)
    print ("and throws it at the shadows")
    time.sleep(4)
    print ("Shadow Man materialises in front of him and they begin to fight")
    input(".")
    print ("The Rock: London is falling")
    input(".")
    print ("A lion comes and attacks the Rock")
    print ("THE ROCK: RUN!!")
    input(".")
    print ("You make a run for your life and find yourself stuck on where to go")
    RoadmanScrap()

def RoadmanScrap():
    print ("You get approached by a roadman")
    time.sleep(3)
    print ("It appears you walked down the wrong street")
    Roadman = 30
    HP = player.health * 100
    while Roadman >=  0:
        Ket = random.randint(1,6)
        if Ket == 6:
            RoadmanSpeed = 1000
        else:
            RoadmanSpeed = 4
        if player.speed > RoadmanSpeed:
            print ("ROADMAN:", Roadman)
            print ("HP:", HP)
            print ("A: Lightsaber Slash")
            print ("B: Lightsaber Throw")
            choice = input(">>")
            if choice in answer_A:
                print ("You two hand your lightsaber and slash down at the roadman")
                Slash = 50
                print ("{",Slash,"}")
                Roadman = Roadman - Slash
            if choice in answer_B:
                print ("You throw your lightsaber at the roadman but you dont have the force to bring it back to you so you quickly roll and grab your saber")
                Throw = 1000
                print ("{",Throw,"}")
                Roadman = Roadman - Throw
            print ("The roadman jumps and shanks you in the chest you begin to bleed")
            Bleed = True
            shank = random.randint(30,50)
            HP = HP - shank
            print ("{",shank,"}")
            if Bleed == True:
                Bleeding = random.randint(20,40)
                print ("{",Bleeding,"}")
                HP = HP - Bleeding
        else:
            print ("The roadman jumps and shanks you in the chest you begin to bleed")
            Bleed = True
            shank = random.randint(30,50)
            HP = HP - shank
            print ("{",shank,"}")
            if Bleed == True:
                Bleeding = random.randint(20,40)
                print ("{",Bleeding,"}")
                HP = HP - Bleeding
            print ("ROADMAN:", Roadman)
            print ("HP:", HP)
            print ("A: Lightsaber Slash")
            print ("B: Lightsaber Throw")
            choice = input(">>")
            if choice in answer_A:
                print ("You two hand your lightsaber and slash down at the roadman")
                Slash = 50
                print ("{",Slash,"}")
                Roadman = Roadman - Slash
            if choice in answer_B:
                print ("You throw your lightsaber at the roadman but you dont have the force to bring it back to you so you quickly roll and grab your saber")
                Throw = 1000
                print ("{",Throw,"}")
                Roadman = Roadman - Throw
        if HP <= 0:
            print ("YOU DIED")
            time.sleep(3)
            RoadmanScrap()
    file = open("Kills.txt","r")
    lines = file.readlines()

    for line in lines:
        for c in line:
            if c.isdigit() == True:
                c = (int(c)) + 1
                file.close
    file = open("Kills.txt","w")
    file.write((str(c)))
    file.close()
    print ("It seems the canada goose coat didnt provide much protection")
    input(".")
    print ("You begin your exploration on London")
    London()

def London():
    player.equipped = Lightsaber
 #map
    dungeonMap = [["0","0","0","0","0","0","0","0","0"],
                  ["0",".",".",".",".",".","O",".","0"],
                  ["0",".",".",".",".",".",".",".","0"],
                  ["S",".",".",".",".",".",".",".","0"],
                  ["0","",".",".",".",".",".","K","0"],
                  ["0",".",".",".",".",".",".",".","0"],
                  ["0",".",".",".","V",".",".","E","0"],
                  ["0","0","0","0","0","0","0","0","0"]]

    playerMap  = [[".",".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".","S",".","."],
                  [".",".",".",".",".",".",".",".","."],
                  ["S",".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".",".","K","."],
                  [".",".",".",".",".",".",".",".","."],
                  [".",".",".",".","V",".",".","E","."],
                  [".",".",".",".",".",".",".",".","."]]


    #Displaying the map
    def displayMap(maps):
        for x in range(0,8):
            print(maps[x])

    #selecting a map
    mapChoice = dungeonMap

    displayMap(playerMap)

    #initialising the players position
    position = mapChoice[0][0]

    def main(mapChoice, playerMap, position):
        #players starting position
        x = 0
        y = 3
        #players inventory
        Steps = 0
        Vader = False
        ShadowMan = True
        Sauron = True
        Orc1Dead = False
        Orc2Dead = False
        Kavu = True
        
        print(mapChoice[y][x])
        position = 0
        while position != "E":
            
            previousX = x
            previousY = y

            movement = input("N,S,E,W,MAP").upper()

            if movement == "N":
                y = y-1
                Steps = Steps + 1

            if movement == "S":
                y = y+1
                Steps = Steps + 1

            if movement == "E":
                x = x+1
                Steps = Steps + 1

            if movement == "W":
                x = x-1
                Steps = Steps + 1

            if movement == "MAP":
                displayMap(playerMap)

            position = mapChoice[y][x]
            playerMap[y][x] = "X"
            
            if position == "0" or position == "1":
                print("Shadow Man has created a dark barrier to prevent anyone getting through to where he is fighting Vecna")
                x = previousX
                y = previousY
                position = mapChoice[y][x]


            if position == ".":
                print("This area is clear")
            
            if position == "V":
                if Vader == False:
                    print ("You see Vader using the force to rid of the orcs")
                    input(".")
                    print ("He senses his lightsaber and uses the force to take it from you")
                    time.sleep(5)
                    print ("Vader: My lightsaber..")
                    input(".")
                    print ("Vader: You took my lightsaber")
                    input(".")
                    print ("Vader force pushes you through a building")
                    player.equipped = Sword
                    Vader = True
                else:
                    print ("Lets not go back there shall we")
                    

            if position == "O":
                if Sauron == False:
                    print ("You look upon the thousands of dead civilians and orcs")
                    position = mapChoice[y][x]
                else:
                    Orc1 = 100
                    Orc2 = 500
                    HP = player.health * 100
                    print ("You bump into two orcs")
                    while Orc1 or Orc2 >= 0:
                        print ("Orc:", Orc1)
                        print ("Orc:", Orc2)
                        print ("HP:", HP)
                        if player.equipped == Lightsaber:
                            print ("A: Lightsaber Slash")
                            print ("B: Lightsaber Throw")
                            choice = input(">>")
                            if choice in answer_A:
                                print ("A: ORC")
                                print ("B: ORC")
                                Choice = input(">>")
                                if Choice in answer_A:
                                    print ("You two hand your lightsaber and slash down at the orc")
                                    Slash = 100
                                    print ("{",Slash,"}")
                                    Orc1 = Orc1 - Slash
                                if Choice in answer_B:
                                    print ("You two hand your lightsaber and slash down at the orc")
                                    Slash = 100
                                    print ("{",Slash,"}")
                                    Orc2 = Orc2 - Slash                                
                            if choice in answer_B:
                                print ("You throw your lightsaber at the orcs and it cuts through them both")
                                Throw = 1000
                                print ("{",Throw,"}")
                                Orc1 = Orc1 - Throw
                                Orc2 = Orc2 - Throw
                            if Orc1 <= 0:
                                if Orc1Dead == True:
                                    print ("")
                                else:
                                    print ("You decapitate the orc")
                                    Orc1Dead = True
                            else:
                                print ("The orc stabs a dagger through your hand")
                                Dagger = random.randint(25,100)
                                print ("{",Dagger,"}")
                                HP = HP - Dagger
                            if Orc2 <= 0:
                                if Orc2Dead == True:
                                    print ("")
                                else:
                                    print ("The Lightsaber burns through the orc")
                                    Orc2Dead = True
                            else:
                                print ("The Orc shoots a crossbow into your chest")
                                Bullseye = random.randint(140,400)
                                print ("{",Bullseye,"}")
                                HP = HP - Bullseye
                            if Orc1 and Orc2 <= 0:
                                break
                        else:
                            print ("A: Light Attack")
                            print ("B: Heavy Attack")
                            choice = input(">>")
                            if choice in answer_A:
                                print ("A: ORC")
                                print ("B: ORC")
                                Choice = input(">>")
                                if Choice in answer_A:
                                    print ("You slice through the guts of the orc")
                                    Slash = 100
                                    print ("{",Slash,"}")
                                    Orc1 = Orc1 - Slash
                                if Choice in answer_B:
                                    print ("You headbutt and stab the chest of the orc")
                                    Slash = 100
                                    print ("{",Slash,"}")
                                    Orc2 = Orc2 - Slash                                
                            if choice in answer_B:
                                print ("You decapitate the orc and use is crossbow to shoot the other orc")
                                Throw = 1000
                                print ("{",Throw,"}")
                                Orc1 = Orc1 - Throw
                                Orc2 = Orc2 - Throw
                            if Orc1 <= 0:
                                if Orc1Dead == True:
                                    print ("")
                                else:
                                    print ("You decapitate the orc")
                                    Orc1Dead = True
                            else:
                                print ("The orc stabs a dagger through your hand")
                                Dagger = random.randint(25,100)
                                print ("{",Dagger,"}")
                                HP = HP - Dagger
                            if Orc2 <= 0:
                                if Orc2Dead == True:
                                    print ("")
                                else:
                                    print ("The Lightsaber burns through the orc")
                                    Orc2Dead = True
                            else:
                                print ("The Orc shoots a crossbow into your chest")
                                Bullseye = random.randint(140,400)
                                print ("{",Bullseye,"}")
                                HP = HP - Bullseye
                            if Orc1 and Orc2 <= 0:
                                break
                    print ("You head towards Sauron")
                    file = open("Kills.txt","r")
                    lines = file.readlines()

                    for line in lines:
                        for c in line:
                            if c.isdigit() == True:
                                c = (int(c)) + 2
                                file.close
                    file = open("Kills.txt","w")
                    file.write((str(c)))
                    file.close()
                    print ("Iron Man crashes down and beams the orcs that are coming from all angles")
                    input(".")
                    print ("Thats until")
                    input(".")
                    print ("Ogbog stands in his way")
                    input(".")
                    print ("Ogbog shadow steps around iron man getting behind him to stab him with his darksword")
                    input(".")
                    print ("Ogbog slices at both his legs making him unable to stand up")
                    input(".")
                    print ("Ogbog lifts his sword up and gets hit by the hammer of thor")
                    input(".")
                    print ("Ogbog vanishes but then Kratos appears and attacks Thor")
                    input(".")
                    print ("Kratos lifts him up and throws him at a wall")
                    input(".")
                    print ("Thor throws his hammer at Kratos who tries to hold it back using his strength")
                    input(".")
                    print ("He isnt worthy to lift it but he has the strength to hold it in place.. but for how long")
                    input(".")
                    print ("Thor sends a lightning strike onto Kratos and calls back his hammer")
                    input(".")
                    print ("Sauron makes his way over and ducks as the screeching sounds of Kavu can be heard in the sky as he flies over")
                    input(".")
                    print ("A military barrage is sent into the area and everyone is forced to run")
                    Sauron = False
            
            if position == "K":
                if Kavu == False:
                    print ("You see the collapsed bridge and the frozen river")
                    position = mapChoice[y][x]
                else:
                    print ("You are on London Bridge and can see Kavu eating away at what he can find")
                    input(".")
                    print ("A military jet flies over and shoots missiles at Kavu")
                    input(".")
                    print ("Kavu absorbs the energy emmitted from the missile and lets out a scream also emitting a lightning beam")
                    input(".")
                    print ("You quickly run past and can see hundreds of jets flying towards the beast")
                    input(".")
                    print ("The jets keep Kavu under heavy fire so that a missile can hit the bridge they are going to make Kavu fall with it")
                    input(".")
                    print ("Kavu flaps his wings letting out high speed winds that make the jets crash into each other")
                    input(".")
                    print ("Kavu spins around creating a tornado. He fires many beams into the sky.")
                    input(".")
                    print ("Meteors start crashing down into london because of this, but it is too slow as a missile connects with the bridge that is powerful enough to collapse it")
                    input(".")
                    print ("Kavu falls with the bridge and sinks into the water below he fires a ice beam that freezes all the river thames")
                    Kavu = False

        print ("You make your way to downing street to confront Boris Johnson")
        input(".")
        print ("Boris has gone rogue and has been driven to insanity")
        input(".")
        print ("Boris now seeks powers to combat these threats and protect his country")
        input(".")
        print ("He became a vessel to the Shadow Man and gained the power to protect himself")
        input(".")
        print ("He didnt care for anyone else he just watnted to make sure he was safe")
        input(".")
        print ("You find him outside of Downing Street and ready yourself for battle")
        if player.equipped == Lightsaber:
            print ("Boris shatters the lightsaber in your hand forcing you to wield your sword")
            player.equipped = Sword
        print ("Boris throws a shadow ball at you and you absorb it")
        input(".")
        print ("You still have the aura of shadow man in you")
        input(".")
        print ("It explains how you are so strong")
        input(".")
        print ("You chop off both of Boris' hands")
        input(".")
        print ("Shadow Man comes from out of nowhere and takes his head clean off")
        input(".")
        print ("You drop to the floor")
        HP = 5
        print ("HP",HP)
        time.sleep(1)
        HP = 4
        print ("HP",HP)
        time.sleep(1)
        HP = 3
        print ("HP",HP)
        time.sleep(1)
        HP = 2
        print ("HP",HP)
        time.sleep(1)
        HP = 1
        print ("HP",HP)
        time.sleep(1)
        HP = 0.9
        print ("HP",HP)
        time.sleep(1)
        HP = 0.75
        print ("HP",HP)
        time.sleep(1)
        HP = 0.5
        print ("HP",HP)
        time.sleep(1)
        HP = 0.25
        print ("HP",HP)
        time.sleep(3)
        HP = 0.2
        print ("HP",HP)
        time.sleep(3)
        HP = 0.1
        print ("HP",HP)
        time.sleep(4)
        print ("Shadow Man: No ")
        HP = 0.0001
        print ("HP",HP)
        time.sleep(1)
        print ("Shadow Man: You won't die.")
        input(".")
        print ("Shadow Man: I am sorry i used you as a puppet")
        input(".")
        print ("Shadow Man: to get where i need to be")
        input(".")
        print ("Shadow Man: But you can no longer be apart of me")
        input(".")
        print ("Shadow Man: I will free you")
        input(".")
        print ("Shadow Man: No more curse")
        input(".")
        time.sleep(2)
        print ("Shadow Man slowly slits your throat with his blade")
        input(".")
        file = open("CharacterName.txt","r")
        Name = file.read()
        print ("{-9999999}")
        time.sleep(1)
        print ("Shadow Man: Goodbye for now..")
        time.sleep(2)
        print ("Shadow Man:", Name)
        time.sleep(1)
        HP = 0
        print ("HP",HP)
        if player.char_type == "mage":
            from Mage import Life
        if player.char_type  == "thief":
            from Thief import Life
        if player.char_type == "prisoner":
            from Prisoner import Life
        if player.char_type== "gamer":
            from Gamer import Life
        if player.char_type == "vagabound":
            from Vagabound import Life
        if player.char_type== "warrior":
            from Warrior  import Life




            


    
    
    main(mapChoice, playerMap, position) 



     

intro()

                        







            
    


        

