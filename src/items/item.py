class Item:
    """Base class for all in-game items."""
    
    def __init__(self, item_id, name, description, value, item_type="misc", rarity="common"):
        self.id = item_id
        self.name = name
        self.description = description
        self.value = value  # Base value in credits
        self.item_type = item_type  # Type of item: weapon, armor, consumable, key, misc
        self.rarity = rarity  # common, uncommon, rare, epic, legendary
        
    def get_value(self):
        """Return the item's value, modified by rarity."""
        rarity_multipliers = {
            "common": 1.0,
            "uncommon": 1.5,
            "rare": 2.5,
            "epic": 4.0,
            "legendary": 10.0
        }
        return int(self.value * rarity_multipliers.get(self.rarity, 1.0))
        
    def __str__(self):
        return f"{self.name}: {self.description}"
        
class Weapon(Item):
    """Weapon that can be equipped for combat."""
    
    def __init__(self, item_id, name, description, value, damage, critical_chance=0.05, rarity="common"):
        super().__init__(item_id, name, description, value, "weapon", rarity)
        self.damage = damage
        self.critical_chance = critical_chance
        self.critical_multiplier = 2.0
        
    def calculate_damage(self):
        """Calculate the base damage of this weapon."""
        import random
        
        if random.random() < self.critical_chance:
            return int(self.damage * self.critical_multiplier), True
        return self.damage, False
        
class Armor(Item):
    """Armor that can be equipped for protection."""
    
    def __init__(self, item_id, name, description, value, defense, tech_defense=0, rarity="common"):
        super().__init__(item_id, name, description, value, "armor", rarity)
        self.defense = defense  # Physical defense
        self.tech_defense = tech_defense  # Defense against tech attacks
        
class Consumable(Item):
    """Item that can be used once for an effect."""
    
    def __init__(self, item_id, name, description, value, effect_type, effect_value, rarity="common"):
        super().__init__(item_id, name, description, value, "consumable", rarity)
        self.effect_type = effect_type  # heal, energy, buff, etc.
        self.effect_value = effect_value  # Amount of effect
        
    def use_effect(self, target):
        """Apply the item's effect to a target."""
        if self.effect_type == "heal":
            return target.heal(self.effect_value)
        elif self.effect_type == "energy":
            target.current_energy = min(target.max_energy, target.current_energy + self.effect_value)
            return self.effect_value
        elif self.effect_type == "buff":
            # Implementation would depend on buff system
            return True
        return False
        
class KeyItem(Item):
    """Special items used for quests or story progression."""
    
    def __init__(self, item_id, name, description, quest_id=None):
        super().__init__(item_id, name, description, 0, "key", "unique")
        self.quest_id = quest_id
        
class ImplantItem(Item):
    """Cybernetic implants that provide passive bonuses."""
    
    def __init__(self, item_id, name, description, value, stat_bonuses=None, rarity="uncommon"):
        super().__init__(item_id, name, description, value, "implant", rarity)
        self.stat_bonuses = stat_bonuses or {}  # Dict of stat_name: bonus_value
        
    def apply_bonuses(self, character):
        """Apply stat bonuses to a character."""
        for stat, bonus in self.stat_bonuses.items():
            if hasattr(character, stat):
                current_value = getattr(character, stat)
                setattr(character, stat, current_value + bonus)
                
    def remove_bonuses(self, character):
        """Remove stat bonuses from a character."""
        for stat, bonus in self.stat_bonuses.items():
            if hasattr(character, stat):
                current_value = getattr(character, stat)
                setattr(character, stat, current_value - bonus) 