class Player:
    """Represents the player character with stats and abilities."""
    
    def __init__(self, name, background, tech=3, logic=3, combat=3, endurance=3, 
                 charm=3, insight=3, medicine=3, knowledge=3):
        self.name = name
        self.background = background
        
        # Core stats
        self.tech = tech  # Technology proficiency 
        self.logic = logic  # Logical reasoning
        self.combat = combat  # Combat effectiveness
        self.endurance = endurance  # Physical resilience
        self.charm = charm  # Social influence
        self.insight = insight  # Perceptiveness
        self.medicine = medicine  # Medical knowledge
        self.knowledge = knowledge  # General knowledge
        
        # Derived stats
        self.max_health = 50 + (self.endurance * 5)
        self.current_health = self.max_health
        self.max_energy = 30 + (self.tech * 3)
        self.current_energy = self.max_energy
        
        # Combat stats
        self.attack_power = self.combat * 2
        self.defense = self.endurance * 1.5
        self.tech_power = self.tech * 2
        self.initiative = (self.insight + self.logic) / 2
        
        # Player level and progression
        self.level = 1
        self.experience = 0
        self.experience_to_level = 100
        
        # Special abilities unlocked based on background
        self.abilities = self._get_starting_abilities()
        
    def _get_starting_abilities(self):
        """Return initial abilities based on background."""
        abilities = []
        
        if self.background == "engineer":
            abilities.append({
                "name": "System Hack", 
                "description": "Temporarily disable an electronic system",
                "energy_cost": 10,
                "cooldown": 2
            })
        elif self.background == "soldier":
            abilities.append({
                "name": "Tactical Strike", 
                "description": "Deal high damage to a single target",
                "energy_cost": 8,
                "cooldown": 1
            })
        elif self.background == "diplomat":
            abilities.append({
                "name": "Persuasive Argument", 
                "description": "Chance to avoid combat or get better prices",
                "energy_cost": 5,
                "cooldown": 3
            })
        elif self.background == "doctor":
            abilities.append({
                "name": "Emergency Treatment", 
                "description": "Restore health to self or ally",
                "energy_cost": 12,
                "cooldown": 2
            })
            
        # Common starting ability for all backgrounds
        abilities.append({
            "name": "Neural Interface", 
            "description": "Analyze electronic systems for information",
            "energy_cost": 5,
            "cooldown": 1
        })
        
        return abilities
        
    def gain_experience(self, amount):
        """Add experience points and level up if threshold reached."""
        self.experience += amount
        
        if self.experience >= self.experience_to_level:
            self.level_up()
            
    def level_up(self):
        """Increase the player's level and stats."""
        self.level += 1
        self.experience -= self.experience_to_level
        self.experience_to_level = int(self.experience_to_level * 1.5)
        
        # Increase stats
        self._increase_random_stats(3)
        
        # Recalculate derived stats
        self.max_health = 50 + (self.endurance * 5)
        self.current_health = self.max_health
        self.max_energy = 30 + (self.tech * 3)
        self.current_energy = self.max_energy
        
        # Update combat stats
        self.attack_power = self.combat * 2
        self.defense = self.endurance * 1.5
        self.tech_power = self.tech * 2
        self.initiative = (self.insight + self.logic) / 2
        
        # Every 3 levels, gain a new ability
        if self.level % 3 == 0:
            self._gain_new_ability()
            
    def _increase_random_stats(self, points):
        """Distribute points randomly among stats."""
        import random
        
        stats = ["tech", "logic", "combat", "endurance", 
                 "charm", "insight", "medicine", "knowledge"]
                 
        for _ in range(points):
            stat = random.choice(stats)
            setattr(self, stat, getattr(self, stat) + 1)
            
    def _gain_new_ability(self):
        """Add a new ability to the player based on their highest stats."""
        # This would be implemented with a list of potential abilities
        # For now, it's a placeholder
        pass
        
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