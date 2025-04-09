import random
import time

class BattleSystem:
    """Handles the battle mechanics for the game."""
    
    def __init__(self, game_state, ui):
        self.game_state = game_state
        self.ui = ui
        self.player_party = []
        self.enemy_party = []
        self.turn_order = []
        self.current_turn_index = 0
        self.battle_log = []
        self.round_number = 0
        self.battle_result = None
        self.battle_rewards = {
            "experience": 0,
            "items": [],
            "credits": 0
        }
        
    def initialize_battle(self, enemies, battle_type="normal"):
        """Set up a battle with enemies."""
        self.game_state.battle_in_progress = True
        self.battle_result = None
        self.battle_log = []
        self.round_number = 0
        
        # Set up player party (player + active companions)
        self.player_party = [self.game_state.player]
        self.player_party.extend(self.game_state.companions)
        
        # Set up enemy party
        self.enemy_party = enemies
        
        # Calculate total possible rewards
        self.battle_rewards = {
            "experience": sum(enemy.experience_reward for enemy in enemies),
            "items": [],
            "credits": random.randint(10, 30) * len(enemies)
        }
        
        # Determine turn order based on initiative
        self._calculate_turn_order()
        
        # Show battle start message
        enemy_names = ", ".join(enemy.name for enemy in enemies)
        self.ui.display_message(f"Battle started! Opponents: {enemy_names}")
        self.ui.display_battle_status(self.player_party, self.enemy_party)
        
    def _calculate_turn_order(self):
        """Determine the order of turns based on initiative/speed."""
        all_combatants = []
        
        # Add player party with their initiative values
        for character in self.player_party:
            all_combatants.append({"combatant": character, "initiative": character.initiative, "is_player_party": True})
            
        # Add enemy party with their speed values
        for enemy in self.enemy_party:
            all_combatants.append({"combatant": enemy, "initiative": enemy.speed, "is_player_party": False})
            
        # Sort by initiative (higher goes first)
        all_combatants.sort(key=lambda x: x["initiative"], reverse=True)
        
        # Create the turn order
        self.turn_order = all_combatants
        self.current_turn_index = 0
        
    def process_turn(self):
        """Process a single turn in the battle."""
        if self.battle_result is not None:
            return self.battle_result
            
        # Get current actor
        current_actor = self.turn_order[self.current_turn_index]
        is_player_party = current_actor["is_player_party"]
        combatant = current_actor["combatant"]
        
        # Skip if combatant is defeated
        if hasattr(combatant, "is_defeated") and combatant.is_defeated():
            self._advance_turn()
            return None
            
        if hasattr(combatant, "current_health") and combatant.current_health <= 0:
            self._advance_turn()
            return None
            
        # Handle AI or player turn
        if is_player_party:
            if combatant == self.game_state.player:
                self._handle_player_turn()
            else:
                self._handle_companion_turn(combatant)
        else:
            self._handle_enemy_turn(combatant)
            
        # Check battle end conditions
        self._check_battle_end()
        
        # Move to next turn
        self._advance_turn()
        
        return self.battle_result
        
    def _handle_player_turn(self):
        """Process the player's turn."""
        self.ui.display_message(f"{self.game_state.player.name}'s turn!")
        
        # Check if enemies remain
        if not any(enemy.current_health > 0 for enemy in self.enemy_party):
            return
            
        # Display battle status
        self.ui.display_battle_status(self.player_party, self.enemy_party)
        
        # Create action options
        options = ["Attack", "Use Ability", "Use Item", "Defend"]
        
        choice = self.ui.get_choice("Choose your action:", options)
        
        if choice == 0:  # Attack
            self._handle_attack(self.game_state.player, is_player=True)
        elif choice == 1:  # Use Ability
            self._handle_ability(self.game_state.player, is_player=True)
        elif choice == 2:  # Use Item
            self._handle_item(self.game_state.player)
        elif choice == 3:  # Defend
            self._handle_defend(self.game_state.player)
            
    def _handle_companion_turn(self, companion):
        """Process a companion's turn."""
        self.ui.display_message(f"{companion.name}'s turn!")
        
        # Simple AI for companions - prioritize abilities if low health, otherwise attack
        if companion.current_health < companion.max_health * 0.3 and companion.abilities:
            healing_abilities = [ability for ability in companion.abilities if "heal" in ability["name"].lower() or "treatment" in ability["name"].lower()]
            if healing_abilities and companion.current_energy >= healing_abilities[0]["energy_cost"]:
                # Use healing ability on self
                ability = healing_abilities[0]
                heal_amount = random.randint(15, 25) + companion.medicine * 2
                companion.heal(heal_amount)
                companion.use_energy(ability["energy_cost"])
                self.ui.display_message(f"{companion.name} uses {ability['name']} and recovers {heal_amount} health!")
                return
                
        # Attack by default
        self._handle_attack(companion, is_player=True)
        
    def _handle_enemy_turn(self, enemy):
        """Process an enemy's turn."""
        self.ui.display_message(f"{enemy.name}'s turn!")
        
        # Simple enemy AI
        # Target selection - prefer player if health is low
        if self.game_state.player.current_health < self.game_state.player.max_health * 0.3:
            target = self.game_state.player
        else:
            # Otherwise, randomly select from player party
            valid_targets = [character for character in self.player_party if character.current_health > 0]
            if not valid_targets:
                return
            target = random.choice(valid_targets)
            
        # Determine attack damage
        base_damage = enemy.attack + random.randint(1, 6)
        damage_dealt = target.take_damage(base_damage)
        
        self.ui.display_message(f"{enemy.name} attacks {target.name} for {damage_dealt} damage!")
        
        # If target is defeated
        if target.current_health <= 0:
            self.ui.display_message(f"{target.name} has been defeated!")
            
    def _handle_attack(self, attacker, is_player=False):
        """Handle a basic attack action."""
        # Select target
        if is_player:
            # Player selects an enemy target
            valid_targets = [enemy for enemy in self.enemy_party if enemy.current_health > 0]
            if not valid_targets:
                return
                
            if len(valid_targets) == 1:
                target = valid_targets[0]
            else:
                target_options = [f"{enemy.name} (HP: {enemy.current_health}/{enemy.max_health})" for enemy in valid_targets]
                choice = self.ui.get_choice("Select a target:", target_options)
                target = valid_targets[choice]
        else:
            # Enemy selects a player party target
            valid_targets = [character for character in self.player_party if character.current_health > 0]
            if not valid_targets:
                return
                
            target = random.choice(valid_targets)
            
        # Calculate damage
        base_damage = attacker.attack_power + random.randint(1, 8)
        damage_dealt = target.take_damage(base_damage)
        
        self.ui.display_message(f"{attacker.name} attacks {target.name} for {damage_dealt} damage!")
        
        # Check if target is defeated
        if target.current_health <= 0:
            self.ui.display_message(f"{target.name} has been defeated!")
            
    def _handle_ability(self, user, is_player=False):
        """Handle using an ability."""
        if not user.abilities:
            self.ui.display_message(f"{user.name} has no abilities available!")
            return
            
        # Display available abilities
        ability_options = [f"{ability['name']} - {ability['description']} (Energy: {ability['energy_cost']})" for ability in user.abilities]
        
        if is_player:
            ability_options.append("Cancel")
            choice = self.ui.get_choice("Select an ability to use:", ability_options)
            
            if choice == len(user.abilities):  # Cancel option
                return self._handle_player_turn()
                
            ability = user.abilities[choice]
        else:
            # AI selects ability
            ability = random.choice(user.abilities)
            
        # Check if enough energy
        if not user.use_energy(ability["energy_cost"]):
            self.ui.display_message(f"Not enough energy to use {ability['name']}!")
            if is_player:
                return self._handle_player_turn()
            return
            
        # Implement ability effects based on name/description
        if "System Hack" in ability["name"]:
            # Temporarily reduce enemy defense
            target = self._select_target(is_player)
            if target:
                target.defense = max(0, target.defense - 2)
                self.ui.display_message(f"{user.name} uses {ability['name']} and weakens {target.name}'s defenses!")
                
        elif "Tactical Strike" in ability["name"]:
            # Deal high damage to single target
            target = self._select_target(is_player)
            if target:
                damage = user.attack_power * 2 + random.randint(5, 10)
                damage_dealt = target.take_damage(damage)
                self.ui.display_message(f"{user.name} uses {ability['name']} and deals {damage_dealt} damage to {target.name}!")
                
        elif "Emergency Treatment" in ability["name"]:
            # Heal self or ally
            if is_player:
                heal_targets = [char for char in self.player_party if char.current_health > 0]
                target_options = [f"{char.name} (HP: {char.current_health}/{char.max_health})" for char in heal_targets]
                choice = self.ui.get_choice("Select who to heal:", target_options)
                target = heal_targets[choice]
            else:
                # AI selects most damaged ally
                heal_targets = [char for char in self.player_party if char.current_health > 0]
                target = min(heal_targets, key=lambda x: x.current_health / x.max_health)
                
            heal_amount = user.medicine * 3 + random.randint(15, 25)
            actual_heal = target.heal(heal_amount)
            self.ui.display_message(f"{user.name} uses {ability['name']} and heals {target.name} for {actual_heal} health!")
            
        else:
            # Generic effect for other abilities
            self.ui.display_message(f"{user.name} uses {ability['name']}!")
            
    def _handle_item(self, user):
        """Handle using an item."""
        items = self.game_state.inventory
        if not items:
            self.ui.display_message("You have no items to use!")
            return self._handle_player_turn()
            
        # Filter to usable items
        usable_items = [item for item in items if hasattr(item, "use_effect")]
        
        if not usable_items:
            self.ui.display_message("You have no usable items!")
            return self._handle_player_turn()
            
        # Display available items
        item_options = [f"{item.name} - {item.description}" for item in usable_items]
        item_options.append("Cancel")
        
        choice = self.ui.get_choice("Select an item to use:", item_options)
        
        if choice == len(usable_items):  # Cancel
            return self._handle_player_turn()
            
        selected_item = usable_items[choice]
        
        # Use the item (implementation would depend on item class)
        # This is a placeholder
        self.ui.display_message(f"{user.name} uses {selected_item.name}!")
        
        # Remove the used item
        self.game_state.remove_from_inventory(selected_item)
        
    def _handle_defend(self, character):
        """Handle defend action to reduce damage until next turn."""
        # Implement temporary defense bonus
        character.defending = True
        self.ui.display_message(f"{character.name} takes a defensive stance.")
        
    def _select_target(self, is_player):
        """Helper method to select a target."""
        if is_player:
            valid_targets = [enemy for enemy in self.enemy_party if enemy.current_health > 0]
            if not valid_targets:
                return None
                
            if len(valid_targets) == 1:
                return valid_targets[0]
                
            target_options = [f"{enemy.name} (HP: {enemy.current_health}/{enemy.max_health})" for enemy in valid_targets]
            choice = self.ui.get_choice("Select a target:", target_options)
            return valid_targets[choice]
        else:
            valid_targets = [character for character in self.player_party if character.current_health > 0]
            if not valid_targets:
                return None
                
            return random.choice(valid_targets)
            
    def _advance_turn(self):
        """Move to the next turn in the battle."""
        self.current_turn_index = (self.current_turn_index + 1) % len(self.turn_order)
        
        # If we've gone through all turns, increment round number
        if self.current_turn_index == 0:
            self.round_number += 1
            
    def _check_battle_end(self):
        """Check if the battle has ended."""
        # Check if all enemies are defeated
        if all(enemy.current_health <= 0 for enemy in self.enemy_party):
            self.battle_result = "victory"
            self._handle_victory()
            return True
            
        # Check if player party is defeated
        if all(character.current_health <= 0 for character in self.player_party):
            self.battle_result = "defeat"
            self._handle_defeat()
            return True
            
        return False
        
    def _handle_victory(self):
        """Process victory results."""
        self.ui.display_message("Victory! All enemies have been defeated.")
        
        # Collect loot from enemies
        for enemy in self.enemy_party:
            loot = enemy.get_loot()
            self.battle_rewards["items"].extend(loot)
            
        # Display rewards
        self.ui.display_message(f"Experience gained: {self.battle_rewards['experience']}")
        
        if self.battle_rewards["items"]:
            item_names = ", ".join(item.name for item in self.battle_rewards["items"])
            self.ui.display_message(f"Items found: {item_names}")
            
        self.ui.display_message(f"Credits found: {self.battle_rewards['credits']}")
        
        # Add rewards to player
        self.game_state.player.gain_experience(self.battle_rewards["experience"])
        
        for item in self.battle_rewards["items"]:
            self.game_state.add_to_inventory(item)
            
        # End battle
        self.game_state.battle_in_progress = False
        
    def _handle_defeat(self):
        """Process defeat results."""
        self.ui.display_message("Defeat! Your party has been defeated.")
        
        # Implement consequences of defeat
        # This could be game over, respawn at a checkpoint, etc.
        self.game_state.battle_in_progress = False
        
    def end_battle(self):
        """Clean up after battle ends."""
        self.player_party = []
        self.enemy_party = []
        self.turn_order = []
        self.battle_log = []
        
        # Reset defending status on characters
        if hasattr(self.game_state.player, "defending"):
            self.game_state.player.defending = False
            
        for companion in self.game_state.companions:
            if hasattr(companion, "defending"):
                companion.defending = False 