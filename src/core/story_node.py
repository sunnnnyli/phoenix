class StoryNode:
    """Represents a single node in the story narrative."""
    
    def __init__(self, node_id, text, choices=None, node_type="narrative", 
                 on_enter=None, on_exit=None, data=None):
        self.id = node_id  # Unique identifier for this node
        self.text = text  # Narrative text for this node
        self.choices = choices or []  # Available choices
        self.node_type = node_type  # Type of node
        self.on_enter = on_enter or {}  # Actions to perform when entering node
        self.on_exit = on_exit or {}  # Actions to perform when exiting node
        self.data = data or {}  # Type-specific data (battle, shop, dialogue)
        
    def add_choice(self, text, next_node, conditions=None, actions=None):
        """Add a choice to this story node."""
        choice = Choice(text, next_node, conditions, actions)
        self.choices.append(choice)
        return self
        
    def add_enter_action(self, action_type, action_data):
        """Add an action to perform when entering this node."""
        self.on_enter[action_type] = action_data
        
    def add_exit_action(self, action_type, action_data):
        """Add an action to perform when exiting this node."""
        self.on_exit[action_type] = action_data


class Choice:
    """Represents a choice option in a story node."""
    
    def __init__(self, text, next_node, conditions=None, actions=None):
        self.text = text  # The text displayed for this choice
        self.next_node = next_node  # ID of the next story node
        self.conditions = conditions or {}  # Requirements to see this choice
        self.actions = actions or {}  # Actions to perform when this choice is selected
        