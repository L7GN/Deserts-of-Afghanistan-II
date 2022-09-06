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


def Leigh():
    print ("You are geared up again and ready for your next challenge")
    input(".")
    print ("Chapter 2.1: DEATH TO THE GODS")
    time.sleep(5)
    print ("You are walking the streets with Jill and Chris and come across a corpse in the street")
    input(".")
    print ("It looks like the corpse of Osiris")
    print ("Jill: This guy's spine got ripped out")
    print ("Chris: Whatever did this is not one to be fucked with")
    input(".")
    print ("You look at the corpses of a spineless Moonknight and a rotting osiris and then you hear a noise")
    input(".")
    print ("You see R2D2 and approach him")
    input(".")
    print ("You apprach R2D2 and the noise gets louder and louder")
    input(".")
    print ("He explodes and you fly over a car ")
    input(".")
    print ("Osama Bin Laden starts shooting at you")
    input(".")
    print ("Jill shoots him in the shoulder and he backs up to a fence")
    input(".")
    print ("A zombie grabs him and rips his throat out, another grabs his arm and starts peeling layers off his skin off with its teeth")
    input(".")
    print ("He screams as more zombies approach and reach with their hand into his chest for his guts")
    input(".")
    print ("He reaches with his other hand slowly for a detonater")
    input(".")
    print ("Bin Laden: ALLAH AKBAR")
    print ("He suicide bombs himself")
    input(".")
    print ("This leaves a hole in the fence which zombies climb through")
    input(".")
    print ("The three of you run")
    input(".")
    print ("Jill gets shot in the stomach and you see a cowboy with a revolver on a roof")
    input(".")
    print ("Jill: Leave me")
    print ("You watch as Jill lays on the ground with zombies approaching her")
    input(".")
    print ("You run into a building with Chris")
    print ("Chris: Whoever that fucker is. i am gonna kill him")
    time.sleep(6)
    print ("Chris: Do something with your time while i murder this son of a bitch")
    input(".")
    print ("You sneak round the streets trying to find who was responsible")
    input(".")
    print ("ALL-KNOWING: Still going..")
    input(".")
    print ("ALL-KNOWING appears behind you")
    input(".")
    print ("ALL-KNOWING: Andy was responsible for killing Osiris. He was against MR TIMES plan")
    input(".")
    print ("ALL-KNOWING: MR TIME froze him in time and accelerated time to leave him behind")
    input(".")
    print ("ALL-KNOWING: We do not know if or when he will escape")
    input(".")
    print ("ALL-KNOWING: But he has made his motive to destroy all life very clear")
    input(".")
    print ("ALL-KNOWING: I must go")
    print ("ALL-KNOWING disappears")
    input(".")
    print ("You hear rumbling and head towards it")
    input(".")
    print ("Shadow Man can be seen wrestling with Ra")
    print ("Shadow Man: Ra, God of the Sun")
    input(".")
    print ("Shadow Man: On this day let it be known that i faced the light and will emerge victorious")
    input(".")
    print ("Shadow Man takes many forms to attack RA")
    input(".")
    print ("RA forces the sun to emerge suddenly making it day")
    input(".")
    print ("RA absorbs the power of the sun while Shadow Man grows weaker in the light")
    input(".")
    print ("RA forces solar beams from the sun down onto Shadow Man almost destroying him")
    input(".")
    print ("The dark aura of Shadow Man starts to glow red from the burning flame of the sun")
    input(".")
    print ("RA raises the intensity  of the sun and he still stands")
    input(".")
    print ("RA uses all the suns power on Shadow Man making the whole Earth burn")
    input(".")
    print ("The shadow begins to melt off Shadow Man")
    input(".")
    print ("Andy arrives and tackles RA into a wall")
    input(".")
    print ("RA stabs Andy with his spear before teleporting away")
    input(".")
    print ("Shadow Man melts to a liquid")
    input(".")
    print ("Chapter 2.1.2: Chris Redfield")
    print ("Chris: Where are you?")
    input(".")
    print ("You are on the rooftops looking to find the cowboy who shot Jill")
    input(".")
    print ("You find mccree")
    input(".")
    print ("Chris: Freeze!")
    input(".")
    print ("Mccree: I mean no harm")
    input(".")
    print ("Chris: Why shoot her?")
    input(".")
    print ("Mccree: I needed bait")
    time.sleep(5)
    print ("Mccree turns around")
    time.sleep(1)
    print ("You shoot Mccree's face off with a shotgun")
    time.sleep(4)
    print ("His body falls off the roof and zombies walk towards the corpse to eat it")
    input(".")
    print ("Chris: Stupid fucker")
    input(".")
    print ("LAKAKA jumps down")
    print ("Chris: What the fuck are you?")
    input(".")
    print ("You shoot at LAKAKA and the bullets bounce off him")
    input(".")
    print ("Lakaka grabs you with his hands and squeezes your head")
    input(".")
    print ("Chris screams and his head is crushed")
    input(".")
    print ("LAKAKA jumps off the roof and storms away")
    input(".")
    print ("Chapter 2.1.3: Sewers | Jill Valentine")
    print ("You wake up in the sewers that you narrowly escaped from")
    input(".")
    print ("You see 3 survivors down in the sewers also")
    print ("Leon Kennedy, Clare Redfield and Ada Wong")
    input(".")
    print ("Your introduction is cut short bu a demogorgan storming through")
    input(".")
    print ("A licker jumps at the demogorgan and they fight")
    input(".")
    print ("The demogorgan rips out the brain of the licker and claws at its guts")
    input(".")
    print ("Claire shoots fire rounds out a grenade launcher at the Demogorgan")
    input(".")
    print ("The demogorgan burns to death")
    input(".")
    print ("LAKAKA punches through a wall in the sewer and drags the headless body of Chris Redfield along the floor")
    print ("Claire: Chris!")
    input(".")
    print ("Jill: You three go i will avenge your brother, Claire")
    input(".")
    JillV = 1000
    Lakaka = 10000
    while JillV >= 0:
        print ("Jill:", JillV)
        print ("Lakaka:", Lakaka)
        print ("A: Shoot")
        choice = input(">>")
        if choice in answer_A:
            print ("You shoot Lakaka")
            time.sleep(4)
            print ("Bullets bounce off lakaka")
        print ("LAKAKA punches you")
        Attack = random.randint(250,500)
        JillV = JillV - Attack
    print ("LAKAKA grabs you and goes to bite you but Jill jams a frag grenade down his throat and runs")
    input(".")
    print ("It explodes leaving a massive hole in lakaka's stomach")
    input(".")
    print ("Chapter 2.1: Finale")
    print ("Shadow Man reforms himself")
    input(".")
    print ("Shadow Man: I cannot be truly defeated")
    input(".")
    print ("Shadow Man approaches you")
    input(".")
    print ("Shadow Man: Great to see you again")
    input(".")
    print ("A hammer is thrown at Shadow Man. its THOR")
    input(".")
    print ("Jill arrives")
    input(".")
    print ("Jill: Quick we need to go. This town is getting destoyed")
    input(".")
    print ("Shadow Man: Fine.. then Thor. Wanna play like that")
    print ("Shadow Man: You need to head to New York")
    input(".")
    print ("Shadow Man: I want to feel the might of all gods")
    ShadowShield = 1000
    ShadowMan = 100000  
    Shield = True
    Darkness = False
    Thor = 10000
    while Thor >= 0:
        print ("Shadow Man:", ShadowMan)
        print ("Thor:", Thor)
        print ("A: Shadow Strike")
        print ("B: Shadow Ball")
        print ("C: Strength of Shadows")
        choice = input(">>")
        if choice in answer_A:
            print ("You send a shadow clone to charge at Thor")
            Attack = random.randint(500,2000)
            print ("{",Attack,"}")
            Thor = Thor - Attack
        if choice in answer_B:
            print("You send a Shadow Ball at Thor")
            Attack = random.randint(50,200)
            print ("{",Attack,"}") 
            Thor = Thor - Attack
        if choice in answer_C:
            print ("You show Thor the strength of the shadow realm and you stomp, punch and throw him into walls")
            Attack = random.randint(5000,7000)
            print ("{",Attack,"}")
            Thor = Thor - Attack
        print ("Thor unleashes a thunder bolt at you")
        Attack = random.randint(500,1000)
        print ("{",Attack,"}")
        if Shield == True:
            ShadowShield = ShadowShield - Attack
        else:
            ShadowMan = ShadowMan - Attack
    
    print ("Thor throws his hammer and you teleport behind him")
    ShadowMan = ShadowMan - 100
    print ("(A!)")
    Fight = input(">")
    if Fight in answer_A:
        print ("You slam Thor into the ground and begin to choke him")
    else:
        print ("Thor hits you with his hammer but you counter with a uppercut and tackle him to the floor and begin to strangle him")
        ShadowMan = ShadowMan - 50
    time.sleep(7)
    print ("(A!)")
    Fight = input(">")
    if Fight in answer_A:
        print ("You punch him with your right hand")
    else:
        print ("You go to punch but miss")
    print ("B!")
    Fight = input(">")
    if Fight in answer_B:
        print ("You punch him with your left hand")
    else:
        print ("You go to punch but miss")
    print ("(A!)")
    Fight = input(">")
    if Fight in answer_A:
        print ("You punch him with your right hand")
    else:
        print ("You go to punch but miss")
    print ("B!")
    Fight = input(">")
    if Fight in answer_B:
        print ("You punch him with your left hand")
    else:
        print ("You go to punch but miss")
    print ("Thor begins to cough up blood")
    print ("(A!)")
    Fight = input(">")
    if Fight in answer_A:
        print ("You punch him with your right hand")
    else:
        print ("You miss but manage to create a sword in your hand and stab him in the chest")
    print ("B!")
    Fight = input(">")
    print ("Thor has been brought to the brink of death")
    time.sleep(4)
    print ("You see Poseidon approaching")
    print ("Shadow Man: Poseidon...")
    time.sleep(4)
    print ("You send thor to the shadow realm and run towards Poseidon")
    time.sleep(5)
    Gods()

def Gods():
    print ("He throws his trident at you impaling you in a wall")
    print ("(B!)")
    Fight = input(">>")
    if Fight in answer_B:
        print ("You teleport behind Poseidion but he punches you to the ground and drags you across the floor")
    else:
        print ("You stay there and die")
        Gods()
    print ("Poseidon: You are no chosen one Shadow Man")
    Poseidon = 100000
    ShadowMan = 100000
    God = False
    while Poseidon >= 0:
        print ("Poseidon:", Poseidon)
        print ("Shadow Man:", ShadowMan)
        print ("A: Shadow Strike")
        print ("B: Shadow Ball")
        print ("C: Strength of Shadows")
        print ("D: REACH TRUE POTENTIAL")
        choice = input(">>")
        if choice in answer_A:
            print ("You send a shadow clone to charge at Poseidon")
            Attack = random.randint(500,2000)
            print ("{",Attack,"}")
            Poseidon = Poseidon - Attack
        if choice in answer_B:
            print("You send a Shadow Ball at Poseidon")
            Attack = random.randint(50,200)
            print ("{",Attack,"}") 
            Poseidon = Poseidon - Attack
        if choice in answer_C:
            print ("You show Poseidon the strength of the shadow realm and you stomp, punch and throw him into walls")
            Attack = random.randint(5000,7000)
            print ("{",Attack,"}")
            Poseidon = Poseidon - Attack 
        if choice in DUEL:
            print ("Shadow Man: You are right. I am no god")
            time.sleep(3)
            print ("Shadow Man: But i am more than just a killer. Poseidon")
            time.sleep(5)
            print ("Shadow Man: I am a devourer")
            print ("You transform into the monster that is SHADONI, EATER OF WORLDS, DESTROYER OF GODS")
            God = True
        if God == True:
            if Poseidon < 50000:
                print ("E: DEVOUR")
                choice = input(">>")
                if choice in "e" or "E":
                    print ("You wrap around poseidon with your own tentacles and squeeze until you hear his whole skeleton break killing him")
                    input(".")
                    print ("You eat Poseidon banishing him to the Shadow Realm as a forever servant")
                    break
                    
        print ("Poseidon swings his trident")
        Attack = random.randint(1000,10000)
        ShadowMan = ShadowMan - Attack
        if ShadowMan < 0:
            print ("YOU DIED")
            Gods()
        if Poseidon < 0:
            print ("Poseidon heals in his waters")
            Poseidon = Poseidon + 10000
    print ("You see the hands of corpses on your back as you go back to human form")
    input(".")
    print ("A arrow flies past and you grab it and throw it at terminal velocity making it go through Artemis Skull")
    input(".")
    print ("Hades appears from out of the ground")
    Kavu = False
    PoseidonSummon = False
    Artemis = False
    Freeze = False
    Stun = False
    Poison = False
    Rage = False
    Flee = 0
    file = open("Companion.txt","r")
    Companion = file.read()
    if Companion == "Kavu":
        Kavu = True
        print ("Kavu swoops down")
        print ("Shadow Man: The god of the underworld and its ruler")
    file.close()
    Hades = 1000000
    ShadowMan = ShadowMan + 5000
    while Hades >= 0:
        print ("Hades:",Hades)
        print ("Shadow Man:", ShadowMan)
        print ("A: Shadow Beam")
        print ("B: Shadow Meteors")
        print ("C: Summon")
        choice = input(">>")
        if choice in answer_A:
            print ("You send a shadow beam between your two hands dangerously towards Hades")
            Attack = random.randint(10000,20000)
            print ("{",Attack,"}")
            Hades = Hades - Attack
        if choice in answer_B:
            print ("You send a barrage of Shadow Balls down")
            Attack = random.randint(20000,25000)
            print ("{",Attack,"}")
            Hades = Hades - Attack
        if choice in answer_C:
            if PoseidonSummon == False:
                print ("Poseidon")
            if Artemis == False:
                print ("Artmeis")
            Summon = input(">>")
            if Summon.lower() == "poseidon":
                PoseidonSummon = True
            if Summon.lower() == "artemis":
                Artemis = True
        if Kavu == True:
            print ("All Kavus heads join together to create a ice beam")
            frost = random.randint(1,12)
            Attack = random.randint(200,2500)
            print ("{",Attack,"}")
            Hades = Hades - Attack 
            if frost > 9:
                print ("Hades seems to be getting frostbite")
                Freeze = True
        if Artemis == True:
            print ("Artemis shoots down three arrows at Hades")
            Tip = random.randint(1,50)
            Attack = random.randint(20,2500)
            print ("{",Attack,"}")
            Hades = Hades - Attack
            if Tip > 45:
                print ("A poison arrow hits Hades")
                Poison = True
        if PoseidonSummon == True:
            print ("Poseidon throws his trident at Hades")
            Attack = random.randint(2000,25000)
            print ("{",Attack,"}")
            Hades = Hades - Attack
            Trident = random.randint(10,40)
            if Trident > 34:
                print ("Poseidon summons a wave and crashes it onto Hades")
                Stun = True
        if Hades < 0:
            break
        print ("Hades grabs his bident")
        Target = random.randint(1,4)
        if Target == 1:
            print ("Hades smacks you with the bident")
            followup = random.randint(1,22)
            Attack = random.randint(2000,2500)
            print ("{",Attack,"}")
            ShadowMan = ShadowMan - Attack
            if followup > 17:
                print ("He stabs you with the bident")
                Attack = random.randint(4000,5000)
                print ("{",Attack,"}")
                ShadowMan = ShadowMan - Attack
            if Rage == True:
                print ("In a fit of rage he swings multiple times at you")
                Attack = random.randint(200,1000)
                print ("{",Attack,"}")
                ShadowMan = ShadowMan - Attack
                time.sleep(2)
                Attack = random.randint(200,1000)
                print ("{",Attack,"}")
                ShadowMan = ShadowMan - Attack
                time.sleep(1)
                Attack = random.randint(200,1000)
                print ("{",Attack,"}")
                ShadowMan = ShadowMan - Attack
                time.sleep(1)
                Attack = random.randint(200,1000)
                print ("{",Attack,"}")
                ShadowMan = ShadowMan - Attack
                time.sleep(1)
                Attack = random.randint(200,1000)
                print ("{",Attack,"}")
                ShadowMan = ShadowMan - Attack
                time.sleep(1)
        if Target == 2:
            if Kavu == True:
                print ("He stabs the hydra and tears off a piece of its flesh")
                Flee = Flee + 1
            else:
                print ("He punches you")
                Attack = random.randint(20,1000)
                print ("{",Attack,"}")
                ShadowMan = ShadowMan - Attack
                time.sleep(1)
        if Target == 3:
            if Artemis == True:
                print ("Hades swings at Artemis")
                blow = random.randint(1,20)
                if blow > 15:
                    print ("Hades kills the shadow of Artemis")
                    print ("{He can be resummoned}")
                    Artemis = False
                    time.sleep(1)
            else:
                print ("He punches you")
                Attack = random.randint(20,1000)
                print ("{",Attack,"}")
                ShadowMan = ShadowMan - Attack
                time.sleep(1)
        if Target == 4:
            if PoseidonSummon == True:
                print ("Hades swings at Poseidon")
                blow = random.randint(1,20)
                if blow > 15:
                    print ("Hades tears Poseidon in half with his bident")
                    print ("{He can be resummoned}")
                    PoseidonSummon = False
                    time.sleep(1)
            else:
                print ("He punches you")
                Attack = random.randint(20,1000)
                print ("{",Attack,"}")
                ShadowMan = ShadowMan - Attack
                time.sleep(1)
        if Hades < 25000:
            Rage = True
        
        if ShadowMan < 0:
            print ("YOU DIED")
            Gods()
    print ("HADES FALLEN")
    time.sleep(3)
    print ("Shadow Man: More gods will fall")
    file = open("Companion.txt","r")
    Companion = file.read()
    if Companion == "Kavu":
        print ("Shadow Man: Now Kavu has full control of the Underworld and will be seen as the GOD")
    else:
        print ("Shadow Man: Now the underworld is free and all of the dead will be able to escape..")
    time.sleep(5)
    print ("Shadow Man: The fragment of earth has been found in new york. I must get it before anyone else does")
    time.sleep(5)
    print ("Shadow Man: Including you, creator")
    time.sleep(3)
    print ("Shadow Man: Shadow, my creator you will not get in the way or i will kill you")
    input(".")
    print ("Back on the helicoper with yourself, Jill, Claire, Leon and Ada")
    print ("Jill: Chris would not have been so stupid to go alone. something is not right")
    input(".")
    print ("Jill goes to look at the corpse of chris")
    input(".")
    print ("Jill: Hold on...")
    print ("Jill grabs a knife and cuts into the chest of chris opening it up")
    input(".")
    print ("They make a shocking discovery")
    input(".")
    print ("Chris has no organs..")
    input(".")
    print ("Jill: This wasn't Chris.. he is still out there")
    input(".")
    print ("Jill: When we got Chris from the somalis it was a decoy")
    input(".")
    print ("Jill: Who would do this")
    input(".")
    print ("Back on the ground on a rooftop is a figure watching the helicopter")
    input(".")
    print ("Leon: Who is that?")
    input(".")
    print ("Jill: Wesker...") 
    input(".")
    print ("Wesker watches as the helicopter flies away whilst Jill stares at him")
    input(".")
    print ("END OF CHAPTER 2.1")
    input(".")
    print ("CHAPTER 2.2: THE FIRST FRAGMENT")
    input(".")
    print ("Shadow Man: The first fragment has been found in NYC discovered by the invading aliens")
    input(".")
    print ("Shadow Man: As soon as this fragment is touched or moved it will send a signal to all life")
    input(".")
    print ("Shadow Man touches the fragment and a blue light shines quickly to the sky")
    input(".")
    print ("Shadow Man: let the mayhem begin")
    s = "TheFirstWar"
    save(s)
    import NYC




    


    



    
    




file=open("loadfile.txt","r")
room=file.read()
file.close()        

if room == "DeathToGods":
    Leigh()