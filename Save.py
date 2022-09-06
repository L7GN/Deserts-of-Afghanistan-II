import os.path
import Character
file_exists = os.path.isfile("loadfile.txt")

def load():
    if file_exists:
        file=open("loadfile.txt","r")
        room=file.read()
        file.close()
    else:
        room="Start"

    roomchooser(room)

def save(s):
    file=open("loadfile.txt","w")
    file.write(s)
    file.close()

def roomchooser(room):
    if room=="Start":
        import CharacterCreator
    if room == "TheDeserts":
        import TheDeserts
    if room == "ShadowsOfEvil":
        file = open("CharacterClass.txt","r")
        char_type = file.read()
        if char_type == "mage":
            from Mage import ShadowsOfEvil
        if char_type == "thief":
            from Thief import ShadowsOfEvil
        if char_type == "prisoner":
            from Prisoner import ShadowsOfEvil
        if char_type == "gamer":
            from Gamer import ShadowsOfEvil
        if char_type == "vagabound":
            from Vagabound import ShadowsOfEvil
        if char_type == "warrior":
            from Warrior  import ShadowsOfEvil
        file.close()
    if room == "Fallen":
        file = open("CharacterClass.txt","r")
        char_type = file.read()
        file.close()
        if char_type == "mage":
            from Mage import Fallen
        if char_type == "thief":
            from Thief import Fallen
        if char_type == "prisoner":
            from Prisoner import Fallen
        if char_type == "gamer":
            from Gamer import Fallen
        if char_type == "vagabound":
            from Vagabound import Fallen
        if char_type == "warrior":
            from Warrior import Fallen
    if room == "Monsterverse":
        file = open("CharacterClass.txt","r")
        char_type = file.read()
        file.close()
        if char_type == "mage":
            from Mage import Monsterverse
        if char_type  == "thief":
            from Thief import Monsterverse
        if char_type == "prisoner":
            from Prisoner import Monsterverse
        if char_type== "gamer":
            from Gamer import Monsterverse
        if char_type == "vagabound":
            from Vagabound import Monsterverse
        if char_type== "warrior":
            from Warrior  import Monsterverse
    if room == "StarWars":
        file = open("CharacterClass.txt","r")
        char_type = file.read()
        file.close()
        if char_type == "mage":
            from Mage import StarWars
        if char_type  == "thief":
            from Thief import StarWars
        if char_type == "prisoner":
            from Prisoner import StarWars
        if char_type== "gamer":
            from Gamer import StarWars
        if char_type == "vagabound":
            from Vagabound import StarWars
        if char_type== "warrior":
            from Warrior  import StarWars
    if room == "Awakening":
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
    else:
        import Void
            




load()