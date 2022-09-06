import os,sys
import os.path
import Character as Character# Import character to access character types
import time
import Weapons as Weapons
from Weapons import Lightsaber, Sword
import random
player = Character.gamer

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
DUEL = ["D", "d"]
yes = ["Y", "y", "yes"] 
no = ["N", "n", "no"]
def Main():
    print ("A: Go to Tavern")
    print ("B: Go to Shops")
    file = open("loadfile.txt")
    Quest = file.read()
    if Quest == "ShadowsOfEvil":
        print ("C: Go to Castle Gates")
    Choice = input(">>")
    if Choice in answer_A:
        Tavern()
    if Choice in answer_B:
        Shop()
    if Choice in answer_C:
        Dawnmire()


def Tavern():
    Drinks = 0
    print ("You enter the Tavern")
    Drown = random.randint(1,20)
    if Drown < 16:
        print ("You go to the Tavern Keeper and ask for a beer")
        time.sleep(3)
        print ("You get the beer and chug it down")
        Drinks = Drinks + 1
        print ("Tavern Keeper: Want more.")
        Drink = input("Y/N")
        while Drink in yes:
            print ("You get the beer and chug it down")
            Drinks = Drinks + 1
            print ("Tavern Keeper: Want more.")
            Drink = input("Y/N")
            if Drinks == 5:
                print ("The beers have made you more aggressive.")
                time.sleep(4)
                print ("Do you fight the nearest citizen")
                choice = input("Y/N")
                if choice in yes:
                    print ("You attack the nearest citizen and splatter his face on the walls")
                    time.sleep(6)
                    print ("You get thrown out of the tavern")
                    Main()
                if choice in no:
                    print ("You get another drink down")
                    Drinks = Drinks + 1
                else:
                    print ("You throw up everywhere and black out")
                    Main()
            if Drinks == 10:
                print ("You end up getting too drunk and black out")
                Main()
        Main()
        
    else:
        print ("A drunk man approaches you and challenges you to a fight")
        Scenario = random.randint(1,5)
        if Scenario == 1:
            print ("You enter a fist fight with the drunk man and send him flying out a window")
            Main()
        if Scenario == 2:
            print ("He goes to stab you but you dodge and easily trip him over. You drag him out with ease")
            Main()
        if Scenario == 3:
            print ("You enter a bloody fight with glasses and weapons being used. You both get thrown out the tavern and the drunken dies of blood loss")
            Main()
        if Scenario == 4:
            print ("Eventhough he is drunk he is still larger than you and chokes the life out of you")
            time.sleep(3)
            print ("YOU DIED")
            import Save
        if Scenario == 5:
            print ("He beats you to a brutal end, you survive and the drunken gets arrested")
            Main()

def Shop():
    print ("You head over to the stalls in the shopping centre")
    time.sleep(3)
    print ("A siren alarms and ballista bolts fire to the clouds")
    time.sleep(4)
    print ("You hear civilian panic and overhear someone say Kavu has been freed")
    time.sleep(4)
    print ("You can see the dark figure in the distance of Kavu")
    time.sleep(3)
    print ("Kavu dives down and goes straight through the ground")
    time.sleep(3)
    print ("His heads come up and start to eat people and destroy the stalls")
    time.sleep(5)
    print ("He looks at you before vanishing")
    Dawnmire()



def Dawnmire():
    print ("You head towards the castle gates and the solider accompanies you in")
    time.sleep(3)
    print ("Soldier: Majesty, i bring a reborn to you")
    time.sleep(2)
    print ("The king stands in full armour and turns around to face you")
    time.sleep(3)
    print ("King of Dawnmire: Soldier, do you not understand. KAVU has been released")
    time.sleep(3)
    print ("Soldier: and this is why i bring you the reborn he could get us to safety")
    time.sleep(4)
    print ("Shadow Man: There is no safety")
    time.sleep(3)
    print ("Shadow Man: Only war")
    time.sleep(2)
    print ("Soldier: Let us go to another world instead of your hellish world")
    time.sleep(3)
    print ("Shadow Man: You are all misunderstood. I didnt create this world its just been hidden for the safety of ALL")
    time.sleep(5)
    print ("Shadow Man: I did not singlehandedly make this world. All of us did. Every god")
    time.sleep(5)
    print ("Shadow Man: Now i am going to finish my ambition. You will be released but into a war. A war in which this world will win")
    time.sleep(4)
    print ("Shadow Man: I will get to rule over the universes so that this very world can become safe and peaceful")
    time.sleep(3)
    print ("Soldier: But what about Kavu and all the other things that we have to coexist with")
    time.sleep(4)
    print ("Shadow Man: Only time can tell what happens to your lives")
    time.sleep(3)
    print ("Shadow Man: Now..")
    time.sleep(2)
    print ("Shadow Man: Think of our world as if it was on shackles.")
    time.sleep(2)
    print ("Shadow Man: We are stuck unable to move. limited in our actions")
    time.sleep(2)
    print ("Shadow Man: Unless we destroy the shackles")
    time.sleep(2)
    print ("Shadow Man: Now i have found a way to destroy the shackles and free us")
    print ("Shadow Man holds up a star. The star in which the whole universe was contained")
    time.sleep(7)
    print ("Shadow Man: See soldiers. I was just like you. I was just trying to find a way out but not to escape but to free.")
    time.sleep(4)
    print ("Soldier: You are going to free us by opening us up to every threat in the universe?")
    time.sleep(5)
    print ("Shadow Man: Yes and there is nothing you can do about that")
    time.sleep(5)
    print ("Shadow Man begins to consume the star. Cracks begin forming in the star")
    time.sleep(4)
    print ("The soldier goes to stop him but the king kills him")
    time.sleep(3)
    print ("The floor beneath you rises as Shadow Man does")
    time.sleep(5)
    print ("Shadow Man: I need another sacrifice")
    print ("You look at the king and he looks back. You both know whats about to go down")
    time.sleep(6)
    TheKing()

def TheKing():
    Broken = False
    global HP
    global player
    HP = player.health * 100
    print ("You can see the multiple different universes and worlds in the sky")
    time.sleep(3)
    print ("But one man stands in your way..")
    KingShield = 100
    KingHealth = 10000
    print ("King HP:", KingHealth, (KingShield))
    print ("HP:", HP)
    while KingHealth > 1:
        print ("A: Lightsaber Slash")
        print ("B: Lightsaber throw")
        choice = input(">>")
        if choice in answer_A:
            print ("You two hand your lightsaber and slash down at the king of dawnmire")
            if KingShield > 1:
                Slash = 50
                KingShield = KingShield - Slash
                print ("{",Slash,"}")
            else:
                Slash = random.randint(1000,6000)
                KingHealth = KingHealth - Slash
                print ("{",Slash,"}")
        if choice in answer_B:
            print ("You throw your lightsaber at the king of dawnmire but you dont have the force to bring it back to you so you quickly roll and grab your saber")
            if KingShield > 1:
                Throw = 100
                KingShield = KingShield - Throw
                print ("{",Throw,"}")
            else:
                Throw = random.randint(4000,5000)
                KingHealth = KingHealth - Throw
                print ("{",Throw,"}")
        else:
            print ("You do nothing for this turn")
        if Broken == False:
            if KingShield <= 0:
                print ("You destroy the orange shield surrounding the king as it explodes it shreds his armour exposing him to be a old man but with the strength of an ox")
                time.sleep(5)
                Broken = True    
        Attack = random.randint(20,100)
        print ("The king swings his greatsword towards you")
        time.sleep(2)
        print ('{',Attack,'}')
        HP = HP - Attack
        if HP < 0:
            print ("YOU DIED")
            time.sleep(3)
            TheKing()
    print ("You strike your lightsaber through the kings chest")
    time.sleep(3)
    print ("King of Dawnmire: You have earned my respect reborn")
    time.sleep(3)
    print ("King of Dawnmire: Safe travels")
    print ("The king lies on the floor and lets out his last breath")
    time.sleep(4)
    print ("Shadow Man: I knew you would come out on top")
    time.sleep(3)
    print ("Shadow Man: Now i can reach my maximu power")
    print ("The star explodes burning the sky so that space was visible to all, meteor showers and shooting stars begin to hit the world")
    time.sleep(6)
    print ("Shadow Man: and so it begins, hopefully Kavu and the rest of this destruction kills them arrogant gods before i have to")
    time.sleep(6)
    print ("Shadow Man: Now i have reached my maximum power..")
    time.sleep(4)
    print ("Shadow Man: But what about my unforeseen maximum potential?")
    time.sleep(3)
    print ("Blood from the battles begins to be picked up by a force")
    time.sleep(4)
    print ("The force of Shadow Man")
    print ("He absorbs a drop of blood from everything in this world which is enough to reach his potential")
    time.sleep(5)
    print ("Shadow Man: With the sacrifices i can become whole again. a physical human not just a shadow")
    time.sleep(4)
    print ("Shadow Man: But with the blood of an entire world i can become THE UNSTOPPABLE")
    time.sleep(4)
    print ("With the connection to the shadow realm and the new world now complete. Shadow Man can now reach his TRUE FORM")
    time.sleep(7)
    print ("Shadoni, THE EATER OF WORLDS, THE DESTROYER OF LIFE")
    THEEND()

def THEEND():
    print ("Now that SHADOW MAN can reach his FINAL FORM. ALL LIFE looks in fear")
    time.sleep(4)
    print ("SHADOW MAN: It is no safe you being here. I will send you back to earth")
    time.sleep(3)
    print ("SHADOW MAN: I hope to see you soon")
    time.sleep(3)
    print ("SHADOW MAN: Now we must say our goodbyes")
    time.sleep(2)
    print ("SHADOW MAN: We will meet again i know it")
    time.sleep(2)
    print ("Shadow Man disappears and a dark cloud forms around you")
    time.sleep(3)
    print ("As the dark cloud fades you find yourself in London back on EARTH")
    time.sleep(3)
    print ("You encounter Doctor Strange who approaches you")
    time.sleep(3)
    print ("Doctor Strange: Who are you?")
    file = open("CharacterName.txt","r")
    Name = file.read()
    time.sleep(1)
    print (Name ,":", Name)
    time.sleep(2)
    print ("Doctor Strange: Well", Name, "Your arrival through a shadow portal does not show a good sign")
    time.sleep(5)
    print ("Doctor Strange: He has broke the barrier hasnt he?")
    time.sleep(2)
    print ("A hydra can be seen hovering in the sky")
    time.sleep(2)
    print ("Its KAVU")
    time.sleep(2)
    print ("Civillians begins to panic and run and Doctor Strange takes you to the Sanctum")
    time.sleep(3)
    print ("You can see KAVU in the window. Three rifts open and three wyverns appear from them")
    time.sleep(4)
    print ("They surrond Kavu and attack him from all angles")
    time.sleep(3)
    print ("They bite and scratch at him")
    time.sleep(2)
    print ("A lightning wyvern opens its mouth to let out a lightning bolt before Kavu sticks its tail down its mouth going straight through the head")
    time.sleep(9)
    print ("Kavu grabs the fire wyvern and sticks its claws down its mouth")
    time.sleep(4)
    print ("The fire wyvern fires a flame from its mouth burning the hand of Kavu")
    time.sleep(5)
    print ("Kavu wraps its tail tightly around the throat of the fire wyvern and wrestles the poison wyvern")
    time.sleep(5)
    print ("Kavu breaks the jaw of the poison wyvern then decapites the wyvern with its claws")
    time.sleep(5)
    print ("Kavu still strangling the fire wyvern to death crushes its throat and then releases it watching it fall flat into the ground.. dead")
    time.sleep(6)
    print ("Doctor Strange: That is some creature they have been hiding. outnumbered and winning that easily")
    time.sleep(4)
    print ("Doctor Strange: Some monster hunter from another realm will probably go hunt for it.")
    time.sleep(4)
    print ("You watch as Kavu eats away at the fire wyvern after a successful first battle on earth. A possible new world for it to conquer.")
    if player.char_type == "mage":
        from Mage import Fallen
    if player.char_type == "thief":
        from Thief import Fallen
    if player.char_type == "prisoner":
        from Prisoner import Fallen
    if player.char_type == "gamer":
        from Gamer import Fallen
    if player.char_type == "vagabound":
        from Vagabound import Fallen
    if player.char_type == "warrior":
        from Warrior  import Fallen 


Main()





