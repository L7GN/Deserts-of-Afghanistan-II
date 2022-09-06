import Character as Character # Import character to access character types
import time 
# Assign character objects to the name (a string)
char_types = {
    "mage": Character.mage,
    "thief": Character.thief
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
    choice = input("Please choose a character by typing its name\n")
 
    # Loop through char_types to check which character the player chose
    for char in char_types.keys():
 
        # If their choice is equal to the current key (Iteration 1 is "mage") then assign that character object to 'player'
        if choice.lower() == char:
            
            # Assign the character object to the variable 'player'
            player = char_types[char]
            
            # Allow them to give their character a name
            name = input("Please give your character a name\n")
            
            # Confirm that they entered their desired name correctly
            conf = input(f"You entered {name}, is this correct? y/n \n")
            
            # If they are satisfied with the name they entered the first time, assign the name to the attribute 'name' of the character object (which is assigned to 'player' on line 40)
            if conf.lower() == 'y':
                player.name = name
                print(f"{name},Welcome to the Deserts of Afganistan")

            
            # If they did not enter the name correctly, use a while loop to ask until they are satisfied with their entry
            while conf.lower() == 'n':
                name = input("Please give your character a name\n")
                conf = input(f"You entered {name}, is this correct? y/n \n")
                
                #If they are satisfied with the name they gave, assign the name to the attribute 'name' of the character object (which is assigned to 'player' on line 40)
                if conf.lower() == 'y':
                    player.name = name
                    print("{name),Welcome to the Deserts Of Afganistan")

 
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
