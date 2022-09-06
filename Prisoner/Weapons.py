# Make a character class
class Weapon:
    # Make initializer function to tell the class what information to expect
    # Aside from name and char_type, all parameters of the initializer function are stats
    def __init__(self, name, char_type,attack, defence, durability, parry, speed,): 

 
        # Stats
        self.attack = attack
        self.defence = defence
        self.parry = parry
        self.durability = durability
        self.speed = speed

        
        # All stats
        self.stats = {
            'Attack': self.attack,
            'Strength': self.defence,
            'Speed': self.speed,
            'Intelligence': self.parry,
            'Charisma': self.durability,
        } 
         #############################################################################################
        ##Next we will be making the functions the player can use/what we will be using in the game##
       #############################################################################################
 
# Make character types. each argument corresponds (positionally) to the parameters in the initializer function of the Character class
Lightsaber = Weapon("", "lightsaber", 20,10,999,7,40) 
Sword = Weapon("", "lightsaber", 5,2,3,4,5) 


def do_action(self, action, **kwargs):
    action_method = getattr(self, action.method.__name__)
    if action_method:
        action_method(**kwargs)

