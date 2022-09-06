import time
Flag = True
Location = []

File = open("loadfile.txt")
Level = File.read()

File = open("Earth.txt","w")
File.write("london\n")
File.write("new york\n")
File.write("los angeles\n")
File.close
File = open("Earth.txt", "r")
Location = File.read()
print (Location)
while Flag == True:
    choice = input(">>")
    choice = choice.lower()
    if choice == "london":
        print ("London")
        time.sleep(2)
        print ("STATUS: DESTROYED")
        time.sleep(1)
        print ("LEADER: DEAD")
        time.sleep(1)
        print ("POPULATION: 100")
        time.sleep(1)
        print ("LATEST EVENT: Hydra god takes London on its own")
        time.sleep(4)
        print ("TRANSITIONING TO LONDON...")
        time.sleep(3)
        print ("ERROR")
        print (Location)
    if choice == "new york":
        print ("New York")
        time.sleep(2)
        print ("STATUS: DANGER")
        time.sleep(1) 
        print ("LEADER: UNKNOWN")
        time.sleep(1)
        print ("POPULATION: 10,000,453") 
        time.sleep(1)
        print ("LATEST EVENT: ALIEN SPECIES INVADE NYC")
        time.sleep(4)
        print ("Transitioning to NYC...")
        time.sleep(3)
        import NYC
    if choice == "los angeles":
        print ("Los Angeles")
        time.sleep(2)
        print ("STATUS: Safe")
        time.sleep(1) 
        print ("LEADER: ALIVE")
        time.sleep(1)
        print ("POPULATION: 8,000,000") 
        time.sleep(1)
        print ("LATEST EVENT: A dead orc drops from sky")
        time.sleep(4)
        print ("Transitioning to LA....")
        time.sleep(3)
        import LA
