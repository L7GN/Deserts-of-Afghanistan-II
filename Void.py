from ast import Delete
import os,sys
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
print ("You look upon all the multiverses through the VOID")
File = open("loadfile.txt")
Level = File.read()

Earth = True

if Earth == True:
    print ("Earth")


if Level == "Chapter2":
    print ("CHAPTER2")





Flag = True

while Flag == True:
    Point = input(">>")

    if Point.lower() == "earth":
        import Earth

    if Point.lower() == "chapter2":
        import Chapter2


