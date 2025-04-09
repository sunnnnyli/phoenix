class NPC:
    """Base class for all non-player characters."""
    
    def __init__(self, npc_id, name, role, description, faction=None, is_companion=False):
        self.id = npc_id
        self.name = name
        self.role = role  # e.g., companion, merchant, enemy, quest-giver
        self.description = description
        self.faction = faction
        self.is_companion = is_companion
        self.dialogue_trees = {}
        self.quest_flags = {}
        
    def add_dialogue_tree(self, tree_id, dialogue_tree):
        """Add a dialogue tree for this NPC."""
        self.dialogue_trees[tree_id] = dialogue_tree
        
    def get_dialogue_tree(self, tree_id):
        """Get a specific dialogue tree."""
        return self.dialogue_trees.get(tree_id)
        
    def set_quest_flag(self, flag_name, value=True):
        """Set a quest flag for this NPC."""
        self.quest_flags[flag_name] = value
        
    def has_quest_flag(self, flag_name):
        """Check if a quest flag is set for this NPC."""
        return self.quest_flags.get(flag_name, False)
        
class Companion(NPC):
    """Special NPC that can join the player's party."""
    
    def __init__(self, npc_id, name, description, faction=None, 
                 tech=0, logic=0, combat=0, endurance=0, 
                 charm=0, insight=0, medicine=0, knowledge=0):
        super().__init__(npc_id, name, "companion", description, faction, True)
        
        # Companion stats
        self.tech = tech
        self.logic = logic
        self.combat = combat
        self.endurance = endurance
        self.charm = charm
        self.insight = insight
        self.medicine = medicine
        self.knowledge = knowledge
        
        # Derived stats
        self.max_health = 40 + (self.endurance * 5)
        self.current_health = self.max_health
        self.max_energy = 25 + (self.tech * 3)
        self.current_energy = self.max_energy
        
        # Combat stats
        self.attack_power = self.combat * 2
        self.defense = self.endurance * 1.5
        self.tech_power = self.tech * 2
        self.initiative = (self.insight + self.logic) / 2
        
        # Companion specific
        self.loyalty = 50  # Ranges from 0-100
        self.abilities = []
        self.personality_traits = []
        
    def modify_loyalty(self, amount):
        """Change companion loyalty."""
        self.loyalty = max(0, min(100, self.loyalty + amount))
        
    def add_ability(self, ability):
        """Add a special ability to the companion."""
        self.abilities.append(ability)
        
    def take_damage(self, amount):
        """Reduce health by the given amount."""
        damage = max(1, amount - int(self.defense / 2))
        self.current_health = max(0, self.current_health - damage)
        return damage
        
    def heal(self, amount):
        """Restore health by the given amount."""
        self.current_health = min(self.max_health, self.current_health + amount)
        return amount
        
    def use_energy(self, amount):
        """Use energy for an ability."""
        if self.current_energy >= amount:
            self.current_energy -= amount
            return True
        return False
        
    def rest(self):
        """Restore some health and energy when resting."""
        health_restore = int(self.max_health * 0.3)
        energy_restore = int(self.max_energy * 0.5)
        
        self.heal(health_restore)
        self.current_energy = min(self.max_energy, self.current_energy + energy_restore)
        
        return health_restore, energy_restore
        
class Enemy(NPC):
    """Hostile NPC for battle encounters."""
    
    def __init__(self, npc_id, name, description, level=1, faction=None):
        super().__init__(npc_id, name, "enemy", description, faction, False)
        
        self.level = level
        
        # Enemy stats scaled by level
        base_stat = 2 + level // 2
        self.attack = base_stat + level
        self.defense = base_stat
        self.tech_power = base_stat
        self.speed = base_stat
        
        # Health scales with level
        self.max_health = 30 + (level * 10)
        self.current_health = self.max_health
        
        # Enemy abilities
        self.abilities = []
        self.loot_table = []
        self.experience_reward = 20 * level
        
    def add_ability(self, ability):
        """Add a special ability to the enemy."""
        self.abilities.append(ability)
        
    def add_loot(self, item, drop_chance):
        """Add a possible item drop with drop chance."""
        self.loot_table.append({"item": item, "chance": drop_chance})
        
    def get_loot(self):
        """Roll for loot drops based on loot table."""
        import random
        
        dropped_items = []
        for loot in self.loot_table:
            if random.random() < loot["chance"]:
                dropped_items.append(loot["item"])
                
        return dropped_items
        
    def take_damage(self, amount):
        """Reduce health by the given amount."""
        damage = max(1, amount - self.defense)
        self.current_health = max(0, self.current_health - damage)
        return damage
        
    def is_defeated(self):
        """Check if enemy is defeated."""
        return self.current_health <= 0 