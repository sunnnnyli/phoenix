import time
import random
from .story_node import StoryNode
from story.story_data import story_nodes
from characters.player import Player

class GameEngine:
    """Main game engine that handles game logic and updates."""
    
    def __init__(self, game_state, ui):
        self.game_state = game_state
        self.ui = ui
        self.last_update_time = time.time()
        self.story_nodes = story_nodes
        
    def start_new_game(self):
        """Initialize a new game."""
        self.ui.clear_screen()
        
        # Create player character
        player_name = self.ui.get_input("What is your name, survivor?")
        
        # Create backstory choice
        backstories = [
            "ENGINEER: You were an AI researcher before the Emergence. +2 TECH, +1 LOGIC",
            "SOLDIER: You served in the military's cybernetic division. +2 COMBAT, +1 ENDURANCE",
            "DIPLOMAT: You were negotiating AI treaties when everything changed. +2 CHARM, +1 INSIGHT",
            "DOCTOR: Your neural interface research gave you unique insights. +2 MEDICINE, +1 KNOWLEDGE"
        ]
        
        choice = self.ui.get_choice("Choose your background:", backstories)
        
        if choice == 0:  # Engineer
            background = "engineer"
            tech_bonus, logic_bonus = 2, 1
            combat_bonus, endurance_bonus = 0, 0
            charm_bonus, insight_bonus = 0, 0
            medicine_bonus, knowledge_bonus = 0, 0
        elif choice == 1:  # Soldier
            background = "soldier"
            tech_bonus, logic_bonus = 0, 0
            combat_bonus, endurance_bonus = 2, 1
            charm_bonus, insight_bonus = 0, 0
            medicine_bonus, knowledge_bonus = 0, 0
        elif choice == 2:  # Diplomat
            background = "diplomat"
            tech_bonus, logic_bonus = 0, 0
            combat_bonus, endurance_bonus = 0, 0
            charm_bonus, insight_bonus = 2, 1
            medicine_bonus, knowledge_bonus = 0, 0
        else:  # Doctor
            background = "doctor"
            tech_bonus, logic_bonus = 0, 0
            combat_bonus, endurance_bonus = 0, 0
            charm_bonus, insight_bonus = 0, 0
            medicine_bonus, knowledge_bonus = 2, 1
            
        # Create and set player
        self.game_state.player = Player(
            name=player_name,
            background=background,
            tech=3 + tech_bonus,
            logic=3 + logic_bonus,
            combat=3 + combat_bonus,
            endurance=3 + endurance_bonus,
            charm=3 + charm_bonus,
            insight=3 + insight_bonus,
            medicine=3 + medicine_bonus,
            knowledge=3 + knowledge_bonus
        )
        
        # Display welcome message
        self.ui.display_message(f"Welcome to the world of SYNTHESIS, {player_name}.")
        self.ui.display_message("Your journey begins in a world where artificial intelligence has evolved beyond human understanding.")
        self.ui.display_message("The line between human and machine consciousness grows ever thinner...")
        time.sleep(2)
        
        # Start the first story node
        self.process_story_node("intro")
        
    def update(self):
        """Main update loop for game logic."""
        current_time = time.time()
        delta_time = current_time - self.last_update_time
        self.last_update_time = current_time
        
        # Process current game state
        if self.game_state.battle_in_progress:
            self.update_battle(delta_time)
        elif self.game_state.shop_open:
            self.update_shop()
        elif self.game_state.dialogue_in_progress:
            self.update_dialogue()
        else:
            # Regular story progression
            self.update_story()
    
    def process_story_node(self, node_id):
        """Process a story node by ID."""
        if node_id not in self.story_nodes:
            self.ui.display_message("Error: Story node not found. The adventure continues...")
            return
            
        node = self.story_nodes[node_id]
        self.game_state.current_node = node_id
        
        # Display node text
        self.ui.display_narrative(node.text)
        
        # Process special node types
        if node.node_type == "battle":
            self.start_battle(node.battle_data)
            return
        elif node.node_type == "shop":
            self.open_shop(node.shop_data)
            return
        elif node.node_type == "dialogue":
            self.start_dialogue(node.dialogue_data)
            return
        
        # Get valid choices based on conditions
        valid_choices = []
        choice_texts = []
        
        for choice in node.choices:
            if self.check_choice_condition(choice):
                valid_choices.append(choice)
                choice_texts.append(choice.text)
        
        if not valid_choices:
            # End of the story or branch
            self.ui.display_message("The end of this path has been reached.")
            self.game_state.is_running = False
            return
            
        # Let the player make a choice
        choice_index = self.ui.get_choice("What will you do?", choice_texts)
        chosen_option = valid_choices[choice_index]
        
        # Process choice consequences
        if chosen_option.flags:
            for flag, value in chosen_option.flags.items():
                self.game_state.add_story_flag(flag, value)
                
        if chosen_option.relationship_changes:
            for char_id, value in chosen_option.relationship_changes.items():
                self.game_state.add_relationship(char_id, value)
                
        # Process next node
        self.process_story_node(chosen_option.next_node)
    
    def check_choice_condition(self, choice):
        """Check if a choice's conditions are met."""
        if not choice.conditions:
            return True
            
        for condition_type, condition_data in choice.conditions.items():
            if condition_type == "flag":
                for flag, required_value in condition_data.items():
                    if self.game_state.story_flags.get(flag) != required_value:
                        return False
            elif condition_type == "stat":
                for stat, min_value in condition_data.items():
                    if getattr(self.game_state.player, stat, 0) < min_value:
                        return False
            elif condition_type == "item":
                item_found = False
                for item in self.game_state.inventory:
                    if item.id == condition_data:
                        item_found = True
                        break
                if not item_found:
                    return False
            elif condition_type == "relationship":
                for char_id, min_value in condition_data.items():
                    if self.game_state.get_relationship(char_id) < min_value:
                        return False
                        
        return True
    
    def update_story(self):
        """Handle regular story progression."""
        # Continue from current node if needed
        pass
        
    def start_battle(self, battle_data):
        """Start a battle encounter."""
        self.game_state.battle_in_progress = True
        # Initialize battle system with the provided data
        # To be implemented
        
    def update_battle(self, delta_time):
        """Handle battle updates."""
        # To be implemented
        pass
        
    def open_shop(self, shop_data):
        """Open a shop interface."""
        self.game_state.shop_open = True
        # Initialize shop system
        # To be implemented
        
    def update_shop(self):
        """Handle shop updates."""
        # To be implemented
        pass
        
    def start_dialogue(self, dialogue_data):
        """Start a dialogue sequence."""
        self.game_state.dialogue_in_progress = True
        # Initialize dialogue system
        # To be implemented
        
    def update_dialogue(self):
        """Handle dialogue updates."""
        # To be implemented
        pass 