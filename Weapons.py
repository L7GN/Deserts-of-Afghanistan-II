# Make a character class
class Weapon:
    # Make initializer function to tell the class what information to expect
    # Aside from name and char_type, all parameters of the initializer function are stats
    def __init__(self,Rarity ,name, char_type,attack, defence, durability, parry, speed,): 

 
        # Stats
        self.attack = attack
        self.defence = defence
        self.parry = parry
        self.durability = durability
        self.speed = speed

        
        # All stats
        self.stats = {
            'Attack': self.attack,
            'Defence': self.defence,
            'Speed': self.speed,
            'Parry': self.parry,
            'Durability': self.durability,
        } 
         #############################################################################################
        ##Next we will be making the functions the player can use/what we will be using in the game##
       #############################################################################################
 
# Make character types. each argument corresponds (positionally) to the parameters in the initializer function of the Character class
Lightsaber = Weapon("Common","", "lightsaber", 50,10,999,7,40) 
Sword = Weapon("Common","", "sword", 5,2,3,4,5) 
PredatorBlade = Weapon( "Rare","PredatorBlade", "Predator's Handblade",35,15,100,10,100)
Combistick = Weapon("Rarest","Combistick", "Combistick",40,25,999,30,40)
Shouldercannon = Weapon("Legendary","Shouldercannon","Shouldercannon",350,0,10,0,6)
PredatorDagger = Weapon ("Epic","Ornamental Dagger","Ornamental Dagger",15,3,50,5,250)

def do_action(self, action, **kwargs):
    action_method = getattr(self, action.method.__name__)
    if action_method:
        action_method(**kwargs)

