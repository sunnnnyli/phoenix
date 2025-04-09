class Choice:
    """Represents a choice option in a story node."""
    
    def __init__(self, text, next_node, conditions=None, flags=None, relationship_changes=None):
        self.text = text  # The text displayed for this choice
        self.next_node = next_node  # ID of the next story node
        self.conditions = conditions or {}  # Requirements to see this choice
        self.flags = flags or {}  # Story flags set when this choice is selected
        self.relationship_changes = relationship_changes or {}  # Changes to relationships
        
class StoryNode:
    """Represents a single node in the story narrative."""
    
    def __init__(self, node_id, text, choices=None, node_type="narrative", 
                 battle_data=None, shop_data=None, dialogue_data=None):
        self.id = node_id  # Unique identifier for this node
        self.text = text  # Narrative text for this node
        self.choices = choices or []  # Available choices
        self.node_type = node_type  # Type of node (narrative, battle, shop, dialogue)
        self.battle_data = battle_data  # Data for battle encounters
        self.shop_data = shop_data  # Data for shop interactions
        self.dialogue_data = dialogue_data  # Data for dialogue sequences
        
    def add_choice(self, text, next_node, conditions=None, flags=None, relationship_changes=None):
        """Add a choice to this story node."""
        choice = Choice(text, next_node, conditions, flags, relationship_changes)
        self.choices.append(choice)
        return self 