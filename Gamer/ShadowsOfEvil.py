
import os,sys
import os.path
import Character as Character# Import character to access character types
import time
import Weapons as Weapons
from Weapons import Lightsaber, Sword




answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
DUEL = ["D", "d"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
player = Character.gamer


def save(s):
    file=open("loadfile.txt","w")
    file.write(s)
    file.close()

s ="ShadowsOfEvil"
save(s)
required = ("\nUse only A, B, or C\n") 

file = open("CharacterClass.txt","r")
char_type = file.read()



def Intro():
    Character.Gold = 100
    print ("Chapter 1: Shadows Of Evil")
    time.sleep(3)
    print ("You are walking through Dawnmire and find a group of soliders")
    time.sleep(3)
    print ("Soldier: HEY YOU!")
    print ("Soldier: Have you seen any disturbance from a hydra lately?")
    time.sleep(4)
    print ("Soldier: It goes by the name KAVU?")
    time.sleep(3)
    print ("Soldier: You look lost do you even know where you are?")
    time.sleep(4)
    print ("Soldier: This is Dawnmire a town in the world of Deakoon")
    time.sleep(4)
    print ("You ask about Deakoon which makes the soldier realise...")
    time.sleep(3)
    print ("Soldier: You are a reborn arent you? You come from Earth?")
    time.sleep(5)
    print ("Soldier: Maybe you can help us escape this hellish realm, The Shadow Man made this world to protect himself all the other worlds are out there.")
    time.sleep(7)
    print ("Soldier: Stay here in Dawnmire, i am going to get someone to aid us.")
    if player.char_type == "mage":
        from Mage import Dawnmire
    if player.char_type == "thief":
        from Thief import Dawnmire
    if player.char_type == "prisoner":
        from Prisoner import Dawnmire
    if player.char_type == "gamer":
        from Gamer import Dawnmire
    if player.char_type == "vagabound":
        from Vagabound import Dawnmire
    if player.char_type == "warrior":
        from Warrior  import Dawnmire

Intro()