
import os,sys
import os.path
import Character as Character # Import character to access character types
import time
import Weapons as Weapons
from Weapons import Lightsaber, Sword


file = open("Kills.txt","w")
file.write("0")
file.close()
file = open("Gold.txt","w")
file.write("100")
file.close()
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

s ="TheDeserts"
save(s)
required = ("\nUse only A, B, or C\n") 


# Assign character objects to the name (a string)
char_types = {
    "mage": Character.mage,
    "thief": Character.thief,
    "gamer": Character.gamer,
    "prisoner":Character.prisoner,
    "vagabound":Character.vagabound,
    "warrior":Character.warrior,
    
}
 
def char_select():
    """
    Allows the player to choose the type of character they would like to be
    """
    #Pull in the list 'char_types'
    global char_types
    print("Please choose a character type\n")
    
    #Loop through the dictionary 'char_types' to list the character types and stats assigned to them
    for char in char_types:
        print(char.title()) #print the name of the character type in title case (Which capitalizes the first letter of each word in a line)
        # Just to make it look better, print a line of dashes
        print("------------------------------------------------------")
        # loop through the character type stats for printing
        for stat in char_types[char].stats.keys():
            #list the stats assigned to the character type
            print(stat, ":", char_types[char].stats[stat])
        
        # Seperate character types and their stats with an empty line
        print("\n")
 
    # Prompt the player to chose a character by entering its name
    Class = input("Please choose a character by typing its name\n")

    
 
    # Loop through char_types to check which character the player chose
    for char in char_types.keys():
 
        # If their choice is equal to the current key (Iteration 1 is "mage") then assign that character object to 'player'
        if Class.lower() == char:
            
            # Assign the character object to the variable 'player'
            player = char_types[char]
            
            # Allow them to give their character a name
            file=open("CharacterClass.txt","w")
            file.write(char)
            file.close()
            name = input("Please give your character a name\n")
            if name.lower() == "shadow man":
                print ("Shadow Man: There can only be one of me")
                name = input("Please give your character a name\n")

            
            # Confirm that they entered their desired name correctly
            conf = input(f"You entered {name}, is this correct? y/n \n")
            
            # If they are satisfied with the name they entered the first time, assign the name to the attribute 'name' of the character object (which is assigned to 'player' on line 40)
            if conf.lower() == 'y':
                player.name = name
                print(f"You are now {name} the {char}")
                file=open("CharacterName.txt","w")
                file.write(name)
                file.close()
                return player            
            
            # If they did not enter the name correctly, use a while loop to ask until they are satisfied with their entry
            while conf.lower() == 'n':
                name = input("Please give your character a name\n")
                if name.lower() == "shadow man":
                    print ("Shadow Man: There is only one true god of the realm")
                    name = input()
                conf = input(f"You entered {name}, is this correct? y/n \n")
                
                #If they are satisfied with the name they gave, assign the name to the attribute 'name' of the character object (which is assigned to 'player' on line 40)
                if conf.lower() == 'y':
                    player.name = name
                    print(f"You are now {name} the {char}")
                    file=open("CharacterName.txt","w")
                    file.write(name)
                    file.close()

                    # Return the complete player object

                    return player

 
            
# Assign the return of char_select() to the player variable
# Note: When assigning a function call to a variable, we are actually assigning the return of the function to the variable
player = char_select() 
 
# If there is no return from char_select() the player variable is set to None.
# So we use a while loop to keep prompting them to select a character until char_select() has a return value
while player == None:
    # Tell them that they didn't enter a listed character type or they had a typo
    print("!!!You did not enter a listed character name or had a typo, please try again!!!")
    
    # Give them 2 seconds to read the warning
    time.sleep(2)
    
    # Assign the return of char_select() to the player variable (which will call the function)
    player = char_select()



def Intro():
    file = open("CharacterStealth.txt","w")
    file.write(str(player.stealth))
    file.close()
    file = open("CharacterStrength.txt","w")
    file.write(str(player.strength))
    file.close()
    file = open("CharacterHealth.txt","w")
    file.write(str(player.health))
    file.close()
    file = open("CharacterSpeed.txt","w")
    file.write(str(player.speed))
    file.close()
    file = open("CharacterIntelligence.txt","w")
    file.write(str(player.intelligence))
    file.close()
    file = open("CharacterCharisma.txt","w")
    file.write(str(player.charisma))
    file.close()
    file = open("CharacterStealth.txt","w")
    file.write(str(player.stealth))
    file.close()
    file = open("CharacterMana.txt","w")
    file.write(str(player.mana))
    file.close()
    print ("Chapter 0: The Deserts")
    time.sleep(3)
    print ("You wake up in the Deserts Of Afghanistan")
    time.sleep(2)
    print ("You always find yourself here and you want to know why")
    time.sleep(4)
    print ("You go south instead of north or west and find...")
    time.sleep(4)
    print ("Remains Of A Temple")
    Temple()


def Temple():
    print ("You enter the temple")
    time.sleep(2)
    print ("You find a sword and grab hold of it")
    time.sleep(2)
    print ("You find the rock here")
    print ("Type SKIP if you wish to SKIP Dialogue")
    print ("Anything else to continue")
    choice = input()
    if choice.lower() == "skip":
        Truth()
    else:
        print ("Rock: So you have returned")
        time.sleep(3)
        print ("Rock: and i am the first person you meet again")
        time.sleep(4)
        print ("Rock: He has really planned this out hasnt he... The Shadow Man")
        time.sleep(4)
        print ("Rock: He knew where he wanted everyone to be to give him the upper hand")
        time.sleep(4)
        print ("Rock: He is trying to desert us all, he wants to become the destroyer of worlds")
        time.sleep(5)
        print ("Rock: You are free of the narrator now you can explore on your own. There is a lot to uncover")
        time.sleep(5)
        print ("Rock: Follow me i need to show you something")
        Truth()

def Truth():
    print ("The Rock leads you to a room full of statues")
    time.sleep(3)
    print ("Rock: The painting on this wall shows the god's foundry were the gods was made")
    time.sleep(5)
    print ("Rock: Shadow Man was forged on 'The First Dark Night' which they say was a curse")
    time.sleep(4)
    print ("Rock: They mistreated him for it thinking he was a curse")
    time.sleep(3)
    print ("Rock: But really he had been gifted more power")
    time.sleep(5)
    print ("Rock: As his power grew so did his ambition but he wanted to protect the world")
    time.sleep(6)
    print ("Rock: Shadow Man was furious and slaughtered three of the gods")
    time.sleep(4)
    print ("Rock: They banished him and he became one with his evil intentions and forever casted as a shadow hence his new name")
    time.sleep(6)
    print ("Rock: He created a realm of his own that he would use to cause destroy the world in which he so did")
    time.sleep(6)
    print("Rock: But we have somehow become alive again they used the power of other universes to forge what people are calling the NEW WORLD")
    time.sleep(7)
    print ("Rock: We all have big challenges ahead of us")
    ShadowManSeeks()

def ShadowManSeeks():
    time.sleep(5)
    print ("Shadow Man: Hello again")
    time.sleep(3)
    file = open("CharacterName.txt","r")
    Name = file.read()
    print ("Shadow Man:", Name ,  "You are a very powerful entity")
    time.sleep(4)
    print ("Shadow Man: However i will not use this to convince you to join me thats your decision")
    time.sleep(5)
    print ("Shadow Man: Before the biggest bang hit i merged our bodies to keep you alive ")
    time.sleep(6)
    print ("Shadow Man: You have a percentage of my power and what decisions you make will dictate the fate of you,people and the universe")
    time.sleep(6)
    print ("Shadow Man: Just thought i woudld let you know")
    print ("Shadow Man teleports away")
    time.sleep(5)
    print ("Rock: What was that all about?")
    time.sleep(4)
    print ("The temple begins to fall")
    time.sleep(3)
    print ("You both run out and see Shadow Man destroying the temple and sending it deep underground")
    time.sleep(5)
    print ("Shadow Man: There are more wars to come")
    print ("Rock: We should stick together for now")
    Desert()




def Desert():
    Character.equipped = Sword
 #map
    dungeonMap = [["0","0","0","0","0","0","0","0","0"],
                  ["0",".",".",".",".",".","D",".","0"],
                  ["0",".",".",".",".",".",".",".","0"],
                  ["S",".",".",".",".",".",".",".","0"],
                  ["0","T",".",".",".",".",".","E","0"],
                  ["0",".",".",".",".",".",".",".","0"],
                  ["0",".",".",".","V",".",".",".","0"],
                  ["0","0","0","0","0","0","0","0","0"]]

    playerMap  = [[".",".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".","D",".","."],
                  [".",".",".",".",".",".",".",".","."],
                  ["S",".",".",".",".",".",".",".","."],
                  [".","T",".",".",".",".",".","E","."],
                  [".",".",".",".",".",".",".",".","."],
                  [".",".",".",".","V",".",".",".","."],
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
                print("thats a landmine field lets not go through that again shall we")
                x = previousX
                y = previousY
                position = mapChoice[y][x]

            if Steps == 5:
                print ("You can hear a wooshing noise in the sky..")
                time.sleep(4)
                print ("Rock: Its Sauron, it meaans he is back to full strength from his rebirth")
                time.sleep(3)
                print ("Soon we will hear the cries of war as he rains it down on us all")

            if position == ".":
                print("This area is clear")

            if position == "T":
                print ("You are back at the ruined temple")
                print ("You look down the hole where the temple was sunk and you can see nothing")
                
                


            if position == "V":
                if Vader == True:
                    print ("You can see the damage that remains from the fight blood splattered all over the sand and rocks.")
                else:
                    print ("You can see a fiugre in the distance")
                    time.sleep(3)
                    print ("You approach it")
                    time.sleep(2)
                    print ("The rock gets the figures attention...")
                    time.sleep(2)
                    print ("Its Darth Vader he sends you flying into a tree and strangles the rock with the force")
                    time.sleep(4)
                    print ("Vader: You do not know the pain i have had to endure")
                    time.sleep(4)
                    print ("Vader: I was crushed by some dark lord called Sauron")
                    time.sleep(4)
                    print ("Vader: Some creature thats face opened up tried to eat me and then")
                    time.sleep(4)
                    print ("Vader: This giant god with one eye in its chest crushed my head")
                    time.sleep(5)
                    print ("Vader: I could still feel it when i awoke")
                    time.sleep(3)
                    print ("Vader: My son died and if i returned then so will he")
                    time.sleep(3)
                    print ("Vader: I will make you all pay for this")
                    time.sleep(2)
                    print ("Vader lets go off the rock")
                    time.sleep(3)
                    print ("Shadow Man: So much suffering Vader")
                    time.sleep(2)
                    print ("Vader: You..")
                    time.sleep(2)
                    print ("Shadow Man: Memory coming back to you")
                    time.sleep(2)
                    print ("Vader: I thought you was one with the Shadows how are you out in a desert in the day?")
                    time.sleep(4)
                    print ("Shadow Man: I am not with one of the shadows i am the shadows. all of them")
                    time.sleep(3)
                    print ("Shadow Man: Winning makes you stronger Vader. You should know")
                    time.sleep(3)
                    print ("Vader: What do you want?")
                    time.sleep(2)
                    print ("Shadow Man: Destruction")
                    print ("Shadow Man creates a spike from out of the ground that stabs Vader")
                    time.sleep(4)
                    print ("Vader bleeds heavily but throws his lightsaber at Shadow Man cutting his arm off he brings it back to him with the force to cut the spike releasing him")
                    time.sleep(7)
                    print ("Shadow Man forms a Shadow of Luke and sends it to fight him")
                    time.sleep(5)
                    print ("With Vader distracted he creates a dagger and uses it to stab Vader 11 times in the stomach")
                    time.sleep(7)
                    print ("Shadow Man: You do fight well")
                    time.sleep(4)
                    print ("Shadow Man: I am going to send you home now but i do not doubt we will meet again")
                    time.sleep(5)
                    print ("Shadow Man sends Vader through a portal and makes one for himself")
                    time.sleep(3)
                    print ("on the ground is a lightsaber, you pick it up and ignite it to see the red glow.")
                    Character.equipped = Lightsaber
                    Vader = True


                    

                    
                position = mapChoice[y][x]


            if position == "D":
                if ShadowMan == True:
                    print ("You find a entrance to a dungeon")
                    if Character.equipped == Lightsaber:
                        print ("You use the lightsaber to light your way down a flight of stairs")
                    else:
                        print ("A torch on the wall lights itself you take it to light your way")
                    print ("You reach a door.") 
                    if Character.equipped == Lightsaber:
                        print ("You use your lightsaber to carve an opening in")
                        time.sleep(4)
                        print ("You enter a chamber and can see souls rising up and fading away")
                        time.sleep(3)
                        print ("Shadow Man is here observing too")
                        time.sleep(2)
                        print ("Shadow Man: This is how they are resurrecting them")
                        time.sleep(2)
                        print ("Shadow Man: This is how we all was reborn to be in this world")
                        time.sleep(3)
                        print ("Shadow Man: Maybe i could take a few souls to the Shadow Realm")
                        time.sleep(4)
                        print ("I am going to need the strength to fight the gods again")
                        time.sleep(3)
                        print ("Shadow Man begins to manifest his power to consume the souls")
                        time.sleep(2)
                        print ("The souls make their way into Shadow Man and you watch as he starts to levitate in the air as he grows more powerful")
                        time.sleep(6)
                        print ("The roof of the dungeon explodes exposing the outerworld and the floor beneath you breaks in")
                        time.sleep(5)
                        print ("You splash into water")
                        print ("Shadow Man: More to explore...")
                        time.sleep(5)
                        print ("There is a star in the water and Shadow Man grabs it")
                        time.sleep(4)
                        print ("A portal opens and outsteps Observation Man")
                        time.sleep(4)
                        print ("He lasers Shadow Man into the ground and looks over him")
                        time.sleep(3)
                        print ("Shadow Man: You have grew in strength.")
                        time.sleep(2)
                        print ("All-Knowing: We have been reforged into more powerful beings absorbing all energy from the biggest bang")
                        time.sleep(4)
                        print ("Shadow Man: That isnt gonna stop me from murdering you all")
                        time.sleep(4)
                        print ("All-Knowing: That Star contains a unlimited amount of well.. everything")
                        time.sleep(3)
                        print ("All-Knowing: Its the last fragment of the foundry of gods")
                        time.sleep(4)
                        print ("Shadow Man: Im guessing you want it..")
                        time.sleep(2)
                        print ("All-Knowing: Yes")
                        time.sleep(1)
                        print ("Shadow Man: Thats a shame")
                        time.sleep(3)
                        print ("Shadow Man destroys a wall releasing a hydra")
                        time.sleep(3)
                        print ("All-Knowing: Kavu, Ruler of the Underworld")
                        print ("Shadow Man sends himself and All-Knowing and Observation Man down to the shadow realm to fight leaving you with Kavu")
                        time.sleep(7)
                        KavuHP = 10,000
                        HP = player.health * 10
                        print ("You can take the option to A) RUN or B)FIGHT this god, what do you do?")
                        try:
                            Flag = True
                            while Flag == True:
                                Option = input()
                                if Option in answer_A:
                                    print ("You run up the stairs as quickly as you can go, Kavu chases and darts a head towards you")
                                    time.sleep(6)
                                    print ("You swing your lightsaber leaving a menacing mark across the front of his face, you get the death stare treatment before he flies off out of the hole in the dungeon roof.")
                                    time.sleep(8)
                                    print ("You have escaped the dungeon and as you move as far away as possible it explodes sending a barrage of debris everywhere")
                                    Flag = False
                                    ShadowMan = False
                                    position = mapChoice[y][x]
                                if Option in answer_B:
                                    print ("You are about to fight a god")
                                    while KavuHP > 0:
                                        print ("KAVU:,",KavuHP)
                                        print ("HP:",HP)
                                        print ("A: Fight B: Dodge")
                                        Option = input(">>")
                                        if Option in answer_A:
                                            print ("You go to attack Kavu and one of his heads grabs the lightsaber bout of your hand while two more heads clamp their jaws around your lower body")
                                            time.sleep(9)
                                            print ("The rest of the heads start to eat away at you")
                                            time.sleep(4)
                                            print ("YOU DIED")
                                            Desert()
                                        if Option in answer_B:
                                            print ("You roll out the way")
                                        else:
                                            print ("You do nothing and get juggled around in Kavus mouths")
                                            print ("YOU DIED")
                                            Desert()
                        except:
                            print ("A or B.")
                    else:
                            print ("You need something to get through the door")        
                                
                    
                    position = mapChoice[y][x]
                else:
                    print ("You look at the damage left from the exploded dungeon. The ruler of the underworld is now in the overworld.")
            position = mapChoice[y][x]


            

            
        if Character.equipped == Sword:
            print ("You find a Lightsaber in the sand and pick it up")
            Character.equipped = Lightsaber
        print("You make your way out of the desert and are now walking along a river")
        time.sleep(2)
        print ("Shadow Man appears next to a tree")
        time.sleep(2)
        print ("The Rock: What is your problem? Why are you following us?")
        time.sleep(3)
        print ("Shadow Man: I am just preparing for the slaughter of this world")
        time.sleep(3)
        print ("Shadow Man: I am going to slaughter all the gods and everyone who gets in my way")
        time.sleep(6)
        print ("Shadow Man: Everyone has been freed.. I am going to kill them all")
        time.sleep(5)
        print ("Shadow Man: The war will now begin.")
        time.sleep(4)
        print ("Shadow Man: I know you dont want to join me.. so just dont get in my way")
        time.sleep(3)
        print ("Iron Man lands and starts to shoot at Shadow Man")
        time.sleep(4)
        print ("You run to get out of the trouble but end up finding yourself back at the crater where the temple was")
        time.sleep(6)
        print ("You realise something...")
        time.sleep(3)
        print ("This is the way to the SHADOWREALM")
        time.sleep(3)
        print ("Shadow Man grabs The Rock and throws him down the SHADOWREALM")
        time.sleep(3)
        print ("Shadow Man: It is time to bring the SHADOW REALM to the surface. This will mean everyone will be freed into this world. THIS MEANS WAR!")
        time.sleep(5)
        print ("A odd looking creature appears from the shadow realm")
        time.sleep(2)
        print ("Shadow Man: We call this a bum licker honestly i dont know where it came from but expect to see a lot of them")
        time.sleep(5)
        print ("Shadow Man drains the life out of the bum licker killing it")
        time.sleep(4)
        print ("Shadow Man: I plan on taking this desert meaning you are gonna have to depart.")
        print ("Shadow Man: I am going to send you through a portal")
        time.sleep(7)
        print ("You go through the portal and end up in a town called Dawnmire")
        if player.char_type == "mage":
            from Mage import ShadowsOfEvil
        if player.char_type == "thief":
            from Thief import ShadowsOfEvil
        if player.char_type == "prisoner":
            from Prisoner import ShadowsOfEvil
        if player.char_type == "gamer":
            from Gamer import ShadowsOfEvil
        if player.char_type == "vagabound":
            from Vagabound import ShadowsOfEvil
        if player.char_type == "warrior":
            from Warrior  import ShadowsOfEvil

        

        
            


            
    main(mapChoice, playerMap, position) 









Intro()
