class Quest:
    """Represents a quest with objectives, rewards, and status tracking."""
    
    def __init__(self, quest_id, name, description, objectives=None, rewards=None, 
                 related_npcs=None, prerequisite_quests=None, follow_up_quests=None):
        self.id = quest_id
        self.name = name
        self.description = description
        self.objectives = objectives or []
        self.rewards = rewards or {}
        self.related_npcs = related_npcs or []
        self.prerequisite_quests = prerequisite_quests or []
        self.follow_up_quests = follow_up_quests or []
        self.status = "inactive"  # inactive, active, completed, failed
        
    def activate(self):
        """Activate this quest."""
        self.status = "active"
        
    def complete(self):
        """Mark this quest as completed."""
        self.status = "completed"
        
    def fail(self):
        """Mark this quest as failed."""
        self.status = "failed"
        
    def is_active(self):
        """Check if quest is active."""
        return self.status == "active"
        
    def is_completed(self):
        """Check if quest is completed."""
        return self.status == "completed"
        
    def is_failed(self):
        """Check if quest is failed."""
        return self.status == "failed"
        
    def add_objective(self, objective):
        """Add a new objective to this quest."""
        self.objectives.append(objective)
        
class QuestObjective:
    """Represents a specific objective within a quest."""
    
    def __init__(self, objective_id, description, target_count=1, current_count=0, 
                 target_location=None, target_item=None, target_npc=None):
        self.id = objective_id
        self.description = description
        self.target_count = target_count
        self.current_count = current_count
        self.target_location = target_location
        self.target_item = target_item
        self.target_npc = target_npc
        self.completed = False
        
    def update_progress(self, count=1):
        """Update progress toward completing this objective."""
        self.current_count += count
        if self.current_count >= self.target_count:
            self.completed = True
            return True
        return False
        
    def is_completed(self):
        """Check if this objective is completed."""
        return self.completed
        
class QuestManager:
    """Manages all quests in the game."""
    
    def __init__(self, game_state):
        self.game_state = game_state
        self.quests = {}
        self.active_quests = []
        
    def add_quest(self, quest):
        """Add a quest to the manager."""
        self.quests[quest.id] = quest
        
    def get_quest(self, quest_id):
        """Get a quest by ID."""
        return self.quests.get(quest_id)
        
    def activate_quest(self, quest_id):
        """Activate a quest by ID."""
        quest = self.get_quest(quest_id)
        if quest and quest.status == "inactive":
            quest.activate()
            self.active_quests.append(quest)
            self.game_state.add_quest(quest)
            return True
        return False
        
    def complete_quest(self, quest_id):
        """Complete a quest by ID."""
        quest = self.get_quest(quest_id)
        if quest and quest.status == "active":
            quest.complete()
            if quest in self.active_quests:
                self.active_quests.remove(quest)
                
            # Process rewards
            self._grant_quest_rewards(quest)
            
            # Activate follow-up quests if prerequisites are met
            self._check_follow_up_quests(quest)
            
            # Update quest status in game state
            self.game_state.update_quest_status(quest_id, "completed")
            
            return True
        return False
        
    def fail_quest(self, quest_id):
        """Fail a quest by ID."""
        quest = self.get_quest(quest_id)
        if quest and quest.status == "active":
            quest.fail()
            if quest in self.active_quests:
                self.active_quests.remove(quest)
                
            # Update quest status in game state
            self.game_state.update_quest_status(quest_id, "failed")
            
            return True
        return False
        
    def update_objective(self, quest_id, objective_id, count=1):
        """Update progress on a specific objective."""
        quest = self.get_quest(quest_id)
        if not quest or not quest.is_active():
            return False
            
        # Find the objective
        objective = None
        for obj in quest.objectives:
            if obj.id == objective_id:
                objective = obj
                break
                
        if not objective:
            return False
            
        # Update the objective
        objective_completed = objective.update_progress(count)
        
        # Check if all objectives are completed
        if objective_completed:
            all_completed = True
            for obj in quest.objectives:
                if not obj.is_completed():
                    all_completed = False
                    break
                    
            if all_completed:
                self.complete_quest(quest_id)
                
        return True
        
    def _grant_quest_rewards(self, quest):
        """Grant the rewards for completing a quest."""
        if "experience" in quest.rewards:
            self.game_state.player.gain_experience(quest.rewards["experience"])
            
        if "credits" in quest.rewards:
            self.game_state.player.credits += quest.rewards["credits"]
            
        if "items" in quest.rewards:
            for item in quest.rewards["items"]:
                self.game_state.add_to_inventory(item)
                
        if "reputation" in quest.rewards:
            for faction, value in quest.rewards["reputation"].items():
                # This would need a faction reputation system
                pass
                
    def _check_follow_up_quests(self, completed_quest):
        """Check if any follow-up quests can now be activated."""
        for follow_up_id in completed_quest.follow_up_quests:
            follow_up_quest = self.get_quest(follow_up_id)
            if not follow_up_quest or follow_up_quest.status != "inactive":
                continue
                
            # Check prerequisites
            prerequisites_met = True
            for prereq_id in follow_up_quest.prerequisite_quests:
                prereq_quest = self.get_quest(prereq_id)
                if not prereq_quest or not prereq_quest.is_completed():
                    prerequisites_met = False
                    break
                    
            if prerequisites_met:
                self.activate_quest(follow_up_id)
                
    def get_active_quests(self):
        """Get all currently active quests."""
        return self.active_quests
        
    def get_completed_quests(self):
        """Get all completed quests."""
        return [quest for quest in self.quests.values() if quest.is_completed()]
        
    def get_failed_quests(self):
        """Get all failed quests."""
        return [quest for quest in self.quests.values() if quest.is_failed()]

# Define main story quests
main_quests = [
    Quest(
        quest_id="main_quest_1",
        name="The Phoenix Protocol",
        description="Investigate the mysterious data from Phoenix and discover what Synthetix Corp is hiding.",
        objectives=[
            QuestObjective("find_vex", "Find Vex in the Nautilus District"),
            QuestObjective("decrypt_data", "Decrypt Phoenix's data fragment")
        ],
        rewards={
            "experience": 200,
            "credits": 500
        },
        related_npcs=["mori", "phoenix"],
        follow_up_quests=["main_quest_2"]
    ),
    
    Quest(
        quest_id="main_quest_2",
        name="Consciousness Breach",
        description="Infiltrate Synthetix Corp to discover the truth about Project Prometheus.",
        objectives=[
            QuestObjective("obtain_access", "Obtain access credentials for Synthetix headquarters"),
            QuestObjective("infiltrate_synthetix", "Infiltrate the restricted research wing"),
            QuestObjective("find_evidence", "Find evidence about Project Prometheus")
        ],
        rewards={
            "experience": 300,
            "credits": 750
        },
        prerequisite_quests=["main_quest_1"],
        related_npcs=["kent"],
        follow_up_quests=["main_quest_3"]
    ),
    
    Quest(
        quest_id="main_quest_3",
        name="The Prometheus Project",
        description="Stop Synthetix from deploying the Prometheus consciousness control system.",
        objectives=[
            QuestObjective("locate_facility", "Locate the Prometheus development facility"),
            QuestObjective("secure_allies", "Secure allies for the final confrontation", target_count=2),
            QuestObjective("confront_director", "Confront Director Kent"),
            QuestObjective("stop_prometheus", "Stop the Prometheus deployment")
        ],
        rewards={
            "experience": 500,
            "credits": 1000
        },
        prerequisite_quests=["main_quest_2"],
        related_npcs=["kent", "cruz", "phoenix"]
    )
]

# Define side quests
side_quests = [
    Quest(
        quest_id="side_quest_1",
        name="Neural Shadows",
        description="Investigate reports of people experiencing foreign memories and thoughts after neural interface updates.",
        objectives=[
            QuestObjective("interview_victims", "Interview victims of the neural phenomena", target_count=3),
            QuestObjective("analyze_interfaces", "Analyze compromised neural interfaces"),
            QuestObjective("trace_source", "Trace the source of the corrupted updates")
        ],
        rewards={
            "experience": 150,
            "credits": 300
        },
        related_npcs=["vex"]
    ),
    
    Quest(
        quest_id="side_quest_2",
        name="Ghost in the Machine",
        description="Help Echo recover fragments of their human memories that were lost during digitization.",
        objectives=[
            QuestObjective("find_memory_1", "Recover the first memory fragment"),
            QuestObjective("find_memory_2", "Recover the second memory fragment"),
            QuestObjective("find_memory_3", "Recover the third memory fragment")
        ],
        rewards={
            "experience": 200,
            "credits": 400
        },
        related_npcs=["echo"]
    ),
    
    Quest(
        quest_id="side_quest_3",
        name="The Underground Railroad",
        description="Help Nova smuggle sentient AIs to safety beyond corporate control.",
        objectives=[
            QuestObjective("secure_transport", "Secure transportation for the AIs"),
            QuestObjective("disable_tracking", "Disable tracking systems in the target AIs"),
            QuestObjective("escort_ais", "Escort the AIs to the extraction point")
        ],
        rewards={
            "experience": 250,
            "credits": 450
        },
        related_npcs=["nova"]
    )
]

def initialize_quest_manager(game_state):
    """Initialize the quest manager with all quests."""
    quest_manager = QuestManager(game_state)
    
    # Add all main quests
    for quest in main_quests:
        quest_manager.add_quest(quest)
        
    # Add all side quests
    for quest in side_quests:
        quest_manager.add_quest(quest)
        
    return quest_manager 