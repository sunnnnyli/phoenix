"""
Main story data file that imports and combines all neural fragments.
"""
from .neural_fragments.genesis_fragment import genesis_nodes
from .neural_fragments.synthetix_fragment import synthetix_nodes
from .neural_fragments.nautilus_fragment import nautilus_nodes
from .neural_fragments.phoenix_fragment import phoenix_nodes
from .neural_fragments.prometheus_fragment import prometheus_nodes
from .neural_fragments.emergence_fragment import emergence_nodes

# Create a dictionary of all story nodes
story_nodes = {}

# Merge all neural fragment dictionaries
story_nodes.update(genesis_nodes)
story_nodes.update(synthetix_nodes)
story_nodes.update(nautilus_nodes)
story_nodes.update(phoenix_nodes)
story_nodes.update(prometheus_nodes)
story_nodes.update(emergence_nodes)

def get_story_node(node_id):
    """Get a story node by ID."""
    return story_nodes.get(node_id)