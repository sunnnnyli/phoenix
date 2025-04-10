"""
Neural Fragment Loader - Utility functions for managing story neural fragments.
"""
import importlib
import os
import inspect
from core.story_node import StoryNode

class FragmentLoader:
    """Helper class for managing neural fragments in the story."""
    
    def __init__(self, fragments_package="story.neural_fragments"):
        """Initialize the fragment loader with the package containing neural fragments."""
        self.fragments_package = fragments_package
        self.fragments = {}
        self.story_nodes = {}
        
    def discover_fragments(self):
        """Automatically discover all neural fragment modules in the package."""
        package = importlib.import_module(self.fragments_package)
        package_dir = os.path.dirname(inspect.getfile(package))
        
        # Find all Python files in the package
        for filename in os.listdir(package_dir):
            if filename.endswith("_fragment.py") and not filename.startswith("__"):
                fragment_name = filename[:-3]  # Remove .py extension
                self.fragments[fragment_name] = f"{self.fragments_package}.{fragment_name}"
                
        return self.fragments
        
    def load_fragment(self, fragment_name):
        """Load a specific neural fragment by name."""
        if fragment_name in self.fragments:
            module = importlib.import_module(self.fragments[fragment_name])
            
            # Each neural fragment should have a dictionary named after the fragment
            # Example: genesis_fragment.py would have genesis_nodes dictionary
            nodes_dict_name = f"{fragment_name.split('_')[0]}_nodes"
            
            if hasattr(module, nodes_dict_name):
                nodes = getattr(module, nodes_dict_name)
                return nodes
                
        return {}
        
    def load_all_fragments(self):
        """Load all discovered neural fragments and merge their nodes."""
        self.discover_fragments()
        
        for fragment_name in self.fragments:
            nodes = self.load_fragment(fragment_name)
            self.story_nodes.update(nodes)
            
        return self.story_nodes
        
    def get_node_by_id(self, node_id):
        """Get a story node by its ID."""
        return self.story_nodes.get(node_id)
        
    def get_fragment_for_node(self, node_id):
        """Find which neural fragment contains a specific node."""
        for fragment_name in self.fragments:
            nodes = self.load_fragment(fragment_name)
            if node_id in nodes:
                return fragment_name
                
        return None
        
    def add_node_to_fragment(self, fragment_name, node_id, node):
        """Add a new story node to a specific neural fragment."""
        if not fragment_name.endswith("_fragment"):
            fragment_name = f"{fragment_name}_fragment"
            
        if fragment_name not in self.fragments:
            # Fragment doesn't exist yet
            return False
            
        # Import the module
        module_name = self.fragments[fragment_name]
        module = importlib.import_module(module_name)
        
        # Get the nodes dictionary
        nodes_dict_name = f"{fragment_name.split('_')[0]}_nodes"
        if hasattr(module, nodes_dict_name):
            nodes = getattr(module, nodes_dict_name)
            
            # Add the node
            nodes[node_id] = node
            
            # Update our local copy
            self.story_nodes[node_id] = node
            
            return True
            
        return False

# Usage example:
# loader = FragmentLoader()
# all_nodes = loader.load_all_fragments()
# intro_node = loader.get_node_by_id("intro")
# fragment = loader.get_fragment_for_node("tech_scan")  # Returns "nautilus_fragment"