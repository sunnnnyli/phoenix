class GameState:
    """Class that manages the global game state and all game data."""
    
    def __init__(self):
        self.is_running = True
        self.current_location = None
        self.player = None
        self.companions = []
        self.inventory = []
        self.quest_log = []
        self.story_flags = {}
        self.relationships = {}
        self.current_node = "intro"
        self.battle_in_progress = False
        self.shop_open = False
        self.dialogue_in_progress = False
        self.tutorial_complete = False
        self.days_passed = 0
        
    def add_story_flag(self, flag_name, value=True):
        """Set a story flag to track narrative choices and progress."""
        self.story_flags[flag_name] = value
        
    def has_flag(self, flag_name):
        """Check if a story flag exists and is True."""
        return self.story_flags.get(flag_name, False)
        
    def add_relationship(self, character_id, value=0):
        """Initialize or update relationship with a character."""
        if character_id not in self.relationships:
            self.relationships[character_id] = value
        else:
            self.relationships[character_id] += value
            
    def get_relationship(self, character_id):
        """Get current relationship value with a character."""
        return self.relationships.get(character_id, 0)
        
    def add_companion(self, companion):
        """Add a character as a companion."""
        if companion not in self.companions:
            self.companions.append(companion)
            
    def remove_companion(self, companion):
        """Remove a character from companions."""
        if companion in self.companions:
            self.companions.remove(companion)
            
    def add_to_inventory(self, item):
        """Add an item to player's inventory."""
        self.inventory.append(item)
        
    def remove_from_inventory(self, item):
        """Remove an item from player's inventory."""
        if item in self.inventory:
            self.inventory.remove(item)
            
    def get_items_by_type(self, item_type):
        """Get all items of a specific type from inventory."""
        return [item for item in self.inventory if item.item_type == item_type]
        
    def add_quest(self, quest):
        """Add a quest to the quest log."""
        self.quest_log.append(quest)
        
    def update_quest_status(self, quest_id, status):
        """Update the status of a quest in the quest log."""
        for quest in self.quest_log:
            if quest.id == quest_id:
                quest.status = status
                break
                
    def advance_time(self, days=1):
        """Advance game time by the specified number of days."""
        self.days_passed += days 