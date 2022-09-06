from ast import Delete
import os,sys
import os.path
import Character as Character# Import character to access character types
import time
import Weapons as Weapon
import random
player = Character.thief

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

s = "Awakening"
save(s)


def intro():
    print ("You crash again..")
    input(".")
    print ("Rock: That will be the last time i fly i think")
    input(".")
    print ("The green goblin flies down on his glider")
    time.sleep(3)
    print ("He starts beating up the rock and you dont want that smoke so you run off")
    input(".")
    print ("You see a news flash on a bill board")
    time.sleep(2)
    print ("NEWS: Hydra razes London")
    print ("Kavu can be seen tearing down buildings")
    input(".")
    print ("You can see a outline of something in a crowd")
    input(".")
    print ("It picks someone up and blood pours out of them")
    time.sleep(3)
    print ("The figure reveals itself")
    time.sleep(3)
    print ("ITS PREDATOR")
    time.sleep(2)
    print ("The predator grabs his sword and cuts through people")
    time.sleep(2)
    print ("A web is shot down at his sword and it manages to take his sword away")
    time.sleep(4)
    print ("Spiderman hops down and intiates combat")
    time.sleep(3)
    print ("Spiderman tries to take control with his webs but predator has his spear and cuts them out quickly")
    time.sleep(3)
    print ("Spiderman gets a punch in but takes a roundhouse kick to the rib")
    time.sleep(3)
    print ("Predator puts his handblade through the leg of spiderman and pushes him over with his other hand")
    time.sleep(5)
    Flag = True
    while Flag == True:
        print ("A: HELP B: Leave")
        choice = input()
        if choice in answer_A:
            help()
        else:
            print ("You stay back and watch the predator stab his sword down in the chest of spiderman")
            input(".")
            print ("Predator puts his attention to you")
            input(".")
            print ("A laser appears on your chest")
            input(".")
            file = open ("Power.txt","r")
            Power = file.read()
            if Power == "Force":
                print ("You use the force to stop the missile in flight")
                input(".")
                print ("You force push him into a building and drag Spiderman away")
                input(".")
                print ("Spiderman bleeds out in your arms")
                input(".")
                Hunt()
            if Power == "Atomic Breath":
                print ("You charge up your atomic beam and incinerate the Predator")
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
                loot = random.randint(1,100)
                if loot in range(1,50):
                    print ("You acquire the armblades from the predator")
                    File = open ("Weapon.txt","w")
                    File.write("PredatorBlade")
                    File.close()
                    File = open ("Weapon.txt","r")
                    weapon = File.read()
                    File.close()
                    player.equipped = weapon
                    print (player.equipped)
                    print (Weapon.PredatorBlade.stats)
                if loot in range(51,70):
                    print ("You acquire the spear from the predator")
                    File = open ("Weapon.txt","w")
                    File.write("Combistick")
                    File.close()
                    File = open ("Weapon.txt","r")
                    weapon = File.read()
                    File.close()
                    player.equipped = weapon
                    print (player.equipped)
                    print (Weapon.Combistick.stats)
                if loot in range (71,95):
                    print ("You acquire the dagger of predator")
                    File = open ("Weapon.txt","w")
                    File.write("Ornamental Dagger")
                    File.close()
                    File = open ("Weapon.txt","r")
                    weapon = File.read()
                    File.close()
                    print ("EPIC")
                    player.equipped = weapon
                    print (player.equipped)
                    print (Weapon.PredatorDagger.stats)
                if loot in range(96,100):
                    print ("You acquire the Shoulder Cannon from the predator")
                    File = open ("Weapon.txt","w")
                    File.write("Shoulder Cannon")
                    File.close()
                    File = open ("Weapon.txt","r")
                    weapon = File.read()
                    File.close()
                    print ("LEGENDARY")
                    player.equipped = weapon
                    print (player.equipped)
                    print (Weapon.Shouldercannon.stats)
                Invasion()





def help():
    print ("You go to help spiderman but a weird ALIEN creature drops down")
    input(".")
    print ("The xenomorph runs straight at you")
    file = open("Power.txt","r")
    power = file.read()
    if power == "Force":
        print ("You try to lift the creature up with the force but you are not that strong yet")
        time.sleep(6)
        print ("Instead you throw bits of debris at it")
        input(".")
        print ("Eventually you end up embedding alien in the debris")
        input(".")
        print ("You look around and Predator and Spiderman are gone")
        input(".")
        print ("You are on your own again..")
    if power == "Atomic Breath":
        print ("You beam the xenomorph and make a gaping hole in its torso")
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
        input(".")
        print ("You look around and Predator and Spiderman are gone")
        input(".")
        print ("You are on your own again..")       
        input(".")
    print ("Crowds are running away")
    input(".")
    print ("You ask someone in the crowd")
    input(".")
    print ("Citizen: HE IS BACK")
    time.sleep(2)
    print ("BENJAMIN MENDY")
    input(".")
    print ("Citizen: He has escaped Alcatraz")
    input(".")
    print ("You sense this is a big danger and make sure you are ready at all times")
    input(".")
    print ("You see groups of aliens on rooftops.")
    input(".")
    print  ("It is looking likely that New York City may be looking likely to fall next")
    input(".")
    print ("A meteor enters the atmosphere")
    input(".")
    print ("You then quickly realise this is no meteor but a man holding what looks to be a dragon")
    input(".")
    print ("He hits the ground and rips the head of the dragon off and throws it at a building")
    input(".")
    print ("It is..")
    time.sleep(3)
    print ("ULTIMATE ANDY")
    print ("He lasers multiple aliens and flies away to stop their attack")
    time.sleep(3)
    print ("Andrew Tate: Do you know why Aliens and dragons are invading us now")
    time.sleep(5)
    print ("Andrew Tate: Because earth is full of weak people like you and they just see it as a easy place to start.")
    print ("ANDREW TATE is doing a speech")
    input(".")
    print ("Andrew Tate: Those aliens know that this place is a failed society and they are cutting off the WEAK. which is you people")
    input(".")
    print ("Andrew Tate: In the end only the strongest will be left standing")
    input(".")
    print ("A alien chases after andrew tate and he hits it with a spinning back kick and then stomps its brains out on the ground")
    input(".")
    print ("Andrew Tate then walks away as if nothing had happened")
    input(".")
    print ("Predator can be found on top of the new world trade centre")
    input(".")
    print ("A plane is approaching the world trade centre at speed")
    input(".")
    print ("Predator uses his shoulder cannon to blow it up")
    print ("Lets not have another plane crash please")
    input(".")
    print ("Osama bin laden has been revived and has resulted to shooting pedestrians")
    input(".")
    print ("A SAS unit arrive")
    print ("Soap")
    print ("Captain Price")
    print ("Gaz")
    print ("Simon 'Ghost' Riley")
    input(".")
    print ("Gaz runs at bin laden guns blazing")
    input(".")
    print ("Bin Laden throws a knife at him that hits him right between the eyes")
    input(".")
    print ("GAZ:DEAD")
    print ("Osama bin laden releases a grenade that destroys their vehicle.")
    input(".")
    print ("The smoke clears and the other three are nowhere to be seen")
    input(".")
    print ("Predator appears behind you")
    input(".")
    print ("He swings his sword and you dodge under it")
    input(".")
    print ("Osama bin laden fires a whole magazine at the predator")
    input(".")
    print ("Most bullets collide with the armour whilst others leave only a cut on the predator")
    input(".")
    print ("Predator runs off to not be seen again")
    input(".")
    print ("Osama bin laden aims a gun at you")
    input(".")
    print ("You get on the ground")
    input(".")
    print ("A captain america shield hits him")
    input(".")
    print ("You get up and run to the WTC")
    input(".")
    print ("New York City is now in chaos. People are trying to escape")
    input(".")
    print ("Kavu flies through the new world trade centre")
    input(".")
    print ("Spiderman webs over to him but gets smacked by his tail")
    input(".")
    print ("A queen xenomorph catches spiderman and eats him")
    input(".")
    print ("All-Knowing arrives and tells you that there is going to be all out war")
    input(".")
    print ("ALL-KNOWING: ALL is dead")
    input(".")
    print ("ALL-KNOWING: There is no order only conflict")
    input(".")
    print ("ALL-KNOWING: He used what was left of him to keep this world intact")
    input(".")
    print ("ALL-KNOWING: Shadow knows where he is. So the best thing he could do was kill himself to bring the chaos, hoping he wont make it out alive")
    input(".")
    print ("Doctor Strange arrives with Mr Time")
    input(".")
    print ("Doctor Strange: Well.. what is our best option")
    input(".")
    print ("ALL-KNOWING: You must portal away from here. Let the chaos happen, whoever wins wins")
    input(".")
    print ("Doctor Strange opens a portal to LA")
    input(".")
    print ("You are now in LA")
    print ("Doctor Strange: This is the awakening")
    input(".")
    print ("Doctor Strange: The awakening is when all the universes begin to realise their existence and attack each other to protect their very own")
    input(".")
    print ("Doctor Strange: after the awakening it will become... War...")
    input(".")
    print ("Doctor Strange: ALL is dead, he saw this as a easy way out for him knowing the destruction of worlds is coming. Earth has been chosen first")
    input(".")
    print ("A white glow appears on your body and everything around you turns to white")
    input(".")
    print ("A tree appears in front of you")
    input(".")
    print ("You touch the tree and it fades away")
    input(".")
    print ("But now you can see all the different universes")
    input(".")
    print ("You are aloud to travel from universe to universe through the tree in the void")
    input(".")
    print ("It is what powers your very being")
    file = open("CharacterClass.txt","r")
    char_type = file.read()
    file.close
    if char_type == "mage":
        from Mage import Void
    if char_type == "thief":
        from Thief import Void
    if char_type == "prisoner":
        from Prisoner import Void
    if char_type == "gamer":
        from Gamer import Void
    if char_type == "vagabound":
        from Vagabound import Void
    if char_type == "warrior":
        from Warrior  import Void


def Hunt():
    print ("Predator emerges and activates his blades")
    time.sleep(2)
    print ("You use the force in a defensive stance to stop him from hitting you")
    input(".")
    print ("You force push him onto a spike and run away")
    input(".")
    print ("You see people getting attacked by facehuggers")
    input(".")
    print ("The alien race is now invading earth")
    input(".")
    print ("Aliens are being attracted to some light and are crawling all over it")
    input(".")
    print ("A thermal energy blast emits off of it disintegrating all the aliens revealing the light to be")
    input(".")
    print ("ULTIMATE ANDY")
    input(".")
    print ("He flies through the New World Trade Centre never to be seen again")
    input(".")
    print ("Predator pounces on top of you and tries to put his sword through your chest")
    input(".")
    print ("The force is too strong for the predator and you can easily handle him")
    input(".")
    print ("You attempt to run away but the predator prevents you from doing")
    input(".")
    print ("You now have to fight the predator")
    PredatorHP = 10000
    Onehand = True
    Forceparry = False
    Twohand = False
    HP = player.health * 100
    while PredatorHP >= 0:
        print ("Predator:", PredatorHP)
        print ("HP:", HP)
        print ("A: Lightsaber")
        print ("B: Force")
        choice = input(">>")
        if choice in answer_A:
            print ("A: Lightsaber Slash")
            print ("B: Lightsaber Boomerang")
            print ("C: Onehand/Twohand")
            choice = input(">> ")
            if choice in answer_A:
                if Onehand == True:
                    Slash = random.randint(1000,3000)
                else:
                    Slash = 4000
                time.sleep(3) 
                print ("{",Slash,"}")
                PredatorHP = PredatorHP - Slash  
                if PredatorHP <= 0:
                    break
            if choice in answer_B:
                print ("You throw your lightsaber at predator and use the force to bring your lightsaber back to you")
                Throw = 4999
                time.sleep(3)
                print ("{",Throw,"}")
                PredatorHP = PredatorHP - Throw
                if PredatorHP <= 0:
                    break
            if choice in answer_C:
                if Onehand == True:
                    print ("You hold your lightsaber in two hands")
                    Onehand = False
                    Twohand = True
                else:
                    print ("You hold your lightsaber in one hand like you was taught by master vader")
                    Onehand = True
                    Twohand = False
        if choice in answer_B:
            print ("A: Force Push")
            print ("B: Force Choke")
            choice = input(">>")
            if choice in answer_A:
                print ("You force push Predator into a wall")
                Push = 200
                time.sleep(3)
                print ("{",Push,"}")
                PredatorHP = PredatorHP - Push
                if PredatorHP <= 0:
                    break
            if choice in answer_B:
                print ("You use the force to pick up Predator and start crushing him")
                Choke = 100000
                time.sleep(3)
                print ("{",Choke,"}")
                PredatorHP = PredatorHP - Choke
                if PredatorHP <= 0:
                    break
        print ("Predator activates his handblades and attacks")
        Double = random.randint(1,4)
        if Onehand == True:
            print ("You use the force to drag predator away from you and then hit him on the back")
            Forceparry = True
        if Twohand == True:
            Forceparry = False
        if Double == 4:
            if Forceparry == False:
                print ("He stabs you in the leg and swiftly stabs the other in the throat")
                Double = 2000
                print ("{",Double,"}")
                HP = HP - Double
        else:
            if Forceparry == False:
                print ("You use your lightsaber to block one but he catches you with the other")
                Double = 250
                print ("{",Double,"}")
                HP = HP - Double
        if HP <= 0:
            print ("YOU DIED")
            time.sleep(3)
            Hunt()
    print ("His body drops to the ground")
    file = open("Kills.txt","r")
    lines = file.readlines()
    
    for line in lines:
        for c in line:
            if c.isdigit() == True:
                c = (int(c)) + 1
                file.close
    file = open("Kills.txt","w")
    file.write((str(c)))
    file.close
    print ("You take a piece of him as a trophy")
    loot = random.randint(1,100)
    if loot in range(1,50):
        print ("You acquire the armblades from the predator")
        File = open ("Weapon.txt","w")
        File.write("PredatorBlade")
        File.close()
        File = open ("Weapon.txt","r")
        weapon = File.read()
        File.close()
        player.equipped = weapon
        print (player.equipped)
        print (Weapon.PredatorBlade.stats)
    if loot in range(51,70):
        print ("You acquire the spear from the predator")
        File = open ("Weapon.txt","w")
        File.write("Combistick")
        File.close()
        File = open ("Weapon.txt","r")
        weapon = File.read()
        File.close()
        player.equipped = weapon
        print (player.equipped)
        print (Weapon.Combistick.stats)
    if loot in range (71,95):
        print ("You acquire the dagger of predator")
        File = open ("Weapon.txt","w")
        File.write("Ornamental Dagger")
        File.close()
        File = open ("Weapon.txt","r")
        weapon = File.read()
        File.close()
        print ("EPIC")
        player.equipped = weapon
        print (player.equipped)
        print (Weapon.PredatorDagger.stats)
    if loot in range(96,100):
        print ("You acquire the Shoulder Cannon from the predator")
        File = open ("Weapon.txt","w")
        File.write("Shoulder Cannon")
        File.close()
        File = open ("Weapon.txt","r")
        weapon = File.read()
        File.close()
        print ("LEGENDARY")
        player.equipped = weapon
        print (player.equipped)
        print (Weapon.Shouldercannon.stats)
    print ("Osama bin laden approaches you")
    input(".")
    print ("You force push him into the sky but he activates a parachute")
    input(".")
    print ("A missile lands on a group of aliens and blood spills everywhere")
    input(".")
    print ("The acidic blood falls onto people burning them")
    input(".")
    print ("Queen Alien looks towards you")
    time.sleep(2)
    print ("You grab your saber and emit the red light")
    time.sleep(2)
    print ("Alien swipes you with her tail into a wall")
    time.sleep(3)
    Alien = 1000000
    HP = player.health * 100
    while Alien >= 0:
        print ("Alien:", Alien)
        print ("HP:", HP)
        print ("A: Lightsaber")
        print ("B: Force")
        file = open ("Power.txt", "r")
        Special = file.read()
        if Special == "Combistick":
            print ("C: Combistick")
        if Special == "PredatorBlade":
            print ("C: Arm blades")
        if Special == "Ornamental Dagger":
            print ("C: Ornamental Dagger")
        if Special == "Shoulder Cannon":
            print ("C: Shoulder Cannon")
        file.close()
        choice = input(">>")
        if choice in answer_A:
            print ("A: Lightsaber Slash")
            print ("B: Lightsaber Boomerang")
            print ("C: Onehand/Twohand")
            choice = input(">> ")
            if choice in answer_A:
                if Onehand == True:
                    Slash = random.randint(1000,3000)
                else:
                    Slash = 4000
                time.sleep(3) 
                print ("{",Slash,"}")
                Alien = Alien - Slash  
                if Alien <= 0:
                    break
            if choice in answer_B:
                print ("You throw your lightsaber at alien and use the force to bring your lightsaber back to you")
                Throw = 4999
                time.sleep(3)
                print ("{",Throw,"}")
                Alien = Alien - Throw
                if Alien <= 0:
                    break
            if choice in answer_C:
                if Onehand == True:
                    print ("You hold your lightsaber in two hands")
                    Onehand = False
                    Twohand = True
                else:
                    print ("You hold your lightsaber in one hand like you was taught by master vader")
                    Onehand = True
                    Twohand = False
        if choice in answer_B:
            print ("A: Force Push")
            print ("B: Force Choke")
            choice = input(">>")
            if choice in answer_A:
                print ("You force push Alien into a wall")
                Push = 200
                time.sleep(3)
                print ("{",Push,"}")
                Alien = Alien - Push
                if Alien <= 0:
                    break
            if choice in answer_B:
                print ("You use the force to pick up Alien and strangle her")
                Choke = 100000
                time.sleep(3)
                print ("{",Choke,"}")
                Alien = Alien - Choke
                if Alien <= 0:
                    break
        if choice in answer_C:
            file = open ("Power.txt", "r")
            Special = file.read()
            if Special == "Combistick":
                print ("The combistick allows you to attack with speed and you manage to get a lot of piercing hits on Alien")
                Spear = random.randint(6000,10000)
                time.sleep(3)
                print ("{",Spear,"}")
                Alien = Alien - Spear
                if Alien <= 0:
                    break
            if Special == "PredatorBlade":
                print ("You swing your arms in a fast motion with the blades attached to your arms")
                Arm = random.randint(1000,3000)
                time.sleep(3)
                print ("{",Arm,"}")
                Alien = Alien - Arm
                if Alien <= 0:
                    break
            if Special == "Ornamental Dagger":
                print ("You slash Alien with a dagger")
                Dagger = random.randint(400,500)
                time.sleep(3)
                print ("{",Dagger,"}")
                Alien = Alien - Dagger
                if Alien <= 0:
                    break
            if Special == "Shoulder Cannon":
                print ("C: You aim the cannon and fire at the massive target of Alien")
                Cannon = 150000
                time.sleep(3)
                print ("{",Cannon,"}")
                Alien = Alien - Cannon
                if Alien <= 0:
                    break
            file.close()
        Slash = random.randint(300,500)
        print ("Alien scratches with its large claws")
        print (Slash,"!!")
        HP = HP - Slash
        if HP <= 0:
            print ("Queen Alien grabs you and tears your arm off")
            time.sleep(5)
            print ("You use the force to grab your lightsaber with your other hand")
            time.sleep(5)
            print ("Alien swipes you with her tail and it uses her tail to rip off both of your legs") 
            time.sleep(7)
            print ("Alien then uses her tail to stab you in the heart killing you")
            time.sleep(6)
            print ("YOU DIED")
            print ("You wake up in front of a white glowing tree")
            input(".")
            print ("You crawl over to it")
            input(".")
            print ("You touch the tree")
            input(".")
            print ("You begin to see all the different universes in the sky")
            input(".")
            print ("You look down to see your legs regenerated")
            file = open("CharacterClass.txt","r")
            char_type = file.read()
            file.close
            if char_type == "mage":
                from Mage import Void
            if char_type == "thief":
                from Thief import Void
            if char_type == "prisoner":
                from Prisoner import Void
            if char_type == "gamer":
                from Gamer import Void
            if char_type == "vagabound":
                from Vagabound import Void
            if char_type == "warrior":
                from Warrior  import Void                      

            



def Invasion():
    print("Spiderman dies on the floor")
    input(".")
    print ("ALL-KNOWING: You need to leave quickly")
    input(".")
    print ("ALL-KNOWING: I am going to send you to the void. go NOW")
    input(".")
    print ("You enter the void but can see through the portal OBSERVATION MAN square off with alien")
    input(".")
    print ("He catches the alien's tail and swings him into a building")
    input(".")
    print ("Alien tries to pounce but he dodges out the way and puts him in a headlock")
    input(".")
    print ("He then snaps his neck")
    input(".")
    print ("Observation Man gets overrun by many smaller aliens but he manages to take them all out 3 at a time")
    input(".")
    print ("You approach the tree")
    input(".")
    print ("and touch it")
    input(".")
    print ("you are able to see all the universes")
    file = open("CharacterClass.txt","r")
    char_type = file.read()
    file.close
    if char_type == "mage":
        from Mage import Void
    if char_type == "thief":
        from Thief import Void
    if char_type == "prisoner":
        from Prisoner import Void
    if char_type == "gamer":
        from Gamer import Void
    if char_type == "vagabound":
        from Vagabound import Void
    if char_type == "warrior":
        from Warrior  import Void   




intro()