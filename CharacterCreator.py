import time

def save(s):
    file=open("loadfile.txt","w")
    file.write(s)
    file.close()

s ="Start"
save(s)
file = open("FirstWarCasualties.txt","w")
file.truncate()
file.close()
file = open("FirstWar.txt","w")
file.truncate()
file.close()
file = open("CharacterClass.txt","w")
file.truncate()
file.close()
file = open("CharacterHair.txt","w")
file.truncate()
file.close()
file = open("CharacterGender.txt","w")
file.truncate()
file.close()
file = open("CharacterName.txt","w")
file.truncate()
file.close()
file = open("CharacterPhysique.txt","w")
file.truncate()
file.close()
file = open("CharacterSkin.txt","w")
file.truncate()
file.close()
file = open("CharacterName.txt","w")
file.truncate()
file.close()
file = open("Companion.txt","w")
file.truncate()
file.close()
file = open("Gold.txt","w")
file.truncate()
file.close()
file = open("Power.txt","w")
file.truncate()
file.close()
file = open("Weapon.txt","w")
file.truncate()
file.close()
file = open("Kills.txt","w")
file.truncate()
file.close()
file = open("CharacterStealth.txt","w")
file.truncate()
file.close()
file = open("CharacterStrength","w")
file.truncate()
file.close()
file = open("CharacterHealth.txt","w")
file.truncate()
file.close()
file = open("CharacterSpeed","w")
file.truncate()
file.close()
file = open("CharacterIntelligence.txt","w")
file.truncate()
file.close()
file = open("CharacterCharisma","w")
file.truncate()
file.close()
file = open("CharacterStealth.txt","w")
file.truncate()
file.close()
file = open("CharacterMana.txt","w")
file.truncate()
file.close()
def CreatorMenu():
    Flag = True
    while Flag == True:
        print ("1. Hair Colour")
        print ("2. Skin Colour")
        print ("3. Race")
        print ("4. Gender")
        print ("5. Physique")
        print ("6. Eye Colour")
        print ("7. Continue")
        try:
            Option = int(input(">>"))
            if Option == 1:
                print ("1. Black")
                print ("2. Blonde")
                print ("3. Brown")
                print ("4. Ginger")
                print ("5. Grey")
                Choice = int(input(">>"))
                if Choice == 1:
                    file=open("CharacterHair.txt","w")
                    file.write("Black")
                    file.close()
                if Choice == 2:
                    file=open("CharacterHair.txt","w")
                    file.write("Blonde")
                    file.close()
                if Choice == 3:
                    file=open("CharacterHair.txt","w")
                    file.write("Brown")
                    file.close()
                if Choice == 4:
                    file=open("CharacterHair.txt","w")
                    file.write("Ginger")
                    file.close()
                if Choice == 5:
                    file=open("CharacterHair.txt","w")
                    file.write("Grey")
                    file.close()
            if Option == 2:
                print ("1. White")
                print ("2. Black")
                print ("3. Brown")
                print ("4. Yellow")
                Choice = int(input(">>"))
                if Choice == 1:
                    file=open("CharacterSkin.txt","w")
                    file.write("White")
                    file.close()
                if Choice == 2:
                    file=open("CharacterSkin.txt","w")
                    file.write("Black")
                    file.close()
                if Choice == 3:
                    file=open("CharacterSkin.txt","w")
                    file.write("Brown")
                    file.close()
                if Choice == 4:
                    file=open("CharacterSkin.txt","w")
                    file.write("Yellow")
                    file.close()
            if Option == 3:
                print ("1. Human")
                print ("2. Dwarf")
                print ("3. Elf")
                print ("4. Orc")
                Choice = int(input(">>"))
                if Choice == 1:
                    file=open("CharacterRace.txt","w")
                    file.write("Human")
                    file.close()
                if Choice == 2:
                    file=open("CharacterRace.txt","w")
                    file.write("Dwarf")
                    file.close()
                if Choice == 3:
                    file=open("CharacterRace.txt","w")
                    file.write("Elf")
                    file.close()
                if Choice == 4:
                    file=open("CharacterRace.txt","w")
                    file.write("Orc")
                    file.close()
            if Option == 4:
                print ("1. Male")
                print ("2. Female")
                print ("If you want to change or be no gender then find god(like seriously he is out there somewhere")
                Choice = int(input(">>"))
                if Choice == 1:
                    file=open("CharacterGender.txt","w")
                    file.write("Male")
                    file.close()
                if Choice == 2:
                    file=open("CharacterGender.txt","w")
                    file.write("Female")
                    file.close()
            if Option == 5:
                print ("1. Skinny")
                print ("2. Muscular")
                print ("3. Obese")
                print ("4. Fat")
                print ("5. Malnourished")
                Choice = int(input(">>"))
                if Choice == 1:
                    file=open("CharacterPhysique.txt","w")
                    file.write("Skinny")
                    file.close()
                if Choice == 2:
                    file=open("CharacterPhysique.txt","w")
                    file.write("Muscular")
                    file.close()
                if Choice == 3:
                    file=open("CharacterPhysique.txt","w")
                    file.write("Obese")
                    file.close()
                if Choice == 4:
                    file=open("CharacterPhysique.txt","w")
                    file.write("Malnourished")
                    file.close()
            if Option == 6:
                print ("1. White")
                print ("2. Green")
                print ("3. Brown")
                print ("4. Blue")
                Choice = int(input(">>"))
                if Choice == 1:
                    file=open("CharacterEye.txt","w")
                    file.write("White")
                    file.close()
                if Choice == 2:
                    file=open("CharacterEye.txt","w")
                    file.write("Green")
                    file.close()
                if Choice == 3:
                    file=open("CharacterEye.txt","w")
                    file.write("Brown")
                    file.close()
                if Choice == 4:
                    file=open("CharacterEye.txt","w")
                    file.write("Blue")
                    file.close()
            if Option == 7:
                break 
                
            else:
                print ("Input a number between 1-7")
        except:
            print ("Input a number")
    import TheDeserts



 

    
            

    


    


def intro():
    print ("Welcome to the New World")
    time.sleep(2)
    print ("Its time you get a identity")
    time.sleep(2)
    print ("Narrator: This is the time where you can become whatever you want to be")
    time.sleep(4)
    print ("Narrator: Currently, you are dead")
    time.sleep(2)
    print ("Narrator: We all are except for one")
    time.sleep(2)
    print ("Narrator: Remember we have a bond me and you")
    time.sleep(3)
    print ("Narrator: I will not be able to return")
    time.sleep(3)
    print ("Narrator: But remember i was always be by your side.. Now to the creation")
    CreatorMenu()

intro()

