# Make a character class



class Character:
    # Make initializer function to tell the class what information to expect
    # Aside from name and char_type, all parameters of the initializer function are stats
    def __init__(self, name, char_type, max_health, health, strength, speed, intelligence, charisma, stealth, defense, max_mana, mana): 
        # Time variables.
        self.night = False #Used for random enemy interactions (Raises chances)
        self.time_count = 0 # This increments with every step.
 
        # Gameplay variables
        self.alive = True 
        self.victory = False
        self.battling = False
        self.wallet = 0
        self.tired = False 
        self.slept = True
        self.level_xp_req = {2: 100, 3: 200, 4:250, 5:500, 6:550, 7:700} # key is the level and the value is how much XP is required to reach that level
        self.inventory = None # The object that will hold the items the player picked up
        self.equipped = None # The weapon the player will use to fight or interact with main quest objects
        self.char_type = char_type
        self.name = name
        self.skill_cap = 150
        self.lvl_cap = 100
        self.body_count = 0
        self.xp = 0
        self.char_lvl = 1
        self.Gold = 0
        
 
        # Quest variables
        self.quests = {} # Accepted Quests
        self.active_quests = {} # Activated Quests
        self.completed_quests = {}
        self.killed_quest_enemies = {}  # For quest type 'hunt monster', enemy.name is the key and the number the user killed is the value; used to see if a quest is complete        
        self.defeated_enemies = {} # When the player dies/wins, list the enemies and how many of each type they've killed
 
        # Stats
        self.health = health
        self.max_health = max_health
        self.max_mana = max_mana
        self.mana = mana
        self.strength = strength
        self.speed = speed
        self.intelligence = intelligence
        self.charisma = charisma
        self.stealth = stealth
        self.defense = defense
        
        # All stats
        self.stats = {
            'Health': self.health,
            'Strength': self.strength,
            'Speed': self.speed,
            'Intelligence': self.intelligence,
            'Charisma': self.charisma,
            'Stealth': self.stealth,
            'Defense': self.defense,
            'Mana': self.mana,
        } 
         #############################################################################################
        ##Next we will be making the functions the player can use/what we will be using in the game##
       #############################################################################################
 
# Make character types. each argument corresponds (positionally) to the parameters in the initializer function of the Character class
mage = Character("", "mage", 5,5,3,4,8,6,1,8,10,10) 
thief = Character("", "thief", 4,4,7,8,8,6,5,4,3,3)
gamer = Character("", "gamer", 4,5,4,2,10,4,6,3,5,5)
prisoner = Character ("", "prisoner", 5,5,6,7,5,3,6,4,6,5,)
vagabound = Character ("", "vagabound",10,10,10,5,6,7,3,6,0,0,)
warrior = Character ("", "warrior", 7,10,10,6,3,7,5,5,4,2,)

def do_action(self, action, **kwargs):
    action_method = getattr(self, action.method.__name__)
    if action_method:
        action_method(**kwargs)

