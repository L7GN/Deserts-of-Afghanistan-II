from ast import Delete, For
from calendar import c
import os,sys
from sre_constants import AT_BEGINNING
import os.path
import Character as Character# Import character to access character types
import time
import Weapons as Weapon
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
def save(s):
    file=open("loadfile.txt","w")
    file.write(s)
    file.close()


def LA():
    try:
        file = open("Power.txt","r")
        power = file.read()
        if power == "Force":
            Player.equipped = Lightsaber
        file.close()
        file = open ("Weapon.txt", "r+")
        Player.equipped = file.read()
        if Player.equipped == "Combistick":
            Player.equipped = Combistick
        if Player.equipped == "PredatorBlade":
            Player.equipped = PredatorBlade
        if Player.equipped == "Ornamental Dagger":
            Player.equipped = PredatorDagger
        if Player.equipped == "Shoulder Cannon":
            Player.equipped = Shouldercannon
        file.close()
    except:
        print ("")
 #map
    dungeonMap = [["0","0","0","0","0","0","0","0","0"],
                  ["0",".",".",".",".",".",".",".","0"],
                  ["0",".",".",".",".",".",".",".","0"],
                  ["S",".",".",".",".",".",".",".","0"],
                  ["0","C",".",".",".",".",".",".","0"],
                  ["0",".",".",".",".",".",".",".","0"],
                  ["0",".",".",".",".",".",".",".","0"],
                  ["0","0","0","0","0","0","0","0","0"]]

    playerMap  = [[".",".",".",".",".",".",".",".","."],
                  [".",".",".",".","W",".",".",".","."],
                  [".",".",".",".",".",".",".",".","."],
                  ["S",".",".",".",".",".",".",".","E"],
                  [".","C",".",".",".","D",".",".","."],
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
        Shop = True
        Witcher = False
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

            if position == "C":
                if Shop == True:
                    print ("You enter a shop")
                    time.sleep(2)
                    print ("You ask for water")
                    time.sleep(2)
                    print ("You go to get the water but it gets smacked out your hand")
                    time.sleep(4)
                    print ("You get knocked down to the ground")
                    time.sleep(3)
                    print ("When you get a clear image you notice it is andrew tate")
                    time.sleep(3)
                    print ("ANDREW TATE: Don't be scared of bubbles pussy. DRINK SPARKLING WATER")
                    time.sleep(5)
                    print ("Andrew tate ges forcefully pushed into a wall you get up and look behind you")
                    input(".")
                    print ("It is DARTH VADER")
                    if Player.equipped == Lightsaber:
                        print ("VADER: I knew we would meet again")
                    time.sleep(2)
                    print ("ANDREW TATE: You are just a fool who hides away in a mask")
                    input(".")
                    print ("ANDREW TATE: Why dont we fight without laser swords. JUST BARE HANDS")
                    input(".")
                    print ("ANDREW TATE: I challenge you to mortal komba--")
                    print ("A spear is thrown through the window catching andrew tate and flinging him away")
                    input(".")
                    print ("Vader snaps the neck of the shopkeeper with the force and slices through other customers in the shop")
                    input(".")
                    print ("You run out to safety")
                    Shop = False
                else:
                    print ("You look at the aftermath of what was someone's shop.")
            
            if position == "D":
                if ShadowMan == True:
                    print ("You see the rock defeated on the floor") 
                    input(".")
                    print ("Shadow Man approaches him")
                    input(".")
                    print ("He shapes his hand into the blade of a sword")
                    input(".")
                    print ("Observation man fires a laser at shadow man sending him flying")
                    input(".")
                    print ("Shadow Man sends a dark cloud in the air turning it from day to night")
                    input(".")
                    print ("Shadow Man blends in with the darkness and is only recongisable by his white glowing eyes")
                    input(".")
                    print ("You watch as shadow man lifts observation man into the air and throws him into the shop destroying it")
                    input(".")
                    print ("Shadow man goes to punch his eye but observation man catches his arm and tears it off before stomping him into the ground")
                    input(".")
                    print ("Shadow Man regenerates his arm and then teleports behind him")
                    input(".")
                    print ("Observation Man can foresee where observation man is gonna appear and grabs his arms and legs and lasers straight through his chest splitting him in half evenly")
                    input(".")
                    print ("OBSERVATION MAN has just defeated and killed the shadow man everyone stands in shock")
                    input(".")
                    print ("A voice can be feintly heard")
                    input(".")
                    print ("Shadow: Thank you for releasing me from my human form")
                    input(".")
                    print ("Shadow: Shadow Man was a great host")
                    input(".")
                    print ("Shadow: But now you have released the god of darkness")
                    input(".")
                    print ("Shadow: The destined destroyer")
                    input(".")
                    print ("The voice appears and looks like the shadow man but more human")
                    input(".")
                    print ("Shadow: Casting me away since the beginning. forced to hide in the darkness")
                    input(".")
                    print ("Observation man knows he is about to do something awful and tries to stop him")
                    input(".")
                    print ("he grabs hold of him but a shadow spike appears from out the ground he tries to minimise the damage with his hand but it goes through and impales the eye")
                    input(".")
                    print ("Shadow approaches the dead body of shadow man")
                    input(".")
                    print ("Shadow absorbs shadow man and he fades away")
                    input(".")
                    print ("Shadow: He will be back. He was never actually reborn and so he will return as the last reborn. Stronger and more bloodthirsty than ever")
                    input(".")
                    print ("Shadow: Now... You have two shadow after you. A GOD and a CHAMPION")
                    input(".")
                    print ("ROCK: What will you do?")
                    input(".")
                    print ("Shadow: Destroy. as the SHADONI")
                    print ("decaying hands appear on his back before he teleports away")
                    input(".")
                    print ("OBSERVATION MAN shows signs of life and you approach him")
                    input(".")
                    print ("He then expands and grows endlessly into a 700ft giant")
                    print ("ALL-KNOWING: He has reverted back to his primal nature. i would leave this area immediately")
                    input(".")
                    print ("You and the rock run away before a giant hand slams down onto the rock crushing all his bones killing him")
                else:
                    print ("The twin shadows are going to be a issue")
            
            if position == "W":
                if Witcher == True:
                    print ("You look behind you and a orc goes to stab you")
                    input(".")
                    print ("The orc is decapitated and when the blood clears you can see geralt of rivia")
                    input(".")
                    print ("Geralt: I have heard there is a monster around.")
                    input(".")
                    print ("Geralt: A hydra, multiple heads, able to use magic")
                    input(".")
                    print ("Geralt: They call it KAVU?")
                    input(".")
                    print ("Geralt: Do you want to accompany me in hunting it down")
                    print ("The nemesis emerges from some debris and makes his way towards you")
                    input(".")
                    print ("It uses its tentacle extension but geralt slices them before they make contact with him")
                    file = open ("Power.txt","r")
                    Power = file.read()
                    if Power == "Atomic Breath":
                        print ("You use your atomic breath to destroy the nemesis")
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
                    if Power == "Force":
                        print ("You force push into a gas station that sets off a chain explosion emitting fire everywhere")
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
                    time.sleep(5)
                    print ("Geralt: I will find you soon and we need to talk")
                else:
                    print ("The witcher says to find him again")
        print ("")
        print ("A man in a hood rolls out of a bush and swings his sword towards you") 
        input(".") 
        print ("Vader pushes him over and his hood falls off revealing himself to be ezio, the assassin")  
        input(".")    
        if Power == "Force":
            print ("You and Vader notice there is something approaching you")
        else:
            print ("You see something approaching from the distance")
        print ("Vader uses the force against it slowing it down causing their arms to tear off due to their sheer speed and sudden impact of the force")
        input(".")    
        print ("The person is revealed to be A-Train and drops onto both knees with no arms")
        input(".")    
        print ("Vader stabs him in the chest killing him")
        input(".")    
        print ("MR TIME appears")
        input(".")    
        print ("MR TIME: i can bring back the gods")
        input(".")    
        print ("MR TIME: But i will have to bring back everyone else from the past")
        input(".")    
        print ("MR TIME: Bad and good..")
        input(".")    
        print ("MR TIME: I am sure people like you, Vader can handle the humans of this earth")
        input(".")    
        print ("MR TIME: This will mean the collapse of all time lines and i will be handed the same fate as observation man as i have broke my own will")
        input(".")    
        print ("MR TIME: I will EXPAND to my giant form")
        input(".")    
        print ("MR TIME glows green and you can feel time accelerate backwards")
        input(".")    
        print ("MR TIME expands into giant form and gets hit by a meteor in the sky")
        input(".")    
        print ("Rock: Its ultimate andy")
        input(".")    
        print ("Andy shoots lasers from his eyes and hands that destroy MR Time")
        input(".")    
        print ("Andy then flies through MR TIME leaving a burning hole in his chest")
        input(".")    
        print ("MR TIME lives.. only just")
        input(".")    
        print ("MR TIME is not in good condition and walks away")
        input(".")    
        END()






                    


                


    import Void





    main(mapChoice, playerMap, position)


def END():
    print ("KAVU lands and screams at you all")
    input(".")
    print ("GODZILLA beams him through multiple buildings")
    input(".")
    print ("KAVU gets back up and fires ice,fire and lightning at godzilla")
    input(".")
    print ("Godzilla gets injured heavily from the different elements")
    input(".")
    print ("You now have to fight KAVU, Ruler of the underworld")
    Kavu()


def Kavu():
    print ("Vader joins the battle")
    time.sleep(2)
    print ("Observation Man joins the battle..")
    time.sleep(2)
    print ("Ezio joins the battle")
    time.sleep(2)
    print ("Geralt joins the battle")
    time.sleep(2)
    print ("Godzilla joins the battle")
    time.sleep(2)
    Vader = 10000
    ObservationMan = 50000
    Ezio = 1000
    Geralt = 2500
    Godzilla = 80000
    HP = Player.health * 100
    KAVU = 10000000
    Burn = 1
    Stun = False
    Cancer = False
    Onehand = True
    Twohand = False
    while KAVU >= 0:
        if Vader <= 0:
            print ("Darth Vader is holding on for his life")
            Vader = 0
        if ObservationMan <= 0:
            print ("Observation Man has turned to stone")
            ObservationMan = 0
        if Ezio <= 0:
            print ("Ezio is dead")
            Ezio = 0
        if Geralt <= 0:
            print ("Geralt is injured")
            Geralt = 0
        if Godzilla <= 0:
            print ("Godzilla drops to the floor")
            Godzilla = 0
        print ("Vader:",Vader)
        print ("Observation Man:",ObservationMan)
        print ("Ezio:",Ezio)
        print ("Geralt:",Geralt)
        print ("Godzilla:",Godzilla)
        print ("HP:",HP)
        print ("KAVU:", KAVU)
        if Vader > 0:
            Move = random.randint (1,3)
            if Move == 1:
                print ("Vader forcepushes Kavu")
                Force = 100000
                print ("{",Force,"}")
                KAVU = KAVU - Force
                time.sleep(2)
                if KAVU <= 0:
                    break
            if Move == 2:
                print ("Vader throws his lightsaber at KAVU")
                Force = 50000
                print ("{",Force,"}")
                KAVU = KAVU - Force
                time.sleep(2)
                if KAVU <= 0:
                    break
            if Move == 3:
                print ("Vader swings his lightsaber")
                Force = 1000000
                print ("{",Force,"}")
                KAVU = KAVU - Force
                time.sleep(2)
                if KAVU <= 0:
                    break
        if ObservationMan > 0:
            Move = random.randint (1,3)
            if Move == 1:
                print ("Observation Man charges up the eye and lets out a golden laserbeam")
                Attack = 2000000
                print ("{",Attack,"}")
                KAVU = KAVU - Attack
                time.sleep(2)
                if KAVU <= 0:
                    break
            if Move == 2:
                print ("Observation Man strikes KAVU with his giant hands")
                Attack = 55000
                print ("{",Attack,"}")
                KAVU = KAVU - Attack
                time.sleep(2)
                if KAVU <= 0:
                    break
            if Move == 3:
                print ("Observation Man throws Kavu onto the ground")
                Attack = 125000
                print ("{",Attack,"}")
                KAVU = KAVU - Attack
                time.sleep(2)
                if KAVU <= 0:
                    break
        if Ezio > 0:
            Move = random.randint (1,3)
            if Move == 1:
                print ("Ezio throws a dagger")
                Attack = 1000
                print ("{",Attack,"}")
                KAVU = KAVU - Attack
                time.sleep(2)
                if KAVU <= 0:
                    break
            if Move == 2:
                print ("Ezio cuts with his sword")
                Attack = 500
                print ("{",Attack,"}")
                KAVU = KAVU - Attack
                time.sleep(2)
                if KAVU <= 0:
                    break
            if Move == 3:
                print ("Ezio shoots Kavu")
                Attack = 1005
                print ("{",Attack,"}")
                KAVU = KAVU - Attack
                time.sleep(2)
                if KAVU <= 0:
                    break
        if Geralt > 0:
            Move = random.randint (1,3)
            if Move == 1:
                print ("Geralt cuts with his monster killing sword")
                Attack = 15000
                print ("{",Attack,"}")
                KAVU = KAVU - Attack
                time.sleep(2)
                if KAVU <= 0:
                    break
            if Move == 2:
                print ("Geralt uses a witcher sign")
                Witcher = random.randint(1,4)
                if Witcher == 1:
                    Form = random.randint(1,2)
                    if Form == 1:
                        print ("Geralt manipulates kinetic energy to force Kavu back")
                        Attack = 50
                        print ("{",Attack,"}")
                        KAVU = KAVU - Attack
                        time.sleep(2)
                        if KAVU <= 0:
                            break
                    if Form == 2:
                        print ("Geralt uses an area of blast effect")
                        Attack = 100
                        print ("{",Attack,"}")
                        KAVU = KAVU - Attack
                        time.sleep(2)
                        if KAVU <= 0:
                            break
                if Witcher == 2:
                    print ("Geralt fires a jet of flame out his hand")
                    fire = random.randint(1,10)
                    Attack = 100000
                    print ("{",Attack,"}")
                    KAVU = KAVU - Attack
                    if fire > 5:
                        print ("KAVU catches the flame and it begins to burn him before he uses the ice beam to put it out")
                        fire = 1000 * Burn
                        Burn = Burn + 1
                    time.sleep(2)
                    if KAVU <= 0:
                        break
                if Witcher == 3:
                    print ("Geralt stuns KAVU")
                    Attack = 10
                    print ("{",Attack,"}")
                    KAVU = KAVU - Attack
                    time.sleep(2)
                    Stun = True
                    if KAVU <= 0:
                        break
                if Witcher == 4:
                    print ("The witcher gives himself a shield and heals himself and you of any wounds")
                    Heal = 200
                    Witcher = Witcher + Heal
                    HP = HP + 200
                    print ("+", Heal)
            if Move == 3:
                print ("The Witcher shoots a crossbow at kavu")
                Attack = 1550
                print ("{",Attack,"}")
                KAVU = KAVU - Attack
                time.sleep(2)
                if KAVU <= 0:
                    break
        if Godzilla > 0:
            Move = random.randint (1,2)
            if Move == 1:
                print ("Godzilla charges his beam and sends it powerfully towards KAVU")
                Radioactive = random.randint(1,40)
                Attack = 1000000
                print ("{",Attack,"}")
                KAVU = KAVU - Attack
                if Radioactive >= 30:
                    Cancer = True
                time.sleep(2)
                if KAVU <= 0:
                    break
            if Move == 2:
                print ("Godzilla bites KAVU")
                Attack = 500000
                print ("{",Attack,"}")
                KAVU = KAVU - Attack
                time.sleep(2)
                if KAVU <= 0:
                    break
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
                KAVU = KAVU - Slash  
                if KAVU <= 0:
                    break
            if Choice in answer_B:
                print ("You throw your lightsaber at KAVU and use the force to bring your lightsaber back to you")
                Throw = 4999
                time.sleep(3)
                print ("{",Throw,"}")
                KAVU = KAVU - Throw
                if KAVU <= 0:
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
                choice = input(">>")
                if choice in answer_A:
                    print ("You force push KAVU into a wall")
                    Push = 200
                    time.sleep(3)
                    print ("{",Push,"}")
                    KAVU = KAVU - Push
                    if KAVU <= 0:
                        break
                if choice in answer_B:
                    print ("You use the force to pick up KAVU and strangle the king")
                    Choke = 100000
                    time.sleep(3)
                    print ("{",Choke,"}")
                    KAVU = KAVU - Choke
                    if KAVU <= 0:
                        break
            if Power == "Atomic Breath":
                Radioactive = random.randint(1,33)
                print ("You beam KAVU")
                Atom = 100000
                print ("{",Atom,"}")
                KAVU = KAVU - Atom
                if Radioactive >= 30:
                    Cancer = True
                
        if choice in answer_A:
                file = open ("Weapon.txt", "r")
                Special = file.read()
                if Special == "Combistick":
                    print ("The combistick allows you to attack with speed and you manage to get a lot of piercing hits on KAVU")
                    Spear = random.randint(6000,10000)
                    time.sleep(3)
                    print ("{",Spear,"}")
                    KAVU = KAVU - Spear
                    if KAVU <= 0:
                        break
                if Special == "PredatorBlade":
                    print ("You swing your arms in a fast motion with the blades attached to your arms")
                    Arm = random.randint(1000,3000)
                    time.sleep(3)
                    print ("{",Arm,"}")
                    KAVU = KAVU - Arm
                    if KAVU <= 0:
                        break
                if Special == "Ornamental Dagger":
                    print ("You slash KAVU with a dagger")
                    Dagger = random.randint(400,500)
                    time.sleep(3)
                    print ("{",Dagger,"}")
                    KAVU = KAVU - Dagger
                    if KAVU <= 0:
                        break
                if Special == "Shoulder Cannon":
                    print ("C: You aim the cannon and fire at the massive target of KAVU")
                    Cannon = 150000
                    time.sleep(3)
                    print ("{",Cannon,"}")
                    KAVU = KAVU - Cannon
                    if KAVU <= 0:
                        break
        if Cancer == True:
            print ("The atomic breath is having an effect on KAVU")
            time.sleep(3)
            print ("KAVU shows a sense of dizziness")
            Poison = random.randint(100000,1000000)
            KAVU = KAVU - Poison
            Stun = True
            Cancer = False
        if Stun == False:
            print ("Kavu sends a lightning bolt down")
            time.sleep(2)
            Target = random.randint(1,6)
            if Target == 1:
                if Vader <= 0:
                    print ("It hits you")
                    Attack = random.randint(100,200)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    HP = HP - Attack 
                else:
                    print ("it hits Darth Vader")
                    Attack = random.randint(10000,30000)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    Vader = Vader - Attack
            if Target == 2:
                if Ezio <= 0:
                    print ("It hits you")
                    Attack = random.randint(100,200)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    HP = HP - Attack 
                else:
                    print ("it hits Ezio")
                    Attack = random.randint(1000,10000)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    Ezio = Ezio - Attack
            if Target == 3:
                if ObservationMan >= 0:
                    print ("It hits you")
                    Attack = random.randint(100,200)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    HP = HP - Attack 
                else:
                    print ("it hits Observation Man")
                    Attack = random.randint(10000,15000)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    ObservationMan = ObservationMan - Attack
            if Target == 4:
                if Geralt <= 0:
                    print ("It hits you")
                    Attack = random.randint(100,200)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    HP = HP - Attack
                else:     
                    print ("it hits geralt")
                    Attack = random.randint(100,300)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    Geralt = Geralt - Attack
            if Target == 5:
                if Godzilla <= 0:
                    print ("It hits you")
                    Attack = random.randint(100,200)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    HP = HP - Attack
                else:                  
                    print ("it hits Godzilla")
                    Attack = random.randint(10000,20000)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    Godzilla = Godzilla - Attack
            if Target == 6:
                print ("it hits you")
                Attack = random.randint(100,200)
                time.sleep(3)
                print ("{",Attack,"}")
                HP = HP - Attack
            print ("Kavu sends a ice beam")
            time.sleep(2)
            Target = random.randint(1,6)
            if Target == 1:
                if Vader <= 0:
                    print ("It hits you")
                    Attack = random.randint(100,200)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    HP = HP - Attack 
                else:
                    print ("it hits Darth Vader")
                    Attack = random.randint(10000,30000)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    Vader = Vader - Attack
            if Target == 2:
                if Ezio <= 0:
                    print ("It hits you")
                    Attack = random.randint(100,200)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    HP = HP - Attack 
                else:
                    print ("it hits Ezio")
                    Attack = random.randint(1000,10000)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    Ezio = Ezio - Attack
            if Target == 3:
                if ObservationMan >= 0:
                    print ("It hits you")
                    Attack = random.randint(100,200)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    HP = HP - Attack 
                else:
                    print ("it hits Observation Man")
                    Attack = random.randint(10000,15000)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    ObservationMan = ObservationMan - Attack
            if Target == 4:
                if Geralt <= 0:
                    print ("It hits you")
                    Attack = random.randint(100,200)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    HP = HP - Attack
                else:     
                    print ("it hits geralt")
                    Attack = random.randint(100,300)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    Geralt = Geralt - Attack
            if Target == 5:
                if Godzilla <= 0:
                    print ("It hits you")
                    Attack = random.randint(100,200)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    HP = HP - Attack
                else:                  
                    print ("it hits Godzilla")
                    Attack = random.randint(10000,20000)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    Godzilla = Godzilla - Attack
            if Target == 6:
                print ("it hits you")
                Attack = random.randint(100,200)
                time.sleep(3)
                print ("{",Attack,"}")
                HP = HP - Attack
            print ("Kavu sends a jet of flames and fireballs towards you")
            time.sleep(2)
            Target = random.randint(1,6)
            if Target == 1:
                if Vader <= 0:
                    print ("It hits you")
                    Attack = random.randint(100,200)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    HP = HP - Attack 
                else:
                    print ("it hits Darth Vader")
                    Attack = random.randint(10000,30000)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    Vader = Vader - Attack
            if Target == 2:
                if Ezio <= 0:
                    print ("It hits you")
                    Attack = random.randint(100,200)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    HP = HP - Attack 
                else:
                    print ("it hits Ezio")
                    Attack = random.randint(1000,10000)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    Ezio = Ezio - Attack
            if Target == 3:
                if ObservationMan >= 0:
                    print ("It hits you")
                    Attack = random.randint(100,200)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    HP = HP - Attack 
                else:
                    print ("it hits Observation Man")
                    Attack = random.randint(10000,15000)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    ObservationMan = ObservationMan - Attack
            if Target == 4:
                if Geralt <= 0:
                    print ("It hits you")
                    Attack = random.randint(100,200)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    HP = HP - Attack
                else:     
                    print ("it hits geralt")
                    Attack = random.randint(100,300)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    Geralt = Geralt - Attack
            if Target == 5:
                if Godzilla <= 0:
                    print ("It hits you")
                    Attack = random.randint(100,200)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    HP = HP - Attack
                else:                  
                    print ("it hits Godzilla")
                    Attack = random.randint(10000,20000)
                    time.sleep(3)
                    print ("{",Attack,"}")
                    Godzilla = Godzilla - Attack
            if Target == 6:
                print ("it hits you")
                Attack = random.randint(100,200)
                time.sleep(3)
                print ("{",Attack,"}")
                HP = HP - Attack
        else:
            print ("KAVU is stunned and remains immobile")
            Stun = False

        if HP <= 0:
            print ("You died")
            time.sleep(2)
            Kavu()

    print ("KAVU FALLS")
    input(".")
    print ("Ezio dies covered in blood")
    input(".")
    print ("You approach KAVU")
    input(".")
    print ("A: Attempt to befriend")
    print ("B: Kill")
    Flag = True
    while Flag == True:
        choice = input("CHOOSE >> ")
        if choice in answer_A:
            print ("You approach the destroyed KAVU")
            input(".")
            print ("You touch his head and a white glow shines from your hand")
            input(".")
            print ("KAVU looks up to you with a glow in his eyes")
            input(".")
            print ("NEW COMPANION: KAVU, RULER OF UNDERWORLD")
            print ("END OF CHAPTER 1: THE SHADOWS OF EVIL")
            file = open("Companion.txt","w")
            file.write("Kavu /n")
            file.close()
            s = "Chapter2"
            save(s)
            import Void

        if choice in answer_B:
            print ("You cut off the head of KAVU and drink the blood as it pours into your mouth")
            input(".")
            print ("Geralt rips out its heart")
            print ("Geralt: Got to make sure its dead")
            input(".")
            print ("You eat the heart and feel a power run through you of THE DRAGON")
            file = open ("Dragon.txt","w")
            file.write("Kavu \n")
            file.close()
            s = "Chapter2"
            save(s)
            import Void








        
        
            


file=open("loadfile.txt","r")
room=file.read()
file.close()        

if room != "Chapter2":
    LA()