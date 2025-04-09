import os
import time
import textwrap
import random

class TextUI:
    """Handles text-based user interface elements."""
    
    def __init__(self, width=80):
        self.width = width
        self.wrapper = textwrap.TextWrapper(width=width)
        
    def clear_screen(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def display_title_screen(self, title, subtitle=None):
        """Display a fancy title screen for the game."""
        self.clear_screen()
        
        # Create a border
        border = "=" * self.width
        
        print("\n\n")
        print(border)
        print()
        
        # Center the title
        padding = " " * ((self.width - len(title)) // 2)
        print(f"{padding}{title}")
        
        if subtitle:
            # Center the subtitle
            sub_padding = " " * ((self.width - len(subtitle)) // 2)
            print(f"{sub_padding}{subtitle}")
            
        print()
        print(border)
        print("\n")
        
    def display_message(self, message, delay=0.5):
        """Display a message with an optional delay."""
        wrapped_lines = self.wrapper.wrap(message)
        for line in wrapped_lines:
            print(line)
        time.sleep(delay)
        
    def display_narrative(self, text, typing_effect=True):
        """Display narrative text with an optional typing effect."""
        wrapped_lines = self.wrapper.wrap(text)
        
        if typing_effect:
            for line in wrapped_lines:
                for char in line:
                    print(char, end='', flush=True)
                    time.sleep(0.02)
                print()
                time.sleep(0.3)
        else:
            for line in wrapped_lines:
                print(line)
                
        print()  # Add an extra line
        time.sleep(0.5)  # Pause after narrative
        
    def get_input(self, prompt):
        """Get text input from the user."""
        print(f"{prompt}")
        return input("> ").strip()
        
    def get_choice(self, prompt, options):
        """Present a list of choices and get the user's selection."""
        print(f"\n{prompt}")
        
        for i, option in enumerate(options):
            print(f"[{i+1}] {option}")
            
        while True:
            try:
                choice = input("\nEnter your choice (number): ")
                choice_index = int(choice) - 1
                
                if 0 <= choice_index < len(options):
                    return choice_index
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")
                
    def display_character_stats(self, character):
        """Display a character's stats."""
        self.clear_screen()
        print(f"=== {character.name} ===")
        print(f"Background: {character.background}")
        print(f"Health: {character.current_health}/{character.max_health}")
        print()
        print("--- STATS ---")
        print(f"TECH: {character.tech}  |  LOGIC: {character.logic}")
        print(f"COMBAT: {character.combat}  |  ENDURANCE: {character.endurance}")
        print(f"CHARM: {character.charm}  |  INSIGHT: {character.insight}")
        print(f"MEDICINE: {character.medicine}  |  KNOWLEDGE: {character.knowledge}")
        print()
        input("Press Enter to continue...")
        
    def display_inventory(self, inventory):
        """Display the player's inventory."""
        self.clear_screen()
        print("=== INVENTORY ===")
        
        if not inventory:
            print("Your inventory is empty.")
        else:
            for i, item in enumerate(inventory):
                print(f"[{i+1}] {item.name} - {item.description}")
                
        print()
        input("Press Enter to continue...")
        
    def display_battle_status(self, player_party, enemy_party):
        """Display the current status of a battle."""
        self.clear_screen()
        print("=== BATTLE ===")
        
        print("YOUR PARTY:")
        for character in player_party:
            health_percentage = character.current_health / character.max_health
            health_bar = "█" * int(20 * health_percentage)
            print(f"{character.name}: {health_bar} {character.current_health}/{character.max_health}")
            
        print("\nENEMIES:")
        for enemy in enemy_party:
            health_percentage = enemy.current_health / enemy.max_health
            health_bar = "█" * int(20 * health_percentage)
            print(f"{enemy.name}: {health_bar} {enemy.current_health}/{enemy.max_health}")
            
        print()
        
    def display_shop_menu(self, shop_name, items):
        """Display a shop interface with items for sale."""
        self.clear_screen()
        print(f"=== {shop_name} ===")
        
        for i, item in enumerate(items):
            print(f"[{i+1}] {item.name} - {item.price} credits - {item.description}")
            
        print(f"[0] Exit shop")
        print()
        
    def display_dialogue(self, speaker, text, portrait=None):
        """Display a dialogue with a character."""
        print(f"\n{speaker}: ", end="")
        
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.02)
        print()
        
    def display_quest_log(self, quests):
        """Display the player's quest log."""
        self.clear_screen()
        print("=== QUEST LOG ===")
        
        active_quests = [q for q in quests if q.status == "active"]
        completed_quests = [q for q in quests if q.status == "completed"]
        
        if active_quests:
            print("\nACTIVE QUESTS:")
            for quest in active_quests:
                print(f"- {quest.name}: {quest.description}")
                
        if completed_quests:
            print("\nCOMPLETED QUESTS:")
            for quest in completed_quests:
                print(f"- {quest.name}")
                
        if not quests:
            print("No active quests.")
            
        print()
        input("Press Enter to continue...") 