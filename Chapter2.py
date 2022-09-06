from ast import And
from asyncio import shield
import os,sys
from re import M
from pickle import TRUE
import os.path
import Character as Character# Import character to access character types
import time
import Weapons as Weapon
import random
player = Character.warrior

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
DUEL = ["D", "d"]
yes = ["Y", "y", "yes"] 
no = ["N", "n", "no"]

print ("CHAPTER 2: RISE OF THE DEAD| Andy")


def intro():
    print ("You are flying in the air")
    time.sleep(2)
    print ("You crash down from the air and laser through a building")
    time.sleep(4)
    print ("You see mr fantastic he stretches to hit you")
    time.sleep(5)
    print ("You grab his arm and start swinging him him around in circles")
    time.sleep(5)
    print ("You progressively get faster and faster until eventually he shreds to pieces")
    input(".")
    print ("You fly back up in the air and go to the entrance of a college")
    input(".")
    print ("You explode the entrance and enter")
    input(".")
    print ("You laser the staff at the entrance and go up to the second floor")
    input(".")
    print ("You enter room 207")
    input(".")
    print ("ANDY: Joanne..")
    input(".")
    print ("A swarm of flies attack you and bite your face")
    input(".")
    print ("You set your body aflame and burn the flies. You run to a window and see a figure fly away with wings")
    input(".")
    print ("You get kicked out the window by captain america")
    input(".")
    print ("He throws his shield and you laser through it and hit his leg")
    input(".")
    print ("He limps away")
    input(".")
    print ("You see the power of MR TIME around you and feel like you are going back and forward in time")
    input(".")
    print ("It stops")
    input(".")
    print ("You see osiris behind you")
    OsirisFight()


def OsirisFight():
    Aflame = 1
    Cryo = False
    Bar = 0
    Andy = 10000000
    OsirisShield = 1000000
    Shield = True
    Osiris = 10000000
    while Osiris >= 0:
        print ("Andy:", Andy)
        if Shield == True:
            print ("Osiris:", OsirisShield)
        else:
            print ("Osiris:", Osiris)
        print ("A: Attack")
        print ("B: Abilites")
        print ("C: Run")
        Move = input(">>")
        if Move in answer_A:
            print ("A: Energy")
            print ("B: Physical Strength")
            print ("C: Elements")
            choice = input(">>")
            if choice in answer_A:
                print ("A: Energy Beam")
                print ("B:Laser Eyes")
                print ("C:Energy Manipulation")
                Choice = input(">>")
                if Choice in answer_A:
                    print ("You shoot a energy beam out your chest")
                    if Shield == True:
                        Attack = random.randint(10000,50000) * Aflame
                        print ("{",Attack,"}")
                        OsirisShield = OsirisShield - Attack
                        if Osiris <= 0:
                            break
                    else:
                        Attack = 90000 * Aflame
                        print ("{",Attack,"}")
                        Osiris = Osiris - Attack
                        if Osiris <= 0:
                            break
                    Bar = Bar + 10
                if Choice in answer_B:
                    print ("You shoot a energy beam out your chest")
                    if Shield == True:
                        Attack = random.randint(25000,50000) * Aflame
                        print ("{",Attack,"}")
                        OsirisShield = OsirisShield - Attack
                        if Osiris <= 0:
                            break
                    else:
                        Attack = 100000 * Aflame
                        print ("{",Attack,"}")
                        Osiris = Osiris - Attack
                        if Osiris <= 0:
                            break
                    Bar = Bar + 7
                if Choice in answer_C:
                    Super = random.randint(1,3)
                    if Super == 1:
                        print ("You throw a yellow orb that explodes like a nuke")
                        if Shield == True:
                            Attack = random.randint(100000,500000) * Aflame
                            print ("{",Attack,"}")
                            OsirisShield = OsirisShield - Attack
                            if Osiris <= 0:
                                break
                        else:
                            Attack = 300000 * Aflame
                            print ("{",Attack,"}")
                            Osiris = Osiris - Attack
                            if Osiris <= 0:
                                break
                        Bar = Bar + 5
                    if Super == 2:
                        print ("You use the power of the sun to send a scorching beam down at Osiris")
                        if Shield == True:
                            Attack = random.randint(100000,500000) * Aflame
                            print ("{",Attack,"}")
                            OsirisShield = OsirisShield - Attack
                            if Osiris <= 0:
                                break
                        else:
                            Attack = 500000 * Aflame
                            print ("{",Attack,"}")
                            Osiris = Osiris - Attack
                            if Osiris <= 0:
                                break
                        Bar = Bar + 15
                    if Super == 3:
                        print ("You force the stars to shoot down at Osiris")
                        if Shield == True:
                            Attack = random.randint(120000,500000) * Aflame
                            print ("{",Attack,"}")
                            OsirisShield = OsirisShield - Attack
                            if Osiris <= 0:
                                break
                        else:
                            Attack = 200000 * Aflame
                            print ("{",Attack,"}")
                            Osiris = Osiris - Attack 
                            if Osiris <= 0:
                                break
                        Bar = Bar + 2
            if choice in answer_B:
                print ("A: Superman Punch")
                print ("B: Super kick")
                print ("C: Grandslam")
                Choice = input(">>")
                if Choice in answer_A:
                    print ("You jump up and hit a superpunch")
                    if Shield == True:
                        Attack = random.randint(1000,5000) * Aflame
                        print ("{",Attack,"}")
                        OsirisShield = OsirisShield - Attack
                        if Osiris <= 0:
                            break
                    else:
                        Attack = 9000 * Aflame
                        print ("{",Attack,"}")
                        Osiris = Osiris - Attack
                        if Osiris <= 0:
                            break
                    Bar = Bar + 3
                if Choice in answer_B:
                    print ("You hit a tornado kick on Osiris")
                    if Shield == True:
                        Attack = random.randint(250,500) * Aflame
                        print ("{",Attack,"}")
                        OsirisShield = OsirisShield - Attack
                        if Osiris <= 0:
                            break
                    else:
                        Attack = 1000 * Aflame
                        print ("{",Attack,"}")
                        Osiris = Osiris - Attack
                        if Osiris <= 0:
                            break
                    Bar = Bar + 2
                if Choice in answer_C:
                    print ("You slam Osiris into the floor and stomp on his head")
                    if Shield == True:
                        Attack = random.randint(2500,5000) * Aflame
                        print ("{",Attack,"}")
                        OsirisShield = OsirisShield - Attack
                        if Osiris <= 0:
                            break
                    else:
                        Attack = 10000 * Aflame
                        print ("{",Attack,"}")
                        Osiris = Osiris - Attack
                        if Osiris <= 0:
                            break
                    Bar = Bar + 6
            if choice in answer_C:
                print ("A: Water")
                print ("B: Fire")
                print ("C: Lightning")
                Choice = input(">>")
                if Choice in answer_A:
                    print ("You shoot water powerfully through a cannon on your back.")
                    if Cryo == False:
                        if Shield == True:
                            Attack = 1000
                            print ("{",Attack,"}")
                            OsirisShield = OsirisShield - Attack
                            if Osiris <= 0:
                                break
                        else:
                            Attack = 1000
                            print ("{",Attack,"}")
                            OsirisShield = OsirisShield - Attack
                            if Osiris <= 0:
                                break
                    else:
                        if Shield == True:
                            Attack = 10000
                            print ("{",Attack,"}")
                            OsirisShield = OsirisShield - Attack
                            if Osiris <= 0:
                                break
                        else:
                            Attack = 10000
                            print ("{",Attack,"}")
                            Osiris = Osiris - Attack
                            if Osiris <= 0:
                                break
                if Choice in answer_B:
                    print ("You use the cannon on your back as a flamethrower")
                    if Shield == True:
                        Attack = random.randint(2500,5000) * Aflame
                        print ("{",Attack,"}")
                        OsirisShield = OsirisShield - Attack
                        if Osiris <= 0:
                            break
                    else:
                        Attack = 10000 * Aflame
                        print ("{",Attack,"}")
                        Osiris = Osiris - Attack
                        if Osiris <= 0:
                            break
                if Choice in answer_C:
                    print ("You emit lightning from the cannon")
                    if Shield == True:
                        Attack = random.randint(25,50) * Aflame
                        print ("{",Attack,"}")
                        OsirisShield = OsirisShield - Attack
                        if Osiris <= 0:
                            break
                    else:
                        Attack = 100 * Aflame
                        print ("{",Attack,"}")
                        Osiris = Osiris - Attack
                        if Osiris <= 0:
                            break



        if Move in answer_B:
            print ("A:Body aflame")
            print ("B: Cryostasis")
            if Bar >= 100:
                print ("C: ULTIMATE")
            Choice = input(">>")
            if Choice in answer_A:
                print ("You set yourself on fire")
                Aflame = 2.5
                Cryo = False
                Andy = Andy - 10000
            if Choice in answer_B:
                print ("You freeze your body")
                Andy = Andy + 1000000
                Cryo = True
                Aflame = 1
            if Choice in answer_C:
                if Bar >= 100:
                    print ("You enter ULTIMATE")
                    print ("All the elements orbit around you, The stars shine brighter towards you")
                    Andy = 99999999
                    Aflame = 100
                    Cryo = True
                    Bar = 0
        
            


            
        if Move in answer_C:
            print ("You run away but get reversed back in time")
            OsirisFight()
        
        print ("Osiris uses his crook and flail")
        if Cryo == True:
            Attack = 10000
            print ("{",Attack,"}")
            Andy = Andy - Attack
        else:
            Attack = random.randint(10000,100000)
            print ("{",Attack,"}")
            Andy = Andy - Attack
        time.sleep(4)
        if Cryo == True:
            Attack = 10000
            print ("{",Attack,"}")
            Andy = Andy - Attack
        else:
            Attack = random.randint(100000,2000000)
            print ("{",Attack,"}")
            Andy = Andy - Attack
        if Shield == False:
            if Osiris < 150000:
                heal = random.randint(4,13)
            else:
                heal = random.randint(1,10)
                if heal > 8:
                    print ("Osiris regenerates")
                    Heal = random.randint(10000,100000)
                    Osiris = Osiris + Heal
                else:
                    print ("")
        if OsirisShield <= 0:
            if Shield == False:
                print ("")
            else:
                print ("Osiris drops to the floor")
                time.sleep(3)
                print ("Blood pours out of Osiris")
                time.sleep(2)
                print ("The god is dead")
                time.sleep(3)
                print ("Osiris uses his power one last time to ressurect his dead body")
                time.sleep(5)
                print ("Osiris is still weak and is now a rotting corpse")
                time.sleep(4)
                print ("Osiris: One more time")
                Shield = False
        if Andy <= 0:
            print ("YOU DIED")
            OsirisFight()

    print ("OSIRIS SLAINED")
    input(".")
    print ("You shred osiris into pieces")
    input(".")
    print ("Moonknight jumps you and throws his scepters at you")
    MoonKnightFight()


def MoonKnightFight():
    print ("MR TIME: ANDY STOP!")
    time.sleep(2)
    print ("MR TIME: THIS IS THE PLAN TO STOP SHADOW MAN")
    time.sleep(3)
    print ("ANDY: I do not care about your plan")
    print ("Moon Knight: Then i will have to kill you then")
    Aflame = 1
    Cryo = False
    Bar = 0
    Andy = 10000000
    MoonKnight = 10000000
    MrKnight = 1000000
    MK = True
    MRK = False
    while MoonKnight or MrKnight >= 0:
        print ("Andy:", Andy)
        if MK == True:
            print ("Moonknight: ", MoonKnight)
        if MRK == True:
            print ("MR KNIGHT: ", MrKnight)
        print ("A: Attack")
        print ("B: Abilites")
        print ("C: Run")
        Move = input(">>")
        if Move in answer_A:
            print ("A: Energy")
            print ("B: Physical Strength")
            print ("C: Elements")
            choice = input(">>")
            if choice in answer_A:
                print ("A: Energy Beam")
                print ("B:Laser Eyes")
                print ("C:Energy Manipulation")
                Choice = input(">>")
                if Choice in answer_A:
                    print ("You shoot a energy beam out your chest")
                    Attack = random.randint(10000,50000) * Aflame
                    print ("{",Attack,"}")
                    if MK == True:
                        MoonKnight = MoonKnight - Attack
                    if MRK == True:
                        MrKnight = MrKnight - Attack
                    if MoonKnight and MrKnight <= 0:
                        break
                    Bar = Bar + 15
                if Choice in answer_B:
                    print ("You shoot a energy beam out your chest")
                    Attack = random.randint(25000,50000) * Aflame
                    print ("{",Attack,"}")
                    if MK == True:
                        MoonKnight = MoonKnight - Attack
                    if MRK == True:
                        MrKnight = MrKnight - Attack
                    if MoonKnight and MrKnight <= 0:
                        break

                    Bar = Bar + 7
                if Choice in answer_C:
                    Super = random.randint(1,3)
                    if Super == 1:
                        print ("You throw a yellow orb that explodes like a nuke")
                        Attack = random.randint(100000,500000) * Aflame
                        print ("{",Attack,"}")
                        if MK == True:
                            MoonKnight = MoonKnight - Attack
                        if MRK == True:
                            MrKnight = MrKnight - Attack
                        if MoonKnight and MrKnight <= 0:
                            break

                        Bar = Bar + 5
                    if Super == 2:
                        print ("You use the power of the sun to send a scorching beam down")
                        Attack = random.randint(100000,500000) * Aflame
                        print ("{",Attack,"}")
                        if MK == True:
                            MoonKnight = MoonKnight - Attack
                        if MRK == True:
                            MrKnight = MrKnight - Attack
                        if MoonKnight and MrKnight <= 0:
                            break

                        Bar = Bar + 15
                    if Super == 3:
                        print ("You force the stars to shoot down")
                        Attack = random.randint(120000,500000) * Aflame
                        print ("{",Attack,"}")
                        if MK == True:
                            MoonKnight = MoonKnight - Attack
                        if MRK == True:
                            MrKnight = MrKnight - Attack
                        if MoonKnight and MrKnight <= 0:
                            break
   
                        Bar = Bar + 2
            if choice in answer_B:
                print ("A: Superman Punch")
                print ("B: Super kick")
                print ("C: Grandslam")
                Choice = input(">>")
                if Choice in answer_A:
                    print ("You jump up and hit a superpunch")
                    Attack = random.randint(1000,5000) * Aflame
                    print ("{",Attack,"}")
                    if MK == True:
                        MoonKnight = MoonKnight - Attack
                    if MRK == True:
                        MrKnight = MrKnight - Attack
                    if MoonKnight and MrKnight <= 0:
                        break

                    Bar = Bar + 3
                if Choice in answer_B:
                    print ("You hit a tornado kick")
                    Attack = random.randint(250,500) * Aflame
                    print ("{",Attack,"}")
                    if MK == True:
                        MoonKnight = MoonKnight - Attack
                    if MRK == True:
                        MrKnight = MrKnight - Attack
                    if MoonKnight and MrKnight <= 0:
                        break

                    Bar = Bar + 2
                if Choice in answer_C:
                    print ("You slam into the floor")
                    Attack = random.randint(2500,5000) * Aflame
                    print ("{",Attack,"}")
                    if MK == True:
                        MoonKnight = MoonKnight - Attack
                    if MRK == True:
                        MrKnight = MrKnight - Attack
                    if MoonKnight and MrKnight <= 0:
                        break

                    Bar = Bar + 6
            if choice in answer_C:
                print ("A: Water")
                print ("B: Fire")
                print ("C: Lightning")
                Choice = input(">>")
                if Choice in answer_A:
                    print ("You shoot water powerfully through a cannon on your back.")
                    if Cryo == False:
                            Attack = 1000
                            print ("{",Attack,"}")
                            if MK == True:
                                MoonKnight = MoonKnight - Attack
                            if MRK == True:
                                MrKnight = MrKnight - Attack
                            if MoonKnight and MrKnight <= 0:
                                break
                    else:
                        Attack = 10000
                        print ("{",Attack,"}")
                        if MK == True:
                            MoonKnight = MoonKnight - Attack
                        if MRK == True:
                            MrKnight = MrKnight - Attack
                        if MoonKnight and MrKnight <= 0:
                            break
                if Choice in answer_B:
                    print ("You use the cannon on your back as a flamethrower")
                    Attack = random.randint(2500,5000) * Aflame
                    print ("{",Attack,"}")
                    if MK == True:
                        MoonKnight = MoonKnight - Attack
                    if MRK == True:
                        MrKnight = MrKnight - Attack
                    if MoonKnight and MrKnight <= 0:
                        break
                if Choice in answer_C:
                    print ("You emit lightning from the cannon")
                    if MK == True:
                        MoonKnight = MoonKnight - Attack
                    if MRK == True:
                        MrKnight = MrKnight - Attack
                    if MoonKnight and MrKnight <= 0:
                        break



        if Move in answer_B:
            print ("A:Body aflame")
            print ("B: Cryostasis")
            if Bar >= 100:
                print ("C: ULTIMATE")
            Choice = input(">>")
            if Choice in answer_A:
                print ("You set yourself on fire")
                Aflame = 2.5
                Cryo = False
                Andy = Andy - 10000
            if Choice in answer_B:
                print ("You freeze your body")
                Andy = Andy + 1000000
                Cryo = True
                Aflame = 1
            if Choice in answer_C:
                if Bar >= 100:
                    print ("You enter ULTIMATE")
                    print ("All the elements orbit around you, The stars shine brighter towards you")
                    Andy = 99999999
                    Aflame = 100
                    Cryo = True
                    Bar = 0
        
            


            
        if Move in answer_C:
            print ("You run away but get reversed back in time")
            OsirisFight()
        
        if MK == True:
            Attack = random.randint(100000,1000000)
            print ("Moon Knight throws his scepters at you")
            print ("{",Attack,"}")
            Andy = Andy - Attack
        
        if MRK == True:
            Attack = random.randint(10000,100000)
            print ("Mr Knight punches you")
            print ("{",Attack,"}")
            Andy = Andy - Attack

        if MK == True:
            Form =  random.randint(1,6)
            if Form >= 4:
                if MrKnight >= 0:
                    MRK = True
                    MK = False
                    print ("Moon knight changes to Mr knight")
            
        if MRK == True:
            Form =  random.randint(7,14)
            if Form >= 12:
                if MoonKnight >= 0:
                    MK = True
                    MRK = False
                    print ("Mr knight reverts to Moon Knight")
                
        if MrKnight <= 0:
            if MRK == True:
                print ("Mr Knight dies")
                if MoonKnight >= 0:
                    print ("Moonknight returns")
                    MRK = False
                    MK = True
                else:
                    break
            else:
                print ("")
    
        if MoonKnight <= 0:
            if MK == True:
                print ("Moon Knight dies")
                if MrKnight >= 0:
                    print ("Mr Knight returns")
                    MRK = False
                    MK = True
                else:
                    break
            else:
                print ("")
    
    print ("You rip his spine out")
    input(".")
    print ("MR TIME: Andy... Please")
    time.sleep(2)
    print ("You turn around and get hit by a cane as you fall you feel time accelerate")
    time.sleep(3)
    print ("You are now stuck.. frozen in time")
    import Somalia
    s = "TheEvil"
    save(s)




def save(s):
    file=open("loadfile.txt","w")
    file.write(s)
    file.close()

    s = "TheEvil"
    save(s)





 








intro()