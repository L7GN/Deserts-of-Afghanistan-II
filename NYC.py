import os,sys
import os.path
from tokenize import Special
from turtle import pos
import Character as Character# Import character to access character types
import time
import Weapons as Weapons
from Weapons import Combistick, Lightsaber, PredatorBlade, PredatorDagger, Shouldercannon, Sword
import random
file = open("CharacterClass.txt","r")
char_type = file.read()
file.close
if char_type == "mage":
    Player = Character.mage
if char_type == "thief":
    Player = Character.thief
if char_type == "prisoner":
    Player = Character.prisoner
if char_type == "gamer":
    Player = Character.gamer
if char_type == "vagabound":
    Player = Character.vagabound
if char_type == "warrior":
    Player = Character.warrior

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
DUEL = ["D", "d"]
yes = ["Y", "y", "yes"] 
no = ["N", "n", "no"]


def NY():
    try:
        file = open("Power.txt","r")
        power = file.read()
        if power == "Force":
            Player.equipped = Lightsaber
        file.close()
        file = open ("Weapon.txt", "r+")
        Special = file.read()
        if Special == "Combistick":
            Player.equipped = Combistick
        if Special == "PredatorBlade":
            Player.equipped = PredatorBlade
        if Special == "Ornamental Dagger":
            Player.equipped = PredatorDagger
        if Special == "Shoulder Cannon":
            Player.equipped = Shouldercannon
        file.close()
    except:
        print ("")
 #map
    dungeonMap = [["0","0","0","0","0","0","0","0","0"],
                  ["0",".",".",".",".",".",".",".","0"],
                  ["0",".",".",".",".",".",".",".","0"],
                  ["S",".",".",".",".",".",".",".","0"],
                  ["0","H",".",".",".",".",".",".","0"],
                  ["0",".",".",".",".",".",".",".","0"],
                  ["0",".",".",".",".",".",".",".","0"],
                  ["0","0","0","0","0","0","0","0","0"]]

    playerMap  = [[".",".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".",".",".","."],
                  ["S",".",".",".",".",".",".",".","E"],
                  [".","H",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".",".",".","."],
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
        Vader = False
        ShadowMan = True
        Homeless = True
        print(mapChoice[y][x])
        position = 0
        while position != "E":
            
            previousX = x
            previousY = y

            movement = input("N,S,E,W,MAP").upper()

            if movement == "N":
                y = y-1
                

            if movement == "S":
                y = y+1
                

            if movement == "E":
                x = x+1
                

            if movement == "W":
                x = x-1
                

            if movement == "MAP":
                displayMap(playerMap)

            position = mapChoice[y][x]
            playerMap[y][x] = "X"

            if position == "H":
                file = open("loadfile.txt","r")
                load = file.read()
                if load == "Awakening" or "Monsterverse":
                    if Homeless == False:
                        print ("You look at the dead homeless man")
                    if Homeless == True:
                        print ("A homeless man asks you to take his vape")
                        choice = input("Y/N")
                        file.close()
                        if choice in yes:
                            print ("You take the vape")
                            file = open("Inventory.txt","w")
                            file.write("Vape \n")
                            file.close()
                        if choice in no:
                            print ("You refuse the vape")
                        print ("The man shrivels up and dies")
                        Homeless = False

                else:
                    print ("You look at the dead homeless man")
        import Void





    main(mapChoice, playerMap, position)



file=open("loadfile.txt","r")
room=file.read()
file.close()        



def FirstWar():
    file = open("FirstWarCasualties.txt","w")
    file.truncate()
    file.close()
    file = open("FirstWar.txt","w")
    file.truncate()
    file.close()
    file = open("FirstWarCasualties.txt","w")
    file.close
    file = open("FirstWar.txt","w")
    file.close()
    print ("Chapter 3: The first war")
    time.sleep(3)
    print ("You wake up and see a beam in the sky. You look down to see a burning helicopter")
    time.sleep(3)
    print ("You limp over to it and collect your gear")
    input(".")
    file=open("CharacterSkin.txt","r")
    skin =file.read()
    if skin == "Black":
        print ("A police officer approaches you")
        time.sleep(3)
        print ("Police Officer: Look its a nig--")
        time.sleep(2)
        print ("The rock appears and stomps on their heads")
    else:
        print ("The Rock appears")
    file.close() 
    print ("Rock: It is great to see you...")
    time.sleep(4)
    print ("Rock: Listen.")
    time.sleep(1)
    print ("Rock: People are gonna die today this is gonna be mayhem okay")
    time.sleep(5)
    print ("Rock: Just be careful and play safe")
    time.sleep(3)
    print ("Rock: There are many ways this could end.")
    input(".")
    print ("You can hear rumbles as more people arrive")
    input(".")
    print ("You hide in a bar")
    input(".")
    print ("The roof of the bar crashes down and you now have to find another exit")
    input(".")
    print ("Pieces of debris get lifted up and you crawl out")
    input(".")
    print ("As you crawl out you see mr x who grabs you and throws you at a wall")
    input(".")
    print ("A red lightsaber is emitted and darth maul appears and starts to attack him")
    input(".")
    print ("Maul cuts off Mr X's hand and goes for the head but he hears a grenade and turns around to force it away which leads Mr X to grab him and throw him into a bus")
    input(".")
    print ("Darth Maul gets back up")
    input(".")
    print ("He runs at Mr X but gets punched by the Nemesis.")
    input(".")
    print ("The nemesis survived your last encounter. he whips his tentacle towards darth maul and it wraps around his leg allowing him to throw him into the burning bar")
    input(".")
    print ("Nemesis and Mr X fight and you run")
    time.sleep(1)
    print ("Well you limp really")
    input(".")
    print ("A: Left B: Right")
    choice = input(">>")
    if choice in answer_A:
        FWLeft()
    if choice in answer_B:
        FWRight()

def FWLeft():
    File = open("FirstWar.txt","w")
    File.write("You go left\n")
    File.close()
    print ("You go left and see the rock")
    input(".")
    print ("Chapter 3.1: The First Loss")
    time.sleep(3)
    print ("Hawkeye shoots an arrow at the chest of Rock")
    input(".")
    print ("The rock throws a piece of a car at Hawkeye making him lose balance and fall off the rooftop")
    input(".")
    print ("He rolls down and runs towards the rock")
    Flag = True
    while Flag == True:
        print ("HELP- A: The Rock B: Hawkeye")
        choice = input(">>")
        if choice in answer_A:
            file = open("FirstWarCasualties.txt","w")
            Hawkeye = "Hawkeye\n"
            file.writelines(Hawkeye)
            file.close()
        if choice in answer_B:
            file = open("FirstWarCasualties.txt","w")
            Rock = "Rock\n"
            file.writelines(Rock)
            file.close()
        FirstLoss()


def FWRight():
    with open("FirstWar.txt","w") as FW:
        Choice = "You go right \n"
        FW.writelines(Choice)
    print ("You go right and see Jill Valentine wounded on the floor")
    print ("Chapter 3.1: The First Loss")
    time.sleep(3)
    print ("She is unable to get up due to her wounds")
    input(".")
    print ("Jill: Please go.. Save yourself")
    Flag = True
    while Flag == True:
        print ("A: Leave B: Help")
        choice = input(">>")
        if choice in answer_A:
            with open("FirstWar.txt","w") as FW:
                Jill = "You leave Jill Valentine wounded \n"
                FW.writelines([Choice,Jill])
        if choice in answer_B:
            with open("FirstWar.txt","w") as FW:
                Jill = "You help Jill\n"
                FW.writelines([Choice,Jill])
        FirstLoss()

def FirstLoss():
    with open("FirstWar.txt","r") as FW:
        Jill = FW.read()    
        with open ("FirstWarCasualties.txt","r") as K:
            Kill = K.read()
            if "You help Jill" in Jill:
                with open("FirstWar.txt","a") as FW:
                    with open("FirstWarCasualties.txt","a") as K:
                        print ("You help Jill up")
                        input(".")
                        print ("Jill gets shot in the head")
                        time.sleep(2)
                        K.write("Jill Valentine\n")
                        print ("You see Ghost aiming an AK at you")
                        time.sleep(5)
                        print ("A tiger pounces at him and rips out his throat")
                        print ("Its Shiva")
                        K.write("Ghost\n")
                        FW.write("Shiva mauls Ghost to death\n")
                        time.sleep(5)
                        print ("You see Rick Grimes and he pulls out his gun and points it on your head")
                        input(".")
                        print ("A arrow pierces his knee and you see hawkeye on a rooftop")
                        input(".")
                        print ("You make a run for it and you hear a gun shot you look behind to see Hawkeyes lifeless body drop off the roofs")
                        K.write("Hawkeye\n")
                        FW.write("Rick Grimes kills Hawkeye\n")
            if "You leave Jill Valentine wounded" in Jill:
                with open("FirstWar.txt","a") as FW:
                    with open("FirstWarCasualties.txt","a") as K:
                        print("You see the Rock snap Hawkeye's neck")
                        K.write("Hawkeye\n")
                        FW.write("Rock neck snaps Hawkeye\n")
                        input(".")
                        print ("Vader storms over but iron man flies towards him")
                        time.sleep(5)
                        print ("Vader hits him without looking and he crashes into the ground")
                        input(".")
                        print ("Skepta slide tackles Vader and runs away")
                        input(".")
                        print ("You chase after Skepta and LAKAKA runs through a wall and grabs him with his stomach ripped open")
                        input(".")
                        print ("He slams Skepta on the ground multiple times his face becomes unrecognisable")
                        input(".")
                        print ("Lakaka drops the dead skepta to the ground and climbs up a building")
                        K.write("Skepta\n")
                        FW.write("Lakaka kills Skepta\n")


            if "Hawkeye" in Kill:
                with open("FirstWar.txt","a") as FW:
                    with open("FirstWarCasualties.txt","a") as K:
                        print ("You roundhouse kick Hawkeye into the rock who gives him the rock bottom")
                        input(".")
                        print ("The Rock grabs a arrow and jams it in his eye he twists and turns it")
                        input(".")
                        print ("The rock picks up a rock and kills him with it\n")
                        FW.write("The rock crushes hawkeye with a rock\n")

            if "Rock" in Kill:
                with open("FirstWar.txt","a") as FW:
                    with open("FirstWarCasualties.txt","a") as K:
                        print ("Rock: What are you doing!")
                        input(".") 
                        print ("He right hooks you knocking you to the floor")
                        input(".")   
                        print ("The Rock and Hawkeye wrestle and obviously The Rock comes out on")
                        input(".")                     
                        print ("A car crushes into them both killing them")
                        input(".")   
                        print ("A wounded Jill Valentine rolls out of the car")
                        input(".")   
                        print ("The Rock and Hawkeye have been crushed to death")
                        FW.write("Jill crushes The Rock and Hawkeye killing them both\n")
                        K.write("Hawkeye\n")
            FirstLoss2()

def FirstLoss2():
    with open("FirstWar.txt","r") as FW:
        Firstloss = FW.read()    
        with open ("FirstWarCasualties.txt","r") as K:
            Death = K.read() 
            if  "Rick Grimes kills Hawkeye" in Firstloss:
                with open("FirstWar.txt","a") as FW:
                    with open("FirstWarCasualties.txt","a") as K:
                        print ("You head around a corner and bump into hitler")
                        input(".")
                        print ("He screams german at you which awakens Thomas Tuchel who runs over and rugby tackles him to the ground")
                        input(".")
                        print ("You walk away as if nothing ever happened")
                        input(".")
                        print ("Green Goblin nearly runs you over with his glider")
                        input(".")
                        print ("He gets off")
                        print ("There will be no running")
                        GoblinFight()
            if  "The rock crushes hawkeye with a rock" in Firstloss:
                with open("FirstWar.txt","a") as FW:
                    with open("FirstWarCasualties.txt","a") as K:
                        print ("")
            if  "Jill crushes The Rock and Hawkeye killing them both" in Firstloss:
                with open("FirstWar.txt","a") as FW:
                    with open("FirstWarCasualties.txt","a") as K:
                        print ("")
            if  "Lakaka kills Skepta" in Firstloss:
                with open("FirstWar.txt","a") as FW:
                    with open("FirstWarCasualties.txt","a") as K:
                        print ("")


def GoblinFight():
    HP = Player.health * 100
    GreenGoblin = 10000
    while GreenGoblin >= 0:
        print ("Green Goblin:", GreenGoblin)
        print ("HP:", HP)
        Burn = 1
        Stun = False
        Cancer = False
        Onehand = True
        Twohand = False
        file = open("Power.txt","r")
        Power = file.read()
        file = open ("Weapon.txt", "r")
        Player.equipped = file.read()
        if Player.equipped == "Combistick":
            print ("A: Combistick")
        if Player.equipped == "PredatorBlade":
            print ("A: Arm blades")
        if Player.equipped == "Ornamental Dagger":
            print ("A: Ornamental Dagger")
        if Player.equipped == "Shoulder cannon":
            print ("A: Shoulder Cannon")
        if Power == "Force":
            print ("B: Force")
        if Power == "Atomic Breath":
            print ("B: Atomic Breath")
        if Power == "Force":
            print ("C: Lightsaber")
        choice = input(">>")
        if choice in answer_C:
            print ("A: Lightsaber Slash")
            print ("B: Lightsaber Boomerang")
            print ("C: Onehand/Twohand")
            Choice = input(">> ")
            if Choice in answer_A:
                print ("You slash with your lightsaber")
                if Onehand == True:
                    Slash = random.randint(1000,3000)
                else:
                    Slash = 4000
                time.sleep(3) 
                print ("{",Slash,"}")
                GreenGoblin = GreenGoblin - Slash  
                if GreenGoblin <= 0:
                    break
            if Choice in answer_B:
                print ("You throw your lightsaber at GreenGoblin and use the force to bring your lightsaber back to you")
                Throw = 4999
                time.sleep(3)
                print ("{",Throw,"}")
                GreenGoblin = GreenGoblin - Throw
                if GreenGoblin <= 0:
                    break
            if Choice in answer_C:
                if Onehand == True:
                    print ("You hold your lightsaber in two hands")
                    Onehand = False
                    Twohand = True
                else:
                    print ("You hold your lightsaber in one hand like you was taught by master vader")
                    Onehand = True
                    Twohand = False
        if choice in answer_B:
            if Power == "Force":
                print ("A: Force Push")
                print ("B: Force Choke")
                Move = input(">>")
                if Move in answer_A:
                    print ("You force push GreenGoblin into a wall")
                    Push = 200
                    time.sleep(3)
                    print ("{",Push,"}")
                    GreenGoblin = GreenGoblin - Push
                    if GreenGoblin <= 0:
                        break
                if Move in answer_B:
                    print ("You use the force to pick up GreenGoblin and strangle the king")
                    Choke = 10000
                    time.sleep(3)
                    print ("{",Choke,"}")
                    GreenGoblin = GreenGoblin - Choke
                    if GreenGoblin <= 0:
                        break
            if Power == "Atomic Breath":
                Radioactive = random.randint(1,33)
                print ("You beam GreenGoblin")
                Atom = 50000
                print ("{",Atom,"}")
                GreenGoblin = GreenGoblin - Atom
                if Radioactive >= 30:
                    Cancer = True
                
        if choice in answer_A:
                file = open ("Weapon.txt", "r")
                Special = file.read()
                if Special == "Combistick":
                    print ("The combistick allows you to attack with speed and you manage to get a lot of piercing hits on GreenGoblin")
                    Spear = random.randint(6000,10000)
                    time.sleep(3)
                    print ("{",Spear,"}")
                    GreenGoblin = GreenGoblin - Spear
                    if GreenGoblin <= 0:
                        break
                if Special == "PredatorBlade":
                    print ("You swing your arms in a fast motion with the blades attached to your arms")
                    Arm = random.randint(1000,3000)
                    time.sleep(3)
                    print ("{",Arm,"}")
                    GreenGoblin = GreenGoblin - Arm
                    if GreenGoblin <= 0:
                        break
                if Special == "Ornamental Dagger":
                    print ("You slash GreenGoblin with a dagger")
                    Dagger = random.randint(400,500)
                    time.sleep(3)
                    print ("{",Dagger,"}")
                    GreenGoblin = GreenGoblin - Dagger
                    if GreenGoblin <= 0:
                        break
                if Special == "Shoulder Cannon":
                    print ("C: You aim the cannon and fire at the massive target of GreenGoblin")
                    Cannon = 5000
                    time.sleep(3)
                    print ("{",Cannon,"}")
                    GreenGoblin = GreenGoblin - Cannon
                    if GreenGoblin <= 0:
                        break
        if Cancer == True:
            print ("The atomic breath is having an effect on GreenGoblin")
            time.sleep(3)
            print ("GreenGoblin shows a sense of dizziness")
            Poison = random.randint(1000,1200)
            GreenGoblin = GreenGoblin - Poison
            Stun = True
            Cancer = False
        if Stun == False:
            print ("Green Goblin attacks")
            Followup = random.randint(1,10)
            if Followup > 6:
                print ("Green Goblin punches you and cuts your leg with his blade")
                Frenzy = random.randint(1,5)
                if Frenzy == 5:
                    Attacks = random.randint(2,15)
                    while Attacks > 0:
                        Move = random.randint(1,5)
                        if Move == 1:
                            print ("Green Goblin powerbombs you")
                            Attack = random.randint(100,500)
                            print ("{",Attack,"}")
                            HP = HP - Attack
                            Attacks = Attacks - 1
                            time.sleep(3)
                        if Move == 2:
                            print ("Green Goblin impales you with his blade")
                            Attack = random.randint(1000,5000)
                            print ("{",Attack,"}")
                            HP = HP - Attack
                            Attacks = Attacks - 1
                            time.sleep(3)
                        if Move == 3:
                            print ("Green Goblin punches you")
                            Attack = random.randint(100,200)
                            print ("{",Attack,"}")
                            HP = HP - Attack
                            Attacks = Attacks - 1
                            time.sleep(3)
                        if Move == 4:
                            print ("Green Goblin throws you into a wall")
                            Attack = random.randint(100,3000)
                            print ("{",Attack,"}")
                            HP = HP - Attack
                            Attacks = Attacks - 1
                            time.sleep(3)
                        if Move == 5:
                            print ("Green Goblin headbutts you")
                            Attack = random.randint(2000,20000)
                            print ("{",Attack,"}")
                            HP = HP - Attack
                            Attacks = Attacks - 1
                            time.sleep(3)
            else:
                print ("Green Goblin punches you")
                Attack = random.randint(100,500)
                print ("{",Attack,"}")
                HP = HP - Attack
            if HP < 0:
                print ("YOU DIED")
                GoblinFight()

GoblinFight()




    

if room == "TheFirstWar":
    FirstWar()
else:
    NY()