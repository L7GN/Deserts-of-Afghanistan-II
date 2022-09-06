import os,sys
import os.path
import Character as Character# Import character to access character types
import time
import Weapons as Weapons
from Weapons import Lightsaber, Sword
import random
player = Character.mage

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

s = "Monsterverse"
save(s)

def Intro():
    print ("You wake up in a earth that you dont find familiar")
    input(".")
    print ("A: North B: West")
    choice = input(">>")
    if choice in answer_A:
        North()
    if choice in answer_B:
        West()
    else:
        Intro()
    

def North():
    print ("You head north")
    input(".")
    print ("You see a resting titan")
    input(".")
    print ("Its GODZILLA")
    print ("You see the all-knowing")
    input(".")
    print ("ALL-KNOWING: Incredible.. isn't it?")
    input(".")
    print ("ALL-KNOWING: You dont realise what is hidden beneath you this entire time")
    input(".")
    choice = input("Type SKIP to skip the cutscene or press enter to continue ")
    if choice.lower() == "skip":
        Godzilla()
    else:
        print ("ALL-KNOWING: I cant believe my father is still alive... after all this time")
        input(".")
        print ("ALL-KNOWING: There are so many titans that live here slumbering")
        input(".")
        print ("ALL-KNOWING: They will be ready to wake soon")
        input(".")
        print ("ALL-KNOWING: They will break through the surface to take back the land that they once inhabited")
        input(".")
        print ("ALL-KNOWING: They are going to cause destruction to earth")
        input(".")
        print ("ALL-KNOWING: It will be us who allows them to")
        print ("ALL-KNOWING: Throws a blue orb at Godzilla")
        input(".")
        print ("GODZILLA wakes and shoots a beam to the sky")
        input(".")
        Godzilla()

def Godzilla():
    GODZILLA = 1000000
    HP = player.health * 100
    print ("GODZILLA",GODZILLA)
    print ("HP:",HP)
    print ("ALL-KNOWING goes to open a portal but gets attacked by ghidorah")
    input(".")
    print ("A: Go to the hut B:Hide behind rock C:Fight")
    choice = input(">>")
    if choice in answer_A:
        print ("You go in the hut and GODZILLA stomps on you")
        time.sleep(2)
        print ("YOU DIED")
        time.sleep(1)
        Intro()
    if choice in answer_B:
        print ("You hide behind a rock and watch as godzilla stamps on a little hut and he smashes his tail through a rock causing you to run")
        input(".")
        print ("A: Run to helicopter B: Run to traveller")    
        choice = input(">>")
        if choice in answer_A:
            print ("You run towards the helicopter")
            time.sleep(2)
            print ("Godzilla beams it causing it to crash into you")
            time.sleep(2)
            print ("YOU DIED")
            Intro()
        if choice in answer_B:
            print ("You dash towards the traveller")
            input(".")
            print ("A helicopter crashes down at you both and the blades on the rotor mangle the traveller's body")
            input(".")
            print ("You grab his bag and make a run across the open land")
            Beam = 10
            print ("Charge:",Beam,"%")
            time.sleep(2)
            Beam = 20
            print ("Charge:",Beam,"%")
            time.sleep(1)
            Beam = 30
            print ("Charge:",Beam,"%")
            time.sleep(1)
            print ("KONG arrives and elbow drops GODZILLA")
            input(".")
            print ("KONG strangles GODZILLA until KAVU swoops down and grabs KONG")
            input(".")
            print ("KONG Rips one of the heads off and chucks it towards you nearly crushing you in the process")
            input(".")
            Beam = 40
            print ("Charge:",Beam,"%")
            time.sleep(1)
            Beam = 50
            print ("Charge:",Beam,"%")
            time.sleep(1)
            Beam = 65
            print ("Charge:",Beam,"%")
            Beam = 70
            print ("Charge:",Beam,"%")
            time.sleep(2)
            Beam = 80
            print ("Charge:",Beam,"%")
            time.sleep(1)
            Beam = 90
            print ("Charge:",Beam,"%")
            time.sleep(2)
            Beam = 95
            print ("Charge:",Beam,"%")
            print ("A: RUN B: HIDE")
            choice = input(">>")
            if choice in answer_A:
                print ("You attempt to run and get incinerated")
                Intro()
            if choice in answer_B:
                print ("you hide behind the head of kavu")
                input(".")
                print ("The head takes the beam and GODZILLA charges again")
                input(".")
                print ("You notice the blood from the head has gone a glowing blue colour")
                input(".")
                print ("A: Drink the blood B:Run")
                choice = input(">>")

                if choice in answer_A:
                    print ("You crawl over to the blood and slurp it up")
                    input(".")
                    print ("A pain runs through your body. considering you just drank a radioactive liquid it is not suprising")
                    input(".")
                    print ("A: Bag B: Run")
                    if choice in answer_A:
                        print ("You go through the travellers bag and find a potion")
                        choice = input("DRINK IT?? Y/N?")
                        if choice in yes:
                            End()
                        if choice in no:
                            print ("You do not drink it and die to poisoning")
                            Intro()
                        else:
                            Intro()
                    else:
                        print ("You try to run but you die to radioactive poisoning")
                        Intro()
                else:
                    print ("You run and get crushed by KONG falling from the sky")
                    Intro()
            else:
                Intro()                  
        else:
            Intro()
    if choice in answer_C:
        print ("You run at godzilla and get beamed")
        time.sleep(2)
        print ("YOU DIED")
        time.sleep(1)
        Intro()
    else:
        Intro()

def End():
    print ("You feel the pain turn into power and you take a final stand")
    Beam = 100
    print ("Charge:",Beam,"%")
    input(".")
    print ("Godzilla fires his atomic breath and you also fire one back")
    input(".")
    print ("You are not as strong as Godzilla so your beam is weaker")
    input(".")
    print ("Your godzilla beam summons a ghost of the head of Kavu that does the beam for you")
    input(".")
    print ("Ghidorah grabs GODZILLA and takes him into the sky to go to Earth")
    input(".")
    print ("You nearly faint due to the sheer power you just emitted")
    input(".")
    print ("You wake up..")
    input(".")
    print ("In the middle of a burned London")
    input(".")
    print ("You are met by a bald man")
    input(".")
    print ("ANDREW TATE: Come on. Get your head up. Get back in the game")
    input(".")
    print ("The man just disappears")
    input(".")
    print ("You manage to stand up and can see a injured Kavu on top of big ben with only 2 heads")
    input(".")
    print ("Do you walk to him?")
    choice = input("Y/N")
    if choice in yes:
        print ("You limp towards the wounded hydra")
        input(".")
        print ("He sends a fire ball your way turning you to ashes")
        input(".")
        print ("TIP: Do not approach a pissed hydra")
        print ("YOU DIED")
        time.sleep(2)
        End()
    else:
        print ("You stare at it and he gives you one mean look and flies off")
        input(".")
        print ("You limp around but there is no where to go")
        input(".")
        print ("You see a plane landing and limp towards it")
        input(".")
        print ("ITS THE ROCK")
        input(".")
        print ("THE ROCK: Hop in we are going to NEW YORK")
        input(".")
        print ("THE ROCK: I promise i wont crash this time.")
        file = open ("Power.txt","w")
        file.write("Atomic Breath")
        file.close()
        file = open("CharacterClass.txt","r")
        char_type = file.read()
        file.close
        if char_type == "mage":
            from Mage import Awakening
        if char_type == "thief":
            from Thief import Awakening
        if char_type == "prisoner":
            from Prisoner import Awakening
        if char_type == "gamer":
            from Gamer import Awakening
        if char_type == "vagabound":
            from Vagabound import Awakening
        if char_type == "warrior":
            from Warrior  import Awakening

def West():
    print ("You head west")
    input(".")
    print ("You see a titan that is a massive gorilla")
    input(".")
    print ("You see military setting up to kill Kong")
    input(".")
    print ("You approach the general")
    input(".")
    print ("General: Who are you? You must leave here now this is a dangerous operation")
    input(".")
    print ("General: LEAVE.. NOW!")
    input(".")
    print ("You refuse")
    input(".")
    print ("A: Leave Kong B: Protect Kong")
    choice = input(">>")
    if choice in answer_A:
        print ("You go to leave Kong but the general shoots you in the head")
        input(".")
        print ("YOU DIED")
        Intro()
    if choice in answer_B:
        print ("You run towards kong avoiding fire from the military")
        input(".")
        print ("You hear a screech in the sky that wakes up Kong")
        input(".")
        print ("Kong wakes and begins to destroy everything")
        input(".")
        print ("A blue beam is emitted in the distance and Kong runs over to it")
        input(".")
        print ("You run over until you see KAVU picking up Kong but KAVU only has 2 heads..")
        input(".")
        print ("KONG ripped off a head of Kavu and is now fighting in the sky")
        input(".")
        print ("The general shoots a sniper at KAVU going straight through his wing")
        input(".")
        print ("KAVU and KONG crash into the floor and you run over to help")
        input(".")
        print ("KAVU has disappeared but KONG remains")
        input(".")
        print ("KONG has been gutted by KAVU and is looking towards a fatal end")
        input(".")
        print ("General: I will get him to safety.")
        input(".")
        print ("General: I cannot guarantee his survival")
        input(".")
        print ("You watch as KONG is transported away and you look down to see the guts of KONG")
        print ("EAT?")
        choice = input("Y/N ")
        if choice in yes:
            print ("You dig in on the guts")
            input(".")
            print ("You feel a strong power running through your veins")
            player.strength == 999
            player.health = 100
            player.stealth = 0
            player.defense = 2
            file = open("CharacterStrength.txt","w")
            file.write(str(player.strength))
            file.close
            file = open("CharacterHealth.txt","w")
            file.write(str(player.health))
            file.close
            file = open("CharacterStealth.txt","w")
            file.write(str(player.stealth))
            file.close
            file = open("CharacterDefence.txt","w")
            file.write(str(player.defense))
            print ('Strength:',player.strength)
            print ('Health:',player.health)
            print ('Stealth:',player.stealth)
            print ('Defense:',player.defense)
            file.close()
            Ending()
        else:
            print ("You leave the remains")
            input(".")
            Ending()
    else:
        West()




def Ending():
    print ("You are teleported back to London.. Burned... Destroyed")
    input(".")
    print ("A bald man approaches you")
    input(".")
    print ("Andrew Tate: What are you doing? Get up. Back in the game")
    input(".")
    print ("The man then disappears")
    input(".")
    print ("You see KAVU.. Injured")
    input(".")
    print ("Survivors try running away but KAVU grabs them and eats them")
    input(".")
    print ("ALL-KNOWING: He wants to conquer the world")
    input(".")
    print ("ALL-KNOWIING: My Father is...")
    input(".")
    print ("ALL-KNOWING: Dying..")
    input(".")
    print ("ALL-KNOWING: Father. Speak to me")
    input(".")
    print ("A blue rift appears")
    print ("ALL: Daughter..")
    input(".")
    print ("ALL: I have reached my end")
    input(".")
    print ("ALL: There is going to be no ORDER while i am gone")
    input(".")
    print ("ALL: Seek the path to my HEART")
    input(".")
    print ("ALL: Stop Shadow Man")
    input(".")
    print ("ALL: The ORDER has now fallen. We require a new AGE")
    input(".")
    print ("ALL: Will it be the AGE Of Knowledge")
    input(".")
    print ("ALL: AGE OF THE SITH")
    input(".")
    print ("ALL: Age of the rings")
    input(".")
    print ("ALL: Or Age of the Shadows")
    input(".")
    print ("ALL: That will be determined")
    input(".")
    print ("ALL-KNOWING: Shadow is waiting.")
    input(".")
    print ("ALL-KNOWING: At the GATE")
    input(".")
    print ("ALL: He is prepared to start his conquest that is why")
    input(".")
    print ("ALL-KNOWING: I need to stop him")
    input(".")
    print ("ALL: ALL will collapse when i die meaning multiversal war to fight for ORDER")
    input(".")
    print ("ALL: GATES are how you travel from universe to universe")
    input(".")
    print ("But to have a GATE you must have a OPENING")
    input(".")
    print ("For Shadow Man the SHADOW REALM is his OPENING")
    input(".")
    print ("For my Daughter, THE INDEX")
    input(".")
    print ("ALL: I am sure you will have one soon but for now you are just going to have to wait until the COLLAPSE")
    input(".")
    print ("ALL: There you will notice rifts similiar to mine they will take you from one universe to another")
    input(".")
    print ("ALL: So long")
    input(".")
    print ("A massive blue light shines in the sky")
    time.sleep(2)
    print ("Followed by an explosion")
    time.sleep(3)
    print ("You can feel the force all around you")
    time.sleep(4)    
    print ("The force begins tearing the crust of the earth")
    time.sleep(5)
    print ("Fragments of the earth fly off into the sky")
    input(".")
    print ("The land beneath you starts to rise")
    input(".")
    print ("You try to run but it happens too fast")
    input(".")
    print ("You are now flying on a fragment of the earth")
    input(".")
    print ("You see a white rift in the sky")
    input(".")
    print ("This is the VOID")
    input(".")
    print ("Your body glows white and you dust away")
    time.sleep(3)
    Void()

def Void():
    print ("You find yourself next to a white glowing tree with tints of gold and an endless amount of branches")
    input(".")
    print ("You approach the tree and realise you can go through it")
    input(".")
    print ("You see a chair and you sit on it")
    input(".")
    print ("The inside of the tree fades and you can now see the different universes")
    input(".")
    print ("THE VOID IS YOUR OPENING")
    input(".")
    print ("You go back to Earth")
    file = open("CharacterClass.txt","r")
    char_type = file.read()
    file.close
    if char_type == "mage":
        from Mage import TheFalling
    if char_type == "thief":
        from Thief import TheFalling
    if char_type == "prisoner":
        from Prisoner import TheFalling
    if char_type == "gamer":
        from Gamer import TheFalling
    if char_type == "vagabound":
        from Vagabound import TheFalling
    if char_type == "warrior":
        from Warrior  import TheFalling




Intro()