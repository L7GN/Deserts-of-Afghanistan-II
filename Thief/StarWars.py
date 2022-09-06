from ast import Delete
import os,sys
import os.path
import Character as Character# Import character to access character types
import time
import Weapons as Weapons
from Weapons import Lightsaber, Sword
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

s = "StarWars"
save(s)

def intro():
    player.health = 4
    print ("You wake up on the death star")
    input(".")
    print ("You are immediately confronted by darth vader")
    input(".")
    print ("He takes all your weapons away")
    input(".")
    print ("Darth Vader: You will be my apprentice and fight for the dark side")
    input(".")
    print ("You agree as not would mean death")
    input(".")
    print ("You get to train with a lightsaber with Vader")
    player.equipped = Lightsaber
    input(".")
    print ("Darth Vader: You do not have the power of the force")
    input(".")
    print ("Darth Vader: Will you be willing to go under a process to give you the force?")
    choice = input("Y/N? ")
    if choice in yes:
        print ("You go under a experiment that will allow for you to unlock the force")
        input(".")
        file = open ("Power.txt", "w")
        file.write("Force")
        file.close()
    else:
        file = open ("Power.txt", "w")
        file.write("None")
        file.close()
        Defend()

    Defend()

def Defend():
    print ("Doors open and Luke Skywalker emerges")
    input(".")
    print ("Luke: Father, our galaxy is under attack by Sauron's forces")
    input(".")
    print ("Vader: Apprentice, it is time to defend")
    input(".")
    print ("You are responsible for the left side of the defence and encounter OGBOG")
    input(".")
    file = open ("Power.txt","r")
    Power = file.read()
    if Power == "Force":
        print ("He throws two daggers that you revert back towards him with the force he dodges them with a forward roll")
    else:
        print ("Your sharpened reflexes catch one but the other stabs you in the thigh")
        input(".")
        print ("You have to tear the dagger out leaving a gaping wound")
        player.health = 2
    Ogbog()


def Ogbog():
    Onehand = True
    Twohand = False
    OgbogHP = 5000
    HP = player.health * 100
    while OgbogHP > 0:
        print ("Ogbog:", OgbogHP)
        print ("HP:", HP)
        file = open ("Power.txt","r")
        Power = file.read()
        if Power == "Force":
            print ("A: Lightsaber")
            print ("B: Force")
            choice = input(">> ")
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
                    print ("Orcs seem to be weak to lightsaber attacks")
                    time.sleep(3) 
                    print ("{",Slash,"}")
                    OgbogHP = OgbogHP - Slash  
                    if OgbogHP <= 0:
                        break
                if choice in answer_B:
                    print ("After being taught by Vader and having the ability to use the force you can boomerang your lightsaber")
                    Throw = 4999
                    time.sleep(3)
                    print ("{",Throw,"}")
                    OgbogHP = OgbogHP - Throw
                    if OgbogHP <= 0:
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
                    print ("You force push ogbog into a wall")
                    Push = 200
                    time.sleep(3)
                    print ("{",Push,"}")
                    OgbogHP = OgbogHP - Push
                    if OgbogHP <= 0:
                        break
                if choice in answer_B:
                    print ("You use the force to pick up ogbog and start crushing his windpipe")
                    Choke = 100000
                    time.sleep(3)
                    print ("{",Choke,"}")
                    OgbogHP = OgbogHP - Choke
                    if OgbogHP <= 0:
                        break
            print ("Ogbog grabs his two swords")
            Double = random.randint(1,4)
            if Double == 4:
                print ("He stabs you through the stomach with one and decapitates your head off with the other")
                Double = 2000
                print ("{",Double,"}")
                HP = HP - Double
            else:
                print ("You use your lightsaber to block one but he catches you with the other")
                Double = 250
                print ("{",Double,"}")
                HP = HP - Double
            if HP <= 0:
                print ("YOU DIED")
                time.sleep(3)
                Ogbog()
        else:
            print ("A: Lightsaber Slash")
            print ("B: Lightsaber Boomerang")
            print ("C: Onehand/Twohand")
            choice = input(">> ")
            if choice in answer_A:
                if Onehand == True:
                    Slash = random.randint(1000,3000)
                else:
                    Slash = 4000
                print ("Orcs seem to be weak to lightsaber attacks")
                time.sleep(3) 
                print ("{",Slash,"}")
                OgbogHP = OgbogHP - Slash  
                if OgbogHP <= 0:
                    break
            if choice in answer_B:
                print ("After being taught by Vader and having the ability to use the force you can boomerang your lightsaber")
                Throw = 4999
                time.sleep(3)
                print ("{",Throw,"}")
                OgbogHP = OgbogHP - Throw
                if OgbogHP <= 0:
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
            print ("Ogbog grabs his two swords")
            Double = random.randint(1,4)
            if Double == 4:
                print ("He stabs you through the stomach with one and decapitates your head off with the other")
                Double = 2000
                print ("{",Double,"}")
                HP = HP - Double
            else:
                print ("You use your lightsaber to block one but he catches you with the other")
                Double = 250
                print ("{",Double,"}")
                HP = HP - Double
            if HP <= 0:
                print ("YOU DIED")
                time.sleep(3)
                intro()

    print ("Ogbog dusts away")
    time.sleep(2)
    print ("OGBOG: We will meet again, dog")
    input(".")
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
    print ("You can see vader fighting sauron")
    time.sleep(4)
    print ("He is getting frustrated with his efforts trying to land good blows and starts tearing apart the ground and throwing it at him")
    input(".")
    print ("Vader violently swings at sauron in a rage")
    input(".")
    print ("Sauron cannot withstand the attack. he makes one last swinging effort before being impaled in the gut by Vader")
    input(".")
    print ("Sauron...")
    time.sleep(2)
    print ("Defeated")
    time.sleep(2)
    print ("A unusual feeling for someone of his stature")
    time.sleep(3)
    print ("Sauron teleports away")
    print ("Vader: We will meet again in a final battle of our fates")
    input(".")
    print ("Vader: Apprentice...")
    input(".")
    print ("Vader: I am sending you back to Earth")
    input(".")
    print ("Vader:We will meet again im sure")
    print ("Luke: May the force be with you")
    time.sleep(4)
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
        print ("Using the force you stop the fire ball in motion")
        input(".")
        print ("You use so much force it explodes")
        time.sleep(2)
        print ("YOU DIED")
        print ("TIP: Dont encounter a pissed off hydra")
        time.sleep(5)
        Ogbog()
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

        











intro()

