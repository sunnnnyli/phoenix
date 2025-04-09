from shop import Shop
from items.item_database import get_item

class Location:
    """Represents a location in the game world."""
    
    def __init__(self, location_id, name, description, available_exits=None, 
                 shop=None, enemies=None, npcs=None, story_nodes=None):
        self.id = location_id
        self.name = name
        self.description = description
        self.available_exits = available_exits or {}  # Dict of {direction: location_id}
        self.shop = shop
        self.enemies = enemies or []
        self.npcs = npcs or []
        self.story_nodes = story_nodes or []  # Story nodes that can trigger at this location
        self.visited = False
        
    def enter(self, game_state):
        """Process entry into this location."""
        game_state.current_location = self
        
        if not self.visited:
            # First-time visit
            self.visited = True
            return self.get_first_visit_text()
        else:
            # Returning to location
            return self.get_return_visit_text()
            
    def get_first_visit_text(self):
        """Get text for first visit to this location."""
        return f"You arrive at {self.name}.\n\n{self.description}"
        
    def get_return_visit_text(self):
        """Get text for returning to this location."""
        return f"You return to {self.name}."
        
    def get_exits_text(self):
        """Get text describing available exits."""
        if not self.available_exits:
            return "There are no obvious exits."
            
        exits_text = "Available exits: "
        exits_list = [f"{direction} to {exit_id}" for direction, exit_id in self.available_exits.items()]
        return exits_text + ", ".join(exits_list)
        
    def has_shop(self):
        """Check if this location has a shop."""
        return self.shop is not None
        
    def has_enemies(self):
        """Check if this location has enemies."""
        return len(self.enemies) > 0
        
    def has_npcs(self):
        """Check if this location has NPCs."""
        return len(self.npcs) > 0
        
# Create a dictionary of all locations in the game
locations = {}

# --- NEW MERIDIAN: PLAYER'S APARTMENT ---
locations["apartment"] = Location(
    location_id="apartment",
    name="Your Apartment",
    description=(
        "Your small apartment in the mid-levels of New Meridian's Eastern Residential Zone. "
        "The walls are lined with neural interface equipment and technical manuals. "
        "A window overlooks the gleaming spires of the city center, where Synthetix Corp's headquarters dominates the skyline."
    ),
    available_exits={
        "outside": "eastern_residential"
    }
)

# --- NEW MERIDIAN: EASTERN RESIDENTIAL ZONE ---
locations["eastern_residential"] = Location(
    location_id="eastern_residential",
    name="Eastern Residential Zone",
    description=(
        "The bustling residential district where middle-tier corporate employees and contractors live. "
        "Holographic advertisements shimmer on building facades, while security drones occasionally pass overhead. "
        "The streets are clean but crowded with commuters heading to various parts of the city."
    ),
    available_exits={
        "north": "university_district",
        "west": "central_plaza",
        "east": "nautilus_district",
        "apartment": "apartment"
    }
)

# --- NEW MERIDIAN: UNIVERSITY DISTRICT ---
locations["university_district"] = Location(
    location_id="university_district",
    name="University District",
    description=(
        "The academic heart of New Meridian, home to the prestigious Institute of Technology and Consciousness Studies. "
        "Students and professors hurry between neo-classical buildings and ultra-modern research facilities. "
        "The area has a youthful energy, with cafes and bookshops lining the tree-lined boulevards - a rarity in this concrete metropolis."
    ),
    available_exits={
        "south": "eastern_residential",
        "west": "government_sector",
        "east": "research_park",
        "nexus": "nexus_coffee"
    }
)

# --- NEW MERIDIAN: NEXUS COFFEE ---
locations["nexus_coffee"] = Location(
    location_id="nexus_coffee",
    name="Nexus Coffee",
    description=(
        "A popular café frequented by students and researchers from the nearby Institute. "
        "The interior features comfortable seating and privacy booths with sound dampening fields. "
        "The café is known for its organic coffee and discreet meeting spaces away from corporate surveillance."
    ),
    available_exits={
        "outside": "university_district"
    }
)

# --- NEW MERIDIAN: CENTRAL PLAZA ---
locations["central_plaza"] = Location(
    location_id="central_plaza",
    name="Central Plaza",
    description=(
        "The bustling heart of New Meridian, where corporate headquarters and government buildings surround a massive circular plaza. "
        "A towering holographic monument at the center commemorates the 'AI Accord of 2142' that established rules for artificial consciousness development. "
        "Security is tight here, with both human officers and automated systems monitoring all activity."
    ),
    available_exits={
        "north": "government_sector",
        "east": "eastern_residential",
        "south": "commercial_district",
        "west": "western_residential",
        "synthetix": "synthetix_plaza"
    }
)

# --- NEW MERIDIAN: SYNTHETIX PLAZA ---
locations["synthetix_plaza"] = Location(
    location_id="synthetix_plaza",
    name="Synthetix Corporate Plaza",
    description=(
        "The gleaming public entrance to Synthetix Corporation's headquarters. "
        "A 200-story tower of glass and carbon nanotubes rises above a circular plaza featuring artistic water features and robotic assistants. "
        "Security checkpoints control access to the building, scanning neural signatures and corporate credentials of all visitors."
    ),
    available_exits={
        "plaza": "central_plaza",
        "lobby": "synthetix_lobby"
    }
)

# --- NEW MERIDIAN: NAUTILUS DISTRICT ---
locations["nautilus_district"] = Location(
    location_id="nautilus_district",
    name="Nautilus District",
    description=(
        "Once an industrial zone, now the home of tech specialists, hackers, and those wishing to avoid corporate oversight. "
        "Retrofitted warehouses house underground tech shops and unofficial medical clinics specializing in neural modifications. "
        "The area has a gritty, cyberpunk aesthetic with neon signs and repurposed machinery lining the narrow streets."
    ),
    available_exits={
        "west": "eastern_residential",
        "south": "maintenance_tunnels",
        "east": "city_outskirts",
        "tech_shop": "vex_shop"
    }
)

# --- NEW MERIDIAN: VEX'S TECH SHOP ---
vex_shop_inventory = [
    get_item("neural_processor"),
    get_item("firewall_mesh"),
    get_item("energy_cell"),
    get_item("cognitive_enhancer"),
    get_item("pulse_pistol")
]

vex_shop = Shop(
    shop_id="vex_shop",
    name="Vex's Neural Solutions",
    description="A cluttered but expertly organized tech shop specializing in neural interface modifications and digital security systems.",
    inventory=vex_shop_inventory,
    discount_rate=0.1  # 10% discount
)

locations["vex_shop"] = Location(
    location_id="vex_shop",
    name="Vex's Neural Solutions",
    description=(
        "A seemingly small storefront that opens into a surprisingly spacious tech workshop. "
        "Workbenches are covered with neural interface components, dismantled security systems, and custom cybernetic parts. "
        "A wall of locked cabinets likely holds more sensitive or valuable equipment. "
        "The owner, a woman with striking augmented eyes and circuitry tattoos, watches you with cautious interest."
    ),
    available_exits={
        "outside": "nautilus_district"
    },
    shop=vex_shop
)

# --- More locations can be added as the game expands ---

def get_location(location_id):
    """Get a location by its ID."""
    return locations.get(location_id)
    
def get_all_locations():
    """Get all locations."""
    return locations.values() 