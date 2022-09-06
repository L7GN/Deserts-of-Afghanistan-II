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


def Somalia():
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
    print ("You wake up in a sandy terrain")
    file = open ("CharacterName.txt","r")
    Name = file.read()
    print (Name,": Where am i?")
    time.sleep(4)
    print ("You find a corpse with the flag of Somalia")
    input(".")
    print (Name,": Ive been asleep for 3 days?")
    print (Name,": I need to find MR TIME")
    time.sleep(4)
    print ("You fall through the ground. it was a trap")
    time.sleep(2)
    print ("You find yourself in a cell and can see people impaled on spikes")
    time.sleep(3)
    print ("a voice can be heard through a radio")
    print ("Ben Mendy: Another victim for my game")
    time.sleep(7)
    print ("A figure appears and knocks you out")
    time.sleep(4)
    file = open ("Power.txt","r")
    power = file.read()
    if power == "Force":
        print ("You are put in shackles")
    else:
        print ("You are put in shackles and have a gag on to stop you from being able to speak and use any other powers")
    input(".")
    time.sleep(6)
    print ("The rock approaches your cell and breaks off two of the bars")
    input(".")
    print ("He frees you off the shackes and you escape the cell")
    input(".")
    print ("The rock gets shot in the shoulder")
    input(".")
    print ("The rock shoots the somali pirate dead")
    input(".")
    print ("A wall begins to break")
    input(".")
    print ("You see the face of LAKAKA and begin to run")
    input(".")
    print ("You climb a ladder")
    input(".")
    print ("A: Left B: Right")
    choice = input(">>")
    if choice in answer_A:
        print ("You go left and see a wall with a crack in")
        time.sleep(4)
        print ("You go through the crack in the wall and see LAKAKA with a chainsaw")
        time.sleep(6)
        print ("YOU DIED")
    if choice in answer_B:
        print ("You go right and see stairs")
        if power == "Force":
            print ("You use the force to open a door Vader only jsut dodges out the way of the door")
        else:
            print ("You see a door and it gets forcefully opened by vader")
        print ("LAKAKA escapes with you too and punches VADER to the sky")
        time.sleep(3)
        print ("LAKAKA is very deranged and storms off in confusion")
        input(".")
        print ("The rock crawls towards you")
        input(".")
        print ("You are approached by someone in S.T.A.R.S uniform")
        input(".")
        print ("Jill Valentine: Hands up")
        print (Name, ": We have a injured man here we mean no harm")
        input(".")
        print ("Jill: You need to be careful out here the T-Virus has made its jump from our universe to this earth")
        input(".")
        print ("A helicopter is called for the rock and you stay with Jill to help her find a friend")
        input(".")
        print ("You find a ship")
        input(".")
        print ("You stealth on the ship")
        print ("Jill: He must be here")
        input(".")
        print ("You find Chris Redfield and uncuff him")
        input(".")
        print ("Chris: We need to get off here fast.")
        input(".")
        print ("You go to escape but encounter...")
        input(".")
        print ("3 somali pirates")
        SomaliPirate = 100
        HP = Player.health * 100
        print ("You realise you do not have any of your weapons")
        print ("Somali:", SomaliPirate)
        if power == "Force":
            print ("You disarm him off his gun with the force and choke him to death")
        if power == "Atomic Breath":
            print ("You extinguish off him with your atomic breath")
        else:
            print ("You pounce onto the pirate and punch him until he is nearly dead before ripping his heart out")
        time.sleep(5)
        print ("You start the ship and get ready to sail away")
        input(".")
        print ("A large thud can be heard on the deck")
        input(".")
        print ("Its Mr.X")
        input(".")
        print ("Jill and Chris start shooting at him and you see other ships in the distance you get on the cannon and prepare to defend")
        from random import randint

        board = []

        for x in range(6):
            board.append(["O"] * 6)

        def print_board(board):
            for row in board:
                print((" ").join(row))

        print("SINK THE SHIP!")
        print_board(board)

        def random_row(board):
            return randint(0, len(board) - 1)
        def random_col(board):
            return randint(0, len(board[0]) - 1)

        ship_row = random_row(board)
        ship_col = random_col(board)

        for turn in range(9):
            print ("Turn"), turn
            guess_row = int(input("Guess Row:"))
            guess_col = int(
                input("Guess Col:"))

            if guess_row == ship_row and guess_col == ship_col:
                print ("You sink the ship")
                break
            else:
                if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
                    print("Chris: At least try to hit the ship")
                elif(board[guess_row][guess_col] == "X"):
                    print("You guessed that one already.")
                else:
                    print("Miss")
                    board[guess_row][guess_col] = "X"
            if turn ==10:
                print("Game Over")
                Somalia()
            turn =+ 1
            print_board(board)
        print ("MR X ragdolls jill and throws her")
        time.sleep(3)
        print ("He punches Chris to the ground")
        File = open("Companion.txt", "r")
        Companion = File.read()
        if Companion == "Kavu ":
            print ("Kavu swoops down and grabs MR.X and throws him in the ocean")
            print ("Jill: What the fuck..")
            input(".")
            print ("Kavu flies down towards you and you jump on his back")
            input(".")
            print ("You fly to a town called LEIGH where disturbances have been recently")
            import Leigh
            s = "DeathToGods"
            save(s)
        else:
            print ("A wyvern knocks MR.X off the ship and you sail away quickly")
            time.sleep(5)
            print ("You sail and stop off in LEIGH as disturbances have been here recently")
            import Leigh
            s = "DeathToGods"
            save(s)



file=open("loadfile.txt","r")
room=file.read()
file.close()        

if room == "TheEvil":
    Somalia()